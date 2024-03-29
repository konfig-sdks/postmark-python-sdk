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
from postmark_python_sdk.model.template_validation_request import TemplateValidationRequest as TemplateValidationRequestSchema

from postmark_python_sdk.type.standard_postmark_response import StandardPostmarkResponse
from postmark_python_sdk.type.template_validation_request import TemplateValidationRequest

from ...api_client import Dictionary
from postmark_python_sdk.pydantic.template_validation_request import TemplateValidationRequest as TemplateValidationRequestPydantic
from postmark_python_sdk.pydantic.standard_postmark_response import StandardPostmarkResponse as StandardPostmarkResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TemplateValidationRequestSchema


request_body_template_validation_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'serverToken',
]
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
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _validate_template_content_mapped_args(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if html_body is not None:
            _body["HtmlBody"] = html_body
        if inline_css_for_html_test_render is not None:
            _body["InlineCssForHtmlTestRender"] = inline_css_for_html_test_render
        if subject is not None:
            _body["Subject"] = subject
        if test_render_model is not None:
            _body["TestRenderModel"] = test_render_model
        if text_body is not None:
            _body["TextBody"] = text_body
        args.body = _body
        return args

    async def _avalidate_template_content_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Test Template Content
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/templates/validate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_template_validation_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _validate_template_content_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Test Template Content
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/templates/validate',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_template_validation_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class ValidateTemplateContentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avalidate_template_content(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validate_template_content_mapped_args(
            body=body,
            html_body=html_body,
            inline_css_for_html_test_render=inline_css_for_html_test_render,
            subject=subject,
            test_render_model=test_render_model,
            text_body=text_body,
        )
        return await self._avalidate_template_content_oapg(
            body=args.body,
            **kwargs,
        )
    
    def validate_template_content(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validate_template_content_mapped_args(
            body=body,
            html_body=html_body,
            inline_css_for_html_test_render=inline_css_for_html_test_render,
            subject=subject,
            test_render_model=test_render_model,
            text_body=text_body,
        )
        return self._validate_template_content_oapg(
            body=args.body,
        )

class ValidateTemplateContent(BaseApi):

    async def avalidate_template_content(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.avalidate_template_content(
            body=body,
            html_body=html_body,
            inline_css_for_html_test_render=inline_css_for_html_test_render,
            subject=subject,
            test_render_model=test_render_model,
            text_body=text_body,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def validate_template_content(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.validate_template_content(
            body=body,
            html_body=html_body,
            inline_css_for_html_test_render=inline_css_for_html_test_render,
            subject=subject,
            test_render_model=test_render_model,
            text_body=text_body,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validate_template_content_mapped_args(
            body=body,
            html_body=html_body,
            inline_css_for_html_test_render=inline_css_for_html_test_render,
            subject=subject,
            test_render_model=test_render_model,
            text_body=text_body,
        )
        return await self._avalidate_template_content_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        html_body: typing.Optional[str] = None,
        inline_css_for_html_test_render: typing.Optional[bool] = None,
        subject: typing.Optional[str] = None,
        test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        text_body: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validate_template_content_mapped_args(
            body=body,
            html_body=html_body,
            inline_css_for_html_test_render=inline_css_for_html_test_render,
            subject=subject,
            test_render_model=test_render_model,
            text_body=text_body,
        )
        return self._validate_template_content_oapg(
            body=args.body,
        )

