# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Account"]


class Account(BaseModel):
    created: str
    """ISO 8601 date-time string of when the account was created"""

    is_subaccount: bool
    """Whether this is a subaccount"""

    name: str
    """Account name"""

    uuid: str
    """Unique identifier for the account"""

    parent_account_id: Optional[str] = None
    """Parent account ID if this is a subaccount"""
