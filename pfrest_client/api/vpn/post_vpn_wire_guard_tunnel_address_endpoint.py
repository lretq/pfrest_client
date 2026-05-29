from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_data_body import (
    PostVPNWireGuardTunnelAddressEndpointDataBody,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_json_body import (
    PostVPNWireGuardTunnelAddressEndpointJsonBody,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_400 import (
    PostVPNWireGuardTunnelAddressEndpointResponse400,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_401 import (
    PostVPNWireGuardTunnelAddressEndpointResponse401,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_403 import (
    PostVPNWireGuardTunnelAddressEndpointResponse403,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_404 import (
    PostVPNWireGuardTunnelAddressEndpointResponse404,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_405 import (
    PostVPNWireGuardTunnelAddressEndpointResponse405,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_406 import (
    PostVPNWireGuardTunnelAddressEndpointResponse406,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_409 import (
    PostVPNWireGuardTunnelAddressEndpointResponse409,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_415 import (
    PostVPNWireGuardTunnelAddressEndpointResponse415,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_422 import (
    PostVPNWireGuardTunnelAddressEndpointResponse422,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_424 import (
    PostVPNWireGuardTunnelAddressEndpointResponse424,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_500 import (
    PostVPNWireGuardTunnelAddressEndpointResponse500,
)
from ...models.post_vpn_wire_guard_tunnel_address_endpoint_response_503 import (
    PostVPNWireGuardTunnelAddressEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNWireGuardTunnelAddressEndpointJsonBody | PostVPNWireGuardTunnelAddressEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/wireguard/tunnel/address",
    }

    if isinstance(body, PostVPNWireGuardTunnelAddressEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNWireGuardTunnelAddressEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNWireGuardTunnelAddressEndpointResponse400
    | PostVPNWireGuardTunnelAddressEndpointResponse401
    | PostVPNWireGuardTunnelAddressEndpointResponse403
    | PostVPNWireGuardTunnelAddressEndpointResponse404
    | PostVPNWireGuardTunnelAddressEndpointResponse405
    | PostVPNWireGuardTunnelAddressEndpointResponse406
    | PostVPNWireGuardTunnelAddressEndpointResponse409
    | PostVPNWireGuardTunnelAddressEndpointResponse415
    | PostVPNWireGuardTunnelAddressEndpointResponse422
    | PostVPNWireGuardTunnelAddressEndpointResponse424
    | PostVPNWireGuardTunnelAddressEndpointResponse500
    | PostVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNWireGuardTunnelAddressEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNWireGuardTunnelAddressEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNWireGuardTunnelAddressEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNWireGuardTunnelAddressEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNWireGuardTunnelAddressEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNWireGuardTunnelAddressEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNWireGuardTunnelAddressEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNWireGuardTunnelAddressEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNWireGuardTunnelAddressEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNWireGuardTunnelAddressEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNWireGuardTunnelAddressEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNWireGuardTunnelAddressEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNWireGuardTunnelAddressEndpointResponse400
    | PostVPNWireGuardTunnelAddressEndpointResponse401
    | PostVPNWireGuardTunnelAddressEndpointResponse403
    | PostVPNWireGuardTunnelAddressEndpointResponse404
    | PostVPNWireGuardTunnelAddressEndpointResponse405
    | PostVPNWireGuardTunnelAddressEndpointResponse406
    | PostVPNWireGuardTunnelAddressEndpointResponse409
    | PostVPNWireGuardTunnelAddressEndpointResponse415
    | PostVPNWireGuardTunnelAddressEndpointResponse422
    | PostVPNWireGuardTunnelAddressEndpointResponse424
    | PostVPNWireGuardTunnelAddressEndpointResponse500
    | PostVPNWireGuardTunnelAddressEndpointResponse503
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
    body: PostVPNWireGuardTunnelAddressEndpointJsonBody | PostVPNWireGuardTunnelAddressEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNWireGuardTunnelAddressEndpointResponse400
    | PostVPNWireGuardTunnelAddressEndpointResponse401
    | PostVPNWireGuardTunnelAddressEndpointResponse403
    | PostVPNWireGuardTunnelAddressEndpointResponse404
    | PostVPNWireGuardTunnelAddressEndpointResponse405
    | PostVPNWireGuardTunnelAddressEndpointResponse406
    | PostVPNWireGuardTunnelAddressEndpointResponse409
    | PostVPNWireGuardTunnelAddressEndpointResponse415
    | PostVPNWireGuardTunnelAddressEndpointResponse422
    | PostVPNWireGuardTunnelAddressEndpointResponse424
    | PostVPNWireGuardTunnelAddressEndpointResponse500
    | PostVPNWireGuardTunnelAddressEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PostVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNWireGuardTunnelAddressEndpointResponse400 | PostVPNWireGuardTunnelAddressEndpointResponse401 | PostVPNWireGuardTunnelAddressEndpointResponse403 | PostVPNWireGuardTunnelAddressEndpointResponse404 | PostVPNWireGuardTunnelAddressEndpointResponse405 | PostVPNWireGuardTunnelAddressEndpointResponse406 | PostVPNWireGuardTunnelAddressEndpointResponse409 | PostVPNWireGuardTunnelAddressEndpointResponse415 | PostVPNWireGuardTunnelAddressEndpointResponse422 | PostVPNWireGuardTunnelAddressEndpointResponse424 | PostVPNWireGuardTunnelAddressEndpointResponse500 | PostVPNWireGuardTunnelAddressEndpointResponse503]
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
    body: PostVPNWireGuardTunnelAddressEndpointJsonBody | PostVPNWireGuardTunnelAddressEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNWireGuardTunnelAddressEndpointResponse400
    | PostVPNWireGuardTunnelAddressEndpointResponse401
    | PostVPNWireGuardTunnelAddressEndpointResponse403
    | PostVPNWireGuardTunnelAddressEndpointResponse404
    | PostVPNWireGuardTunnelAddressEndpointResponse405
    | PostVPNWireGuardTunnelAddressEndpointResponse406
    | PostVPNWireGuardTunnelAddressEndpointResponse409
    | PostVPNWireGuardTunnelAddressEndpointResponse415
    | PostVPNWireGuardTunnelAddressEndpointResponse422
    | PostVPNWireGuardTunnelAddressEndpointResponse424
    | PostVPNWireGuardTunnelAddressEndpointResponse500
    | PostVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PostVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNWireGuardTunnelAddressEndpointResponse400 | PostVPNWireGuardTunnelAddressEndpointResponse401 | PostVPNWireGuardTunnelAddressEndpointResponse403 | PostVPNWireGuardTunnelAddressEndpointResponse404 | PostVPNWireGuardTunnelAddressEndpointResponse405 | PostVPNWireGuardTunnelAddressEndpointResponse406 | PostVPNWireGuardTunnelAddressEndpointResponse409 | PostVPNWireGuardTunnelAddressEndpointResponse415 | PostVPNWireGuardTunnelAddressEndpointResponse422 | PostVPNWireGuardTunnelAddressEndpointResponse424 | PostVPNWireGuardTunnelAddressEndpointResponse500 | PostVPNWireGuardTunnelAddressEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNWireGuardTunnelAddressEndpointJsonBody | PostVPNWireGuardTunnelAddressEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNWireGuardTunnelAddressEndpointResponse400
    | PostVPNWireGuardTunnelAddressEndpointResponse401
    | PostVPNWireGuardTunnelAddressEndpointResponse403
    | PostVPNWireGuardTunnelAddressEndpointResponse404
    | PostVPNWireGuardTunnelAddressEndpointResponse405
    | PostVPNWireGuardTunnelAddressEndpointResponse406
    | PostVPNWireGuardTunnelAddressEndpointResponse409
    | PostVPNWireGuardTunnelAddressEndpointResponse415
    | PostVPNWireGuardTunnelAddressEndpointResponse422
    | PostVPNWireGuardTunnelAddressEndpointResponse424
    | PostVPNWireGuardTunnelAddressEndpointResponse500
    | PostVPNWireGuardTunnelAddressEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PostVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNWireGuardTunnelAddressEndpointResponse400 | PostVPNWireGuardTunnelAddressEndpointResponse401 | PostVPNWireGuardTunnelAddressEndpointResponse403 | PostVPNWireGuardTunnelAddressEndpointResponse404 | PostVPNWireGuardTunnelAddressEndpointResponse405 | PostVPNWireGuardTunnelAddressEndpointResponse406 | PostVPNWireGuardTunnelAddressEndpointResponse409 | PostVPNWireGuardTunnelAddressEndpointResponse415 | PostVPNWireGuardTunnelAddressEndpointResponse422 | PostVPNWireGuardTunnelAddressEndpointResponse424 | PostVPNWireGuardTunnelAddressEndpointResponse500 | PostVPNWireGuardTunnelAddressEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNWireGuardTunnelAddressEndpointJsonBody | PostVPNWireGuardTunnelAddressEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNWireGuardTunnelAddressEndpointResponse400
    | PostVPNWireGuardTunnelAddressEndpointResponse401
    | PostVPNWireGuardTunnelAddressEndpointResponse403
    | PostVPNWireGuardTunnelAddressEndpointResponse404
    | PostVPNWireGuardTunnelAddressEndpointResponse405
    | PostVPNWireGuardTunnelAddressEndpointResponse406
    | PostVPNWireGuardTunnelAddressEndpointResponse409
    | PostVPNWireGuardTunnelAddressEndpointResponse415
    | PostVPNWireGuardTunnelAddressEndpointResponse422
    | PostVPNWireGuardTunnelAddressEndpointResponse424
    | PostVPNWireGuardTunnelAddressEndpointResponse500
    | PostVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PostVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNWireGuardTunnelAddressEndpointResponse400 | PostVPNWireGuardTunnelAddressEndpointResponse401 | PostVPNWireGuardTunnelAddressEndpointResponse403 | PostVPNWireGuardTunnelAddressEndpointResponse404 | PostVPNWireGuardTunnelAddressEndpointResponse405 | PostVPNWireGuardTunnelAddressEndpointResponse406 | PostVPNWireGuardTunnelAddressEndpointResponse409 | PostVPNWireGuardTunnelAddressEndpointResponse415 | PostVPNWireGuardTunnelAddressEndpointResponse422 | PostVPNWireGuardTunnelAddressEndpointResponse424 | PostVPNWireGuardTunnelAddressEndpointResponse500 | PostVPNWireGuardTunnelAddressEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
