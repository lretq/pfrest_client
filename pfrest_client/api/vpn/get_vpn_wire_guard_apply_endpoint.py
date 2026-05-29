from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpn_wire_guard_apply_endpoint_response_400 import GetVPNWireGuardApplyEndpointResponse400
from ...models.get_vpn_wire_guard_apply_endpoint_response_401 import GetVPNWireGuardApplyEndpointResponse401
from ...models.get_vpn_wire_guard_apply_endpoint_response_403 import GetVPNWireGuardApplyEndpointResponse403
from ...models.get_vpn_wire_guard_apply_endpoint_response_404 import GetVPNWireGuardApplyEndpointResponse404
from ...models.get_vpn_wire_guard_apply_endpoint_response_405 import GetVPNWireGuardApplyEndpointResponse405
from ...models.get_vpn_wire_guard_apply_endpoint_response_406 import GetVPNWireGuardApplyEndpointResponse406
from ...models.get_vpn_wire_guard_apply_endpoint_response_409 import GetVPNWireGuardApplyEndpointResponse409
from ...models.get_vpn_wire_guard_apply_endpoint_response_415 import GetVPNWireGuardApplyEndpointResponse415
from ...models.get_vpn_wire_guard_apply_endpoint_response_422 import GetVPNWireGuardApplyEndpointResponse422
from ...models.get_vpn_wire_guard_apply_endpoint_response_424 import GetVPNWireGuardApplyEndpointResponse424
from ...models.get_vpn_wire_guard_apply_endpoint_response_500 import GetVPNWireGuardApplyEndpointResponse500
from ...models.get_vpn_wire_guard_apply_endpoint_response_503 import GetVPNWireGuardApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/vpn/wireguard/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNWireGuardApplyEndpointResponse400
    | GetVPNWireGuardApplyEndpointResponse401
    | GetVPNWireGuardApplyEndpointResponse403
    | GetVPNWireGuardApplyEndpointResponse404
    | GetVPNWireGuardApplyEndpointResponse405
    | GetVPNWireGuardApplyEndpointResponse406
    | GetVPNWireGuardApplyEndpointResponse409
    | GetVPNWireGuardApplyEndpointResponse415
    | GetVPNWireGuardApplyEndpointResponse422
    | GetVPNWireGuardApplyEndpointResponse424
    | GetVPNWireGuardApplyEndpointResponse500
    | GetVPNWireGuardApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNWireGuardApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNWireGuardApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNWireGuardApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNWireGuardApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNWireGuardApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNWireGuardApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNWireGuardApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNWireGuardApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNWireGuardApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNWireGuardApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNWireGuardApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNWireGuardApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNWireGuardApplyEndpointResponse400
    | GetVPNWireGuardApplyEndpointResponse401
    | GetVPNWireGuardApplyEndpointResponse403
    | GetVPNWireGuardApplyEndpointResponse404
    | GetVPNWireGuardApplyEndpointResponse405
    | GetVPNWireGuardApplyEndpointResponse406
    | GetVPNWireGuardApplyEndpointResponse409
    | GetVPNWireGuardApplyEndpointResponse415
    | GetVPNWireGuardApplyEndpointResponse422
    | GetVPNWireGuardApplyEndpointResponse424
    | GetVPNWireGuardApplyEndpointResponse500
    | GetVPNWireGuardApplyEndpointResponse503
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
    GetVPNWireGuardApplyEndpointResponse400
    | GetVPNWireGuardApplyEndpointResponse401
    | GetVPNWireGuardApplyEndpointResponse403
    | GetVPNWireGuardApplyEndpointResponse404
    | GetVPNWireGuardApplyEndpointResponse405
    | GetVPNWireGuardApplyEndpointResponse406
    | GetVPNWireGuardApplyEndpointResponse409
    | GetVPNWireGuardApplyEndpointResponse415
    | GetVPNWireGuardApplyEndpointResponse422
    | GetVPNWireGuardApplyEndpointResponse424
    | GetVPNWireGuardApplyEndpointResponse500
    | GetVPNWireGuardApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending WireGuard change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-apply-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNWireGuardApplyEndpointResponse400 | GetVPNWireGuardApplyEndpointResponse401 | GetVPNWireGuardApplyEndpointResponse403 | GetVPNWireGuardApplyEndpointResponse404 | GetVPNWireGuardApplyEndpointResponse405 | GetVPNWireGuardApplyEndpointResponse406 | GetVPNWireGuardApplyEndpointResponse409 | GetVPNWireGuardApplyEndpointResponse415 | GetVPNWireGuardApplyEndpointResponse422 | GetVPNWireGuardApplyEndpointResponse424 | GetVPNWireGuardApplyEndpointResponse500 | GetVPNWireGuardApplyEndpointResponse503]
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
    GetVPNWireGuardApplyEndpointResponse400
    | GetVPNWireGuardApplyEndpointResponse401
    | GetVPNWireGuardApplyEndpointResponse403
    | GetVPNWireGuardApplyEndpointResponse404
    | GetVPNWireGuardApplyEndpointResponse405
    | GetVPNWireGuardApplyEndpointResponse406
    | GetVPNWireGuardApplyEndpointResponse409
    | GetVPNWireGuardApplyEndpointResponse415
    | GetVPNWireGuardApplyEndpointResponse422
    | GetVPNWireGuardApplyEndpointResponse424
    | GetVPNWireGuardApplyEndpointResponse500
    | GetVPNWireGuardApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending WireGuard change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-apply-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNWireGuardApplyEndpointResponse400 | GetVPNWireGuardApplyEndpointResponse401 | GetVPNWireGuardApplyEndpointResponse403 | GetVPNWireGuardApplyEndpointResponse404 | GetVPNWireGuardApplyEndpointResponse405 | GetVPNWireGuardApplyEndpointResponse406 | GetVPNWireGuardApplyEndpointResponse409 | GetVPNWireGuardApplyEndpointResponse415 | GetVPNWireGuardApplyEndpointResponse422 | GetVPNWireGuardApplyEndpointResponse424 | GetVPNWireGuardApplyEndpointResponse500 | GetVPNWireGuardApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetVPNWireGuardApplyEndpointResponse400
    | GetVPNWireGuardApplyEndpointResponse401
    | GetVPNWireGuardApplyEndpointResponse403
    | GetVPNWireGuardApplyEndpointResponse404
    | GetVPNWireGuardApplyEndpointResponse405
    | GetVPNWireGuardApplyEndpointResponse406
    | GetVPNWireGuardApplyEndpointResponse409
    | GetVPNWireGuardApplyEndpointResponse415
    | GetVPNWireGuardApplyEndpointResponse422
    | GetVPNWireGuardApplyEndpointResponse424
    | GetVPNWireGuardApplyEndpointResponse500
    | GetVPNWireGuardApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending WireGuard change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-apply-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNWireGuardApplyEndpointResponse400 | GetVPNWireGuardApplyEndpointResponse401 | GetVPNWireGuardApplyEndpointResponse403 | GetVPNWireGuardApplyEndpointResponse404 | GetVPNWireGuardApplyEndpointResponse405 | GetVPNWireGuardApplyEndpointResponse406 | GetVPNWireGuardApplyEndpointResponse409 | GetVPNWireGuardApplyEndpointResponse415 | GetVPNWireGuardApplyEndpointResponse422 | GetVPNWireGuardApplyEndpointResponse424 | GetVPNWireGuardApplyEndpointResponse500 | GetVPNWireGuardApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetVPNWireGuardApplyEndpointResponse400
    | GetVPNWireGuardApplyEndpointResponse401
    | GetVPNWireGuardApplyEndpointResponse403
    | GetVPNWireGuardApplyEndpointResponse404
    | GetVPNWireGuardApplyEndpointResponse405
    | GetVPNWireGuardApplyEndpointResponse406
    | GetVPNWireGuardApplyEndpointResponse409
    | GetVPNWireGuardApplyEndpointResponse415
    | GetVPNWireGuardApplyEndpointResponse422
    | GetVPNWireGuardApplyEndpointResponse424
    | GetVPNWireGuardApplyEndpointResponse500
    | GetVPNWireGuardApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending WireGuard change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-apply-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNWireGuardApplyEndpointResponse400 | GetVPNWireGuardApplyEndpointResponse401 | GetVPNWireGuardApplyEndpointResponse403 | GetVPNWireGuardApplyEndpointResponse404 | GetVPNWireGuardApplyEndpointResponse405 | GetVPNWireGuardApplyEndpointResponse406 | GetVPNWireGuardApplyEndpointResponse409 | GetVPNWireGuardApplyEndpointResponse415 | GetVPNWireGuardApplyEndpointResponse422 | GetVPNWireGuardApplyEndpointResponse424 | GetVPNWireGuardApplyEndpointResponse500 | GetVPNWireGuardApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
