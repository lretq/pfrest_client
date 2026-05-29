from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_data_body import (
    PatchServicesHAProxySettingsDNSResolverEndpointDataBody,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_json_body import (
    PatchServicesHAProxySettingsDNSResolverEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_400 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_401 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse401,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_403 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse403,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_404 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse404,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_405 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse405,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_406 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse406,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_409 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse409,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_415 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse415,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_422 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse422,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_424 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse424,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_500 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse500,
)
from ...models.patch_services_ha_proxy_settings_dns_resolver_endpoint_response_503 import (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PatchServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/settings/dns_resolver",
    }

    if isinstance(body, PatchServicesHAProxySettingsDNSResolverEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxySettingsDNSResolverEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse401
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse403
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse404
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse405
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse406
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse409
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse415
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse422
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse424
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse500
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxySettingsDNSResolverEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxySettingsDNSResolverEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxySettingsDNSResolverEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxySettingsDNSResolverEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxySettingsDNSResolverEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxySettingsDNSResolverEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxySettingsDNSResolverEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxySettingsDNSResolverEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxySettingsDNSResolverEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxySettingsDNSResolverEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxySettingsDNSResolverEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxySettingsDNSResolverEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse401
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse403
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse404
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse405
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse406
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse409
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse415
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse422
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse424
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse500
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
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
    body: PatchServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PatchServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse401
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse403
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse404
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse405
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse406
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse409
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse415
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse422
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse424
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse500
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxySettingsDNSResolverEndpointResponse400 | PatchServicesHAProxySettingsDNSResolverEndpointResponse401 | PatchServicesHAProxySettingsDNSResolverEndpointResponse403 | PatchServicesHAProxySettingsDNSResolverEndpointResponse404 | PatchServicesHAProxySettingsDNSResolverEndpointResponse405 | PatchServicesHAProxySettingsDNSResolverEndpointResponse406 | PatchServicesHAProxySettingsDNSResolverEndpointResponse409 | PatchServicesHAProxySettingsDNSResolverEndpointResponse415 | PatchServicesHAProxySettingsDNSResolverEndpointResponse422 | PatchServicesHAProxySettingsDNSResolverEndpointResponse424 | PatchServicesHAProxySettingsDNSResolverEndpointResponse500 | PatchServicesHAProxySettingsDNSResolverEndpointResponse503]
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
    body: PatchServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PatchServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse401
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse403
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse404
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse405
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse406
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse409
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse415
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse422
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse424
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse500
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxySettingsDNSResolverEndpointResponse400 | PatchServicesHAProxySettingsDNSResolverEndpointResponse401 | PatchServicesHAProxySettingsDNSResolverEndpointResponse403 | PatchServicesHAProxySettingsDNSResolverEndpointResponse404 | PatchServicesHAProxySettingsDNSResolverEndpointResponse405 | PatchServicesHAProxySettingsDNSResolverEndpointResponse406 | PatchServicesHAProxySettingsDNSResolverEndpointResponse409 | PatchServicesHAProxySettingsDNSResolverEndpointResponse415 | PatchServicesHAProxySettingsDNSResolverEndpointResponse422 | PatchServicesHAProxySettingsDNSResolverEndpointResponse424 | PatchServicesHAProxySettingsDNSResolverEndpointResponse500 | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PatchServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse401
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse403
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse404
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse405
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse406
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse409
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse415
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse422
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse424
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse500
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxySettingsDNSResolverEndpointResponse400 | PatchServicesHAProxySettingsDNSResolverEndpointResponse401 | PatchServicesHAProxySettingsDNSResolverEndpointResponse403 | PatchServicesHAProxySettingsDNSResolverEndpointResponse404 | PatchServicesHAProxySettingsDNSResolverEndpointResponse405 | PatchServicesHAProxySettingsDNSResolverEndpointResponse406 | PatchServicesHAProxySettingsDNSResolverEndpointResponse409 | PatchServicesHAProxySettingsDNSResolverEndpointResponse415 | PatchServicesHAProxySettingsDNSResolverEndpointResponse422 | PatchServicesHAProxySettingsDNSResolverEndpointResponse424 | PatchServicesHAProxySettingsDNSResolverEndpointResponse500 | PatchServicesHAProxySettingsDNSResolverEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PatchServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxySettingsDNSResolverEndpointResponse400
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse401
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse403
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse404
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse405
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse406
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse409
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse415
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse422
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse424
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse500
    | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PatchServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxySettingsDNSResolverEndpointResponse400 | PatchServicesHAProxySettingsDNSResolverEndpointResponse401 | PatchServicesHAProxySettingsDNSResolverEndpointResponse403 | PatchServicesHAProxySettingsDNSResolverEndpointResponse404 | PatchServicesHAProxySettingsDNSResolverEndpointResponse405 | PatchServicesHAProxySettingsDNSResolverEndpointResponse406 | PatchServicesHAProxySettingsDNSResolverEndpointResponse409 | PatchServicesHAProxySettingsDNSResolverEndpointResponse415 | PatchServicesHAProxySettingsDNSResolverEndpointResponse422 | PatchServicesHAProxySettingsDNSResolverEndpointResponse424 | PatchServicesHAProxySettingsDNSResolverEndpointResponse500 | PatchServicesHAProxySettingsDNSResolverEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
