from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routing_gateway_default_endpoint_response_400 import GetRoutingGatewayDefaultEndpointResponse400
from ...models.get_routing_gateway_default_endpoint_response_401 import GetRoutingGatewayDefaultEndpointResponse401
from ...models.get_routing_gateway_default_endpoint_response_403 import GetRoutingGatewayDefaultEndpointResponse403
from ...models.get_routing_gateway_default_endpoint_response_404 import GetRoutingGatewayDefaultEndpointResponse404
from ...models.get_routing_gateway_default_endpoint_response_405 import GetRoutingGatewayDefaultEndpointResponse405
from ...models.get_routing_gateway_default_endpoint_response_406 import GetRoutingGatewayDefaultEndpointResponse406
from ...models.get_routing_gateway_default_endpoint_response_409 import GetRoutingGatewayDefaultEndpointResponse409
from ...models.get_routing_gateway_default_endpoint_response_415 import GetRoutingGatewayDefaultEndpointResponse415
from ...models.get_routing_gateway_default_endpoint_response_422 import GetRoutingGatewayDefaultEndpointResponse422
from ...models.get_routing_gateway_default_endpoint_response_424 import GetRoutingGatewayDefaultEndpointResponse424
from ...models.get_routing_gateway_default_endpoint_response_500 import GetRoutingGatewayDefaultEndpointResponse500
from ...models.get_routing_gateway_default_endpoint_response_503 import GetRoutingGatewayDefaultEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/routing/gateway/default",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRoutingGatewayDefaultEndpointResponse400
    | GetRoutingGatewayDefaultEndpointResponse401
    | GetRoutingGatewayDefaultEndpointResponse403
    | GetRoutingGatewayDefaultEndpointResponse404
    | GetRoutingGatewayDefaultEndpointResponse405
    | GetRoutingGatewayDefaultEndpointResponse406
    | GetRoutingGatewayDefaultEndpointResponse409
    | GetRoutingGatewayDefaultEndpointResponse415
    | GetRoutingGatewayDefaultEndpointResponse422
    | GetRoutingGatewayDefaultEndpointResponse424
    | GetRoutingGatewayDefaultEndpointResponse500
    | GetRoutingGatewayDefaultEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetRoutingGatewayDefaultEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRoutingGatewayDefaultEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetRoutingGatewayDefaultEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRoutingGatewayDefaultEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetRoutingGatewayDefaultEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetRoutingGatewayDefaultEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetRoutingGatewayDefaultEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetRoutingGatewayDefaultEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetRoutingGatewayDefaultEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetRoutingGatewayDefaultEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetRoutingGatewayDefaultEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetRoutingGatewayDefaultEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRoutingGatewayDefaultEndpointResponse400
    | GetRoutingGatewayDefaultEndpointResponse401
    | GetRoutingGatewayDefaultEndpointResponse403
    | GetRoutingGatewayDefaultEndpointResponse404
    | GetRoutingGatewayDefaultEndpointResponse405
    | GetRoutingGatewayDefaultEndpointResponse406
    | GetRoutingGatewayDefaultEndpointResponse409
    | GetRoutingGatewayDefaultEndpointResponse415
    | GetRoutingGatewayDefaultEndpointResponse422
    | GetRoutingGatewayDefaultEndpointResponse424
    | GetRoutingGatewayDefaultEndpointResponse500
    | GetRoutingGatewayDefaultEndpointResponse503
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
) -> Response[
    GetRoutingGatewayDefaultEndpointResponse400
    | GetRoutingGatewayDefaultEndpointResponse401
    | GetRoutingGatewayDefaultEndpointResponse403
    | GetRoutingGatewayDefaultEndpointResponse404
    | GetRoutingGatewayDefaultEndpointResponse405
    | GetRoutingGatewayDefaultEndpointResponse406
    | GetRoutingGatewayDefaultEndpointResponse409
    | GetRoutingGatewayDefaultEndpointResponse415
    | GetRoutingGatewayDefaultEndpointResponse422
    | GetRoutingGatewayDefaultEndpointResponse424
    | GetRoutingGatewayDefaultEndpointResponse500
    | GetRoutingGatewayDefaultEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoutingGatewayDefaultEndpointResponse400 | GetRoutingGatewayDefaultEndpointResponse401 | GetRoutingGatewayDefaultEndpointResponse403 | GetRoutingGatewayDefaultEndpointResponse404 | GetRoutingGatewayDefaultEndpointResponse405 | GetRoutingGatewayDefaultEndpointResponse406 | GetRoutingGatewayDefaultEndpointResponse409 | GetRoutingGatewayDefaultEndpointResponse415 | GetRoutingGatewayDefaultEndpointResponse422 | GetRoutingGatewayDefaultEndpointResponse424 | GetRoutingGatewayDefaultEndpointResponse500 | GetRoutingGatewayDefaultEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetRoutingGatewayDefaultEndpointResponse400
    | GetRoutingGatewayDefaultEndpointResponse401
    | GetRoutingGatewayDefaultEndpointResponse403
    | GetRoutingGatewayDefaultEndpointResponse404
    | GetRoutingGatewayDefaultEndpointResponse405
    | GetRoutingGatewayDefaultEndpointResponse406
    | GetRoutingGatewayDefaultEndpointResponse409
    | GetRoutingGatewayDefaultEndpointResponse415
    | GetRoutingGatewayDefaultEndpointResponse422
    | GetRoutingGatewayDefaultEndpointResponse424
    | GetRoutingGatewayDefaultEndpointResponse500
    | GetRoutingGatewayDefaultEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoutingGatewayDefaultEndpointResponse400 | GetRoutingGatewayDefaultEndpointResponse401 | GetRoutingGatewayDefaultEndpointResponse403 | GetRoutingGatewayDefaultEndpointResponse404 | GetRoutingGatewayDefaultEndpointResponse405 | GetRoutingGatewayDefaultEndpointResponse406 | GetRoutingGatewayDefaultEndpointResponse409 | GetRoutingGatewayDefaultEndpointResponse415 | GetRoutingGatewayDefaultEndpointResponse422 | GetRoutingGatewayDefaultEndpointResponse424 | GetRoutingGatewayDefaultEndpointResponse500 | GetRoutingGatewayDefaultEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetRoutingGatewayDefaultEndpointResponse400
    | GetRoutingGatewayDefaultEndpointResponse401
    | GetRoutingGatewayDefaultEndpointResponse403
    | GetRoutingGatewayDefaultEndpointResponse404
    | GetRoutingGatewayDefaultEndpointResponse405
    | GetRoutingGatewayDefaultEndpointResponse406
    | GetRoutingGatewayDefaultEndpointResponse409
    | GetRoutingGatewayDefaultEndpointResponse415
    | GetRoutingGatewayDefaultEndpointResponse422
    | GetRoutingGatewayDefaultEndpointResponse424
    | GetRoutingGatewayDefaultEndpointResponse500
    | GetRoutingGatewayDefaultEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoutingGatewayDefaultEndpointResponse400 | GetRoutingGatewayDefaultEndpointResponse401 | GetRoutingGatewayDefaultEndpointResponse403 | GetRoutingGatewayDefaultEndpointResponse404 | GetRoutingGatewayDefaultEndpointResponse405 | GetRoutingGatewayDefaultEndpointResponse406 | GetRoutingGatewayDefaultEndpointResponse409 | GetRoutingGatewayDefaultEndpointResponse415 | GetRoutingGatewayDefaultEndpointResponse422 | GetRoutingGatewayDefaultEndpointResponse424 | GetRoutingGatewayDefaultEndpointResponse500 | GetRoutingGatewayDefaultEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetRoutingGatewayDefaultEndpointResponse400
    | GetRoutingGatewayDefaultEndpointResponse401
    | GetRoutingGatewayDefaultEndpointResponse403
    | GetRoutingGatewayDefaultEndpointResponse404
    | GetRoutingGatewayDefaultEndpointResponse405
    | GetRoutingGatewayDefaultEndpointResponse406
    | GetRoutingGatewayDefaultEndpointResponse409
    | GetRoutingGatewayDefaultEndpointResponse415
    | GetRoutingGatewayDefaultEndpointResponse422
    | GetRoutingGatewayDefaultEndpointResponse424
    | GetRoutingGatewayDefaultEndpointResponse500
    | GetRoutingGatewayDefaultEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoutingGatewayDefaultEndpointResponse400 | GetRoutingGatewayDefaultEndpointResponse401 | GetRoutingGatewayDefaultEndpointResponse403 | GetRoutingGatewayDefaultEndpointResponse404 | GetRoutingGatewayDefaultEndpointResponse405 | GetRoutingGatewayDefaultEndpointResponse406 | GetRoutingGatewayDefaultEndpointResponse409 | GetRoutingGatewayDefaultEndpointResponse415 | GetRoutingGatewayDefaultEndpointResponse422 | GetRoutingGatewayDefaultEndpointResponse424 | GetRoutingGatewayDefaultEndpointResponse500 | GetRoutingGatewayDefaultEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
