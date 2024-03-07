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


class EditServerConfigurationRequest(BaseModel):
    bounce_hook_url: typing.Optional[str] = Field(None, alias='BounceHookUrl')

    # Webhook url allowing real-time notification when tracked links are clicked.
    click_hook_url: typing.Optional[str] = Field(None, alias='ClickHookUrl')

    color: typing.Optional[Literal["purple", "blue", "turqoise", "green", "red", "yellow", "grey"]] = Field(None, alias='Color')

    delivery_hook_url: typing.Optional[str] = Field(None, alias='DeliveryHookUrl')

    inbound_domain: typing.Optional[str] = Field(None, alias='InboundDomain')

    inbound_hook_url: typing.Optional[str] = Field(None, alias='InboundHookUrl')

    inbound_spam_threshold: typing.Optional[int] = Field(None, alias='InboundSpamThreshold')

    name: typing.Optional[str] = Field(None, alias='Name')

    open_hook_url: typing.Optional[str] = Field(None, alias='OpenHookUrl')

    post_first_open_only: typing.Optional[bool] = Field(None, alias='PostFirstOpenOnly')

    raw_email_enabled: typing.Optional[bool] = Field(None, alias='RawEmailEnabled')

    smtp_api_activated: typing.Optional[bool] = Field(None, alias='SmtpApiActivated')

    track_links: typing.Optional[Literal["None", "HtmlAndText", "HtmlOnly", "TextOnly"]] = Field(None, alias='TrackLinks')

    track_opens: typing.Optional[bool] = Field(None, alias='TrackOpens')
    class Config:
        arbitrary_types_allowed = True
