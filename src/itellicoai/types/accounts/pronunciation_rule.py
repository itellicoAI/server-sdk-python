# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PronunciationRule"]


class PronunciationRule(BaseModel):
    replacement: str
    """The phonetic spelling or pronunciation guide (e.g., 'sequel', 'see ee oh')"""

    target: str
    """The word or phrase to replace (e.g., 'SQL', 'CEO')"""
