from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_auth_key_endpoint_data_body import PostAuthKeyEndpointDataBody
from ...models.post_auth_key_endpoint_json_body import PostAuthKeyEndpointJsonBody
from ...models.post_auth_key_endpoint_response_400 import PostAuthKeyEndpointResponse400
from ...models.post_auth_key_endpoint_response_401 import PostAuthKeyEndpointResponse401
from ...models.post_auth_key_endpoint_response_403 import PostAuthKeyEndpointResponse403
from ...models.post_auth_key_endpoint_response_404 import PostAuthKeyEndpointResponse404
from ...models.post_auth_key_endpoint_response_405 import PostAuthKeyEndpointResponse405
from ...models.post_auth_key_endpoint_response_406 import PostAuthKeyEndpointResponse406
from ...models.post_auth_key_endpoint_response_409 import PostAuthKeyEndpointResponse409
from ...models.post_auth_key_endpoint_response_415 import PostAuthKeyEndpointResponse415
from ...models.post_auth_key_endpoint_response_422 import PostAuthKeyEndpointResponse422
from ...models.post_auth_key_endpoint_response_424 import PostAuthKeyEndpointResponse424
from ...models.post_auth_key_endpoint_response_500 import PostAuthKeyEndpointResponse500
from ...models.post_auth_key_endpoint_response_503 import PostAuthKeyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostAuthKeyEndpointJsonBody | PostAuthKeyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/auth/key",
    }

    if isinstance(body, PostAuthKeyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostAuthKeyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostAuthKeyEndpointResponse400
    | PostAuthKeyEndpointResponse401
    | PostAuthKeyEndpointResponse403
    | PostAuthKeyEndpointResponse404
    | PostAuthKeyEndpointResponse405
    | PostAuthKeyEndpointResponse406
    | PostAuthKeyEndpointResponse409
    | PostAuthKeyEndpointResponse415
    | PostAuthKeyEndpointResponse422
    | PostAuthKeyEndpointResponse424
    | PostAuthKeyEndpointResponse500
    | PostAuthKeyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostAuthKeyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostAuthKeyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostAuthKeyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostAuthKeyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostAuthKeyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostAuthKeyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostAuthKeyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostAuthKeyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostAuthKeyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostAuthKeyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostAuthKeyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostAuthKeyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostAuthKeyEndpointResponse400
    | PostAuthKeyEndpointResponse401
    | PostAuthKeyEndpointResponse403
    | PostAuthKeyEndpointResponse404
    | PostAuthKeyEndpointResponse405
    | PostAuthKeyEndpointResponse406
    | PostAuthKeyEndpointResponse409
    | PostAuthKeyEndpointResponse415
    | PostAuthKeyEndpointResponse422
    | PostAuthKeyEndpointResponse424
    | PostAuthKeyEndpointResponse500
    | PostAuthKeyEndpointResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAuthKeyEndpointJsonBody | PostAuthKeyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostAuthKeyEndpointResponse400
    | PostAuthKeyEndpointResponse401
    | PostAuthKeyEndpointResponse403
    | PostAuthKeyEndpointResponse404
    | PostAuthKeyEndpointResponse405
    | PostAuthKeyEndpointResponse406
    | PostAuthKeyEndpointResponse409
    | PostAuthKeyEndpointResponse415
    | PostAuthKeyEndpointResponse422
    | PostAuthKeyEndpointResponse424
    | PostAuthKeyEndpointResponse500
    | PostAuthKeyEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new REST API Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-key-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostAuthKeyEndpointJsonBody | Unset):
        body (PostAuthKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAuthKeyEndpointResponse400 | PostAuthKeyEndpointResponse401 | PostAuthKeyEndpointResponse403 | PostAuthKeyEndpointResponse404 | PostAuthKeyEndpointResponse405 | PostAuthKeyEndpointResponse406 | PostAuthKeyEndpointResponse409 | PostAuthKeyEndpointResponse415 | PostAuthKeyEndpointResponse422 | PostAuthKeyEndpointResponse424 | PostAuthKeyEndpointResponse500 | PostAuthKeyEndpointResponse503]
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
    client: AuthenticatedClient,
    body: PostAuthKeyEndpointJsonBody | PostAuthKeyEndpointDataBody | Unset = UNSET,
) -> (
    PostAuthKeyEndpointResponse400
    | PostAuthKeyEndpointResponse401
    | PostAuthKeyEndpointResponse403
    | PostAuthKeyEndpointResponse404
    | PostAuthKeyEndpointResponse405
    | PostAuthKeyEndpointResponse406
    | PostAuthKeyEndpointResponse409
    | PostAuthKeyEndpointResponse415
    | PostAuthKeyEndpointResponse422
    | PostAuthKeyEndpointResponse424
    | PostAuthKeyEndpointResponse500
    | PostAuthKeyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new REST API Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-key-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostAuthKeyEndpointJsonBody | Unset):
        body (PostAuthKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAuthKeyEndpointResponse400 | PostAuthKeyEndpointResponse401 | PostAuthKeyEndpointResponse403 | PostAuthKeyEndpointResponse404 | PostAuthKeyEndpointResponse405 | PostAuthKeyEndpointResponse406 | PostAuthKeyEndpointResponse409 | PostAuthKeyEndpointResponse415 | PostAuthKeyEndpointResponse422 | PostAuthKeyEndpointResponse424 | PostAuthKeyEndpointResponse500 | PostAuthKeyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAuthKeyEndpointJsonBody | PostAuthKeyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostAuthKeyEndpointResponse400
    | PostAuthKeyEndpointResponse401
    | PostAuthKeyEndpointResponse403
    | PostAuthKeyEndpointResponse404
    | PostAuthKeyEndpointResponse405
    | PostAuthKeyEndpointResponse406
    | PostAuthKeyEndpointResponse409
    | PostAuthKeyEndpointResponse415
    | PostAuthKeyEndpointResponse422
    | PostAuthKeyEndpointResponse424
    | PostAuthKeyEndpointResponse500
    | PostAuthKeyEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new REST API Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-key-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostAuthKeyEndpointJsonBody | Unset):
        body (PostAuthKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAuthKeyEndpointResponse400 | PostAuthKeyEndpointResponse401 | PostAuthKeyEndpointResponse403 | PostAuthKeyEndpointResponse404 | PostAuthKeyEndpointResponse405 | PostAuthKeyEndpointResponse406 | PostAuthKeyEndpointResponse409 | PostAuthKeyEndpointResponse415 | PostAuthKeyEndpointResponse422 | PostAuthKeyEndpointResponse424 | PostAuthKeyEndpointResponse500 | PostAuthKeyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostAuthKeyEndpointJsonBody | PostAuthKeyEndpointDataBody | Unset = UNSET,
) -> (
    PostAuthKeyEndpointResponse400
    | PostAuthKeyEndpointResponse401
    | PostAuthKeyEndpointResponse403
    | PostAuthKeyEndpointResponse404
    | PostAuthKeyEndpointResponse405
    | PostAuthKeyEndpointResponse406
    | PostAuthKeyEndpointResponse409
    | PostAuthKeyEndpointResponse415
    | PostAuthKeyEndpointResponse422
    | PostAuthKeyEndpointResponse424
    | PostAuthKeyEndpointResponse500
    | PostAuthKeyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new REST API Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-key-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostAuthKeyEndpointJsonBody | Unset):
        body (PostAuthKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAuthKeyEndpointResponse400 | PostAuthKeyEndpointResponse401 | PostAuthKeyEndpointResponse403 | PostAuthKeyEndpointResponse404 | PostAuthKeyEndpointResponse405 | PostAuthKeyEndpointResponse406 | PostAuthKeyEndpointResponse409 | PostAuthKeyEndpointResponse415 | PostAuthKeyEndpointResponse422 | PostAuthKeyEndpointResponse424 | PostAuthKeyEndpointResponse500 | PostAuthKeyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
