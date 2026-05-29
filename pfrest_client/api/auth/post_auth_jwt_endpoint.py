from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_auth_jwt_endpoint_data_body import PostAuthJWTEndpointDataBody
from ...models.post_auth_jwt_endpoint_json_body import PostAuthJWTEndpointJsonBody
from ...models.post_auth_jwt_endpoint_response_400 import PostAuthJWTEndpointResponse400
from ...models.post_auth_jwt_endpoint_response_401 import PostAuthJWTEndpointResponse401
from ...models.post_auth_jwt_endpoint_response_403 import PostAuthJWTEndpointResponse403
from ...models.post_auth_jwt_endpoint_response_404 import PostAuthJWTEndpointResponse404
from ...models.post_auth_jwt_endpoint_response_405 import PostAuthJWTEndpointResponse405
from ...models.post_auth_jwt_endpoint_response_406 import PostAuthJWTEndpointResponse406
from ...models.post_auth_jwt_endpoint_response_409 import PostAuthJWTEndpointResponse409
from ...models.post_auth_jwt_endpoint_response_415 import PostAuthJWTEndpointResponse415
from ...models.post_auth_jwt_endpoint_response_422 import PostAuthJWTEndpointResponse422
from ...models.post_auth_jwt_endpoint_response_424 import PostAuthJWTEndpointResponse424
from ...models.post_auth_jwt_endpoint_response_500 import PostAuthJWTEndpointResponse500
from ...models.post_auth_jwt_endpoint_response_503 import PostAuthJWTEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostAuthJWTEndpointJsonBody | PostAuthJWTEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/auth/jwt",
    }

    if isinstance(body, PostAuthJWTEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostAuthJWTEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostAuthJWTEndpointResponse400
    | PostAuthJWTEndpointResponse401
    | PostAuthJWTEndpointResponse403
    | PostAuthJWTEndpointResponse404
    | PostAuthJWTEndpointResponse405
    | PostAuthJWTEndpointResponse406
    | PostAuthJWTEndpointResponse409
    | PostAuthJWTEndpointResponse415
    | PostAuthJWTEndpointResponse422
    | PostAuthJWTEndpointResponse424
    | PostAuthJWTEndpointResponse500
    | PostAuthJWTEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostAuthJWTEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostAuthJWTEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostAuthJWTEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostAuthJWTEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostAuthJWTEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostAuthJWTEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostAuthJWTEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostAuthJWTEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostAuthJWTEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostAuthJWTEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostAuthJWTEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostAuthJWTEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostAuthJWTEndpointResponse400
    | PostAuthJWTEndpointResponse401
    | PostAuthJWTEndpointResponse403
    | PostAuthJWTEndpointResponse404
    | PostAuthJWTEndpointResponse405
    | PostAuthJWTEndpointResponse406
    | PostAuthJWTEndpointResponse409
    | PostAuthJWTEndpointResponse415
    | PostAuthJWTEndpointResponse422
    | PostAuthJWTEndpointResponse424
    | PostAuthJWTEndpointResponse500
    | PostAuthJWTEndpointResponse503
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
    body: PostAuthJWTEndpointJsonBody | PostAuthJWTEndpointDataBody | Unset = UNSET,
) -> Response[
    PostAuthJWTEndpointResponse400
    | PostAuthJWTEndpointResponse401
    | PostAuthJWTEndpointResponse403
    | PostAuthJWTEndpointResponse404
    | PostAuthJWTEndpointResponse405
    | PostAuthJWTEndpointResponse406
    | PostAuthJWTEndpointResponse409
    | PostAuthJWTEndpointResponse415
    | PostAuthJWTEndpointResponse422
    | PostAuthJWTEndpointResponse424
    | PostAuthJWTEndpointResponse500
    | PostAuthJWTEndpointResponse503
]:
    """<h3>Description:</h3>Creates REST API JWT.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIJWT<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-jwt-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostAuthJWTEndpointJsonBody | Unset):
        body (PostAuthJWTEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAuthJWTEndpointResponse400 | PostAuthJWTEndpointResponse401 | PostAuthJWTEndpointResponse403 | PostAuthJWTEndpointResponse404 | PostAuthJWTEndpointResponse405 | PostAuthJWTEndpointResponse406 | PostAuthJWTEndpointResponse409 | PostAuthJWTEndpointResponse415 | PostAuthJWTEndpointResponse422 | PostAuthJWTEndpointResponse424 | PostAuthJWTEndpointResponse500 | PostAuthJWTEndpointResponse503]
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
    body: PostAuthJWTEndpointJsonBody | PostAuthJWTEndpointDataBody | Unset = UNSET,
) -> (
    PostAuthJWTEndpointResponse400
    | PostAuthJWTEndpointResponse401
    | PostAuthJWTEndpointResponse403
    | PostAuthJWTEndpointResponse404
    | PostAuthJWTEndpointResponse405
    | PostAuthJWTEndpointResponse406
    | PostAuthJWTEndpointResponse409
    | PostAuthJWTEndpointResponse415
    | PostAuthJWTEndpointResponse422
    | PostAuthJWTEndpointResponse424
    | PostAuthJWTEndpointResponse500
    | PostAuthJWTEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates REST API JWT.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIJWT<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-jwt-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostAuthJWTEndpointJsonBody | Unset):
        body (PostAuthJWTEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAuthJWTEndpointResponse400 | PostAuthJWTEndpointResponse401 | PostAuthJWTEndpointResponse403 | PostAuthJWTEndpointResponse404 | PostAuthJWTEndpointResponse405 | PostAuthJWTEndpointResponse406 | PostAuthJWTEndpointResponse409 | PostAuthJWTEndpointResponse415 | PostAuthJWTEndpointResponse422 | PostAuthJWTEndpointResponse424 | PostAuthJWTEndpointResponse500 | PostAuthJWTEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAuthJWTEndpointJsonBody | PostAuthJWTEndpointDataBody | Unset = UNSET,
) -> Response[
    PostAuthJWTEndpointResponse400
    | PostAuthJWTEndpointResponse401
    | PostAuthJWTEndpointResponse403
    | PostAuthJWTEndpointResponse404
    | PostAuthJWTEndpointResponse405
    | PostAuthJWTEndpointResponse406
    | PostAuthJWTEndpointResponse409
    | PostAuthJWTEndpointResponse415
    | PostAuthJWTEndpointResponse422
    | PostAuthJWTEndpointResponse424
    | PostAuthJWTEndpointResponse500
    | PostAuthJWTEndpointResponse503
]:
    """<h3>Description:</h3>Creates REST API JWT.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIJWT<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-jwt-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostAuthJWTEndpointJsonBody | Unset):
        body (PostAuthJWTEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAuthJWTEndpointResponse400 | PostAuthJWTEndpointResponse401 | PostAuthJWTEndpointResponse403 | PostAuthJWTEndpointResponse404 | PostAuthJWTEndpointResponse405 | PostAuthJWTEndpointResponse406 | PostAuthJWTEndpointResponse409 | PostAuthJWTEndpointResponse415 | PostAuthJWTEndpointResponse422 | PostAuthJWTEndpointResponse424 | PostAuthJWTEndpointResponse500 | PostAuthJWTEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostAuthJWTEndpointJsonBody | PostAuthJWTEndpointDataBody | Unset = UNSET,
) -> (
    PostAuthJWTEndpointResponse400
    | PostAuthJWTEndpointResponse401
    | PostAuthJWTEndpointResponse403
    | PostAuthJWTEndpointResponse404
    | PostAuthJWTEndpointResponse405
    | PostAuthJWTEndpointResponse406
    | PostAuthJWTEndpointResponse409
    | PostAuthJWTEndpointResponse415
    | PostAuthJWTEndpointResponse422
    | PostAuthJWTEndpointResponse424
    | PostAuthJWTEndpointResponse500
    | PostAuthJWTEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates REST API JWT.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIJWT<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-auth-jwt-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostAuthJWTEndpointJsonBody | Unset):
        body (PostAuthJWTEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAuthJWTEndpointResponse400 | PostAuthJWTEndpointResponse401 | PostAuthJWTEndpointResponse403 | PostAuthJWTEndpointResponse404 | PostAuthJWTEndpointResponse405 | PostAuthJWTEndpointResponse406 | PostAuthJWTEndpointResponse409 | PostAuthJWTEndpointResponse415 | PostAuthJWTEndpointResponse422 | PostAuthJWTEndpointResponse424 | PostAuthJWTEndpointResponse500 | PostAuthJWTEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
