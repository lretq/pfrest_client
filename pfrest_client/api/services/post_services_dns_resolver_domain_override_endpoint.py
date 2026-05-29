from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dns_resolver_domain_override_endpoint_data_body import (
    PostServicesDNSResolverDomainOverrideEndpointDataBody,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_json_body import (
    PostServicesDNSResolverDomainOverrideEndpointJsonBody,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_400 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse400,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_401 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse401,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_403 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse403,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_404 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse404,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_405 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse405,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_406 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse406,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_409 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse409,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_415 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse415,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_422 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse422,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_424 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse424,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_500 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse500,
)
from ...models.post_services_dns_resolver_domain_override_endpoint_response_503 import (
    PostServicesDNSResolverDomainOverrideEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDNSResolverDomainOverrideEndpointJsonBody
    | PostServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dns_resolver/domain_override",
    }

    if isinstance(body, PostServicesDNSResolverDomainOverrideEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDNSResolverDomainOverrideEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDNSResolverDomainOverrideEndpointResponse400
    | PostServicesDNSResolverDomainOverrideEndpointResponse401
    | PostServicesDNSResolverDomainOverrideEndpointResponse403
    | PostServicesDNSResolverDomainOverrideEndpointResponse404
    | PostServicesDNSResolverDomainOverrideEndpointResponse405
    | PostServicesDNSResolverDomainOverrideEndpointResponse406
    | PostServicesDNSResolverDomainOverrideEndpointResponse409
    | PostServicesDNSResolverDomainOverrideEndpointResponse415
    | PostServicesDNSResolverDomainOverrideEndpointResponse422
    | PostServicesDNSResolverDomainOverrideEndpointResponse424
    | PostServicesDNSResolverDomainOverrideEndpointResponse500
    | PostServicesDNSResolverDomainOverrideEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDNSResolverDomainOverrideEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDNSResolverDomainOverrideEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDNSResolverDomainOverrideEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDNSResolverDomainOverrideEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDNSResolverDomainOverrideEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDNSResolverDomainOverrideEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDNSResolverDomainOverrideEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDNSResolverDomainOverrideEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDNSResolverDomainOverrideEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDNSResolverDomainOverrideEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDNSResolverDomainOverrideEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDNSResolverDomainOverrideEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDNSResolverDomainOverrideEndpointResponse400
    | PostServicesDNSResolverDomainOverrideEndpointResponse401
    | PostServicesDNSResolverDomainOverrideEndpointResponse403
    | PostServicesDNSResolverDomainOverrideEndpointResponse404
    | PostServicesDNSResolverDomainOverrideEndpointResponse405
    | PostServicesDNSResolverDomainOverrideEndpointResponse406
    | PostServicesDNSResolverDomainOverrideEndpointResponse409
    | PostServicesDNSResolverDomainOverrideEndpointResponse415
    | PostServicesDNSResolverDomainOverrideEndpointResponse422
    | PostServicesDNSResolverDomainOverrideEndpointResponse424
    | PostServicesDNSResolverDomainOverrideEndpointResponse500
    | PostServicesDNSResolverDomainOverrideEndpointResponse503
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
    body: PostServicesDNSResolverDomainOverrideEndpointJsonBody
    | PostServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverDomainOverrideEndpointResponse400
    | PostServicesDNSResolverDomainOverrideEndpointResponse401
    | PostServicesDNSResolverDomainOverrideEndpointResponse403
    | PostServicesDNSResolverDomainOverrideEndpointResponse404
    | PostServicesDNSResolverDomainOverrideEndpointResponse405
    | PostServicesDNSResolverDomainOverrideEndpointResponse406
    | PostServicesDNSResolverDomainOverrideEndpointResponse409
    | PostServicesDNSResolverDomainOverrideEndpointResponse415
    | PostServicesDNSResolverDomainOverrideEndpointResponse422
    | PostServicesDNSResolverDomainOverrideEndpointResponse424
    | PostServicesDNSResolverDomainOverrideEndpointResponse500
    | PostServicesDNSResolverDomainOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Domain Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverDomainOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-domain-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverDomainOverrideEndpointResponse400 | PostServicesDNSResolverDomainOverrideEndpointResponse401 | PostServicesDNSResolverDomainOverrideEndpointResponse403 | PostServicesDNSResolverDomainOverrideEndpointResponse404 | PostServicesDNSResolverDomainOverrideEndpointResponse405 | PostServicesDNSResolverDomainOverrideEndpointResponse406 | PostServicesDNSResolverDomainOverrideEndpointResponse409 | PostServicesDNSResolverDomainOverrideEndpointResponse415 | PostServicesDNSResolverDomainOverrideEndpointResponse422 | PostServicesDNSResolverDomainOverrideEndpointResponse424 | PostServicesDNSResolverDomainOverrideEndpointResponse500 | PostServicesDNSResolverDomainOverrideEndpointResponse503]
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
    body: PostServicesDNSResolverDomainOverrideEndpointJsonBody
    | PostServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverDomainOverrideEndpointResponse400
    | PostServicesDNSResolverDomainOverrideEndpointResponse401
    | PostServicesDNSResolverDomainOverrideEndpointResponse403
    | PostServicesDNSResolverDomainOverrideEndpointResponse404
    | PostServicesDNSResolverDomainOverrideEndpointResponse405
    | PostServicesDNSResolverDomainOverrideEndpointResponse406
    | PostServicesDNSResolverDomainOverrideEndpointResponse409
    | PostServicesDNSResolverDomainOverrideEndpointResponse415
    | PostServicesDNSResolverDomainOverrideEndpointResponse422
    | PostServicesDNSResolverDomainOverrideEndpointResponse424
    | PostServicesDNSResolverDomainOverrideEndpointResponse500
    | PostServicesDNSResolverDomainOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Domain Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverDomainOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-domain-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverDomainOverrideEndpointResponse400 | PostServicesDNSResolverDomainOverrideEndpointResponse401 | PostServicesDNSResolverDomainOverrideEndpointResponse403 | PostServicesDNSResolverDomainOverrideEndpointResponse404 | PostServicesDNSResolverDomainOverrideEndpointResponse405 | PostServicesDNSResolverDomainOverrideEndpointResponse406 | PostServicesDNSResolverDomainOverrideEndpointResponse409 | PostServicesDNSResolverDomainOverrideEndpointResponse415 | PostServicesDNSResolverDomainOverrideEndpointResponse422 | PostServicesDNSResolverDomainOverrideEndpointResponse424 | PostServicesDNSResolverDomainOverrideEndpointResponse500 | PostServicesDNSResolverDomainOverrideEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverDomainOverrideEndpointJsonBody
    | PostServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverDomainOverrideEndpointResponse400
    | PostServicesDNSResolverDomainOverrideEndpointResponse401
    | PostServicesDNSResolverDomainOverrideEndpointResponse403
    | PostServicesDNSResolverDomainOverrideEndpointResponse404
    | PostServicesDNSResolverDomainOverrideEndpointResponse405
    | PostServicesDNSResolverDomainOverrideEndpointResponse406
    | PostServicesDNSResolverDomainOverrideEndpointResponse409
    | PostServicesDNSResolverDomainOverrideEndpointResponse415
    | PostServicesDNSResolverDomainOverrideEndpointResponse422
    | PostServicesDNSResolverDomainOverrideEndpointResponse424
    | PostServicesDNSResolverDomainOverrideEndpointResponse500
    | PostServicesDNSResolverDomainOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Domain Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverDomainOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-domain-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverDomainOverrideEndpointResponse400 | PostServicesDNSResolverDomainOverrideEndpointResponse401 | PostServicesDNSResolverDomainOverrideEndpointResponse403 | PostServicesDNSResolverDomainOverrideEndpointResponse404 | PostServicesDNSResolverDomainOverrideEndpointResponse405 | PostServicesDNSResolverDomainOverrideEndpointResponse406 | PostServicesDNSResolverDomainOverrideEndpointResponse409 | PostServicesDNSResolverDomainOverrideEndpointResponse415 | PostServicesDNSResolverDomainOverrideEndpointResponse422 | PostServicesDNSResolverDomainOverrideEndpointResponse424 | PostServicesDNSResolverDomainOverrideEndpointResponse500 | PostServicesDNSResolverDomainOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverDomainOverrideEndpointJsonBody
    | PostServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverDomainOverrideEndpointResponse400
    | PostServicesDNSResolverDomainOverrideEndpointResponse401
    | PostServicesDNSResolverDomainOverrideEndpointResponse403
    | PostServicesDNSResolverDomainOverrideEndpointResponse404
    | PostServicesDNSResolverDomainOverrideEndpointResponse405
    | PostServicesDNSResolverDomainOverrideEndpointResponse406
    | PostServicesDNSResolverDomainOverrideEndpointResponse409
    | PostServicesDNSResolverDomainOverrideEndpointResponse415
    | PostServicesDNSResolverDomainOverrideEndpointResponse422
    | PostServicesDNSResolverDomainOverrideEndpointResponse424
    | PostServicesDNSResolverDomainOverrideEndpointResponse500
    | PostServicesDNSResolverDomainOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Domain Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverDomainOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-domain-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverDomainOverrideEndpointResponse400 | PostServicesDNSResolverDomainOverrideEndpointResponse401 | PostServicesDNSResolverDomainOverrideEndpointResponse403 | PostServicesDNSResolverDomainOverrideEndpointResponse404 | PostServicesDNSResolverDomainOverrideEndpointResponse405 | PostServicesDNSResolverDomainOverrideEndpointResponse406 | PostServicesDNSResolverDomainOverrideEndpointResponse409 | PostServicesDNSResolverDomainOverrideEndpointResponse415 | PostServicesDNSResolverDomainOverrideEndpointResponse422 | PostServicesDNSResolverDomainOverrideEndpointResponse424 | PostServicesDNSResolverDomainOverrideEndpointResponse500 | PostServicesDNSResolverDomainOverrideEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
