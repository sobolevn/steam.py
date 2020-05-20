# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2020 James

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import abc
import json
import re
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

import aiohttp

from .enums import *
from .errors import HTTPException
from .game import Game
from .iterators import CommentsIterator
from .models import URL, Ban, UserBadges
from .trade import Inventory

if TYPE_CHECKING:
    from .user import User
    from .group import Group
    from .image import Image

__all__ = (
    'SteamID',
    'make_steam64'
)

ETypeChars = ''.join([type_char.name for type_char in ETypeChar])

_ICODE_HEX = "0123456789abcdef"
_ICODE_CUSTOM = "bcdfghjkmnpqrtvw"
_ICODE_VALID = f'{_ICODE_HEX}{_ICODE_CUSTOM}'
_ICODE_MAPPING = dict(zip(_ICODE_HEX, _ICODE_CUSTOM))
_ICODE_INVERSE_MAPPING = dict(zip(_ICODE_CUSTOM, _ICODE_HEX))


class SteamID(int, metaclass=abc.ABCMeta):
    """Convert a Steam ID between its various representations."""

    def __new__(cls, *args, **kwargs):
        user_id64 = make_steam64(*args, **kwargs)
        return super().__new__(cls, user_id64)

    def __repr__(self):
        attrs = (
            'id', 'type', 'universe', 'instance'
        )
        resolved = [f'{attr}={repr(getattr(self, attr))}' for attr in attrs]
        return f"<SteamID {' '.join(resolved)}>"

    @property
    def id(self) -> int:
        """:class:`int`: Represents the account id.
        This is also known as the 32 bit id.
        """
        return int(self) & 0xFFffFFff

    @property
    def instance(self) -> int:
        """:class:`int`: Returns the instance of the account."""
        return (int(self) >> 32) & 0xFFffF

    @property
    def type(self) -> EType:
        """:class:`~steam.EType`: Represents the Steam type of the account."""
        return EType((int(self) >> 52) & 0xF)

    @property
    def universe(self) -> EUniverse:
        """:class:`~steam.EUniverse`: Represents the Steam universe of the account."""
        return EUniverse((int(self) >> 56) & 0xFF)

    @property
    def as_32(self) -> int:
        """:class:`int`: The account's id.
        An alias to :attr:`SteamID.id`.
        """
        return self.id

    @property
    def id64(self) -> int:
        """:class:`int`: The steam 64 bit id of the account.
        Used for community profiles along with other useful things.
        """
        return int(self)

    @property
    def as_64(self) -> int:
        """:class:`int`: The steam 64 bit id of the account.
        An alias to :attr:`SteamID.id64`.
        """
        return self.id64

    @property
    def id2(self) -> str:
        """class:`str`: The Steam2 id of the account.
            e.g ``STEAM_1:0:1234``.

        .. note::
            ``STEAM_X:Y:Z``. The value of ``X`` should represent the universe, or ``1``
            for ``Public``. However, there was a bug in GoldSrc and Orange Box games
            and ``X`` was ``0``. If you need that format use :attr:`SteamID.as_steam2_zero`.
        """
        return f'STEAM_{int(self.universe)}:{self.id % 2}:{self.id >> 1}'

    @property
    def as_steam2(self) -> str:
        """class:`str`: The Steam2 id of the account.
            e.g ``STEAM_1:0:1234``.

        .. note::
            ``STEAM_X:Y:Z``. The value of ``X`` should represent the universe, or ``1``
            for ``Public``. However, there was a bug in GoldSrc and Orange Box games
            and ``X`` was ``0``. If you need that format use :attr:`SteamID.as_steam2_zero`.

        An alias to :attr:`SteamID.id2`.
        """
        return self.id2

    @property
    def as_steam2_zero(self) -> str:
        """:class:`str`: The Steam2 id of the account.
            e.g ``STEAM_0:0:1234``.

        For GoldSrc and Orange Box games.
        See :attr:`SteamID.as_steam2`.
        """
        return self.as_steam2.replace('_1', '_0')

    @property
    def id3(self) -> str:
        """:class:`str`: The Steam3 id of the account.
            e.g ``[U:1:1234]``.

        This is used for more recent games.
        """
        typechar = str(ETypeChar(self.type))
        instance = None

        if self.type in (EType.AnonGameServer, EType.Multiseat):
            instance = self.instance
        elif self.type == EType.Individual:
            if self.instance != 1:
                instance = self.instance
        elif self.type == EType.Chat:
            if self.instance & EInstanceFlag.Clan:
                typechar = 'c'
            elif self.instance & EInstanceFlag.Lobby:
                typechar = 'L'
            else:
                typechar = 'T'

        parts = [typechar, int(self.universe), self.id]

        if instance is not None:
            parts.append(instance)

        return f'[{":".join(map(str, parts))}]'

    @property
    def as_steam3(self) -> str:
        """:class:`str`: The Steam3 id of the account.
        An alias to :attr:`SteamID.id3`.
        """
        return self.id3

    @property
    def as_invite_code(self):
        """:class:`str`: s.team invite code format
            e.g. ``cv-dgb``
        """
        if self.type == EType.Individual and self.is_valid():
            def repl_mapper(x):
                return _ICODE_MAPPING[x.group()]

            invite_code = re.sub(f"[{_ICODE_HEX}]", repl_mapper, f"{self.id:x}")
            split_idx = len(invite_code) // 2

            if split_idx:
                invite_code = f'{invite_code[:split_idx]}-{invite_code[split_idx:]}'

            return invite_code

    @property
    def invite_url(self):
        """:class:`str`: The user's full invite code URL.
            e.g ``https://s.team/p/cv-dgb``
        """
        code = self.as_invite_code
        if code:
            return f'https://s.team/p/{code}'

    @property
    def community_url(self) -> Optional[str]:
        """Optional[:class:`str`]: The community url of the account
            e.g https://steamcommunity.com/profiles/123456789.
        """
        suffix = {
            EType.Individual: 'profiles',
            EType.Clan: 'gid',
        }
        if self.type in suffix:
            return f'https://steamcommunity.com/{suffix[self.type]}/{self.as_64}'

        return None

    def is_valid(self) -> bool:
        """:class:`bool`: Check whether this SteamID is valid.
        This doesn't however mean that a matching profile can be found.
        """
        if self.type == EType.Invalid or self.type >= EType.Max:
            return False

        if self.universe == EUniverse.Invalid or self.universe >= EUniverse.Max:
            return False

        if self.type == EType.Individual:
            if self.id == 0 or self.instance > 4:
                return False

        if self.type == EType.Clan:
            if self.id == 0 or self.instance != 0:
                return False

        if self.type == EType.GameServer:
            if self.id == 0:
                return False

        if self.type == EType.AnonGameServer:
            if self.id == 0 and self.instance == 0:
                return False

        return True

    @classmethod
    async def from_url(cls, url, timeout=30) -> Optional['SteamID']:
        """Takes Steam community url and returns a SteamID instance or ``None``.
        See :func:`steam64_from_url` for details.

        Parameters
        ----------
        url: :class:`str`
            The Steam community url.
        timeout: :class:`int`
            How long to wait for the http request before turning ``None``.

        Returns
        -------
        SteamID: Optional[:class:`SteamID`]
            `SteamID` instance or ``None``.
        """

        steam64 = await steam64_from_url(url, timeout)

        if steam64:
            return cls(steam64)
        return None


