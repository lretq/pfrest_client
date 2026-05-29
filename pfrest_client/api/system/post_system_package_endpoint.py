from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_package_endpoint_data_body import PostSystemPackageEndpointDataBody
from ...models.post_system_package_endpoint_json_body import PostSystemPackageEndpointJsonBody
from ...models.post_system_package_endpoint_response_400 import PostSystemPackageEndpointResponse400
from ...models.post_system_package_endpoint_response_401 import PostSystemPackageEndpointResponse401
from ...models.post_system_package_endpoint_response_403 import PostSystemPackageEndpointResponse403
from ...models.post_system_package_endpoint_response_404 import PostSystemPackageEndpointResponse404
from ...models.post_system_package_endpoint_response_405 import PostSystemPackageEndpointResponse405
from ...models.post_system_package_endpoint_response_406 import PostSystemPackageEndpointResponse406
from ...models.post_system_package_endpoint_response_409 import PostSystemPackageEndpointResponse409
from ...models.post_system_package_endpoint_response_415 import PostSystemPackageEndpointResponse415
from ...models.post_system_package_endpoint_response_422 import PostSystemPackageEndpointResponse422
from ...models.post_system_package_endpoint_response_424 import PostSystemPackageEndpointResponse424
from ...models.post_system_package_endpoint_response_500 import PostSystemPackageEndpointResponse500
from ...models.post_system_package_endpoint_response_503 import PostSystemPackageEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemPackageEndpointJsonBody | PostSystemPackageEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/package",
    }

    if isinstance(body, PostSystemPackageEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemPackageEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemPackageEndpointResponse400
    | PostSystemPackageEndpointResponse401
    | PostSystemPackageEndpointResponse403
    | PostSystemPackageEndpointResponse404
    | PostSystemPackageEndpointResponse405
    | PostSystemPackageEndpointResponse406
    | PostSystemPackageEndpointResponse409
    | PostSystemPackageEndpointResponse415
    | PostSystemPackageEndpointResponse422
    | PostSystemPackageEndpointResponse424
    | PostSystemPackageEndpointResponse500
    | PostSystemPackageEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemPackageEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemPackageEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemPackageEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemPackageEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemPackageEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemPackageEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemPackageEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemPackageEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemPackageEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemPackageEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemPackageEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemPackageEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemPackageEndpointResponse400
    | PostSystemPackageEndpointResponse401
    | PostSystemPackageEndpointResponse403
    | PostSystemPackageEndpointResponse404
    | PostSystemPackageEndpointResponse405
    | PostSystemPackageEndpointResponse406
    | PostSystemPackageEndpointResponse409
    | PostSystemPackageEndpointResponse415
    | PostSystemPackageEndpointResponse422
    | PostSystemPackageEndpointResponse424
    | PostSystemPackageEndpointResponse500
    | PostSystemPackageEndpointResponse503
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
    body: PostSystemPackageEndpointJsonBody | PostSystemPackageEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemPackageEndpointResponse400
    | PostSystemPackageEndpointResponse401
    | PostSystemPackageEndpointResponse403
    | PostSystemPackageEndpointResponse404
    | PostSystemPackageEndpointResponse405
    | PostSystemPackageEndpointResponse406
    | PostSystemPackageEndpointResponse409
    | PostSystemPackageEndpointResponse415
    | PostSystemPackageEndpointResponse422
    | PostSystemPackageEndpointResponse424
    | PostSystemPackageEndpointResponse500
    | PostSystemPackageEndpointResponse503
]:
    """<h3>Description:</h3>Installs a new Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-post ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemPackageEndpointJsonBody | Unset):
        body (PostSystemPackageEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemPackageEndpointResponse400 | PostSystemPackageEndpointResponse401 | PostSystemPackageEndpointResponse403 | PostSystemPackageEndpointResponse404 | PostSystemPackageEndpointResponse405 | PostSystemPackageEndpointResponse406 | PostSystemPackageEndpointResponse409 | PostSystemPackageEndpointResponse415 | PostSystemPackageEndpointResponse422 | PostSystemPackageEndpointResponse424 | PostSystemPackageEndpointResponse500 | PostSystemPackageEndpointResponse503]
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
    body: PostSystemPackageEndpointJsonBody | PostSystemPackageEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemPackageEndpointResponse400
    | PostSystemPackageEndpointResponse401
    | PostSystemPackageEndpointResponse403
    | PostSystemPackageEndpointResponse404
    | PostSystemPackageEndpointResponse405
    | PostSystemPackageEndpointResponse406
    | PostSystemPackageEndpointResponse409
    | PostSystemPackageEndpointResponse415
    | PostSystemPackageEndpointResponse422
    | PostSystemPackageEndpointResponse424
    | PostSystemPackageEndpointResponse500
    | PostSystemPackageEndpointResponse503
    | None
):
    """<h3>Description:</h3>Installs a new Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-post ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemPackageEndpointJsonBody | Unset):
        body (PostSystemPackageEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemPackageEndpointResponse400 | PostSystemPackageEndpointResponse401 | PostSystemPackageEndpointResponse403 | PostSystemPackageEndpointResponse404 | PostSystemPackageEndpointResponse405 | PostSystemPackageEndpointResponse406 | PostSystemPackageEndpointResponse409 | PostSystemPackageEndpointResponse415 | PostSystemPackageEndpointResponse422 | PostSystemPackageEndpointResponse424 | PostSystemPackageEndpointResponse500 | PostSystemPackageEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemPackageEndpointJsonBody | PostSystemPackageEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemPackageEndpointResponse400
    | PostSystemPackageEndpointResponse401
    | PostSystemPackageEndpointResponse403
    | PostSystemPackageEndpointResponse404
    | PostSystemPackageEndpointResponse405
    | PostSystemPackageEndpointResponse406
    | PostSystemPackageEndpointResponse409
    | PostSystemPackageEndpointResponse415
    | PostSystemPackageEndpointResponse422
    | PostSystemPackageEndpointResponse424
    | PostSystemPackageEndpointResponse500
    | PostSystemPackageEndpointResponse503
]:
    """<h3>Description:</h3>Installs a new Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-post ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemPackageEndpointJsonBody | Unset):
        body (PostSystemPackageEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemPackageEndpointResponse400 | PostSystemPackageEndpointResponse401 | PostSystemPackageEndpointResponse403 | PostSystemPackageEndpointResponse404 | PostSystemPackageEndpointResponse405 | PostSystemPackageEndpointResponse406 | PostSystemPackageEndpointResponse409 | PostSystemPackageEndpointResponse415 | PostSystemPackageEndpointResponse422 | PostSystemPackageEndpointResponse424 | PostSystemPackageEndpointResponse500 | PostSystemPackageEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemPackageEndpointJsonBody | PostSystemPackageEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemPackageEndpointResponse400
    | PostSystemPackageEndpointResponse401
    | PostSystemPackageEndpointResponse403
    | PostSystemPackageEndpointResponse404
    | PostSystemPackageEndpointResponse405
    | PostSystemPackageEndpointResponse406
    | PostSystemPackageEndpointResponse409
    | PostSystemPackageEndpointResponse415
    | PostSystemPackageEndpointResponse422
    | PostSystemPackageEndpointResponse424
    | PostSystemPackageEndpointResponse500
    | PostSystemPackageEndpointResponse503
    | None
):
    """<h3>Description:</h3>Installs a new Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-post ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemPackageEndpointJsonBody | Unset):
        body (PostSystemPackageEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemPackageEndpointResponse400 | PostSystemPackageEndpointResponse401 | PostSystemPackageEndpointResponse403 | PostSystemPackageEndpointResponse404 | PostSystemPackageEndpointResponse405 | PostSystemPackageEndpointResponse406 | PostSystemPackageEndpointResponse409 | PostSystemPackageEndpointResponse415 | PostSystemPackageEndpointResponse422 | PostSystemPackageEndpointResponse424 | PostSystemPackageEndpointResponse500 | PostSystemPackageEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
