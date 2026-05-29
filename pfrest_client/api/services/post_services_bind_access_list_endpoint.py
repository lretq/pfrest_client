from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_bind_access_list_endpoint_data_body import PostServicesBINDAccessListEndpointDataBody
from ...models.post_services_bind_access_list_endpoint_json_body import PostServicesBINDAccessListEndpointJsonBody
from ...models.post_services_bind_access_list_endpoint_response_400 import PostServicesBINDAccessListEndpointResponse400
from ...models.post_services_bind_access_list_endpoint_response_401 import PostServicesBINDAccessListEndpointResponse401
from ...models.post_services_bind_access_list_endpoint_response_403 import PostServicesBINDAccessListEndpointResponse403
from ...models.post_services_bind_access_list_endpoint_response_404 import PostServicesBINDAccessListEndpointResponse404
from ...models.post_services_bind_access_list_endpoint_response_405 import PostServicesBINDAccessListEndpointResponse405
from ...models.post_services_bind_access_list_endpoint_response_406 import PostServicesBINDAccessListEndpointResponse406
from ...models.post_services_bind_access_list_endpoint_response_409 import PostServicesBINDAccessListEndpointResponse409
from ...models.post_services_bind_access_list_endpoint_response_415 import PostServicesBINDAccessListEndpointResponse415
from ...models.post_services_bind_access_list_endpoint_response_422 import PostServicesBINDAccessListEndpointResponse422
from ...models.post_services_bind_access_list_endpoint_response_424 import PostServicesBINDAccessListEndpointResponse424
from ...models.post_services_bind_access_list_endpoint_response_500 import PostServicesBINDAccessListEndpointResponse500
from ...models.post_services_bind_access_list_endpoint_response_503 import PostServicesBINDAccessListEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesBINDAccessListEndpointJsonBody | PostServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/bind/access_list",
    }

    if isinstance(body, PostServicesBINDAccessListEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesBINDAccessListEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesBINDAccessListEndpointResponse400
    | PostServicesBINDAccessListEndpointResponse401
    | PostServicesBINDAccessListEndpointResponse403
    | PostServicesBINDAccessListEndpointResponse404
    | PostServicesBINDAccessListEndpointResponse405
    | PostServicesBINDAccessListEndpointResponse406
    | PostServicesBINDAccessListEndpointResponse409
    | PostServicesBINDAccessListEndpointResponse415
    | PostServicesBINDAccessListEndpointResponse422
    | PostServicesBINDAccessListEndpointResponse424
    | PostServicesBINDAccessListEndpointResponse500
    | PostServicesBINDAccessListEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesBINDAccessListEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesBINDAccessListEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesBINDAccessListEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesBINDAccessListEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesBINDAccessListEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesBINDAccessListEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesBINDAccessListEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesBINDAccessListEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesBINDAccessListEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesBINDAccessListEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesBINDAccessListEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesBINDAccessListEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesBINDAccessListEndpointResponse400
    | PostServicesBINDAccessListEndpointResponse401
    | PostServicesBINDAccessListEndpointResponse403
    | PostServicesBINDAccessListEndpointResponse404
    | PostServicesBINDAccessListEndpointResponse405
    | PostServicesBINDAccessListEndpointResponse406
    | PostServicesBINDAccessListEndpointResponse409
    | PostServicesBINDAccessListEndpointResponse415
    | PostServicesBINDAccessListEndpointResponse422
    | PostServicesBINDAccessListEndpointResponse424
    | PostServicesBINDAccessListEndpointResponse500
    | PostServicesBINDAccessListEndpointResponse503
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
    body: PostServicesBINDAccessListEndpointJsonBody | PostServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesBINDAccessListEndpointResponse400
    | PostServicesBINDAccessListEndpointResponse401
    | PostServicesBINDAccessListEndpointResponse403
    | PostServicesBINDAccessListEndpointResponse404
    | PostServicesBINDAccessListEndpointResponse405
    | PostServicesBINDAccessListEndpointResponse406
    | PostServicesBINDAccessListEndpointResponse409
    | PostServicesBINDAccessListEndpointResponse415
    | PostServicesBINDAccessListEndpointResponse422
    | PostServicesBINDAccessListEndpointResponse424
    | PostServicesBINDAccessListEndpointResponse500
    | PostServicesBINDAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-post ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDAccessListEndpointJsonBody | Unset):
        body (PostServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesBINDAccessListEndpointResponse400 | PostServicesBINDAccessListEndpointResponse401 | PostServicesBINDAccessListEndpointResponse403 | PostServicesBINDAccessListEndpointResponse404 | PostServicesBINDAccessListEndpointResponse405 | PostServicesBINDAccessListEndpointResponse406 | PostServicesBINDAccessListEndpointResponse409 | PostServicesBINDAccessListEndpointResponse415 | PostServicesBINDAccessListEndpointResponse422 | PostServicesBINDAccessListEndpointResponse424 | PostServicesBINDAccessListEndpointResponse500 | PostServicesBINDAccessListEndpointResponse503]
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
    body: PostServicesBINDAccessListEndpointJsonBody | PostServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesBINDAccessListEndpointResponse400
    | PostServicesBINDAccessListEndpointResponse401
    | PostServicesBINDAccessListEndpointResponse403
    | PostServicesBINDAccessListEndpointResponse404
    | PostServicesBINDAccessListEndpointResponse405
    | PostServicesBINDAccessListEndpointResponse406
    | PostServicesBINDAccessListEndpointResponse409
    | PostServicesBINDAccessListEndpointResponse415
    | PostServicesBINDAccessListEndpointResponse422
    | PostServicesBINDAccessListEndpointResponse424
    | PostServicesBINDAccessListEndpointResponse500
    | PostServicesBINDAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-post ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDAccessListEndpointJsonBody | Unset):
        body (PostServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesBINDAccessListEndpointResponse400 | PostServicesBINDAccessListEndpointResponse401 | PostServicesBINDAccessListEndpointResponse403 | PostServicesBINDAccessListEndpointResponse404 | PostServicesBINDAccessListEndpointResponse405 | PostServicesBINDAccessListEndpointResponse406 | PostServicesBINDAccessListEndpointResponse409 | PostServicesBINDAccessListEndpointResponse415 | PostServicesBINDAccessListEndpointResponse422 | PostServicesBINDAccessListEndpointResponse424 | PostServicesBINDAccessListEndpointResponse500 | PostServicesBINDAccessListEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesBINDAccessListEndpointJsonBody | PostServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesBINDAccessListEndpointResponse400
    | PostServicesBINDAccessListEndpointResponse401
    | PostServicesBINDAccessListEndpointResponse403
    | PostServicesBINDAccessListEndpointResponse404
    | PostServicesBINDAccessListEndpointResponse405
    | PostServicesBINDAccessListEndpointResponse406
    | PostServicesBINDAccessListEndpointResponse409
    | PostServicesBINDAccessListEndpointResponse415
    | PostServicesBINDAccessListEndpointResponse422
    | PostServicesBINDAccessListEndpointResponse424
    | PostServicesBINDAccessListEndpointResponse500
    | PostServicesBINDAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-post ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDAccessListEndpointJsonBody | Unset):
        body (PostServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesBINDAccessListEndpointResponse400 | PostServicesBINDAccessListEndpointResponse401 | PostServicesBINDAccessListEndpointResponse403 | PostServicesBINDAccessListEndpointResponse404 | PostServicesBINDAccessListEndpointResponse405 | PostServicesBINDAccessListEndpointResponse406 | PostServicesBINDAccessListEndpointResponse409 | PostServicesBINDAccessListEndpointResponse415 | PostServicesBINDAccessListEndpointResponse422 | PostServicesBINDAccessListEndpointResponse424 | PostServicesBINDAccessListEndpointResponse500 | PostServicesBINDAccessListEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesBINDAccessListEndpointJsonBody | PostServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesBINDAccessListEndpointResponse400
    | PostServicesBINDAccessListEndpointResponse401
    | PostServicesBINDAccessListEndpointResponse403
    | PostServicesBINDAccessListEndpointResponse404
    | PostServicesBINDAccessListEndpointResponse405
    | PostServicesBINDAccessListEndpointResponse406
    | PostServicesBINDAccessListEndpointResponse409
    | PostServicesBINDAccessListEndpointResponse415
    | PostServicesBINDAccessListEndpointResponse422
    | PostServicesBINDAccessListEndpointResponse424
    | PostServicesBINDAccessListEndpointResponse500
    | PostServicesBINDAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-post ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesBINDAccessListEndpointJsonBody | Unset):
        body (PostServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesBINDAccessListEndpointResponse400 | PostServicesBINDAccessListEndpointResponse401 | PostServicesBINDAccessListEndpointResponse403 | PostServicesBINDAccessListEndpointResponse404 | PostServicesBINDAccessListEndpointResponse405 | PostServicesBINDAccessListEndpointResponse406 | PostServicesBINDAccessListEndpointResponse409 | PostServicesBINDAccessListEndpointResponse415 | PostServicesBINDAccessListEndpointResponse422 | PostServicesBINDAccessListEndpointResponse424 | PostServicesBINDAccessListEndpointResponse500 | PostServicesBINDAccessListEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
