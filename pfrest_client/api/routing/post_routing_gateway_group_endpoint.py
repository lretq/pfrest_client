from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_routing_gateway_group_endpoint_data_body import PostRoutingGatewayGroupEndpointDataBody
from ...models.post_routing_gateway_group_endpoint_json_body import PostRoutingGatewayGroupEndpointJsonBody
from ...models.post_routing_gateway_group_endpoint_response_400 import PostRoutingGatewayGroupEndpointResponse400
from ...models.post_routing_gateway_group_endpoint_response_401 import PostRoutingGatewayGroupEndpointResponse401
from ...models.post_routing_gateway_group_endpoint_response_403 import PostRoutingGatewayGroupEndpointResponse403
from ...models.post_routing_gateway_group_endpoint_response_404 import PostRoutingGatewayGroupEndpointResponse404
from ...models.post_routing_gateway_group_endpoint_response_405 import PostRoutingGatewayGroupEndpointResponse405
from ...models.post_routing_gateway_group_endpoint_response_406 import PostRoutingGatewayGroupEndpointResponse406
from ...models.post_routing_gateway_group_endpoint_response_409 import PostRoutingGatewayGroupEndpointResponse409
from ...models.post_routing_gateway_group_endpoint_response_415 import PostRoutingGatewayGroupEndpointResponse415
from ...models.post_routing_gateway_group_endpoint_response_422 import PostRoutingGatewayGroupEndpointResponse422
from ...models.post_routing_gateway_group_endpoint_response_424 import PostRoutingGatewayGroupEndpointResponse424
from ...models.post_routing_gateway_group_endpoint_response_500 import PostRoutingGatewayGroupEndpointResponse500
from ...models.post_routing_gateway_group_endpoint_response_503 import PostRoutingGatewayGroupEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostRoutingGatewayGroupEndpointJsonBody | PostRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/routing/gateway/group",
    }

    if isinstance(body, PostRoutingGatewayGroupEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostRoutingGatewayGroupEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostRoutingGatewayGroupEndpointResponse400
    | PostRoutingGatewayGroupEndpointResponse401
    | PostRoutingGatewayGroupEndpointResponse403
    | PostRoutingGatewayGroupEndpointResponse404
    | PostRoutingGatewayGroupEndpointResponse405
    | PostRoutingGatewayGroupEndpointResponse406
    | PostRoutingGatewayGroupEndpointResponse409
    | PostRoutingGatewayGroupEndpointResponse415
    | PostRoutingGatewayGroupEndpointResponse422
    | PostRoutingGatewayGroupEndpointResponse424
    | PostRoutingGatewayGroupEndpointResponse500
    | PostRoutingGatewayGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostRoutingGatewayGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostRoutingGatewayGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostRoutingGatewayGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostRoutingGatewayGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostRoutingGatewayGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostRoutingGatewayGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostRoutingGatewayGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostRoutingGatewayGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostRoutingGatewayGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostRoutingGatewayGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostRoutingGatewayGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostRoutingGatewayGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostRoutingGatewayGroupEndpointResponse400
    | PostRoutingGatewayGroupEndpointResponse401
    | PostRoutingGatewayGroupEndpointResponse403
    | PostRoutingGatewayGroupEndpointResponse404
    | PostRoutingGatewayGroupEndpointResponse405
    | PostRoutingGatewayGroupEndpointResponse406
    | PostRoutingGatewayGroupEndpointResponse409
    | PostRoutingGatewayGroupEndpointResponse415
    | PostRoutingGatewayGroupEndpointResponse422
    | PostRoutingGatewayGroupEndpointResponse424
    | PostRoutingGatewayGroupEndpointResponse500
    | PostRoutingGatewayGroupEndpointResponse503
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
    body: PostRoutingGatewayGroupEndpointJsonBody | PostRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PostRoutingGatewayGroupEndpointResponse400
    | PostRoutingGatewayGroupEndpointResponse401
    | PostRoutingGatewayGroupEndpointResponse403
    | PostRoutingGatewayGroupEndpointResponse404
    | PostRoutingGatewayGroupEndpointResponse405
    | PostRoutingGatewayGroupEndpointResponse406
    | PostRoutingGatewayGroupEndpointResponse409
    | PostRoutingGatewayGroupEndpointResponse415
    | PostRoutingGatewayGroupEndpointResponse422
    | PostRoutingGatewayGroupEndpointResponse424
    | PostRoutingGatewayGroupEndpointResponse500
    | PostRoutingGatewayGroupEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PostRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRoutingGatewayGroupEndpointResponse400 | PostRoutingGatewayGroupEndpointResponse401 | PostRoutingGatewayGroupEndpointResponse403 | PostRoutingGatewayGroupEndpointResponse404 | PostRoutingGatewayGroupEndpointResponse405 | PostRoutingGatewayGroupEndpointResponse406 | PostRoutingGatewayGroupEndpointResponse409 | PostRoutingGatewayGroupEndpointResponse415 | PostRoutingGatewayGroupEndpointResponse422 | PostRoutingGatewayGroupEndpointResponse424 | PostRoutingGatewayGroupEndpointResponse500 | PostRoutingGatewayGroupEndpointResponse503]
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
    body: PostRoutingGatewayGroupEndpointJsonBody | PostRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> (
    PostRoutingGatewayGroupEndpointResponse400
    | PostRoutingGatewayGroupEndpointResponse401
    | PostRoutingGatewayGroupEndpointResponse403
    | PostRoutingGatewayGroupEndpointResponse404
    | PostRoutingGatewayGroupEndpointResponse405
    | PostRoutingGatewayGroupEndpointResponse406
    | PostRoutingGatewayGroupEndpointResponse409
    | PostRoutingGatewayGroupEndpointResponse415
    | PostRoutingGatewayGroupEndpointResponse422
    | PostRoutingGatewayGroupEndpointResponse424
    | PostRoutingGatewayGroupEndpointResponse500
    | PostRoutingGatewayGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PostRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRoutingGatewayGroupEndpointResponse400 | PostRoutingGatewayGroupEndpointResponse401 | PostRoutingGatewayGroupEndpointResponse403 | PostRoutingGatewayGroupEndpointResponse404 | PostRoutingGatewayGroupEndpointResponse405 | PostRoutingGatewayGroupEndpointResponse406 | PostRoutingGatewayGroupEndpointResponse409 | PostRoutingGatewayGroupEndpointResponse415 | PostRoutingGatewayGroupEndpointResponse422 | PostRoutingGatewayGroupEndpointResponse424 | PostRoutingGatewayGroupEndpointResponse500 | PostRoutingGatewayGroupEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutingGatewayGroupEndpointJsonBody | PostRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PostRoutingGatewayGroupEndpointResponse400
    | PostRoutingGatewayGroupEndpointResponse401
    | PostRoutingGatewayGroupEndpointResponse403
    | PostRoutingGatewayGroupEndpointResponse404
    | PostRoutingGatewayGroupEndpointResponse405
    | PostRoutingGatewayGroupEndpointResponse406
    | PostRoutingGatewayGroupEndpointResponse409
    | PostRoutingGatewayGroupEndpointResponse415
    | PostRoutingGatewayGroupEndpointResponse422
    | PostRoutingGatewayGroupEndpointResponse424
    | PostRoutingGatewayGroupEndpointResponse500
    | PostRoutingGatewayGroupEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PostRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRoutingGatewayGroupEndpointResponse400 | PostRoutingGatewayGroupEndpointResponse401 | PostRoutingGatewayGroupEndpointResponse403 | PostRoutingGatewayGroupEndpointResponse404 | PostRoutingGatewayGroupEndpointResponse405 | PostRoutingGatewayGroupEndpointResponse406 | PostRoutingGatewayGroupEndpointResponse409 | PostRoutingGatewayGroupEndpointResponse415 | PostRoutingGatewayGroupEndpointResponse422 | PostRoutingGatewayGroupEndpointResponse424 | PostRoutingGatewayGroupEndpointResponse500 | PostRoutingGatewayGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutingGatewayGroupEndpointJsonBody | PostRoutingGatewayGroupEndpointDataBody | Unset = UNSET,
) -> (
    PostRoutingGatewayGroupEndpointResponse400
    | PostRoutingGatewayGroupEndpointResponse401
    | PostRoutingGatewayGroupEndpointResponse403
    | PostRoutingGatewayGroupEndpointResponse404
    | PostRoutingGatewayGroupEndpointResponse405
    | PostRoutingGatewayGroupEndpointResponse406
    | PostRoutingGatewayGroupEndpointResponse409
    | PostRoutingGatewayGroupEndpointResponse415
    | PostRoutingGatewayGroupEndpointResponse422
    | PostRoutingGatewayGroupEndpointResponse424
    | PostRoutingGatewayGroupEndpointResponse500
    | PostRoutingGatewayGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostRoutingGatewayGroupEndpointJsonBody | Unset):
        body (PostRoutingGatewayGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRoutingGatewayGroupEndpointResponse400 | PostRoutingGatewayGroupEndpointResponse401 | PostRoutingGatewayGroupEndpointResponse403 | PostRoutingGatewayGroupEndpointResponse404 | PostRoutingGatewayGroupEndpointResponse405 | PostRoutingGatewayGroupEndpointResponse406 | PostRoutingGatewayGroupEndpointResponse409 | PostRoutingGatewayGroupEndpointResponse415 | PostRoutingGatewayGroupEndpointResponse422 | PostRoutingGatewayGroupEndpointResponse424 | PostRoutingGatewayGroupEndpointResponse500 | PostRoutingGatewayGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
