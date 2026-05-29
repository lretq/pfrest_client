from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_routing_gateway_group_endpoint_data_body import PatchRoutingGatewayGroupEndpointDataBody
from ...models.patch_routing_gateway_group_endpoint_json_body import PatchRoutingGatewayGroupEndpointJsonBody
from ...models.patch_routing_gateway_group_endpoint_response_400 import PatchRoutingGatewayGroupEndpointResponse400
from ...models.patch_routing_gateway_group_endpoint_response_401 import PatchRoutingGatewayGroupEndpointResponse401
from ...models.patch_routing_gateway_group_endpoint_response_403 import PatchRoutingGatewayGroupEndpointResponse403
from ...models.patch_routing_gateway_group_endpoint_response_404 import PatchRoutingGatewayGroupEndpointResponse404
from ...models.patch_routing_gateway_group_endpoint_response_405 import PatchRoutingGatewayGroupEndpointResponse405
from ...models.patch_routing_gateway_group_endpoint_response_406 import PatchRoutingGatewayGroupEndpointResponse406
from ...models.patch_routing_gateway_group_endpoint_response_409 import PatchRoutingGatewayGroupEndpointResponse409
from ...models.patch_routing_gateway_group_endpoint_response_415 import PatchRoutingGatewayGroupEndpointResponse415
from ...models.patch_routing_gateway_group_endpoint_response_422 import PatchRoutingGatewayGroupEndpointResponse422
from ...models.patch_routing_gateway_group_endpoint_response_424 import PatchRoutingGatewayGroupEndpointResponse424
from ...models.patch_routing_gateway_group_endpoint_response_500 import PatchRoutingGatewayGroupEndpointResponse500
from ...models.patch_routing_gateway_group_endpoint_response_503 import PatchRoutingGatewayGroupEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchRoutingGatewayGroupEndpointJsonBody | PatchRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/routing/gateway/group",
    }

    if isinstance(body, PatchRoutingGatewayGroupEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchRoutingGatewayGroupEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchRoutingGatewayGroupEndpointResponse400
    | PatchRoutingGatewayGroupEndpointResponse401
    | PatchRoutingGatewayGroupEndpointResponse403
    | PatchRoutingGatewayGroupEndpointResponse404
    | PatchRoutingGatewayGroupEndpointResponse405
    | PatchRoutingGatewayGroupEndpointResponse406
    | PatchRoutingGatewayGroupEndpointResponse409
    | PatchRoutingGatewayGroupEndpointResponse415
    | PatchRoutingGatewayGroupEndpointResponse422
    | PatchRoutingGatewayGroupEndpointResponse424
    | PatchRoutingGatewayGroupEndpointResponse500
    | PatchRoutingGatewayGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchRoutingGatewayGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchRoutingGatewayGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchRoutingGatewayGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchRoutingGatewayGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchRoutingGatewayGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchRoutingGatewayGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchRoutingGatewayGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchRoutingGatewayGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchRoutingGatewayGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchRoutingGatewayGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchRoutingGatewayGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchRoutingGatewayGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchRoutingGatewayGroupEndpointResponse400
    | PatchRoutingGatewayGroupEndpointResponse401
    | PatchRoutingGatewayGroupEndpointResponse403
    | PatchRoutingGatewayGroupEndpointResponse404
    | PatchRoutingGatewayGroupEndpointResponse405
    | PatchRoutingGatewayGroupEndpointResponse406
    | PatchRoutingGatewayGroupEndpointResponse409
    | PatchRoutingGatewayGroupEndpointResponse415
    | PatchRoutingGatewayGroupEndpointResponse422
    | PatchRoutingGatewayGroupEndpointResponse424
    | PatchRoutingGatewayGroupEndpointResponse500
    | PatchRoutingGatewayGroupEndpointResponse503
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
    body: PatchRoutingGatewayGroupEndpointJsonBody | PatchRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchRoutingGatewayGroupEndpointResponse400
    | PatchRoutingGatewayGroupEndpointResponse401
    | PatchRoutingGatewayGroupEndpointResponse403
    | PatchRoutingGatewayGroupEndpointResponse404
    | PatchRoutingGatewayGroupEndpointResponse405
    | PatchRoutingGatewayGroupEndpointResponse406
    | PatchRoutingGatewayGroupEndpointResponse409
    | PatchRoutingGatewayGroupEndpointResponse415
    | PatchRoutingGatewayGroupEndpointResponse422
    | PatchRoutingGatewayGroupEndpointResponse424
    | PatchRoutingGatewayGroupEndpointResponse500
    | PatchRoutingGatewayGroupEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingGatewayGroupEndpointResponse400 | PatchRoutingGatewayGroupEndpointResponse401 | PatchRoutingGatewayGroupEndpointResponse403 | PatchRoutingGatewayGroupEndpointResponse404 | PatchRoutingGatewayGroupEndpointResponse405 | PatchRoutingGatewayGroupEndpointResponse406 | PatchRoutingGatewayGroupEndpointResponse409 | PatchRoutingGatewayGroupEndpointResponse415 | PatchRoutingGatewayGroupEndpointResponse422 | PatchRoutingGatewayGroupEndpointResponse424 | PatchRoutingGatewayGroupEndpointResponse500 | PatchRoutingGatewayGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayGroupEndpointJsonBody | PatchRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> (
    PatchRoutingGatewayGroupEndpointResponse400
    | PatchRoutingGatewayGroupEndpointResponse401
    | PatchRoutingGatewayGroupEndpointResponse403
    | PatchRoutingGatewayGroupEndpointResponse404
    | PatchRoutingGatewayGroupEndpointResponse405
    | PatchRoutingGatewayGroupEndpointResponse406
    | PatchRoutingGatewayGroupEndpointResponse409
    | PatchRoutingGatewayGroupEndpointResponse415
    | PatchRoutingGatewayGroupEndpointResponse422
    | PatchRoutingGatewayGroupEndpointResponse424
    | PatchRoutingGatewayGroupEndpointResponse500
    | PatchRoutingGatewayGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingGatewayGroupEndpointResponse400 | PatchRoutingGatewayGroupEndpointResponse401 | PatchRoutingGatewayGroupEndpointResponse403 | PatchRoutingGatewayGroupEndpointResponse404 | PatchRoutingGatewayGroupEndpointResponse405 | PatchRoutingGatewayGroupEndpointResponse406 | PatchRoutingGatewayGroupEndpointResponse409 | PatchRoutingGatewayGroupEndpointResponse415 | PatchRoutingGatewayGroupEndpointResponse422 | PatchRoutingGatewayGroupEndpointResponse424 | PatchRoutingGatewayGroupEndpointResponse500 | PatchRoutingGatewayGroupEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayGroupEndpointJsonBody | PatchRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchRoutingGatewayGroupEndpointResponse400
    | PatchRoutingGatewayGroupEndpointResponse401
    | PatchRoutingGatewayGroupEndpointResponse403
    | PatchRoutingGatewayGroupEndpointResponse404
    | PatchRoutingGatewayGroupEndpointResponse405
    | PatchRoutingGatewayGroupEndpointResponse406
    | PatchRoutingGatewayGroupEndpointResponse409
    | PatchRoutingGatewayGroupEndpointResponse415
    | PatchRoutingGatewayGroupEndpointResponse422
    | PatchRoutingGatewayGroupEndpointResponse424
    | PatchRoutingGatewayGroupEndpointResponse500
    | PatchRoutingGatewayGroupEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingGatewayGroupEndpointResponse400 | PatchRoutingGatewayGroupEndpointResponse401 | PatchRoutingGatewayGroupEndpointResponse403 | PatchRoutingGatewayGroupEndpointResponse404 | PatchRoutingGatewayGroupEndpointResponse405 | PatchRoutingGatewayGroupEndpointResponse406 | PatchRoutingGatewayGroupEndpointResponse409 | PatchRoutingGatewayGroupEndpointResponse415 | PatchRoutingGatewayGroupEndpointResponse422 | PatchRoutingGatewayGroupEndpointResponse424 | PatchRoutingGatewayGroupEndpointResponse500 | PatchRoutingGatewayGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayGroupEndpointJsonBody | PatchRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> (
    PatchRoutingGatewayGroupEndpointResponse400
    | PatchRoutingGatewayGroupEndpointResponse401
    | PatchRoutingGatewayGroupEndpointResponse403
    | PatchRoutingGatewayGroupEndpointResponse404
    | PatchRoutingGatewayGroupEndpointResponse405
    | PatchRoutingGatewayGroupEndpointResponse406
    | PatchRoutingGatewayGroupEndpointResponse409
    | PatchRoutingGatewayGroupEndpointResponse415
    | PatchRoutingGatewayGroupEndpointResponse422
    | PatchRoutingGatewayGroupEndpointResponse424
    | PatchRoutingGatewayGroupEndpointResponse500
    | PatchRoutingGatewayGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingGatewayGroupEndpointResponse400 | PatchRoutingGatewayGroupEndpointResponse401 | PatchRoutingGatewayGroupEndpointResponse403 | PatchRoutingGatewayGroupEndpointResponse404 | PatchRoutingGatewayGroupEndpointResponse405 | PatchRoutingGatewayGroupEndpointResponse406 | PatchRoutingGatewayGroupEndpointResponse409 | PatchRoutingGatewayGroupEndpointResponse415 | PatchRoutingGatewayGroupEndpointResponse422 | PatchRoutingGatewayGroupEndpointResponse424 | PatchRoutingGatewayGroupEndpointResponse500 | PatchRoutingGatewayGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
