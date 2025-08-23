# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PronunciationRuleParam"]


class PronunciationRuleParam(TypedDict, total=False):
    replacement: Required[str]
    """The phonetic spelling or pronunciation guide (e.g., 'sequel', 'see ee oh')"""

    target: Required[str]
    """The word or phrase to replace (e.g., 'SQL', 'CEO')"""
