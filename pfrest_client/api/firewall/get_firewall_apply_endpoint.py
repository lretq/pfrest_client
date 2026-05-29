from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_apply_endpoint_response_400 import GetFirewallApplyEndpointResponse400
from ...models.get_firewall_apply_endpoint_response_401 import GetFirewallApplyEndpointResponse401
from ...models.get_firewall_apply_endpoint_response_403 import GetFirewallApplyEndpointResponse403
from ...models.get_firewall_apply_endpoint_response_404 import GetFirewallApplyEndpointResponse404
from ...models.get_firewall_apply_endpoint_response_405 import GetFirewallApplyEndpointResponse405
from ...models.get_firewall_apply_endpoint_response_406 import GetFirewallApplyEndpointResponse406
from ...models.get_firewall_apply_endpoint_response_409 import GetFirewallApplyEndpointResponse409
from ...models.get_firewall_apply_endpoint_response_415 import GetFirewallApplyEndpointResponse415
from ...models.get_firewall_apply_endpoint_response_422 import GetFirewallApplyEndpointResponse422
from ...models.get_firewall_apply_endpoint_response_424 import GetFirewallApplyEndpointResponse424
from ...models.get_firewall_apply_endpoint_response_500 import GetFirewallApplyEndpointResponse500
from ...models.get_firewall_apply_endpoint_response_503 import GetFirewallApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/firewall/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallApplyEndpointResponse400
    | GetFirewallApplyEndpointResponse401
    | GetFirewallApplyEndpointResponse403
    | GetFirewallApplyEndpointResponse404
    | GetFirewallApplyEndpointResponse405
    | GetFirewallApplyEndpointResponse406
    | GetFirewallApplyEndpointResponse409
    | GetFirewallApplyEndpointResponse415
    | GetFirewallApplyEndpointResponse422
    | GetFirewallApplyEndpointResponse424
    | GetFirewallApplyEndpointResponse500
    | GetFirewallApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallApplyEndpointResponse400
    | GetFirewallApplyEndpointResponse401
    | GetFirewallApplyEndpointResponse403
    | GetFirewallApplyEndpointResponse404
    | GetFirewallApplyEndpointResponse405
    | GetFirewallApplyEndpointResponse406
    | GetFirewallApplyEndpointResponse409
    | GetFirewallApplyEndpointResponse415
    | GetFirewallApplyEndpointResponse422
    | GetFirewallApplyEndpointResponse424
    | GetFirewallApplyEndpointResponse500
    | GetFirewallApplyEndpointResponse503
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
    GetFirewallApplyEndpointResponse400
    | GetFirewallApplyEndpointResponse401
    | GetFirewallApplyEndpointResponse403
    | GetFirewallApplyEndpointResponse404
    | GetFirewallApplyEndpointResponse405
    | GetFirewallApplyEndpointResponse406
    | GetFirewallApplyEndpointResponse409
    | GetFirewallApplyEndpointResponse415
    | GetFirewallApplyEndpointResponse422
    | GetFirewallApplyEndpointResponse424
    | GetFirewallApplyEndpointResponse500
    | GetFirewallApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending firewall change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallApplyEndpointResponse400 | GetFirewallApplyEndpointResponse401 | GetFirewallApplyEndpointResponse403 | GetFirewallApplyEndpointResponse404 | GetFirewallApplyEndpointResponse405 | GetFirewallApplyEndpointResponse406 | GetFirewallApplyEndpointResponse409 | GetFirewallApplyEndpointResponse415 | GetFirewallApplyEndpointResponse422 | GetFirewallApplyEndpointResponse424 | GetFirewallApplyEndpointResponse500 | GetFirewallApplyEndpointResponse503]
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
    GetFirewallApplyEndpointResponse400
    | GetFirewallApplyEndpointResponse401
    | GetFirewallApplyEndpointResponse403
    | GetFirewallApplyEndpointResponse404
    | GetFirewallApplyEndpointResponse405
    | GetFirewallApplyEndpointResponse406
    | GetFirewallApplyEndpointResponse409
    | GetFirewallApplyEndpointResponse415
    | GetFirewallApplyEndpointResponse422
    | GetFirewallApplyEndpointResponse424
    | GetFirewallApplyEndpointResponse500
    | GetFirewallApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending firewall change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallApplyEndpointResponse400 | GetFirewallApplyEndpointResponse401 | GetFirewallApplyEndpointResponse403 | GetFirewallApplyEndpointResponse404 | GetFirewallApplyEndpointResponse405 | GetFirewallApplyEndpointResponse406 | GetFirewallApplyEndpointResponse409 | GetFirewallApplyEndpointResponse415 | GetFirewallApplyEndpointResponse422 | GetFirewallApplyEndpointResponse424 | GetFirewallApplyEndpointResponse500 | GetFirewallApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetFirewallApplyEndpointResponse400
    | GetFirewallApplyEndpointResponse401
    | GetFirewallApplyEndpointResponse403
    | GetFirewallApplyEndpointResponse404
    | GetFirewallApplyEndpointResponse405
    | GetFirewallApplyEndpointResponse406
    | GetFirewallApplyEndpointResponse409
    | GetFirewallApplyEndpointResponse415
    | GetFirewallApplyEndpointResponse422
    | GetFirewallApplyEndpointResponse424
    | GetFirewallApplyEndpointResponse500
    | GetFirewallApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending firewall change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallApplyEndpointResponse400 | GetFirewallApplyEndpointResponse401 | GetFirewallApplyEndpointResponse403 | GetFirewallApplyEndpointResponse404 | GetFirewallApplyEndpointResponse405 | GetFirewallApplyEndpointResponse406 | GetFirewallApplyEndpointResponse409 | GetFirewallApplyEndpointResponse415 | GetFirewallApplyEndpointResponse422 | GetFirewallApplyEndpointResponse424 | GetFirewallApplyEndpointResponse500 | GetFirewallApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetFirewallApplyEndpointResponse400
    | GetFirewallApplyEndpointResponse401
    | GetFirewallApplyEndpointResponse403
    | GetFirewallApplyEndpointResponse404
    | GetFirewallApplyEndpointResponse405
    | GetFirewallApplyEndpointResponse406
    | GetFirewallApplyEndpointResponse409
    | GetFirewallApplyEndpointResponse415
    | GetFirewallApplyEndpointResponse422
    | GetFirewallApplyEndpointResponse424
    | GetFirewallApplyEndpointResponse500
    | GetFirewallApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending firewall change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallApplyEndpointResponse400 | GetFirewallApplyEndpointResponse401 | GetFirewallApplyEndpointResponse403 | GetFirewallApplyEndpointResponse404 | GetFirewallApplyEndpointResponse405 | GetFirewallApplyEndpointResponse406 | GetFirewallApplyEndpointResponse409 | GetFirewallApplyEndpointResponse415 | GetFirewallApplyEndpointResponse422 | GetFirewallApplyEndpointResponse424 | GetFirewallApplyEndpointResponse500 | GetFirewallApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
