# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .usage_group_by import UsageGroupBy

__all__ = ["AnalyticsGetUsageResponse", "Meta", "Data", "DataValue"]


class Meta(BaseModel):
    """Metadata describing the usage analytics response.

    Attributes:
        account_id: UUID of the account for this usage data.
        start: Start datetime of the query range.
        end: End datetime of the query range.
        granularity: Time bucket granularity used.
        group_by: Grouping dimensions requested.
        tz: Timezone applied to bucket boundaries.
    """

    account_id: str

    end: datetime

    granularity: Literal["hour", "day", "month"]
    """Time bucket granularity for usage aggregation.

    Attributes: HOUR: Aggregate data by hour. DAY: Aggregate data by day. MONTH:
    Aggregate data by month.
    """

    start: datetime

    group_by: Optional[List[UsageGroupBy]] = None
    """Requested grouping dimensions."""

    tz: Optional[str] = None
    """Timezone applied to bucket boundaries."""


class DataValue(BaseModel):
    """Metric values aggregated for a single time bucket and dimension set.

    Attributes:
        seconds: Total conversation seconds for this value.
        conversations: Number of completed conversations.
        dimensions: Optional grouping dimension key/value pairs.
    """

    conversations: int
    """Completed conversations represented by this value."""

    seconds: int
    """Total conversation seconds represented by this value."""

    dimensions: Optional[Dict[str, str]] = None
    """Grouping dimension key/value pairs for this value."""


class Data(BaseModel):
    """Time bucket containing aggregated metric values.

    Attributes:
        ts: Bucket start timestamp in the requested timezone.
        values: List of metric values for this bucket.
    """

    ts: datetime
    """Bucket start timestamp in the requested timezone."""

    values: Optional[List[DataValue]] = None
    """Metric values for this bucket."""


class AnalyticsGetUsageResponse(BaseModel):
    """Complete usage analytics response payload.

    Attributes:
        meta: Metadata about the query and response.
        data: List of time buckets with aggregated usage values.
    """

    meta: Meta
    """Metadata describing the usage analytics response.

    Attributes: account_id: UUID of the account for this usage data. start: Start
    datetime of the query range. end: End datetime of the query range. granularity:
    Time bucket granularity used. group_by: Grouping dimensions requested. tz:
    Timezone applied to bucket boundaries.
    """

    data: Optional[List[Data]] = None
