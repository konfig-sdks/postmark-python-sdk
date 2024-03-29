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


class RequiredTemplateRecordResponse(TypedDict):
    pass

class OptionalTemplateRecordResponse(TypedDict, total=False):
    # True if this template is currently available for use.
    Active: bool

    # The user-supplied alias for this template.
    Alias: str

    # The display name for this template.
    Name: str

    # The associated ID for this template.
    TemplateId: typing.Union[int, float]

class TemplateRecordResponse(RequiredTemplateRecordResponse, OptionalTemplateRecordResponse):
    pass
