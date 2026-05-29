from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_advanced_settings_endpoint_data_body import PatchFirewallAdvancedSettingsEndpointDataBody
from ...models.patch_firewall_advanced_settings_endpoint_json_body import PatchFirewallAdvancedSettingsEndpointJsonBody
from ...models.patch_firewall_advanced_settings_endpoint_response_400 import (
    PatchFirewallAdvancedSettingsEndpointResponse400,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_401 import (
    PatchFirewallAdvancedSettingsEndpointResponse401,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_403 import (
    PatchFirewallAdvancedSettingsEndpointResponse403,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_404 import (
    PatchFirewallAdvancedSettingsEndpointResponse404,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_405 import (
    PatchFirewallAdvancedSettingsEndpointResponse405,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_406 import (
    PatchFirewallAdvancedSettingsEndpointResponse406,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_409 import (
    PatchFirewallAdvancedSettingsEndpointResponse409,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_415 import (
    PatchFirewallAdvancedSettingsEndpointResponse415,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_422 import (
    PatchFirewallAdvancedSettingsEndpointResponse422,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_424 import (
    PatchFirewallAdvancedSettingsEndpointResponse424,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_500 import (
    PatchFirewallAdvancedSettingsEndpointResponse500,
)
from ...models.patch_firewall_advanced_settings_endpoint_response_503 import (
    PatchFirewallAdvancedSettingsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallAdvancedSettingsEndpointJsonBody | PatchFirewallAdvancedSettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/advanced_settings",
    }

    if isinstance(body, PatchFirewallAdvancedSettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallAdvancedSettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallAdvancedSettingsEndpointResponse400
    | PatchFirewallAdvancedSettingsEndpointResponse401
    | PatchFirewallAdvancedSettingsEndpointResponse403
    | PatchFirewallAdvancedSettingsEndpointResponse404
    | PatchFirewallAdvancedSettingsEndpointResponse405
    | PatchFirewallAdvancedSettingsEndpointResponse406
    | PatchFirewallAdvancedSettingsEndpointResponse409
    | PatchFirewallAdvancedSettingsEndpointResponse415
    | PatchFirewallAdvancedSettingsEndpointResponse422
    | PatchFirewallAdvancedSettingsEndpointResponse424
    | PatchFirewallAdvancedSettingsEndpointResponse500
    | PatchFirewallAdvancedSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallAdvancedSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallAdvancedSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallAdvancedSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallAdvancedSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallAdvancedSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallAdvancedSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallAdvancedSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallAdvancedSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallAdvancedSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallAdvancedSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallAdvancedSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallAdvancedSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallAdvancedSettingsEndpointResponse400
    | PatchFirewallAdvancedSettingsEndpointResponse401
    | PatchFirewallAdvancedSettingsEndpointResponse403
    | PatchFirewallAdvancedSettingsEndpointResponse404
    | PatchFirewallAdvancedSettingsEndpointResponse405
    | PatchFirewallAdvancedSettingsEndpointResponse406
    | PatchFirewallAdvancedSettingsEndpointResponse409
    | PatchFirewallAdvancedSettingsEndpointResponse415
    | PatchFirewallAdvancedSettingsEndpointResponse422
    | PatchFirewallAdvancedSettingsEndpointResponse424
    | PatchFirewallAdvancedSettingsEndpointResponse500
    | PatchFirewallAdvancedSettingsEndpointResponse503
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
    body: PatchFirewallAdvancedSettingsEndpointJsonBody | PatchFirewallAdvancedSettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallAdvancedSettingsEndpointResponse400
    | PatchFirewallAdvancedSettingsEndpointResponse401
    | PatchFirewallAdvancedSettingsEndpointResponse403
    | PatchFirewallAdvancedSettingsEndpointResponse404
    | PatchFirewallAdvancedSettingsEndpointResponse405
    | PatchFirewallAdvancedSettingsEndpointResponse406
    | PatchFirewallAdvancedSettingsEndpointResponse409
    | PatchFirewallAdvancedSettingsEndpointResponse415
    | PatchFirewallAdvancedSettingsEndpointResponse422
    | PatchFirewallAdvancedSettingsEndpointResponse424
    | PatchFirewallAdvancedSettingsEndpointResponse500
    | PatchFirewallAdvancedSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallAdvancedSettingsEndpointJsonBody | Unset):
        body (PatchFirewallAdvancedSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallAdvancedSettingsEndpointResponse400 | PatchFirewallAdvancedSettingsEndpointResponse401 | PatchFirewallAdvancedSettingsEndpointResponse403 | PatchFirewallAdvancedSettingsEndpointResponse404 | PatchFirewallAdvancedSettingsEndpointResponse405 | PatchFirewallAdvancedSettingsEndpointResponse406 | PatchFirewallAdvancedSettingsEndpointResponse409 | PatchFirewallAdvancedSettingsEndpointResponse415 | PatchFirewallAdvancedSettingsEndpointResponse422 | PatchFirewallAdvancedSettingsEndpointResponse424 | PatchFirewallAdvancedSettingsEndpointResponse500 | PatchFirewallAdvancedSettingsEndpointResponse503]
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
    body: PatchFirewallAdvancedSettingsEndpointJsonBody | PatchFirewallAdvancedSettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallAdvancedSettingsEndpointResponse400
    | PatchFirewallAdvancedSettingsEndpointResponse401
    | PatchFirewallAdvancedSettingsEndpointResponse403
    | PatchFirewallAdvancedSettingsEndpointResponse404
    | PatchFirewallAdvancedSettingsEndpointResponse405
    | PatchFirewallAdvancedSettingsEndpointResponse406
    | PatchFirewallAdvancedSettingsEndpointResponse409
    | PatchFirewallAdvancedSettingsEndpointResponse415
    | PatchFirewallAdvancedSettingsEndpointResponse422
    | PatchFirewallAdvancedSettingsEndpointResponse424
    | PatchFirewallAdvancedSettingsEndpointResponse500
    | PatchFirewallAdvancedSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallAdvancedSettingsEndpointJsonBody | Unset):
        body (PatchFirewallAdvancedSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallAdvancedSettingsEndpointResponse400 | PatchFirewallAdvancedSettingsEndpointResponse401 | PatchFirewallAdvancedSettingsEndpointResponse403 | PatchFirewallAdvancedSettingsEndpointResponse404 | PatchFirewallAdvancedSettingsEndpointResponse405 | PatchFirewallAdvancedSettingsEndpointResponse406 | PatchFirewallAdvancedSettingsEndpointResponse409 | PatchFirewallAdvancedSettingsEndpointResponse415 | PatchFirewallAdvancedSettingsEndpointResponse422 | PatchFirewallAdvancedSettingsEndpointResponse424 | PatchFirewallAdvancedSettingsEndpointResponse500 | PatchFirewallAdvancedSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallAdvancedSettingsEndpointJsonBody | PatchFirewallAdvancedSettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallAdvancedSettingsEndpointResponse400
    | PatchFirewallAdvancedSettingsEndpointResponse401
    | PatchFirewallAdvancedSettingsEndpointResponse403
    | PatchFirewallAdvancedSettingsEndpointResponse404
    | PatchFirewallAdvancedSettingsEndpointResponse405
    | PatchFirewallAdvancedSettingsEndpointResponse406
    | PatchFirewallAdvancedSettingsEndpointResponse409
    | PatchFirewallAdvancedSettingsEndpointResponse415
    | PatchFirewallAdvancedSettingsEndpointResponse422
    | PatchFirewallAdvancedSettingsEndpointResponse424
    | PatchFirewallAdvancedSettingsEndpointResponse500
    | PatchFirewallAdvancedSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallAdvancedSettingsEndpointJsonBody | Unset):
        body (PatchFirewallAdvancedSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallAdvancedSettingsEndpointResponse400 | PatchFirewallAdvancedSettingsEndpointResponse401 | PatchFirewallAdvancedSettingsEndpointResponse403 | PatchFirewallAdvancedSettingsEndpointResponse404 | PatchFirewallAdvancedSettingsEndpointResponse405 | PatchFirewallAdvancedSettingsEndpointResponse406 | PatchFirewallAdvancedSettingsEndpointResponse409 | PatchFirewallAdvancedSettingsEndpointResponse415 | PatchFirewallAdvancedSettingsEndpointResponse422 | PatchFirewallAdvancedSettingsEndpointResponse424 | PatchFirewallAdvancedSettingsEndpointResponse500 | PatchFirewallAdvancedSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallAdvancedSettingsEndpointJsonBody | PatchFirewallAdvancedSettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallAdvancedSettingsEndpointResponse400
    | PatchFirewallAdvancedSettingsEndpointResponse401
    | PatchFirewallAdvancedSettingsEndpointResponse403
    | PatchFirewallAdvancedSettingsEndpointResponse404
    | PatchFirewallAdvancedSettingsEndpointResponse405
    | PatchFirewallAdvancedSettingsEndpointResponse406
    | PatchFirewallAdvancedSettingsEndpointResponse409
    | PatchFirewallAdvancedSettingsEndpointResponse415
    | PatchFirewallAdvancedSettingsEndpointResponse422
    | PatchFirewallAdvancedSettingsEndpointResponse424
    | PatchFirewallAdvancedSettingsEndpointResponse500
    | PatchFirewallAdvancedSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Firewall Advanced Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: FirewallAdvancedSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-advanced-settings-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallAdvancedSettingsEndpointJsonBody | Unset):
        body (PatchFirewallAdvancedSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallAdvancedSettingsEndpointResponse400 | PatchFirewallAdvancedSettingsEndpointResponse401 | PatchFirewallAdvancedSettingsEndpointResponse403 | PatchFirewallAdvancedSettingsEndpointResponse404 | PatchFirewallAdvancedSettingsEndpointResponse405 | PatchFirewallAdvancedSettingsEndpointResponse406 | PatchFirewallAdvancedSettingsEndpointResponse409 | PatchFirewallAdvancedSettingsEndpointResponse415 | PatchFirewallAdvancedSettingsEndpointResponse422 | PatchFirewallAdvancedSettingsEndpointResponse424 | PatchFirewallAdvancedSettingsEndpointResponse500 | PatchFirewallAdvancedSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
