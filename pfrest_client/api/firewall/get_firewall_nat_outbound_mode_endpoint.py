from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_nat_outbound_mode_endpoint_response_400 import GetFirewallNATOutboundModeEndpointResponse400
from ...models.get_firewall_nat_outbound_mode_endpoint_response_401 import GetFirewallNATOutboundModeEndpointResponse401
from ...models.get_firewall_nat_outbound_mode_endpoint_response_403 import GetFirewallNATOutboundModeEndpointResponse403
from ...models.get_firewall_nat_outbound_mode_endpoint_response_404 import GetFirewallNATOutboundModeEndpointResponse404
from ...models.get_firewall_nat_outbound_mode_endpoint_response_405 import GetFirewallNATOutboundModeEndpointResponse405
from ...models.get_firewall_nat_outbound_mode_endpoint_response_406 import GetFirewallNATOutboundModeEndpointResponse406
from ...models.get_firewall_nat_outbound_mode_endpoint_response_409 import GetFirewallNATOutboundModeEndpointResponse409
from ...models.get_firewall_nat_outbound_mode_endpoint_response_415 import GetFirewallNATOutboundModeEndpointResponse415
from ...models.get_firewall_nat_outbound_mode_endpoint_response_422 import GetFirewallNATOutboundModeEndpointResponse422
from ...models.get_firewall_nat_outbound_mode_endpoint_response_424 import GetFirewallNATOutboundModeEndpointResponse424
from ...models.get_firewall_nat_outbound_mode_endpoint_response_500 import GetFirewallNATOutboundModeEndpointResponse500
from ...models.get_firewall_nat_outbound_mode_endpoint_response_503 import GetFirewallNATOutboundModeEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/firewall/nat/outbound/mode",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallNATOutboundModeEndpointResponse400
    | GetFirewallNATOutboundModeEndpointResponse401
    | GetFirewallNATOutboundModeEndpointResponse403
    | GetFirewallNATOutboundModeEndpointResponse404
    | GetFirewallNATOutboundModeEndpointResponse405
    | GetFirewallNATOutboundModeEndpointResponse406
    | GetFirewallNATOutboundModeEndpointResponse409
    | GetFirewallNATOutboundModeEndpointResponse415
    | GetFirewallNATOutboundModeEndpointResponse422
    | GetFirewallNATOutboundModeEndpointResponse424
    | GetFirewallNATOutboundModeEndpointResponse500
    | GetFirewallNATOutboundModeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallNATOutboundModeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallNATOutboundModeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallNATOutboundModeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallNATOutboundModeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallNATOutboundModeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallNATOutboundModeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallNATOutboundModeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallNATOutboundModeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallNATOutboundModeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallNATOutboundModeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallNATOutboundModeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallNATOutboundModeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallNATOutboundModeEndpointResponse400
    | GetFirewallNATOutboundModeEndpointResponse401
    | GetFirewallNATOutboundModeEndpointResponse403
    | GetFirewallNATOutboundModeEndpointResponse404
    | GetFirewallNATOutboundModeEndpointResponse405
    | GetFirewallNATOutboundModeEndpointResponse406
    | GetFirewallNATOutboundModeEndpointResponse409
    | GetFirewallNATOutboundModeEndpointResponse415
    | GetFirewallNATOutboundModeEndpointResponse422
    | GetFirewallNATOutboundModeEndpointResponse424
    | GetFirewallNATOutboundModeEndpointResponse500
    | GetFirewallNATOutboundModeEndpointResponse503
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
    GetFirewallNATOutboundModeEndpointResponse400
    | GetFirewallNATOutboundModeEndpointResponse401
    | GetFirewallNATOutboundModeEndpointResponse403
    | GetFirewallNATOutboundModeEndpointResponse404
    | GetFirewallNATOutboundModeEndpointResponse405
    | GetFirewallNATOutboundModeEndpointResponse406
    | GetFirewallNATOutboundModeEndpointResponse409
    | GetFirewallNATOutboundModeEndpointResponse415
    | GetFirewallNATOutboundModeEndpointResponse422
    | GetFirewallNATOutboundModeEndpointResponse424
    | GetFirewallNATOutboundModeEndpointResponse500
    | GetFirewallNATOutboundModeEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Outbound NAT Mode.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMode<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mode-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallNATOutboundModeEndpointResponse400 | GetFirewallNATOutboundModeEndpointResponse401 | GetFirewallNATOutboundModeEndpointResponse403 | GetFirewallNATOutboundModeEndpointResponse404 | GetFirewallNATOutboundModeEndpointResponse405 | GetFirewallNATOutboundModeEndpointResponse406 | GetFirewallNATOutboundModeEndpointResponse409 | GetFirewallNATOutboundModeEndpointResponse415 | GetFirewallNATOutboundModeEndpointResponse422 | GetFirewallNATOutboundModeEndpointResponse424 | GetFirewallNATOutboundModeEndpointResponse500 | GetFirewallNATOutboundModeEndpointResponse503]
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
    GetFirewallNATOutboundModeEndpointResponse400
    | GetFirewallNATOutboundModeEndpointResponse401
    | GetFirewallNATOutboundModeEndpointResponse403
    | GetFirewallNATOutboundModeEndpointResponse404
    | GetFirewallNATOutboundModeEndpointResponse405
    | GetFirewallNATOutboundModeEndpointResponse406
    | GetFirewallNATOutboundModeEndpointResponse409
    | GetFirewallNATOutboundModeEndpointResponse415
    | GetFirewallNATOutboundModeEndpointResponse422
    | GetFirewallNATOutboundModeEndpointResponse424
    | GetFirewallNATOutboundModeEndpointResponse500
    | GetFirewallNATOutboundModeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Outbound NAT Mode.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMode<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mode-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallNATOutboundModeEndpointResponse400 | GetFirewallNATOutboundModeEndpointResponse401 | GetFirewallNATOutboundModeEndpointResponse403 | GetFirewallNATOutboundModeEndpointResponse404 | GetFirewallNATOutboundModeEndpointResponse405 | GetFirewallNATOutboundModeEndpointResponse406 | GetFirewallNATOutboundModeEndpointResponse409 | GetFirewallNATOutboundModeEndpointResponse415 | GetFirewallNATOutboundModeEndpointResponse422 | GetFirewallNATOutboundModeEndpointResponse424 | GetFirewallNATOutboundModeEndpointResponse500 | GetFirewallNATOutboundModeEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetFirewallNATOutboundModeEndpointResponse400
    | GetFirewallNATOutboundModeEndpointResponse401
    | GetFirewallNATOutboundModeEndpointResponse403
    | GetFirewallNATOutboundModeEndpointResponse404
    | GetFirewallNATOutboundModeEndpointResponse405
    | GetFirewallNATOutboundModeEndpointResponse406
    | GetFirewallNATOutboundModeEndpointResponse409
    | GetFirewallNATOutboundModeEndpointResponse415
    | GetFirewallNATOutboundModeEndpointResponse422
    | GetFirewallNATOutboundModeEndpointResponse424
    | GetFirewallNATOutboundModeEndpointResponse500
    | GetFirewallNATOutboundModeEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Outbound NAT Mode.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMode<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mode-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallNATOutboundModeEndpointResponse400 | GetFirewallNATOutboundModeEndpointResponse401 | GetFirewallNATOutboundModeEndpointResponse403 | GetFirewallNATOutboundModeEndpointResponse404 | GetFirewallNATOutboundModeEndpointResponse405 | GetFirewallNATOutboundModeEndpointResponse406 | GetFirewallNATOutboundModeEndpointResponse409 | GetFirewallNATOutboundModeEndpointResponse415 | GetFirewallNATOutboundModeEndpointResponse422 | GetFirewallNATOutboundModeEndpointResponse424 | GetFirewallNATOutboundModeEndpointResponse500 | GetFirewallNATOutboundModeEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetFirewallNATOutboundModeEndpointResponse400
    | GetFirewallNATOutboundModeEndpointResponse401
    | GetFirewallNATOutboundModeEndpointResponse403
    | GetFirewallNATOutboundModeEndpointResponse404
    | GetFirewallNATOutboundModeEndpointResponse405
    | GetFirewallNATOutboundModeEndpointResponse406
    | GetFirewallNATOutboundModeEndpointResponse409
    | GetFirewallNATOutboundModeEndpointResponse415
    | GetFirewallNATOutboundModeEndpointResponse422
    | GetFirewallNATOutboundModeEndpointResponse424
    | GetFirewallNATOutboundModeEndpointResponse500
    | GetFirewallNATOutboundModeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Outbound NAT Mode.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMode<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mode-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallNATOutboundModeEndpointResponse400 | GetFirewallNATOutboundModeEndpointResponse401 | GetFirewallNATOutboundModeEndpointResponse403 | GetFirewallNATOutboundModeEndpointResponse404 | GetFirewallNATOutboundModeEndpointResponse405 | GetFirewallNATOutboundModeEndpointResponse406 | GetFirewallNATOutboundModeEndpointResponse409 | GetFirewallNATOutboundModeEndpointResponse415 | GetFirewallNATOutboundModeEndpointResponse422 | GetFirewallNATOutboundModeEndpointResponse424 | GetFirewallNATOutboundModeEndpointResponse500 | GetFirewallNATOutboundModeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
