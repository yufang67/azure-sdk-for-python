# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._temporary_data_references_operations import build_create_or_get_temporary_data_reference_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TemporaryDataReferencesOperations:
    """TemporaryDataReferencesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_or_get_temporary_data_reference(
        self,
        name: str,
        version: str,
        resource_group_name: str,
        registry_name: str,
        body: "_models.TemporaryDataReferenceRequestDto",
        **kwargs: Any
    ) -> "_models.TemporaryDataReferenceResponseDto":
        """create_or_get_temporary_data_reference.

        :param name:
        :type name: str
        :param version:
        :type version: str
        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param registry_name:
        :type registry_name: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.TemporaryDataReferenceRequestDto
        :keyword api_version: Api Version. The default value is "2021-10-01-dataplanepreview". Note
         that overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemporaryDataReferenceResponseDto, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.TemporaryDataReferenceResponseDto
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemporaryDataReferenceResponseDto"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-10-01-dataplanepreview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(body, 'TemporaryDataReferenceRequestDto')

        request = build_create_or_get_temporary_data_reference_request(
            name=name,
            version=version,
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_get_temporary_data_reference.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemporaryDataReferenceResponseDto', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_get_temporary_data_reference.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}/tempdatarefs/{name}/versions/{version}'}  # type: ignore
