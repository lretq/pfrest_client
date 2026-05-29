from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routing_gateway_group_endpoint_response_400 import GetRoutingGatewayGroupEndpointResponse400
from ...models.get_routing_gateway_group_endpoint_response_401 import GetRoutingGatewayGroupEndpointResponse401
from ...models.get_routing_gateway_group_endpoint_response_403 import GetRoutingGatewayGroupEndpointResponse403
from ...models.get_routing_gateway_group_endpoint_response_404 import GetRoutingGatewayGroupEndpointResponse404
from ...models.get_routing_gateway_group_endpoint_response_405 import GetRoutingGatewayGroupEndpointResponse405
from ...models.get_routing_gateway_group_endpoint_response_406 import GetRoutingGatewayGroupEndpointResponse406
from ...models.get_routing_gateway_group_endpoint_response_409 import GetRoutingGatewayGroupEndpointResponse409
from ...models.get_routing_gateway_group_endpoint_response_415 import GetRoutingGatewayGroupEndpointResponse415
from ...models.get_routing_gateway_group_endpoint_response_422 import GetRoutingGatewayGroupEndpointResponse422
from ...models.get_routing_gateway_group_endpoint_response_424 import GetRoutingGatewayGroupEndpointResponse424
from ...models.get_routing_gateway_group_endpoint_response_500 import GetRoutingGatewayGroupEndpointResponse500
from ...models.get_routing_gateway_group_endpoint_response_503 import GetRoutingGatewayGroupEndpointResponse503
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
        "url": "/api/v2/routing/gateway/group",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRoutingGatewayGroupEndpointResponse400
    | GetRoutingGatewayGroupEndpointResponse401
    | GetRoutingGatewayGroupEndpointResponse403
    | GetRoutingGatewayGroupEndpointResponse404
    | GetRoutingGatewayGroupEndpointResponse405
    | GetRoutingGatewayGroupEndpointResponse406
    | GetRoutingGatewayGroupEndpointResponse409
    | GetRoutingGatewayGroupEndpointResponse415
    | GetRoutingGatewayGroupEndpointResponse422
    | GetRoutingGatewayGroupEndpointResponse424
    | GetRoutingGatewayGroupEndpointResponse500
    | GetRoutingGatewayGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetRoutingGatewayGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRoutingGatewayGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetRoutingGatewayGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRoutingGatewayGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetRoutingGatewayGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetRoutingGatewayGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetRoutingGatewayGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetRoutingGatewayGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetRoutingGatewayGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetRoutingGatewayGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetRoutingGatewayGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetRoutingGatewayGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRoutingGatewayGroupEndpointResponse400
    | GetRoutingGatewayGroupEndpointResponse401
    | GetRoutingGatewayGroupEndpointResponse403
    | GetRoutingGatewayGroupEndpointResponse404
    | GetRoutingGatewayGroupEndpointResponse405
    | GetRoutingGatewayGroupEndpointResponse406
    | GetRoutingGatewayGroupEndpointResponse409
    | GetRoutingGatewayGroupEndpointResponse415
    | GetRoutingGatewayGroupEndpointResponse422
    | GetRoutingGatewayGroupEndpointResponse424
    | GetRoutingGatewayGroupEndpointResponse500
    | GetRoutingGatewayGroupEndpointResponse503
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
    GetRoutingGatewayGroupEndpointResponse400
    | GetRoutingGatewayGroupEndpointResponse401
    | GetRoutingGatewayGroupEndpointResponse403
    | GetRoutingGatewayGroupEndpointResponse404
    | GetRoutingGatewayGroupEndpointResponse405
    | GetRoutingGatewayGroupEndpointResponse406
    | GetRoutingGatewayGroupEndpointResponse409
    | GetRoutingGatewayGroupEndpointResponse415
    | GetRoutingGatewayGroupEndpointResponse422
    | GetRoutingGatewayGroupEndpointResponse424
    | GetRoutingGatewayGroupEndpointResponse500
    | GetRoutingGatewayGroupEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoutingGatewayGroupEndpointResponse400 | GetRoutingGatewayGroupEndpointResponse401 | GetRoutingGatewayGroupEndpointResponse403 | GetRoutingGatewayGroupEndpointResponse404 | GetRoutingGatewayGroupEndpointResponse405 | GetRoutingGatewayGroupEndpointResponse406 | GetRoutingGatewayGroupEndpointResponse409 | GetRoutingGatewayGroupEndpointResponse415 | GetRoutingGatewayGroupEndpointResponse422 | GetRoutingGatewayGroupEndpointResponse424 | GetRoutingGatewayGroupEndpointResponse500 | GetRoutingGatewayGroupEndpointResponse503]
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
    GetRoutingGatewayGroupEndpointResponse400
    | GetRoutingGatewayGroupEndpointResponse401
    | GetRoutingGatewayGroupEndpointResponse403
    | GetRoutingGatewayGroupEndpointResponse404
    | GetRoutingGatewayGroupEndpointResponse405
    | GetRoutingGatewayGroupEndpointResponse406
    | GetRoutingGatewayGroupEndpointResponse409
    | GetRoutingGatewayGroupEndpointResponse415
    | GetRoutingGatewayGroupEndpointResponse422
    | GetRoutingGatewayGroupEndpointResponse424
    | GetRoutingGatewayGroupEndpointResponse500
    | GetRoutingGatewayGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoutingGatewayGroupEndpointResponse400 | GetRoutingGatewayGroupEndpointResponse401 | GetRoutingGatewayGroupEndpointResponse403 | GetRoutingGatewayGroupEndpointResponse404 | GetRoutingGatewayGroupEndpointResponse405 | GetRoutingGatewayGroupEndpointResponse406 | GetRoutingGatewayGroupEndpointResponse409 | GetRoutingGatewayGroupEndpointResponse415 | GetRoutingGatewayGroupEndpointResponse422 | GetRoutingGatewayGroupEndpointResponse424 | GetRoutingGatewayGroupEndpointResponse500 | GetRoutingGatewayGroupEndpointResponse503
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
    GetRoutingGatewayGroupEndpointResponse400
    | GetRoutingGatewayGroupEndpointResponse401
    | GetRoutingGatewayGroupEndpointResponse403
    | GetRoutingGatewayGroupEndpointResponse404
    | GetRoutingGatewayGroupEndpointResponse405
    | GetRoutingGatewayGroupEndpointResponse406
    | GetRoutingGatewayGroupEndpointResponse409
    | GetRoutingGatewayGroupEndpointResponse415
    | GetRoutingGatewayGroupEndpointResponse422
    | GetRoutingGatewayGroupEndpointResponse424
    | GetRoutingGatewayGroupEndpointResponse500
    | GetRoutingGatewayGroupEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoutingGatewayGroupEndpointResponse400 | GetRoutingGatewayGroupEndpointResponse401 | GetRoutingGatewayGroupEndpointResponse403 | GetRoutingGatewayGroupEndpointResponse404 | GetRoutingGatewayGroupEndpointResponse405 | GetRoutingGatewayGroupEndpointResponse406 | GetRoutingGatewayGroupEndpointResponse409 | GetRoutingGatewayGroupEndpointResponse415 | GetRoutingGatewayGroupEndpointResponse422 | GetRoutingGatewayGroupEndpointResponse424 | GetRoutingGatewayGroupEndpointResponse500 | GetRoutingGatewayGroupEndpointResponse503]
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
    GetRoutingGatewayGroupEndpointResponse400
    | GetRoutingGatewayGroupEndpointResponse401
    | GetRoutingGatewayGroupEndpointResponse403
    | GetRoutingGatewayGroupEndpointResponse404
    | GetRoutingGatewayGroupEndpointResponse405
    | GetRoutingGatewayGroupEndpointResponse406
    | GetRoutingGatewayGroupEndpointResponse409
    | GetRoutingGatewayGroupEndpointResponse415
    | GetRoutingGatewayGroupEndpointResponse422
    | GetRoutingGatewayGroupEndpointResponse424
    | GetRoutingGatewayGroupEndpointResponse500
    | GetRoutingGatewayGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoutingGatewayGroupEndpointResponse400 | GetRoutingGatewayGroupEndpointResponse401 | GetRoutingGatewayGroupEndpointResponse403 | GetRoutingGatewayGroupEndpointResponse404 | GetRoutingGatewayGroupEndpointResponse405 | GetRoutingGatewayGroupEndpointResponse406 | GetRoutingGatewayGroupEndpointResponse409 | GetRoutingGatewayGroupEndpointResponse415 | GetRoutingGatewayGroupEndpointResponse422 | GetRoutingGatewayGroupEndpointResponse424 | GetRoutingGatewayGroupEndpointResponse500 | GetRoutingGatewayGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
