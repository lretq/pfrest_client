from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_tunable_endpoint_data_body import PostSystemTunableEndpointDataBody
from ...models.post_system_tunable_endpoint_json_body import PostSystemTunableEndpointJsonBody
from ...models.post_system_tunable_endpoint_response_400 import PostSystemTunableEndpointResponse400
from ...models.post_system_tunable_endpoint_response_401 import PostSystemTunableEndpointResponse401
from ...models.post_system_tunable_endpoint_response_403 import PostSystemTunableEndpointResponse403
from ...models.post_system_tunable_endpoint_response_404 import PostSystemTunableEndpointResponse404
from ...models.post_system_tunable_endpoint_response_405 import PostSystemTunableEndpointResponse405
from ...models.post_system_tunable_endpoint_response_406 import PostSystemTunableEndpointResponse406
from ...models.post_system_tunable_endpoint_response_409 import PostSystemTunableEndpointResponse409
from ...models.post_system_tunable_endpoint_response_415 import PostSystemTunableEndpointResponse415
from ...models.post_system_tunable_endpoint_response_422 import PostSystemTunableEndpointResponse422
from ...models.post_system_tunable_endpoint_response_424 import PostSystemTunableEndpointResponse424
from ...models.post_system_tunable_endpoint_response_500 import PostSystemTunableEndpointResponse500
from ...models.post_system_tunable_endpoint_response_503 import PostSystemTunableEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemTunableEndpointJsonBody | PostSystemTunableEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/tunable",
    }

    if isinstance(body, PostSystemTunableEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemTunableEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemTunableEndpointResponse400
    | PostSystemTunableEndpointResponse401
    | PostSystemTunableEndpointResponse403
    | PostSystemTunableEndpointResponse404
    | PostSystemTunableEndpointResponse405
    | PostSystemTunableEndpointResponse406
    | PostSystemTunableEndpointResponse409
    | PostSystemTunableEndpointResponse415
    | PostSystemTunableEndpointResponse422
    | PostSystemTunableEndpointResponse424
    | PostSystemTunableEndpointResponse500
    | PostSystemTunableEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemTunableEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemTunableEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemTunableEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemTunableEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemTunableEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemTunableEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemTunableEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemTunableEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemTunableEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemTunableEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemTunableEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemTunableEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemTunableEndpointResponse400
    | PostSystemTunableEndpointResponse401
    | PostSystemTunableEndpointResponse403
    | PostSystemTunableEndpointResponse404
    | PostSystemTunableEndpointResponse405
    | PostSystemTunableEndpointResponse406
    | PostSystemTunableEndpointResponse409
    | PostSystemTunableEndpointResponse415
    | PostSystemTunableEndpointResponse422
    | PostSystemTunableEndpointResponse424
    | PostSystemTunableEndpointResponse500
    | PostSystemTunableEndpointResponse503
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
    body: PostSystemTunableEndpointJsonBody | PostSystemTunableEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemTunableEndpointResponse400
    | PostSystemTunableEndpointResponse401
    | PostSystemTunableEndpointResponse403
    | PostSystemTunableEndpointResponse404
    | PostSystemTunableEndpointResponse405
    | PostSystemTunableEndpointResponse406
    | PostSystemTunableEndpointResponse409
    | PostSystemTunableEndpointResponse415
    | PostSystemTunableEndpointResponse422
    | PostSystemTunableEndpointResponse424
    | PostSystemTunableEndpointResponse500
    | PostSystemTunableEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemTunableEndpointJsonBody | Unset):
        body (PostSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemTunableEndpointResponse400 | PostSystemTunableEndpointResponse401 | PostSystemTunableEndpointResponse403 | PostSystemTunableEndpointResponse404 | PostSystemTunableEndpointResponse405 | PostSystemTunableEndpointResponse406 | PostSystemTunableEndpointResponse409 | PostSystemTunableEndpointResponse415 | PostSystemTunableEndpointResponse422 | PostSystemTunableEndpointResponse424 | PostSystemTunableEndpointResponse500 | PostSystemTunableEndpointResponse503]
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
    body: PostSystemTunableEndpointJsonBody | PostSystemTunableEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemTunableEndpointResponse400
    | PostSystemTunableEndpointResponse401
    | PostSystemTunableEndpointResponse403
    | PostSystemTunableEndpointResponse404
    | PostSystemTunableEndpointResponse405
    | PostSystemTunableEndpointResponse406
    | PostSystemTunableEndpointResponse409
    | PostSystemTunableEndpointResponse415
    | PostSystemTunableEndpointResponse422
    | PostSystemTunableEndpointResponse424
    | PostSystemTunableEndpointResponse500
    | PostSystemTunableEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemTunableEndpointJsonBody | Unset):
        body (PostSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemTunableEndpointResponse400 | PostSystemTunableEndpointResponse401 | PostSystemTunableEndpointResponse403 | PostSystemTunableEndpointResponse404 | PostSystemTunableEndpointResponse405 | PostSystemTunableEndpointResponse406 | PostSystemTunableEndpointResponse409 | PostSystemTunableEndpointResponse415 | PostSystemTunableEndpointResponse422 | PostSystemTunableEndpointResponse424 | PostSystemTunableEndpointResponse500 | PostSystemTunableEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemTunableEndpointJsonBody | PostSystemTunableEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemTunableEndpointResponse400
    | PostSystemTunableEndpointResponse401
    | PostSystemTunableEndpointResponse403
    | PostSystemTunableEndpointResponse404
    | PostSystemTunableEndpointResponse405
    | PostSystemTunableEndpointResponse406
    | PostSystemTunableEndpointResponse409
    | PostSystemTunableEndpointResponse415
    | PostSystemTunableEndpointResponse422
    | PostSystemTunableEndpointResponse424
    | PostSystemTunableEndpointResponse500
    | PostSystemTunableEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemTunableEndpointJsonBody | Unset):
        body (PostSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemTunableEndpointResponse400 | PostSystemTunableEndpointResponse401 | PostSystemTunableEndpointResponse403 | PostSystemTunableEndpointResponse404 | PostSystemTunableEndpointResponse405 | PostSystemTunableEndpointResponse406 | PostSystemTunableEndpointResponse409 | PostSystemTunableEndpointResponse415 | PostSystemTunableEndpointResponse422 | PostSystemTunableEndpointResponse424 | PostSystemTunableEndpointResponse500 | PostSystemTunableEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemTunableEndpointJsonBody | PostSystemTunableEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemTunableEndpointResponse400
    | PostSystemTunableEndpointResponse401
    | PostSystemTunableEndpointResponse403
    | PostSystemTunableEndpointResponse404
    | PostSystemTunableEndpointResponse405
    | PostSystemTunableEndpointResponse406
    | PostSystemTunableEndpointResponse409
    | PostSystemTunableEndpointResponse415
    | PostSystemTunableEndpointResponse422
    | PostSystemTunableEndpointResponse424
    | PostSystemTunableEndpointResponse500
    | PostSystemTunableEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemTunableEndpointJsonBody | Unset):
        body (PostSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemTunableEndpointResponse400 | PostSystemTunableEndpointResponse401 | PostSystemTunableEndpointResponse403 | PostSystemTunableEndpointResponse404 | PostSystemTunableEndpointResponse405 | PostSystemTunableEndpointResponse406 | PostSystemTunableEndpointResponse409 | PostSystemTunableEndpointResponse415 | PostSystemTunableEndpointResponse422 | PostSystemTunableEndpointResponse424 | PostSystemTunableEndpointResponse500 | PostSystemTunableEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
