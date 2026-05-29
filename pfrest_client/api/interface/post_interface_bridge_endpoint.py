from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_interface_bridge_endpoint_data_body import PostInterfaceBridgeEndpointDataBody
from ...models.post_interface_bridge_endpoint_json_body import PostInterfaceBridgeEndpointJsonBody
from ...models.post_interface_bridge_endpoint_response_400 import PostInterfaceBridgeEndpointResponse400
from ...models.post_interface_bridge_endpoint_response_401 import PostInterfaceBridgeEndpointResponse401
from ...models.post_interface_bridge_endpoint_response_403 import PostInterfaceBridgeEndpointResponse403
from ...models.post_interface_bridge_endpoint_response_404 import PostInterfaceBridgeEndpointResponse404
from ...models.post_interface_bridge_endpoint_response_405 import PostInterfaceBridgeEndpointResponse405
from ...models.post_interface_bridge_endpoint_response_406 import PostInterfaceBridgeEndpointResponse406
from ...models.post_interface_bridge_endpoint_response_409 import PostInterfaceBridgeEndpointResponse409
from ...models.post_interface_bridge_endpoint_response_415 import PostInterfaceBridgeEndpointResponse415
from ...models.post_interface_bridge_endpoint_response_422 import PostInterfaceBridgeEndpointResponse422
from ...models.post_interface_bridge_endpoint_response_424 import PostInterfaceBridgeEndpointResponse424
from ...models.post_interface_bridge_endpoint_response_500 import PostInterfaceBridgeEndpointResponse500
from ...models.post_interface_bridge_endpoint_response_503 import PostInterfaceBridgeEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostInterfaceBridgeEndpointJsonBody | PostInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/interface/bridge",
    }

    if isinstance(body, PostInterfaceBridgeEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostInterfaceBridgeEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostInterfaceBridgeEndpointResponse400
    | PostInterfaceBridgeEndpointResponse401
    | PostInterfaceBridgeEndpointResponse403
    | PostInterfaceBridgeEndpointResponse404
    | PostInterfaceBridgeEndpointResponse405
    | PostInterfaceBridgeEndpointResponse406
    | PostInterfaceBridgeEndpointResponse409
    | PostInterfaceBridgeEndpointResponse415
    | PostInterfaceBridgeEndpointResponse422
    | PostInterfaceBridgeEndpointResponse424
    | PostInterfaceBridgeEndpointResponse500
    | PostInterfaceBridgeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostInterfaceBridgeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostInterfaceBridgeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostInterfaceBridgeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostInterfaceBridgeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostInterfaceBridgeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostInterfaceBridgeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostInterfaceBridgeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostInterfaceBridgeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostInterfaceBridgeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostInterfaceBridgeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostInterfaceBridgeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostInterfaceBridgeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostInterfaceBridgeEndpointResponse400
    | PostInterfaceBridgeEndpointResponse401
    | PostInterfaceBridgeEndpointResponse403
    | PostInterfaceBridgeEndpointResponse404
    | PostInterfaceBridgeEndpointResponse405
    | PostInterfaceBridgeEndpointResponse406
    | PostInterfaceBridgeEndpointResponse409
    | PostInterfaceBridgeEndpointResponse415
    | PostInterfaceBridgeEndpointResponse422
    | PostInterfaceBridgeEndpointResponse424
    | PostInterfaceBridgeEndpointResponse500
    | PostInterfaceBridgeEndpointResponse503
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
    body: PostInterfaceBridgeEndpointJsonBody | PostInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceBridgeEndpointResponse400
    | PostInterfaceBridgeEndpointResponse401
    | PostInterfaceBridgeEndpointResponse403
    | PostInterfaceBridgeEndpointResponse404
    | PostInterfaceBridgeEndpointResponse405
    | PostInterfaceBridgeEndpointResponse406
    | PostInterfaceBridgeEndpointResponse409
    | PostInterfaceBridgeEndpointResponse415
    | PostInterfaceBridgeEndpointResponse422
    | PostInterfaceBridgeEndpointResponse424
    | PostInterfaceBridgeEndpointResponse500
    | PostInterfaceBridgeEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceBridgeEndpointJsonBody | Unset):
        body (PostInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceBridgeEndpointResponse400 | PostInterfaceBridgeEndpointResponse401 | PostInterfaceBridgeEndpointResponse403 | PostInterfaceBridgeEndpointResponse404 | PostInterfaceBridgeEndpointResponse405 | PostInterfaceBridgeEndpointResponse406 | PostInterfaceBridgeEndpointResponse409 | PostInterfaceBridgeEndpointResponse415 | PostInterfaceBridgeEndpointResponse422 | PostInterfaceBridgeEndpointResponse424 | PostInterfaceBridgeEndpointResponse500 | PostInterfaceBridgeEndpointResponse503]
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
    body: PostInterfaceBridgeEndpointJsonBody | PostInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceBridgeEndpointResponse400
    | PostInterfaceBridgeEndpointResponse401
    | PostInterfaceBridgeEndpointResponse403
    | PostInterfaceBridgeEndpointResponse404
    | PostInterfaceBridgeEndpointResponse405
    | PostInterfaceBridgeEndpointResponse406
    | PostInterfaceBridgeEndpointResponse409
    | PostInterfaceBridgeEndpointResponse415
    | PostInterfaceBridgeEndpointResponse422
    | PostInterfaceBridgeEndpointResponse424
    | PostInterfaceBridgeEndpointResponse500
    | PostInterfaceBridgeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceBridgeEndpointJsonBody | Unset):
        body (PostInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceBridgeEndpointResponse400 | PostInterfaceBridgeEndpointResponse401 | PostInterfaceBridgeEndpointResponse403 | PostInterfaceBridgeEndpointResponse404 | PostInterfaceBridgeEndpointResponse405 | PostInterfaceBridgeEndpointResponse406 | PostInterfaceBridgeEndpointResponse409 | PostInterfaceBridgeEndpointResponse415 | PostInterfaceBridgeEndpointResponse422 | PostInterfaceBridgeEndpointResponse424 | PostInterfaceBridgeEndpointResponse500 | PostInterfaceBridgeEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceBridgeEndpointJsonBody | PostInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceBridgeEndpointResponse400
    | PostInterfaceBridgeEndpointResponse401
    | PostInterfaceBridgeEndpointResponse403
    | PostInterfaceBridgeEndpointResponse404
    | PostInterfaceBridgeEndpointResponse405
    | PostInterfaceBridgeEndpointResponse406
    | PostInterfaceBridgeEndpointResponse409
    | PostInterfaceBridgeEndpointResponse415
    | PostInterfaceBridgeEndpointResponse422
    | PostInterfaceBridgeEndpointResponse424
    | PostInterfaceBridgeEndpointResponse500
    | PostInterfaceBridgeEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceBridgeEndpointJsonBody | Unset):
        body (PostInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceBridgeEndpointResponse400 | PostInterfaceBridgeEndpointResponse401 | PostInterfaceBridgeEndpointResponse403 | PostInterfaceBridgeEndpointResponse404 | PostInterfaceBridgeEndpointResponse405 | PostInterfaceBridgeEndpointResponse406 | PostInterfaceBridgeEndpointResponse409 | PostInterfaceBridgeEndpointResponse415 | PostInterfaceBridgeEndpointResponse422 | PostInterfaceBridgeEndpointResponse424 | PostInterfaceBridgeEndpointResponse500 | PostInterfaceBridgeEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceBridgeEndpointJsonBody | PostInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceBridgeEndpointResponse400
    | PostInterfaceBridgeEndpointResponse401
    | PostInterfaceBridgeEndpointResponse403
    | PostInterfaceBridgeEndpointResponse404
    | PostInterfaceBridgeEndpointResponse405
    | PostInterfaceBridgeEndpointResponse406
    | PostInterfaceBridgeEndpointResponse409
    | PostInterfaceBridgeEndpointResponse415
    | PostInterfaceBridgeEndpointResponse422
    | PostInterfaceBridgeEndpointResponse424
    | PostInterfaceBridgeEndpointResponse500
    | PostInterfaceBridgeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceBridgeEndpointJsonBody | Unset):
        body (PostInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceBridgeEndpointResponse400 | PostInterfaceBridgeEndpointResponse401 | PostInterfaceBridgeEndpointResponse403 | PostInterfaceBridgeEndpointResponse404 | PostInterfaceBridgeEndpointResponse405 | PostInterfaceBridgeEndpointResponse406 | PostInterfaceBridgeEndpointResponse409 | PostInterfaceBridgeEndpointResponse415 | PostInterfaceBridgeEndpointResponse422 | PostInterfaceBridgeEndpointResponse424 | PostInterfaceBridgeEndpointResponse500 | PostInterfaceBridgeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
