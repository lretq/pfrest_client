from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dns_resolver_access_list_endpoint_data_body import (
    PostServicesDNSResolverAccessListEndpointDataBody,
)
from ...models.post_services_dns_resolver_access_list_endpoint_json_body import (
    PostServicesDNSResolverAccessListEndpointJsonBody,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_400 import (
    PostServicesDNSResolverAccessListEndpointResponse400,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_401 import (
    PostServicesDNSResolverAccessListEndpointResponse401,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_403 import (
    PostServicesDNSResolverAccessListEndpointResponse403,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_404 import (
    PostServicesDNSResolverAccessListEndpointResponse404,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_405 import (
    PostServicesDNSResolverAccessListEndpointResponse405,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_406 import (
    PostServicesDNSResolverAccessListEndpointResponse406,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_409 import (
    PostServicesDNSResolverAccessListEndpointResponse409,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_415 import (
    PostServicesDNSResolverAccessListEndpointResponse415,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_422 import (
    PostServicesDNSResolverAccessListEndpointResponse422,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_424 import (
    PostServicesDNSResolverAccessListEndpointResponse424,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_500 import (
    PostServicesDNSResolverAccessListEndpointResponse500,
)
from ...models.post_services_dns_resolver_access_list_endpoint_response_503 import (
    PostServicesDNSResolverAccessListEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDNSResolverAccessListEndpointJsonBody
    | PostServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dns_resolver/access_list",
    }

    if isinstance(body, PostServicesDNSResolverAccessListEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDNSResolverAccessListEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDNSResolverAccessListEndpointResponse400
    | PostServicesDNSResolverAccessListEndpointResponse401
    | PostServicesDNSResolverAccessListEndpointResponse403
    | PostServicesDNSResolverAccessListEndpointResponse404
    | PostServicesDNSResolverAccessListEndpointResponse405
    | PostServicesDNSResolverAccessListEndpointResponse406
    | PostServicesDNSResolverAccessListEndpointResponse409
    | PostServicesDNSResolverAccessListEndpointResponse415
    | PostServicesDNSResolverAccessListEndpointResponse422
    | PostServicesDNSResolverAccessListEndpointResponse424
    | PostServicesDNSResolverAccessListEndpointResponse500
    | PostServicesDNSResolverAccessListEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDNSResolverAccessListEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDNSResolverAccessListEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDNSResolverAccessListEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDNSResolverAccessListEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDNSResolverAccessListEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDNSResolverAccessListEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDNSResolverAccessListEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDNSResolverAccessListEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDNSResolverAccessListEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDNSResolverAccessListEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDNSResolverAccessListEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDNSResolverAccessListEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDNSResolverAccessListEndpointResponse400
    | PostServicesDNSResolverAccessListEndpointResponse401
    | PostServicesDNSResolverAccessListEndpointResponse403
    | PostServicesDNSResolverAccessListEndpointResponse404
    | PostServicesDNSResolverAccessListEndpointResponse405
    | PostServicesDNSResolverAccessListEndpointResponse406
    | PostServicesDNSResolverAccessListEndpointResponse409
    | PostServicesDNSResolverAccessListEndpointResponse415
    | PostServicesDNSResolverAccessListEndpointResponse422
    | PostServicesDNSResolverAccessListEndpointResponse424
    | PostServicesDNSResolverAccessListEndpointResponse500
    | PostServicesDNSResolverAccessListEndpointResponse503
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
    body: PostServicesDNSResolverAccessListEndpointJsonBody
    | PostServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverAccessListEndpointResponse400
    | PostServicesDNSResolverAccessListEndpointResponse401
    | PostServicesDNSResolverAccessListEndpointResponse403
    | PostServicesDNSResolverAccessListEndpointResponse404
    | PostServicesDNSResolverAccessListEndpointResponse405
    | PostServicesDNSResolverAccessListEndpointResponse406
    | PostServicesDNSResolverAccessListEndpointResponse409
    | PostServicesDNSResolverAccessListEndpointResponse415
    | PostServicesDNSResolverAccessListEndpointResponse422
    | PostServicesDNSResolverAccessListEndpointResponse424
    | PostServicesDNSResolverAccessListEndpointResponse500
    | PostServicesDNSResolverAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverAccessListEndpointResponse400 | PostServicesDNSResolverAccessListEndpointResponse401 | PostServicesDNSResolverAccessListEndpointResponse403 | PostServicesDNSResolverAccessListEndpointResponse404 | PostServicesDNSResolverAccessListEndpointResponse405 | PostServicesDNSResolverAccessListEndpointResponse406 | PostServicesDNSResolverAccessListEndpointResponse409 | PostServicesDNSResolverAccessListEndpointResponse415 | PostServicesDNSResolverAccessListEndpointResponse422 | PostServicesDNSResolverAccessListEndpointResponse424 | PostServicesDNSResolverAccessListEndpointResponse500 | PostServicesDNSResolverAccessListEndpointResponse503]
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
    body: PostServicesDNSResolverAccessListEndpointJsonBody
    | PostServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverAccessListEndpointResponse400
    | PostServicesDNSResolverAccessListEndpointResponse401
    | PostServicesDNSResolverAccessListEndpointResponse403
    | PostServicesDNSResolverAccessListEndpointResponse404
    | PostServicesDNSResolverAccessListEndpointResponse405
    | PostServicesDNSResolverAccessListEndpointResponse406
    | PostServicesDNSResolverAccessListEndpointResponse409
    | PostServicesDNSResolverAccessListEndpointResponse415
    | PostServicesDNSResolverAccessListEndpointResponse422
    | PostServicesDNSResolverAccessListEndpointResponse424
    | PostServicesDNSResolverAccessListEndpointResponse500
    | PostServicesDNSResolverAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverAccessListEndpointResponse400 | PostServicesDNSResolverAccessListEndpointResponse401 | PostServicesDNSResolverAccessListEndpointResponse403 | PostServicesDNSResolverAccessListEndpointResponse404 | PostServicesDNSResolverAccessListEndpointResponse405 | PostServicesDNSResolverAccessListEndpointResponse406 | PostServicesDNSResolverAccessListEndpointResponse409 | PostServicesDNSResolverAccessListEndpointResponse415 | PostServicesDNSResolverAccessListEndpointResponse422 | PostServicesDNSResolverAccessListEndpointResponse424 | PostServicesDNSResolverAccessListEndpointResponse500 | PostServicesDNSResolverAccessListEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverAccessListEndpointJsonBody
    | PostServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverAccessListEndpointResponse400
    | PostServicesDNSResolverAccessListEndpointResponse401
    | PostServicesDNSResolverAccessListEndpointResponse403
    | PostServicesDNSResolverAccessListEndpointResponse404
    | PostServicesDNSResolverAccessListEndpointResponse405
    | PostServicesDNSResolverAccessListEndpointResponse406
    | PostServicesDNSResolverAccessListEndpointResponse409
    | PostServicesDNSResolverAccessListEndpointResponse415
    | PostServicesDNSResolverAccessListEndpointResponse422
    | PostServicesDNSResolverAccessListEndpointResponse424
    | PostServicesDNSResolverAccessListEndpointResponse500
    | PostServicesDNSResolverAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverAccessListEndpointResponse400 | PostServicesDNSResolverAccessListEndpointResponse401 | PostServicesDNSResolverAccessListEndpointResponse403 | PostServicesDNSResolverAccessListEndpointResponse404 | PostServicesDNSResolverAccessListEndpointResponse405 | PostServicesDNSResolverAccessListEndpointResponse406 | PostServicesDNSResolverAccessListEndpointResponse409 | PostServicesDNSResolverAccessListEndpointResponse415 | PostServicesDNSResolverAccessListEndpointResponse422 | PostServicesDNSResolverAccessListEndpointResponse424 | PostServicesDNSResolverAccessListEndpointResponse500 | PostServicesDNSResolverAccessListEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverAccessListEndpointJsonBody
    | PostServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSResolverAccessListEndpointResponse400
    | PostServicesDNSResolverAccessListEndpointResponse401
    | PostServicesDNSResolverAccessListEndpointResponse403
    | PostServicesDNSResolverAccessListEndpointResponse404
    | PostServicesDNSResolverAccessListEndpointResponse405
    | PostServicesDNSResolverAccessListEndpointResponse406
    | PostServicesDNSResolverAccessListEndpointResponse409
    | PostServicesDNSResolverAccessListEndpointResponse415
    | PostServicesDNSResolverAccessListEndpointResponse422
    | PostServicesDNSResolverAccessListEndpointResponse424
    | PostServicesDNSResolverAccessListEndpointResponse500
    | PostServicesDNSResolverAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PostServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverAccessListEndpointResponse400 | PostServicesDNSResolverAccessListEndpointResponse401 | PostServicesDNSResolverAccessListEndpointResponse403 | PostServicesDNSResolverAccessListEndpointResponse404 | PostServicesDNSResolverAccessListEndpointResponse405 | PostServicesDNSResolverAccessListEndpointResponse406 | PostServicesDNSResolverAccessListEndpointResponse409 | PostServicesDNSResolverAccessListEndpointResponse415 | PostServicesDNSResolverAccessListEndpointResponse422 | PostServicesDNSResolverAccessListEndpointResponse424 | PostServicesDNSResolverAccessListEndpointResponse500 | PostServicesDNSResolverAccessListEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
