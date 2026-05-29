from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_data_body import (
    PostVPNWireGuardPeerAllowedIPEndpointDataBody,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_json_body import (
    PostVPNWireGuardPeerAllowedIPEndpointJsonBody,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_400 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse400,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_401 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse401,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_403 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse403,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_404 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse404,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_405 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse405,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_406 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse406,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_409 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse409,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_415 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse415,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_422 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse422,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_424 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse424,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_500 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse500,
)
from ...models.post_vpn_wire_guard_peer_allowed_ip_endpoint_response_503 import (
    PostVPNWireGuardPeerAllowedIPEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNWireGuardPeerAllowedIPEndpointJsonBody | PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/wireguard/peer/allowed_ip",
    }

    if isinstance(body, PostVPNWireGuardPeerAllowedIPEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNWireGuardPeerAllowedIPEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNWireGuardPeerAllowedIPEndpointResponse400
    | PostVPNWireGuardPeerAllowedIPEndpointResponse401
    | PostVPNWireGuardPeerAllowedIPEndpointResponse403
    | PostVPNWireGuardPeerAllowedIPEndpointResponse404
    | PostVPNWireGuardPeerAllowedIPEndpointResponse405
    | PostVPNWireGuardPeerAllowedIPEndpointResponse406
    | PostVPNWireGuardPeerAllowedIPEndpointResponse409
    | PostVPNWireGuardPeerAllowedIPEndpointResponse415
    | PostVPNWireGuardPeerAllowedIPEndpointResponse422
    | PostVPNWireGuardPeerAllowedIPEndpointResponse424
    | PostVPNWireGuardPeerAllowedIPEndpointResponse500
    | PostVPNWireGuardPeerAllowedIPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNWireGuardPeerAllowedIPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNWireGuardPeerAllowedIPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNWireGuardPeerAllowedIPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNWireGuardPeerAllowedIPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNWireGuardPeerAllowedIPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNWireGuardPeerAllowedIPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNWireGuardPeerAllowedIPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNWireGuardPeerAllowedIPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNWireGuardPeerAllowedIPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNWireGuardPeerAllowedIPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNWireGuardPeerAllowedIPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNWireGuardPeerAllowedIPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNWireGuardPeerAllowedIPEndpointResponse400
    | PostVPNWireGuardPeerAllowedIPEndpointResponse401
    | PostVPNWireGuardPeerAllowedIPEndpointResponse403
    | PostVPNWireGuardPeerAllowedIPEndpointResponse404
    | PostVPNWireGuardPeerAllowedIPEndpointResponse405
    | PostVPNWireGuardPeerAllowedIPEndpointResponse406
    | PostVPNWireGuardPeerAllowedIPEndpointResponse409
    | PostVPNWireGuardPeerAllowedIPEndpointResponse415
    | PostVPNWireGuardPeerAllowedIPEndpointResponse422
    | PostVPNWireGuardPeerAllowedIPEndpointResponse424
    | PostVPNWireGuardPeerAllowedIPEndpointResponse500
    | PostVPNWireGuardPeerAllowedIPEndpointResponse503
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
    body: PostVPNWireGuardPeerAllowedIPEndpointJsonBody | PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNWireGuardPeerAllowedIPEndpointResponse400
    | PostVPNWireGuardPeerAllowedIPEndpointResponse401
    | PostVPNWireGuardPeerAllowedIPEndpointResponse403
    | PostVPNWireGuardPeerAllowedIPEndpointResponse404
    | PostVPNWireGuardPeerAllowedIPEndpointResponse405
    | PostVPNWireGuardPeerAllowedIPEndpointResponse406
    | PostVPNWireGuardPeerAllowedIPEndpointResponse409
    | PostVPNWireGuardPeerAllowedIPEndpointResponse415
    | PostVPNWireGuardPeerAllowedIPEndpointResponse422
    | PostVPNWireGuardPeerAllowedIPEndpointResponse424
    | PostVPNWireGuardPeerAllowedIPEndpointResponse500
    | PostVPNWireGuardPeerAllowedIPEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new WireGuard Peer Allowed IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeerAllowedIP<br>**Parent model**:
    WireGuardPeer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-
    allowed-ip-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardPeerAllowedIPEndpointJsonBody | Unset):
        body (PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNWireGuardPeerAllowedIPEndpointResponse400 | PostVPNWireGuardPeerAllowedIPEndpointResponse401 | PostVPNWireGuardPeerAllowedIPEndpointResponse403 | PostVPNWireGuardPeerAllowedIPEndpointResponse404 | PostVPNWireGuardPeerAllowedIPEndpointResponse405 | PostVPNWireGuardPeerAllowedIPEndpointResponse406 | PostVPNWireGuardPeerAllowedIPEndpointResponse409 | PostVPNWireGuardPeerAllowedIPEndpointResponse415 | PostVPNWireGuardPeerAllowedIPEndpointResponse422 | PostVPNWireGuardPeerAllowedIPEndpointResponse424 | PostVPNWireGuardPeerAllowedIPEndpointResponse500 | PostVPNWireGuardPeerAllowedIPEndpointResponse503]
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
    body: PostVPNWireGuardPeerAllowedIPEndpointJsonBody | PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNWireGuardPeerAllowedIPEndpointResponse400
    | PostVPNWireGuardPeerAllowedIPEndpointResponse401
    | PostVPNWireGuardPeerAllowedIPEndpointResponse403
    | PostVPNWireGuardPeerAllowedIPEndpointResponse404
    | PostVPNWireGuardPeerAllowedIPEndpointResponse405
    | PostVPNWireGuardPeerAllowedIPEndpointResponse406
    | PostVPNWireGuardPeerAllowedIPEndpointResponse409
    | PostVPNWireGuardPeerAllowedIPEndpointResponse415
    | PostVPNWireGuardPeerAllowedIPEndpointResponse422
    | PostVPNWireGuardPeerAllowedIPEndpointResponse424
    | PostVPNWireGuardPeerAllowedIPEndpointResponse500
    | PostVPNWireGuardPeerAllowedIPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new WireGuard Peer Allowed IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeerAllowedIP<br>**Parent model**:
    WireGuardPeer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-
    allowed-ip-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardPeerAllowedIPEndpointJsonBody | Unset):
        body (PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNWireGuardPeerAllowedIPEndpointResponse400 | PostVPNWireGuardPeerAllowedIPEndpointResponse401 | PostVPNWireGuardPeerAllowedIPEndpointResponse403 | PostVPNWireGuardPeerAllowedIPEndpointResponse404 | PostVPNWireGuardPeerAllowedIPEndpointResponse405 | PostVPNWireGuardPeerAllowedIPEndpointResponse406 | PostVPNWireGuardPeerAllowedIPEndpointResponse409 | PostVPNWireGuardPeerAllowedIPEndpointResponse415 | PostVPNWireGuardPeerAllowedIPEndpointResponse422 | PostVPNWireGuardPeerAllowedIPEndpointResponse424 | PostVPNWireGuardPeerAllowedIPEndpointResponse500 | PostVPNWireGuardPeerAllowedIPEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNWireGuardPeerAllowedIPEndpointJsonBody | PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNWireGuardPeerAllowedIPEndpointResponse400
    | PostVPNWireGuardPeerAllowedIPEndpointResponse401
    | PostVPNWireGuardPeerAllowedIPEndpointResponse403
    | PostVPNWireGuardPeerAllowedIPEndpointResponse404
    | PostVPNWireGuardPeerAllowedIPEndpointResponse405
    | PostVPNWireGuardPeerAllowedIPEndpointResponse406
    | PostVPNWireGuardPeerAllowedIPEndpointResponse409
    | PostVPNWireGuardPeerAllowedIPEndpointResponse415
    | PostVPNWireGuardPeerAllowedIPEndpointResponse422
    | PostVPNWireGuardPeerAllowedIPEndpointResponse424
    | PostVPNWireGuardPeerAllowedIPEndpointResponse500
    | PostVPNWireGuardPeerAllowedIPEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new WireGuard Peer Allowed IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeerAllowedIP<br>**Parent model**:
    WireGuardPeer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-
    allowed-ip-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardPeerAllowedIPEndpointJsonBody | Unset):
        body (PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNWireGuardPeerAllowedIPEndpointResponse400 | PostVPNWireGuardPeerAllowedIPEndpointResponse401 | PostVPNWireGuardPeerAllowedIPEndpointResponse403 | PostVPNWireGuardPeerAllowedIPEndpointResponse404 | PostVPNWireGuardPeerAllowedIPEndpointResponse405 | PostVPNWireGuardPeerAllowedIPEndpointResponse406 | PostVPNWireGuardPeerAllowedIPEndpointResponse409 | PostVPNWireGuardPeerAllowedIPEndpointResponse415 | PostVPNWireGuardPeerAllowedIPEndpointResponse422 | PostVPNWireGuardPeerAllowedIPEndpointResponse424 | PostVPNWireGuardPeerAllowedIPEndpointResponse500 | PostVPNWireGuardPeerAllowedIPEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNWireGuardPeerAllowedIPEndpointJsonBody | PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNWireGuardPeerAllowedIPEndpointResponse400
    | PostVPNWireGuardPeerAllowedIPEndpointResponse401
    | PostVPNWireGuardPeerAllowedIPEndpointResponse403
    | PostVPNWireGuardPeerAllowedIPEndpointResponse404
    | PostVPNWireGuardPeerAllowedIPEndpointResponse405
    | PostVPNWireGuardPeerAllowedIPEndpointResponse406
    | PostVPNWireGuardPeerAllowedIPEndpointResponse409
    | PostVPNWireGuardPeerAllowedIPEndpointResponse415
    | PostVPNWireGuardPeerAllowedIPEndpointResponse422
    | PostVPNWireGuardPeerAllowedIPEndpointResponse424
    | PostVPNWireGuardPeerAllowedIPEndpointResponse500
    | PostVPNWireGuardPeerAllowedIPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new WireGuard Peer Allowed IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeerAllowedIP<br>**Parent model**:
    WireGuardPeer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-
    allowed-ip-post ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostVPNWireGuardPeerAllowedIPEndpointJsonBody | Unset):
        body (PostVPNWireGuardPeerAllowedIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNWireGuardPeerAllowedIPEndpointResponse400 | PostVPNWireGuardPeerAllowedIPEndpointResponse401 | PostVPNWireGuardPeerAllowedIPEndpointResponse403 | PostVPNWireGuardPeerAllowedIPEndpointResponse404 | PostVPNWireGuardPeerAllowedIPEndpointResponse405 | PostVPNWireGuardPeerAllowedIPEndpointResponse406 | PostVPNWireGuardPeerAllowedIPEndpointResponse409 | PostVPNWireGuardPeerAllowedIPEndpointResponse415 | PostVPNWireGuardPeerAllowedIPEndpointResponse422 | PostVPNWireGuardPeerAllowedIPEndpointResponse424 | PostVPNWireGuardPeerAllowedIPEndpointResponse500 | PostVPNWireGuardPeerAllowedIPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
