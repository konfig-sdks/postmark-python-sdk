# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredOutboundOverviewStatsResponse(TypedDict):
    pass

class OptionalOutboundOverviewStatsResponse(TypedDict, total=False):
    BounceRate: int

    Bounced: int

    Opens: int

    SMTPAPIErrors: int

    Sent: int

    SpamComplaints: int

    SpamComplaintsRate: int

    TotalClicks: int

    TotalTrackedLinksSent: int

    Tracked: int

    UniqueLinksClicked: int

    UniqueOpens: int

    WithClientRecorded: int

    WithLinkTracking: int

    WithOpenTracking: int

    WithPlatformRecorded: int

class OutboundOverviewStatsResponse(RequiredOutboundOverviewStatsResponse, OptionalOutboundOverviewStatsResponse):
    pass
