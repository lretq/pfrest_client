from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_400 import (
    DeleteServicesHAProxyBackendServerEndpointResponse400,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_401 import (
    DeleteServicesHAProxyBackendServerEndpointResponse401,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_403 import (
    DeleteServicesHAProxyBackendServerEndpointResponse403,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_404 import (
    DeleteServicesHAProxyBackendServerEndpointResponse404,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_405 import (
    DeleteServicesHAProxyBackendServerEndpointResponse405,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_406 import (
    DeleteServicesHAProxyBackendServerEndpointResponse406,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_409 import (
    DeleteServicesHAProxyBackendServerEndpointResponse409,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_415 import (
    DeleteServicesHAProxyBackendServerEndpointResponse415,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_422 import (
    DeleteServicesHAProxyBackendServerEndpointResponse422,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_424 import (
    DeleteServicesHAProxyBackendServerEndpointResponse424,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_500 import (
    DeleteServicesHAProxyBackendServerEndpointResponse500,
)
from ...models.delete_services_ha_proxy_backend_server_endpoint_response_503 import (
    DeleteServicesHAProxyBackendServerEndpointResponse503,
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
        "url": "/api/v2/services/haproxy/backend/server",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxyBackendServerEndpointResponse400
    | DeleteServicesHAProxyBackendServerEndpointResponse401
    | DeleteServicesHAProxyBackendServerEndpointResponse403
    | DeleteServicesHAProxyBackendServerEndpointResponse404
    | DeleteServicesHAProxyBackendServerEndpointResponse405
    | DeleteServicesHAProxyBackendServerEndpointResponse406
    | DeleteServicesHAProxyBackendServerEndpointResponse409
    | DeleteServicesHAProxyBackendServerEndpointResponse415
    | DeleteServicesHAProxyBackendServerEndpointResponse422
    | DeleteServicesHAProxyBackendServerEndpointResponse424
    | DeleteServicesHAProxyBackendServerEndpointResponse500
    | DeleteServicesHAProxyBackendServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxyBackendServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxyBackendServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxyBackendServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxyBackendServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxyBackendServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxyBackendServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxyBackendServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxyBackendServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxyBackendServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxyBackendServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxyBackendServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxyBackendServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxyBackendServerEndpointResponse400
    | DeleteServicesHAProxyBackendServerEndpointResponse401
    | DeleteServicesHAProxyBackendServerEndpointResponse403
    | DeleteServicesHAProxyBackendServerEndpointResponse404
    | DeleteServicesHAProxyBackendServerEndpointResponse405
    | DeleteServicesHAProxyBackendServerEndpointResponse406
    | DeleteServicesHAProxyBackendServerEndpointResponse409
    | DeleteServicesHAProxyBackendServerEndpointResponse415
    | DeleteServicesHAProxyBackendServerEndpointResponse422
    | DeleteServicesHAProxyBackendServerEndpointResponse424
    | DeleteServicesHAProxyBackendServerEndpointResponse500
    | DeleteServicesHAProxyBackendServerEndpointResponse503
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
    DeleteServicesHAProxyBackendServerEndpointResponse400
    | DeleteServicesHAProxyBackendServerEndpointResponse401
    | DeleteServicesHAProxyBackendServerEndpointResponse403
    | DeleteServicesHAProxyBackendServerEndpointResponse404
    | DeleteServicesHAProxyBackendServerEndpointResponse405
    | DeleteServicesHAProxyBackendServerEndpointResponse406
    | DeleteServicesHAProxyBackendServerEndpointResponse409
    | DeleteServicesHAProxyBackendServerEndpointResponse415
    | DeleteServicesHAProxyBackendServerEndpointResponse422
    | DeleteServicesHAProxyBackendServerEndpointResponse424
    | DeleteServicesHAProxyBackendServerEndpointResponse500
    | DeleteServicesHAProxyBackendServerEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyBackendServerEndpointResponse400 | DeleteServicesHAProxyBackendServerEndpointResponse401 | DeleteServicesHAProxyBackendServerEndpointResponse403 | DeleteServicesHAProxyBackendServerEndpointResponse404 | DeleteServicesHAProxyBackendServerEndpointResponse405 | DeleteServicesHAProxyBackendServerEndpointResponse406 | DeleteServicesHAProxyBackendServerEndpointResponse409 | DeleteServicesHAProxyBackendServerEndpointResponse415 | DeleteServicesHAProxyBackendServerEndpointResponse422 | DeleteServicesHAProxyBackendServerEndpointResponse424 | DeleteServicesHAProxyBackendServerEndpointResponse500 | DeleteServicesHAProxyBackendServerEndpointResponse503]
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
    DeleteServicesHAProxyBackendServerEndpointResponse400
    | DeleteServicesHAProxyBackendServerEndpointResponse401
    | DeleteServicesHAProxyBackendServerEndpointResponse403
    | DeleteServicesHAProxyBackendServerEndpointResponse404
    | DeleteServicesHAProxyBackendServerEndpointResponse405
    | DeleteServicesHAProxyBackendServerEndpointResponse406
    | DeleteServicesHAProxyBackendServerEndpointResponse409
    | DeleteServicesHAProxyBackendServerEndpointResponse415
    | DeleteServicesHAProxyBackendServerEndpointResponse422
    | DeleteServicesHAProxyBackendServerEndpointResponse424
    | DeleteServicesHAProxyBackendServerEndpointResponse500
    | DeleteServicesHAProxyBackendServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyBackendServerEndpointResponse400 | DeleteServicesHAProxyBackendServerEndpointResponse401 | DeleteServicesHAProxyBackendServerEndpointResponse403 | DeleteServicesHAProxyBackendServerEndpointResponse404 | DeleteServicesHAProxyBackendServerEndpointResponse405 | DeleteServicesHAProxyBackendServerEndpointResponse406 | DeleteServicesHAProxyBackendServerEndpointResponse409 | DeleteServicesHAProxyBackendServerEndpointResponse415 | DeleteServicesHAProxyBackendServerEndpointResponse422 | DeleteServicesHAProxyBackendServerEndpointResponse424 | DeleteServicesHAProxyBackendServerEndpointResponse500 | DeleteServicesHAProxyBackendServerEndpointResponse503
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
    DeleteServicesHAProxyBackendServerEndpointResponse400
    | DeleteServicesHAProxyBackendServerEndpointResponse401
    | DeleteServicesHAProxyBackendServerEndpointResponse403
    | DeleteServicesHAProxyBackendServerEndpointResponse404
    | DeleteServicesHAProxyBackendServerEndpointResponse405
    | DeleteServicesHAProxyBackendServerEndpointResponse406
    | DeleteServicesHAProxyBackendServerEndpointResponse409
    | DeleteServicesHAProxyBackendServerEndpointResponse415
    | DeleteServicesHAProxyBackendServerEndpointResponse422
    | DeleteServicesHAProxyBackendServerEndpointResponse424
    | DeleteServicesHAProxyBackendServerEndpointResponse500
    | DeleteServicesHAProxyBackendServerEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyBackendServerEndpointResponse400 | DeleteServicesHAProxyBackendServerEndpointResponse401 | DeleteServicesHAProxyBackendServerEndpointResponse403 | DeleteServicesHAProxyBackendServerEndpointResponse404 | DeleteServicesHAProxyBackendServerEndpointResponse405 | DeleteServicesHAProxyBackendServerEndpointResponse406 | DeleteServicesHAProxyBackendServerEndpointResponse409 | DeleteServicesHAProxyBackendServerEndpointResponse415 | DeleteServicesHAProxyBackendServerEndpointResponse422 | DeleteServicesHAProxyBackendServerEndpointResponse424 | DeleteServicesHAProxyBackendServerEndpointResponse500 | DeleteServicesHAProxyBackendServerEndpointResponse503]
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
    DeleteServicesHAProxyBackendServerEndpointResponse400
    | DeleteServicesHAProxyBackendServerEndpointResponse401
    | DeleteServicesHAProxyBackendServerEndpointResponse403
    | DeleteServicesHAProxyBackendServerEndpointResponse404
    | DeleteServicesHAProxyBackendServerEndpointResponse405
    | DeleteServicesHAProxyBackendServerEndpointResponse406
    | DeleteServicesHAProxyBackendServerEndpointResponse409
    | DeleteServicesHAProxyBackendServerEndpointResponse415
    | DeleteServicesHAProxyBackendServerEndpointResponse422
    | DeleteServicesHAProxyBackendServerEndpointResponse424
    | DeleteServicesHAProxyBackendServerEndpointResponse500
    | DeleteServicesHAProxyBackendServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyBackendServerEndpointResponse400 | DeleteServicesHAProxyBackendServerEndpointResponse401 | DeleteServicesHAProxyBackendServerEndpointResponse403 | DeleteServicesHAProxyBackendServerEndpointResponse404 | DeleteServicesHAProxyBackendServerEndpointResponse405 | DeleteServicesHAProxyBackendServerEndpointResponse406 | DeleteServicesHAProxyBackendServerEndpointResponse409 | DeleteServicesHAProxyBackendServerEndpointResponse415 | DeleteServicesHAProxyBackendServerEndpointResponse422 | DeleteServicesHAProxyBackendServerEndpointResponse424 | DeleteServicesHAProxyBackendServerEndpointResponse500 | DeleteServicesHAProxyBackendServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