class BaseUser(SteamID, metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a Steam user.
    The following classes implement this ABC:

        - :class:`~steam.User`
        - :class:`~steam.ClientUser`

    .. container:: operations

        .. describe:: x == y

            Checks if two users are equal.

        .. describe:: x != y

            Checks if two users are not equal.

        .. describe:: str(x)

            Returns the user's name.

    Attributes
    ----------
    name: :class:`str`
        The user's username.
    state: :class:`~steam.EPersonaState`
        The current persona state of the account (e.g. LookingToTrade).
    game: Optional[:class:`~steam.Game`]
        The Game instance attached to the user. Is None if the user
        isn't in a game or one that is recognised by the api.
    avatar_url: :class:`str`
        The avatar url of the user. Uses the large (184x184 px) image url.
    real_name: Optional[:class:`str`]
        The user's real name defined by them. Could be None.
    created_at: Optional[:class:`datetime.datetime`]
        The time at which the user's account was created. Could be None.
    last_logoff: Optional[:class:`datetime.datetime`]
        The last time the user logged into steam. Could be None (e.g. if they are currently online).
    country: Optional[:class:`str`]
        The country code of the account. Could be None.
    flags: :class:`~steam.EPersonaStateFlag`
        The persona state flags of the account.
    """

    def __new__(cls, *args, **kwargs):
        data = kwargs.pop('data')
        user_id64 = make_steam64(data['steamid'])
        return super().__new__(cls, user_id64)

    def __init__(self, state, data):
        SteamID.__init__(data['steamid'])
        self._state = state
        self._update(data)

    def __repr__(self):
        attrs = (
            'name', 'state',
        )
        resolved = [f'{attr}={repr(getattr(self, attr))}' for attr in attrs]
        resolved.append(super().__repr__())
        return f"<User {' '.join(resolved)}>"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def _update(self, data):
        self._data = data
        self.name = data['personaname']
        self.real_name = data.get('realname')
        self.avatar_url = data.get('avatarfull')
        self.trade_url = f'{URL.COMMUNITY}/tradeoffer/new/?partner={self.id}'

        self.primary_group = int(data['primaryclanid']) if 'primaryclanid' in data else None
        self.country = data.get('loccountrycode')
        self.created_at = datetime.utcfromtimestamp(data['timecreated']) if 'timecreated' in data else None
        # steam is dumb I have no clue why this sometimes isn't given sometimes
        self.last_logoff = datetime.utcfromtimestamp(data['lastlogoff']) if 'lastlogoff' in data else None
        self.state = EPersonaState(data.get('personastate', 0))
        self.flags = EPersonaStateFlag(data.get('personastateflags', 0))
        self.game = Game(title=data['gameextrainfo'], app_id=int(data['gameid'])) if 'gameextrainfo' in data else None

    async def comment(self, content: str) -> None:
        """|coro|
        Post a comment to an :class:`User`'s profile.

        Parameters
        -----------
        content: :class:`str`
            The comment to add the user's profile.
        """
        await self._state.http.post_comment(self.id64, 'Profile', content)

    async def fetch_inventory(self, game: Game) -> Inventory:
        """|coro|
        Fetch an :class:`User`'s :class:`~steam.Inventory` for trading.

        Parameters
        -----------
        game: :class:`~steam.Game`
            The game to fetch the inventory for.

        Raises
        ------
        :class:`~steam.Forbidden`
            The user's inventory is private.

        Returns
        -------
        :class:`Inventory`
            The user's inventory.
        """
        resp = await self._state.http.fetch_user_inventory(self.id64, game.app_id, game.context_id)
        return Inventory(state=self._state, data=resp, owner=self)

    async def fetch_friends(self) -> List['User']:
        """|coro|
        Fetch the list of :class:`~steam.User`'s friends from the API.

        Returns
        -------
        List[:class:`~steam.User`]
            The list of :class:`~steam.User`'s friends from the API.
        """
        friends = await self._state.http.fetch_friends(self.id64)
        return [self._state._store_user(friend) for friend in friends]

    async def fetch_games(self) -> List[Game]:
        """|coro|
        Fetches the list of :class:`~steam.Game` objects from the API.

        Returns
        -------
        List[:class:`~steam.Game`]
            The list of :class:`~steam.Game` objects from the API.
        """
        data = await self._state.http.fetch_user_games(self.id64)
        games = data['response'].get('games', [])
        return [Game._from_api(game) for game in games]

    async def fetch_groups(self) -> List['Group']:
        """|coro|
        Fetches a list of the :class:`User`'s :class:`~steam.Group` objects.

        Returns
        -------
        List[:class:`~steam.Group`]
            The user's groups.
        """
        resp = await self._state.http.fetch_user_groups(self.id64)
        groups = []
        for group in resp['response']['groups']:
            try:
                group = await self._state.client.fetch_group(group['gid'])
            except HTTPException:
                break
            else:
                groups.append(group)
        return groups

    async def fetch_bans(self) -> Ban:
        """|coro|
        Fetches the :class:`User`'s :class:`~steam.Ban` objects.

        Returns
        -------
        :class:`~steam.Ban`
            The user's bans.
        """
        resp = await self._state.http.fetch_user_bans(self.id64)
        resp['EconomyBan'] = False if resp['EconomyBan'] == 'none' else resp['EconomyBan']
        return Ban(data=resp)

    async def fetch_badges(self) -> UserBadges:
        """|coro|
        Fetches the :class:`User`'s :class:`~steam.UserBadges` objects.

        Returns
        -------
        :class:`~steam.UserBadges`
            The user's badges.
        """
        resp = await self._state.http.fetch_user_badges(self.id64)
        return UserBadges(data=resp['response'])

    async def fetch_level(self) -> int:
        """|coro|
        Fetches the :class:`User`'s level.

        Returns
        -------
        :class:`int`
            The user's level.
        """
        resp = await self._state.http.fetch_user_level(self.id64)
        return resp['response']['player_level']

    def is_commentable(self) -> bool:
        """:class:`bool`: Specifies if the user's account is able to be commented on."""
        return bool(self._data.get('commentpermission'))

    def is_private(self) -> bool:
        """:class:`bool`: Specifies if the user has a public profile."""
        state = self._data.get('communityvisibilitystate', 0)
        return state in {0, 1, 2}

    def has_setup_profile(self) -> bool:
        """:class:`bool`: Specifies if the user has a setup their profile."""
        return bool(self._data.get('profilestate'))

    async def is_banned(self) -> bool:
        """|coro|
        :class:`bool`: Specifies if the user is banned from any part of Steam.

        This is equivalent to::

            bans = await user.fetch_bans()
            bans.is_banned()
        """
        bans = await self.fetch_bans()
        return bans.is_banned()

    def comments(self, limit=None, before: datetime = None, after: datetime = None) -> CommentsIterator:
        """An iterator for accessing a :class:`~steam.User`'s :class:`~steam.Comment` objects.

        Examples
        -----------

        Usage::

            async for comment in user.comments(limit=10):
                print('Author:', comment.author, 'Said:', comment.content)

        Flattening into a list::

            comments = await user.comments(limit=50).flatten()
            # comments is now a list of Comment

        All parameters are optional.

        Parameters
        ----------
        limit: Optional[:class:`int`]
            The maximum number of comments to search through.
            Default is ``None`` which will fetch the user's entire comments section.
        before: Optional[:class:`datetime.datetime`]
            A time to search for comments before.
        after: Optional[:class:`datetime.datetime`]
            A time to search for comments after.

        Yields
        ---------
        :class:`~steam.Comment`
            The comment with the comment information parsed.
        """
        return CommentsIterator(state=self._state, id=self.id64, limit=limit, before=before, after=after,
                                comment_type='Profile')


class Messageable(metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a Steam message.
    The following classes implement this ABC:

        - :class:`~steam.User`
        - :class:`~steam.Message`
    """

    __slots__ = ()

    async def send(self, content: str = None, image: 'Image' = None):
        """|coro|
        Send a message to a certain destination.

        Parameters
        ----------
        content: Optional[:class:`str`]
            The content of the message to send.
        image: Optional[:class:`.Image`]
            The image to send to the user. This doesn't fully work yet.

        Raises
        ------
        ~steam.HTTPException
            Sending the message failed.
        ~steam.Forbidden
            You do not have permission to send the message.

        Returns
        -------
        :class:`~steam.Message`
            The message that was sent.
        """
        # ret = state.create_message(channel=channel, data=data)
        # return ret
        pass


def make_steam64(id=0, *args, **kwargs) -> int:
    """Returns a Steam 64-bit ID from various other representations.

    .. code:: python

        make_steam64()  # invalid steam_id
        make_steam64(12345)  # account_id
        make_steam64('12345')
        make_steam64(id=12345, type='Invalid', universe='Invalid', instance=0)
        make_steam64(103582791429521412)  # steam64
        make_steam64('103582791429521412')
        make_steam64('STEAM_1:0:2')  # steam2
        make_steam64('[g:1:4]')  # steam3
        make_steam64('cv-dgb')  # invite code

    Raises
    ------
    :exc:`TypeError`
        Too many arguments have been given.

    Returns
    -------
    :class:`int`
        The 64-bit Steam ID.
    """

    etype = EType.Invalid
    universe = EUniverse.Invalid
    instance = None

    if len(args) == 0 and len(kwargs) == 0:
        value = str(id)

        # numeric input
        if value.isdigit():
            value = int(value)

            # 32 bit account id
            if 0 < value < 2 ** 32:
                id = value
                etype = EType.Individual
                universe = EUniverse.Public
            # 64 bit
            elif value < 2 ** 64:
                return value

        # textual input e.g. [g:1:4]
        else:
            result = steam2_to_tuple(value) or steam3_to_tuple(value) or invite_code_to_tuple(value)

            if result:
                id, etype, universe, instance = result
            else:
                id = 0

    elif len(args) > 0:
        length = len(args)
        if length == 1:
            etype, = args
        elif length == 2:
            etype, universe = args
        elif length == 3:
            etype, universe, instance = args
        else:
            raise TypeError(f"Takes at most 4 arguments ({length} given)")

    if len(kwargs) > 0:
        etype = kwargs.get('type', etype)
        universe = kwargs.get('universe', universe)
        instance = kwargs.get('instance', instance)

    etype = (EType(etype.value if isinstance(etype, EType) else etype)
             if isinstance(etype, (int, EType)) else EType[etype])
    universe = (EUniverse(universe.value if isinstance(universe, EUniverse) else etype)
                if isinstance(universe, (int, EUniverse)) else EUniverse[universe])

    if instance is None:
        instance = 1 if etype in (EType.Individual, EType.GameServer) else 0

    return (universe.value << 56) | (etype.value << 52) | (instance << 32) | id


def steam2_to_tuple(value: str):
    """
    Parameters
    ----------
    value: :class:`str`
        steam2 e.g. ``STEAM_1:0:1234``.

    Returns
    -------
    Optional[:class:`tuple`]
        e.g. (account_id, type, universe, instance) or ``None``.

    .. note::
        The universe will be always set to ``1``. See :attr:`SteamID.as_steam2`.
    """
    match = re.match(
        r"^STEAM_(?P<universe>\d+)"
        r":(?P<reminder>[0-1])"
        r":(?P<id>\d+)$", value
    )

    if not match:
        return None

    steam_32 = (int(match.group('id')) << 1) | int(match.group('reminder'))
    universe = int(match.group('universe'))

    # Games before orange box used to incorrectly display universe as 0, we support that
    if universe == 0:
        universe = 1

    return steam_32, EType(1), EUniverse(universe), 1


def steam3_to_tuple(value: str):
    """
    Parameters
    ----------
    value: :class:`str`
        steam3 e.g. ``[U:1:1234]``.

    Returns
    -------
    Optional[:class:`tuple`]
        e.g. (account_id, type, universe, instance) or ``None``.
    """
    match = re.match(
        r"^\["
        rf"(?P<type>[i{ETypeChars}]):"  # type char
        r"(?P<universe>[0-4]):"  # universe
        r"(?P<id>\d{1,10})"  # accountid
        r"(:(?P<instance>\d+))?"  # instance
        r"\]$",
        value
    )
    if not match:
        return None

    steam_32 = int(match.group('id'))
    universe = EUniverse(int(match.group('universe')))
    typechar = match.group('type').replace('i', 'I')
    etype = EType(ETypeChar[typechar])
    instance = match.group('instance')

    if typechar in 'gT':
        instance = 0
    elif instance is not None:
        instance = int(instance)
    elif typechar == 'L':
        instance = EInstanceFlag.Lobby
    elif typechar == 'c':
        instance = EInstanceFlag.Clan
    elif etype in (EType.Individual, EType.GameServer):
        instance = 1
    else:
        instance = 0

    instance = int(instance)

    return steam_32, etype, universe, instance


def invite_code_to_tuple(code, universe=EUniverse.Public):
    match = re.match(rf'(https?://s\.team/p/(?P<code1>[\-{_ICODE_VALID}]+))'
                     rf'|(?P<code2>[\-{_ICODE_VALID}]+$)', code)
    if not match:
        return None

    code = (match.group('code1') or match.group('code2')).replace('-', '')

    def repl_mapper(x):
        return _ICODE_INVERSE_MAPPING[x.group()]

    steam_32 = int(re.sub(f"[{_ICODE_CUSTOM}]", repl_mapper, code), 16)

    if 0 < steam_32 < 2 ** 32:
        return steam_32, EType(1), EUniverse(universe) if isinstance(universe, int) else EUniverse(universe.value), 1


async def steam64_from_url(url: str, timeout=30) -> Optional[int]:
    """Takes a Steam Community url and returns steam64 or None

    .. note::
        Each call makes a http request to steamcommunity.com

    .. note::
        Example URLs
            https://steamcommunity.com/gid/[g:1:4]

            https://steamcommunity.com/gid/103582791429521412

            https://steamcommunity.com/groups/Valve

            https://steamcommunity.com/profiles/[U:1:12]

            https://steamcommunity.com/profiles/76561197960265740

            https://steamcommunity.com/id/johnc

    Parameters
    ----------
    url: :class:`str`
        The Steam community url.
    timeout: :class:`int`
        How long to wait on http request before turning ``None``.

    Returns
    -------
    steam64: Optional[:class:`int`]
        If ``steamcommunity.com`` is down or no matching account is found returns ``None``
    """

    match = re.match(r'^(?P<clean_url>https?://steamcommunity.com/'
                     r'(?P<type>profiles|id|gid|groups)/(?P<value>.*?))(?:/(?:.*)?)?$', str(url))

    if match is None:
        return None

    session = aiohttp.ClientSession()

    try:
        # user profiles
        if match.group('type') in ('id', 'profiles'):
            async with session.get(match.group('clean_url'), timeout=timeout) as r:
                text = await r.text()
                await session.close()
            data_match = re.search("g_rgProfileData = (?P<json>{.*?});\s*", text)

            if data_match:
                data = json.loads(data_match.group('json'))
                return int(data['steamid'])
        # group profiles
        else:
            async with session.get(match.group('clean_url'), timeout=timeout) as r:
                text = await r.text()
                await session.close()
            data_match = re.search(r"OpenGroupChat\( *'(?P<steamid>\d+)'", text)

            if data_match:
                return int(data_match.group('steamid'))
    except aiohttp.InvalidURL:
        return None
