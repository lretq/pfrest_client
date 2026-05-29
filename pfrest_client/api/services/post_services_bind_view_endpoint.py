from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_bind_view_endpoint_data_body import PostServicesBINDViewEndpointDataBody
from ...models.post_services_bind_view_endpoint_json_body import PostServicesBINDViewEndpointJsonBody
from ...models.post_services_bind_view_endpoint_response_400 import PostServicesBINDViewEndpointResponse400
from ...models.post_services_bind_view_endpoint_response_401 import PostServicesBINDViewEndpointResponse401
from ...models.post_services_bind_view_endpoint_response_403 import PostServicesBINDViewEndpointResponse403
from ...models.post_services_bind_view_endpoint_response_404 import PostServicesBINDViewEndpointResponse404
from ...models.post_services_bind_view_endpoint_response_405 import PostServicesBINDViewEndpointResponse405
from ...models.post_services_bind_view_endpoint_response_406 import PostServicesBINDViewEndpointResponse406
from ...models.post_services_bind_view_endpoint_response_409 import PostServicesBINDViewEndpointResponse409
from ...models.post_services_bind_view_endpoint_response_415 import PostServicesBINDViewEndpointResponse415
from ...models.post_services_bind_view_endpoint_response_422 import PostServicesBINDViewEndpointResponse422
from ...models.post_services_bind_view_endpoint_response_424 import PostServicesBINDViewEndpointResponse424
from ...models.post_services_bind_view_endpoint_response_500 import PostServicesBINDViewEndpointResponse500
from ...models.post_services_bind_view_endpoint_response_503 import PostServicesBINDViewEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesBINDViewEndpointJsonBody | PostServicesBINDViewEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/bind/view",
    }

    if isinstance(body, PostServicesBINDViewEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesBINDViewEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesBINDViewEndpointResponse400
    | PostServicesBINDViewEndpointResponse401
    | PostServicesBINDViewEndpointResponse403
    | PostServicesBINDViewEndpointResponse404
    | PostServicesBINDViewEndpointResponse405
    | PostServicesBINDViewEndpointResponse406
    | PostServicesBINDViewEndpointResponse409
    | PostServicesBINDViewEndpointResponse415
    | PostServicesBINDViewEndpointResponse422
    | PostServicesBINDViewEndpointResponse424
    | PostServicesBINDViewEndpointResponse500
    | PostServicesBINDViewEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesBINDViewEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesBINDViewEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesBINDViewEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesBINDViewEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesBINDViewEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesBINDViewEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesBINDViewEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesBINDViewEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesBINDViewEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesBINDViewEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesBINDViewEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesBINDViewEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesBINDViewEndpointResponse400
    | PostServicesBINDViewEndpointResponse401
    | PostServicesBINDViewEndpointResponse403
    | PostServicesBINDViewEndpointResponse404
    | PostServicesBINDViewEndpointResponse405
    | PostServicesBINDViewEndpointResponse406
    | PostServicesBINDViewEndpointResponse409
    | PostServicesBINDViewEndpointResponse415
    | PostServicesBINDViewEndpointResponse422
    | PostServicesBINDViewEndpointResponse424
    | PostServicesBINDViewEndpointResponse500
    | PostServicesBINDViewEndpointResponse503
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
    body: PostServicesBINDViewEndpointJsonBody | PostServicesBINDViewEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesBINDViewEndpointResponse400
    | PostServicesBINDViewEndpointResponse401
    | PostServicesBINDViewEndpointResponse403
    | PostServicesBINDViewEndpointResponse404
    | PostServicesBINDViewEndpointResponse405
    | PostServicesBINDViewEndpointResponse406
    | PostServicesBINDViewEndpointResponse409
    | PostServicesBINDViewEndpointResponse415
    | PostServicesBINDViewEndpointResponse422
    | PostServicesBINDViewEndpointResponse424
    | PostServicesBINDViewEndpointResponse500
    | PostServicesBINDViewEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new BIND View.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-view-post ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDViewEndpointJsonBody | Unset):
        body (PostServicesBINDViewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesBINDViewEndpointResponse400 | PostServicesBINDViewEndpointResponse401 | PostServicesBINDViewEndpointResponse403 | PostServicesBINDViewEndpointResponse404 | PostServicesBINDViewEndpointResponse405 | PostServicesBINDViewEndpointResponse406 | PostServicesBINDViewEndpointResponse409 | PostServicesBINDViewEndpointResponse415 | PostServicesBINDViewEndpointResponse422 | PostServicesBINDViewEndpointResponse424 | PostServicesBINDViewEndpointResponse500 | PostServicesBINDViewEndpointResponse503]
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
    body: PostServicesBINDViewEndpointJsonBody | PostServicesBINDViewEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesBINDViewEndpointResponse400
    | PostServicesBINDViewEndpointResponse401
    | PostServicesBINDViewEndpointResponse403
    | PostServicesBINDViewEndpointResponse404
    | PostServicesBINDViewEndpointResponse405
    | PostServicesBINDViewEndpointResponse406
    | PostServicesBINDViewEndpointResponse409
    | PostServicesBINDViewEndpointResponse415
    | PostServicesBINDViewEndpointResponse422
    | PostServicesBINDViewEndpointResponse424
    | PostServicesBINDViewEndpointResponse500
    | PostServicesBINDViewEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new BIND View.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-view-post ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDViewEndpointJsonBody | Unset):
        body (PostServicesBINDViewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesBINDViewEndpointResponse400 | PostServicesBINDViewEndpointResponse401 | PostServicesBINDViewEndpointResponse403 | PostServicesBINDViewEndpointResponse404 | PostServicesBINDViewEndpointResponse405 | PostServicesBINDViewEndpointResponse406 | PostServicesBINDViewEndpointResponse409 | PostServicesBINDViewEndpointResponse415 | PostServicesBINDViewEndpointResponse422 | PostServicesBINDViewEndpointResponse424 | PostServicesBINDViewEndpointResponse500 | PostServicesBINDViewEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesBINDViewEndpointJsonBody | PostServicesBINDViewEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesBINDViewEndpointResponse400
    | PostServicesBINDViewEndpointResponse401
    | PostServicesBINDViewEndpointResponse403
    | PostServicesBINDViewEndpointResponse404
    | PostServicesBINDViewEndpointResponse405
    | PostServicesBINDViewEndpointResponse406
    | PostServicesBINDViewEndpointResponse409
    | PostServicesBINDViewEndpointResponse415
    | PostServicesBINDViewEndpointResponse422
    | PostServicesBINDViewEndpointResponse424
    | PostServicesBINDViewEndpointResponse500
    | PostServicesBINDViewEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new BIND View.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-view-post ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDViewEndpointJsonBody | Unset):
        body (PostServicesBINDViewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesBINDViewEndpointResponse400 | PostServicesBINDViewEndpointResponse401 | PostServicesBINDViewEndpointResponse403 | PostServicesBINDViewEndpointResponse404 | PostServicesBINDViewEndpointResponse405 | PostServicesBINDViewEndpointResponse406 | PostServicesBINDViewEndpointResponse409 | PostServicesBINDViewEndpointResponse415 | PostServicesBINDViewEndpointResponse422 | PostServicesBINDViewEndpointResponse424 | PostServicesBINDViewEndpointResponse500 | PostServicesBINDViewEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesBINDViewEndpointJsonBody | PostServicesBINDViewEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesBINDViewEndpointResponse400
    | PostServicesBINDViewEndpointResponse401
    | PostServicesBINDViewEndpointResponse403
    | PostServicesBINDViewEndpointResponse404
    | PostServicesBINDViewEndpointResponse405
    | PostServicesBINDViewEndpointResponse406
    | PostServicesBINDViewEndpointResponse409
    | PostServicesBINDViewEndpointResponse415
    | PostServicesBINDViewEndpointResponse422
    | PostServicesBINDViewEndpointResponse424
    | PostServicesBINDViewEndpointResponse500
    | PostServicesBINDViewEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new BIND View.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-view-post ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDViewEndpointJsonBody | Unset):
        body (PostServicesBINDViewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesBINDViewEndpointResponse400 | PostServicesBINDViewEndpointResponse401 | PostServicesBINDViewEndpointResponse403 | PostServicesBINDViewEndpointResponse404 | PostServicesBINDViewEndpointResponse405 | PostServicesBINDViewEndpointResponse406 | PostServicesBINDViewEndpointResponse409 | PostServicesBINDViewEndpointResponse415 | PostServicesBINDViewEndpointResponse422 | PostServicesBINDViewEndpointResponse424 | PostServicesBINDViewEndpointResponse500 | PostServicesBINDViewEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
