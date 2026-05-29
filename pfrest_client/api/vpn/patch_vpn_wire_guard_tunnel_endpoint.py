from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpn_wire_guard_tunnel_endpoint_data_body import PatchVPNWireGuardTunnelEndpointDataBody
from ...models.patch_vpn_wire_guard_tunnel_endpoint_json_body import PatchVPNWireGuardTunnelEndpointJsonBody
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_400 import PatchVPNWireGuardTunnelEndpointResponse400
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_401 import PatchVPNWireGuardTunnelEndpointResponse401
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_403 import PatchVPNWireGuardTunnelEndpointResponse403
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_404 import PatchVPNWireGuardTunnelEndpointResponse404
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_405 import PatchVPNWireGuardTunnelEndpointResponse405
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_406 import PatchVPNWireGuardTunnelEndpointResponse406
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_409 import PatchVPNWireGuardTunnelEndpointResponse409
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_415 import PatchVPNWireGuardTunnelEndpointResponse415
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_422 import PatchVPNWireGuardTunnelEndpointResponse422
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_424 import PatchVPNWireGuardTunnelEndpointResponse424
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_500 import PatchVPNWireGuardTunnelEndpointResponse500
from ...models.patch_vpn_wire_guard_tunnel_endpoint_response_503 import PatchVPNWireGuardTunnelEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNWireGuardTunnelEndpointJsonBody | PatchVPNWireGuardTunnelEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/wireguard/tunnel",
    }

    if isinstance(body, PatchVPNWireGuardTunnelEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNWireGuardTunnelEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNWireGuardTunnelEndpointResponse400
    | PatchVPNWireGuardTunnelEndpointResponse401
    | PatchVPNWireGuardTunnelEndpointResponse403
    | PatchVPNWireGuardTunnelEndpointResponse404
    | PatchVPNWireGuardTunnelEndpointResponse405
    | PatchVPNWireGuardTunnelEndpointResponse406
    | PatchVPNWireGuardTunnelEndpointResponse409
    | PatchVPNWireGuardTunnelEndpointResponse415
    | PatchVPNWireGuardTunnelEndpointResponse422
    | PatchVPNWireGuardTunnelEndpointResponse424
    | PatchVPNWireGuardTunnelEndpointResponse500
    | PatchVPNWireGuardTunnelEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNWireGuardTunnelEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNWireGuardTunnelEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNWireGuardTunnelEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNWireGuardTunnelEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNWireGuardTunnelEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNWireGuardTunnelEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNWireGuardTunnelEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNWireGuardTunnelEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNWireGuardTunnelEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNWireGuardTunnelEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNWireGuardTunnelEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNWireGuardTunnelEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNWireGuardTunnelEndpointResponse400
    | PatchVPNWireGuardTunnelEndpointResponse401
    | PatchVPNWireGuardTunnelEndpointResponse403
    | PatchVPNWireGuardTunnelEndpointResponse404
    | PatchVPNWireGuardTunnelEndpointResponse405
    | PatchVPNWireGuardTunnelEndpointResponse406
    | PatchVPNWireGuardTunnelEndpointResponse409
    | PatchVPNWireGuardTunnelEndpointResponse415
    | PatchVPNWireGuardTunnelEndpointResponse422
    | PatchVPNWireGuardTunnelEndpointResponse424
    | PatchVPNWireGuardTunnelEndpointResponse500
    | PatchVPNWireGuardTunnelEndpointResponse503
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
    body: PatchVPNWireGuardTunnelEndpointJsonBody | PatchVPNWireGuardTunnelEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNWireGuardTunnelEndpointResponse400
    | PatchVPNWireGuardTunnelEndpointResponse401
    | PatchVPNWireGuardTunnelEndpointResponse403
    | PatchVPNWireGuardTunnelEndpointResponse404
    | PatchVPNWireGuardTunnelEndpointResponse405
    | PatchVPNWireGuardTunnelEndpointResponse406
    | PatchVPNWireGuardTunnelEndpointResponse409
    | PatchVPNWireGuardTunnelEndpointResponse415
    | PatchVPNWireGuardTunnelEndpointResponse422
    | PatchVPNWireGuardTunnelEndpointResponse424
    | PatchVPNWireGuardTunnelEndpointResponse500
    | PatchVPNWireGuardTunnelEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-patch ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNWireGuardTunnelEndpointResponse400 | PatchVPNWireGuardTunnelEndpointResponse401 | PatchVPNWireGuardTunnelEndpointResponse403 | PatchVPNWireGuardTunnelEndpointResponse404 | PatchVPNWireGuardTunnelEndpointResponse405 | PatchVPNWireGuardTunnelEndpointResponse406 | PatchVPNWireGuardTunnelEndpointResponse409 | PatchVPNWireGuardTunnelEndpointResponse415 | PatchVPNWireGuardTunnelEndpointResponse422 | PatchVPNWireGuardTunnelEndpointResponse424 | PatchVPNWireGuardTunnelEndpointResponse500 | PatchVPNWireGuardTunnelEndpointResponse503]
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
    body: PatchVPNWireGuardTunnelEndpointJsonBody | PatchVPNWireGuardTunnelEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNWireGuardTunnelEndpointResponse400
    | PatchVPNWireGuardTunnelEndpointResponse401
    | PatchVPNWireGuardTunnelEndpointResponse403
    | PatchVPNWireGuardTunnelEndpointResponse404
    | PatchVPNWireGuardTunnelEndpointResponse405
    | PatchVPNWireGuardTunnelEndpointResponse406
    | PatchVPNWireGuardTunnelEndpointResponse409
    | PatchVPNWireGuardTunnelEndpointResponse415
    | PatchVPNWireGuardTunnelEndpointResponse422
    | PatchVPNWireGuardTunnelEndpointResponse424
    | PatchVPNWireGuardTunnelEndpointResponse500
    | PatchVPNWireGuardTunnelEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-patch ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNWireGuardTunnelEndpointResponse400 | PatchVPNWireGuardTunnelEndpointResponse401 | PatchVPNWireGuardTunnelEndpointResponse403 | PatchVPNWireGuardTunnelEndpointResponse404 | PatchVPNWireGuardTunnelEndpointResponse405 | PatchVPNWireGuardTunnelEndpointResponse406 | PatchVPNWireGuardTunnelEndpointResponse409 | PatchVPNWireGuardTunnelEndpointResponse415 | PatchVPNWireGuardTunnelEndpointResponse422 | PatchVPNWireGuardTunnelEndpointResponse424 | PatchVPNWireGuardTunnelEndpointResponse500 | PatchVPNWireGuardTunnelEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNWireGuardTunnelEndpointJsonBody | PatchVPNWireGuardTunnelEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNWireGuardTunnelEndpointResponse400
    | PatchVPNWireGuardTunnelEndpointResponse401
    | PatchVPNWireGuardTunnelEndpointResponse403
    | PatchVPNWireGuardTunnelEndpointResponse404
    | PatchVPNWireGuardTunnelEndpointResponse405
    | PatchVPNWireGuardTunnelEndpointResponse406
    | PatchVPNWireGuardTunnelEndpointResponse409
    | PatchVPNWireGuardTunnelEndpointResponse415
    | PatchVPNWireGuardTunnelEndpointResponse422
    | PatchVPNWireGuardTunnelEndpointResponse424
    | PatchVPNWireGuardTunnelEndpointResponse500
    | PatchVPNWireGuardTunnelEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-patch ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNWireGuardTunnelEndpointResponse400 | PatchVPNWireGuardTunnelEndpointResponse401 | PatchVPNWireGuardTunnelEndpointResponse403 | PatchVPNWireGuardTunnelEndpointResponse404 | PatchVPNWireGuardTunnelEndpointResponse405 | PatchVPNWireGuardTunnelEndpointResponse406 | PatchVPNWireGuardTunnelEndpointResponse409 | PatchVPNWireGuardTunnelEndpointResponse415 | PatchVPNWireGuardTunnelEndpointResponse422 | PatchVPNWireGuardTunnelEndpointResponse424 | PatchVPNWireGuardTunnelEndpointResponse500 | PatchVPNWireGuardTunnelEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNWireGuardTunnelEndpointJsonBody | PatchVPNWireGuardTunnelEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNWireGuardTunnelEndpointResponse400
    | PatchVPNWireGuardTunnelEndpointResponse401
    | PatchVPNWireGuardTunnelEndpointResponse403
    | PatchVPNWireGuardTunnelEndpointResponse404
    | PatchVPNWireGuardTunnelEndpointResponse405
    | PatchVPNWireGuardTunnelEndpointResponse406
    | PatchVPNWireGuardTunnelEndpointResponse409
    | PatchVPNWireGuardTunnelEndpointResponse415
    | PatchVPNWireGuardTunnelEndpointResponse422
    | PatchVPNWireGuardTunnelEndpointResponse424
    | PatchVPNWireGuardTunnelEndpointResponse500
    | PatchVPNWireGuardTunnelEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing WireGuard Tunnel.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-patch ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardTunnelEndpointJsonBody | Unset):
        body (PatchVPNWireGuardTunnelEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNWireGuardTunnelEndpointResponse400 | PatchVPNWireGuardTunnelEndpointResponse401 | PatchVPNWireGuardTunnelEndpointResponse403 | PatchVPNWireGuardTunnelEndpointResponse404 | PatchVPNWireGuardTunnelEndpointResponse405 | PatchVPNWireGuardTunnelEndpointResponse406 | PatchVPNWireGuardTunnelEndpointResponse409 | PatchVPNWireGuardTunnelEndpointResponse415 | PatchVPNWireGuardTunnelEndpointResponse422 | PatchVPNWireGuardTunnelEndpointResponse424 | PatchVPNWireGuardTunnelEndpointResponse500 | PatchVPNWireGuardTunnelEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
