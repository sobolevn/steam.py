# -*- coding: utf-8 -*-

"""
MIT License

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


class SteamException(Exception):
    """Base exception class for steam.py"""
    pass


class ClientException(SteamException):
    """Exception that's thrown when something isn't possible
    but is handled by the client.
    Subclass of :exc:`SteamException`
    """


class HTTPException(SteamException):
    """Exception that's thrown for any web API error.
    Subclass of :exc:`SteamException`
    """
    pass


class Forbidden(HTTPException):
    """Exception that's thrown when status code 403 occurs.
    Subclass of :exc:`HTTPException`
    """
    pass


class NotFound(HTTPException):
    """Exception that's thrown when status code 404 occurs.
    Subclass of :exc:`HTTPException`
    """
    pass


class LoginError(HTTPException):
    """Exception that's thrown when a login fails.
    Subclass of :exc:`HTTPException`
    """
    pass


class InvalidCredentials(LoginError):
    """Exception that's thrown when credentials are incorrect.
    Subclass of :exc:`LoginError`
    """
    pass


class SteamAuthenticatorError(LoginError):
    """Exception that's thrown when steam cannot authenticate your details.
    Subclass of :exc:`LoginError`
    """
    pass


class ConfirmationError(SteamAuthenticatorError):
    """Exception that's thrown when a confirmation fails.
    Subclass of :exc:`SteamAuthenticatorError`
    """
    pass