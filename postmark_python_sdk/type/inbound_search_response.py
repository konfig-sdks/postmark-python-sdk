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

from postmark_python_sdk.type.inbound_message_detail import InboundMessageDetail

class RequiredInboundSearchResponse(TypedDict):
    pass

class OptionalInboundSearchResponse(TypedDict, total=False):
    InboundMessages: typing.List[InboundMessageDetail]

    TotalCount: int

class InboundSearchResponse(RequiredInboundSearchResponse, OptionalInboundSearchResponse):
    pass
