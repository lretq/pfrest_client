from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_400 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_401 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse401,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_403 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse403,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_404 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse404,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_405 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse405,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_406 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse406,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_409 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse409,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_415 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse415,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_422 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse422,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_424 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse424,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_500 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse500,
)
from ...models.delete_services_ha_proxy_backend_error_file_endpoint_response_503 import (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/haproxy/backend/error_file",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse401
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse403
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse404
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse405
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse406
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse409
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse415
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse422
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse424
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse500
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxyBackendErrorFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxyBackendErrorFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxyBackendErrorFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxyBackendErrorFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxyBackendErrorFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxyBackendErrorFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxyBackendErrorFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxyBackendErrorFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxyBackendErrorFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxyBackendErrorFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxyBackendErrorFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxyBackendErrorFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse401
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse403
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse404
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse405
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse406
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse409
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse415
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse422
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse424
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse500
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse401
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse403
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse404
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse405
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse406
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse409
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse415
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse422
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse424
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse500
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyBackendErrorFileEndpointResponse400 | DeleteServicesHAProxyBackendErrorFileEndpointResponse401 | DeleteServicesHAProxyBackendErrorFileEndpointResponse403 | DeleteServicesHAProxyBackendErrorFileEndpointResponse404 | DeleteServicesHAProxyBackendErrorFileEndpointResponse405 | DeleteServicesHAProxyBackendErrorFileEndpointResponse406 | DeleteServicesHAProxyBackendErrorFileEndpointResponse409 | DeleteServicesHAProxyBackendErrorFileEndpointResponse415 | DeleteServicesHAProxyBackendErrorFileEndpointResponse422 | DeleteServicesHAProxyBackendErrorFileEndpointResponse424 | DeleteServicesHAProxyBackendErrorFileEndpointResponse500 | DeleteServicesHAProxyBackendErrorFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse401
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse403
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse404
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse405
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse406
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse409
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse415
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse422
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse424
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse500
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyBackendErrorFileEndpointResponse400 | DeleteServicesHAProxyBackendErrorFileEndpointResponse401 | DeleteServicesHAProxyBackendErrorFileEndpointResponse403 | DeleteServicesHAProxyBackendErrorFileEndpointResponse404 | DeleteServicesHAProxyBackendErrorFileEndpointResponse405 | DeleteServicesHAProxyBackendErrorFileEndpointResponse406 | DeleteServicesHAProxyBackendErrorFileEndpointResponse409 | DeleteServicesHAProxyBackendErrorFileEndpointResponse415 | DeleteServicesHAProxyBackendErrorFileEndpointResponse422 | DeleteServicesHAProxyBackendErrorFileEndpointResponse424 | DeleteServicesHAProxyBackendErrorFileEndpointResponse500 | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse401
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse403
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse404
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse405
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse406
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse409
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse415
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse422
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse424
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse500
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyBackendErrorFileEndpointResponse400 | DeleteServicesHAProxyBackendErrorFileEndpointResponse401 | DeleteServicesHAProxyBackendErrorFileEndpointResponse403 | DeleteServicesHAProxyBackendErrorFileEndpointResponse404 | DeleteServicesHAProxyBackendErrorFileEndpointResponse405 | DeleteServicesHAProxyBackendErrorFileEndpointResponse406 | DeleteServicesHAProxyBackendErrorFileEndpointResponse409 | DeleteServicesHAProxyBackendErrorFileEndpointResponse415 | DeleteServicesHAProxyBackendErrorFileEndpointResponse422 | DeleteServicesHAProxyBackendErrorFileEndpointResponse424 | DeleteServicesHAProxyBackendErrorFileEndpointResponse500 | DeleteServicesHAProxyBackendErrorFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesHAProxyBackendErrorFileEndpointResponse400
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse401
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse403
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse404
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse405
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse406
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse409
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse415
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse422
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse424
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse500
    | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyBackendErrorFileEndpointResponse400 | DeleteServicesHAProxyBackendErrorFileEndpointResponse401 | DeleteServicesHAProxyBackendErrorFileEndpointResponse403 | DeleteServicesHAProxyBackendErrorFileEndpointResponse404 | DeleteServicesHAProxyBackendErrorFileEndpointResponse405 | DeleteServicesHAProxyBackendErrorFileEndpointResponse406 | DeleteServicesHAProxyBackendErrorFileEndpointResponse409 | DeleteServicesHAProxyBackendErrorFileEndpointResponse415 | DeleteServicesHAProxyBackendErrorFileEndpointResponse422 | DeleteServicesHAProxyBackendErrorFileEndpointResponse424 | DeleteServicesHAProxyBackendErrorFileEndpointResponse500 | DeleteServicesHAProxyBackendErrorFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
