from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_data_body import (
    PatchVPNOpenVPNClientExportConfigEndpointDataBody,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_json_body import (
    PatchVPNOpenVPNClientExportConfigEndpointJsonBody,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_400 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse400,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_401 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse401,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_403 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse403,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_404 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse404,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_405 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse405,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_406 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse406,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_409 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse409,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_415 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse415,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_422 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse422,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_424 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse424,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_500 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse500,
)
from ...models.patch_vpn_open_vpn_client_export_config_endpoint_response_503 import (
    PatchVPNOpenVPNClientExportConfigEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNOpenVPNClientExportConfigEndpointJsonBody
    | PatchVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/openvpn/client_export/config",
    }

    if isinstance(body, PatchVPNOpenVPNClientExportConfigEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNOpenVPNClientExportConfigEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNOpenVPNClientExportConfigEndpointResponse400
    | PatchVPNOpenVPNClientExportConfigEndpointResponse401
    | PatchVPNOpenVPNClientExportConfigEndpointResponse403
    | PatchVPNOpenVPNClientExportConfigEndpointResponse404
    | PatchVPNOpenVPNClientExportConfigEndpointResponse405
    | PatchVPNOpenVPNClientExportConfigEndpointResponse406
    | PatchVPNOpenVPNClientExportConfigEndpointResponse409
    | PatchVPNOpenVPNClientExportConfigEndpointResponse415
    | PatchVPNOpenVPNClientExportConfigEndpointResponse422
    | PatchVPNOpenVPNClientExportConfigEndpointResponse424
    | PatchVPNOpenVPNClientExportConfigEndpointResponse500
    | PatchVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNOpenVPNClientExportConfigEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNOpenVPNClientExportConfigEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNOpenVPNClientExportConfigEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNOpenVPNClientExportConfigEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNOpenVPNClientExportConfigEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNOpenVPNClientExportConfigEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNOpenVPNClientExportConfigEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNOpenVPNClientExportConfigEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNOpenVPNClientExportConfigEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNOpenVPNClientExportConfigEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNOpenVPNClientExportConfigEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNOpenVPNClientExportConfigEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNOpenVPNClientExportConfigEndpointResponse400
    | PatchVPNOpenVPNClientExportConfigEndpointResponse401
    | PatchVPNOpenVPNClientExportConfigEndpointResponse403
    | PatchVPNOpenVPNClientExportConfigEndpointResponse404
    | PatchVPNOpenVPNClientExportConfigEndpointResponse405
    | PatchVPNOpenVPNClientExportConfigEndpointResponse406
    | PatchVPNOpenVPNClientExportConfigEndpointResponse409
    | PatchVPNOpenVPNClientExportConfigEndpointResponse415
    | PatchVPNOpenVPNClientExportConfigEndpointResponse422
    | PatchVPNOpenVPNClientExportConfigEndpointResponse424
    | PatchVPNOpenVPNClientExportConfigEndpointResponse500
    | PatchVPNOpenVPNClientExportConfigEndpointResponse503
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
    body: PatchVPNOpenVPNClientExportConfigEndpointJsonBody
    | PatchVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchVPNOpenVPNClientExportConfigEndpointResponse400
    | PatchVPNOpenVPNClientExportConfigEndpointResponse401
    | PatchVPNOpenVPNClientExportConfigEndpointResponse403
    | PatchVPNOpenVPNClientExportConfigEndpointResponse404
    | PatchVPNOpenVPNClientExportConfigEndpointResponse405
    | PatchVPNOpenVPNClientExportConfigEndpointResponse406
    | PatchVPNOpenVPNClientExportConfigEndpointResponse409
    | PatchVPNOpenVPNClientExportConfigEndpointResponse415
    | PatchVPNOpenVPNClientExportConfigEndpointResponse422
    | PatchVPNOpenVPNClientExportConfigEndpointResponse424
    | PatchVPNOpenVPNClientExportConfigEndpointResponse500
    | PatchVPNOpenVPNClientExportConfigEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing OpenVPN Client Export
    Config.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-patch ]<br>**Required packages**:
    [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNOpenVPNClientExportConfigEndpointResponse400 | PatchVPNOpenVPNClientExportConfigEndpointResponse401 | PatchVPNOpenVPNClientExportConfigEndpointResponse403 | PatchVPNOpenVPNClientExportConfigEndpointResponse404 | PatchVPNOpenVPNClientExportConfigEndpointResponse405 | PatchVPNOpenVPNClientExportConfigEndpointResponse406 | PatchVPNOpenVPNClientExportConfigEndpointResponse409 | PatchVPNOpenVPNClientExportConfigEndpointResponse415 | PatchVPNOpenVPNClientExportConfigEndpointResponse422 | PatchVPNOpenVPNClientExportConfigEndpointResponse424 | PatchVPNOpenVPNClientExportConfigEndpointResponse500 | PatchVPNOpenVPNClientExportConfigEndpointResponse503]
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
    body: PatchVPNOpenVPNClientExportConfigEndpointJsonBody
    | PatchVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchVPNOpenVPNClientExportConfigEndpointResponse400
    | PatchVPNOpenVPNClientExportConfigEndpointResponse401
    | PatchVPNOpenVPNClientExportConfigEndpointResponse403
    | PatchVPNOpenVPNClientExportConfigEndpointResponse404
    | PatchVPNOpenVPNClientExportConfigEndpointResponse405
    | PatchVPNOpenVPNClientExportConfigEndpointResponse406
    | PatchVPNOpenVPNClientExportConfigEndpointResponse409
    | PatchVPNOpenVPNClientExportConfigEndpointResponse415
    | PatchVPNOpenVPNClientExportConfigEndpointResponse422
    | PatchVPNOpenVPNClientExportConfigEndpointResponse424
    | PatchVPNOpenVPNClientExportConfigEndpointResponse500
    | PatchVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing OpenVPN Client Export
    Config.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-patch ]<br>**Required packages**:
    [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNOpenVPNClientExportConfigEndpointResponse400 | PatchVPNOpenVPNClientExportConfigEndpointResponse401 | PatchVPNOpenVPNClientExportConfigEndpointResponse403 | PatchVPNOpenVPNClientExportConfigEndpointResponse404 | PatchVPNOpenVPNClientExportConfigEndpointResponse405 | PatchVPNOpenVPNClientExportConfigEndpointResponse406 | PatchVPNOpenVPNClientExportConfigEndpointResponse409 | PatchVPNOpenVPNClientExportConfigEndpointResponse415 | PatchVPNOpenVPNClientExportConfigEndpointResponse422 | PatchVPNOpenVPNClientExportConfigEndpointResponse424 | PatchVPNOpenVPNClientExportConfigEndpointResponse500 | PatchVPNOpenVPNClientExportConfigEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNOpenVPNClientExportConfigEndpointJsonBody
    | PatchVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchVPNOpenVPNClientExportConfigEndpointResponse400
    | PatchVPNOpenVPNClientExportConfigEndpointResponse401
    | PatchVPNOpenVPNClientExportConfigEndpointResponse403
    | PatchVPNOpenVPNClientExportConfigEndpointResponse404
    | PatchVPNOpenVPNClientExportConfigEndpointResponse405
    | PatchVPNOpenVPNClientExportConfigEndpointResponse406
    | PatchVPNOpenVPNClientExportConfigEndpointResponse409
    | PatchVPNOpenVPNClientExportConfigEndpointResponse415
    | PatchVPNOpenVPNClientExportConfigEndpointResponse422
    | PatchVPNOpenVPNClientExportConfigEndpointResponse424
    | PatchVPNOpenVPNClientExportConfigEndpointResponse500
    | PatchVPNOpenVPNClientExportConfigEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing OpenVPN Client Export
    Config.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-patch ]<br>**Required packages**:
    [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNOpenVPNClientExportConfigEndpointResponse400 | PatchVPNOpenVPNClientExportConfigEndpointResponse401 | PatchVPNOpenVPNClientExportConfigEndpointResponse403 | PatchVPNOpenVPNClientExportConfigEndpointResponse404 | PatchVPNOpenVPNClientExportConfigEndpointResponse405 | PatchVPNOpenVPNClientExportConfigEndpointResponse406 | PatchVPNOpenVPNClientExportConfigEndpointResponse409 | PatchVPNOpenVPNClientExportConfigEndpointResponse415 | PatchVPNOpenVPNClientExportConfigEndpointResponse422 | PatchVPNOpenVPNClientExportConfigEndpointResponse424 | PatchVPNOpenVPNClientExportConfigEndpointResponse500 | PatchVPNOpenVPNClientExportConfigEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNOpenVPNClientExportConfigEndpointJsonBody
    | PatchVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchVPNOpenVPNClientExportConfigEndpointResponse400
    | PatchVPNOpenVPNClientExportConfigEndpointResponse401
    | PatchVPNOpenVPNClientExportConfigEndpointResponse403
    | PatchVPNOpenVPNClientExportConfigEndpointResponse404
    | PatchVPNOpenVPNClientExportConfigEndpointResponse405
    | PatchVPNOpenVPNClientExportConfigEndpointResponse406
    | PatchVPNOpenVPNClientExportConfigEndpointResponse409
    | PatchVPNOpenVPNClientExportConfigEndpointResponse415
    | PatchVPNOpenVPNClientExportConfigEndpointResponse422
    | PatchVPNOpenVPNClientExportConfigEndpointResponse424
    | PatchVPNOpenVPNClientExportConfigEndpointResponse500
    | PatchVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing OpenVPN Client Export
    Config.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-patch ]<br>**Required packages**:
    [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNOpenVPNClientExportConfigEndpointResponse400 | PatchVPNOpenVPNClientExportConfigEndpointResponse401 | PatchVPNOpenVPNClientExportConfigEndpointResponse403 | PatchVPNOpenVPNClientExportConfigEndpointResponse404 | PatchVPNOpenVPNClientExportConfigEndpointResponse405 | PatchVPNOpenVPNClientExportConfigEndpointResponse406 | PatchVPNOpenVPNClientExportConfigEndpointResponse409 | PatchVPNOpenVPNClientExportConfigEndpointResponse415 | PatchVPNOpenVPNClientExportConfigEndpointResponse422 | PatchVPNOpenVPNClientExportConfigEndpointResponse424 | PatchVPNOpenVPNClientExportConfigEndpointResponse500 | PatchVPNOpenVPNClientExportConfigEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
