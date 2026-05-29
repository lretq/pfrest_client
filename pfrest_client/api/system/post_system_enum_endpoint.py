from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_enum_endpoint_data_body import PostSystemEnumEndpointDataBody
from ...models.post_system_enum_endpoint_json_body import PostSystemEnumEndpointJsonBody
from ...models.post_system_enum_endpoint_response_400 import PostSystemEnumEndpointResponse400
from ...models.post_system_enum_endpoint_response_401 import PostSystemEnumEndpointResponse401
from ...models.post_system_enum_endpoint_response_403 import PostSystemEnumEndpointResponse403
from ...models.post_system_enum_endpoint_response_404 import PostSystemEnumEndpointResponse404
from ...models.post_system_enum_endpoint_response_405 import PostSystemEnumEndpointResponse405
from ...models.post_system_enum_endpoint_response_406 import PostSystemEnumEndpointResponse406
from ...models.post_system_enum_endpoint_response_409 import PostSystemEnumEndpointResponse409
from ...models.post_system_enum_endpoint_response_415 import PostSystemEnumEndpointResponse415
from ...models.post_system_enum_endpoint_response_422 import PostSystemEnumEndpointResponse422
from ...models.post_system_enum_endpoint_response_424 import PostSystemEnumEndpointResponse424
from ...models.post_system_enum_endpoint_response_500 import PostSystemEnumEndpointResponse500
from ...models.post_system_enum_endpoint_response_503 import PostSystemEnumEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemEnumEndpointJsonBody | PostSystemEnumEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/enum",
    }

    if isinstance(body, PostSystemEnumEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemEnumEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemEnumEndpointResponse400
    | PostSystemEnumEndpointResponse401
    | PostSystemEnumEndpointResponse403
    | PostSystemEnumEndpointResponse404
    | PostSystemEnumEndpointResponse405
    | PostSystemEnumEndpointResponse406
    | PostSystemEnumEndpointResponse409
    | PostSystemEnumEndpointResponse415
    | PostSystemEnumEndpointResponse422
    | PostSystemEnumEndpointResponse424
    | PostSystemEnumEndpointResponse500
    | PostSystemEnumEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemEnumEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemEnumEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemEnumEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemEnumEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemEnumEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemEnumEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemEnumEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemEnumEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemEnumEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemEnumEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemEnumEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemEnumEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemEnumEndpointResponse400
    | PostSystemEnumEndpointResponse401
    | PostSystemEnumEndpointResponse403
    | PostSystemEnumEndpointResponse404
    | PostSystemEnumEndpointResponse405
    | PostSystemEnumEndpointResponse406
    | PostSystemEnumEndpointResponse409
    | PostSystemEnumEndpointResponse415
    | PostSystemEnumEndpointResponse422
    | PostSystemEnumEndpointResponse424
    | PostSystemEnumEndpointResponse500
    | PostSystemEnumEndpointResponse503
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
    body: PostSystemEnumEndpointJsonBody | PostSystemEnumEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemEnumEndpointResponse400
    | PostSystemEnumEndpointResponse401
    | PostSystemEnumEndpointResponse403
    | PostSystemEnumEndpointResponse404
    | PostSystemEnumEndpointResponse405
    | PostSystemEnumEndpointResponse406
    | PostSystemEnumEndpointResponse409
    | PostSystemEnumEndpointResponse415
    | PostSystemEnumEndpointResponse422
    | PostSystemEnumEndpointResponse424
    | PostSystemEnumEndpointResponse500
    | PostSystemEnumEndpointResponse503
]:
    """<h3>Description:</h3>Enumerate all possible choices for a given model
    field.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Enum<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-enum-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemEnumEndpointJsonBody | Unset):
        body (PostSystemEnumEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemEnumEndpointResponse400 | PostSystemEnumEndpointResponse401 | PostSystemEnumEndpointResponse403 | PostSystemEnumEndpointResponse404 | PostSystemEnumEndpointResponse405 | PostSystemEnumEndpointResponse406 | PostSystemEnumEndpointResponse409 | PostSystemEnumEndpointResponse415 | PostSystemEnumEndpointResponse422 | PostSystemEnumEndpointResponse424 | PostSystemEnumEndpointResponse500 | PostSystemEnumEndpointResponse503]
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
    body: PostSystemEnumEndpointJsonBody | PostSystemEnumEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemEnumEndpointResponse400
    | PostSystemEnumEndpointResponse401
    | PostSystemEnumEndpointResponse403
    | PostSystemEnumEndpointResponse404
    | PostSystemEnumEndpointResponse405
    | PostSystemEnumEndpointResponse406
    | PostSystemEnumEndpointResponse409
    | PostSystemEnumEndpointResponse415
    | PostSystemEnumEndpointResponse422
    | PostSystemEnumEndpointResponse424
    | PostSystemEnumEndpointResponse500
    | PostSystemEnumEndpointResponse503
    | None
):
    """<h3>Description:</h3>Enumerate all possible choices for a given model
    field.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Enum<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-enum-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemEnumEndpointJsonBody | Unset):
        body (PostSystemEnumEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemEnumEndpointResponse400 | PostSystemEnumEndpointResponse401 | PostSystemEnumEndpointResponse403 | PostSystemEnumEndpointResponse404 | PostSystemEnumEndpointResponse405 | PostSystemEnumEndpointResponse406 | PostSystemEnumEndpointResponse409 | PostSystemEnumEndpointResponse415 | PostSystemEnumEndpointResponse422 | PostSystemEnumEndpointResponse424 | PostSystemEnumEndpointResponse500 | PostSystemEnumEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemEnumEndpointJsonBody | PostSystemEnumEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemEnumEndpointResponse400
    | PostSystemEnumEndpointResponse401
    | PostSystemEnumEndpointResponse403
    | PostSystemEnumEndpointResponse404
    | PostSystemEnumEndpointResponse405
    | PostSystemEnumEndpointResponse406
    | PostSystemEnumEndpointResponse409
    | PostSystemEnumEndpointResponse415
    | PostSystemEnumEndpointResponse422
    | PostSystemEnumEndpointResponse424
    | PostSystemEnumEndpointResponse500
    | PostSystemEnumEndpointResponse503
]:
    """<h3>Description:</h3>Enumerate all possible choices for a given model
    field.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Enum<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-enum-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemEnumEndpointJsonBody | Unset):
        body (PostSystemEnumEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemEnumEndpointResponse400 | PostSystemEnumEndpointResponse401 | PostSystemEnumEndpointResponse403 | PostSystemEnumEndpointResponse404 | PostSystemEnumEndpointResponse405 | PostSystemEnumEndpointResponse406 | PostSystemEnumEndpointResponse409 | PostSystemEnumEndpointResponse415 | PostSystemEnumEndpointResponse422 | PostSystemEnumEndpointResponse424 | PostSystemEnumEndpointResponse500 | PostSystemEnumEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemEnumEndpointJsonBody | PostSystemEnumEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemEnumEndpointResponse400
    | PostSystemEnumEndpointResponse401
    | PostSystemEnumEndpointResponse403
    | PostSystemEnumEndpointResponse404
    | PostSystemEnumEndpointResponse405
    | PostSystemEnumEndpointResponse406
    | PostSystemEnumEndpointResponse409
    | PostSystemEnumEndpointResponse415
    | PostSystemEnumEndpointResponse422
    | PostSystemEnumEndpointResponse424
    | PostSystemEnumEndpointResponse500
    | PostSystemEnumEndpointResponse503
    | None
):
    """<h3>Description:</h3>Enumerate all possible choices for a given model
    field.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Enum<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-enum-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemEnumEndpointJsonBody | Unset):
        body (PostSystemEnumEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemEnumEndpointResponse400 | PostSystemEnumEndpointResponse401 | PostSystemEnumEndpointResponse403 | PostSystemEnumEndpointResponse404 | PostSystemEnumEndpointResponse405 | PostSystemEnumEndpointResponse406 | PostSystemEnumEndpointResponse409 | PostSystemEnumEndpointResponse415 | PostSystemEnumEndpointResponse422 | PostSystemEnumEndpointResponse424 | PostSystemEnumEndpointResponse500 | PostSystemEnumEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
