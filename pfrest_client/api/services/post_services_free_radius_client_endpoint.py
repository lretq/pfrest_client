from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_free_radius_client_endpoint_data_body import PostServicesFreeRADIUSClientEndpointDataBody
from ...models.post_services_free_radius_client_endpoint_json_body import PostServicesFreeRADIUSClientEndpointJsonBody
from ...models.post_services_free_radius_client_endpoint_response_400 import (
    PostServicesFreeRADIUSClientEndpointResponse400,
)
from ...models.post_services_free_radius_client_endpoint_response_401 import (
    PostServicesFreeRADIUSClientEndpointResponse401,
)
from ...models.post_services_free_radius_client_endpoint_response_403 import (
    PostServicesFreeRADIUSClientEndpointResponse403,
)
from ...models.post_services_free_radius_client_endpoint_response_404 import (
    PostServicesFreeRADIUSClientEndpointResponse404,
)
from ...models.post_services_free_radius_client_endpoint_response_405 import (
    PostServicesFreeRADIUSClientEndpointResponse405,
)
from ...models.post_services_free_radius_client_endpoint_response_406 import (
    PostServicesFreeRADIUSClientEndpointResponse406,
)
from ...models.post_services_free_radius_client_endpoint_response_409 import (
    PostServicesFreeRADIUSClientEndpointResponse409,
)
from ...models.post_services_free_radius_client_endpoint_response_415 import (
    PostServicesFreeRADIUSClientEndpointResponse415,
)
from ...models.post_services_free_radius_client_endpoint_response_422 import (
    PostServicesFreeRADIUSClientEndpointResponse422,
)
from ...models.post_services_free_radius_client_endpoint_response_424 import (
    PostServicesFreeRADIUSClientEndpointResponse424,
)
from ...models.post_services_free_radius_client_endpoint_response_500 import (
    PostServicesFreeRADIUSClientEndpointResponse500,
)
from ...models.post_services_free_radius_client_endpoint_response_503 import (
    PostServicesFreeRADIUSClientEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesFreeRADIUSClientEndpointJsonBody | PostServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/freeradius/client",
    }

    if isinstance(body, PostServicesFreeRADIUSClientEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesFreeRADIUSClientEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesFreeRADIUSClientEndpointResponse400
    | PostServicesFreeRADIUSClientEndpointResponse401
    | PostServicesFreeRADIUSClientEndpointResponse403
    | PostServicesFreeRADIUSClientEndpointResponse404
    | PostServicesFreeRADIUSClientEndpointResponse405
    | PostServicesFreeRADIUSClientEndpointResponse406
    | PostServicesFreeRADIUSClientEndpointResponse409
    | PostServicesFreeRADIUSClientEndpointResponse415
    | PostServicesFreeRADIUSClientEndpointResponse422
    | PostServicesFreeRADIUSClientEndpointResponse424
    | PostServicesFreeRADIUSClientEndpointResponse500
    | PostServicesFreeRADIUSClientEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesFreeRADIUSClientEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesFreeRADIUSClientEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesFreeRADIUSClientEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesFreeRADIUSClientEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesFreeRADIUSClientEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesFreeRADIUSClientEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesFreeRADIUSClientEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesFreeRADIUSClientEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesFreeRADIUSClientEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesFreeRADIUSClientEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesFreeRADIUSClientEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesFreeRADIUSClientEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesFreeRADIUSClientEndpointResponse400
    | PostServicesFreeRADIUSClientEndpointResponse401
    | PostServicesFreeRADIUSClientEndpointResponse403
    | PostServicesFreeRADIUSClientEndpointResponse404
    | PostServicesFreeRADIUSClientEndpointResponse405
    | PostServicesFreeRADIUSClientEndpointResponse406
    | PostServicesFreeRADIUSClientEndpointResponse409
    | PostServicesFreeRADIUSClientEndpointResponse415
    | PostServicesFreeRADIUSClientEndpointResponse422
    | PostServicesFreeRADIUSClientEndpointResponse424
    | PostServicesFreeRADIUSClientEndpointResponse500
    | PostServicesFreeRADIUSClientEndpointResponse503
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
    body: PostServicesFreeRADIUSClientEndpointJsonBody | PostServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSClientEndpointResponse400
    | PostServicesFreeRADIUSClientEndpointResponse401
    | PostServicesFreeRADIUSClientEndpointResponse403
    | PostServicesFreeRADIUSClientEndpointResponse404
    | PostServicesFreeRADIUSClientEndpointResponse405
    | PostServicesFreeRADIUSClientEndpointResponse406
    | PostServicesFreeRADIUSClientEndpointResponse409
    | PostServicesFreeRADIUSClientEndpointResponse415
    | PostServicesFreeRADIUSClientEndpointResponse422
    | PostServicesFreeRADIUSClientEndpointResponse424
    | PostServicesFreeRADIUSClientEndpointResponse500
    | PostServicesFreeRADIUSClientEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSClientEndpointResponse400 | PostServicesFreeRADIUSClientEndpointResponse401 | PostServicesFreeRADIUSClientEndpointResponse403 | PostServicesFreeRADIUSClientEndpointResponse404 | PostServicesFreeRADIUSClientEndpointResponse405 | PostServicesFreeRADIUSClientEndpointResponse406 | PostServicesFreeRADIUSClientEndpointResponse409 | PostServicesFreeRADIUSClientEndpointResponse415 | PostServicesFreeRADIUSClientEndpointResponse422 | PostServicesFreeRADIUSClientEndpointResponse424 | PostServicesFreeRADIUSClientEndpointResponse500 | PostServicesFreeRADIUSClientEndpointResponse503]
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
    body: PostServicesFreeRADIUSClientEndpointJsonBody | PostServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSClientEndpointResponse400
    | PostServicesFreeRADIUSClientEndpointResponse401
    | PostServicesFreeRADIUSClientEndpointResponse403
    | PostServicesFreeRADIUSClientEndpointResponse404
    | PostServicesFreeRADIUSClientEndpointResponse405
    | PostServicesFreeRADIUSClientEndpointResponse406
    | PostServicesFreeRADIUSClientEndpointResponse409
    | PostServicesFreeRADIUSClientEndpointResponse415
    | PostServicesFreeRADIUSClientEndpointResponse422
    | PostServicesFreeRADIUSClientEndpointResponse424
    | PostServicesFreeRADIUSClientEndpointResponse500
    | PostServicesFreeRADIUSClientEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSClientEndpointResponse400 | PostServicesFreeRADIUSClientEndpointResponse401 | PostServicesFreeRADIUSClientEndpointResponse403 | PostServicesFreeRADIUSClientEndpointResponse404 | PostServicesFreeRADIUSClientEndpointResponse405 | PostServicesFreeRADIUSClientEndpointResponse406 | PostServicesFreeRADIUSClientEndpointResponse409 | PostServicesFreeRADIUSClientEndpointResponse415 | PostServicesFreeRADIUSClientEndpointResponse422 | PostServicesFreeRADIUSClientEndpointResponse424 | PostServicesFreeRADIUSClientEndpointResponse500 | PostServicesFreeRADIUSClientEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSClientEndpointJsonBody | PostServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSClientEndpointResponse400
    | PostServicesFreeRADIUSClientEndpointResponse401
    | PostServicesFreeRADIUSClientEndpointResponse403
    | PostServicesFreeRADIUSClientEndpointResponse404
    | PostServicesFreeRADIUSClientEndpointResponse405
    | PostServicesFreeRADIUSClientEndpointResponse406
    | PostServicesFreeRADIUSClientEndpointResponse409
    | PostServicesFreeRADIUSClientEndpointResponse415
    | PostServicesFreeRADIUSClientEndpointResponse422
    | PostServicesFreeRADIUSClientEndpointResponse424
    | PostServicesFreeRADIUSClientEndpointResponse500
    | PostServicesFreeRADIUSClientEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSClientEndpointResponse400 | PostServicesFreeRADIUSClientEndpointResponse401 | PostServicesFreeRADIUSClientEndpointResponse403 | PostServicesFreeRADIUSClientEndpointResponse404 | PostServicesFreeRADIUSClientEndpointResponse405 | PostServicesFreeRADIUSClientEndpointResponse406 | PostServicesFreeRADIUSClientEndpointResponse409 | PostServicesFreeRADIUSClientEndpointResponse415 | PostServicesFreeRADIUSClientEndpointResponse422 | PostServicesFreeRADIUSClientEndpointResponse424 | PostServicesFreeRADIUSClientEndpointResponse500 | PostServicesFreeRADIUSClientEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSClientEndpointJsonBody | PostServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSClientEndpointResponse400
    | PostServicesFreeRADIUSClientEndpointResponse401
    | PostServicesFreeRADIUSClientEndpointResponse403
    | PostServicesFreeRADIUSClientEndpointResponse404
    | PostServicesFreeRADIUSClientEndpointResponse405
    | PostServicesFreeRADIUSClientEndpointResponse406
    | PostServicesFreeRADIUSClientEndpointResponse409
    | PostServicesFreeRADIUSClientEndpointResponse415
    | PostServicesFreeRADIUSClientEndpointResponse422
    | PostServicesFreeRADIUSClientEndpointResponse424
    | PostServicesFreeRADIUSClientEndpointResponse500
    | PostServicesFreeRADIUSClientEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSClientEndpointResponse400 | PostServicesFreeRADIUSClientEndpointResponse401 | PostServicesFreeRADIUSClientEndpointResponse403 | PostServicesFreeRADIUSClientEndpointResponse404 | PostServicesFreeRADIUSClientEndpointResponse405 | PostServicesFreeRADIUSClientEndpointResponse406 | PostServicesFreeRADIUSClientEndpointResponse409 | PostServicesFreeRADIUSClientEndpointResponse415 | PostServicesFreeRADIUSClientEndpointResponse422 | PostServicesFreeRADIUSClientEndpointResponse424 | PostServicesFreeRADIUSClientEndpointResponse500 | PostServicesFreeRADIUSClientEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
