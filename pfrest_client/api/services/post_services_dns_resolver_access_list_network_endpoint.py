from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dns_resolver_access_list_network_endpoint_data_body import (
    PostServicesDNSResolverAccessListNetworkEndpointDataBody,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_json_body import (
    PostServicesDNSResolverAccessListNetworkEndpointJsonBody,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_400 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse400,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_401 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse401,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_403 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse403,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_404 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse404,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_405 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse405,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_406 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse406,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_409 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse409,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_415 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse415,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_422 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse422,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_424 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse424,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_500 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse500,
)
from ...models.post_services_dns_resolver_access_list_network_endpoint_response_503 import (
    PostServicesDNSResolverAccessListNetworkEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PostServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dns_resolver/access_list/network",
    }

    if isinstance(body, PostServicesDNSResolverAccessListNetworkEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDNSResolverAccessListNetworkEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDNSResolverAccessListNetworkEndpointResponse400
    | PostServicesDNSResolverAccessListNetworkEndpointResponse401
    | PostServicesDNSResolverAccessListNetworkEndpointResponse403
    | PostServicesDNSResolverAccessListNetworkEndpointResponse404
    | PostServicesDNSResolverAccessListNetworkEndpointResponse405
    | PostServicesDNSResolverAccessListNetworkEndpointResponse406
    | PostServicesDNSResolverAccessListNetworkEndpointResponse409
    | PostServicesDNSResolverAccessListNetworkEndpointResponse415
    | PostServicesDNSResolverAccessListNetworkEndpointResponse422
    | PostServicesDNSResolverAccessListNetworkEndpointResponse424
    | PostServicesDNSResolverAccessListNetworkEndpointResponse500
    | PostServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDNSResolverAccessListNetworkEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDNSResolverAccessListNetworkEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDNSResolverAccessListNetworkEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDNSResolverAccessListNetworkEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDNSResolverAccessListNetworkEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDNSResolverAccessListNetworkEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDNSResolverAccessListNetworkEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDNSResolverAccessListNetworkEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDNSResolverAccessListNetworkEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDNSResolverAccessListNetworkEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDNSResolverAccessListNetworkEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDNSResolverAccessListNetworkEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDNSResolverAccessListNetworkEndpointResponse400
    | PostServicesDNSResolverAccessListNetworkEndpointResponse401
    | PostServicesDNSResolverAccessListNetworkEndpointResponse403
    | PostServicesDNSResolverAccessListNetworkEndpointResponse404
    | PostServicesDNSResolverAccessListNetworkEndpointResponse405
    | PostServicesDNSResolverAccessListNetworkEndpointResponse406
    | PostServicesDNSResolverAccessListNetworkEndpointResponse409
    | PostServicesDNSResolverAccessListNetworkEndpointResponse415
    | PostServicesDNSResolverAccessListNetworkEndpointResponse422
    | PostServicesDNSResolverAccessListNetworkEndpointResponse424
    | PostServicesDNSResolverAccessListNetworkEndpointResponse500
    | PostServicesDNSResolverAccessListNetworkEndpointResponse503
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
    body: PostServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PostServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverAccessListNetworkEndpointResponse400
    | PostServicesDNSResolverAccessListNetworkEndpointResponse401
    | PostServicesDNSResolverAccessListNetworkEndpointResponse403
    | PostServicesDNSResolverAccessListNetworkEndpointResponse404
    | PostServicesDNSResolverAccessListNetworkEndpointResponse405
    | PostServicesDNSResolverAccessListNetworkEndpointResponse406
    | PostServicesDNSResolverAccessListNetworkEndpointResponse409
    | PostServicesDNSResolverAccessListNetworkEndpointResponse415
    | PostServicesDNSResolverAccessListNetworkEndpointResponse422
    | PostServicesDNSResolverAccessListNetworkEndpointResponse424
    | PostServicesDNSResolverAccessListNetworkEndpointResponse500
    | PostServicesDNSResolverAccessListNetworkEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Access List Network.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessListNetwork<br>**Parent model**:
    DNSResolverAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    access-list-network-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverAccessListNetworkEndpointResponse400 | PostServicesDNSResolverAccessListNetworkEndpointResponse401 | PostServicesDNSResolverAccessListNetworkEndpointResponse403 | PostServicesDNSResolverAccessListNetworkEndpointResponse404 | PostServicesDNSResolverAccessListNetworkEndpointResponse405 | PostServicesDNSResolverAccessListNetworkEndpointResponse406 | PostServicesDNSResolverAccessListNetworkEndpointResponse409 | PostServicesDNSResolverAccessListNetworkEndpointResponse415 | PostServicesDNSResolverAccessListNetworkEndpointResponse422 | PostServicesDNSResolverAccessListNetworkEndpointResponse424 | PostServicesDNSResolverAccessListNetworkEndpointResponse500 | PostServicesDNSResolverAccessListNetworkEndpointResponse503]
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
    body: PostServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PostServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverAccessListNetworkEndpointResponse400
    | PostServicesDNSResolverAccessListNetworkEndpointResponse401
    | PostServicesDNSResolverAccessListNetworkEndpointResponse403
    | PostServicesDNSResolverAccessListNetworkEndpointResponse404
    | PostServicesDNSResolverAccessListNetworkEndpointResponse405
    | PostServicesDNSResolverAccessListNetworkEndpointResponse406
    | PostServicesDNSResolverAccessListNetworkEndpointResponse409
    | PostServicesDNSResolverAccessListNetworkEndpointResponse415
    | PostServicesDNSResolverAccessListNetworkEndpointResponse422
    | PostServicesDNSResolverAccessListNetworkEndpointResponse424
    | PostServicesDNSResolverAccessListNetworkEndpointResponse500
    | PostServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Access List Network.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessListNetwork<br>**Parent model**:
    DNSResolverAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    access-list-network-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverAccessListNetworkEndpointResponse400 | PostServicesDNSResolverAccessListNetworkEndpointResponse401 | PostServicesDNSResolverAccessListNetworkEndpointResponse403 | PostServicesDNSResolverAccessListNetworkEndpointResponse404 | PostServicesDNSResolverAccessListNetworkEndpointResponse405 | PostServicesDNSResolverAccessListNetworkEndpointResponse406 | PostServicesDNSResolverAccessListNetworkEndpointResponse409 | PostServicesDNSResolverAccessListNetworkEndpointResponse415 | PostServicesDNSResolverAccessListNetworkEndpointResponse422 | PostServicesDNSResolverAccessListNetworkEndpointResponse424 | PostServicesDNSResolverAccessListNetworkEndpointResponse500 | PostServicesDNSResolverAccessListNetworkEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PostServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverAccessListNetworkEndpointResponse400
    | PostServicesDNSResolverAccessListNetworkEndpointResponse401
    | PostServicesDNSResolverAccessListNetworkEndpointResponse403
    | PostServicesDNSResolverAccessListNetworkEndpointResponse404
    | PostServicesDNSResolverAccessListNetworkEndpointResponse405
    | PostServicesDNSResolverAccessListNetworkEndpointResponse406
    | PostServicesDNSResolverAccessListNetworkEndpointResponse409
    | PostServicesDNSResolverAccessListNetworkEndpointResponse415
    | PostServicesDNSResolverAccessListNetworkEndpointResponse422
    | PostServicesDNSResolverAccessListNetworkEndpointResponse424
    | PostServicesDNSResolverAccessListNetworkEndpointResponse500
    | PostServicesDNSResolverAccessListNetworkEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Access List Network.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessListNetwork<br>**Parent model**:
    DNSResolverAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    access-list-network-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverAccessListNetworkEndpointResponse400 | PostServicesDNSResolverAccessListNetworkEndpointResponse401 | PostServicesDNSResolverAccessListNetworkEndpointResponse403 | PostServicesDNSResolverAccessListNetworkEndpointResponse404 | PostServicesDNSResolverAccessListNetworkEndpointResponse405 | PostServicesDNSResolverAccessListNetworkEndpointResponse406 | PostServicesDNSResolverAccessListNetworkEndpointResponse409 | PostServicesDNSResolverAccessListNetworkEndpointResponse415 | PostServicesDNSResolverAccessListNetworkEndpointResponse422 | PostServicesDNSResolverAccessListNetworkEndpointResponse424 | PostServicesDNSResolverAccessListNetworkEndpointResponse500 | PostServicesDNSResolverAccessListNetworkEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PostServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverAccessListNetworkEndpointResponse400
    | PostServicesDNSResolverAccessListNetworkEndpointResponse401
    | PostServicesDNSResolverAccessListNetworkEndpointResponse403
    | PostServicesDNSResolverAccessListNetworkEndpointResponse404
    | PostServicesDNSResolverAccessListNetworkEndpointResponse405
    | PostServicesDNSResolverAccessListNetworkEndpointResponse406
    | PostServicesDNSResolverAccessListNetworkEndpointResponse409
    | PostServicesDNSResolverAccessListNetworkEndpointResponse415
    | PostServicesDNSResolverAccessListNetworkEndpointResponse422
    | PostServicesDNSResolverAccessListNetworkEndpointResponse424
    | PostServicesDNSResolverAccessListNetworkEndpointResponse500
    | PostServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Access List Network.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessListNetwork<br>**Parent model**:
    DNSResolverAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-
    access-list-network-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverAccessListNetworkEndpointResponse400 | PostServicesDNSResolverAccessListNetworkEndpointResponse401 | PostServicesDNSResolverAccessListNetworkEndpointResponse403 | PostServicesDNSResolverAccessListNetworkEndpointResponse404 | PostServicesDNSResolverAccessListNetworkEndpointResponse405 | PostServicesDNSResolverAccessListNetworkEndpointResponse406 | PostServicesDNSResolverAccessListNetworkEndpointResponse409 | PostServicesDNSResolverAccessListNetworkEndpointResponse415 | PostServicesDNSResolverAccessListNetworkEndpointResponse422 | PostServicesDNSResolverAccessListNetworkEndpointResponse424 | PostServicesDNSResolverAccessListNetworkEndpointResponse500 | PostServicesDNSResolverAccessListNetworkEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
