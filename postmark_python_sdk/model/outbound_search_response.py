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


class OutboundSearchResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class Messages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OutboundMessageDetail']:
                        return OutboundMessageDetail
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OutboundMessageDetail'], typing.List['OutboundMessageDetail']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Messages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OutboundMessageDetail':
                    return super().__getitem__(i)
            TotalCount = schemas.IntSchema
            __annotations__ = {
                "Messages": Messages,
                "TotalCount": TotalCount,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Messages"]) -> MetaOapg.properties.Messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalCount"]) -> MetaOapg.properties.TotalCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Messages", "TotalCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Messages"]) -> typing.Union[MetaOapg.properties.Messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalCount"]) -> typing.Union[MetaOapg.properties.TotalCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Messages", "TotalCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        Messages: typing.Union[MetaOapg.properties.Messages, list, tuple, schemas.Unset] = schemas.unset,
        TotalCount: typing.Union[MetaOapg.properties.TotalCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OutboundSearchResponse':
        return super().__new__(
            cls,
            *args,
            Messages=Messages,
            TotalCount=TotalCount,
            _configuration=_configuration,
            **kwargs,
        )

from postmark_python_sdk.model.outbound_message_detail import OutboundMessageDetail
