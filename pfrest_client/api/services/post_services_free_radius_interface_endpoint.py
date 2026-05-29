from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_free_radius_interface_endpoint_data_body import (
    PostServicesFreeRADIUSInterfaceEndpointDataBody,
)
from ...models.post_services_free_radius_interface_endpoint_json_body import (
    PostServicesFreeRADIUSInterfaceEndpointJsonBody,
)
from ...models.post_services_free_radius_interface_endpoint_response_400 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse400,
)
from ...models.post_services_free_radius_interface_endpoint_response_401 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse401,
)
from ...models.post_services_free_radius_interface_endpoint_response_403 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse403,
)
from ...models.post_services_free_radius_interface_endpoint_response_404 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse404,
)
from ...models.post_services_free_radius_interface_endpoint_response_405 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse405,
)
from ...models.post_services_free_radius_interface_endpoint_response_406 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse406,
)
from ...models.post_services_free_radius_interface_endpoint_response_409 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse409,
)
from ...models.post_services_free_radius_interface_endpoint_response_415 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse415,
)
from ...models.post_services_free_radius_interface_endpoint_response_422 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse422,
)
from ...models.post_services_free_radius_interface_endpoint_response_424 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse424,
)
from ...models.post_services_free_radius_interface_endpoint_response_500 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse500,
)
from ...models.post_services_free_radius_interface_endpoint_response_503 import (
    PostServicesFreeRADIUSInterfaceEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesFreeRADIUSInterfaceEndpointJsonBody
    | PostServicesFreeRADIUSInterfaceEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/freeradius/interface",
    }

    if isinstance(body, PostServicesFreeRADIUSInterfaceEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesFreeRADIUSInterfaceEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesFreeRADIUSInterfaceEndpointResponse400
    | PostServicesFreeRADIUSInterfaceEndpointResponse401
    | PostServicesFreeRADIUSInterfaceEndpointResponse403
    | PostServicesFreeRADIUSInterfaceEndpointResponse404
    | PostServicesFreeRADIUSInterfaceEndpointResponse405
    | PostServicesFreeRADIUSInterfaceEndpointResponse406
    | PostServicesFreeRADIUSInterfaceEndpointResponse409
    | PostServicesFreeRADIUSInterfaceEndpointResponse415
    | PostServicesFreeRADIUSInterfaceEndpointResponse422
    | PostServicesFreeRADIUSInterfaceEndpointResponse424
    | PostServicesFreeRADIUSInterfaceEndpointResponse500
    | PostServicesFreeRADIUSInterfaceEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesFreeRADIUSInterfaceEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesFreeRADIUSInterfaceEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesFreeRADIUSInterfaceEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesFreeRADIUSInterfaceEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesFreeRADIUSInterfaceEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesFreeRADIUSInterfaceEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesFreeRADIUSInterfaceEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesFreeRADIUSInterfaceEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesFreeRADIUSInterfaceEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesFreeRADIUSInterfaceEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesFreeRADIUSInterfaceEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesFreeRADIUSInterfaceEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesFreeRADIUSInterfaceEndpointResponse400
    | PostServicesFreeRADIUSInterfaceEndpointResponse401
    | PostServicesFreeRADIUSInterfaceEndpointResponse403
    | PostServicesFreeRADIUSInterfaceEndpointResponse404
    | PostServicesFreeRADIUSInterfaceEndpointResponse405
    | PostServicesFreeRADIUSInterfaceEndpointResponse406
    | PostServicesFreeRADIUSInterfaceEndpointResponse409
    | PostServicesFreeRADIUSInterfaceEndpointResponse415
    | PostServicesFreeRADIUSInterfaceEndpointResponse422
    | PostServicesFreeRADIUSInterfaceEndpointResponse424
    | PostServicesFreeRADIUSInterfaceEndpointResponse500
    | PostServicesFreeRADIUSInterfaceEndpointResponse503
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
    body: PostServicesFreeRADIUSInterfaceEndpointJsonBody
    | PostServicesFreeRADIUSInterfaceEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSInterfaceEndpointResponse400
    | PostServicesFreeRADIUSInterfaceEndpointResponse401
    | PostServicesFreeRADIUSInterfaceEndpointResponse403
    | PostServicesFreeRADIUSInterfaceEndpointResponse404
    | PostServicesFreeRADIUSInterfaceEndpointResponse405
    | PostServicesFreeRADIUSInterfaceEndpointResponse406
    | PostServicesFreeRADIUSInterfaceEndpointResponse409
    | PostServicesFreeRADIUSInterfaceEndpointResponse415
    | PostServicesFreeRADIUSInterfaceEndpointResponse422
    | PostServicesFreeRADIUSInterfaceEndpointResponse424
    | PostServicesFreeRADIUSInterfaceEndpointResponse500
    | PostServicesFreeRADIUSInterfaceEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS Interface.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interface-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSInterfaceEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSInterfaceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSInterfaceEndpointResponse400 | PostServicesFreeRADIUSInterfaceEndpointResponse401 | PostServicesFreeRADIUSInterfaceEndpointResponse403 | PostServicesFreeRADIUSInterfaceEndpointResponse404 | PostServicesFreeRADIUSInterfaceEndpointResponse405 | PostServicesFreeRADIUSInterfaceEndpointResponse406 | PostServicesFreeRADIUSInterfaceEndpointResponse409 | PostServicesFreeRADIUSInterfaceEndpointResponse415 | PostServicesFreeRADIUSInterfaceEndpointResponse422 | PostServicesFreeRADIUSInterfaceEndpointResponse424 | PostServicesFreeRADIUSInterfaceEndpointResponse500 | PostServicesFreeRADIUSInterfaceEndpointResponse503]
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
    body: PostServicesFreeRADIUSInterfaceEndpointJsonBody
    | PostServicesFreeRADIUSInterfaceEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSInterfaceEndpointResponse400
    | PostServicesFreeRADIUSInterfaceEndpointResponse401
    | PostServicesFreeRADIUSInterfaceEndpointResponse403
    | PostServicesFreeRADIUSInterfaceEndpointResponse404
    | PostServicesFreeRADIUSInterfaceEndpointResponse405
    | PostServicesFreeRADIUSInterfaceEndpointResponse406
    | PostServicesFreeRADIUSInterfaceEndpointResponse409
    | PostServicesFreeRADIUSInterfaceEndpointResponse415
    | PostServicesFreeRADIUSInterfaceEndpointResponse422
    | PostServicesFreeRADIUSInterfaceEndpointResponse424
    | PostServicesFreeRADIUSInterfaceEndpointResponse500
    | PostServicesFreeRADIUSInterfaceEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS Interface.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interface-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSInterfaceEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSInterfaceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSInterfaceEndpointResponse400 | PostServicesFreeRADIUSInterfaceEndpointResponse401 | PostServicesFreeRADIUSInterfaceEndpointResponse403 | PostServicesFreeRADIUSInterfaceEndpointResponse404 | PostServicesFreeRADIUSInterfaceEndpointResponse405 | PostServicesFreeRADIUSInterfaceEndpointResponse406 | PostServicesFreeRADIUSInterfaceEndpointResponse409 | PostServicesFreeRADIUSInterfaceEndpointResponse415 | PostServicesFreeRADIUSInterfaceEndpointResponse422 | PostServicesFreeRADIUSInterfaceEndpointResponse424 | PostServicesFreeRADIUSInterfaceEndpointResponse500 | PostServicesFreeRADIUSInterfaceEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSInterfaceEndpointJsonBody
    | PostServicesFreeRADIUSInterfaceEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesFreeRADIUSInterfaceEndpointResponse400
    | PostServicesFreeRADIUSInterfaceEndpointResponse401
    | PostServicesFreeRADIUSInterfaceEndpointResponse403
    | PostServicesFreeRADIUSInterfaceEndpointResponse404
    | PostServicesFreeRADIUSInterfaceEndpointResponse405
    | PostServicesFreeRADIUSInterfaceEndpointResponse406
    | PostServicesFreeRADIUSInterfaceEndpointResponse409
    | PostServicesFreeRADIUSInterfaceEndpointResponse415
    | PostServicesFreeRADIUSInterfaceEndpointResponse422
    | PostServicesFreeRADIUSInterfaceEndpointResponse424
    | PostServicesFreeRADIUSInterfaceEndpointResponse500
    | PostServicesFreeRADIUSInterfaceEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new FreeRADIUS Interface.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interface-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSInterfaceEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSInterfaceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesFreeRADIUSInterfaceEndpointResponse400 | PostServicesFreeRADIUSInterfaceEndpointResponse401 | PostServicesFreeRADIUSInterfaceEndpointResponse403 | PostServicesFreeRADIUSInterfaceEndpointResponse404 | PostServicesFreeRADIUSInterfaceEndpointResponse405 | PostServicesFreeRADIUSInterfaceEndpointResponse406 | PostServicesFreeRADIUSInterfaceEndpointResponse409 | PostServicesFreeRADIUSInterfaceEndpointResponse415 | PostServicesFreeRADIUSInterfaceEndpointResponse422 | PostServicesFreeRADIUSInterfaceEndpointResponse424 | PostServicesFreeRADIUSInterfaceEndpointResponse500 | PostServicesFreeRADIUSInterfaceEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesFreeRADIUSInterfaceEndpointJsonBody
    | PostServicesFreeRADIUSInterfaceEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesFreeRADIUSInterfaceEndpointResponse400
    | PostServicesFreeRADIUSInterfaceEndpointResponse401
    | PostServicesFreeRADIUSInterfaceEndpointResponse403
    | PostServicesFreeRADIUSInterfaceEndpointResponse404
    | PostServicesFreeRADIUSInterfaceEndpointResponse405
    | PostServicesFreeRADIUSInterfaceEndpointResponse406
    | PostServicesFreeRADIUSInterfaceEndpointResponse409
    | PostServicesFreeRADIUSInterfaceEndpointResponse415
    | PostServicesFreeRADIUSInterfaceEndpointResponse422
    | PostServicesFreeRADIUSInterfaceEndpointResponse424
    | PostServicesFreeRADIUSInterfaceEndpointResponse500
    | PostServicesFreeRADIUSInterfaceEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new FreeRADIUS Interface.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interface-post ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesFreeRADIUSInterfaceEndpointJsonBody | Unset):
        body (PostServicesFreeRADIUSInterfaceEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesFreeRADIUSInterfaceEndpointResponse400 | PostServicesFreeRADIUSInterfaceEndpointResponse401 | PostServicesFreeRADIUSInterfaceEndpointResponse403 | PostServicesFreeRADIUSInterfaceEndpointResponse404 | PostServicesFreeRADIUSInterfaceEndpointResponse405 | PostServicesFreeRADIUSInterfaceEndpointResponse406 | PostServicesFreeRADIUSInterfaceEndpointResponse409 | PostServicesFreeRADIUSInterfaceEndpointResponse415 | PostServicesFreeRADIUSInterfaceEndpointResponse422 | PostServicesFreeRADIUSInterfaceEndpointResponse424 | PostServicesFreeRADIUSInterfaceEndpointResponse500 | PostServicesFreeRADIUSInterfaceEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
