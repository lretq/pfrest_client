from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_data_body import (
    PostServicesHAProxySettingsDNSResolverEndpointDataBody,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_json_body import (
    PostServicesHAProxySettingsDNSResolverEndpointJsonBody,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_400 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse400,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_401 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse401,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_403 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse403,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_404 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse404,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_405 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse405,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_406 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse406,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_409 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse409,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_415 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse415,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_422 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse422,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_424 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse424,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_500 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse500,
)
from ...models.post_services_ha_proxy_settings_dns_resolver_endpoint_response_503 import (
    PostServicesHAProxySettingsDNSResolverEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PostServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/settings/dns_resolver",
    }

    if isinstance(body, PostServicesHAProxySettingsDNSResolverEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxySettingsDNSResolverEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxySettingsDNSResolverEndpointResponse400
    | PostServicesHAProxySettingsDNSResolverEndpointResponse401
    | PostServicesHAProxySettingsDNSResolverEndpointResponse403
    | PostServicesHAProxySettingsDNSResolverEndpointResponse404
    | PostServicesHAProxySettingsDNSResolverEndpointResponse405
    | PostServicesHAProxySettingsDNSResolverEndpointResponse406
    | PostServicesHAProxySettingsDNSResolverEndpointResponse409
    | PostServicesHAProxySettingsDNSResolverEndpointResponse415
    | PostServicesHAProxySettingsDNSResolverEndpointResponse422
    | PostServicesHAProxySettingsDNSResolverEndpointResponse424
    | PostServicesHAProxySettingsDNSResolverEndpointResponse500
    | PostServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxySettingsDNSResolverEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxySettingsDNSResolverEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxySettingsDNSResolverEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxySettingsDNSResolverEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxySettingsDNSResolverEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxySettingsDNSResolverEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxySettingsDNSResolverEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxySettingsDNSResolverEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxySettingsDNSResolverEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxySettingsDNSResolverEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxySettingsDNSResolverEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxySettingsDNSResolverEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxySettingsDNSResolverEndpointResponse400
    | PostServicesHAProxySettingsDNSResolverEndpointResponse401
    | PostServicesHAProxySettingsDNSResolverEndpointResponse403
    | PostServicesHAProxySettingsDNSResolverEndpointResponse404
    | PostServicesHAProxySettingsDNSResolverEndpointResponse405
    | PostServicesHAProxySettingsDNSResolverEndpointResponse406
    | PostServicesHAProxySettingsDNSResolverEndpointResponse409
    | PostServicesHAProxySettingsDNSResolverEndpointResponse415
    | PostServicesHAProxySettingsDNSResolverEndpointResponse422
    | PostServicesHAProxySettingsDNSResolverEndpointResponse424
    | PostServicesHAProxySettingsDNSResolverEndpointResponse500
    | PostServicesHAProxySettingsDNSResolverEndpointResponse503
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
    body: PostServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PostServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxySettingsDNSResolverEndpointResponse400
    | PostServicesHAProxySettingsDNSResolverEndpointResponse401
    | PostServicesHAProxySettingsDNSResolverEndpointResponse403
    | PostServicesHAProxySettingsDNSResolverEndpointResponse404
    | PostServicesHAProxySettingsDNSResolverEndpointResponse405
    | PostServicesHAProxySettingsDNSResolverEndpointResponse406
    | PostServicesHAProxySettingsDNSResolverEndpointResponse409
    | PostServicesHAProxySettingsDNSResolverEndpointResponse415
    | PostServicesHAProxySettingsDNSResolverEndpointResponse422
    | PostServicesHAProxySettingsDNSResolverEndpointResponse424
    | PostServicesHAProxySettingsDNSResolverEndpointResponse500
    | PostServicesHAProxySettingsDNSResolverEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxySettingsDNSResolverEndpointResponse400 | PostServicesHAProxySettingsDNSResolverEndpointResponse401 | PostServicesHAProxySettingsDNSResolverEndpointResponse403 | PostServicesHAProxySettingsDNSResolverEndpointResponse404 | PostServicesHAProxySettingsDNSResolverEndpointResponse405 | PostServicesHAProxySettingsDNSResolverEndpointResponse406 | PostServicesHAProxySettingsDNSResolverEndpointResponse409 | PostServicesHAProxySettingsDNSResolverEndpointResponse415 | PostServicesHAProxySettingsDNSResolverEndpointResponse422 | PostServicesHAProxySettingsDNSResolverEndpointResponse424 | PostServicesHAProxySettingsDNSResolverEndpointResponse500 | PostServicesHAProxySettingsDNSResolverEndpointResponse503]
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
    body: PostServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PostServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxySettingsDNSResolverEndpointResponse400
    | PostServicesHAProxySettingsDNSResolverEndpointResponse401
    | PostServicesHAProxySettingsDNSResolverEndpointResponse403
    | PostServicesHAProxySettingsDNSResolverEndpointResponse404
    | PostServicesHAProxySettingsDNSResolverEndpointResponse405
    | PostServicesHAProxySettingsDNSResolverEndpointResponse406
    | PostServicesHAProxySettingsDNSResolverEndpointResponse409
    | PostServicesHAProxySettingsDNSResolverEndpointResponse415
    | PostServicesHAProxySettingsDNSResolverEndpointResponse422
    | PostServicesHAProxySettingsDNSResolverEndpointResponse424
    | PostServicesHAProxySettingsDNSResolverEndpointResponse500
    | PostServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxySettingsDNSResolverEndpointResponse400 | PostServicesHAProxySettingsDNSResolverEndpointResponse401 | PostServicesHAProxySettingsDNSResolverEndpointResponse403 | PostServicesHAProxySettingsDNSResolverEndpointResponse404 | PostServicesHAProxySettingsDNSResolverEndpointResponse405 | PostServicesHAProxySettingsDNSResolverEndpointResponse406 | PostServicesHAProxySettingsDNSResolverEndpointResponse409 | PostServicesHAProxySettingsDNSResolverEndpointResponse415 | PostServicesHAProxySettingsDNSResolverEndpointResponse422 | PostServicesHAProxySettingsDNSResolverEndpointResponse424 | PostServicesHAProxySettingsDNSResolverEndpointResponse500 | PostServicesHAProxySettingsDNSResolverEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PostServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxySettingsDNSResolverEndpointResponse400
    | PostServicesHAProxySettingsDNSResolverEndpointResponse401
    | PostServicesHAProxySettingsDNSResolverEndpointResponse403
    | PostServicesHAProxySettingsDNSResolverEndpointResponse404
    | PostServicesHAProxySettingsDNSResolverEndpointResponse405
    | PostServicesHAProxySettingsDNSResolverEndpointResponse406
    | PostServicesHAProxySettingsDNSResolverEndpointResponse409
    | PostServicesHAProxySettingsDNSResolverEndpointResponse415
    | PostServicesHAProxySettingsDNSResolverEndpointResponse422
    | PostServicesHAProxySettingsDNSResolverEndpointResponse424
    | PostServicesHAProxySettingsDNSResolverEndpointResponse500
    | PostServicesHAProxySettingsDNSResolverEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxySettingsDNSResolverEndpointResponse400 | PostServicesHAProxySettingsDNSResolverEndpointResponse401 | PostServicesHAProxySettingsDNSResolverEndpointResponse403 | PostServicesHAProxySettingsDNSResolverEndpointResponse404 | PostServicesHAProxySettingsDNSResolverEndpointResponse405 | PostServicesHAProxySettingsDNSResolverEndpointResponse406 | PostServicesHAProxySettingsDNSResolverEndpointResponse409 | PostServicesHAProxySettingsDNSResolverEndpointResponse415 | PostServicesHAProxySettingsDNSResolverEndpointResponse422 | PostServicesHAProxySettingsDNSResolverEndpointResponse424 | PostServicesHAProxySettingsDNSResolverEndpointResponse500 | PostServicesHAProxySettingsDNSResolverEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxySettingsDNSResolverEndpointJsonBody
    | PostServicesHAProxySettingsDNSResolverEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxySettingsDNSResolverEndpointResponse400
    | PostServicesHAProxySettingsDNSResolverEndpointResponse401
    | PostServicesHAProxySettingsDNSResolverEndpointResponse403
    | PostServicesHAProxySettingsDNSResolverEndpointResponse404
    | PostServicesHAProxySettingsDNSResolverEndpointResponse405
    | PostServicesHAProxySettingsDNSResolverEndpointResponse406
    | PostServicesHAProxySettingsDNSResolverEndpointResponse409
    | PostServicesHAProxySettingsDNSResolverEndpointResponse415
    | PostServicesHAProxySettingsDNSResolverEndpointResponse422
    | PostServicesHAProxySettingsDNSResolverEndpointResponse424
    | PostServicesHAProxySettingsDNSResolverEndpointResponse500
    | PostServicesHAProxySettingsDNSResolverEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy DNS Resolver.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyDNSResolver<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-dns-resolver-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsDNSResolverEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsDNSResolverEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxySettingsDNSResolverEndpointResponse400 | PostServicesHAProxySettingsDNSResolverEndpointResponse401 | PostServicesHAProxySettingsDNSResolverEndpointResponse403 | PostServicesHAProxySettingsDNSResolverEndpointResponse404 | PostServicesHAProxySettingsDNSResolverEndpointResponse405 | PostServicesHAProxySettingsDNSResolverEndpointResponse406 | PostServicesHAProxySettingsDNSResolverEndpointResponse409 | PostServicesHAProxySettingsDNSResolverEndpointResponse415 | PostServicesHAProxySettingsDNSResolverEndpointResponse422 | PostServicesHAProxySettingsDNSResolverEndpointResponse424 | PostServicesHAProxySettingsDNSResolverEndpointResponse500 | PostServicesHAProxySettingsDNSResolverEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
