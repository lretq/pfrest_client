from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_free_radiusmac_endpoint_data_body import PostServicesFreeRADIUSMACEndpointDataBody
from ...models.post_services_free_radiusmac_endpoint_json_body import PostServicesFreeRADIUSMACEndpointJsonBody
from ...models.post_services_free_radiusmac_endpoint_response_400 import PostServicesFreeRADIUSMACEndpointResponse400
from ...models.post_services_free_radiusmac_endpoint_response_401 import PostServicesFreeRADIUSMACEndpointResponse401
from ...models.post_services_free_radiusmac_endpoint_response_403 import PostServicesFreeRADIUSMACEndpointResponse403
from ...models.post_services_free_radiusmac_endpoint_response_404 import PostServicesFreeRADIUSMACEndpointResponse404
from ...models.post_services_free_radiusmac_endpoint_response_405 import PostServicesFreeRADIUSMACEndpointResponse405
from ...models.post_services_free_radiusmac_endpoint_response_406 import PostServicesFreeRADIUSMACEndpointResponse406
from ...models.post_services_free_radiusmac_endpoint_response_409 import PostServicesFreeRADIUSMACEndpointResponse409
from ...models.post_services_free_radiusmac_endpoint_response_415 import PostServicesFreeRADIUSMACEndpointResponse415
from ...models.post_services_free_radiusmac_endpoint_response_422 import PostServicesFreeRADIUSMACEndpointResponse422
from ...models.post_services_free_radiusmac_endpoint_response_424 import PostServicesFreeRADIUSMACEndpointResponse424
from ...models.post_services_free_radiusmac_endpoint_response_500 import PostServicesFreeRADIUSMACEndpointResponse500
from ...models.post_services_free_radiusmac_endpoint_response_503 import PostServicesFreeRADIUSMACEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesFreeRADIUSMACEndpointJsonBody | PostServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/freeradius/mac",
    }

    if isinstance(body, PostServicesFreeRADIUSMACEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesFreeRADIUSMACEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesFreeRADIUSMACEndpointResponse400
    | PostServicesFreeRADIUSMACEndpointResponse401
    | PostServicesFreeRADIUSMACEndpointResponse403
    | PostServicesFreeRADIUSMACEndpointResponse404
    | PostServicesFreeRADIUSMACEndpointResponse405
    | PostServicesFreeRADIUSMACEndpointResponse406
    | PostServicesFreeRADIUSMACEndpointResponse409
    | PostServicesFreeRADIUSMACEndpointResponse415
    | PostServicesFreeRADIUSMACEndpointResponse422
    | PostServicesFreeRADIUSMACEndpointResponse424
    | PostServicesFreeRADIUSMACEndpointResponse500
    | PostServicesFreeRADIUSMACEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesFreeRADIUSMACEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesFreeRADIUSMACEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesFreeRADIUSMACEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesFreeRADIUSMACEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesFreeRADIUSMACEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesFreeRADIUSMACEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesFreeRADIUSMACEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesFreeRADIUSMACEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesFreeRADIUSMACEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesFreeRADIUSMACEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesFreeRADIUSMACEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesFreeRADIUSMACEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesFreeRADIUSMACEndpointResponse400
    | PostServicesFreeRADIUSMACEndpointResponse401
    | PostServicesFreeRADIUSMACEndpointResponse403
    | PostServicesFreeRADIUSMACEndpointResponse404
    | PostServicesFreeRADIUSMACEndpointResponse405
    | PostServicesFreeRADIUSMACEndpointResponse406
    | PostServicesFreeRADIUSMACEndpointResponse409
    | PostServicesFreeRADIUSMACEndpointResponse415
    | PostServicesFreeRADIUSMACEndpointResponse422
    | PostServicesFreeRADIUSMACEndpointResponse424
    | PostServicesFreeRADIUSMACEndpointResponse500
    | PostServicesFreeRADIUSMACEndpointResponse503
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
    body: PostServicesFreeRADIUSMACEndpointJsonBody | PostServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSMACEndpointResponse400
    | PostServicesFreeRADIUSMACEndpointResponse401
    | PostServicesFreeRADIUSMACEndpointResponse403
    | PostServicesFreeRADIUSMACEndpointResponse404
    | PostServicesFreeRADIUSMACEndpointResponse405
    | PostServicesFreeRADIUSMACEndpointResponse406
    | PostServicesFreeRADIUSMACEndpointResponse409
    | PostServicesFreeRADIUSMACEndpointResponse415
    | PostServicesFreeRADIUSMACEndpointResponse422
    | PostServicesFreeRADIUSMACEndpointResponse424
    | PostServicesFreeRADIUSMACEndpointResponse500
    | PostServicesFreeRADIUSMACEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSMACEndpointResponse400 | PostServicesFreeRADIUSMACEndpointResponse401 | PostServicesFreeRADIUSMACEndpointResponse403 | PostServicesFreeRADIUSMACEndpointResponse404 | PostServicesFreeRADIUSMACEndpointResponse405 | PostServicesFreeRADIUSMACEndpointResponse406 | PostServicesFreeRADIUSMACEndpointResponse409 | PostServicesFreeRADIUSMACEndpointResponse415 | PostServicesFreeRADIUSMACEndpointResponse422 | PostServicesFreeRADIUSMACEndpointResponse424 | PostServicesFreeRADIUSMACEndpointResponse500 | PostServicesFreeRADIUSMACEndpointResponse503]
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
    body: PostServicesFreeRADIUSMACEndpointJsonBody | PostServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSMACEndpointResponse400
    | PostServicesFreeRADIUSMACEndpointResponse401
    | PostServicesFreeRADIUSMACEndpointResponse403
    | PostServicesFreeRADIUSMACEndpointResponse404
    | PostServicesFreeRADIUSMACEndpointResponse405
    | PostServicesFreeRADIUSMACEndpointResponse406
    | PostServicesFreeRADIUSMACEndpointResponse409
    | PostServicesFreeRADIUSMACEndpointResponse415
    | PostServicesFreeRADIUSMACEndpointResponse422
    | PostServicesFreeRADIUSMACEndpointResponse424
    | PostServicesFreeRADIUSMACEndpointResponse500
    | PostServicesFreeRADIUSMACEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSMACEndpointResponse400 | PostServicesFreeRADIUSMACEndpointResponse401 | PostServicesFreeRADIUSMACEndpointResponse403 | PostServicesFreeRADIUSMACEndpointResponse404 | PostServicesFreeRADIUSMACEndpointResponse405 | PostServicesFreeRADIUSMACEndpointResponse406 | PostServicesFreeRADIUSMACEndpointResponse409 | PostServicesFreeRADIUSMACEndpointResponse415 | PostServicesFreeRADIUSMACEndpointResponse422 | PostServicesFreeRADIUSMACEndpointResponse424 | PostServicesFreeRADIUSMACEndpointResponse500 | PostServicesFreeRADIUSMACEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSMACEndpointJsonBody | PostServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSMACEndpointResponse400
    | PostServicesFreeRADIUSMACEndpointResponse401
    | PostServicesFreeRADIUSMACEndpointResponse403
    | PostServicesFreeRADIUSMACEndpointResponse404
    | PostServicesFreeRADIUSMACEndpointResponse405
    | PostServicesFreeRADIUSMACEndpointResponse406
    | PostServicesFreeRADIUSMACEndpointResponse409
    | PostServicesFreeRADIUSMACEndpointResponse415
    | PostServicesFreeRADIUSMACEndpointResponse422
    | PostServicesFreeRADIUSMACEndpointResponse424
    | PostServicesFreeRADIUSMACEndpointResponse500
    | PostServicesFreeRADIUSMACEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSMACEndpointResponse400 | PostServicesFreeRADIUSMACEndpointResponse401 | PostServicesFreeRADIUSMACEndpointResponse403 | PostServicesFreeRADIUSMACEndpointResponse404 | PostServicesFreeRADIUSMACEndpointResponse405 | PostServicesFreeRADIUSMACEndpointResponse406 | PostServicesFreeRADIUSMACEndpointResponse409 | PostServicesFreeRADIUSMACEndpointResponse415 | PostServicesFreeRADIUSMACEndpointResponse422 | PostServicesFreeRADIUSMACEndpointResponse424 | PostServicesFreeRADIUSMACEndpointResponse500 | PostServicesFreeRADIUSMACEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSMACEndpointJsonBody | PostServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSMACEndpointResponse400
    | PostServicesFreeRADIUSMACEndpointResponse401
    | PostServicesFreeRADIUSMACEndpointResponse403
    | PostServicesFreeRADIUSMACEndpointResponse404
    | PostServicesFreeRADIUSMACEndpointResponse405
    | PostServicesFreeRADIUSMACEndpointResponse406
    | PostServicesFreeRADIUSMACEndpointResponse409
    | PostServicesFreeRADIUSMACEndpointResponse415
    | PostServicesFreeRADIUSMACEndpointResponse422
    | PostServicesFreeRADIUSMACEndpointResponse424
    | PostServicesFreeRADIUSMACEndpointResponse500
    | PostServicesFreeRADIUSMACEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSMACEndpointResponse400 | PostServicesFreeRADIUSMACEndpointResponse401 | PostServicesFreeRADIUSMACEndpointResponse403 | PostServicesFreeRADIUSMACEndpointResponse404 | PostServicesFreeRADIUSMACEndpointResponse405 | PostServicesFreeRADIUSMACEndpointResponse406 | PostServicesFreeRADIUSMACEndpointResponse409 | PostServicesFreeRADIUSMACEndpointResponse415 | PostServicesFreeRADIUSMACEndpointResponse422 | PostServicesFreeRADIUSMACEndpointResponse424 | PostServicesFreeRADIUSMACEndpointResponse500 | PostServicesFreeRADIUSMACEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
