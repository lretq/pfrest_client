from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_data_body import (
    PatchVPNWireGuardTunnelAddressEndpointDataBody,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_json_body import (
    PatchVPNWireGuardTunnelAddressEndpointJsonBody,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_400 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse400,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_401 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse401,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_403 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse403,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_404 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse404,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_405 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse405,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_406 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse406,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_409 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse409,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_415 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse415,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_422 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse422,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_424 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse424,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_500 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse500,
)
from ...models.patch_vpn_wire_guard_tunnel_address_endpoint_response_503 import (
    PatchVPNWireGuardTunnelAddressEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNWireGuardTunnelAddressEndpointJsonBody
    | PatchVPNWireGuardTunnelAddressEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/wireguard/tunnel/address",
    }

    if isinstance(body, PatchVPNWireGuardTunnelAddressEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNWireGuardTunnelAddressEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNWireGuardTunnelAddressEndpointResponse400
    | PatchVPNWireGuardTunnelAddressEndpointResponse401
    | PatchVPNWireGuardTunnelAddressEndpointResponse403
    | PatchVPNWireGuardTunnelAddressEndpointResponse404
    | PatchVPNWireGuardTunnelAddressEndpointResponse405
    | PatchVPNWireGuardTunnelAddressEndpointResponse406
    | PatchVPNWireGuardTunnelAddressEndpointResponse409
    | PatchVPNWireGuardTunnelAddressEndpointResponse415
    | PatchVPNWireGuardTunnelAddressEndpointResponse422
    | PatchVPNWireGuardTunnelAddressEndpointResponse424
    | PatchVPNWireGuardTunnelAddressEndpointResponse500
    | PatchVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNWireGuardTunnelAddressEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNWireGuardTunnelAddressEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNWireGuardTunnelAddressEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNWireGuardTunnelAddressEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNWireGuardTunnelAddressEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNWireGuardTunnelAddressEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNWireGuardTunnelAddressEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNWireGuardTunnelAddressEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNWireGuardTunnelAddressEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNWireGuardTunnelAddressEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNWireGuardTunnelAddressEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNWireGuardTunnelAddressEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNWireGuardTunnelAddressEndpointResponse400
    | PatchVPNWireGuardTunnelAddressEndpointResponse401
    | PatchVPNWireGuardTunnelAddressEndpointResponse403
    | PatchVPNWireGuardTunnelAddressEndpointResponse404
    | PatchVPNWireGuardTunnelAddressEndpointResponse405
    | PatchVPNWireGuardTunnelAddressEndpointResponse406
    | PatchVPNWireGuardTunnelAddressEndpointResponse409
    | PatchVPNWireGuardTunnelAddressEndpointResponse415
    | PatchVPNWireGuardTunnelAddressEndpointResponse422
    | PatchVPNWireGuardTunnelAddressEndpointResponse424
    | PatchVPNWireGuardTunnelAddressEndpointResponse500
    | PatchVPNWireGuardTunnelAddressEndpointResponse503
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
    body: PatchVPNWireGuardTunnelAddressEndpointJsonBody
    | PatchVPNWireGuardTunnelAddressEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchVPNWireGuardTunnelAddressEndpointResponse400
    | PatchVPNWireGuardTunnelAddressEndpointResponse401
    | PatchVPNWireGuardTunnelAddressEndpointResponse403
    | PatchVPNWireGuardTunnelAddressEndpointResponse404
    | PatchVPNWireGuardTunnelAddressEndpointResponse405
    | PatchVPNWireGuardTunnelAddressEndpointResponse406
    | PatchVPNWireGuardTunnelAddressEndpointResponse409
    | PatchVPNWireGuardTunnelAddressEndpointResponse415
    | PatchVPNWireGuardTunnelAddressEndpointResponse422
    | PatchVPNWireGuardTunnelAddressEndpointResponse424
    | PatchVPNWireGuardTunnelAddressEndpointResponse500
    | PatchVPNWireGuardTunnelAddressEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-patch ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNWireGuardTunnelAddressEndpointResponse400 | PatchVPNWireGuardTunnelAddressEndpointResponse401 | PatchVPNWireGuardTunnelAddressEndpointResponse403 | PatchVPNWireGuardTunnelAddressEndpointResponse404 | PatchVPNWireGuardTunnelAddressEndpointResponse405 | PatchVPNWireGuardTunnelAddressEndpointResponse406 | PatchVPNWireGuardTunnelAddressEndpointResponse409 | PatchVPNWireGuardTunnelAddressEndpointResponse415 | PatchVPNWireGuardTunnelAddressEndpointResponse422 | PatchVPNWireGuardTunnelAddressEndpointResponse424 | PatchVPNWireGuardTunnelAddressEndpointResponse500 | PatchVPNWireGuardTunnelAddressEndpointResponse503]
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
    body: PatchVPNWireGuardTunnelAddressEndpointJsonBody
    | PatchVPNWireGuardTunnelAddressEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchVPNWireGuardTunnelAddressEndpointResponse400
    | PatchVPNWireGuardTunnelAddressEndpointResponse401
    | PatchVPNWireGuardTunnelAddressEndpointResponse403
    | PatchVPNWireGuardTunnelAddressEndpointResponse404
    | PatchVPNWireGuardTunnelAddressEndpointResponse405
    | PatchVPNWireGuardTunnelAddressEndpointResponse406
    | PatchVPNWireGuardTunnelAddressEndpointResponse409
    | PatchVPNWireGuardTunnelAddressEndpointResponse415
    | PatchVPNWireGuardTunnelAddressEndpointResponse422
    | PatchVPNWireGuardTunnelAddressEndpointResponse424
    | PatchVPNWireGuardTunnelAddressEndpointResponse500
    | PatchVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-patch ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNWireGuardTunnelAddressEndpointResponse400 | PatchVPNWireGuardTunnelAddressEndpointResponse401 | PatchVPNWireGuardTunnelAddressEndpointResponse403 | PatchVPNWireGuardTunnelAddressEndpointResponse404 | PatchVPNWireGuardTunnelAddressEndpointResponse405 | PatchVPNWireGuardTunnelAddressEndpointResponse406 | PatchVPNWireGuardTunnelAddressEndpointResponse409 | PatchVPNWireGuardTunnelAddressEndpointResponse415 | PatchVPNWireGuardTunnelAddressEndpointResponse422 | PatchVPNWireGuardTunnelAddressEndpointResponse424 | PatchVPNWireGuardTunnelAddressEndpointResponse500 | PatchVPNWireGuardTunnelAddressEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNWireGuardTunnelAddressEndpointJsonBody
    | PatchVPNWireGuardTunnelAddressEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchVPNWireGuardTunnelAddressEndpointResponse400
    | PatchVPNWireGuardTunnelAddressEndpointResponse401
    | PatchVPNWireGuardTunnelAddressEndpointResponse403
    | PatchVPNWireGuardTunnelAddressEndpointResponse404
    | PatchVPNWireGuardTunnelAddressEndpointResponse405
    | PatchVPNWireGuardTunnelAddressEndpointResponse406
    | PatchVPNWireGuardTunnelAddressEndpointResponse409
    | PatchVPNWireGuardTunnelAddressEndpointResponse415
    | PatchVPNWireGuardTunnelAddressEndpointResponse422
    | PatchVPNWireGuardTunnelAddressEndpointResponse424
    | PatchVPNWireGuardTunnelAddressEndpointResponse500
    | PatchVPNWireGuardTunnelAddressEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-patch ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNWireGuardTunnelAddressEndpointResponse400 | PatchVPNWireGuardTunnelAddressEndpointResponse401 | PatchVPNWireGuardTunnelAddressEndpointResponse403 | PatchVPNWireGuardTunnelAddressEndpointResponse404 | PatchVPNWireGuardTunnelAddressEndpointResponse405 | PatchVPNWireGuardTunnelAddressEndpointResponse406 | PatchVPNWireGuardTunnelAddressEndpointResponse409 | PatchVPNWireGuardTunnelAddressEndpointResponse415 | PatchVPNWireGuardTunnelAddressEndpointResponse422 | PatchVPNWireGuardTunnelAddressEndpointResponse424 | PatchVPNWireGuardTunnelAddressEndpointResponse500 | PatchVPNWireGuardTunnelAddressEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNWireGuardTunnelAddressEndpointJsonBody
    | PatchVPNWireGuardTunnelAddressEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchVPNWireGuardTunnelAddressEndpointResponse400
    | PatchVPNWireGuardTunnelAddressEndpointResponse401
    | PatchVPNWireGuardTunnelAddressEndpointResponse403
    | PatchVPNWireGuardTunnelAddressEndpointResponse404
    | PatchVPNWireGuardTunnelAddressEndpointResponse405
    | PatchVPNWireGuardTunnelAddressEndpointResponse406
    | PatchVPNWireGuardTunnelAddressEndpointResponse409
    | PatchVPNWireGuardTunnelAddressEndpointResponse415
    | PatchVPNWireGuardTunnelAddressEndpointResponse422
    | PatchVPNWireGuardTunnelAddressEndpointResponse424
    | PatchVPNWireGuardTunnelAddressEndpointResponse500
    | PatchVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-patch ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelAddressEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNWireGuardTunnelAddressEndpointResponse400 | PatchVPNWireGuardTunnelAddressEndpointResponse401 | PatchVPNWireGuardTunnelAddressEndpointResponse403 | PatchVPNWireGuardTunnelAddressEndpointResponse404 | PatchVPNWireGuardTunnelAddressEndpointResponse405 | PatchVPNWireGuardTunnelAddressEndpointResponse406 | PatchVPNWireGuardTunnelAddressEndpointResponse409 | PatchVPNWireGuardTunnelAddressEndpointResponse415 | PatchVPNWireGuardTunnelAddressEndpointResponse422 | PatchVPNWireGuardTunnelAddressEndpointResponse424 | PatchVPNWireGuardTunnelAddressEndpointResponse500 | PatchVPNWireGuardTunnelAddressEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
