from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_user_auth_server_endpoint_data_body import PostUserAuthServerEndpointDataBody
from ...models.post_user_auth_server_endpoint_json_body import PostUserAuthServerEndpointJsonBody
from ...models.post_user_auth_server_endpoint_response_400 import PostUserAuthServerEndpointResponse400
from ...models.post_user_auth_server_endpoint_response_401 import PostUserAuthServerEndpointResponse401
from ...models.post_user_auth_server_endpoint_response_403 import PostUserAuthServerEndpointResponse403
from ...models.post_user_auth_server_endpoint_response_404 import PostUserAuthServerEndpointResponse404
from ...models.post_user_auth_server_endpoint_response_405 import PostUserAuthServerEndpointResponse405
from ...models.post_user_auth_server_endpoint_response_406 import PostUserAuthServerEndpointResponse406
from ...models.post_user_auth_server_endpoint_response_409 import PostUserAuthServerEndpointResponse409
from ...models.post_user_auth_server_endpoint_response_415 import PostUserAuthServerEndpointResponse415
from ...models.post_user_auth_server_endpoint_response_422 import PostUserAuthServerEndpointResponse422
from ...models.post_user_auth_server_endpoint_response_424 import PostUserAuthServerEndpointResponse424
from ...models.post_user_auth_server_endpoint_response_500 import PostUserAuthServerEndpointResponse500
from ...models.post_user_auth_server_endpoint_response_503 import PostUserAuthServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostUserAuthServerEndpointJsonBody | PostUserAuthServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/user/auth_server",
    }

    if isinstance(body, PostUserAuthServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostUserAuthServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostUserAuthServerEndpointResponse400
    | PostUserAuthServerEndpointResponse401
    | PostUserAuthServerEndpointResponse403
    | PostUserAuthServerEndpointResponse404
    | PostUserAuthServerEndpointResponse405
    | PostUserAuthServerEndpointResponse406
    | PostUserAuthServerEndpointResponse409
    | PostUserAuthServerEndpointResponse415
    | PostUserAuthServerEndpointResponse422
    | PostUserAuthServerEndpointResponse424
    | PostUserAuthServerEndpointResponse500
    | PostUserAuthServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostUserAuthServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostUserAuthServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostUserAuthServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostUserAuthServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostUserAuthServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostUserAuthServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostUserAuthServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostUserAuthServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostUserAuthServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostUserAuthServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostUserAuthServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostUserAuthServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostUserAuthServerEndpointResponse400
    | PostUserAuthServerEndpointResponse401
    | PostUserAuthServerEndpointResponse403
    | PostUserAuthServerEndpointResponse404
    | PostUserAuthServerEndpointResponse405
    | PostUserAuthServerEndpointResponse406
    | PostUserAuthServerEndpointResponse409
    | PostUserAuthServerEndpointResponse415
    | PostUserAuthServerEndpointResponse422
    | PostUserAuthServerEndpointResponse424
    | PostUserAuthServerEndpointResponse500
    | PostUserAuthServerEndpointResponse503
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
    body: PostUserAuthServerEndpointJsonBody | PostUserAuthServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostUserAuthServerEndpointResponse400
    | PostUserAuthServerEndpointResponse401
    | PostUserAuthServerEndpointResponse403
    | PostUserAuthServerEndpointResponse404
    | PostUserAuthServerEndpointResponse405
    | PostUserAuthServerEndpointResponse406
    | PostUserAuthServerEndpointResponse409
    | PostUserAuthServerEndpointResponse415
    | PostUserAuthServerEndpointResponse422
    | PostUserAuthServerEndpointResponse424
    | PostUserAuthServerEndpointResponse500
    | PostUserAuthServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new authentication server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostUserAuthServerEndpointJsonBody | Unset):
        body (PostUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUserAuthServerEndpointResponse400 | PostUserAuthServerEndpointResponse401 | PostUserAuthServerEndpointResponse403 | PostUserAuthServerEndpointResponse404 | PostUserAuthServerEndpointResponse405 | PostUserAuthServerEndpointResponse406 | PostUserAuthServerEndpointResponse409 | PostUserAuthServerEndpointResponse415 | PostUserAuthServerEndpointResponse422 | PostUserAuthServerEndpointResponse424 | PostUserAuthServerEndpointResponse500 | PostUserAuthServerEndpointResponse503]
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
    body: PostUserAuthServerEndpointJsonBody | PostUserAuthServerEndpointDataBody | Unset = UNSET,
) -> (
    PostUserAuthServerEndpointResponse400
    | PostUserAuthServerEndpointResponse401
    | PostUserAuthServerEndpointResponse403
    | PostUserAuthServerEndpointResponse404
    | PostUserAuthServerEndpointResponse405
    | PostUserAuthServerEndpointResponse406
    | PostUserAuthServerEndpointResponse409
    | PostUserAuthServerEndpointResponse415
    | PostUserAuthServerEndpointResponse422
    | PostUserAuthServerEndpointResponse424
    | PostUserAuthServerEndpointResponse500
    | PostUserAuthServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new authentication server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostUserAuthServerEndpointJsonBody | Unset):
        body (PostUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUserAuthServerEndpointResponse400 | PostUserAuthServerEndpointResponse401 | PostUserAuthServerEndpointResponse403 | PostUserAuthServerEndpointResponse404 | PostUserAuthServerEndpointResponse405 | PostUserAuthServerEndpointResponse406 | PostUserAuthServerEndpointResponse409 | PostUserAuthServerEndpointResponse415 | PostUserAuthServerEndpointResponse422 | PostUserAuthServerEndpointResponse424 | PostUserAuthServerEndpointResponse500 | PostUserAuthServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostUserAuthServerEndpointJsonBody | PostUserAuthServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostUserAuthServerEndpointResponse400
    | PostUserAuthServerEndpointResponse401
    | PostUserAuthServerEndpointResponse403
    | PostUserAuthServerEndpointResponse404
    | PostUserAuthServerEndpointResponse405
    | PostUserAuthServerEndpointResponse406
    | PostUserAuthServerEndpointResponse409
    | PostUserAuthServerEndpointResponse415
    | PostUserAuthServerEndpointResponse422
    | PostUserAuthServerEndpointResponse424
    | PostUserAuthServerEndpointResponse500
    | PostUserAuthServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new authentication server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostUserAuthServerEndpointJsonBody | Unset):
        body (PostUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUserAuthServerEndpointResponse400 | PostUserAuthServerEndpointResponse401 | PostUserAuthServerEndpointResponse403 | PostUserAuthServerEndpointResponse404 | PostUserAuthServerEndpointResponse405 | PostUserAuthServerEndpointResponse406 | PostUserAuthServerEndpointResponse409 | PostUserAuthServerEndpointResponse415 | PostUserAuthServerEndpointResponse422 | PostUserAuthServerEndpointResponse424 | PostUserAuthServerEndpointResponse500 | PostUserAuthServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostUserAuthServerEndpointJsonBody | PostUserAuthServerEndpointDataBody | Unset = UNSET,
) -> (
    PostUserAuthServerEndpointResponse400
    | PostUserAuthServerEndpointResponse401
    | PostUserAuthServerEndpointResponse403
    | PostUserAuthServerEndpointResponse404
    | PostUserAuthServerEndpointResponse405
    | PostUserAuthServerEndpointResponse406
    | PostUserAuthServerEndpointResponse409
    | PostUserAuthServerEndpointResponse415
    | PostUserAuthServerEndpointResponse422
    | PostUserAuthServerEndpointResponse424
    | PostUserAuthServerEndpointResponse500
    | PostUserAuthServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new authentication server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostUserAuthServerEndpointJsonBody | Unset):
        body (PostUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUserAuthServerEndpointResponse400 | PostUserAuthServerEndpointResponse401 | PostUserAuthServerEndpointResponse403 | PostUserAuthServerEndpointResponse404 | PostUserAuthServerEndpointResponse405 | PostUserAuthServerEndpointResponse406 | PostUserAuthServerEndpointResponse409 | PostUserAuthServerEndpointResponse415 | PostUserAuthServerEndpointResponse422 | PostUserAuthServerEndpointResponse424 | PostUserAuthServerEndpointResponse500 | PostUserAuthServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
