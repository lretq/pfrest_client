from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_data_body_item import (
    PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_json_body_item import (
    PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_400 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse400,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_401 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse401,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_403 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse403,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_404 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse404,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_405 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse405,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_406 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse406,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_409 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse409,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_415 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse415,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_422 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse422,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_424 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse424,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_500 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse500,
)
from ...models.put_vpn_open_vpn_client_export_configs_endpoint_response_503 import (
    PutVPNOpenVPNClientExportConfigsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem]
    | list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/vpn/openvpn/client_export/configs",
    }

    if isinstance(body, list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutVPNOpenVPNClientExportConfigsEndpointResponse400
    | PutVPNOpenVPNClientExportConfigsEndpointResponse401
    | PutVPNOpenVPNClientExportConfigsEndpointResponse403
    | PutVPNOpenVPNClientExportConfigsEndpointResponse404
    | PutVPNOpenVPNClientExportConfigsEndpointResponse405
    | PutVPNOpenVPNClientExportConfigsEndpointResponse406
    | PutVPNOpenVPNClientExportConfigsEndpointResponse409
    | PutVPNOpenVPNClientExportConfigsEndpointResponse415
    | PutVPNOpenVPNClientExportConfigsEndpointResponse422
    | PutVPNOpenVPNClientExportConfigsEndpointResponse424
    | PutVPNOpenVPNClientExportConfigsEndpointResponse500
    | PutVPNOpenVPNClientExportConfigsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutVPNOpenVPNClientExportConfigsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutVPNOpenVPNClientExportConfigsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutVPNOpenVPNClientExportConfigsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutVPNOpenVPNClientExportConfigsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutVPNOpenVPNClientExportConfigsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutVPNOpenVPNClientExportConfigsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutVPNOpenVPNClientExportConfigsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutVPNOpenVPNClientExportConfigsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutVPNOpenVPNClientExportConfigsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutVPNOpenVPNClientExportConfigsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutVPNOpenVPNClientExportConfigsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutVPNOpenVPNClientExportConfigsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutVPNOpenVPNClientExportConfigsEndpointResponse400
    | PutVPNOpenVPNClientExportConfigsEndpointResponse401
    | PutVPNOpenVPNClientExportConfigsEndpointResponse403
    | PutVPNOpenVPNClientExportConfigsEndpointResponse404
    | PutVPNOpenVPNClientExportConfigsEndpointResponse405
    | PutVPNOpenVPNClientExportConfigsEndpointResponse406
    | PutVPNOpenVPNClientExportConfigsEndpointResponse409
    | PutVPNOpenVPNClientExportConfigsEndpointResponse415
    | PutVPNOpenVPNClientExportConfigsEndpointResponse422
    | PutVPNOpenVPNClientExportConfigsEndpointResponse424
    | PutVPNOpenVPNClientExportConfigsEndpointResponse500
    | PutVPNOpenVPNClientExportConfigsEndpointResponse503
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
    body: list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem]
    | list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutVPNOpenVPNClientExportConfigsEndpointResponse400
    | PutVPNOpenVPNClientExportConfigsEndpointResponse401
    | PutVPNOpenVPNClientExportConfigsEndpointResponse403
    | PutVPNOpenVPNClientExportConfigsEndpointResponse404
    | PutVPNOpenVPNClientExportConfigsEndpointResponse405
    | PutVPNOpenVPNClientExportConfigsEndpointResponse406
    | PutVPNOpenVPNClientExportConfigsEndpointResponse409
    | PutVPNOpenVPNClientExportConfigsEndpointResponse415
    | PutVPNOpenVPNClientExportConfigsEndpointResponse422
    | PutVPNOpenVPNClientExportConfigsEndpointResponse424
    | PutVPNOpenVPNClientExportConfigsEndpointResponse500
    | PutVPNOpenVPNClientExportConfigsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing OpenVPN Client Export
    Configs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-configs-put ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNOpenVPNClientExportConfigsEndpointResponse400 | PutVPNOpenVPNClientExportConfigsEndpointResponse401 | PutVPNOpenVPNClientExportConfigsEndpointResponse403 | PutVPNOpenVPNClientExportConfigsEndpointResponse404 | PutVPNOpenVPNClientExportConfigsEndpointResponse405 | PutVPNOpenVPNClientExportConfigsEndpointResponse406 | PutVPNOpenVPNClientExportConfigsEndpointResponse409 | PutVPNOpenVPNClientExportConfigsEndpointResponse415 | PutVPNOpenVPNClientExportConfigsEndpointResponse422 | PutVPNOpenVPNClientExportConfigsEndpointResponse424 | PutVPNOpenVPNClientExportConfigsEndpointResponse500 | PutVPNOpenVPNClientExportConfigsEndpointResponse503]
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
    body: list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem]
    | list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutVPNOpenVPNClientExportConfigsEndpointResponse400
    | PutVPNOpenVPNClientExportConfigsEndpointResponse401
    | PutVPNOpenVPNClientExportConfigsEndpointResponse403
    | PutVPNOpenVPNClientExportConfigsEndpointResponse404
    | PutVPNOpenVPNClientExportConfigsEndpointResponse405
    | PutVPNOpenVPNClientExportConfigsEndpointResponse406
    | PutVPNOpenVPNClientExportConfigsEndpointResponse409
    | PutVPNOpenVPNClientExportConfigsEndpointResponse415
    | PutVPNOpenVPNClientExportConfigsEndpointResponse422
    | PutVPNOpenVPNClientExportConfigsEndpointResponse424
    | PutVPNOpenVPNClientExportConfigsEndpointResponse500
    | PutVPNOpenVPNClientExportConfigsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing OpenVPN Client Export
    Configs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-configs-put ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNOpenVPNClientExportConfigsEndpointResponse400 | PutVPNOpenVPNClientExportConfigsEndpointResponse401 | PutVPNOpenVPNClientExportConfigsEndpointResponse403 | PutVPNOpenVPNClientExportConfigsEndpointResponse404 | PutVPNOpenVPNClientExportConfigsEndpointResponse405 | PutVPNOpenVPNClientExportConfigsEndpointResponse406 | PutVPNOpenVPNClientExportConfigsEndpointResponse409 | PutVPNOpenVPNClientExportConfigsEndpointResponse415 | PutVPNOpenVPNClientExportConfigsEndpointResponse422 | PutVPNOpenVPNClientExportConfigsEndpointResponse424 | PutVPNOpenVPNClientExportConfigsEndpointResponse500 | PutVPNOpenVPNClientExportConfigsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem]
    | list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutVPNOpenVPNClientExportConfigsEndpointResponse400
    | PutVPNOpenVPNClientExportConfigsEndpointResponse401
    | PutVPNOpenVPNClientExportConfigsEndpointResponse403
    | PutVPNOpenVPNClientExportConfigsEndpointResponse404
    | PutVPNOpenVPNClientExportConfigsEndpointResponse405
    | PutVPNOpenVPNClientExportConfigsEndpointResponse406
    | PutVPNOpenVPNClientExportConfigsEndpointResponse409
    | PutVPNOpenVPNClientExportConfigsEndpointResponse415
    | PutVPNOpenVPNClientExportConfigsEndpointResponse422
    | PutVPNOpenVPNClientExportConfigsEndpointResponse424
    | PutVPNOpenVPNClientExportConfigsEndpointResponse500
    | PutVPNOpenVPNClientExportConfigsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing OpenVPN Client Export
    Configs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-configs-put ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNOpenVPNClientExportConfigsEndpointResponse400 | PutVPNOpenVPNClientExportConfigsEndpointResponse401 | PutVPNOpenVPNClientExportConfigsEndpointResponse403 | PutVPNOpenVPNClientExportConfigsEndpointResponse404 | PutVPNOpenVPNClientExportConfigsEndpointResponse405 | PutVPNOpenVPNClientExportConfigsEndpointResponse406 | PutVPNOpenVPNClientExportConfigsEndpointResponse409 | PutVPNOpenVPNClientExportConfigsEndpointResponse415 | PutVPNOpenVPNClientExportConfigsEndpointResponse422 | PutVPNOpenVPNClientExportConfigsEndpointResponse424 | PutVPNOpenVPNClientExportConfigsEndpointResponse500 | PutVPNOpenVPNClientExportConfigsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem]
    | list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutVPNOpenVPNClientExportConfigsEndpointResponse400
    | PutVPNOpenVPNClientExportConfigsEndpointResponse401
    | PutVPNOpenVPNClientExportConfigsEndpointResponse403
    | PutVPNOpenVPNClientExportConfigsEndpointResponse404
    | PutVPNOpenVPNClientExportConfigsEndpointResponse405
    | PutVPNOpenVPNClientExportConfigsEndpointResponse406
    | PutVPNOpenVPNClientExportConfigsEndpointResponse409
    | PutVPNOpenVPNClientExportConfigsEndpointResponse415
    | PutVPNOpenVPNClientExportConfigsEndpointResponse422
    | PutVPNOpenVPNClientExportConfigsEndpointResponse424
    | PutVPNOpenVPNClientExportConfigsEndpointResponse500
    | PutVPNOpenVPNClientExportConfigsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing OpenVPN Client Export
    Configs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    OpenVPNClientExportConfig<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-configs-put ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNOpenVPNClientExportConfigsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNOpenVPNClientExportConfigsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNOpenVPNClientExportConfigsEndpointResponse400 | PutVPNOpenVPNClientExportConfigsEndpointResponse401 | PutVPNOpenVPNClientExportConfigsEndpointResponse403 | PutVPNOpenVPNClientExportConfigsEndpointResponse404 | PutVPNOpenVPNClientExportConfigsEndpointResponse405 | PutVPNOpenVPNClientExportConfigsEndpointResponse406 | PutVPNOpenVPNClientExportConfigsEndpointResponse409 | PutVPNOpenVPNClientExportConfigsEndpointResponse415 | PutVPNOpenVPNClientExportConfigsEndpointResponse422 | PutVPNOpenVPNClientExportConfigsEndpointResponse424 | PutVPNOpenVPNClientExportConfigsEndpointResponse500 | PutVPNOpenVPNClientExportConfigsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
