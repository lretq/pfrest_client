from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpn_wire_guard_settings_endpoint_response_400 import GetVPNWireGuardSettingsEndpointResponse400
from ...models.get_vpn_wire_guard_settings_endpoint_response_401 import GetVPNWireGuardSettingsEndpointResponse401
from ...models.get_vpn_wire_guard_settings_endpoint_response_403 import GetVPNWireGuardSettingsEndpointResponse403
from ...models.get_vpn_wire_guard_settings_endpoint_response_404 import GetVPNWireGuardSettingsEndpointResponse404
from ...models.get_vpn_wire_guard_settings_endpoint_response_405 import GetVPNWireGuardSettingsEndpointResponse405
from ...models.get_vpn_wire_guard_settings_endpoint_response_406 import GetVPNWireGuardSettingsEndpointResponse406
from ...models.get_vpn_wire_guard_settings_endpoint_response_409 import GetVPNWireGuardSettingsEndpointResponse409
from ...models.get_vpn_wire_guard_settings_endpoint_response_415 import GetVPNWireGuardSettingsEndpointResponse415
from ...models.get_vpn_wire_guard_settings_endpoint_response_422 import GetVPNWireGuardSettingsEndpointResponse422
from ...models.get_vpn_wire_guard_settings_endpoint_response_424 import GetVPNWireGuardSettingsEndpointResponse424
from ...models.get_vpn_wire_guard_settings_endpoint_response_500 import GetVPNWireGuardSettingsEndpointResponse500
from ...models.get_vpn_wire_guard_settings_endpoint_response_503 import GetVPNWireGuardSettingsEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/vpn/wireguard/settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNWireGuardSettingsEndpointResponse400
    | GetVPNWireGuardSettingsEndpointResponse401
    | GetVPNWireGuardSettingsEndpointResponse403
    | GetVPNWireGuardSettingsEndpointResponse404
    | GetVPNWireGuardSettingsEndpointResponse405
    | GetVPNWireGuardSettingsEndpointResponse406
    | GetVPNWireGuardSettingsEndpointResponse409
    | GetVPNWireGuardSettingsEndpointResponse415
    | GetVPNWireGuardSettingsEndpointResponse422
    | GetVPNWireGuardSettingsEndpointResponse424
    | GetVPNWireGuardSettingsEndpointResponse500
    | GetVPNWireGuardSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNWireGuardSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNWireGuardSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNWireGuardSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNWireGuardSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNWireGuardSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNWireGuardSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNWireGuardSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNWireGuardSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNWireGuardSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNWireGuardSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNWireGuardSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNWireGuardSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNWireGuardSettingsEndpointResponse400
    | GetVPNWireGuardSettingsEndpointResponse401
    | GetVPNWireGuardSettingsEndpointResponse403
    | GetVPNWireGuardSettingsEndpointResponse404
    | GetVPNWireGuardSettingsEndpointResponse405
    | GetVPNWireGuardSettingsEndpointResponse406
    | GetVPNWireGuardSettingsEndpointResponse409
    | GetVPNWireGuardSettingsEndpointResponse415
    | GetVPNWireGuardSettingsEndpointResponse422
    | GetVPNWireGuardSettingsEndpointResponse424
    | GetVPNWireGuardSettingsEndpointResponse500
    | GetVPNWireGuardSettingsEndpointResponse503
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
    GetVPNWireGuardSettingsEndpointResponse400
    | GetVPNWireGuardSettingsEndpointResponse401
    | GetVPNWireGuardSettingsEndpointResponse403
    | GetVPNWireGuardSettingsEndpointResponse404
    | GetVPNWireGuardSettingsEndpointResponse405
    | GetVPNWireGuardSettingsEndpointResponse406
    | GetVPNWireGuardSettingsEndpointResponse409
    | GetVPNWireGuardSettingsEndpointResponse415
    | GetVPNWireGuardSettingsEndpointResponse422
    | GetVPNWireGuardSettingsEndpointResponse424
    | GetVPNWireGuardSettingsEndpointResponse500
    | GetVPNWireGuardSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current WireGuard Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNWireGuardSettingsEndpointResponse400 | GetVPNWireGuardSettingsEndpointResponse401 | GetVPNWireGuardSettingsEndpointResponse403 | GetVPNWireGuardSettingsEndpointResponse404 | GetVPNWireGuardSettingsEndpointResponse405 | GetVPNWireGuardSettingsEndpointResponse406 | GetVPNWireGuardSettingsEndpointResponse409 | GetVPNWireGuardSettingsEndpointResponse415 | GetVPNWireGuardSettingsEndpointResponse422 | GetVPNWireGuardSettingsEndpointResponse424 | GetVPNWireGuardSettingsEndpointResponse500 | GetVPNWireGuardSettingsEndpointResponse503]
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
    GetVPNWireGuardSettingsEndpointResponse400
    | GetVPNWireGuardSettingsEndpointResponse401
    | GetVPNWireGuardSettingsEndpointResponse403
    | GetVPNWireGuardSettingsEndpointResponse404
    | GetVPNWireGuardSettingsEndpointResponse405
    | GetVPNWireGuardSettingsEndpointResponse406
    | GetVPNWireGuardSettingsEndpointResponse409
    | GetVPNWireGuardSettingsEndpointResponse415
    | GetVPNWireGuardSettingsEndpointResponse422
    | GetVPNWireGuardSettingsEndpointResponse424
    | GetVPNWireGuardSettingsEndpointResponse500
    | GetVPNWireGuardSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current WireGuard Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNWireGuardSettingsEndpointResponse400 | GetVPNWireGuardSettingsEndpointResponse401 | GetVPNWireGuardSettingsEndpointResponse403 | GetVPNWireGuardSettingsEndpointResponse404 | GetVPNWireGuardSettingsEndpointResponse405 | GetVPNWireGuardSettingsEndpointResponse406 | GetVPNWireGuardSettingsEndpointResponse409 | GetVPNWireGuardSettingsEndpointResponse415 | GetVPNWireGuardSettingsEndpointResponse422 | GetVPNWireGuardSettingsEndpointResponse424 | GetVPNWireGuardSettingsEndpointResponse500 | GetVPNWireGuardSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetVPNWireGuardSettingsEndpointResponse400
    | GetVPNWireGuardSettingsEndpointResponse401
    | GetVPNWireGuardSettingsEndpointResponse403
    | GetVPNWireGuardSettingsEndpointResponse404
    | GetVPNWireGuardSettingsEndpointResponse405
    | GetVPNWireGuardSettingsEndpointResponse406
    | GetVPNWireGuardSettingsEndpointResponse409
    | GetVPNWireGuardSettingsEndpointResponse415
    | GetVPNWireGuardSettingsEndpointResponse422
    | GetVPNWireGuardSettingsEndpointResponse424
    | GetVPNWireGuardSettingsEndpointResponse500
    | GetVPNWireGuardSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current WireGuard Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNWireGuardSettingsEndpointResponse400 | GetVPNWireGuardSettingsEndpointResponse401 | GetVPNWireGuardSettingsEndpointResponse403 | GetVPNWireGuardSettingsEndpointResponse404 | GetVPNWireGuardSettingsEndpointResponse405 | GetVPNWireGuardSettingsEndpointResponse406 | GetVPNWireGuardSettingsEndpointResponse409 | GetVPNWireGuardSettingsEndpointResponse415 | GetVPNWireGuardSettingsEndpointResponse422 | GetVPNWireGuardSettingsEndpointResponse424 | GetVPNWireGuardSettingsEndpointResponse500 | GetVPNWireGuardSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetVPNWireGuardSettingsEndpointResponse400
    | GetVPNWireGuardSettingsEndpointResponse401
    | GetVPNWireGuardSettingsEndpointResponse403
    | GetVPNWireGuardSettingsEndpointResponse404
    | GetVPNWireGuardSettingsEndpointResponse405
    | GetVPNWireGuardSettingsEndpointResponse406
    | GetVPNWireGuardSettingsEndpointResponse409
    | GetVPNWireGuardSettingsEndpointResponse415
    | GetVPNWireGuardSettingsEndpointResponse422
    | GetVPNWireGuardSettingsEndpointResponse424
    | GetVPNWireGuardSettingsEndpointResponse500
    | GetVPNWireGuardSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current WireGuard Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNWireGuardSettingsEndpointResponse400 | GetVPNWireGuardSettingsEndpointResponse401 | GetVPNWireGuardSettingsEndpointResponse403 | GetVPNWireGuardSettingsEndpointResponse404 | GetVPNWireGuardSettingsEndpointResponse405 | GetVPNWireGuardSettingsEndpointResponse406 | GetVPNWireGuardSettingsEndpointResponse409 | GetVPNWireGuardSettingsEndpointResponse415 | GetVPNWireGuardSettingsEndpointResponse422 | GetVPNWireGuardSettingsEndpointResponse424 | GetVPNWireGuardSettingsEndpointResponse500 | GetVPNWireGuardSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
