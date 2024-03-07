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
from pydantic import BaseModel, Field, RootModel


class ExtendedMessageClickEventInformation(BaseModel):
    click_location: typing.Optional[str] = Field(None, alias='ClickLocation')

    client: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='Client')

    geo: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='Geo')

    message_i_d: typing.Optional[str] = Field(None, alias='MessageID')

    o_s: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='OS')

    original_link: typing.Optional[str] = Field(None, alias='OriginalLink')

    platform: typing.Optional[str] = Field(None, alias='Platform')

    received_at: typing.Optional[datetime] = Field(None, alias='ReceivedAt')

    recipient: typing.Optional[str] = Field(None, alias='Recipient')

    tag: typing.Optional[str] = Field(None, alias='Tag')

    user_agent: typing.Optional[str] = Field(None, alias='UserAgent')
    class Config:
        arbitrary_types_allowed = True