from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_routing_static_route_endpoint_data_body import PostRoutingStaticRouteEndpointDataBody
from ...models.post_routing_static_route_endpoint_json_body import PostRoutingStaticRouteEndpointJsonBody
from ...models.post_routing_static_route_endpoint_response_400 import PostRoutingStaticRouteEndpointResponse400
from ...models.post_routing_static_route_endpoint_response_401 import PostRoutingStaticRouteEndpointResponse401
from ...models.post_routing_static_route_endpoint_response_403 import PostRoutingStaticRouteEndpointResponse403
from ...models.post_routing_static_route_endpoint_response_404 import PostRoutingStaticRouteEndpointResponse404
from ...models.post_routing_static_route_endpoint_response_405 import PostRoutingStaticRouteEndpointResponse405
from ...models.post_routing_static_route_endpoint_response_406 import PostRoutingStaticRouteEndpointResponse406
from ...models.post_routing_static_route_endpoint_response_409 import PostRoutingStaticRouteEndpointResponse409
from ...models.post_routing_static_route_endpoint_response_415 import PostRoutingStaticRouteEndpointResponse415
from ...models.post_routing_static_route_endpoint_response_422 import PostRoutingStaticRouteEndpointResponse422
from ...models.post_routing_static_route_endpoint_response_424 import PostRoutingStaticRouteEndpointResponse424
from ...models.post_routing_static_route_endpoint_response_500 import PostRoutingStaticRouteEndpointResponse500
from ...models.post_routing_static_route_endpoint_response_503 import PostRoutingStaticRouteEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostRoutingStaticRouteEndpointJsonBody | PostRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/routing/static_route",
    }

    if isinstance(body, PostRoutingStaticRouteEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostRoutingStaticRouteEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostRoutingStaticRouteEndpointResponse400
    | PostRoutingStaticRouteEndpointResponse401
    | PostRoutingStaticRouteEndpointResponse403
    | PostRoutingStaticRouteEndpointResponse404
    | PostRoutingStaticRouteEndpointResponse405
    | PostRoutingStaticRouteEndpointResponse406
    | PostRoutingStaticRouteEndpointResponse409
    | PostRoutingStaticRouteEndpointResponse415
    | PostRoutingStaticRouteEndpointResponse422
    | PostRoutingStaticRouteEndpointResponse424
    | PostRoutingStaticRouteEndpointResponse500
    | PostRoutingStaticRouteEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostRoutingStaticRouteEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostRoutingStaticRouteEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostRoutingStaticRouteEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostRoutingStaticRouteEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostRoutingStaticRouteEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostRoutingStaticRouteEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostRoutingStaticRouteEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostRoutingStaticRouteEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostRoutingStaticRouteEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostRoutingStaticRouteEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostRoutingStaticRouteEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostRoutingStaticRouteEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostRoutingStaticRouteEndpointResponse400
    | PostRoutingStaticRouteEndpointResponse401
    | PostRoutingStaticRouteEndpointResponse403
    | PostRoutingStaticRouteEndpointResponse404
    | PostRoutingStaticRouteEndpointResponse405
    | PostRoutingStaticRouteEndpointResponse406
    | PostRoutingStaticRouteEndpointResponse409
    | PostRoutingStaticRouteEndpointResponse415
    | PostRoutingStaticRouteEndpointResponse422
    | PostRoutingStaticRouteEndpointResponse424
    | PostRoutingStaticRouteEndpointResponse500
    | PostRoutingStaticRouteEndpointResponse503
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
    body: PostRoutingStaticRouteEndpointJsonBody | PostRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> Response[
    PostRoutingStaticRouteEndpointResponse400
    | PostRoutingStaticRouteEndpointResponse401
    | PostRoutingStaticRouteEndpointResponse403
    | PostRoutingStaticRouteEndpointResponse404
    | PostRoutingStaticRouteEndpointResponse405
    | PostRoutingStaticRouteEndpointResponse406
    | PostRoutingStaticRouteEndpointResponse409
    | PostRoutingStaticRouteEndpointResponse415
    | PostRoutingStaticRouteEndpointResponse422
    | PostRoutingStaticRouteEndpointResponse424
    | PostRoutingStaticRouteEndpointResponse500
    | PostRoutingStaticRouteEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingStaticRouteEndpointJsonBody | Unset):
        body (PostRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRoutingStaticRouteEndpointResponse400 | PostRoutingStaticRouteEndpointResponse401 | PostRoutingStaticRouteEndpointResponse403 | PostRoutingStaticRouteEndpointResponse404 | PostRoutingStaticRouteEndpointResponse405 | PostRoutingStaticRouteEndpointResponse406 | PostRoutingStaticRouteEndpointResponse409 | PostRoutingStaticRouteEndpointResponse415 | PostRoutingStaticRouteEndpointResponse422 | PostRoutingStaticRouteEndpointResponse424 | PostRoutingStaticRouteEndpointResponse500 | PostRoutingStaticRouteEndpointResponse503]
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
    body: PostRoutingStaticRouteEndpointJsonBody | PostRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> (
    PostRoutingStaticRouteEndpointResponse400
    | PostRoutingStaticRouteEndpointResponse401
    | PostRoutingStaticRouteEndpointResponse403
    | PostRoutingStaticRouteEndpointResponse404
    | PostRoutingStaticRouteEndpointResponse405
    | PostRoutingStaticRouteEndpointResponse406
    | PostRoutingStaticRouteEndpointResponse409
    | PostRoutingStaticRouteEndpointResponse415
    | PostRoutingStaticRouteEndpointResponse422
    | PostRoutingStaticRouteEndpointResponse424
    | PostRoutingStaticRouteEndpointResponse500
    | PostRoutingStaticRouteEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingStaticRouteEndpointJsonBody | Unset):
        body (PostRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRoutingStaticRouteEndpointResponse400 | PostRoutingStaticRouteEndpointResponse401 | PostRoutingStaticRouteEndpointResponse403 | PostRoutingStaticRouteEndpointResponse404 | PostRoutingStaticRouteEndpointResponse405 | PostRoutingStaticRouteEndpointResponse406 | PostRoutingStaticRouteEndpointResponse409 | PostRoutingStaticRouteEndpointResponse415 | PostRoutingStaticRouteEndpointResponse422 | PostRoutingStaticRouteEndpointResponse424 | PostRoutingStaticRouteEndpointResponse500 | PostRoutingStaticRouteEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutingStaticRouteEndpointJsonBody | PostRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> Response[
    PostRoutingStaticRouteEndpointResponse400
    | PostRoutingStaticRouteEndpointResponse401
    | PostRoutingStaticRouteEndpointResponse403
    | PostRoutingStaticRouteEndpointResponse404
    | PostRoutingStaticRouteEndpointResponse405
    | PostRoutingStaticRouteEndpointResponse406
    | PostRoutingStaticRouteEndpointResponse409
    | PostRoutingStaticRouteEndpointResponse415
    | PostRoutingStaticRouteEndpointResponse422
    | PostRoutingStaticRouteEndpointResponse424
    | PostRoutingStaticRouteEndpointResponse500
    | PostRoutingStaticRouteEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingStaticRouteEndpointJsonBody | Unset):
        body (PostRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRoutingStaticRouteEndpointResponse400 | PostRoutingStaticRouteEndpointResponse401 | PostRoutingStaticRouteEndpointResponse403 | PostRoutingStaticRouteEndpointResponse404 | PostRoutingStaticRouteEndpointResponse405 | PostRoutingStaticRouteEndpointResponse406 | PostRoutingStaticRouteEndpointResponse409 | PostRoutingStaticRouteEndpointResponse415 | PostRoutingStaticRouteEndpointResponse422 | PostRoutingStaticRouteEndpointResponse424 | PostRoutingStaticRouteEndpointResponse500 | PostRoutingStaticRouteEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutingStaticRouteEndpointJsonBody | PostRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> (
    PostRoutingStaticRouteEndpointResponse400
    | PostRoutingStaticRouteEndpointResponse401
    | PostRoutingStaticRouteEndpointResponse403
    | PostRoutingStaticRouteEndpointResponse404
    | PostRoutingStaticRouteEndpointResponse405
    | PostRoutingStaticRouteEndpointResponse406
    | PostRoutingStaticRouteEndpointResponse409
    | PostRoutingStaticRouteEndpointResponse415
    | PostRoutingStaticRouteEndpointResponse422
    | PostRoutingStaticRouteEndpointResponse424
    | PostRoutingStaticRouteEndpointResponse500
    | PostRoutingStaticRouteEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingStaticRouteEndpointJsonBody | Unset):
        body (PostRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRoutingStaticRouteEndpointResponse400 | PostRoutingStaticRouteEndpointResponse401 | PostRoutingStaticRouteEndpointResponse403 | PostRoutingStaticRouteEndpointResponse404 | PostRoutingStaticRouteEndpointResponse405 | PostRoutingStaticRouteEndpointResponse406 | PostRoutingStaticRouteEndpointResponse409 | PostRoutingStaticRouteEndpointResponse415 | PostRoutingStaticRouteEndpointResponse422 | PostRoutingStaticRouteEndpointResponse424 | PostRoutingStaticRouteEndpointResponse500 | PostRoutingStaticRouteEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
