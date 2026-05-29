from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_interface_group_endpoint_data_body import PostInterfaceGroupEndpointDataBody
from ...models.post_interface_group_endpoint_json_body import PostInterfaceGroupEndpointJsonBody
from ...models.post_interface_group_endpoint_response_400 import PostInterfaceGroupEndpointResponse400
from ...models.post_interface_group_endpoint_response_401 import PostInterfaceGroupEndpointResponse401
from ...models.post_interface_group_endpoint_response_403 import PostInterfaceGroupEndpointResponse403
from ...models.post_interface_group_endpoint_response_404 import PostInterfaceGroupEndpointResponse404
from ...models.post_interface_group_endpoint_response_405 import PostInterfaceGroupEndpointResponse405
from ...models.post_interface_group_endpoint_response_406 import PostInterfaceGroupEndpointResponse406
from ...models.post_interface_group_endpoint_response_409 import PostInterfaceGroupEndpointResponse409
from ...models.post_interface_group_endpoint_response_415 import PostInterfaceGroupEndpointResponse415
from ...models.post_interface_group_endpoint_response_422 import PostInterfaceGroupEndpointResponse422
from ...models.post_interface_group_endpoint_response_424 import PostInterfaceGroupEndpointResponse424
from ...models.post_interface_group_endpoint_response_500 import PostInterfaceGroupEndpointResponse500
from ...models.post_interface_group_endpoint_response_503 import PostInterfaceGroupEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostInterfaceGroupEndpointJsonBody | PostInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/interface/group",
    }

    if isinstance(body, PostInterfaceGroupEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostInterfaceGroupEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostInterfaceGroupEndpointResponse400
    | PostInterfaceGroupEndpointResponse401
    | PostInterfaceGroupEndpointResponse403
    | PostInterfaceGroupEndpointResponse404
    | PostInterfaceGroupEndpointResponse405
    | PostInterfaceGroupEndpointResponse406
    | PostInterfaceGroupEndpointResponse409
    | PostInterfaceGroupEndpointResponse415
    | PostInterfaceGroupEndpointResponse422
    | PostInterfaceGroupEndpointResponse424
    | PostInterfaceGroupEndpointResponse500
    | PostInterfaceGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostInterfaceGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostInterfaceGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostInterfaceGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostInterfaceGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostInterfaceGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostInterfaceGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostInterfaceGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostInterfaceGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostInterfaceGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostInterfaceGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostInterfaceGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostInterfaceGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostInterfaceGroupEndpointResponse400
    | PostInterfaceGroupEndpointResponse401
    | PostInterfaceGroupEndpointResponse403
    | PostInterfaceGroupEndpointResponse404
    | PostInterfaceGroupEndpointResponse405
    | PostInterfaceGroupEndpointResponse406
    | PostInterfaceGroupEndpointResponse409
    | PostInterfaceGroupEndpointResponse415
    | PostInterfaceGroupEndpointResponse422
    | PostInterfaceGroupEndpointResponse424
    | PostInterfaceGroupEndpointResponse500
    | PostInterfaceGroupEndpointResponse503
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
    body: PostInterfaceGroupEndpointJsonBody | PostInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceGroupEndpointResponse400
    | PostInterfaceGroupEndpointResponse401
    | PostInterfaceGroupEndpointResponse403
    | PostInterfaceGroupEndpointResponse404
    | PostInterfaceGroupEndpointResponse405
    | PostInterfaceGroupEndpointResponse406
    | PostInterfaceGroupEndpointResponse409
    | PostInterfaceGroupEndpointResponse415
    | PostInterfaceGroupEndpointResponse422
    | PostInterfaceGroupEndpointResponse424
    | PostInterfaceGroupEndpointResponse500
    | PostInterfaceGroupEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceGroupEndpointJsonBody | Unset):
        body (PostInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceGroupEndpointResponse400 | PostInterfaceGroupEndpointResponse401 | PostInterfaceGroupEndpointResponse403 | PostInterfaceGroupEndpointResponse404 | PostInterfaceGroupEndpointResponse405 | PostInterfaceGroupEndpointResponse406 | PostInterfaceGroupEndpointResponse409 | PostInterfaceGroupEndpointResponse415 | PostInterfaceGroupEndpointResponse422 | PostInterfaceGroupEndpointResponse424 | PostInterfaceGroupEndpointResponse500 | PostInterfaceGroupEndpointResponse503]
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
    body: PostInterfaceGroupEndpointJsonBody | PostInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceGroupEndpointResponse400
    | PostInterfaceGroupEndpointResponse401
    | PostInterfaceGroupEndpointResponse403
    | PostInterfaceGroupEndpointResponse404
    | PostInterfaceGroupEndpointResponse405
    | PostInterfaceGroupEndpointResponse406
    | PostInterfaceGroupEndpointResponse409
    | PostInterfaceGroupEndpointResponse415
    | PostInterfaceGroupEndpointResponse422
    | PostInterfaceGroupEndpointResponse424
    | PostInterfaceGroupEndpointResponse500
    | PostInterfaceGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceGroupEndpointJsonBody | Unset):
        body (PostInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceGroupEndpointResponse400 | PostInterfaceGroupEndpointResponse401 | PostInterfaceGroupEndpointResponse403 | PostInterfaceGroupEndpointResponse404 | PostInterfaceGroupEndpointResponse405 | PostInterfaceGroupEndpointResponse406 | PostInterfaceGroupEndpointResponse409 | PostInterfaceGroupEndpointResponse415 | PostInterfaceGroupEndpointResponse422 | PostInterfaceGroupEndpointResponse424 | PostInterfaceGroupEndpointResponse500 | PostInterfaceGroupEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceGroupEndpointJsonBody | PostInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceGroupEndpointResponse400
    | PostInterfaceGroupEndpointResponse401
    | PostInterfaceGroupEndpointResponse403
    | PostInterfaceGroupEndpointResponse404
    | PostInterfaceGroupEndpointResponse405
    | PostInterfaceGroupEndpointResponse406
    | PostInterfaceGroupEndpointResponse409
    | PostInterfaceGroupEndpointResponse415
    | PostInterfaceGroupEndpointResponse422
    | PostInterfaceGroupEndpointResponse424
    | PostInterfaceGroupEndpointResponse500
    | PostInterfaceGroupEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceGroupEndpointJsonBody | Unset):
        body (PostInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceGroupEndpointResponse400 | PostInterfaceGroupEndpointResponse401 | PostInterfaceGroupEndpointResponse403 | PostInterfaceGroupEndpointResponse404 | PostInterfaceGroupEndpointResponse405 | PostInterfaceGroupEndpointResponse406 | PostInterfaceGroupEndpointResponse409 | PostInterfaceGroupEndpointResponse415 | PostInterfaceGroupEndpointResponse422 | PostInterfaceGroupEndpointResponse424 | PostInterfaceGroupEndpointResponse500 | PostInterfaceGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceGroupEndpointJsonBody | PostInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceGroupEndpointResponse400
    | PostInterfaceGroupEndpointResponse401
    | PostInterfaceGroupEndpointResponse403
    | PostInterfaceGroupEndpointResponse404
    | PostInterfaceGroupEndpointResponse405
    | PostInterfaceGroupEndpointResponse406
    | PostInterfaceGroupEndpointResponse409
    | PostInterfaceGroupEndpointResponse415
    | PostInterfaceGroupEndpointResponse422
    | PostInterfaceGroupEndpointResponse424
    | PostInterfaceGroupEndpointResponse500
    | PostInterfaceGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceGroupEndpointJsonBody | Unset):
        body (PostInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceGroupEndpointResponse400 | PostInterfaceGroupEndpointResponse401 | PostInterfaceGroupEndpointResponse403 | PostInterfaceGroupEndpointResponse404 | PostInterfaceGroupEndpointResponse405 | PostInterfaceGroupEndpointResponse406 | PostInterfaceGroupEndpointResponse409 | PostInterfaceGroupEndpointResponse415 | PostInterfaceGroupEndpointResponse422 | PostInterfaceGroupEndpointResponse424 | PostInterfaceGroupEndpointResponse500 | PostInterfaceGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
