from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_advanced_settings_endpoint_response_400 import (
    GetFirewallAdvancedSettingsEndpointResponse400,
)
from ...models.get_firewall_advanced_settings_endpoint_response_401 import (
    GetFirewallAdvancedSettingsEndpointResponse401,
)
from ...models.get_firewall_advanced_settings_endpoint_response_403 import (
    GetFirewallAdvancedSettingsEndpointResponse403,
)
from ...models.get_firewall_advanced_settings_endpoint_response_404 import (
    GetFirewallAdvancedSettingsEndpointResponse404,
)
from ...models.get_firewall_advanced_settings_endpoint_response_405 import (
    GetFirewallAdvancedSettingsEndpointResponse405,
)
from ...models.get_firewall_advanced_settings_endpoint_response_406 import (
    GetFirewallAdvancedSettingsEndpointResponse406,
)
from ...models.get_firewall_advanced_settings_endpoint_response_409 import (
    GetFirewallAdvancedSettingsEndpointResponse409,
)
from ...models.get_firewall_advanced_settings_endpoint_response_415 import (
    GetFirewallAdvancedSettingsEndpointResponse415,
)
from ...models.get_firewall_advanced_settings_endpoint_response_422 import (
    GetFirewallAdvancedSettingsEndpointResponse422,
)
from ...models.get_firewall_advanced_settings_endpoint_response_424 import (
    GetFirewallAdvancedSettingsEndpointResponse424,
)
from ...models.get_firewall_advanced_settings_endpoint_response_500 import (
    GetFirewallAdvancedSettingsEndpointResponse500,
)
from ...models.get_firewall_advanced_settings_endpoint_response_503 import (
    GetFirewallAdvancedSettingsEndpointResponse503,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/firewall/advanced_settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallAdvancedSettingsEndpointResponse400
    | GetFirewallAdvancedSettingsEndpointResponse401
    | GetFirewallAdvancedSettingsEndpointResponse403
    | GetFirewallAdvancedSettingsEndpointResponse404
    | GetFirewallAdvancedSettingsEndpointResponse405
    | GetFirewallAdvancedSettingsEndpointResponse406
    | GetFirewallAdvancedSettingsEndpointResponse409
    | GetFirewallAdvancedSettingsEndpointResponse415
    | GetFirewallAdvancedSettingsEndpointResponse422
    | GetFirewallAdvancedSettingsEndpointResponse424
    | GetFirewallAdvancedSettingsEndpointResponse500
    | GetFirewallAdvancedSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallAdvancedSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallAdvancedSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallAdvancedSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallAdvancedSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallAdvancedSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallAdvancedSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallAdvancedSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallAdvancedSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallAdvancedSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallAdvancedSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallAdvancedSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallAdvancedSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallAdvancedSettingsEndpointResponse400
    | GetFirewallAdvancedSettingsEndpointResponse401
    | GetFirewallAdvancedSettingsEndpointResponse403
    | GetFirewallAdvancedSettingsEndpointResponse404
    | GetFirewallAdvancedSettingsEndpointResponse405
    | GetFirewallAdvancedSettingsEndpointResponse406
    | GetFirewallAdvancedSettingsEndpointResponse409
    | GetFirewallAdvancedSettingsEndpointResponse415
    | GetFirewallAdvancedSettingsEndpointResponse422
    | GetFirewallAdvancedSettingsEndpointResponse424
    | GetFirewallAdvancedSettingsEndpointResponse500
    | GetFirewallAdvancedSettingsEndpointResponse503
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
    GetFirewallAdvancedSettingsEndpointResponse400
    | GetFirewallAdvancedSettingsEndpointResponse401
    | GetFirewallAdvancedSettingsEndpointResponse403
    | GetFirewallAdvancedSettingsEndpointResponse404
    | GetFirewallAdvancedSettingsEndpointResponse405
    | GetFirewallAdvancedSettingsEndpointResponse406
    | GetFirewallAdvancedSettingsEndpointResponse409
    | GetFirewallAdvancedSettingsEndpointResponse415
    | GetFirewallAdvancedSettingsEndpointResponse422
    | GetFirewallAdvancedSettingsEndpointResponse424
    | GetFirewallAdvancedSettingsEndpointResponse500
    | GetFirewallAdvancedSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallAdvancedSettingsEndpointResponse400 | GetFirewallAdvancedSettingsEndpointResponse401 | GetFirewallAdvancedSettingsEndpointResponse403 | GetFirewallAdvancedSettingsEndpointResponse404 | GetFirewallAdvancedSettingsEndpointResponse405 | GetFirewallAdvancedSettingsEndpointResponse406 | GetFirewallAdvancedSettingsEndpointResponse409 | GetFirewallAdvancedSettingsEndpointResponse415 | GetFirewallAdvancedSettingsEndpointResponse422 | GetFirewallAdvancedSettingsEndpointResponse424 | GetFirewallAdvancedSettingsEndpointResponse500 | GetFirewallAdvancedSettingsEndpointResponse503]
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
    GetFirewallAdvancedSettingsEndpointResponse400
    | GetFirewallAdvancedSettingsEndpointResponse401
    | GetFirewallAdvancedSettingsEndpointResponse403
    | GetFirewallAdvancedSettingsEndpointResponse404
    | GetFirewallAdvancedSettingsEndpointResponse405
    | GetFirewallAdvancedSettingsEndpointResponse406
    | GetFirewallAdvancedSettingsEndpointResponse409
    | GetFirewallAdvancedSettingsEndpointResponse415
    | GetFirewallAdvancedSettingsEndpointResponse422
    | GetFirewallAdvancedSettingsEndpointResponse424
    | GetFirewallAdvancedSettingsEndpointResponse500
    | GetFirewallAdvancedSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallAdvancedSettingsEndpointResponse400 | GetFirewallAdvancedSettingsEndpointResponse401 | GetFirewallAdvancedSettingsEndpointResponse403 | GetFirewallAdvancedSettingsEndpointResponse404 | GetFirewallAdvancedSettingsEndpointResponse405 | GetFirewallAdvancedSettingsEndpointResponse406 | GetFirewallAdvancedSettingsEndpointResponse409 | GetFirewallAdvancedSettingsEndpointResponse415 | GetFirewallAdvancedSettingsEndpointResponse422 | GetFirewallAdvancedSettingsEndpointResponse424 | GetFirewallAdvancedSettingsEndpointResponse500 | GetFirewallAdvancedSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetFirewallAdvancedSettingsEndpointResponse400
    | GetFirewallAdvancedSettingsEndpointResponse401
    | GetFirewallAdvancedSettingsEndpointResponse403
    | GetFirewallAdvancedSettingsEndpointResponse404
    | GetFirewallAdvancedSettingsEndpointResponse405
    | GetFirewallAdvancedSettingsEndpointResponse406
    | GetFirewallAdvancedSettingsEndpointResponse409
    | GetFirewallAdvancedSettingsEndpointResponse415
    | GetFirewallAdvancedSettingsEndpointResponse422
    | GetFirewallAdvancedSettingsEndpointResponse424
    | GetFirewallAdvancedSettingsEndpointResponse500
    | GetFirewallAdvancedSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallAdvancedSettingsEndpointResponse400 | GetFirewallAdvancedSettingsEndpointResponse401 | GetFirewallAdvancedSettingsEndpointResponse403 | GetFirewallAdvancedSettingsEndpointResponse404 | GetFirewallAdvancedSettingsEndpointResponse405 | GetFirewallAdvancedSettingsEndpointResponse406 | GetFirewallAdvancedSettingsEndpointResponse409 | GetFirewallAdvancedSettingsEndpointResponse415 | GetFirewallAdvancedSettingsEndpointResponse422 | GetFirewallAdvancedSettingsEndpointResponse424 | GetFirewallAdvancedSettingsEndpointResponse500 | GetFirewallAdvancedSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetFirewallAdvancedSettingsEndpointResponse400
    | GetFirewallAdvancedSettingsEndpointResponse401
    | GetFirewallAdvancedSettingsEndpointResponse403
    | GetFirewallAdvancedSettingsEndpointResponse404
    | GetFirewallAdvancedSettingsEndpointResponse405
    | GetFirewallAdvancedSettingsEndpointResponse406
    | GetFirewallAdvancedSettingsEndpointResponse409
    | GetFirewallAdvancedSettingsEndpointResponse415
    | GetFirewallAdvancedSettingsEndpointResponse422
    | GetFirewallAdvancedSettingsEndpointResponse424
    | GetFirewallAdvancedSettingsEndpointResponse500
    | GetFirewallAdvancedSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallAdvancedSettingsEndpointResponse400 | GetFirewallAdvancedSettingsEndpointResponse401 | GetFirewallAdvancedSettingsEndpointResponse403 | GetFirewallAdvancedSettingsEndpointResponse404 | GetFirewallAdvancedSettingsEndpointResponse405 | GetFirewallAdvancedSettingsEndpointResponse406 | GetFirewallAdvancedSettingsEndpointResponse409 | GetFirewallAdvancedSettingsEndpointResponse415 | GetFirewallAdvancedSettingsEndpointResponse422 | GetFirewallAdvancedSettingsEndpointResponse424 | GetFirewallAdvancedSettingsEndpointResponse500 | GetFirewallAdvancedSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
