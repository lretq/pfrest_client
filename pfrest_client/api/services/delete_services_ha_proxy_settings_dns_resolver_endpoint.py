from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_400 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_401 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse401,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_403 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse403,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_404 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse404,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_405 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse405,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_406 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse406,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_409 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse409,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_415 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse415,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_422 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse422,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_424 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse424,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_500 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse500,
)
from ...models.delete_services_ha_proxy_settings_dns_resolver_endpoint_response_503 import (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/haproxy/settings/dns_resolver",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxySettingsDNSResolverEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxySettingsDNSResolverEndpointResponse400 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxySettingsDNSResolverEndpointResponse400 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxySettingsDNSResolverEndpointResponse400 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesHAProxySettingsDNSResolverEndpointResponse400
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500
    | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxySettingsDNSResolverEndpointResponse400 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse401 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse403 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse404 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse405 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse406 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse409 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse415 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse422 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse424 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse500 | DeleteServicesHAProxySettingsDNSResolverEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
