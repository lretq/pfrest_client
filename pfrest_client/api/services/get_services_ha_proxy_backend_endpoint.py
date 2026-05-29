from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ha_proxy_backend_endpoint_response_400 import GetServicesHAProxyBackendEndpointResponse400
from ...models.get_services_ha_proxy_backend_endpoint_response_401 import GetServicesHAProxyBackendEndpointResponse401
from ...models.get_services_ha_proxy_backend_endpoint_response_403 import GetServicesHAProxyBackendEndpointResponse403
from ...models.get_services_ha_proxy_backend_endpoint_response_404 import GetServicesHAProxyBackendEndpointResponse404
from ...models.get_services_ha_proxy_backend_endpoint_response_405 import GetServicesHAProxyBackendEndpointResponse405
from ...models.get_services_ha_proxy_backend_endpoint_response_406 import GetServicesHAProxyBackendEndpointResponse406
from ...models.get_services_ha_proxy_backend_endpoint_response_409 import GetServicesHAProxyBackendEndpointResponse409
from ...models.get_services_ha_proxy_backend_endpoint_response_415 import GetServicesHAProxyBackendEndpointResponse415
from ...models.get_services_ha_proxy_backend_endpoint_response_422 import GetServicesHAProxyBackendEndpointResponse422
from ...models.get_services_ha_proxy_backend_endpoint_response_424 import GetServicesHAProxyBackendEndpointResponse424
from ...models.get_services_ha_proxy_backend_endpoint_response_500 import GetServicesHAProxyBackendEndpointResponse500
from ...models.get_services_ha_proxy_backend_endpoint_response_503 import GetServicesHAProxyBackendEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/haproxy/backend",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesHAProxyBackendEndpointResponse400
    | GetServicesHAProxyBackendEndpointResponse401
    | GetServicesHAProxyBackendEndpointResponse403
    | GetServicesHAProxyBackendEndpointResponse404
    | GetServicesHAProxyBackendEndpointResponse405
    | GetServicesHAProxyBackendEndpointResponse406
    | GetServicesHAProxyBackendEndpointResponse409
    | GetServicesHAProxyBackendEndpointResponse415
    | GetServicesHAProxyBackendEndpointResponse422
    | GetServicesHAProxyBackendEndpointResponse424
    | GetServicesHAProxyBackendEndpointResponse500
    | GetServicesHAProxyBackendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesHAProxyBackendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesHAProxyBackendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesHAProxyBackendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesHAProxyBackendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesHAProxyBackendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesHAProxyBackendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesHAProxyBackendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesHAProxyBackendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesHAProxyBackendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesHAProxyBackendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesHAProxyBackendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesHAProxyBackendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesHAProxyBackendEndpointResponse400
    | GetServicesHAProxyBackendEndpointResponse401
    | GetServicesHAProxyBackendEndpointResponse403
    | GetServicesHAProxyBackendEndpointResponse404
    | GetServicesHAProxyBackendEndpointResponse405
    | GetServicesHAProxyBackendEndpointResponse406
    | GetServicesHAProxyBackendEndpointResponse409
    | GetServicesHAProxyBackendEndpointResponse415
    | GetServicesHAProxyBackendEndpointResponse422
    | GetServicesHAProxyBackendEndpointResponse424
    | GetServicesHAProxyBackendEndpointResponse500
    | GetServicesHAProxyBackendEndpointResponse503
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
    id: int | str,
) -> Response[
    GetServicesHAProxyBackendEndpointResponse400
    | GetServicesHAProxyBackendEndpointResponse401
    | GetServicesHAProxyBackendEndpointResponse403
    | GetServicesHAProxyBackendEndpointResponse404
    | GetServicesHAProxyBackendEndpointResponse405
    | GetServicesHAProxyBackendEndpointResponse406
    | GetServicesHAProxyBackendEndpointResponse409
    | GetServicesHAProxyBackendEndpointResponse415
    | GetServicesHAProxyBackendEndpointResponse422
    | GetServicesHAProxyBackendEndpointResponse424
    | GetServicesHAProxyBackendEndpointResponse500
    | GetServicesHAProxyBackendEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyBackendEndpointResponse400 | GetServicesHAProxyBackendEndpointResponse401 | GetServicesHAProxyBackendEndpointResponse403 | GetServicesHAProxyBackendEndpointResponse404 | GetServicesHAProxyBackendEndpointResponse405 | GetServicesHAProxyBackendEndpointResponse406 | GetServicesHAProxyBackendEndpointResponse409 | GetServicesHAProxyBackendEndpointResponse415 | GetServicesHAProxyBackendEndpointResponse422 | GetServicesHAProxyBackendEndpointResponse424 | GetServicesHAProxyBackendEndpointResponse500 | GetServicesHAProxyBackendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetServicesHAProxyBackendEndpointResponse400
    | GetServicesHAProxyBackendEndpointResponse401
    | GetServicesHAProxyBackendEndpointResponse403
    | GetServicesHAProxyBackendEndpointResponse404
    | GetServicesHAProxyBackendEndpointResponse405
    | GetServicesHAProxyBackendEndpointResponse406
    | GetServicesHAProxyBackendEndpointResponse409
    | GetServicesHAProxyBackendEndpointResponse415
    | GetServicesHAProxyBackendEndpointResponse422
    | GetServicesHAProxyBackendEndpointResponse424
    | GetServicesHAProxyBackendEndpointResponse500
    | GetServicesHAProxyBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyBackendEndpointResponse400 | GetServicesHAProxyBackendEndpointResponse401 | GetServicesHAProxyBackendEndpointResponse403 | GetServicesHAProxyBackendEndpointResponse404 | GetServicesHAProxyBackendEndpointResponse405 | GetServicesHAProxyBackendEndpointResponse406 | GetServicesHAProxyBackendEndpointResponse409 | GetServicesHAProxyBackendEndpointResponse415 | GetServicesHAProxyBackendEndpointResponse422 | GetServicesHAProxyBackendEndpointResponse424 | GetServicesHAProxyBackendEndpointResponse500 | GetServicesHAProxyBackendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    GetServicesHAProxyBackendEndpointResponse400
    | GetServicesHAProxyBackendEndpointResponse401
    | GetServicesHAProxyBackendEndpointResponse403
    | GetServicesHAProxyBackendEndpointResponse404
    | GetServicesHAProxyBackendEndpointResponse405
    | GetServicesHAProxyBackendEndpointResponse406
    | GetServicesHAProxyBackendEndpointResponse409
    | GetServicesHAProxyBackendEndpointResponse415
    | GetServicesHAProxyBackendEndpointResponse422
    | GetServicesHAProxyBackendEndpointResponse424
    | GetServicesHAProxyBackendEndpointResponse500
    | GetServicesHAProxyBackendEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyBackendEndpointResponse400 | GetServicesHAProxyBackendEndpointResponse401 | GetServicesHAProxyBackendEndpointResponse403 | GetServicesHAProxyBackendEndpointResponse404 | GetServicesHAProxyBackendEndpointResponse405 | GetServicesHAProxyBackendEndpointResponse406 | GetServicesHAProxyBackendEndpointResponse409 | GetServicesHAProxyBackendEndpointResponse415 | GetServicesHAProxyBackendEndpointResponse422 | GetServicesHAProxyBackendEndpointResponse424 | GetServicesHAProxyBackendEndpointResponse500 | GetServicesHAProxyBackendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetServicesHAProxyBackendEndpointResponse400
    | GetServicesHAProxyBackendEndpointResponse401
    | GetServicesHAProxyBackendEndpointResponse403
    | GetServicesHAProxyBackendEndpointResponse404
    | GetServicesHAProxyBackendEndpointResponse405
    | GetServicesHAProxyBackendEndpointResponse406
    | GetServicesHAProxyBackendEndpointResponse409
    | GetServicesHAProxyBackendEndpointResponse415
    | GetServicesHAProxyBackendEndpointResponse422
    | GetServicesHAProxyBackendEndpointResponse424
    | GetServicesHAProxyBackendEndpointResponse500
    | GetServicesHAProxyBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyBackendEndpointResponse400 | GetServicesHAProxyBackendEndpointResponse401 | GetServicesHAProxyBackendEndpointResponse403 | GetServicesHAProxyBackendEndpointResponse404 | GetServicesHAProxyBackendEndpointResponse405 | GetServicesHAProxyBackendEndpointResponse406 | GetServicesHAProxyBackendEndpointResponse409 | GetServicesHAProxyBackendEndpointResponse415 | GetServicesHAProxyBackendEndpointResponse422 | GetServicesHAProxyBackendEndpointResponse424 | GetServicesHAProxyBackendEndpointResponse500 | GetServicesHAProxyBackendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
