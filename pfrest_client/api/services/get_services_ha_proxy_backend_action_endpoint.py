from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ha_proxy_backend_action_endpoint_response_400 import (
    GetServicesHAProxyBackendActionEndpointResponse400,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_401 import (
    GetServicesHAProxyBackendActionEndpointResponse401,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_403 import (
    GetServicesHAProxyBackendActionEndpointResponse403,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_404 import (
    GetServicesHAProxyBackendActionEndpointResponse404,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_405 import (
    GetServicesHAProxyBackendActionEndpointResponse405,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_406 import (
    GetServicesHAProxyBackendActionEndpointResponse406,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_409 import (
    GetServicesHAProxyBackendActionEndpointResponse409,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_415 import (
    GetServicesHAProxyBackendActionEndpointResponse415,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_422 import (
    GetServicesHAProxyBackendActionEndpointResponse422,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_424 import (
    GetServicesHAProxyBackendActionEndpointResponse424,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_500 import (
    GetServicesHAProxyBackendActionEndpointResponse500,
)
from ...models.get_services_ha_proxy_backend_action_endpoint_response_503 import (
    GetServicesHAProxyBackendActionEndpointResponse503,
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
        "method": "get",
        "url": "/api/v2/services/haproxy/backend/action",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesHAProxyBackendActionEndpointResponse400
    | GetServicesHAProxyBackendActionEndpointResponse401
    | GetServicesHAProxyBackendActionEndpointResponse403
    | GetServicesHAProxyBackendActionEndpointResponse404
    | GetServicesHAProxyBackendActionEndpointResponse405
    | GetServicesHAProxyBackendActionEndpointResponse406
    | GetServicesHAProxyBackendActionEndpointResponse409
    | GetServicesHAProxyBackendActionEndpointResponse415
    | GetServicesHAProxyBackendActionEndpointResponse422
    | GetServicesHAProxyBackendActionEndpointResponse424
    | GetServicesHAProxyBackendActionEndpointResponse500
    | GetServicesHAProxyBackendActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesHAProxyBackendActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesHAProxyBackendActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesHAProxyBackendActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesHAProxyBackendActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesHAProxyBackendActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesHAProxyBackendActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesHAProxyBackendActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesHAProxyBackendActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesHAProxyBackendActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesHAProxyBackendActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesHAProxyBackendActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesHAProxyBackendActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesHAProxyBackendActionEndpointResponse400
    | GetServicesHAProxyBackendActionEndpointResponse401
    | GetServicesHAProxyBackendActionEndpointResponse403
    | GetServicesHAProxyBackendActionEndpointResponse404
    | GetServicesHAProxyBackendActionEndpointResponse405
    | GetServicesHAProxyBackendActionEndpointResponse406
    | GetServicesHAProxyBackendActionEndpointResponse409
    | GetServicesHAProxyBackendActionEndpointResponse415
    | GetServicesHAProxyBackendActionEndpointResponse422
    | GetServicesHAProxyBackendActionEndpointResponse424
    | GetServicesHAProxyBackendActionEndpointResponse500
    | GetServicesHAProxyBackendActionEndpointResponse503
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
    GetServicesHAProxyBackendActionEndpointResponse400
    | GetServicesHAProxyBackendActionEndpointResponse401
    | GetServicesHAProxyBackendActionEndpointResponse403
    | GetServicesHAProxyBackendActionEndpointResponse404
    | GetServicesHAProxyBackendActionEndpointResponse405
    | GetServicesHAProxyBackendActionEndpointResponse406
    | GetServicesHAProxyBackendActionEndpointResponse409
    | GetServicesHAProxyBackendActionEndpointResponse415
    | GetServicesHAProxyBackendActionEndpointResponse422
    | GetServicesHAProxyBackendActionEndpointResponse424
    | GetServicesHAProxyBackendActionEndpointResponse500
    | GetServicesHAProxyBackendActionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyBackendActionEndpointResponse400 | GetServicesHAProxyBackendActionEndpointResponse401 | GetServicesHAProxyBackendActionEndpointResponse403 | GetServicesHAProxyBackendActionEndpointResponse404 | GetServicesHAProxyBackendActionEndpointResponse405 | GetServicesHAProxyBackendActionEndpointResponse406 | GetServicesHAProxyBackendActionEndpointResponse409 | GetServicesHAProxyBackendActionEndpointResponse415 | GetServicesHAProxyBackendActionEndpointResponse422 | GetServicesHAProxyBackendActionEndpointResponse424 | GetServicesHAProxyBackendActionEndpointResponse500 | GetServicesHAProxyBackendActionEndpointResponse503]
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
    GetServicesHAProxyBackendActionEndpointResponse400
    | GetServicesHAProxyBackendActionEndpointResponse401
    | GetServicesHAProxyBackendActionEndpointResponse403
    | GetServicesHAProxyBackendActionEndpointResponse404
    | GetServicesHAProxyBackendActionEndpointResponse405
    | GetServicesHAProxyBackendActionEndpointResponse406
    | GetServicesHAProxyBackendActionEndpointResponse409
    | GetServicesHAProxyBackendActionEndpointResponse415
    | GetServicesHAProxyBackendActionEndpointResponse422
    | GetServicesHAProxyBackendActionEndpointResponse424
    | GetServicesHAProxyBackendActionEndpointResponse500
    | GetServicesHAProxyBackendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyBackendActionEndpointResponse400 | GetServicesHAProxyBackendActionEndpointResponse401 | GetServicesHAProxyBackendActionEndpointResponse403 | GetServicesHAProxyBackendActionEndpointResponse404 | GetServicesHAProxyBackendActionEndpointResponse405 | GetServicesHAProxyBackendActionEndpointResponse406 | GetServicesHAProxyBackendActionEndpointResponse409 | GetServicesHAProxyBackendActionEndpointResponse415 | GetServicesHAProxyBackendActionEndpointResponse422 | GetServicesHAProxyBackendActionEndpointResponse424 | GetServicesHAProxyBackendActionEndpointResponse500 | GetServicesHAProxyBackendActionEndpointResponse503
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
    GetServicesHAProxyBackendActionEndpointResponse400
    | GetServicesHAProxyBackendActionEndpointResponse401
    | GetServicesHAProxyBackendActionEndpointResponse403
    | GetServicesHAProxyBackendActionEndpointResponse404
    | GetServicesHAProxyBackendActionEndpointResponse405
    | GetServicesHAProxyBackendActionEndpointResponse406
    | GetServicesHAProxyBackendActionEndpointResponse409
    | GetServicesHAProxyBackendActionEndpointResponse415
    | GetServicesHAProxyBackendActionEndpointResponse422
    | GetServicesHAProxyBackendActionEndpointResponse424
    | GetServicesHAProxyBackendActionEndpointResponse500
    | GetServicesHAProxyBackendActionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyBackendActionEndpointResponse400 | GetServicesHAProxyBackendActionEndpointResponse401 | GetServicesHAProxyBackendActionEndpointResponse403 | GetServicesHAProxyBackendActionEndpointResponse404 | GetServicesHAProxyBackendActionEndpointResponse405 | GetServicesHAProxyBackendActionEndpointResponse406 | GetServicesHAProxyBackendActionEndpointResponse409 | GetServicesHAProxyBackendActionEndpointResponse415 | GetServicesHAProxyBackendActionEndpointResponse422 | GetServicesHAProxyBackendActionEndpointResponse424 | GetServicesHAProxyBackendActionEndpointResponse500 | GetServicesHAProxyBackendActionEndpointResponse503]
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
    GetServicesHAProxyBackendActionEndpointResponse400
    | GetServicesHAProxyBackendActionEndpointResponse401
    | GetServicesHAProxyBackendActionEndpointResponse403
    | GetServicesHAProxyBackendActionEndpointResponse404
    | GetServicesHAProxyBackendActionEndpointResponse405
    | GetServicesHAProxyBackendActionEndpointResponse406
    | GetServicesHAProxyBackendActionEndpointResponse409
    | GetServicesHAProxyBackendActionEndpointResponse415
    | GetServicesHAProxyBackendActionEndpointResponse422
    | GetServicesHAProxyBackendActionEndpointResponse424
    | GetServicesHAProxyBackendActionEndpointResponse500
    | GetServicesHAProxyBackendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyBackendActionEndpointResponse400 | GetServicesHAProxyBackendActionEndpointResponse401 | GetServicesHAProxyBackendActionEndpointResponse403 | GetServicesHAProxyBackendActionEndpointResponse404 | GetServicesHAProxyBackendActionEndpointResponse405 | GetServicesHAProxyBackendActionEndpointResponse406 | GetServicesHAProxyBackendActionEndpointResponse409 | GetServicesHAProxyBackendActionEndpointResponse415 | GetServicesHAProxyBackendActionEndpointResponse422 | GetServicesHAProxyBackendActionEndpointResponse424 | GetServicesHAProxyBackendActionEndpointResponse500 | GetServicesHAProxyBackendActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
