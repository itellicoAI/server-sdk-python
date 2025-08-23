# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CheckInParam"]


class CheckInParam(TypedDict, total=False):
    max_count: int
    """Maximum number of check-in messages to send when the user is unresponsive.

    Set to 0 to disable check-in messages entirely. Maximum value is 10.
    """

    timeout_ms: int
    """Time in milliseconds to wait for user response before sending a check-in
    message.

    This keeps the conversation flowing when users are unresponsive. Minimum value
    is 5000ms (5 seconds), maximum is 300000ms (300 seconds).
    """
