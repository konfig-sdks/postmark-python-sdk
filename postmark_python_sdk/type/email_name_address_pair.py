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


class RequiredEmailNameAddressPair(TypedDict):
    pass

class OptionalEmailNameAddressPair(TypedDict, total=False):
    Email: str

    Name: str

class EmailNameAddressPair(RequiredEmailNameAddressPair, OptionalEmailNameAddressPair):
    pass
