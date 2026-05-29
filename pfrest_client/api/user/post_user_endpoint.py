from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_user_endpoint_data_body import PostUserEndpointDataBody
from ...models.post_user_endpoint_json_body import PostUserEndpointJsonBody
from ...models.post_user_endpoint_response_400 import PostUserEndpointResponse400
from ...models.post_user_endpoint_response_401 import PostUserEndpointResponse401
from ...models.post_user_endpoint_response_403 import PostUserEndpointResponse403
from ...models.post_user_endpoint_response_404 import PostUserEndpointResponse404
from ...models.post_user_endpoint_response_405 import PostUserEndpointResponse405
from ...models.post_user_endpoint_response_406 import PostUserEndpointResponse406
from ...models.post_user_endpoint_response_409 import PostUserEndpointResponse409
from ...models.post_user_endpoint_response_415 import PostUserEndpointResponse415
from ...models.post_user_endpoint_response_422 import PostUserEndpointResponse422
from ...models.post_user_endpoint_response_424 import PostUserEndpointResponse424
from ...models.post_user_endpoint_response_500 import PostUserEndpointResponse500
from ...models.post_user_endpoint_response_503 import PostUserEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostUserEndpointJsonBody | PostUserEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/user",
    }

    if isinstance(body, PostUserEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostUserEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostUserEndpointResponse400
    | PostUserEndpointResponse401
    | PostUserEndpointResponse403
    | PostUserEndpointResponse404
    | PostUserEndpointResponse405
    | PostUserEndpointResponse406
    | PostUserEndpointResponse409
    | PostUserEndpointResponse415
    | PostUserEndpointResponse422
    | PostUserEndpointResponse424
    | PostUserEndpointResponse500
    | PostUserEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostUserEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostUserEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostUserEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostUserEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostUserEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostUserEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostUserEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostUserEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostUserEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostUserEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostUserEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostUserEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostUserEndpointResponse400
    | PostUserEndpointResponse401
    | PostUserEndpointResponse403
    | PostUserEndpointResponse404
    | PostUserEndpointResponse405
    | PostUserEndpointResponse406
    | PostUserEndpointResponse409
    | PostUserEndpointResponse415
    | PostUserEndpointResponse422
    | PostUserEndpointResponse424
    | PostUserEndpointResponse500
    | PostUserEndpointResponse503
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
    body: PostUserEndpointJsonBody | PostUserEndpointDataBody | Unset = UNSET,
) -> Response[
    PostUserEndpointResponse400
    | PostUserEndpointResponse401
    | PostUserEndpointResponse403
    | PostUserEndpointResponse404
    | PostUserEndpointResponse405
    | PostUserEndpointResponse406
    | PostUserEndpointResponse409
    | PostUserEndpointResponse415
    | PostUserEndpointResponse422
    | PostUserEndpointResponse424
    | PostUserEndpointResponse500
    | PostUserEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostUserEndpointJsonBody | Unset):
        body (PostUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUserEndpointResponse400 | PostUserEndpointResponse401 | PostUserEndpointResponse403 | PostUserEndpointResponse404 | PostUserEndpointResponse405 | PostUserEndpointResponse406 | PostUserEndpointResponse409 | PostUserEndpointResponse415 | PostUserEndpointResponse422 | PostUserEndpointResponse424 | PostUserEndpointResponse500 | PostUserEndpointResponse503]
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
    body: PostUserEndpointJsonBody | PostUserEndpointDataBody | Unset = UNSET,
) -> (
    PostUserEndpointResponse400
    | PostUserEndpointResponse401
    | PostUserEndpointResponse403
    | PostUserEndpointResponse404
    | PostUserEndpointResponse405
    | PostUserEndpointResponse406
    | PostUserEndpointResponse409
    | PostUserEndpointResponse415
    | PostUserEndpointResponse422
    | PostUserEndpointResponse424
    | PostUserEndpointResponse500
    | PostUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostUserEndpointJsonBody | Unset):
        body (PostUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUserEndpointResponse400 | PostUserEndpointResponse401 | PostUserEndpointResponse403 | PostUserEndpointResponse404 | PostUserEndpointResponse405 | PostUserEndpointResponse406 | PostUserEndpointResponse409 | PostUserEndpointResponse415 | PostUserEndpointResponse422 | PostUserEndpointResponse424 | PostUserEndpointResponse500 | PostUserEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostUserEndpointJsonBody | PostUserEndpointDataBody | Unset = UNSET,
) -> Response[
    PostUserEndpointResponse400
    | PostUserEndpointResponse401
    | PostUserEndpointResponse403
    | PostUserEndpointResponse404
    | PostUserEndpointResponse405
    | PostUserEndpointResponse406
    | PostUserEndpointResponse409
    | PostUserEndpointResponse415
    | PostUserEndpointResponse422
    | PostUserEndpointResponse424
    | PostUserEndpointResponse500
    | PostUserEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostUserEndpointJsonBody | Unset):
        body (PostUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUserEndpointResponse400 | PostUserEndpointResponse401 | PostUserEndpointResponse403 | PostUserEndpointResponse404 | PostUserEndpointResponse405 | PostUserEndpointResponse406 | PostUserEndpointResponse409 | PostUserEndpointResponse415 | PostUserEndpointResponse422 | PostUserEndpointResponse424 | PostUserEndpointResponse500 | PostUserEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostUserEndpointJsonBody | PostUserEndpointDataBody | Unset = UNSET,
) -> (
    PostUserEndpointResponse400
    | PostUserEndpointResponse401
    | PostUserEndpointResponse403
    | PostUserEndpointResponse404
    | PostUserEndpointResponse405
    | PostUserEndpointResponse406
    | PostUserEndpointResponse409
    | PostUserEndpointResponse415
    | PostUserEndpointResponse422
    | PostUserEndpointResponse424
    | PostUserEndpointResponse500
    | PostUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostUserEndpointJsonBody | Unset):
        body (PostUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUserEndpointResponse400 | PostUserEndpointResponse401 | PostUserEndpointResponse403 | PostUserEndpointResponse404 | PostUserEndpointResponse405 | PostUserEndpointResponse406 | PostUserEndpointResponse409 | PostUserEndpointResponse415 | PostUserEndpointResponse422 | PostUserEndpointResponse424 | PostUserEndpointResponse500 | PostUserEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
