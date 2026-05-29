from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_virtual_ip_endpoint_data_body import PatchFirewallVirtualIPEndpointDataBody
from ...models.patch_firewall_virtual_ip_endpoint_json_body import PatchFirewallVirtualIPEndpointJsonBody
from ...models.patch_firewall_virtual_ip_endpoint_response_400 import PatchFirewallVirtualIPEndpointResponse400
from ...models.patch_firewall_virtual_ip_endpoint_response_401 import PatchFirewallVirtualIPEndpointResponse401
from ...models.patch_firewall_virtual_ip_endpoint_response_403 import PatchFirewallVirtualIPEndpointResponse403
from ...models.patch_firewall_virtual_ip_endpoint_response_404 import PatchFirewallVirtualIPEndpointResponse404
from ...models.patch_firewall_virtual_ip_endpoint_response_405 import PatchFirewallVirtualIPEndpointResponse405
from ...models.patch_firewall_virtual_ip_endpoint_response_406 import PatchFirewallVirtualIPEndpointResponse406
from ...models.patch_firewall_virtual_ip_endpoint_response_409 import PatchFirewallVirtualIPEndpointResponse409
from ...models.patch_firewall_virtual_ip_endpoint_response_415 import PatchFirewallVirtualIPEndpointResponse415
from ...models.patch_firewall_virtual_ip_endpoint_response_422 import PatchFirewallVirtualIPEndpointResponse422
from ...models.patch_firewall_virtual_ip_endpoint_response_424 import PatchFirewallVirtualIPEndpointResponse424
from ...models.patch_firewall_virtual_ip_endpoint_response_500 import PatchFirewallVirtualIPEndpointResponse500
from ...models.patch_firewall_virtual_ip_endpoint_response_503 import PatchFirewallVirtualIPEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallVirtualIPEndpointJsonBody | PatchFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/virtual_ip",
    }

    if isinstance(body, PatchFirewallVirtualIPEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallVirtualIPEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallVirtualIPEndpointResponse400
    | PatchFirewallVirtualIPEndpointResponse401
    | PatchFirewallVirtualIPEndpointResponse403
    | PatchFirewallVirtualIPEndpointResponse404
    | PatchFirewallVirtualIPEndpointResponse405
    | PatchFirewallVirtualIPEndpointResponse406
    | PatchFirewallVirtualIPEndpointResponse409
    | PatchFirewallVirtualIPEndpointResponse415
    | PatchFirewallVirtualIPEndpointResponse422
    | PatchFirewallVirtualIPEndpointResponse424
    | PatchFirewallVirtualIPEndpointResponse500
    | PatchFirewallVirtualIPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallVirtualIPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallVirtualIPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallVirtualIPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallVirtualIPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallVirtualIPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallVirtualIPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallVirtualIPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallVirtualIPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallVirtualIPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallVirtualIPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallVirtualIPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallVirtualIPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallVirtualIPEndpointResponse400
    | PatchFirewallVirtualIPEndpointResponse401
    | PatchFirewallVirtualIPEndpointResponse403
    | PatchFirewallVirtualIPEndpointResponse404
    | PatchFirewallVirtualIPEndpointResponse405
    | PatchFirewallVirtualIPEndpointResponse406
    | PatchFirewallVirtualIPEndpointResponse409
    | PatchFirewallVirtualIPEndpointResponse415
    | PatchFirewallVirtualIPEndpointResponse422
    | PatchFirewallVirtualIPEndpointResponse424
    | PatchFirewallVirtualIPEndpointResponse500
    | PatchFirewallVirtualIPEndpointResponse503
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
    body: PatchFirewallVirtualIPEndpointJsonBody | PatchFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallVirtualIPEndpointResponse400
    | PatchFirewallVirtualIPEndpointResponse401
    | PatchFirewallVirtualIPEndpointResponse403
    | PatchFirewallVirtualIPEndpointResponse404
    | PatchFirewallVirtualIPEndpointResponse405
    | PatchFirewallVirtualIPEndpointResponse406
    | PatchFirewallVirtualIPEndpointResponse409
    | PatchFirewallVirtualIPEndpointResponse415
    | PatchFirewallVirtualIPEndpointResponse422
    | PatchFirewallVirtualIPEndpointResponse424
    | PatchFirewallVirtualIPEndpointResponse500
    | PatchFirewallVirtualIPEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallVirtualIPEndpointJsonBody | Unset):
        body (PatchFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallVirtualIPEndpointResponse400 | PatchFirewallVirtualIPEndpointResponse401 | PatchFirewallVirtualIPEndpointResponse403 | PatchFirewallVirtualIPEndpointResponse404 | PatchFirewallVirtualIPEndpointResponse405 | PatchFirewallVirtualIPEndpointResponse406 | PatchFirewallVirtualIPEndpointResponse409 | PatchFirewallVirtualIPEndpointResponse415 | PatchFirewallVirtualIPEndpointResponse422 | PatchFirewallVirtualIPEndpointResponse424 | PatchFirewallVirtualIPEndpointResponse500 | PatchFirewallVirtualIPEndpointResponse503]
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
    body: PatchFirewallVirtualIPEndpointJsonBody | PatchFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallVirtualIPEndpointResponse400
    | PatchFirewallVirtualIPEndpointResponse401
    | PatchFirewallVirtualIPEndpointResponse403
    | PatchFirewallVirtualIPEndpointResponse404
    | PatchFirewallVirtualIPEndpointResponse405
    | PatchFirewallVirtualIPEndpointResponse406
    | PatchFirewallVirtualIPEndpointResponse409
    | PatchFirewallVirtualIPEndpointResponse415
    | PatchFirewallVirtualIPEndpointResponse422
    | PatchFirewallVirtualIPEndpointResponse424
    | PatchFirewallVirtualIPEndpointResponse500
    | PatchFirewallVirtualIPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallVirtualIPEndpointJsonBody | Unset):
        body (PatchFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallVirtualIPEndpointResponse400 | PatchFirewallVirtualIPEndpointResponse401 | PatchFirewallVirtualIPEndpointResponse403 | PatchFirewallVirtualIPEndpointResponse404 | PatchFirewallVirtualIPEndpointResponse405 | PatchFirewallVirtualIPEndpointResponse406 | PatchFirewallVirtualIPEndpointResponse409 | PatchFirewallVirtualIPEndpointResponse415 | PatchFirewallVirtualIPEndpointResponse422 | PatchFirewallVirtualIPEndpointResponse424 | PatchFirewallVirtualIPEndpointResponse500 | PatchFirewallVirtualIPEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallVirtualIPEndpointJsonBody | PatchFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallVirtualIPEndpointResponse400
    | PatchFirewallVirtualIPEndpointResponse401
    | PatchFirewallVirtualIPEndpointResponse403
    | PatchFirewallVirtualIPEndpointResponse404
    | PatchFirewallVirtualIPEndpointResponse405
    | PatchFirewallVirtualIPEndpointResponse406
    | PatchFirewallVirtualIPEndpointResponse409
    | PatchFirewallVirtualIPEndpointResponse415
    | PatchFirewallVirtualIPEndpointResponse422
    | PatchFirewallVirtualIPEndpointResponse424
    | PatchFirewallVirtualIPEndpointResponse500
    | PatchFirewallVirtualIPEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallVirtualIPEndpointJsonBody | Unset):
        body (PatchFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallVirtualIPEndpointResponse400 | PatchFirewallVirtualIPEndpointResponse401 | PatchFirewallVirtualIPEndpointResponse403 | PatchFirewallVirtualIPEndpointResponse404 | PatchFirewallVirtualIPEndpointResponse405 | PatchFirewallVirtualIPEndpointResponse406 | PatchFirewallVirtualIPEndpointResponse409 | PatchFirewallVirtualIPEndpointResponse415 | PatchFirewallVirtualIPEndpointResponse422 | PatchFirewallVirtualIPEndpointResponse424 | PatchFirewallVirtualIPEndpointResponse500 | PatchFirewallVirtualIPEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallVirtualIPEndpointJsonBody | PatchFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallVirtualIPEndpointResponse400
    | PatchFirewallVirtualIPEndpointResponse401
    | PatchFirewallVirtualIPEndpointResponse403
    | PatchFirewallVirtualIPEndpointResponse404
    | PatchFirewallVirtualIPEndpointResponse405
    | PatchFirewallVirtualIPEndpointResponse406
    | PatchFirewallVirtualIPEndpointResponse409
    | PatchFirewallVirtualIPEndpointResponse415
    | PatchFirewallVirtualIPEndpointResponse422
    | PatchFirewallVirtualIPEndpointResponse424
    | PatchFirewallVirtualIPEndpointResponse500
    | PatchFirewallVirtualIPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallVirtualIPEndpointJsonBody | Unset):
        body (PatchFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallVirtualIPEndpointResponse400 | PatchFirewallVirtualIPEndpointResponse401 | PatchFirewallVirtualIPEndpointResponse403 | PatchFirewallVirtualIPEndpointResponse404 | PatchFirewallVirtualIPEndpointResponse405 | PatchFirewallVirtualIPEndpointResponse406 | PatchFirewallVirtualIPEndpointResponse409 | PatchFirewallVirtualIPEndpointResponse415 | PatchFirewallVirtualIPEndpointResponse422 | PatchFirewallVirtualIPEndpointResponse424 | PatchFirewallVirtualIPEndpointResponse500 | PatchFirewallVirtualIPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
