# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from postmark_python_sdk import schemas  # noqa: F401


class TemplateDetailResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            Active = schemas.BoolSchema
            Alias = schemas.StrSchema
            AssociatedServerId = schemas.IntSchema
            HtmlBody = schemas.StrSchema
            Name = schemas.StrSchema
            Subject = schemas.StrSchema
            TemplateID = schemas.IntSchema
            TextBody = schemas.StrSchema
            __annotations__ = {
                "Active": Active,
                "Alias": Alias,
                "AssociatedServerId": AssociatedServerId,
                "HtmlBody": HtmlBody,
                "Name": Name,
                "Subject": Subject,
                "TemplateID": TemplateID,
                "TextBody": TextBody,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Active"]) -> MetaOapg.properties.Active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Alias"]) -> MetaOapg.properties.Alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssociatedServerId"]) -> MetaOapg.properties.AssociatedServerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HtmlBody"]) -> MetaOapg.properties.HtmlBody: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Subject"]) -> MetaOapg.properties.Subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TemplateID"]) -> MetaOapg.properties.TemplateID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TextBody"]) -> MetaOapg.properties.TextBody: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Active", "Alias", "AssociatedServerId", "HtmlBody", "Name", "Subject", "TemplateID", "TextBody", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Active"]) -> typing.Union[MetaOapg.properties.Active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Alias"]) -> typing.Union[MetaOapg.properties.Alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssociatedServerId"]) -> typing.Union[MetaOapg.properties.AssociatedServerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HtmlBody"]) -> typing.Union[MetaOapg.properties.HtmlBody, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Subject"]) -> typing.Union[MetaOapg.properties.Subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TemplateID"]) -> typing.Union[MetaOapg.properties.TemplateID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TextBody"]) -> typing.Union[MetaOapg.properties.TextBody, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Active", "Alias", "AssociatedServerId", "HtmlBody", "Name", "Subject", "TemplateID", "TextBody", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        Active: typing.Union[MetaOapg.properties.Active, bool, schemas.Unset] = schemas.unset,
        Alias: typing.Union[MetaOapg.properties.Alias, str, schemas.Unset] = schemas.unset,
        AssociatedServerId: typing.Union[MetaOapg.properties.AssociatedServerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        HtmlBody: typing.Union[MetaOapg.properties.HtmlBody, str, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        Subject: typing.Union[MetaOapg.properties.Subject, str, schemas.Unset] = schemas.unset,
        TemplateID: typing.Union[MetaOapg.properties.TemplateID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TextBody: typing.Union[MetaOapg.properties.TextBody, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateDetailResponse':
        return super().__new__(
            cls,
            *args,
            Active=Active,
            Alias=Alias,
            AssociatedServerId=AssociatedServerId,
            HtmlBody=HtmlBody,
            Name=Name,
            Subject=Subject,
            TemplateID=TemplateID,
            TextBody=TextBody,
            _configuration=_configuration,
            **kwargs,
        )
