from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_virtual_ip_apply_endpoint_response_400 import GetFirewallVirtualIPApplyEndpointResponse400
from ...models.get_firewall_virtual_ip_apply_endpoint_response_401 import GetFirewallVirtualIPApplyEndpointResponse401
from ...models.get_firewall_virtual_ip_apply_endpoint_response_403 import GetFirewallVirtualIPApplyEndpointResponse403
from ...models.get_firewall_virtual_ip_apply_endpoint_response_404 import GetFirewallVirtualIPApplyEndpointResponse404
from ...models.get_firewall_virtual_ip_apply_endpoint_response_405 import GetFirewallVirtualIPApplyEndpointResponse405
from ...models.get_firewall_virtual_ip_apply_endpoint_response_406 import GetFirewallVirtualIPApplyEndpointResponse406
from ...models.get_firewall_virtual_ip_apply_endpoint_response_409 import GetFirewallVirtualIPApplyEndpointResponse409
from ...models.get_firewall_virtual_ip_apply_endpoint_response_415 import GetFirewallVirtualIPApplyEndpointResponse415
from ...models.get_firewall_virtual_ip_apply_endpoint_response_422 import GetFirewallVirtualIPApplyEndpointResponse422
from ...models.get_firewall_virtual_ip_apply_endpoint_response_424 import GetFirewallVirtualIPApplyEndpointResponse424
from ...models.get_firewall_virtual_ip_apply_endpoint_response_500 import GetFirewallVirtualIPApplyEndpointResponse500
from ...models.get_firewall_virtual_ip_apply_endpoint_response_503 import GetFirewallVirtualIPApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/firewall/virtual_ip/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallVirtualIPApplyEndpointResponse400
    | GetFirewallVirtualIPApplyEndpointResponse401
    | GetFirewallVirtualIPApplyEndpointResponse403
    | GetFirewallVirtualIPApplyEndpointResponse404
    | GetFirewallVirtualIPApplyEndpointResponse405
    | GetFirewallVirtualIPApplyEndpointResponse406
    | GetFirewallVirtualIPApplyEndpointResponse409
    | GetFirewallVirtualIPApplyEndpointResponse415
    | GetFirewallVirtualIPApplyEndpointResponse422
    | GetFirewallVirtualIPApplyEndpointResponse424
    | GetFirewallVirtualIPApplyEndpointResponse500
    | GetFirewallVirtualIPApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallVirtualIPApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallVirtualIPApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallVirtualIPApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallVirtualIPApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallVirtualIPApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallVirtualIPApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallVirtualIPApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallVirtualIPApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallVirtualIPApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallVirtualIPApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallVirtualIPApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallVirtualIPApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallVirtualIPApplyEndpointResponse400
    | GetFirewallVirtualIPApplyEndpointResponse401
    | GetFirewallVirtualIPApplyEndpointResponse403
    | GetFirewallVirtualIPApplyEndpointResponse404
    | GetFirewallVirtualIPApplyEndpointResponse405
    | GetFirewallVirtualIPApplyEndpointResponse406
    | GetFirewallVirtualIPApplyEndpointResponse409
    | GetFirewallVirtualIPApplyEndpointResponse415
    | GetFirewallVirtualIPApplyEndpointResponse422
    | GetFirewallVirtualIPApplyEndpointResponse424
    | GetFirewallVirtualIPApplyEndpointResponse500
    | GetFirewallVirtualIPApplyEndpointResponse503
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
    GetFirewallVirtualIPApplyEndpointResponse400
    | GetFirewallVirtualIPApplyEndpointResponse401
    | GetFirewallVirtualIPApplyEndpointResponse403
    | GetFirewallVirtualIPApplyEndpointResponse404
    | GetFirewallVirtualIPApplyEndpointResponse405
    | GetFirewallVirtualIPApplyEndpointResponse406
    | GetFirewallVirtualIPApplyEndpointResponse409
    | GetFirewallVirtualIPApplyEndpointResponse415
    | GetFirewallVirtualIPApplyEndpointResponse422
    | GetFirewallVirtualIPApplyEndpointResponse424
    | GetFirewallVirtualIPApplyEndpointResponse500
    | GetFirewallVirtualIPApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending virtual IP status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallVirtualIPApplyEndpointResponse400 | GetFirewallVirtualIPApplyEndpointResponse401 | GetFirewallVirtualIPApplyEndpointResponse403 | GetFirewallVirtualIPApplyEndpointResponse404 | GetFirewallVirtualIPApplyEndpointResponse405 | GetFirewallVirtualIPApplyEndpointResponse406 | GetFirewallVirtualIPApplyEndpointResponse409 | GetFirewallVirtualIPApplyEndpointResponse415 | GetFirewallVirtualIPApplyEndpointResponse422 | GetFirewallVirtualIPApplyEndpointResponse424 | GetFirewallVirtualIPApplyEndpointResponse500 | GetFirewallVirtualIPApplyEndpointResponse503]
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
    GetFirewallVirtualIPApplyEndpointResponse400
    | GetFirewallVirtualIPApplyEndpointResponse401
    | GetFirewallVirtualIPApplyEndpointResponse403
    | GetFirewallVirtualIPApplyEndpointResponse404
    | GetFirewallVirtualIPApplyEndpointResponse405
    | GetFirewallVirtualIPApplyEndpointResponse406
    | GetFirewallVirtualIPApplyEndpointResponse409
    | GetFirewallVirtualIPApplyEndpointResponse415
    | GetFirewallVirtualIPApplyEndpointResponse422
    | GetFirewallVirtualIPApplyEndpointResponse424
    | GetFirewallVirtualIPApplyEndpointResponse500
    | GetFirewallVirtualIPApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending virtual IP status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallVirtualIPApplyEndpointResponse400 | GetFirewallVirtualIPApplyEndpointResponse401 | GetFirewallVirtualIPApplyEndpointResponse403 | GetFirewallVirtualIPApplyEndpointResponse404 | GetFirewallVirtualIPApplyEndpointResponse405 | GetFirewallVirtualIPApplyEndpointResponse406 | GetFirewallVirtualIPApplyEndpointResponse409 | GetFirewallVirtualIPApplyEndpointResponse415 | GetFirewallVirtualIPApplyEndpointResponse422 | GetFirewallVirtualIPApplyEndpointResponse424 | GetFirewallVirtualIPApplyEndpointResponse500 | GetFirewallVirtualIPApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetFirewallVirtualIPApplyEndpointResponse400
    | GetFirewallVirtualIPApplyEndpointResponse401
    | GetFirewallVirtualIPApplyEndpointResponse403
    | GetFirewallVirtualIPApplyEndpointResponse404
    | GetFirewallVirtualIPApplyEndpointResponse405
    | GetFirewallVirtualIPApplyEndpointResponse406
    | GetFirewallVirtualIPApplyEndpointResponse409
    | GetFirewallVirtualIPApplyEndpointResponse415
    | GetFirewallVirtualIPApplyEndpointResponse422
    | GetFirewallVirtualIPApplyEndpointResponse424
    | GetFirewallVirtualIPApplyEndpointResponse500
    | GetFirewallVirtualIPApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending virtual IP status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallVirtualIPApplyEndpointResponse400 | GetFirewallVirtualIPApplyEndpointResponse401 | GetFirewallVirtualIPApplyEndpointResponse403 | GetFirewallVirtualIPApplyEndpointResponse404 | GetFirewallVirtualIPApplyEndpointResponse405 | GetFirewallVirtualIPApplyEndpointResponse406 | GetFirewallVirtualIPApplyEndpointResponse409 | GetFirewallVirtualIPApplyEndpointResponse415 | GetFirewallVirtualIPApplyEndpointResponse422 | GetFirewallVirtualIPApplyEndpointResponse424 | GetFirewallVirtualIPApplyEndpointResponse500 | GetFirewallVirtualIPApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetFirewallVirtualIPApplyEndpointResponse400
    | GetFirewallVirtualIPApplyEndpointResponse401
    | GetFirewallVirtualIPApplyEndpointResponse403
    | GetFirewallVirtualIPApplyEndpointResponse404
    | GetFirewallVirtualIPApplyEndpointResponse405
    | GetFirewallVirtualIPApplyEndpointResponse406
    | GetFirewallVirtualIPApplyEndpointResponse409
    | GetFirewallVirtualIPApplyEndpointResponse415
    | GetFirewallVirtualIPApplyEndpointResponse422
    | GetFirewallVirtualIPApplyEndpointResponse424
    | GetFirewallVirtualIPApplyEndpointResponse500
    | GetFirewallVirtualIPApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending virtual IP status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallVirtualIPApplyEndpointResponse400 | GetFirewallVirtualIPApplyEndpointResponse401 | GetFirewallVirtualIPApplyEndpointResponse403 | GetFirewallVirtualIPApplyEndpointResponse404 | GetFirewallVirtualIPApplyEndpointResponse405 | GetFirewallVirtualIPApplyEndpointResponse406 | GetFirewallVirtualIPApplyEndpointResponse409 | GetFirewallVirtualIPApplyEndpointResponse415 | GetFirewallVirtualIPApplyEndpointResponse422 | GetFirewallVirtualIPApplyEndpointResponse424 | GetFirewallVirtualIPApplyEndpointResponse500 | GetFirewallVirtualIPApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
