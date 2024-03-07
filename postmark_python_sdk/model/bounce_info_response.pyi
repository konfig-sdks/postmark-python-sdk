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


class BounceInfoResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            BouncedAt = schemas.DateTimeSchema
            CanActivate = schemas.BoolSchema
            Content = schemas.StrSchema
            Description = schemas.StrSchema
            Details = schemas.StrSchema
            DumpAvailable = schemas.BoolSchema
            Email = schemas.StrSchema
            ID = schemas.StrSchema
            Inactive = schemas.BoolSchema
            MessageID = schemas.StrSchema
            Name = schemas.StrSchema
            Subject = schemas.StrSchema
            Tag = schemas.StrSchema
            Type = schemas.StrSchema
            TypeCode = schemas.IntSchema
            __annotations__ = {
                "BouncedAt": BouncedAt,
                "CanActivate": CanActivate,
                "Content": Content,
                "Description": Description,
                "Details": Details,
                "DumpAvailable": DumpAvailable,
                "Email": Email,
                "ID": ID,
                "Inactive": Inactive,
                "MessageID": MessageID,
                "Name": Name,
                "Subject": Subject,
                "Tag": Tag,
                "Type": Type,
                "TypeCode": TypeCode,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BouncedAt"]) -> MetaOapg.properties.BouncedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CanActivate"]) -> MetaOapg.properties.CanActivate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Content"]) -> MetaOapg.properties.Content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Details"]) -> MetaOapg.properties.Details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DumpAvailable"]) -> MetaOapg.properties.DumpAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ID"]) -> MetaOapg.properties.ID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Inactive"]) -> MetaOapg.properties.Inactive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MessageID"]) -> MetaOapg.properties.MessageID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Subject"]) -> MetaOapg.properties.Subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Tag"]) -> MetaOapg.properties.Tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TypeCode"]) -> MetaOapg.properties.TypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["BouncedAt", "CanActivate", "Content", "Description", "Details", "DumpAvailable", "Email", "ID", "Inactive", "MessageID", "Name", "Subject", "Tag", "Type", "TypeCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BouncedAt"]) -> typing.Union[MetaOapg.properties.BouncedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CanActivate"]) -> typing.Union[MetaOapg.properties.CanActivate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Content"]) -> typing.Union[MetaOapg.properties.Content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Details"]) -> typing.Union[MetaOapg.properties.Details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DumpAvailable"]) -> typing.Union[MetaOapg.properties.DumpAvailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ID"]) -> typing.Union[MetaOapg.properties.ID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Inactive"]) -> typing.Union[MetaOapg.properties.Inactive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MessageID"]) -> typing.Union[MetaOapg.properties.MessageID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Subject"]) -> typing.Union[MetaOapg.properties.Subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Tag"]) -> typing.Union[MetaOapg.properties.Tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union[MetaOapg.properties.Type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TypeCode"]) -> typing.Union[MetaOapg.properties.TypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["BouncedAt", "CanActivate", "Content", "Description", "Details", "DumpAvailable", "Email", "ID", "Inactive", "MessageID", "Name", "Subject", "Tag", "Type", "TypeCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        BouncedAt: typing.Union[MetaOapg.properties.BouncedAt, str, datetime, schemas.Unset] = schemas.unset,
        CanActivate: typing.Union[MetaOapg.properties.CanActivate, bool, schemas.Unset] = schemas.unset,
        Content: typing.Union[MetaOapg.properties.Content, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, str, schemas.Unset] = schemas.unset,
        Details: typing.Union[MetaOapg.properties.Details, str, schemas.Unset] = schemas.unset,
        DumpAvailable: typing.Union[MetaOapg.properties.DumpAvailable, bool, schemas.Unset] = schemas.unset,
        Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
        ID: typing.Union[MetaOapg.properties.ID, str, schemas.Unset] = schemas.unset,
        Inactive: typing.Union[MetaOapg.properties.Inactive, bool, schemas.Unset] = schemas.unset,
        MessageID: typing.Union[MetaOapg.properties.MessageID, str, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        Subject: typing.Union[MetaOapg.properties.Subject, str, schemas.Unset] = schemas.unset,
        Tag: typing.Union[MetaOapg.properties.Tag, str, schemas.Unset] = schemas.unset,
        Type: typing.Union[MetaOapg.properties.Type, str, schemas.Unset] = schemas.unset,
        TypeCode: typing.Union[MetaOapg.properties.TypeCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BounceInfoResponse':
        return super().__new__(
            cls,
            *args,
            BouncedAt=BouncedAt,
            CanActivate=CanActivate,
            Content=Content,
            Description=Description,
            Details=Details,
            DumpAvailable=DumpAvailable,
            Email=Email,
            ID=ID,
            Inactive=Inactive,
            MessageID=MessageID,
            Name=Name,
            Subject=Subject,
            Tag=Tag,
            Type=Type,
            TypeCode=TypeCode,
            _configuration=_configuration,
            **kwargs,
        )
