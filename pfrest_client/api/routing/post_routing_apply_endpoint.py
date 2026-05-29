from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_routing_apply_endpoint_data_body import PostRoutingApplyEndpointDataBody
from ...models.post_routing_apply_endpoint_json_body import PostRoutingApplyEndpointJsonBody
from ...models.post_routing_apply_endpoint_response_400 import PostRoutingApplyEndpointResponse400
from ...models.post_routing_apply_endpoint_response_401 import PostRoutingApplyEndpointResponse401
from ...models.post_routing_apply_endpoint_response_403 import PostRoutingApplyEndpointResponse403
from ...models.post_routing_apply_endpoint_response_404 import PostRoutingApplyEndpointResponse404
from ...models.post_routing_apply_endpoint_response_405 import PostRoutingApplyEndpointResponse405
from ...models.post_routing_apply_endpoint_response_406 import PostRoutingApplyEndpointResponse406
from ...models.post_routing_apply_endpoint_response_409 import PostRoutingApplyEndpointResponse409
from ...models.post_routing_apply_endpoint_response_415 import PostRoutingApplyEndpointResponse415
from ...models.post_routing_apply_endpoint_response_422 import PostRoutingApplyEndpointResponse422
from ...models.post_routing_apply_endpoint_response_424 import PostRoutingApplyEndpointResponse424
from ...models.post_routing_apply_endpoint_response_500 import PostRoutingApplyEndpointResponse500
from ...models.post_routing_apply_endpoint_response_503 import PostRoutingApplyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostRoutingApplyEndpointJsonBody | PostRoutingApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/routing/apply",
    }

    if isinstance(body, PostRoutingApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostRoutingApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostRoutingApplyEndpointResponse400
    | PostRoutingApplyEndpointResponse401
    | PostRoutingApplyEndpointResponse403
    | PostRoutingApplyEndpointResponse404
    | PostRoutingApplyEndpointResponse405
    | PostRoutingApplyEndpointResponse406
    | PostRoutingApplyEndpointResponse409
    | PostRoutingApplyEndpointResponse415
    | PostRoutingApplyEndpointResponse422
    | PostRoutingApplyEndpointResponse424
    | PostRoutingApplyEndpointResponse500
    | PostRoutingApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostRoutingApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostRoutingApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostRoutingApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostRoutingApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostRoutingApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostRoutingApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostRoutingApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostRoutingApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostRoutingApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostRoutingApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostRoutingApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostRoutingApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostRoutingApplyEndpointResponse400
    | PostRoutingApplyEndpointResponse401
    | PostRoutingApplyEndpointResponse403
    | PostRoutingApplyEndpointResponse404
    | PostRoutingApplyEndpointResponse405
    | PostRoutingApplyEndpointResponse406
    | PostRoutingApplyEndpointResponse409
    | PostRoutingApplyEndpointResponse415
    | PostRoutingApplyEndpointResponse422
    | PostRoutingApplyEndpointResponse424
    | PostRoutingApplyEndpointResponse500
    | PostRoutingApplyEndpointResponse503
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
    body: PostRoutingApplyEndpointJsonBody | PostRoutingApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostRoutingApplyEndpointResponse400
    | PostRoutingApplyEndpointResponse401
    | PostRoutingApplyEndpointResponse403
    | PostRoutingApplyEndpointResponse404
    | PostRoutingApplyEndpointResponse405
    | PostRoutingApplyEndpointResponse406
    | PostRoutingApplyEndpointResponse409
    | PostRoutingApplyEndpointResponse415
    | PostRoutingApplyEndpointResponse422
    | PostRoutingApplyEndpointResponse424
    | PostRoutingApplyEndpointResponse500
    | PostRoutingApplyEndpointResponse503
]:
    """<h3>Description:</h3>Creates Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostRoutingApplyEndpointJsonBody | Unset):
        body (PostRoutingApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRoutingApplyEndpointResponse400 | PostRoutingApplyEndpointResponse401 | PostRoutingApplyEndpointResponse403 | PostRoutingApplyEndpointResponse404 | PostRoutingApplyEndpointResponse405 | PostRoutingApplyEndpointResponse406 | PostRoutingApplyEndpointResponse409 | PostRoutingApplyEndpointResponse415 | PostRoutingApplyEndpointResponse422 | PostRoutingApplyEndpointResponse424 | PostRoutingApplyEndpointResponse500 | PostRoutingApplyEndpointResponse503]
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
    body: PostRoutingApplyEndpointJsonBody | PostRoutingApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostRoutingApplyEndpointResponse400
    | PostRoutingApplyEndpointResponse401
    | PostRoutingApplyEndpointResponse403
    | PostRoutingApplyEndpointResponse404
    | PostRoutingApplyEndpointResponse405
    | PostRoutingApplyEndpointResponse406
    | PostRoutingApplyEndpointResponse409
    | PostRoutingApplyEndpointResponse415
    | PostRoutingApplyEndpointResponse422
    | PostRoutingApplyEndpointResponse424
    | PostRoutingApplyEndpointResponse500
    | PostRoutingApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostRoutingApplyEndpointJsonBody | Unset):
        body (PostRoutingApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRoutingApplyEndpointResponse400 | PostRoutingApplyEndpointResponse401 | PostRoutingApplyEndpointResponse403 | PostRoutingApplyEndpointResponse404 | PostRoutingApplyEndpointResponse405 | PostRoutingApplyEndpointResponse406 | PostRoutingApplyEndpointResponse409 | PostRoutingApplyEndpointResponse415 | PostRoutingApplyEndpointResponse422 | PostRoutingApplyEndpointResponse424 | PostRoutingApplyEndpointResponse500 | PostRoutingApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutingApplyEndpointJsonBody | PostRoutingApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostRoutingApplyEndpointResponse400
    | PostRoutingApplyEndpointResponse401
    | PostRoutingApplyEndpointResponse403
    | PostRoutingApplyEndpointResponse404
    | PostRoutingApplyEndpointResponse405
    | PostRoutingApplyEndpointResponse406
    | PostRoutingApplyEndpointResponse409
    | PostRoutingApplyEndpointResponse415
    | PostRoutingApplyEndpointResponse422
    | PostRoutingApplyEndpointResponse424
    | PostRoutingApplyEndpointResponse500
    | PostRoutingApplyEndpointResponse503
]:
    """<h3>Description:</h3>Creates Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostRoutingApplyEndpointJsonBody | Unset):
        body (PostRoutingApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRoutingApplyEndpointResponse400 | PostRoutingApplyEndpointResponse401 | PostRoutingApplyEndpointResponse403 | PostRoutingApplyEndpointResponse404 | PostRoutingApplyEndpointResponse405 | PostRoutingApplyEndpointResponse406 | PostRoutingApplyEndpointResponse409 | PostRoutingApplyEndpointResponse415 | PostRoutingApplyEndpointResponse422 | PostRoutingApplyEndpointResponse424 | PostRoutingApplyEndpointResponse500 | PostRoutingApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostRoutingApplyEndpointJsonBody | PostRoutingApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostRoutingApplyEndpointResponse400
    | PostRoutingApplyEndpointResponse401
    | PostRoutingApplyEndpointResponse403
    | PostRoutingApplyEndpointResponse404
    | PostRoutingApplyEndpointResponse405
    | PostRoutingApplyEndpointResponse406
    | PostRoutingApplyEndpointResponse409
    | PostRoutingApplyEndpointResponse415
    | PostRoutingApplyEndpointResponse422
    | PostRoutingApplyEndpointResponse424
    | PostRoutingApplyEndpointResponse500
    | PostRoutingApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostRoutingApplyEndpointJsonBody | Unset):
        body (PostRoutingApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRoutingApplyEndpointResponse400 | PostRoutingApplyEndpointResponse401 | PostRoutingApplyEndpointResponse403 | PostRoutingApplyEndpointResponse404 | PostRoutingApplyEndpointResponse405 | PostRoutingApplyEndpointResponse406 | PostRoutingApplyEndpointResponse409 | PostRoutingApplyEndpointResponse415 | PostRoutingApplyEndpointResponse422 | PostRoutingApplyEndpointResponse424 | PostRoutingApplyEndpointResponse500 | PostRoutingApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
