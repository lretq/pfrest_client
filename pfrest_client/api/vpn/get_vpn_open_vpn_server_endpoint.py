from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpn_open_vpn_server_endpoint_response_400 import GetVPNOpenVPNServerEndpointResponse400
from ...models.get_vpn_open_vpn_server_endpoint_response_401 import GetVPNOpenVPNServerEndpointResponse401
from ...models.get_vpn_open_vpn_server_endpoint_response_403 import GetVPNOpenVPNServerEndpointResponse403
from ...models.get_vpn_open_vpn_server_endpoint_response_404 import GetVPNOpenVPNServerEndpointResponse404
from ...models.get_vpn_open_vpn_server_endpoint_response_405 import GetVPNOpenVPNServerEndpointResponse405
from ...models.get_vpn_open_vpn_server_endpoint_response_406 import GetVPNOpenVPNServerEndpointResponse406
from ...models.get_vpn_open_vpn_server_endpoint_response_409 import GetVPNOpenVPNServerEndpointResponse409
from ...models.get_vpn_open_vpn_server_endpoint_response_415 import GetVPNOpenVPNServerEndpointResponse415
from ...models.get_vpn_open_vpn_server_endpoint_response_422 import GetVPNOpenVPNServerEndpointResponse422
from ...models.get_vpn_open_vpn_server_endpoint_response_424 import GetVPNOpenVPNServerEndpointResponse424
from ...models.get_vpn_open_vpn_server_endpoint_response_500 import GetVPNOpenVPNServerEndpointResponse500
from ...models.get_vpn_open_vpn_server_endpoint_response_503 import GetVPNOpenVPNServerEndpointResponse503
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
        "url": "/api/v2/vpn/openvpn/server",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNOpenVPNServerEndpointResponse400
    | GetVPNOpenVPNServerEndpointResponse401
    | GetVPNOpenVPNServerEndpointResponse403
    | GetVPNOpenVPNServerEndpointResponse404
    | GetVPNOpenVPNServerEndpointResponse405
    | GetVPNOpenVPNServerEndpointResponse406
    | GetVPNOpenVPNServerEndpointResponse409
    | GetVPNOpenVPNServerEndpointResponse415
    | GetVPNOpenVPNServerEndpointResponse422
    | GetVPNOpenVPNServerEndpointResponse424
    | GetVPNOpenVPNServerEndpointResponse500
    | GetVPNOpenVPNServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNOpenVPNServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNOpenVPNServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNOpenVPNServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNOpenVPNServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNOpenVPNServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNOpenVPNServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNOpenVPNServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNOpenVPNServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNOpenVPNServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNOpenVPNServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNOpenVPNServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNOpenVPNServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNOpenVPNServerEndpointResponse400
    | GetVPNOpenVPNServerEndpointResponse401
    | GetVPNOpenVPNServerEndpointResponse403
    | GetVPNOpenVPNServerEndpointResponse404
    | GetVPNOpenVPNServerEndpointResponse405
    | GetVPNOpenVPNServerEndpointResponse406
    | GetVPNOpenVPNServerEndpointResponse409
    | GetVPNOpenVPNServerEndpointResponse415
    | GetVPNOpenVPNServerEndpointResponse422
    | GetVPNOpenVPNServerEndpointResponse424
    | GetVPNOpenVPNServerEndpointResponse500
    | GetVPNOpenVPNServerEndpointResponse503
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
    GetVPNOpenVPNServerEndpointResponse400
    | GetVPNOpenVPNServerEndpointResponse401
    | GetVPNOpenVPNServerEndpointResponse403
    | GetVPNOpenVPNServerEndpointResponse404
    | GetVPNOpenVPNServerEndpointResponse405
    | GetVPNOpenVPNServerEndpointResponse406
    | GetVPNOpenVPNServerEndpointResponse409
    | GetVPNOpenVPNServerEndpointResponse415
    | GetVPNOpenVPNServerEndpointResponse422
    | GetVPNOpenVPNServerEndpointResponse424
    | GetVPNOpenVPNServerEndpointResponse500
    | GetVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNOpenVPNServerEndpointResponse400 | GetVPNOpenVPNServerEndpointResponse401 | GetVPNOpenVPNServerEndpointResponse403 | GetVPNOpenVPNServerEndpointResponse404 | GetVPNOpenVPNServerEndpointResponse405 | GetVPNOpenVPNServerEndpointResponse406 | GetVPNOpenVPNServerEndpointResponse409 | GetVPNOpenVPNServerEndpointResponse415 | GetVPNOpenVPNServerEndpointResponse422 | GetVPNOpenVPNServerEndpointResponse424 | GetVPNOpenVPNServerEndpointResponse500 | GetVPNOpenVPNServerEndpointResponse503]
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
    GetVPNOpenVPNServerEndpointResponse400
    | GetVPNOpenVPNServerEndpointResponse401
    | GetVPNOpenVPNServerEndpointResponse403
    | GetVPNOpenVPNServerEndpointResponse404
    | GetVPNOpenVPNServerEndpointResponse405
    | GetVPNOpenVPNServerEndpointResponse406
    | GetVPNOpenVPNServerEndpointResponse409
    | GetVPNOpenVPNServerEndpointResponse415
    | GetVPNOpenVPNServerEndpointResponse422
    | GetVPNOpenVPNServerEndpointResponse424
    | GetVPNOpenVPNServerEndpointResponse500
    | GetVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNOpenVPNServerEndpointResponse400 | GetVPNOpenVPNServerEndpointResponse401 | GetVPNOpenVPNServerEndpointResponse403 | GetVPNOpenVPNServerEndpointResponse404 | GetVPNOpenVPNServerEndpointResponse405 | GetVPNOpenVPNServerEndpointResponse406 | GetVPNOpenVPNServerEndpointResponse409 | GetVPNOpenVPNServerEndpointResponse415 | GetVPNOpenVPNServerEndpointResponse422 | GetVPNOpenVPNServerEndpointResponse424 | GetVPNOpenVPNServerEndpointResponse500 | GetVPNOpenVPNServerEndpointResponse503
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
    GetVPNOpenVPNServerEndpointResponse400
    | GetVPNOpenVPNServerEndpointResponse401
    | GetVPNOpenVPNServerEndpointResponse403
    | GetVPNOpenVPNServerEndpointResponse404
    | GetVPNOpenVPNServerEndpointResponse405
    | GetVPNOpenVPNServerEndpointResponse406
    | GetVPNOpenVPNServerEndpointResponse409
    | GetVPNOpenVPNServerEndpointResponse415
    | GetVPNOpenVPNServerEndpointResponse422
    | GetVPNOpenVPNServerEndpointResponse424
    | GetVPNOpenVPNServerEndpointResponse500
    | GetVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNOpenVPNServerEndpointResponse400 | GetVPNOpenVPNServerEndpointResponse401 | GetVPNOpenVPNServerEndpointResponse403 | GetVPNOpenVPNServerEndpointResponse404 | GetVPNOpenVPNServerEndpointResponse405 | GetVPNOpenVPNServerEndpointResponse406 | GetVPNOpenVPNServerEndpointResponse409 | GetVPNOpenVPNServerEndpointResponse415 | GetVPNOpenVPNServerEndpointResponse422 | GetVPNOpenVPNServerEndpointResponse424 | GetVPNOpenVPNServerEndpointResponse500 | GetVPNOpenVPNServerEndpointResponse503]
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
    GetVPNOpenVPNServerEndpointResponse400
    | GetVPNOpenVPNServerEndpointResponse401
    | GetVPNOpenVPNServerEndpointResponse403
    | GetVPNOpenVPNServerEndpointResponse404
    | GetVPNOpenVPNServerEndpointResponse405
    | GetVPNOpenVPNServerEndpointResponse406
    | GetVPNOpenVPNServerEndpointResponse409
    | GetVPNOpenVPNServerEndpointResponse415
    | GetVPNOpenVPNServerEndpointResponse422
    | GetVPNOpenVPNServerEndpointResponse424
    | GetVPNOpenVPNServerEndpointResponse500
    | GetVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNOpenVPNServerEndpointResponse400 | GetVPNOpenVPNServerEndpointResponse401 | GetVPNOpenVPNServerEndpointResponse403 | GetVPNOpenVPNServerEndpointResponse404 | GetVPNOpenVPNServerEndpointResponse405 | GetVPNOpenVPNServerEndpointResponse406 | GetVPNOpenVPNServerEndpointResponse409 | GetVPNOpenVPNServerEndpointResponse415 | GetVPNOpenVPNServerEndpointResponse422 | GetVPNOpenVPNServerEndpointResponse424 | GetVPNOpenVPNServerEndpointResponse500 | GetVPNOpenVPNServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
