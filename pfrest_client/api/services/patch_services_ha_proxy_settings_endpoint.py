from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_settings_endpoint_data_body import PatchServicesHAProxySettingsEndpointDataBody
from ...models.patch_services_ha_proxy_settings_endpoint_json_body import PatchServicesHAProxySettingsEndpointJsonBody
from ...models.patch_services_ha_proxy_settings_endpoint_response_400 import (
    PatchServicesHAProxySettingsEndpointResponse400,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_401 import (
    PatchServicesHAProxySettingsEndpointResponse401,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_403 import (
    PatchServicesHAProxySettingsEndpointResponse403,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_404 import (
    PatchServicesHAProxySettingsEndpointResponse404,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_405 import (
    PatchServicesHAProxySettingsEndpointResponse405,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_406 import (
    PatchServicesHAProxySettingsEndpointResponse406,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_409 import (
    PatchServicesHAProxySettingsEndpointResponse409,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_415 import (
    PatchServicesHAProxySettingsEndpointResponse415,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_422 import (
    PatchServicesHAProxySettingsEndpointResponse422,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_424 import (
    PatchServicesHAProxySettingsEndpointResponse424,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_500 import (
    PatchServicesHAProxySettingsEndpointResponse500,
)
from ...models.patch_services_ha_proxy_settings_endpoint_response_503 import (
    PatchServicesHAProxySettingsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxySettingsEndpointJsonBody | PatchServicesHAProxySettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/settings",
    }

    if isinstance(body, PatchServicesHAProxySettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxySettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxySettingsEndpointResponse400
    | PatchServicesHAProxySettingsEndpointResponse401
    | PatchServicesHAProxySettingsEndpointResponse403
    | PatchServicesHAProxySettingsEndpointResponse404
    | PatchServicesHAProxySettingsEndpointResponse405
    | PatchServicesHAProxySettingsEndpointResponse406
    | PatchServicesHAProxySettingsEndpointResponse409
    | PatchServicesHAProxySettingsEndpointResponse415
    | PatchServicesHAProxySettingsEndpointResponse422
    | PatchServicesHAProxySettingsEndpointResponse424
    | PatchServicesHAProxySettingsEndpointResponse500
    | PatchServicesHAProxySettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxySettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxySettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxySettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxySettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxySettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxySettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxySettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxySettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxySettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxySettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxySettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxySettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxySettingsEndpointResponse400
    | PatchServicesHAProxySettingsEndpointResponse401
    | PatchServicesHAProxySettingsEndpointResponse403
    | PatchServicesHAProxySettingsEndpointResponse404
    | PatchServicesHAProxySettingsEndpointResponse405
    | PatchServicesHAProxySettingsEndpointResponse406
    | PatchServicesHAProxySettingsEndpointResponse409
    | PatchServicesHAProxySettingsEndpointResponse415
    | PatchServicesHAProxySettingsEndpointResponse422
    | PatchServicesHAProxySettingsEndpointResponse424
    | PatchServicesHAProxySettingsEndpointResponse500
    | PatchServicesHAProxySettingsEndpointResponse503
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
    body: PatchServicesHAProxySettingsEndpointJsonBody | PatchServicesHAProxySettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxySettingsEndpointResponse400
    | PatchServicesHAProxySettingsEndpointResponse401
    | PatchServicesHAProxySettingsEndpointResponse403
    | PatchServicesHAProxySettingsEndpointResponse404
    | PatchServicesHAProxySettingsEndpointResponse405
    | PatchServicesHAProxySettingsEndpointResponse406
    | PatchServicesHAProxySettingsEndpointResponse409
    | PatchServicesHAProxySettingsEndpointResponse415
    | PatchServicesHAProxySettingsEndpointResponse422
    | PatchServicesHAProxySettingsEndpointResponse424
    | PatchServicesHAProxySettingsEndpointResponse500
    | PatchServicesHAProxySettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current HAProxy Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxySettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxySettingsEndpointResponse400 | PatchServicesHAProxySettingsEndpointResponse401 | PatchServicesHAProxySettingsEndpointResponse403 | PatchServicesHAProxySettingsEndpointResponse404 | PatchServicesHAProxySettingsEndpointResponse405 | PatchServicesHAProxySettingsEndpointResponse406 | PatchServicesHAProxySettingsEndpointResponse409 | PatchServicesHAProxySettingsEndpointResponse415 | PatchServicesHAProxySettingsEndpointResponse422 | PatchServicesHAProxySettingsEndpointResponse424 | PatchServicesHAProxySettingsEndpointResponse500 | PatchServicesHAProxySettingsEndpointResponse503]
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
    body: PatchServicesHAProxySettingsEndpointJsonBody | PatchServicesHAProxySettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxySettingsEndpointResponse400
    | PatchServicesHAProxySettingsEndpointResponse401
    | PatchServicesHAProxySettingsEndpointResponse403
    | PatchServicesHAProxySettingsEndpointResponse404
    | PatchServicesHAProxySettingsEndpointResponse405
    | PatchServicesHAProxySettingsEndpointResponse406
    | PatchServicesHAProxySettingsEndpointResponse409
    | PatchServicesHAProxySettingsEndpointResponse415
    | PatchServicesHAProxySettingsEndpointResponse422
    | PatchServicesHAProxySettingsEndpointResponse424
    | PatchServicesHAProxySettingsEndpointResponse500
    | PatchServicesHAProxySettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current HAProxy Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxySettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxySettingsEndpointResponse400 | PatchServicesHAProxySettingsEndpointResponse401 | PatchServicesHAProxySettingsEndpointResponse403 | PatchServicesHAProxySettingsEndpointResponse404 | PatchServicesHAProxySettingsEndpointResponse405 | PatchServicesHAProxySettingsEndpointResponse406 | PatchServicesHAProxySettingsEndpointResponse409 | PatchServicesHAProxySettingsEndpointResponse415 | PatchServicesHAProxySettingsEndpointResponse422 | PatchServicesHAProxySettingsEndpointResponse424 | PatchServicesHAProxySettingsEndpointResponse500 | PatchServicesHAProxySettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxySettingsEndpointJsonBody | PatchServicesHAProxySettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxySettingsEndpointResponse400
    | PatchServicesHAProxySettingsEndpointResponse401
    | PatchServicesHAProxySettingsEndpointResponse403
    | PatchServicesHAProxySettingsEndpointResponse404
    | PatchServicesHAProxySettingsEndpointResponse405
    | PatchServicesHAProxySettingsEndpointResponse406
    | PatchServicesHAProxySettingsEndpointResponse409
    | PatchServicesHAProxySettingsEndpointResponse415
    | PatchServicesHAProxySettingsEndpointResponse422
    | PatchServicesHAProxySettingsEndpointResponse424
    | PatchServicesHAProxySettingsEndpointResponse500
    | PatchServicesHAProxySettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current HAProxy Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxySettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxySettingsEndpointResponse400 | PatchServicesHAProxySettingsEndpointResponse401 | PatchServicesHAProxySettingsEndpointResponse403 | PatchServicesHAProxySettingsEndpointResponse404 | PatchServicesHAProxySettingsEndpointResponse405 | PatchServicesHAProxySettingsEndpointResponse406 | PatchServicesHAProxySettingsEndpointResponse409 | PatchServicesHAProxySettingsEndpointResponse415 | PatchServicesHAProxySettingsEndpointResponse422 | PatchServicesHAProxySettingsEndpointResponse424 | PatchServicesHAProxySettingsEndpointResponse500 | PatchServicesHAProxySettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxySettingsEndpointJsonBody | PatchServicesHAProxySettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxySettingsEndpointResponse400
    | PatchServicesHAProxySettingsEndpointResponse401
    | PatchServicesHAProxySettingsEndpointResponse403
    | PatchServicesHAProxySettingsEndpointResponse404
    | PatchServicesHAProxySettingsEndpointResponse405
    | PatchServicesHAProxySettingsEndpointResponse406
    | PatchServicesHAProxySettingsEndpointResponse409
    | PatchServicesHAProxySettingsEndpointResponse415
    | PatchServicesHAProxySettingsEndpointResponse422
    | PatchServicesHAProxySettingsEndpointResponse424
    | PatchServicesHAProxySettingsEndpointResponse500
    | PatchServicesHAProxySettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current HAProxy Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxySettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxySettingsEndpointResponse400 | PatchServicesHAProxySettingsEndpointResponse401 | PatchServicesHAProxySettingsEndpointResponse403 | PatchServicesHAProxySettingsEndpointResponse404 | PatchServicesHAProxySettingsEndpointResponse405 | PatchServicesHAProxySettingsEndpointResponse406 | PatchServicesHAProxySettingsEndpointResponse409 | PatchServicesHAProxySettingsEndpointResponse415 | PatchServicesHAProxySettingsEndpointResponse422 | PatchServicesHAProxySettingsEndpointResponse424 | PatchServicesHAProxySettingsEndpointResponse500 | PatchServicesHAProxySettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
