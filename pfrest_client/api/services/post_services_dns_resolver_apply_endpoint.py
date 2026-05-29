from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dns_resolver_apply_endpoint_data_body import PostServicesDNSResolverApplyEndpointDataBody
from ...models.post_services_dns_resolver_apply_endpoint_json_body import PostServicesDNSResolverApplyEndpointJsonBody
from ...models.post_services_dns_resolver_apply_endpoint_response_400 import (
    PostServicesDNSResolverApplyEndpointResponse400,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_401 import (
    PostServicesDNSResolverApplyEndpointResponse401,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_403 import (
    PostServicesDNSResolverApplyEndpointResponse403,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_404 import (
    PostServicesDNSResolverApplyEndpointResponse404,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_405 import (
    PostServicesDNSResolverApplyEndpointResponse405,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_406 import (
    PostServicesDNSResolverApplyEndpointResponse406,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_409 import (
    PostServicesDNSResolverApplyEndpointResponse409,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_415 import (
    PostServicesDNSResolverApplyEndpointResponse415,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_422 import (
    PostServicesDNSResolverApplyEndpointResponse422,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_424 import (
    PostServicesDNSResolverApplyEndpointResponse424,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_500 import (
    PostServicesDNSResolverApplyEndpointResponse500,
)
from ...models.post_services_dns_resolver_apply_endpoint_response_503 import (
    PostServicesDNSResolverApplyEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDNSResolverApplyEndpointJsonBody | PostServicesDNSResolverApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dns_resolver/apply",
    }

    if isinstance(body, PostServicesDNSResolverApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDNSResolverApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDNSResolverApplyEndpointResponse400
    | PostServicesDNSResolverApplyEndpointResponse401
    | PostServicesDNSResolverApplyEndpointResponse403
    | PostServicesDNSResolverApplyEndpointResponse404
    | PostServicesDNSResolverApplyEndpointResponse405
    | PostServicesDNSResolverApplyEndpointResponse406
    | PostServicesDNSResolverApplyEndpointResponse409
    | PostServicesDNSResolverApplyEndpointResponse415
    | PostServicesDNSResolverApplyEndpointResponse422
    | PostServicesDNSResolverApplyEndpointResponse424
    | PostServicesDNSResolverApplyEndpointResponse500
    | PostServicesDNSResolverApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDNSResolverApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDNSResolverApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDNSResolverApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDNSResolverApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDNSResolverApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDNSResolverApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDNSResolverApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDNSResolverApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDNSResolverApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDNSResolverApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDNSResolverApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDNSResolverApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDNSResolverApplyEndpointResponse400
    | PostServicesDNSResolverApplyEndpointResponse401
    | PostServicesDNSResolverApplyEndpointResponse403
    | PostServicesDNSResolverApplyEndpointResponse404
    | PostServicesDNSResolverApplyEndpointResponse405
    | PostServicesDNSResolverApplyEndpointResponse406
    | PostServicesDNSResolverApplyEndpointResponse409
    | PostServicesDNSResolverApplyEndpointResponse415
    | PostServicesDNSResolverApplyEndpointResponse422
    | PostServicesDNSResolverApplyEndpointResponse424
    | PostServicesDNSResolverApplyEndpointResponse500
    | PostServicesDNSResolverApplyEndpointResponse503
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
    body: PostServicesDNSResolverApplyEndpointJsonBody | PostServicesDNSResolverApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverApplyEndpointResponse400
    | PostServicesDNSResolverApplyEndpointResponse401
    | PostServicesDNSResolverApplyEndpointResponse403
    | PostServicesDNSResolverApplyEndpointResponse404
    | PostServicesDNSResolverApplyEndpointResponse405
    | PostServicesDNSResolverApplyEndpointResponse406
    | PostServicesDNSResolverApplyEndpointResponse409
    | PostServicesDNSResolverApplyEndpointResponse415
    | PostServicesDNSResolverApplyEndpointResponse422
    | PostServicesDNSResolverApplyEndpointResponse424
    | PostServicesDNSResolverApplyEndpointResponse500
    | PostServicesDNSResolverApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending DNS Resolver changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverApplyEndpointJsonBody | Unset):
        body (PostServicesDNSResolverApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverApplyEndpointResponse400 | PostServicesDNSResolverApplyEndpointResponse401 | PostServicesDNSResolverApplyEndpointResponse403 | PostServicesDNSResolverApplyEndpointResponse404 | PostServicesDNSResolverApplyEndpointResponse405 | PostServicesDNSResolverApplyEndpointResponse406 | PostServicesDNSResolverApplyEndpointResponse409 | PostServicesDNSResolverApplyEndpointResponse415 | PostServicesDNSResolverApplyEndpointResponse422 | PostServicesDNSResolverApplyEndpointResponse424 | PostServicesDNSResolverApplyEndpointResponse500 | PostServicesDNSResolverApplyEndpointResponse503]
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
    body: PostServicesDNSResolverApplyEndpointJsonBody | PostServicesDNSResolverApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesDNSResolverApplyEndpointResponse400
    | PostServicesDNSResolverApplyEndpointResponse401
    | PostServicesDNSResolverApplyEndpointResponse403
    | PostServicesDNSResolverApplyEndpointResponse404
    | PostServicesDNSResolverApplyEndpointResponse405
    | PostServicesDNSResolverApplyEndpointResponse406
    | PostServicesDNSResolverApplyEndpointResponse409
    | PostServicesDNSResolverApplyEndpointResponse415
    | PostServicesDNSResolverApplyEndpointResponse422
    | PostServicesDNSResolverApplyEndpointResponse424
    | PostServicesDNSResolverApplyEndpointResponse500
    | PostServicesDNSResolverApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending DNS Resolver changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverApplyEndpointJsonBody | Unset):
        body (PostServicesDNSResolverApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverApplyEndpointResponse400 | PostServicesDNSResolverApplyEndpointResponse401 | PostServicesDNSResolverApplyEndpointResponse403 | PostServicesDNSResolverApplyEndpointResponse404 | PostServicesDNSResolverApplyEndpointResponse405 | PostServicesDNSResolverApplyEndpointResponse406 | PostServicesDNSResolverApplyEndpointResponse409 | PostServicesDNSResolverApplyEndpointResponse415 | PostServicesDNSResolverApplyEndpointResponse422 | PostServicesDNSResolverApplyEndpointResponse424 | PostServicesDNSResolverApplyEndpointResponse500 | PostServicesDNSResolverApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverApplyEndpointJsonBody | PostServicesDNSResolverApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesDNSResolverApplyEndpointResponse400
    | PostServicesDNSResolverApplyEndpointResponse401
    | PostServicesDNSResolverApplyEndpointResponse403
    | PostServicesDNSResolverApplyEndpointResponse404
    | PostServicesDNSResolverApplyEndpointResponse405
    | PostServicesDNSResolverApplyEndpointResponse406
    | PostServicesDNSResolverApplyEndpointResponse409
    | PostServicesDNSResolverApplyEndpointResponse415
    | PostServicesDNSResolverApplyEndpointResponse422
    | PostServicesDNSResolverApplyEndpointResponse424
    | PostServicesDNSResolverApplyEndpointResponse500
    | PostServicesDNSResolverApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending DNS Resolver changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverApplyEndpointJsonBody | Unset):
        body (PostServicesDNSResolverApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSResolverApplyEndpointResponse400 | PostServicesDNSResolverApplyEndpointResponse401 | PostServicesDNSResolverApplyEndpointResponse403 | PostServicesDNSResolverApplyEndpointResponse404 | PostServicesDNSResolverApplyEndpointResponse405 | PostServicesDNSResolverApplyEndpointResponse406 | PostServicesDNSResolverApplyEndpointResponse409 | PostServicesDNSResolverApplyEndpointResponse415 | PostServicesDNSResolverApplyEndpointResponse422 | PostServicesDNSResolverApplyEndpointResponse424 | PostServicesDNSResolverApplyEndpointResponse500 | PostServicesDNSResolverApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSResolverApplyEndpointJsonBody | PostServicesDNSResolverApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesDNSResolverApplyEndpointResponse400
    | PostServicesDNSResolverApplyEndpointResponse401
    | PostServicesDNSResolverApplyEndpointResponse403
    | PostServicesDNSResolverApplyEndpointResponse404
    | PostServicesDNSResolverApplyEndpointResponse405
    | PostServicesDNSResolverApplyEndpointResponse406
    | PostServicesDNSResolverApplyEndpointResponse409
    | PostServicesDNSResolverApplyEndpointResponse415
    | PostServicesDNSResolverApplyEndpointResponse422
    | PostServicesDNSResolverApplyEndpointResponse424
    | PostServicesDNSResolverApplyEndpointResponse500
    | PostServicesDNSResolverApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending DNS Resolver changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDNSResolverApplyEndpointJsonBody | Unset):
        body (PostServicesDNSResolverApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSResolverApplyEndpointResponse400 | PostServicesDNSResolverApplyEndpointResponse401 | PostServicesDNSResolverApplyEndpointResponse403 | PostServicesDNSResolverApplyEndpointResponse404 | PostServicesDNSResolverApplyEndpointResponse405 | PostServicesDNSResolverApplyEndpointResponse406 | PostServicesDNSResolverApplyEndpointResponse409 | PostServicesDNSResolverApplyEndpointResponse415 | PostServicesDNSResolverApplyEndpointResponse422 | PostServicesDNSResolverApplyEndpointResponse424 | PostServicesDNSResolverApplyEndpointResponse500 | PostServicesDNSResolverApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
