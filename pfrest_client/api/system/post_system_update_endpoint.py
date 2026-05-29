from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_update_endpoint_data_body import PostSystemUpdateEndpointDataBody
from ...models.post_system_update_endpoint_json_body import PostSystemUpdateEndpointJsonBody
from ...models.post_system_update_endpoint_response_400 import PostSystemUpdateEndpointResponse400
from ...models.post_system_update_endpoint_response_401 import PostSystemUpdateEndpointResponse401
from ...models.post_system_update_endpoint_response_403 import PostSystemUpdateEndpointResponse403
from ...models.post_system_update_endpoint_response_404 import PostSystemUpdateEndpointResponse404
from ...models.post_system_update_endpoint_response_405 import PostSystemUpdateEndpointResponse405
from ...models.post_system_update_endpoint_response_406 import PostSystemUpdateEndpointResponse406
from ...models.post_system_update_endpoint_response_409 import PostSystemUpdateEndpointResponse409
from ...models.post_system_update_endpoint_response_415 import PostSystemUpdateEndpointResponse415
from ...models.post_system_update_endpoint_response_422 import PostSystemUpdateEndpointResponse422
from ...models.post_system_update_endpoint_response_424 import PostSystemUpdateEndpointResponse424
from ...models.post_system_update_endpoint_response_500 import PostSystemUpdateEndpointResponse500
from ...models.post_system_update_endpoint_response_503 import PostSystemUpdateEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemUpdateEndpointJsonBody | PostSystemUpdateEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/update",
    }

    if isinstance(body, PostSystemUpdateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemUpdateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemUpdateEndpointResponse400
    | PostSystemUpdateEndpointResponse401
    | PostSystemUpdateEndpointResponse403
    | PostSystemUpdateEndpointResponse404
    | PostSystemUpdateEndpointResponse405
    | PostSystemUpdateEndpointResponse406
    | PostSystemUpdateEndpointResponse409
    | PostSystemUpdateEndpointResponse415
    | PostSystemUpdateEndpointResponse422
    | PostSystemUpdateEndpointResponse424
    | PostSystemUpdateEndpointResponse500
    | PostSystemUpdateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemUpdateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemUpdateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemUpdateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemUpdateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemUpdateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemUpdateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemUpdateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemUpdateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemUpdateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemUpdateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemUpdateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemUpdateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemUpdateEndpointResponse400
    | PostSystemUpdateEndpointResponse401
    | PostSystemUpdateEndpointResponse403
    | PostSystemUpdateEndpointResponse404
    | PostSystemUpdateEndpointResponse405
    | PostSystemUpdateEndpointResponse406
    | PostSystemUpdateEndpointResponse409
    | PostSystemUpdateEndpointResponse415
    | PostSystemUpdateEndpointResponse422
    | PostSystemUpdateEndpointResponse424
    | PostSystemUpdateEndpointResponse500
    | PostSystemUpdateEndpointResponse503
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
    body: PostSystemUpdateEndpointJsonBody | PostSystemUpdateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemUpdateEndpointResponse400
    | PostSystemUpdateEndpointResponse401
    | PostSystemUpdateEndpointResponse403
    | PostSystemUpdateEndpointResponse404
    | PostSystemUpdateEndpointResponse405
    | PostSystemUpdateEndpointResponse406
    | PostSystemUpdateEndpointResponse409
    | PostSystemUpdateEndpointResponse415
    | PostSystemUpdateEndpointResponse422
    | PostSystemUpdateEndpointResponse424
    | PostSystemUpdateEndpointResponse500
    | PostSystemUpdateEndpointResponse503
]:
    """<h3>Description:</h3>Initiates a pfSense update process.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemUpdate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-update-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemUpdateEndpointJsonBody | Unset):
        body (PostSystemUpdateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemUpdateEndpointResponse400 | PostSystemUpdateEndpointResponse401 | PostSystemUpdateEndpointResponse403 | PostSystemUpdateEndpointResponse404 | PostSystemUpdateEndpointResponse405 | PostSystemUpdateEndpointResponse406 | PostSystemUpdateEndpointResponse409 | PostSystemUpdateEndpointResponse415 | PostSystemUpdateEndpointResponse422 | PostSystemUpdateEndpointResponse424 | PostSystemUpdateEndpointResponse500 | PostSystemUpdateEndpointResponse503]
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
    body: PostSystemUpdateEndpointJsonBody | PostSystemUpdateEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemUpdateEndpointResponse400
    | PostSystemUpdateEndpointResponse401
    | PostSystemUpdateEndpointResponse403
    | PostSystemUpdateEndpointResponse404
    | PostSystemUpdateEndpointResponse405
    | PostSystemUpdateEndpointResponse406
    | PostSystemUpdateEndpointResponse409
    | PostSystemUpdateEndpointResponse415
    | PostSystemUpdateEndpointResponse422
    | PostSystemUpdateEndpointResponse424
    | PostSystemUpdateEndpointResponse500
    | PostSystemUpdateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Initiates a pfSense update process.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemUpdate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-update-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemUpdateEndpointJsonBody | Unset):
        body (PostSystemUpdateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemUpdateEndpointResponse400 | PostSystemUpdateEndpointResponse401 | PostSystemUpdateEndpointResponse403 | PostSystemUpdateEndpointResponse404 | PostSystemUpdateEndpointResponse405 | PostSystemUpdateEndpointResponse406 | PostSystemUpdateEndpointResponse409 | PostSystemUpdateEndpointResponse415 | PostSystemUpdateEndpointResponse422 | PostSystemUpdateEndpointResponse424 | PostSystemUpdateEndpointResponse500 | PostSystemUpdateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemUpdateEndpointJsonBody | PostSystemUpdateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemUpdateEndpointResponse400
    | PostSystemUpdateEndpointResponse401
    | PostSystemUpdateEndpointResponse403
    | PostSystemUpdateEndpointResponse404
    | PostSystemUpdateEndpointResponse405
    | PostSystemUpdateEndpointResponse406
    | PostSystemUpdateEndpointResponse409
    | PostSystemUpdateEndpointResponse415
    | PostSystemUpdateEndpointResponse422
    | PostSystemUpdateEndpointResponse424
    | PostSystemUpdateEndpointResponse500
    | PostSystemUpdateEndpointResponse503
]:
    """<h3>Description:</h3>Initiates a pfSense update process.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemUpdate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-update-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemUpdateEndpointJsonBody | Unset):
        body (PostSystemUpdateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemUpdateEndpointResponse400 | PostSystemUpdateEndpointResponse401 | PostSystemUpdateEndpointResponse403 | PostSystemUpdateEndpointResponse404 | PostSystemUpdateEndpointResponse405 | PostSystemUpdateEndpointResponse406 | PostSystemUpdateEndpointResponse409 | PostSystemUpdateEndpointResponse415 | PostSystemUpdateEndpointResponse422 | PostSystemUpdateEndpointResponse424 | PostSystemUpdateEndpointResponse500 | PostSystemUpdateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemUpdateEndpointJsonBody | PostSystemUpdateEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemUpdateEndpointResponse400
    | PostSystemUpdateEndpointResponse401
    | PostSystemUpdateEndpointResponse403
    | PostSystemUpdateEndpointResponse404
    | PostSystemUpdateEndpointResponse405
    | PostSystemUpdateEndpointResponse406
    | PostSystemUpdateEndpointResponse409
    | PostSystemUpdateEndpointResponse415
    | PostSystemUpdateEndpointResponse422
    | PostSystemUpdateEndpointResponse424
    | PostSystemUpdateEndpointResponse500
    | PostSystemUpdateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Initiates a pfSense update process.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemUpdate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-update-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemUpdateEndpointJsonBody | Unset):
        body (PostSystemUpdateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemUpdateEndpointResponse400 | PostSystemUpdateEndpointResponse401 | PostSystemUpdateEndpointResponse403 | PostSystemUpdateEndpointResponse404 | PostSystemUpdateEndpointResponse405 | PostSystemUpdateEndpointResponse406 | PostSystemUpdateEndpointResponse409 | PostSystemUpdateEndpointResponse415 | PostSystemUpdateEndpointResponse422 | PostSystemUpdateEndpointResponse424 | PostSystemUpdateEndpointResponse500 | PostSystemUpdateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
