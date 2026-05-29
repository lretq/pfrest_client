from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dns_resolver_host_override_alias_endpoint_data_body import (
    PostServicesDNSResolverHostOverrideAliasEndpointDataBody,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_json_body import (
    PostServicesDNSResolverHostOverrideAliasEndpointJsonBody,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_400 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_401 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse401,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_403 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse403,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_404 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse404,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_405 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse405,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_406 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse406,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_409 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse409,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_415 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse415,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_422 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse422,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_424 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse424,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_500 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse500,
)
from ...models.post_services_dns_resolver_host_override_alias_endpoint_response_503 import (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDNSResolverHostOverrideAliasEndpointJsonBody
    | PostServicesDNSResolverHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dns_resolver/host_override/alias",
    }

    if isinstance(body, PostServicesDNSResolverHostOverrideAliasEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDNSResolverHostOverrideAliasEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse401
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse403
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse404
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse405
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse406
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse409
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse415
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse422
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse424
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse500
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDNSResolverHostOverrideAliasEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDNSResolverHostOverrideAliasEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDNSResolverHostOverrideAliasEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDNSResolverHostOverrideAliasEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDNSResolverHostOverrideAliasEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDNSResolverHostOverrideAliasEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDNSResolverHostOverrideAliasEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDNSResolverHostOverrideAliasEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDNSResolverHostOverrideAliasEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDNSResolverHostOverrideAliasEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDNSResolverHostOverrideAliasEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDNSResolverHostOverrideAliasEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse401
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse403
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse404
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse405
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse406
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse409
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse415
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse422
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse424
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse500
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
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
    body: PostServicesDNSResolverHostOverrideAliasEndpointJsonBody
    | PostServicesDNSResolverHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse401
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse403
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse404
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse405
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse406
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse409
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse415
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse422
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse424
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse500
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Host Override Alias.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverrideAlias<br>**Parent model**:
    DNSResolverHostOverride<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    host-override-alias-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverHostOverrideAliasEndpointJsonBody | Unset):
        body (PostServicesDNSResolverHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverHostOverrideAliasEndpointResponse400 | PostServicesDNSResolverHostOverrideAliasEndpointResponse401 | PostServicesDNSResolverHostOverrideAliasEndpointResponse403 | PostServicesDNSResolverHostOverrideAliasEndpointResponse404 | PostServicesDNSResolverHostOverrideAliasEndpointResponse405 | PostServicesDNSResolverHostOverrideAliasEndpointResponse406 | PostServicesDNSResolverHostOverrideAliasEndpointResponse409 | PostServicesDNSResolverHostOverrideAliasEndpointResponse415 | PostServicesDNSResolverHostOverrideAliasEndpointResponse422 | PostServicesDNSResolverHostOverrideAliasEndpointResponse424 | PostServicesDNSResolverHostOverrideAliasEndpointResponse500 | PostServicesDNSResolverHostOverrideAliasEndpointResponse503]
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
    body: PostServicesDNSResolverHostOverrideAliasEndpointJsonBody
    | PostServicesDNSResolverHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse401
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse403
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse404
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse405
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse406
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse409
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse415
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse422
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse424
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse500
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Host Override Alias.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverrideAlias<br>**Parent model**:
    DNSResolverHostOverride<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    host-override-alias-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverHostOverrideAliasEndpointJsonBody | Unset):
        body (PostServicesDNSResolverHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverHostOverrideAliasEndpointResponse400 | PostServicesDNSResolverHostOverrideAliasEndpointResponse401 | PostServicesDNSResolverHostOverrideAliasEndpointResponse403 | PostServicesDNSResolverHostOverrideAliasEndpointResponse404 | PostServicesDNSResolverHostOverrideAliasEndpointResponse405 | PostServicesDNSResolverHostOverrideAliasEndpointResponse406 | PostServicesDNSResolverHostOverrideAliasEndpointResponse409 | PostServicesDNSResolverHostOverrideAliasEndpointResponse415 | PostServicesDNSResolverHostOverrideAliasEndpointResponse422 | PostServicesDNSResolverHostOverrideAliasEndpointResponse424 | PostServicesDNSResolverHostOverrideAliasEndpointResponse500 | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverHostOverrideAliasEndpointJsonBody
    | PostServicesDNSResolverHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse401
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse403
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse404
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse405
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse406
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse409
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse415
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse422
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse424
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse500
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Host Override Alias.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverrideAlias<br>**Parent model**:
    DNSResolverHostOverride<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    host-override-alias-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverHostOverrideAliasEndpointJsonBody | Unset):
        body (PostServicesDNSResolverHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverHostOverrideAliasEndpointResponse400 | PostServicesDNSResolverHostOverrideAliasEndpointResponse401 | PostServicesDNSResolverHostOverrideAliasEndpointResponse403 | PostServicesDNSResolverHostOverrideAliasEndpointResponse404 | PostServicesDNSResolverHostOverrideAliasEndpointResponse405 | PostServicesDNSResolverHostOverrideAliasEndpointResponse406 | PostServicesDNSResolverHostOverrideAliasEndpointResponse409 | PostServicesDNSResolverHostOverrideAliasEndpointResponse415 | PostServicesDNSResolverHostOverrideAliasEndpointResponse422 | PostServicesDNSResolverHostOverrideAliasEndpointResponse424 | PostServicesDNSResolverHostOverrideAliasEndpointResponse500 | PostServicesDNSResolverHostOverrideAliasEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverHostOverrideAliasEndpointJsonBody
    | PostServicesDNSResolverHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverHostOverrideAliasEndpointResponse400
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse401
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse403
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse404
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse405
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse406
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse409
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse415
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse422
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse424
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse500
    | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Host Override Alias.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverrideAlias<br>**Parent model**:
    DNSResolverHostOverride<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    host-override-alias-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverHostOverrideAliasEndpointJsonBody | Unset):
        body (PostServicesDNSResolverHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverHostOverrideAliasEndpointResponse400 | PostServicesDNSResolverHostOverrideAliasEndpointResponse401 | PostServicesDNSResolverHostOverrideAliasEndpointResponse403 | PostServicesDNSResolverHostOverrideAliasEndpointResponse404 | PostServicesDNSResolverHostOverrideAliasEndpointResponse405 | PostServicesDNSResolverHostOverrideAliasEndpointResponse406 | PostServicesDNSResolverHostOverrideAliasEndpointResponse409 | PostServicesDNSResolverHostOverrideAliasEndpointResponse415 | PostServicesDNSResolverHostOverrideAliasEndpointResponse422 | PostServicesDNSResolverHostOverrideAliasEndpointResponse424 | PostServicesDNSResolverHostOverrideAliasEndpointResponse500 | PostServicesDNSResolverHostOverrideAliasEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
