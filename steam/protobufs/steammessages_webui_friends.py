# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_webui_friends.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List, TYPE_CHECKING

import betterproto

if TYPE_CHECKING:
    from .steammessages_base import CMsgIPAddress


@dataclass
class CCommunity_GetApps_Request(betterproto.Message):
    appids: List[int] = betterproto.int32_field(1)
    language: int = betterproto.uint32_field(2)


@dataclass
class CCommunity_GetApps_Response(betterproto.Message):
    apps: List["CCDDBAppDetailCommon"] = betterproto.message_field(1)


@dataclass
class CCommunity_GetAppRichPresenceLocalization_Request(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    language: str = betterproto.string_field(2)


@dataclass
class CCommunity_GetAppRichPresenceLocalization_Response(betterproto.Message):
    appid: int = betterproto.int32_field(1)
    token_lists: List[
        "CCommunity_GetAppRichPresenceLocalization_Response_TokenList"
    ] = betterproto.message_field(2)


@dataclass
class CCommunity_GetAppRichPresenceLocalization_Response_Token(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CCommunity_GetAppRichPresenceLocalization_Response_TokenList(betterproto.Message):
    language: str = betterproto.string_field(1)
    tokens: List[
        "CCommunity_GetAppRichPresenceLocalization_Response_Token"
    ] = betterproto.message_field(2)


@dataclass
class CCommunity_Comment(betterproto.Message):
    gidcomment: float = betterproto.fixed64_field(1)
    steamid: float = betterproto.fixed64_field(2)
    timestamp: int = betterproto.uint32_field(3)
    text: str = betterproto.string_field(4)
    upvotes: int = betterproto.int32_field(5)
    hidden: bool = betterproto.bool_field(6)
    hidden_by_user: bool = betterproto.bool_field(7)
    deleted: bool = betterproto.bool_field(8)
    ipaddress: "CMsgIPAddress" = betterproto.message_field(9)
    total_hidden: int = betterproto.int32_field(10)
    upvoted_by_user: bool = betterproto.bool_field(11)


@dataclass
class CCommunity_GetCommentThread_Response(betterproto.Message):
    comments: List["CCommunity_Comment"] = betterproto.message_field(1)
    deleted_comments: List["CCommunity_Comment"] = betterproto.message_field(2)
    steamid: float = betterproto.fixed64_field(3)
    commentthreadid: float = betterproto.fixed64_field(4)
    start: int = betterproto.int32_field(5)
    count: int = betterproto.int32_field(6)
    total_count: int = betterproto.int32_field(7)
    upvotes: int = betterproto.int32_field(8)
    upvoters: List[int] = betterproto.uint32_field(9)
    user_subscribed: bool = betterproto.bool_field(10)
    user_upvoted: bool = betterproto.bool_field(11)
    answer_commentid: float = betterproto.fixed64_field(12)
    answer_actor: int = betterproto.uint32_field(13)
    answer_actor_rank: int = betterproto.int32_field(14)
    can_post: bool = betterproto.bool_field(15)


@dataclass
class CCommunity_PostCommentToThread_Response(betterproto.Message):
    gidcomment: float = betterproto.fixed64_field(1)
    commentthreadid: float = betterproto.fixed64_field(2)
    count: int = betterproto.int32_field(3)
    upvotes: int = betterproto.int32_field(4)


@dataclass
class CCommunity_DeleteCommentFromThread_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_RateCommentThread_Response(betterproto.Message):
    gidcomment: int = betterproto.uint64_field(1)
    commentthreadid: int = betterproto.uint64_field(2)
    count: int = betterproto.uint32_field(3)
    upvotes: int = betterproto.uint32_field(4)
    has_upvoted: bool = betterproto.bool_field(5)


@dataclass
class CCommunity_GetCommentThreadRatings_Response(betterproto.Message):
    commentthreadid: int = betterproto.uint64_field(1)
    gidcomment: int = betterproto.uint64_field(2)
    upvotes: int = betterproto.uint32_field(3)
    has_upvoted: bool = betterproto.bool_field(4)
    upvoter_accountids: List[int] = betterproto.uint32_field(5)


@dataclass
class CCommunity_RateClanAnnouncement_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_GetClanAnnouncementVoteForUser_Response(betterproto.Message):
    voted_up: bool = betterproto.bool_field(1)
    voted_down: bool = betterproto.bool_field(2)


@dataclass
class CAppPriority(betterproto.Message):
    priority: int = betterproto.uint32_field(1)
    appid: List[int] = betterproto.uint32_field(2)


@dataclass
class CCommunity_GetUserPartnerEventNews_Response(betterproto.Message):
    results: List["CClanMatchEventByRange"] = betterproto.message_field(1)


@dataclass
class CCommunity_PartnerEventResult(betterproto.Message):
    clanid: int = betterproto.uint32_field(1)
    event_gid: float = betterproto.fixed64_field(2)
    announcement_gid: float = betterproto.fixed64_field(3)
    appid: int = betterproto.uint32_field(4)
    possible_takeover: bool = betterproto.bool_field(5)
    rtime32_last_modified: int = betterproto.uint32_field(6)
    user_app_priority: int = betterproto.int32_field(7)


@dataclass
class CCommunity_GetBestEventsForUser_Response(betterproto.Message):
    results: List["CCommunity_PartnerEventResult"] = betterproto.message_field(1)


@dataclass
class CCommunity_ClearUserPartnerEventsAppPriorities_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_PartnerEventsAppPriority(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    user_app_priority: int = betterproto.int32_field(2)


@dataclass
class CCommunity_GetUserPartnerEventsAppPriorities_Response(betterproto.Message):
    priorities: List["CCommunity_PartnerEventsAppPriority"] = betterproto.message_field(
        1
    )


@dataclass
class CCommunity_ClearSinglePartnerEventsAppPriority_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_PartnerEventsShowMoreForApp_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_PartnerEventsShowLessForApp_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_MarkPartnerEventsForUser_Request_PartnerEventMarking(
    betterproto.Message
):
    clanid: int = betterproto.uint32_field(1)
    event_gid: float = betterproto.fixed64_field(2)
    display_location: int = betterproto.int32_field(3)
    mark_shown: bool = betterproto.bool_field(4)
    mark_read: bool = betterproto.bool_field(5)


@dataclass
class CCommunity_MarkPartnerEventsForUser_Response(betterproto.Message):
    pass


@dataclass
class CCommunity_GetUserPartnerEventViewStatus_Response(betterproto.Message):
    events: List[
        "CCommunity_GetUserPartnerEventViewStatus_Response_PartnerEvent"
    ] = betterproto.message_field(1)


@dataclass
class CCommunity_GetUserPartnerEventViewStatus_Response_PartnerEvent(
    betterproto.Message
):
    event_gid: float = betterproto.fixed64_field(1)
    last_shown_time: int = betterproto.uint32_field(2)
    last_read_time: int = betterproto.uint32_field(3)
    clan_account_id: int = betterproto.uint32_field(4)


@dataclass
class ProfileItem(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)
    image_small: str = betterproto.string_field(2)
    image_large: str = betterproto.string_field(3)
    name: str = betterproto.string_field(4)
    item_title: str = betterproto.string_field(5)
    item_description: str = betterproto.string_field(6)
    appid: int = betterproto.uint32_field(7)
    item_type: int = betterproto.uint32_field(8)
    item_class: int = betterproto.uint32_field(9)
    movie_webm: str = betterproto.string_field(10)
    movie_mp4: str = betterproto.string_field(11)


@dataclass
class CPlayer_GetProfileBackground_Response(betterproto.Message):
    profile_background: "ProfileItem" = betterproto.message_field(1)


@dataclass
class CPlayer_SetProfileBackground_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetMiniProfileBackground_Response(betterproto.Message):
    profile_background: "ProfileItem" = betterproto.message_field(1)


@dataclass
class CPlayer_SetMiniProfileBackground_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetAvatarFrame_Response(betterproto.Message):
    avatar_frame: "ProfileItem" = betterproto.message_field(1)


@dataclass
class CPlayer_SetAvatarFrame_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetAnimatedAvatar_Response(betterproto.Message):
    avatar: "ProfileItem" = betterproto.message_field(1)


@dataclass
class CPlayer_SetAnimatedAvatar_Response(betterproto.Message):
    pass


@dataclass
class CPlayer_GetProfileItemsOwned_Response(betterproto.Message):
    profile_backgrounds: List["ProfileItem"] = betterproto.message_field(1)
    mini_profile_backgrounds: List["ProfileItem"] = betterproto.message_field(2)
    avatar_frames: List["ProfileItem"] = betterproto.message_field(3)
    animated_avatars: List["ProfileItem"] = betterproto.message_field(4)


@dataclass
class CPlayer_GetProfileItemsEquipped_Response(betterproto.Message):
    profile_background: "ProfileItem" = betterproto.message_field(1)
    mini_profile_background: "ProfileItem" = betterproto.message_field(2)
    avatar_frame: "ProfileItem" = betterproto.message_field(3)
    animated_avatar: "ProfileItem" = betterproto.message_field(4)


@dataclass
class CWebRTCClient_InitiateWebRTCConnection_Request(betterproto.Message):
    sdp: str = betterproto.string_field(1)


@dataclass
class CWebRTCClient_InitiateWebRTCConnection_Response(betterproto.Message):
    remote_description: str = betterproto.string_field(1)


@dataclass
class CWebRTC_WebRTCSessionConnected_Notification(betterproto.Message):
    ssrc: int = betterproto.uint32_field(1)
    client_ip: int = betterproto.uint32_field(2)
    client_port: int = betterproto.uint32_field(3)
    server_ip: int = betterproto.uint32_field(4)
    server_port: int = betterproto.uint32_field(5)


@dataclass
class CWebRTC_WebRTCUpdateRemoteDescription_Notification(betterproto.Message):
    remote_description: str = betterproto.string_field(1)
    remote_description_version: int = betterproto.uint64_field(2)
    ssrcs_to_accountids: List[
        "CWebRTC_WebRTCUpdateRemoteDescription_Notification_CSSRCToAccountIDMapping"
    ] = betterproto.message_field(3)


@dataclass
class CWebRTC_WebRTCUpdateRemoteDescription_Notification_CSSRCToAccountIDMapping(
    betterproto.Message
):
    ssrc: int = betterproto.uint32_field(1)
    accountid: int = betterproto.uint32_field(2)


@dataclass
class CWebRTCClient_AcknowledgeUpdatedRemoteDescription_Request(betterproto.Message):
    ip_webrtc_server: int = betterproto.uint32_field(1)
    port_webrtc_server: int = betterproto.uint32_field(2)
    ip_webrtc_session_client: int = betterproto.uint32_field(3)
    port_webrtc_session_client: int = betterproto.uint32_field(4)
    remote_description_version: int = betterproto.uint64_field(5)


@dataclass
class CWebRTCClient_AcknowledgeUpdatedRemoteDescription_Response(betterproto.Message):
    pass


@dataclass
class CVoiceChat_RequestOneOnOneChat_Request(betterproto.Message):
    steamid_partner: float = betterproto.fixed64_field(1)


@dataclass
class CVoiceChat_RequestOneOnOneChat_Response(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)


@dataclass
class CVoiceChat_OneOnOneChatRequested_Notification(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    steamid_partner: float = betterproto.fixed64_field(2)


@dataclass
class CVoiceChat_AnswerOneOnOneChat_Request(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    steamid_partner: float = betterproto.fixed64_field(2)
    accepted_request: bool = betterproto.bool_field(3)


@dataclass
class CVoiceChat_AnswerOneOnOneChat_Response(betterproto.Message):
    pass


@dataclass
class CVoiceChat_OneOnOneChatRequestResponse_Notification(betterproto.Message):
    voicechat_id: float = betterproto.fixed64_field(1)
    steamid_partner: float = betterproto.fixed64_field(2)
    accepted_request: bool = betterproto.bool_field(3)


@dataclass
class CVoiceChat_EndOneOnOneChat_Request(betterproto.Message):
    steamid_partner: float = betterproto.fixed64_field(1)


@dataclass
class CVoiceChat_EndOneOnOneChat_Response(betterproto.Message):
    pass


@dataclass
class CVoiceChat_LeaveOneOnOneChat_Request(betterproto.Message):
    steamid_partner: float = betterproto.fixed64_field(1)
    voice_chatid: float = betterproto.fixed64_field(2)


@dataclass
class CVoiceChat_LeaveOneOnOneChat_Response(betterproto.Message):
    pass


@dataclass
class CVoiceChat_UserJoinedVoiceChat_Notification(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    user_steamid: float = betterproto.fixed64_field(2)
    chatid: int = betterproto.uint64_field(3)
    one_on_one_steamid_lower: float = betterproto.fixed64_field(4)
    one_on_one_steamid_higher: float = betterproto.fixed64_field(5)
    chat_group_id: int = betterproto.uint64_field(6)
    user_sessionid: int = betterproto.uint32_field(7)


@dataclass
class CVoiceChat_UserVoiceStatus_Notification(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    user_steamid: float = betterproto.fixed64_field(2)
    user_muted_mic_locally: bool = betterproto.bool_field(3)
    user_muted_output_locally: bool = betterproto.bool_field(4)
    user_has_no_mic_for_session: bool = betterproto.bool_field(5)
    user_webaudio_sample_rate: int = betterproto.int32_field(6)


@dataclass
class CVoiceChat_AllMembersStatus_Notification(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    users: List["CVoiceChat_UserVoiceStatus_Notification"] = betterproto.message_field(
        2
    )


@dataclass
class CVoiceChat_UpdateVoiceChatWebRTCData_Request(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    ip_webrtc_server: int = betterproto.uint32_field(2)
    port_webrtc_server: int = betterproto.uint32_field(3)
    ip_webrtc_client: int = betterproto.uint32_field(4)
    port_webrtc_client: int = betterproto.uint32_field(5)
    ssrc_my_sending_stream: int = betterproto.uint32_field(6)
    user_agent: str = betterproto.string_field(7)
    has_audio_worklets_support: bool = betterproto.bool_field(8)


@dataclass
class CVoiceChat_UpdateVoiceChatWebRTCData_Response(betterproto.Message):
    send_client_voice_logs: bool = betterproto.bool_field(1)


@dataclass
class CVoiceChat_UploadClientVoiceChatLogs_Request(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    client_voice_logs_new_lines: str = betterproto.string_field(2)


@dataclass
class CVoiceChat_UploadClientVoiceChatLogs_Response(betterproto.Message):
    pass


@dataclass
class CVoiceChat_LeaveVoiceChat_Response(betterproto.Message):
    pass


@dataclass
class CVoiceChat_UserLeftVoiceChat_Notification(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    user_steamid: float = betterproto.fixed64_field(2)
    chatid: int = betterproto.uint64_field(3)
    one_on_one_steamid_lower: float = betterproto.fixed64_field(4)
    one_on_one_steamid_higher: float = betterproto.fixed64_field(5)
    chat_group_id: int = betterproto.uint64_field(6)
    user_sessionid: int = betterproto.uint32_field(7)


@dataclass
class CVoiceChat_VoiceChatEnded_Notification(betterproto.Message):
    voice_chatid: float = betterproto.fixed64_field(1)
    one_on_one_steamid_lower: float = betterproto.fixed64_field(2)
    one_on_one_steamid_higher: float = betterproto.fixed64_field(3)
    chatid: int = betterproto.uint64_field(4)
    chat_group_id: int = betterproto.uint64_field(5)


@dataclass
class CSteamTV_CreateBroadcastChannel_Response(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)


@dataclass
class CSteamTV_GetBroadcastChannelID_Response(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)
    unique_name: str = betterproto.string_field(2)
    steamid: float = betterproto.fixed64_field(3)


@dataclass
class CSteamTV_SetBroadcastChannelProfile_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetBroadcastChannelProfile_Response(betterproto.Message):
    unique_name: str = betterproto.string_field(1)
    owner_steamid: float = betterproto.fixed64_field(2)
    name: str = betterproto.string_field(3)
    language: str = betterproto.string_field(4)
    headline: str = betterproto.string_field(5)
    summary: str = betterproto.string_field(6)
    schedule: str = betterproto.string_field(7)
    rules: str = betterproto.string_field(8)
    panels: str = betterproto.string_field(9)
    is_partnered: bool = betterproto.bool_field(10)


@dataclass
class CSteamTV_SetBroadcastChannelImage_Response(betterproto.Message):
    replace_image_hash: str = betterproto.string_field(1)


@dataclass
class CSteamTV_GetBroadcastChannelImages_Response(betterproto.Message):
    images: List[
        "CSteamTV_GetBroadcastChannelImages_Response_Images"
    ] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetBroadcastChannelImages_Response_Images(betterproto.Message):
    image_type: int = betterproto.int32_field(1)
    image_path: str = betterproto.string_field(2)
    image_index: int = betterproto.uint32_field(3)


@dataclass
class CSteamTV_GetBroadcastChannelLinks_Response(betterproto.Message):
    links: List[
        "CSteamTV_GetBroadcastChannelLinks_Response_Links"
    ] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetBroadcastChannelLinks_Response_Links(betterproto.Message):
    link_index: int = betterproto.uint32_field(1)
    url: str = betterproto.string_field(2)
    link_description: str = betterproto.string_field(3)
    left: int = betterproto.uint32_field(4)
    top: int = betterproto.uint32_field(5)
    width: int = betterproto.uint32_field(6)
    height: int = betterproto.uint32_field(7)


@dataclass
class CSteamTV_SetBroadcastChannelLinkRegions_Request_Links(betterproto.Message):
    link_index: int = betterproto.uint32_field(1)
    url: str = betterproto.string_field(2)
    link_description: str = betterproto.string_field(3)
    left: int = betterproto.uint32_field(4)
    top: int = betterproto.uint32_field(5)
    width: int = betterproto.uint32_field(6)
    height: int = betterproto.uint32_field(7)


@dataclass
class CSteamTV_SetBroadcastChannelLinkRegions_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetBroadcastChannelStatus_Response(betterproto.Message):
    is_live: bool = betterproto.bool_field(1)
    is_disabled: bool = betterproto.bool_field(2)
    appid: int = betterproto.uint32_field(3)
    viewers: int = betterproto.uint64_field(4)
    views: int = betterproto.uint64_field(5)
    broadcaster_steamid: float = betterproto.fixed64_field(6)
    thumbnail_url: str = betterproto.string_field(7)
    followers: int = betterproto.uint64_field(8)
    subscribers: int = betterproto.uint64_field(9)
    unique_name: str = betterproto.string_field(10)
    broadcast_session_id: int = betterproto.uint64_field(11)


@dataclass
class GetBroadcastChannelEntry(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)
    unique_name: str = betterproto.string_field(2)
    name: str = betterproto.string_field(3)
    appid: int = betterproto.uint32_field(4)
    viewers: int = betterproto.uint64_field(5)
    views: int = betterproto.uint64_field(6)
    thumbnail_url: str = betterproto.string_field(7)
    followers: int = betterproto.uint64_field(8)
    headline: str = betterproto.string_field(9)
    avatar_url: str = betterproto.string_field(10)
    broadcaster_steamid: float = betterproto.fixed64_field(11)
    subscribers: int = betterproto.uint64_field(12)
    background_url: str = betterproto.string_field(13)
    is_featured: bool = betterproto.bool_field(14)
    is_disabled: bool = betterproto.bool_field(15)
    is_live: bool = betterproto.bool_field(16)
    language: str = betterproto.string_field(17)
    reports: int = betterproto.uint32_field(18)
    is_partnered: bool = betterproto.bool_field(19)


@dataclass
class CSteamTV_GetFollowedChannels_Response(betterproto.Message):
    results: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetSubscribedChannels_Response(betterproto.Message):
    results: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)


@dataclass
class CSteamTV_FollowBroadcastChannel_Response(betterproto.Message):
    is_followed: bool = betterproto.bool_field(1)


@dataclass
class CSteamTV_SubscribeBroadcastChannel_Response(betterproto.Message):
    is_subscribed: bool = betterproto.bool_field(1)


@dataclass
class CSteamTV_ReportBroadcastChannel_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetBroadcastChannelInteraction_Response(betterproto.Message):
    is_followed: bool = betterproto.bool_field(1)
    is_subscribed: bool = betterproto.bool_field(2)


@dataclass
class CSteamTV_Game(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    image: str = betterproto.string_field(3)
    viewers: int = betterproto.uint64_field(4)
    channels: List["GetBroadcastChannelEntry"] = betterproto.message_field(5)
    release_date: str = betterproto.string_field(6)
    developer: str = betterproto.string_field(7)
    publisher: str = betterproto.string_field(8)


@dataclass
class CSteamTV_GetGames_Response(betterproto.Message):
    results: List["CSteamTV_Game"] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetChannels_Response(betterproto.Message):
    results: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetBroadcastChannelBroadcasters_Response(betterproto.Message):
    broadcasters: List[
        "CSteamTV_GetBroadcastChannelBroadcasters_Response_Broadcaster"
    ] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetBroadcastChannelBroadcasters_Response_Broadcaster(
    betterproto.Message
):
    steamid: float = betterproto.fixed64_field(1)
    name: str = betterproto.string_field(2)
    rtmp_token: str = betterproto.string_field(3)


@dataclass
class CSteamTV_ChatBan(betterproto.Message):
    issuer_steamid: float = betterproto.fixed64_field(1)
    chatter_steamid: float = betterproto.fixed64_field(2)
    time_expires: str = betterproto.string_field(3)
    permanent: bool = betterproto.bool_field(4)
    name: str = betterproto.string_field(5)


@dataclass
class CSteamTV_AddChatBan_Request(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)
    chatter_steamid: float = betterproto.fixed64_field(2)
    duration: int = betterproto.uint32_field(3)
    permanent: bool = betterproto.bool_field(4)
    undo: bool = betterproto.bool_field(5)


@dataclass
class CSteamTV_AddChatBan_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetChatBans_Response(betterproto.Message):
    results: List["CSteamTV_ChatBan"] = betterproto.message_field(1)


@dataclass
class CSteamTV_AddChatModerator_Request(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)
    moderator_steamid: float = betterproto.fixed64_field(2)
    undo: bool = betterproto.bool_field(3)


@dataclass
class CSteamTV_AddChatModerator_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetChatModerators_Request(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)


@dataclass
class CSteamTV_ChatModerator(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    name: str = betterproto.string_field(2)


@dataclass
class CSteamTV_GetChatModerators_Response(betterproto.Message):
    results: List["CSteamTV_ChatModerator"] = betterproto.message_field(1)


@dataclass
class CSteamTV_AddWordBan_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetWordBans_Response(betterproto.Message):
    results: List[str] = betterproto.string_field(1)


@dataclass
class CSteamTV_JoinChat_Request(betterproto.Message):
    broadcast_channel_id: float = betterproto.fixed64_field(1)


@dataclass
class CSteamTV_JoinChat_Response(betterproto.Message):
    chat_id: float = betterproto.fixed64_field(1)
    view_url_template: str = betterproto.string_field(2)
    flair_group_ids: List[int] = betterproto.uint64_field(3)


@dataclass
class CSteamTV_Search_Response(betterproto.Message):
    results: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)


@dataclass
class CSteamTV_GetSteamTVUserSettings_Response(betterproto.Message):
    stream_live_email: bool = betterproto.bool_field(1)
    stream_live_notification: bool = betterproto.bool_field(2)


@dataclass
class CSteamTV_SetSteamTVUserSettings_Response(betterproto.Message):
    pass


@dataclass
class CSteamTV_GetMyBroadcastChannels_Response(betterproto.Message):
    results: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)


@dataclass
class CSteamTV_HomePageTemplate_Takeover(betterproto.Message):
    broadcasts: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)


@dataclass
class CSteamTV_HomePageTemplate_SingleGame(betterproto.Message):
    broadcasts: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)
    appid: int = betterproto.uint32_field(2)
    title: str = betterproto.string_field(3)


@dataclass
class GameListEntry(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    game_name: str = betterproto.string_field(2)
    broadcast: "GetBroadcastChannelEntry" = betterproto.message_field(3)


@dataclass
class CSteamTV_HomePageTemplate_GameList(betterproto.Message):
    entries: List["GameListEntry"] = betterproto.message_field(1)
    title: str = betterproto.string_field(2)


@dataclass
class CSteamTV_HomePageTemplate_QuickExplore(betterproto.Message):
    broadcasts: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)
    title: str = betterproto.string_field(2)


@dataclass
class CSteamTV_HomePageTemplate_ConveyorBelt(betterproto.Message):
    broadcasts: List["GetBroadcastChannelEntry"] = betterproto.message_field(1)
    title: str = betterproto.string_field(2)


@dataclass
class CSteamTV_HomePageTemplate_WatchParty(betterproto.Message):
    broadcast: "GetBroadcastChannelEntry" = betterproto.message_field(1)
    title: str = betterproto.string_field(2)
    chat_group_id: int = betterproto.uint64_field(3)


@dataclass
class CSteamTV_HomePageTemplate_Developer(betterproto.Message):
    broadcast: "GetBroadcastChannelEntry" = betterproto.message_field(1)
    title: str = betterproto.string_field(2)


@dataclass
class CSteamTV_HomePageTemplate_Event(betterproto.Message):
    title: str = betterproto.string_field(1)


@dataclass
class CSteamTV_HomePageContentRow(betterproto.Message):
    template_type: int = betterproto.int32_field(1)
    takeover: "CSteamTV_HomePageTemplate_Takeover" = betterproto.message_field(2)
    single_game: "CSteamTV_HomePageTemplate_SingleGame" = betterproto.message_field(3)
    game_list: "CSteamTV_HomePageTemplate_GameList" = betterproto.message_field(4)
    quick_explore: "CSteamTV_HomePageTemplate_QuickExplore" = betterproto.message_field(5)
    conveyor_belt: "CSteamTV_HomePageTemplate_ConveyorBelt" = betterproto.message_field(6)
    watch_party: "CSteamTV_HomePageTemplate_WatchParty" = betterproto.message_field(7)
    developer: "CSteamTV_HomePageTemplate_Developer" = betterproto.message_field(8)
    event: "CSteamTV_HomePageTemplate_Event" = betterproto.message_field(9)


@dataclass
class CSteamTV_GetHomePageContents_Response(betterproto.Message):
    rows: List["CSteamTV_HomePageContentRow"] = betterproto.message_field(1)


@dataclass
class CSteamTV_BroadcastClipInfo(betterproto.Message):
    broadcast_clip_id: int = betterproto.uint64_field(1)
    channel_id: int = betterproto.uint64_field(2)
    app_id: int = betterproto.uint32_field(3)
    broadcaster_steamid: float = betterproto.fixed64_field(4)
    creator_steamid: float = betterproto.fixed64_field(5)
    video_description: str = betterproto.string_field(6)
    live_time: int = betterproto.uint32_field(7)
    length_ms: int = betterproto.uint32_field(8)
    thumbnail_path: str = betterproto.string_field(9)


@dataclass
class CSteamTV_GetBroadcastChannelClips_Response(betterproto.Message):
    clips: List["CSteamTV_BroadcastClipInfo"] = betterproto.message_field(1)
    thumbnail_host: str = betterproto.string_field(2)


@dataclass
class CFriendsListCategory(betterproto.Message):
    groupid: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    accountid_members: List[int] = betterproto.uint32_field(3)


@dataclass
class CFriendsList_GetCategories_Request(betterproto.Message):
    pass


@dataclass
class CFriendsList_GetCategories_Response(betterproto.Message):
    categories: List["CFriendsListCategory"] = betterproto.message_field(1)


@dataclass
class CFriendsListFavoriteEntry(betterproto.Message):
    accountid: int = betterproto.uint32_field(1)
    clanid: int = betterproto.uint32_field(2)
    chat_group_id: int = betterproto.uint64_field(3)


@dataclass
class CFriendsList_GetFavorites_Request(betterproto.Message):
    pass


@dataclass
class CFriendsList_GetFavorites_Response(betterproto.Message):
    favorites: List["CFriendsListFavoriteEntry"] = betterproto.message_field(1)


@dataclass
class CFriendsList_SetFavorites_Request(betterproto.Message):
    favorites: List["CFriendsListFavoriteEntry"] = betterproto.message_field(1)


@dataclass
class CFriendsList_SetFavorites_Response(betterproto.Message):
    pass


@dataclass
class CFriendsList_FavoritesChanged_Notification(betterproto.Message):
    favorites: List["CFriendsListFavoriteEntry"] = betterproto.message_field(1)


@dataclass
class CFriendsList_GetFriendsList_Request(betterproto.Message):
    pass


@dataclass
class CFriendsList_GetFriendsList_Response(betterproto.Message):
    friends_list: "CMsgClientFriendsList" = betterproto.message_field(1)


@dataclass
class CClan_RespondToClanInvite_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    accept: bool = betterproto.bool_field(2)


@dataclass
class CClan_RespondToClanInvite_Response(betterproto.Message):
    pass


@dataclass
class CProductImpressionsFromClient_Notification(betterproto.Message):
    impressions: List[
        "CProductImpressionsFromClient_Notification_Impression"
    ] = betterproto.message_field(1)


@dataclass
class CProductImpressionsFromClient_Notification_Impression(betterproto.Message):
    type: int = betterproto.int32_field(1)
    appid: int = betterproto.uint32_field(2)
    num_impressions: int = betterproto.uint32_field(3)


@dataclass
class NotImplemented(betterproto.Message):
    pass