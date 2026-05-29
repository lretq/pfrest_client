from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_routing_gateway_default_endpoint_data_body import PatchRoutingGatewayDefaultEndpointDataBody
from ...models.patch_routing_gateway_default_endpoint_json_body import PatchRoutingGatewayDefaultEndpointJsonBody
from ...models.patch_routing_gateway_default_endpoint_response_400 import PatchRoutingGatewayDefaultEndpointResponse400
from ...models.patch_routing_gateway_default_endpoint_response_401 import PatchRoutingGatewayDefaultEndpointResponse401
from ...models.patch_routing_gateway_default_endpoint_response_403 import PatchRoutingGatewayDefaultEndpointResponse403
from ...models.patch_routing_gateway_default_endpoint_response_404 import PatchRoutingGatewayDefaultEndpointResponse404
from ...models.patch_routing_gateway_default_endpoint_response_405 import PatchRoutingGatewayDefaultEndpointResponse405
from ...models.patch_routing_gateway_default_endpoint_response_406 import PatchRoutingGatewayDefaultEndpointResponse406
from ...models.patch_routing_gateway_default_endpoint_response_409 import PatchRoutingGatewayDefaultEndpointResponse409
from ...models.patch_routing_gateway_default_endpoint_response_415 import PatchRoutingGatewayDefaultEndpointResponse415
from ...models.patch_routing_gateway_default_endpoint_response_422 import PatchRoutingGatewayDefaultEndpointResponse422
from ...models.patch_routing_gateway_default_endpoint_response_424 import PatchRoutingGatewayDefaultEndpointResponse424
from ...models.patch_routing_gateway_default_endpoint_response_500 import PatchRoutingGatewayDefaultEndpointResponse500
from ...models.patch_routing_gateway_default_endpoint_response_503 import PatchRoutingGatewayDefaultEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchRoutingGatewayDefaultEndpointJsonBody | PatchRoutingGatewayDefaultEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/routing/gateway/default",
    }

    if isinstance(body, PatchRoutingGatewayDefaultEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchRoutingGatewayDefaultEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchRoutingGatewayDefaultEndpointResponse400
    | PatchRoutingGatewayDefaultEndpointResponse401
    | PatchRoutingGatewayDefaultEndpointResponse403
    | PatchRoutingGatewayDefaultEndpointResponse404
    | PatchRoutingGatewayDefaultEndpointResponse405
    | PatchRoutingGatewayDefaultEndpointResponse406
    | PatchRoutingGatewayDefaultEndpointResponse409
    | PatchRoutingGatewayDefaultEndpointResponse415
    | PatchRoutingGatewayDefaultEndpointResponse422
    | PatchRoutingGatewayDefaultEndpointResponse424
    | PatchRoutingGatewayDefaultEndpointResponse500
    | PatchRoutingGatewayDefaultEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchRoutingGatewayDefaultEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchRoutingGatewayDefaultEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchRoutingGatewayDefaultEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchRoutingGatewayDefaultEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchRoutingGatewayDefaultEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchRoutingGatewayDefaultEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchRoutingGatewayDefaultEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchRoutingGatewayDefaultEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchRoutingGatewayDefaultEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchRoutingGatewayDefaultEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchRoutingGatewayDefaultEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchRoutingGatewayDefaultEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchRoutingGatewayDefaultEndpointResponse400
    | PatchRoutingGatewayDefaultEndpointResponse401
    | PatchRoutingGatewayDefaultEndpointResponse403
    | PatchRoutingGatewayDefaultEndpointResponse404
    | PatchRoutingGatewayDefaultEndpointResponse405
    | PatchRoutingGatewayDefaultEndpointResponse406
    | PatchRoutingGatewayDefaultEndpointResponse409
    | PatchRoutingGatewayDefaultEndpointResponse415
    | PatchRoutingGatewayDefaultEndpointResponse422
    | PatchRoutingGatewayDefaultEndpointResponse424
    | PatchRoutingGatewayDefaultEndpointResponse500
    | PatchRoutingGatewayDefaultEndpointResponse503
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
    body: PatchRoutingGatewayDefaultEndpointJsonBody | PatchRoutingGatewayDefaultEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchRoutingGatewayDefaultEndpointResponse400
    | PatchRoutingGatewayDefaultEndpointResponse401
    | PatchRoutingGatewayDefaultEndpointResponse403
    | PatchRoutingGatewayDefaultEndpointResponse404
    | PatchRoutingGatewayDefaultEndpointResponse405
    | PatchRoutingGatewayDefaultEndpointResponse406
    | PatchRoutingGatewayDefaultEndpointResponse409
    | PatchRoutingGatewayDefaultEndpointResponse415
    | PatchRoutingGatewayDefaultEndpointResponse422
    | PatchRoutingGatewayDefaultEndpointResponse424
    | PatchRoutingGatewayDefaultEndpointResponse500
    | PatchRoutingGatewayDefaultEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayDefaultEndpointJsonBody | Unset):
        body (PatchRoutingGatewayDefaultEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingGatewayDefaultEndpointResponse400 | PatchRoutingGatewayDefaultEndpointResponse401 | PatchRoutingGatewayDefaultEndpointResponse403 | PatchRoutingGatewayDefaultEndpointResponse404 | PatchRoutingGatewayDefaultEndpointResponse405 | PatchRoutingGatewayDefaultEndpointResponse406 | PatchRoutingGatewayDefaultEndpointResponse409 | PatchRoutingGatewayDefaultEndpointResponse415 | PatchRoutingGatewayDefaultEndpointResponse422 | PatchRoutingGatewayDefaultEndpointResponse424 | PatchRoutingGatewayDefaultEndpointResponse500 | PatchRoutingGatewayDefaultEndpointResponse503]
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
    body: PatchRoutingGatewayDefaultEndpointJsonBody | PatchRoutingGatewayDefaultEndpointDataBody | Unset = UNSET,
) -> (
    PatchRoutingGatewayDefaultEndpointResponse400
    | PatchRoutingGatewayDefaultEndpointResponse401
    | PatchRoutingGatewayDefaultEndpointResponse403
    | PatchRoutingGatewayDefaultEndpointResponse404
    | PatchRoutingGatewayDefaultEndpointResponse405
    | PatchRoutingGatewayDefaultEndpointResponse406
    | PatchRoutingGatewayDefaultEndpointResponse409
    | PatchRoutingGatewayDefaultEndpointResponse415
    | PatchRoutingGatewayDefaultEndpointResponse422
    | PatchRoutingGatewayDefaultEndpointResponse424
    | PatchRoutingGatewayDefaultEndpointResponse500
    | PatchRoutingGatewayDefaultEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayDefaultEndpointJsonBody | Unset):
        body (PatchRoutingGatewayDefaultEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingGatewayDefaultEndpointResponse400 | PatchRoutingGatewayDefaultEndpointResponse401 | PatchRoutingGatewayDefaultEndpointResponse403 | PatchRoutingGatewayDefaultEndpointResponse404 | PatchRoutingGatewayDefaultEndpointResponse405 | PatchRoutingGatewayDefaultEndpointResponse406 | PatchRoutingGatewayDefaultEndpointResponse409 | PatchRoutingGatewayDefaultEndpointResponse415 | PatchRoutingGatewayDefaultEndpointResponse422 | PatchRoutingGatewayDefaultEndpointResponse424 | PatchRoutingGatewayDefaultEndpointResponse500 | PatchRoutingGatewayDefaultEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayDefaultEndpointJsonBody | PatchRoutingGatewayDefaultEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchRoutingGatewayDefaultEndpointResponse400
    | PatchRoutingGatewayDefaultEndpointResponse401
    | PatchRoutingGatewayDefaultEndpointResponse403
    | PatchRoutingGatewayDefaultEndpointResponse404
    | PatchRoutingGatewayDefaultEndpointResponse405
    | PatchRoutingGatewayDefaultEndpointResponse406
    | PatchRoutingGatewayDefaultEndpointResponse409
    | PatchRoutingGatewayDefaultEndpointResponse415
    | PatchRoutingGatewayDefaultEndpointResponse422
    | PatchRoutingGatewayDefaultEndpointResponse424
    | PatchRoutingGatewayDefaultEndpointResponse500
    | PatchRoutingGatewayDefaultEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayDefaultEndpointJsonBody | Unset):
        body (PatchRoutingGatewayDefaultEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingGatewayDefaultEndpointResponse400 | PatchRoutingGatewayDefaultEndpointResponse401 | PatchRoutingGatewayDefaultEndpointResponse403 | PatchRoutingGatewayDefaultEndpointResponse404 | PatchRoutingGatewayDefaultEndpointResponse405 | PatchRoutingGatewayDefaultEndpointResponse406 | PatchRoutingGatewayDefaultEndpointResponse409 | PatchRoutingGatewayDefaultEndpointResponse415 | PatchRoutingGatewayDefaultEndpointResponse422 | PatchRoutingGatewayDefaultEndpointResponse424 | PatchRoutingGatewayDefaultEndpointResponse500 | PatchRoutingGatewayDefaultEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayDefaultEndpointJsonBody | PatchRoutingGatewayDefaultEndpointDataBody | Unset = UNSET,
) -> (
    PatchRoutingGatewayDefaultEndpointResponse400
    | PatchRoutingGatewayDefaultEndpointResponse401
    | PatchRoutingGatewayDefaultEndpointResponse403
    | PatchRoutingGatewayDefaultEndpointResponse404
    | PatchRoutingGatewayDefaultEndpointResponse405
    | PatchRoutingGatewayDefaultEndpointResponse406
    | PatchRoutingGatewayDefaultEndpointResponse409
    | PatchRoutingGatewayDefaultEndpointResponse415
    | PatchRoutingGatewayDefaultEndpointResponse422
    | PatchRoutingGatewayDefaultEndpointResponse424
    | PatchRoutingGatewayDefaultEndpointResponse500
    | PatchRoutingGatewayDefaultEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Default Gateway.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayDefaultEndpointJsonBody | Unset):
        body (PatchRoutingGatewayDefaultEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingGatewayDefaultEndpointResponse400 | PatchRoutingGatewayDefaultEndpointResponse401 | PatchRoutingGatewayDefaultEndpointResponse403 | PatchRoutingGatewayDefaultEndpointResponse404 | PatchRoutingGatewayDefaultEndpointResponse405 | PatchRoutingGatewayDefaultEndpointResponse406 | PatchRoutingGatewayDefaultEndpointResponse409 | PatchRoutingGatewayDefaultEndpointResponse415 | PatchRoutingGatewayDefaultEndpointResponse422 | PatchRoutingGatewayDefaultEndpointResponse424 | PatchRoutingGatewayDefaultEndpointResponse500 | PatchRoutingGatewayDefaultEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
