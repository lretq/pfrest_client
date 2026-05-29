from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_interface_vlan_endpoint_data_body import PostInterfaceVLANEndpointDataBody
from ...models.post_interface_vlan_endpoint_json_body import PostInterfaceVLANEndpointJsonBody
from ...models.post_interface_vlan_endpoint_response_400 import PostInterfaceVLANEndpointResponse400
from ...models.post_interface_vlan_endpoint_response_401 import PostInterfaceVLANEndpointResponse401
from ...models.post_interface_vlan_endpoint_response_403 import PostInterfaceVLANEndpointResponse403
from ...models.post_interface_vlan_endpoint_response_404 import PostInterfaceVLANEndpointResponse404
from ...models.post_interface_vlan_endpoint_response_405 import PostInterfaceVLANEndpointResponse405
from ...models.post_interface_vlan_endpoint_response_406 import PostInterfaceVLANEndpointResponse406
from ...models.post_interface_vlan_endpoint_response_409 import PostInterfaceVLANEndpointResponse409
from ...models.post_interface_vlan_endpoint_response_415 import PostInterfaceVLANEndpointResponse415
from ...models.post_interface_vlan_endpoint_response_422 import PostInterfaceVLANEndpointResponse422
from ...models.post_interface_vlan_endpoint_response_424 import PostInterfaceVLANEndpointResponse424
from ...models.post_interface_vlan_endpoint_response_500 import PostInterfaceVLANEndpointResponse500
from ...models.post_interface_vlan_endpoint_response_503 import PostInterfaceVLANEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostInterfaceVLANEndpointJsonBody | PostInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/interface/vlan",
    }

    if isinstance(body, PostInterfaceVLANEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostInterfaceVLANEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostInterfaceVLANEndpointResponse400
    | PostInterfaceVLANEndpointResponse401
    | PostInterfaceVLANEndpointResponse403
    | PostInterfaceVLANEndpointResponse404
    | PostInterfaceVLANEndpointResponse405
    | PostInterfaceVLANEndpointResponse406
    | PostInterfaceVLANEndpointResponse409
    | PostInterfaceVLANEndpointResponse415
    | PostInterfaceVLANEndpointResponse422
    | PostInterfaceVLANEndpointResponse424
    | PostInterfaceVLANEndpointResponse500
    | PostInterfaceVLANEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostInterfaceVLANEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostInterfaceVLANEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostInterfaceVLANEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostInterfaceVLANEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostInterfaceVLANEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostInterfaceVLANEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostInterfaceVLANEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostInterfaceVLANEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostInterfaceVLANEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostInterfaceVLANEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostInterfaceVLANEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostInterfaceVLANEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostInterfaceVLANEndpointResponse400
    | PostInterfaceVLANEndpointResponse401
    | PostInterfaceVLANEndpointResponse403
    | PostInterfaceVLANEndpointResponse404
    | PostInterfaceVLANEndpointResponse405
    | PostInterfaceVLANEndpointResponse406
    | PostInterfaceVLANEndpointResponse409
    | PostInterfaceVLANEndpointResponse415
    | PostInterfaceVLANEndpointResponse422
    | PostInterfaceVLANEndpointResponse424
    | PostInterfaceVLANEndpointResponse500
    | PostInterfaceVLANEndpointResponse503
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
    body: PostInterfaceVLANEndpointJsonBody | PostInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceVLANEndpointResponse400
    | PostInterfaceVLANEndpointResponse401
    | PostInterfaceVLANEndpointResponse403
    | PostInterfaceVLANEndpointResponse404
    | PostInterfaceVLANEndpointResponse405
    | PostInterfaceVLANEndpointResponse406
    | PostInterfaceVLANEndpointResponse409
    | PostInterfaceVLANEndpointResponse415
    | PostInterfaceVLANEndpointResponse422
    | PostInterfaceVLANEndpointResponse424
    | PostInterfaceVLANEndpointResponse500
    | PostInterfaceVLANEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceVLANEndpointJsonBody | Unset):
        body (PostInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceVLANEndpointResponse400 | PostInterfaceVLANEndpointResponse401 | PostInterfaceVLANEndpointResponse403 | PostInterfaceVLANEndpointResponse404 | PostInterfaceVLANEndpointResponse405 | PostInterfaceVLANEndpointResponse406 | PostInterfaceVLANEndpointResponse409 | PostInterfaceVLANEndpointResponse415 | PostInterfaceVLANEndpointResponse422 | PostInterfaceVLANEndpointResponse424 | PostInterfaceVLANEndpointResponse500 | PostInterfaceVLANEndpointResponse503]
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
    body: PostInterfaceVLANEndpointJsonBody | PostInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceVLANEndpointResponse400
    | PostInterfaceVLANEndpointResponse401
    | PostInterfaceVLANEndpointResponse403
    | PostInterfaceVLANEndpointResponse404
    | PostInterfaceVLANEndpointResponse405
    | PostInterfaceVLANEndpointResponse406
    | PostInterfaceVLANEndpointResponse409
    | PostInterfaceVLANEndpointResponse415
    | PostInterfaceVLANEndpointResponse422
    | PostInterfaceVLANEndpointResponse424
    | PostInterfaceVLANEndpointResponse500
    | PostInterfaceVLANEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceVLANEndpointJsonBody | Unset):
        body (PostInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceVLANEndpointResponse400 | PostInterfaceVLANEndpointResponse401 | PostInterfaceVLANEndpointResponse403 | PostInterfaceVLANEndpointResponse404 | PostInterfaceVLANEndpointResponse405 | PostInterfaceVLANEndpointResponse406 | PostInterfaceVLANEndpointResponse409 | PostInterfaceVLANEndpointResponse415 | PostInterfaceVLANEndpointResponse422 | PostInterfaceVLANEndpointResponse424 | PostInterfaceVLANEndpointResponse500 | PostInterfaceVLANEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceVLANEndpointJsonBody | PostInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceVLANEndpointResponse400
    | PostInterfaceVLANEndpointResponse401
    | PostInterfaceVLANEndpointResponse403
    | PostInterfaceVLANEndpointResponse404
    | PostInterfaceVLANEndpointResponse405
    | PostInterfaceVLANEndpointResponse406
    | PostInterfaceVLANEndpointResponse409
    | PostInterfaceVLANEndpointResponse415
    | PostInterfaceVLANEndpointResponse422
    | PostInterfaceVLANEndpointResponse424
    | PostInterfaceVLANEndpointResponse500
    | PostInterfaceVLANEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceVLANEndpointJsonBody | Unset):
        body (PostInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceVLANEndpointResponse400 | PostInterfaceVLANEndpointResponse401 | PostInterfaceVLANEndpointResponse403 | PostInterfaceVLANEndpointResponse404 | PostInterfaceVLANEndpointResponse405 | PostInterfaceVLANEndpointResponse406 | PostInterfaceVLANEndpointResponse409 | PostInterfaceVLANEndpointResponse415 | PostInterfaceVLANEndpointResponse422 | PostInterfaceVLANEndpointResponse424 | PostInterfaceVLANEndpointResponse500 | PostInterfaceVLANEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceVLANEndpointJsonBody | PostInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceVLANEndpointResponse400
    | PostInterfaceVLANEndpointResponse401
    | PostInterfaceVLANEndpointResponse403
    | PostInterfaceVLANEndpointResponse404
    | PostInterfaceVLANEndpointResponse405
    | PostInterfaceVLANEndpointResponse406
    | PostInterfaceVLANEndpointResponse409
    | PostInterfaceVLANEndpointResponse415
    | PostInterfaceVLANEndpointResponse422
    | PostInterfaceVLANEndpointResponse424
    | PostInterfaceVLANEndpointResponse500
    | PostInterfaceVLANEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceVLANEndpointJsonBody | Unset):
        body (PostInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceVLANEndpointResponse400 | PostInterfaceVLANEndpointResponse401 | PostInterfaceVLANEndpointResponse403 | PostInterfaceVLANEndpointResponse404 | PostInterfaceVLANEndpointResponse405 | PostInterfaceVLANEndpointResponse406 | PostInterfaceVLANEndpointResponse409 | PostInterfaceVLANEndpointResponse415 | PostInterfaceVLANEndpointResponse422 | PostInterfaceVLANEndpointResponse424 | PostInterfaceVLANEndpointResponse500 | PostInterfaceVLANEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
