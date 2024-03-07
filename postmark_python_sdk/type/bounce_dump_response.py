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


class RequiredBounceDumpResponse(TypedDict):
    pass

class OptionalBounceDumpResponse(TypedDict, total=False):
    # Raw source of bounce. If no dump is available this will return an empty string.
    Body: str

class BounceDumpResponse(RequiredBounceDumpResponse, OptionalBounceDumpResponse):
    pass