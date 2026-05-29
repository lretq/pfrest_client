from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dhcp_server_endpoint_data_body import PostServicesDHCPServerEndpointDataBody
from ...models.post_services_dhcp_server_endpoint_json_body import PostServicesDHCPServerEndpointJsonBody
from ...models.post_services_dhcp_server_endpoint_response_400 import PostServicesDHCPServerEndpointResponse400
from ...models.post_services_dhcp_server_endpoint_response_401 import PostServicesDHCPServerEndpointResponse401
from ...models.post_services_dhcp_server_endpoint_response_403 import PostServicesDHCPServerEndpointResponse403
from ...models.post_services_dhcp_server_endpoint_response_404 import PostServicesDHCPServerEndpointResponse404
from ...models.post_services_dhcp_server_endpoint_response_405 import PostServicesDHCPServerEndpointResponse405
from ...models.post_services_dhcp_server_endpoint_response_406 import PostServicesDHCPServerEndpointResponse406
from ...models.post_services_dhcp_server_endpoint_response_409 import PostServicesDHCPServerEndpointResponse409
from ...models.post_services_dhcp_server_endpoint_response_415 import PostServicesDHCPServerEndpointResponse415
from ...models.post_services_dhcp_server_endpoint_response_422 import PostServicesDHCPServerEndpointResponse422
from ...models.post_services_dhcp_server_endpoint_response_424 import PostServicesDHCPServerEndpointResponse424
from ...models.post_services_dhcp_server_endpoint_response_500 import PostServicesDHCPServerEndpointResponse500
from ...models.post_services_dhcp_server_endpoint_response_503 import PostServicesDHCPServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDHCPServerEndpointJsonBody | PostServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dhcp_server",
    }

    if isinstance(body, PostServicesDHCPServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDHCPServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDHCPServerEndpointResponse400
    | PostServicesDHCPServerEndpointResponse401
    | PostServicesDHCPServerEndpointResponse403
    | PostServicesDHCPServerEndpointResponse404
    | PostServicesDHCPServerEndpointResponse405
    | PostServicesDHCPServerEndpointResponse406
    | PostServicesDHCPServerEndpointResponse409
    | PostServicesDHCPServerEndpointResponse415
    | PostServicesDHCPServerEndpointResponse422
    | PostServicesDHCPServerEndpointResponse424
    | PostServicesDHCPServerEndpointResponse500
    | PostServicesDHCPServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDHCPServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDHCPServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDHCPServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDHCPServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDHCPServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDHCPServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDHCPServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDHCPServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDHCPServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDHCPServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDHCPServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDHCPServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDHCPServerEndpointResponse400
    | PostServicesDHCPServerEndpointResponse401
    | PostServicesDHCPServerEndpointResponse403
    | PostServicesDHCPServerEndpointResponse404
    | PostServicesDHCPServerEndpointResponse405
    | PostServicesDHCPServerEndpointResponse406
    | PostServicesDHCPServerEndpointResponse409
    | PostServicesDHCPServerEndpointResponse415
    | PostServicesDHCPServerEndpointResponse422
    | PostServicesDHCPServerEndpointResponse424
    | PostServicesDHCPServerEndpointResponse500
    | PostServicesDHCPServerEndpointResponse503
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
    body: PostServicesDHCPServerEndpointJsonBody | PostServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesDHCPServerEndpointResponse400
    | PostServicesDHCPServerEndpointResponse401
    | PostServicesDHCPServerEndpointResponse403
    | PostServicesDHCPServerEndpointResponse404
    | PostServicesDHCPServerEndpointResponse405
    | PostServicesDHCPServerEndpointResponse406
    | PostServicesDHCPServerEndpointResponse409
    | PostServicesDHCPServerEndpointResponse415
    | PostServicesDHCPServerEndpointResponse422
    | PostServicesDHCPServerEndpointResponse424
    | PostServicesDHCPServerEndpointResponse500
    | PostServicesDHCPServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerEndpointJsonBody | Unset):
        body (PostServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDHCPServerEndpointResponse400 | PostServicesDHCPServerEndpointResponse401 | PostServicesDHCPServerEndpointResponse403 | PostServicesDHCPServerEndpointResponse404 | PostServicesDHCPServerEndpointResponse405 | PostServicesDHCPServerEndpointResponse406 | PostServicesDHCPServerEndpointResponse409 | PostServicesDHCPServerEndpointResponse415 | PostServicesDHCPServerEndpointResponse422 | PostServicesDHCPServerEndpointResponse424 | PostServicesDHCPServerEndpointResponse500 | PostServicesDHCPServerEndpointResponse503]
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
    body: PostServicesDHCPServerEndpointJsonBody | PostServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesDHCPServerEndpointResponse400
    | PostServicesDHCPServerEndpointResponse401
    | PostServicesDHCPServerEndpointResponse403
    | PostServicesDHCPServerEndpointResponse404
    | PostServicesDHCPServerEndpointResponse405
    | PostServicesDHCPServerEndpointResponse406
    | PostServicesDHCPServerEndpointResponse409
    | PostServicesDHCPServerEndpointResponse415
    | PostServicesDHCPServerEndpointResponse422
    | PostServicesDHCPServerEndpointResponse424
    | PostServicesDHCPServerEndpointResponse500
    | PostServicesDHCPServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerEndpointJsonBody | Unset):
        body (PostServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDHCPServerEndpointResponse400 | PostServicesDHCPServerEndpointResponse401 | PostServicesDHCPServerEndpointResponse403 | PostServicesDHCPServerEndpointResponse404 | PostServicesDHCPServerEndpointResponse405 | PostServicesDHCPServerEndpointResponse406 | PostServicesDHCPServerEndpointResponse409 | PostServicesDHCPServerEndpointResponse415 | PostServicesDHCPServerEndpointResponse422 | PostServicesDHCPServerEndpointResponse424 | PostServicesDHCPServerEndpointResponse500 | PostServicesDHCPServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDHCPServerEndpointJsonBody | PostServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesDHCPServerEndpointResponse400
    | PostServicesDHCPServerEndpointResponse401
    | PostServicesDHCPServerEndpointResponse403
    | PostServicesDHCPServerEndpointResponse404
    | PostServicesDHCPServerEndpointResponse405
    | PostServicesDHCPServerEndpointResponse406
    | PostServicesDHCPServerEndpointResponse409
    | PostServicesDHCPServerEndpointResponse415
    | PostServicesDHCPServerEndpointResponse422
    | PostServicesDHCPServerEndpointResponse424
    | PostServicesDHCPServerEndpointResponse500
    | PostServicesDHCPServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerEndpointJsonBody | Unset):
        body (PostServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDHCPServerEndpointResponse400 | PostServicesDHCPServerEndpointResponse401 | PostServicesDHCPServerEndpointResponse403 | PostServicesDHCPServerEndpointResponse404 | PostServicesDHCPServerEndpointResponse405 | PostServicesDHCPServerEndpointResponse406 | PostServicesDHCPServerEndpointResponse409 | PostServicesDHCPServerEndpointResponse415 | PostServicesDHCPServerEndpointResponse422 | PostServicesDHCPServerEndpointResponse424 | PostServicesDHCPServerEndpointResponse500 | PostServicesDHCPServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDHCPServerEndpointJsonBody | PostServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesDHCPServerEndpointResponse400
    | PostServicesDHCPServerEndpointResponse401
    | PostServicesDHCPServerEndpointResponse403
    | PostServicesDHCPServerEndpointResponse404
    | PostServicesDHCPServerEndpointResponse405
    | PostServicesDHCPServerEndpointResponse406
    | PostServicesDHCPServerEndpointResponse409
    | PostServicesDHCPServerEndpointResponse415
    | PostServicesDHCPServerEndpointResponse422
    | PostServicesDHCPServerEndpointResponse424
    | PostServicesDHCPServerEndpointResponse500
    | PostServicesDHCPServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerEndpointJsonBody | Unset):
        body (PostServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDHCPServerEndpointResponse400 | PostServicesDHCPServerEndpointResponse401 | PostServicesDHCPServerEndpointResponse403 | PostServicesDHCPServerEndpointResponse404 | PostServicesDHCPServerEndpointResponse405 | PostServicesDHCPServerEndpointResponse406 | PostServicesDHCPServerEndpointResponse409 | PostServicesDHCPServerEndpointResponse415 | PostServicesDHCPServerEndpointResponse422 | PostServicesDHCPServerEndpointResponse424 | PostServicesDHCPServerEndpointResponse500 | PostServicesDHCPServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
