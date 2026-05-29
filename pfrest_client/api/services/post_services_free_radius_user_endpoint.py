from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_free_radius_user_endpoint_data_body import PostServicesFreeRADIUSUserEndpointDataBody
from ...models.post_services_free_radius_user_endpoint_json_body import PostServicesFreeRADIUSUserEndpointJsonBody
from ...models.post_services_free_radius_user_endpoint_response_400 import PostServicesFreeRADIUSUserEndpointResponse400
from ...models.post_services_free_radius_user_endpoint_response_401 import PostServicesFreeRADIUSUserEndpointResponse401
from ...models.post_services_free_radius_user_endpoint_response_403 import PostServicesFreeRADIUSUserEndpointResponse403
from ...models.post_services_free_radius_user_endpoint_response_404 import PostServicesFreeRADIUSUserEndpointResponse404
from ...models.post_services_free_radius_user_endpoint_response_405 import PostServicesFreeRADIUSUserEndpointResponse405
from ...models.post_services_free_radius_user_endpoint_response_406 import PostServicesFreeRADIUSUserEndpointResponse406
from ...models.post_services_free_radius_user_endpoint_response_409 import PostServicesFreeRADIUSUserEndpointResponse409
from ...models.post_services_free_radius_user_endpoint_response_415 import PostServicesFreeRADIUSUserEndpointResponse415
from ...models.post_services_free_radius_user_endpoint_response_422 import PostServicesFreeRADIUSUserEndpointResponse422
from ...models.post_services_free_radius_user_endpoint_response_424 import PostServicesFreeRADIUSUserEndpointResponse424
from ...models.post_services_free_radius_user_endpoint_response_500 import PostServicesFreeRADIUSUserEndpointResponse500
from ...models.post_services_free_radius_user_endpoint_response_503 import PostServicesFreeRADIUSUserEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesFreeRADIUSUserEndpointJsonBody | PostServicesFreeRADIUSUserEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/freeradius/user",
    }

    if isinstance(body, PostServicesFreeRADIUSUserEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesFreeRADIUSUserEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesFreeRADIUSUserEndpointResponse400
    | PostServicesFreeRADIUSUserEndpointResponse401
    | PostServicesFreeRADIUSUserEndpointResponse403
    | PostServicesFreeRADIUSUserEndpointResponse404
    | PostServicesFreeRADIUSUserEndpointResponse405
    | PostServicesFreeRADIUSUserEndpointResponse406
    | PostServicesFreeRADIUSUserEndpointResponse409
    | PostServicesFreeRADIUSUserEndpointResponse415
    | PostServicesFreeRADIUSUserEndpointResponse422
    | PostServicesFreeRADIUSUserEndpointResponse424
    | PostServicesFreeRADIUSUserEndpointResponse500
    | PostServicesFreeRADIUSUserEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesFreeRADIUSUserEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesFreeRADIUSUserEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesFreeRADIUSUserEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesFreeRADIUSUserEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesFreeRADIUSUserEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesFreeRADIUSUserEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesFreeRADIUSUserEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesFreeRADIUSUserEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesFreeRADIUSUserEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesFreeRADIUSUserEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesFreeRADIUSUserEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesFreeRADIUSUserEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesFreeRADIUSUserEndpointResponse400
    | PostServicesFreeRADIUSUserEndpointResponse401
    | PostServicesFreeRADIUSUserEndpointResponse403
    | PostServicesFreeRADIUSUserEndpointResponse404
    | PostServicesFreeRADIUSUserEndpointResponse405
    | PostServicesFreeRADIUSUserEndpointResponse406
    | PostServicesFreeRADIUSUserEndpointResponse409
    | PostServicesFreeRADIUSUserEndpointResponse415
    | PostServicesFreeRADIUSUserEndpointResponse422
    | PostServicesFreeRADIUSUserEndpointResponse424
    | PostServicesFreeRADIUSUserEndpointResponse500
    | PostServicesFreeRADIUSUserEndpointResponse503
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
    body: PostServicesFreeRADIUSUserEndpointJsonBody | PostServicesFreeRADIUSUserEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSUserEndpointResponse400
    | PostServicesFreeRADIUSUserEndpointResponse401
    | PostServicesFreeRADIUSUserEndpointResponse403
    | PostServicesFreeRADIUSUserEndpointResponse404
    | PostServicesFreeRADIUSUserEndpointResponse405
    | PostServicesFreeRADIUSUserEndpointResponse406
    | PostServicesFreeRADIUSUserEndpointResponse409
    | PostServicesFreeRADIUSUserEndpointResponse415
    | PostServicesFreeRADIUSUserEndpointResponse422
    | PostServicesFreeRADIUSUserEndpointResponse424
    | PostServicesFreeRADIUSUserEndpointResponse500
    | PostServicesFreeRADIUSUserEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-user-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSUserEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSUserEndpointResponse400 | PostServicesFreeRADIUSUserEndpointResponse401 | PostServicesFreeRADIUSUserEndpointResponse403 | PostServicesFreeRADIUSUserEndpointResponse404 | PostServicesFreeRADIUSUserEndpointResponse405 | PostServicesFreeRADIUSUserEndpointResponse406 | PostServicesFreeRADIUSUserEndpointResponse409 | PostServicesFreeRADIUSUserEndpointResponse415 | PostServicesFreeRADIUSUserEndpointResponse422 | PostServicesFreeRADIUSUserEndpointResponse424 | PostServicesFreeRADIUSUserEndpointResponse500 | PostServicesFreeRADIUSUserEndpointResponse503]
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
    body: PostServicesFreeRADIUSUserEndpointJsonBody | PostServicesFreeRADIUSUserEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSUserEndpointResponse400
    | PostServicesFreeRADIUSUserEndpointResponse401
    | PostServicesFreeRADIUSUserEndpointResponse403
    | PostServicesFreeRADIUSUserEndpointResponse404
    | PostServicesFreeRADIUSUserEndpointResponse405
    | PostServicesFreeRADIUSUserEndpointResponse406
    | PostServicesFreeRADIUSUserEndpointResponse409
    | PostServicesFreeRADIUSUserEndpointResponse415
    | PostServicesFreeRADIUSUserEndpointResponse422
    | PostServicesFreeRADIUSUserEndpointResponse424
    | PostServicesFreeRADIUSUserEndpointResponse500
    | PostServicesFreeRADIUSUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-user-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSUserEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSUserEndpointResponse400 | PostServicesFreeRADIUSUserEndpointResponse401 | PostServicesFreeRADIUSUserEndpointResponse403 | PostServicesFreeRADIUSUserEndpointResponse404 | PostServicesFreeRADIUSUserEndpointResponse405 | PostServicesFreeRADIUSUserEndpointResponse406 | PostServicesFreeRADIUSUserEndpointResponse409 | PostServicesFreeRADIUSUserEndpointResponse415 | PostServicesFreeRADIUSUserEndpointResponse422 | PostServicesFreeRADIUSUserEndpointResponse424 | PostServicesFreeRADIUSUserEndpointResponse500 | PostServicesFreeRADIUSUserEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSUserEndpointJsonBody | PostServicesFreeRADIUSUserEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSUserEndpointResponse400
    | PostServicesFreeRADIUSUserEndpointResponse401
    | PostServicesFreeRADIUSUserEndpointResponse403
    | PostServicesFreeRADIUSUserEndpointResponse404
    | PostServicesFreeRADIUSUserEndpointResponse405
    | PostServicesFreeRADIUSUserEndpointResponse406
    | PostServicesFreeRADIUSUserEndpointResponse409
    | PostServicesFreeRADIUSUserEndpointResponse415
    | PostServicesFreeRADIUSUserEndpointResponse422
    | PostServicesFreeRADIUSUserEndpointResponse424
    | PostServicesFreeRADIUSUserEndpointResponse500
    | PostServicesFreeRADIUSUserEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-user-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSUserEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSUserEndpointResponse400 | PostServicesFreeRADIUSUserEndpointResponse401 | PostServicesFreeRADIUSUserEndpointResponse403 | PostServicesFreeRADIUSUserEndpointResponse404 | PostServicesFreeRADIUSUserEndpointResponse405 | PostServicesFreeRADIUSUserEndpointResponse406 | PostServicesFreeRADIUSUserEndpointResponse409 | PostServicesFreeRADIUSUserEndpointResponse415 | PostServicesFreeRADIUSUserEndpointResponse422 | PostServicesFreeRADIUSUserEndpointResponse424 | PostServicesFreeRADIUSUserEndpointResponse500 | PostServicesFreeRADIUSUserEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSUserEndpointJsonBody | PostServicesFreeRADIUSUserEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSUserEndpointResponse400
    | PostServicesFreeRADIUSUserEndpointResponse401
    | PostServicesFreeRADIUSUserEndpointResponse403
    | PostServicesFreeRADIUSUserEndpointResponse404
    | PostServicesFreeRADIUSUserEndpointResponse405
    | PostServicesFreeRADIUSUserEndpointResponse406
    | PostServicesFreeRADIUSUserEndpointResponse409
    | PostServicesFreeRADIUSUserEndpointResponse415
    | PostServicesFreeRADIUSUserEndpointResponse422
    | PostServicesFreeRADIUSUserEndpointResponse424
    | PostServicesFreeRADIUSUserEndpointResponse500
    | PostServicesFreeRADIUSUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-user-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSUserEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSUserEndpointResponse400 | PostServicesFreeRADIUSUserEndpointResponse401 | PostServicesFreeRADIUSUserEndpointResponse403 | PostServicesFreeRADIUSUserEndpointResponse404 | PostServicesFreeRADIUSUserEndpointResponse405 | PostServicesFreeRADIUSUserEndpointResponse406 | PostServicesFreeRADIUSUserEndpointResponse409 | PostServicesFreeRADIUSUserEndpointResponse415 | PostServicesFreeRADIUSUserEndpointResponse422 | PostServicesFreeRADIUSUserEndpointResponse424 | PostServicesFreeRADIUSUserEndpointResponse500 | PostServicesFreeRADIUSUserEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
