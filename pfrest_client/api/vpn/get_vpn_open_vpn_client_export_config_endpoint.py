from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_400 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse400,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_401 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse401,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_403 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse403,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_404 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse404,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_405 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse405,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_406 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse406,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_409 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse409,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_415 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse415,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_422 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse422,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_424 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse424,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_500 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse500,
)
from ...models.get_vpn_open_vpn_client_export_config_endpoint_response_503 import (
    GetVPNOpenVPNClientExportConfigEndpointResponse503,
)
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
        "url": "/api/v2/vpn/openvpn/client_export/config",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNOpenVPNClientExportConfigEndpointResponse400
    | GetVPNOpenVPNClientExportConfigEndpointResponse401
    | GetVPNOpenVPNClientExportConfigEndpointResponse403
    | GetVPNOpenVPNClientExportConfigEndpointResponse404
    | GetVPNOpenVPNClientExportConfigEndpointResponse405
    | GetVPNOpenVPNClientExportConfigEndpointResponse406
    | GetVPNOpenVPNClientExportConfigEndpointResponse409
    | GetVPNOpenVPNClientExportConfigEndpointResponse415
    | GetVPNOpenVPNClientExportConfigEndpointResponse422
    | GetVPNOpenVPNClientExportConfigEndpointResponse424
    | GetVPNOpenVPNClientExportConfigEndpointResponse500
    | GetVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNOpenVPNClientExportConfigEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNOpenVPNClientExportConfigEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNOpenVPNClientExportConfigEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNOpenVPNClientExportConfigEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNOpenVPNClientExportConfigEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNOpenVPNClientExportConfigEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNOpenVPNClientExportConfigEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNOpenVPNClientExportConfigEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNOpenVPNClientExportConfigEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNOpenVPNClientExportConfigEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNOpenVPNClientExportConfigEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNOpenVPNClientExportConfigEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNOpenVPNClientExportConfigEndpointResponse400
    | GetVPNOpenVPNClientExportConfigEndpointResponse401
    | GetVPNOpenVPNClientExportConfigEndpointResponse403
    | GetVPNOpenVPNClientExportConfigEndpointResponse404
    | GetVPNOpenVPNClientExportConfigEndpointResponse405
    | GetVPNOpenVPNClientExportConfigEndpointResponse406
    | GetVPNOpenVPNClientExportConfigEndpointResponse409
    | GetVPNOpenVPNClientExportConfigEndpointResponse415
    | GetVPNOpenVPNClientExportConfigEndpointResponse422
    | GetVPNOpenVPNClientExportConfigEndpointResponse424
    | GetVPNOpenVPNClientExportConfigEndpointResponse500
    | GetVPNOpenVPNClientExportConfigEndpointResponse503
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
    GetVPNOpenVPNClientExportConfigEndpointResponse400
    | GetVPNOpenVPNClientExportConfigEndpointResponse401
    | GetVPNOpenVPNClientExportConfigEndpointResponse403
    | GetVPNOpenVPNClientExportConfigEndpointResponse404
    | GetVPNOpenVPNClientExportConfigEndpointResponse405
    | GetVPNOpenVPNClientExportConfigEndpointResponse406
    | GetVPNOpenVPNClientExportConfigEndpointResponse409
    | GetVPNOpenVPNClientExportConfigEndpointResponse415
    | GetVPNOpenVPNClientExportConfigEndpointResponse422
    | GetVPNOpenVPNClientExportConfigEndpointResponse424
    | GetVPNOpenVPNClientExportConfigEndpointResponse500
    | GetVPNOpenVPNClientExportConfigEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    get ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNOpenVPNClientExportConfigEndpointResponse400 | GetVPNOpenVPNClientExportConfigEndpointResponse401 | GetVPNOpenVPNClientExportConfigEndpointResponse403 | GetVPNOpenVPNClientExportConfigEndpointResponse404 | GetVPNOpenVPNClientExportConfigEndpointResponse405 | GetVPNOpenVPNClientExportConfigEndpointResponse406 | GetVPNOpenVPNClientExportConfigEndpointResponse409 | GetVPNOpenVPNClientExportConfigEndpointResponse415 | GetVPNOpenVPNClientExportConfigEndpointResponse422 | GetVPNOpenVPNClientExportConfigEndpointResponse424 | GetVPNOpenVPNClientExportConfigEndpointResponse500 | GetVPNOpenVPNClientExportConfigEndpointResponse503]
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
    GetVPNOpenVPNClientExportConfigEndpointResponse400
    | GetVPNOpenVPNClientExportConfigEndpointResponse401
    | GetVPNOpenVPNClientExportConfigEndpointResponse403
    | GetVPNOpenVPNClientExportConfigEndpointResponse404
    | GetVPNOpenVPNClientExportConfigEndpointResponse405
    | GetVPNOpenVPNClientExportConfigEndpointResponse406
    | GetVPNOpenVPNClientExportConfigEndpointResponse409
    | GetVPNOpenVPNClientExportConfigEndpointResponse415
    | GetVPNOpenVPNClientExportConfigEndpointResponse422
    | GetVPNOpenVPNClientExportConfigEndpointResponse424
    | GetVPNOpenVPNClientExportConfigEndpointResponse500
    | GetVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    get ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNOpenVPNClientExportConfigEndpointResponse400 | GetVPNOpenVPNClientExportConfigEndpointResponse401 | GetVPNOpenVPNClientExportConfigEndpointResponse403 | GetVPNOpenVPNClientExportConfigEndpointResponse404 | GetVPNOpenVPNClientExportConfigEndpointResponse405 | GetVPNOpenVPNClientExportConfigEndpointResponse406 | GetVPNOpenVPNClientExportConfigEndpointResponse409 | GetVPNOpenVPNClientExportConfigEndpointResponse415 | GetVPNOpenVPNClientExportConfigEndpointResponse422 | GetVPNOpenVPNClientExportConfigEndpointResponse424 | GetVPNOpenVPNClientExportConfigEndpointResponse500 | GetVPNOpenVPNClientExportConfigEndpointResponse503
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
    GetVPNOpenVPNClientExportConfigEndpointResponse400
    | GetVPNOpenVPNClientExportConfigEndpointResponse401
    | GetVPNOpenVPNClientExportConfigEndpointResponse403
    | GetVPNOpenVPNClientExportConfigEndpointResponse404
    | GetVPNOpenVPNClientExportConfigEndpointResponse405
    | GetVPNOpenVPNClientExportConfigEndpointResponse406
    | GetVPNOpenVPNClientExportConfigEndpointResponse409
    | GetVPNOpenVPNClientExportConfigEndpointResponse415
    | GetVPNOpenVPNClientExportConfigEndpointResponse422
    | GetVPNOpenVPNClientExportConfigEndpointResponse424
    | GetVPNOpenVPNClientExportConfigEndpointResponse500
    | GetVPNOpenVPNClientExportConfigEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    get ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNOpenVPNClientExportConfigEndpointResponse400 | GetVPNOpenVPNClientExportConfigEndpointResponse401 | GetVPNOpenVPNClientExportConfigEndpointResponse403 | GetVPNOpenVPNClientExportConfigEndpointResponse404 | GetVPNOpenVPNClientExportConfigEndpointResponse405 | GetVPNOpenVPNClientExportConfigEndpointResponse406 | GetVPNOpenVPNClientExportConfigEndpointResponse409 | GetVPNOpenVPNClientExportConfigEndpointResponse415 | GetVPNOpenVPNClientExportConfigEndpointResponse422 | GetVPNOpenVPNClientExportConfigEndpointResponse424 | GetVPNOpenVPNClientExportConfigEndpointResponse500 | GetVPNOpenVPNClientExportConfigEndpointResponse503]
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
    GetVPNOpenVPNClientExportConfigEndpointResponse400
    | GetVPNOpenVPNClientExportConfigEndpointResponse401
    | GetVPNOpenVPNClientExportConfigEndpointResponse403
    | GetVPNOpenVPNClientExportConfigEndpointResponse404
    | GetVPNOpenVPNClientExportConfigEndpointResponse405
    | GetVPNOpenVPNClientExportConfigEndpointResponse406
    | GetVPNOpenVPNClientExportConfigEndpointResponse409
    | GetVPNOpenVPNClientExportConfigEndpointResponse415
    | GetVPNOpenVPNClientExportConfigEndpointResponse422
    | GetVPNOpenVPNClientExportConfigEndpointResponse424
    | GetVPNOpenVPNClientExportConfigEndpointResponse500
    | GetVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    get ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNOpenVPNClientExportConfigEndpointResponse400 | GetVPNOpenVPNClientExportConfigEndpointResponse401 | GetVPNOpenVPNClientExportConfigEndpointResponse403 | GetVPNOpenVPNClientExportConfigEndpointResponse404 | GetVPNOpenVPNClientExportConfigEndpointResponse405 | GetVPNOpenVPNClientExportConfigEndpointResponse406 | GetVPNOpenVPNClientExportConfigEndpointResponse409 | GetVPNOpenVPNClientExportConfigEndpointResponse415 | GetVPNOpenVPNClientExportConfigEndpointResponse422 | GetVPNOpenVPNClientExportConfigEndpointResponse424 | GetVPNOpenVPNClientExportConfigEndpointResponse500 | GetVPNOpenVPNClientExportConfigEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
