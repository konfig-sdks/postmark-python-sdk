# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from postmark_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from postmark_python_sdk.api_response import AsyncGeneratorResponse
from postmark_python_sdk import api_client, exceptions
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

from postmark_python_sdk.model.standard_postmark_response import StandardPostmarkResponse as StandardPostmarkResponseSchema

from postmark_python_sdk.type.standard_postmark_response import StandardPostmarkResponse

from ...api_client import Dictionary
from postmark_python_sdk.pydantic.standard_postmark_response import StandardPostmarkResponse as StandardPostmarkResponsePydantic

# Query params
CountSchema = schemas.IntSchema
OffsetSchema = schemas.IntSchema
RecipientSchema = schemas.StrSchema
TagSchema = schemas.StrSchema
ClientNameSchema = schemas.StrSchema
ClientCompanySchema = schemas.StrSchema
ClientFamilySchema = schemas.StrSchema
OsNameSchema = schemas.StrSchema
OsFamilySchema = schemas.StrSchema
OsCompanySchema = schemas.StrSchema
PlatformSchema = schemas.StrSchema
CountrySchema = schemas.StrSchema
RegionSchema = schemas.StrSchema
CitySchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'count': typing.Union[CountSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'recipient': typing.Union[RecipientSchema, str, ],
        'tag': typing.Union[TagSchema, str, ],
        'client_name': typing.Union[ClientNameSchema, str, ],
        'client_company': typing.Union[ClientCompanySchema, str, ],
        'client_family': typing.Union[ClientFamilySchema, str, ],
        'os_name': typing.Union[OsNameSchema, str, ],
        'os_family': typing.Union[OsFamilySchema, str, ],
        'os_company': typing.Union[OsCompanySchema, str, ],
        'platform': typing.Union[PlatformSchema, str, ],
        'country': typing.Union[CountrySchema, str, ],
        'region': typing.Union[RegionSchema, str, ],
        'city': typing.Union[CitySchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_count = api_client.QueryParameter(
    name="count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
    required=True,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    required=True,
    explode=True,
)
request_query_recipient = api_client.QueryParameter(
    name="recipient",
    style=api_client.ParameterStyle.FORM,
    schema=RecipientSchema,
    explode=True,
)
request_query_tag = api_client.QueryParameter(
    name="tag",
    style=api_client.ParameterStyle.FORM,
    schema=TagSchema,
    explode=True,
)
request_query_client_name = api_client.QueryParameter(
    name="client_name",
    style=api_client.ParameterStyle.FORM,
    schema=ClientNameSchema,
    explode=True,
)
request_query_client_company = api_client.QueryParameter(
    name="client_company",
    style=api_client.ParameterStyle.FORM,
    schema=ClientCompanySchema,
    explode=True,
)
request_query_client_family = api_client.QueryParameter(
    name="client_family",
    style=api_client.ParameterStyle.FORM,
    schema=ClientFamilySchema,
    explode=True,
)
request_query_os_name = api_client.QueryParameter(
    name="os_name",
    style=api_client.ParameterStyle.FORM,
    schema=OsNameSchema,
    explode=True,
)
request_query_os_family = api_client.QueryParameter(
    name="os_family",
    style=api_client.ParameterStyle.FORM,
    schema=OsFamilySchema,
    explode=True,
)
request_query_os_company = api_client.QueryParameter(
    name="os_company",
    style=api_client.ParameterStyle.FORM,
    schema=OsCompanySchema,
    explode=True,
)
request_query_platform = api_client.QueryParameter(
    name="platform",
    style=api_client.ParameterStyle.FORM,
    schema=PlatformSchema,
    explode=True,
)
request_query_country = api_client.QueryParameter(
    name="country",
    style=api_client.ParameterStyle.FORM,
    schema=CountrySchema,
    explode=True,
)
request_query_region = api_client.QueryParameter(
    name="region",
    style=api_client.ParameterStyle.FORM,
    schema=RegionSchema,
    explode=True,
)
request_query_city = api_client.QueryParameter(
    name="city",
    style=api_client.ParameterStyle.FORM,
    schema=CitySchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = StandardPostmarkResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: StandardPostmarkResponse


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: StandardPostmarkResponse


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_opens_for_outbound_mapped_args(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if count is not None:
            _query_params["count"] = count
        if offset is not None:
            _query_params["offset"] = offset
        if recipient is not None:
            _query_params["recipient"] = recipient
        if tag is not None:
            _query_params["tag"] = tag
        if client_name is not None:
            _query_params["client_name"] = client_name
        if client_company is not None:
            _query_params["client_company"] = client_company
        if client_family is not None:
            _query_params["client_family"] = client_family
        if os_name is not None:
            _query_params["os_name"] = os_name
        if os_family is not None:
            _query_params["os_family"] = os_family
        if os_company is not None:
            _query_params["os_company"] = os_company
        if platform is not None:
            _query_params["platform"] = platform
        if country is not None:
            _query_params["country"] = country
        if region is not None:
            _query_params["region"] = region
        if city is not None:
            _query_params["city"] = city
        args.query = _query_params
        return args

    async def _alist_opens_for_outbound_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Opens for all messages
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_count,
            request_query_offset,
            request_query_recipient,
            request_query_tag,
            request_query_client_name,
            request_query_client_company,
            request_query_client_family,
            request_query_os_name,
            request_query_os_family,
            request_query_os_company,
            request_query_platform,
            request_query_country,
            request_query_region,
            request_query_city,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/messages/outbound/opens',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_opens_for_outbound_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Opens for all messages
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_count,
            request_query_offset,
            request_query_recipient,
            request_query_tag,
            request_query_client_name,
            request_query_client_company,
            request_query_client_family,
            request_query_os_name,
            request_query_os_family,
            request_query_os_company,
            request_query_platform,
            request_query_country,
            request_query_region,
            request_query_city,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/messages/outbound/opens',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListOpensForOutboundRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_opens_for_outbound(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_opens_for_outbound_mapped_args(
            count=count,
            offset=offset,
            recipient=recipient,
            tag=tag,
            client_name=client_name,
            client_company=client_company,
            client_family=client_family,
            os_name=os_name,
            os_family=os_family,
            os_company=os_company,
            platform=platform,
            country=country,
            region=region,
            city=city,
        )
        return await self._alist_opens_for_outbound_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_opens_for_outbound(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_opens_for_outbound_mapped_args(
            count=count,
            offset=offset,
            recipient=recipient,
            tag=tag,
            client_name=client_name,
            client_company=client_company,
            client_family=client_family,
            os_name=os_name,
            os_family=os_family,
            os_company=os_company,
            platform=platform,
            country=country,
            region=region,
            city=city,
        )
        return self._list_opens_for_outbound_oapg(
            query_params=args.query,
        )

class ListOpensForOutbound(BaseApi):

    async def alist_opens_for_outbound(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.alist_opens_for_outbound(
            count=count,
            offset=offset,
            recipient=recipient,
            tag=tag,
            client_name=client_name,
            client_company=client_company,
            client_family=client_family,
            os_name=os_name,
            os_family=os_family,
            os_company=os_company,
            platform=platform,
            country=country,
            region=region,
            city=city,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def list_opens_for_outbound(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.list_opens_for_outbound(
            count=count,
            offset=offset,
            recipient=recipient,
            tag=tag,
            client_name=client_name,
            client_company=client_company,
            client_family=client_family,
            os_name=os_name,
            os_family=os_family,
            os_company=os_company,
            platform=platform,
            country=country,
            region=region,
            city=city,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_opens_for_outbound_mapped_args(
            count=count,
            offset=offset,
            recipient=recipient,
            tag=tag,
            client_name=client_name,
            client_company=client_company,
            client_family=client_family,
            os_name=os_name,
            os_family=os_family,
            os_company=os_company,
            platform=platform,
            country=country,
            region=region,
            city=city,
        )
        return await self._alist_opens_for_outbound_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        count: int,
        offset: int,
        recipient: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        client_name: typing.Optional[str] = None,
        client_company: typing.Optional[str] = None,
        client_family: typing.Optional[str] = None,
        os_name: typing.Optional[str] = None,
        os_family: typing.Optional[str] = None,
        os_company: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_opens_for_outbound_mapped_args(
            count=count,
            offset=offset,
            recipient=recipient,
            tag=tag,
            client_name=client_name,
            client_company=client_company,
            client_family=client_family,
            os_name=os_name,
            os_family=os_family,
            os_company=os_company,
            platform=platform,
            country=country,
            region=region,
            city=city,
        )
        return self._list_opens_for_outbound_oapg(
            query_params=args.query,
        )
