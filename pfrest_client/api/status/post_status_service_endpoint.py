from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_status_service_endpoint_data_body import PostStatusServiceEndpointDataBody
from ...models.post_status_service_endpoint_json_body import PostStatusServiceEndpointJsonBody
from ...models.post_status_service_endpoint_response_400 import PostStatusServiceEndpointResponse400
from ...models.post_status_service_endpoint_response_401 import PostStatusServiceEndpointResponse401
from ...models.post_status_service_endpoint_response_403 import PostStatusServiceEndpointResponse403
from ...models.post_status_service_endpoint_response_404 import PostStatusServiceEndpointResponse404
from ...models.post_status_service_endpoint_response_405 import PostStatusServiceEndpointResponse405
from ...models.post_status_service_endpoint_response_406 import PostStatusServiceEndpointResponse406
from ...models.post_status_service_endpoint_response_409 import PostStatusServiceEndpointResponse409
from ...models.post_status_service_endpoint_response_415 import PostStatusServiceEndpointResponse415
from ...models.post_status_service_endpoint_response_422 import PostStatusServiceEndpointResponse422
from ...models.post_status_service_endpoint_response_424 import PostStatusServiceEndpointResponse424
from ...models.post_status_service_endpoint_response_500 import PostStatusServiceEndpointResponse500
from ...models.post_status_service_endpoint_response_503 import PostStatusServiceEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostStatusServiceEndpointJsonBody | PostStatusServiceEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/status/service",
    }

    if isinstance(body, PostStatusServiceEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostStatusServiceEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostStatusServiceEndpointResponse400
    | PostStatusServiceEndpointResponse401
    | PostStatusServiceEndpointResponse403
    | PostStatusServiceEndpointResponse404
    | PostStatusServiceEndpointResponse405
    | PostStatusServiceEndpointResponse406
    | PostStatusServiceEndpointResponse409
    | PostStatusServiceEndpointResponse415
    | PostStatusServiceEndpointResponse422
    | PostStatusServiceEndpointResponse424
    | PostStatusServiceEndpointResponse500
    | PostStatusServiceEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostStatusServiceEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostStatusServiceEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostStatusServiceEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostStatusServiceEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostStatusServiceEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostStatusServiceEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostStatusServiceEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostStatusServiceEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostStatusServiceEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostStatusServiceEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostStatusServiceEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostStatusServiceEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostStatusServiceEndpointResponse400
    | PostStatusServiceEndpointResponse401
    | PostStatusServiceEndpointResponse403
    | PostStatusServiceEndpointResponse404
    | PostStatusServiceEndpointResponse405
    | PostStatusServiceEndpointResponse406
    | PostStatusServiceEndpointResponse409
    | PostStatusServiceEndpointResponse415
    | PostStatusServiceEndpointResponse422
    | PostStatusServiceEndpointResponse424
    | PostStatusServiceEndpointResponse500
    | PostStatusServiceEndpointResponse503
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
    body: PostStatusServiceEndpointJsonBody | PostStatusServiceEndpointDataBody | Unset = UNSET,
) -> Response[
    PostStatusServiceEndpointResponse400
    | PostStatusServiceEndpointResponse401
    | PostStatusServiceEndpointResponse403
    | PostStatusServiceEndpointResponse404
    | PostStatusServiceEndpointResponse405
    | PostStatusServiceEndpointResponse406
    | PostStatusServiceEndpointResponse409
    | PostStatusServiceEndpointResponse415
    | PostStatusServiceEndpointResponse422
    | PostStatusServiceEndpointResponse424
    | PostStatusServiceEndpointResponse500
    | PostStatusServiceEndpointResponse503
]:
    """<h3>Description:</h3>Triggers a start, stop or restart action for an existing
    Service<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Service<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-service-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostStatusServiceEndpointJsonBody | Unset):
        body (PostStatusServiceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostStatusServiceEndpointResponse400 | PostStatusServiceEndpointResponse401 | PostStatusServiceEndpointResponse403 | PostStatusServiceEndpointResponse404 | PostStatusServiceEndpointResponse405 | PostStatusServiceEndpointResponse406 | PostStatusServiceEndpointResponse409 | PostStatusServiceEndpointResponse415 | PostStatusServiceEndpointResponse422 | PostStatusServiceEndpointResponse424 | PostStatusServiceEndpointResponse500 | PostStatusServiceEndpointResponse503]
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
    body: PostStatusServiceEndpointJsonBody | PostStatusServiceEndpointDataBody | Unset = UNSET,
) -> (
    PostStatusServiceEndpointResponse400
    | PostStatusServiceEndpointResponse401
    | PostStatusServiceEndpointResponse403
    | PostStatusServiceEndpointResponse404
    | PostStatusServiceEndpointResponse405
    | PostStatusServiceEndpointResponse406
    | PostStatusServiceEndpointResponse409
    | PostStatusServiceEndpointResponse415
    | PostStatusServiceEndpointResponse422
    | PostStatusServiceEndpointResponse424
    | PostStatusServiceEndpointResponse500
    | PostStatusServiceEndpointResponse503
    | None
):
    """<h3>Description:</h3>Triggers a start, stop or restart action for an existing
    Service<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Service<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-service-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostStatusServiceEndpointJsonBody | Unset):
        body (PostStatusServiceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostStatusServiceEndpointResponse400 | PostStatusServiceEndpointResponse401 | PostStatusServiceEndpointResponse403 | PostStatusServiceEndpointResponse404 | PostStatusServiceEndpointResponse405 | PostStatusServiceEndpointResponse406 | PostStatusServiceEndpointResponse409 | PostStatusServiceEndpointResponse415 | PostStatusServiceEndpointResponse422 | PostStatusServiceEndpointResponse424 | PostStatusServiceEndpointResponse500 | PostStatusServiceEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostStatusServiceEndpointJsonBody | PostStatusServiceEndpointDataBody | Unset = UNSET,
) -> Response[
    PostStatusServiceEndpointResponse400
    | PostStatusServiceEndpointResponse401
    | PostStatusServiceEndpointResponse403
    | PostStatusServiceEndpointResponse404
    | PostStatusServiceEndpointResponse405
    | PostStatusServiceEndpointResponse406
    | PostStatusServiceEndpointResponse409
    | PostStatusServiceEndpointResponse415
    | PostStatusServiceEndpointResponse422
    | PostStatusServiceEndpointResponse424
    | PostStatusServiceEndpointResponse500
    | PostStatusServiceEndpointResponse503
]:
    """<h3>Description:</h3>Triggers a start, stop or restart action for an existing
    Service<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Service<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-service-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostStatusServiceEndpointJsonBody | Unset):
        body (PostStatusServiceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostStatusServiceEndpointResponse400 | PostStatusServiceEndpointResponse401 | PostStatusServiceEndpointResponse403 | PostStatusServiceEndpointResponse404 | PostStatusServiceEndpointResponse405 | PostStatusServiceEndpointResponse406 | PostStatusServiceEndpointResponse409 | PostStatusServiceEndpointResponse415 | PostStatusServiceEndpointResponse422 | PostStatusServiceEndpointResponse424 | PostStatusServiceEndpointResponse500 | PostStatusServiceEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostStatusServiceEndpointJsonBody | PostStatusServiceEndpointDataBody | Unset = UNSET,
) -> (
    PostStatusServiceEndpointResponse400
    | PostStatusServiceEndpointResponse401
    | PostStatusServiceEndpointResponse403
    | PostStatusServiceEndpointResponse404
    | PostStatusServiceEndpointResponse405
    | PostStatusServiceEndpointResponse406
    | PostStatusServiceEndpointResponse409
    | PostStatusServiceEndpointResponse415
    | PostStatusServiceEndpointResponse422
    | PostStatusServiceEndpointResponse424
    | PostStatusServiceEndpointResponse500
    | PostStatusServiceEndpointResponse503
    | None
):
    """<h3>Description:</h3>Triggers a start, stop or restart action for an existing
    Service<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Service<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-service-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostStatusServiceEndpointJsonBody | Unset):
        body (PostStatusServiceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostStatusServiceEndpointResponse400 | PostStatusServiceEndpointResponse401 | PostStatusServiceEndpointResponse403 | PostStatusServiceEndpointResponse404 | PostStatusServiceEndpointResponse405 | PostStatusServiceEndpointResponse406 | PostStatusServiceEndpointResponse409 | PostStatusServiceEndpointResponse415 | PostStatusServiceEndpointResponse422 | PostStatusServiceEndpointResponse424 | PostStatusServiceEndpointResponse500 | PostStatusServiceEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
