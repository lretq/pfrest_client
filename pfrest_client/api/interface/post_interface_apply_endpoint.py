from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_interface_apply_endpoint_data_body import PostInterfaceApplyEndpointDataBody
from ...models.post_interface_apply_endpoint_json_body import PostInterfaceApplyEndpointJsonBody
from ...models.post_interface_apply_endpoint_response_400 import PostInterfaceApplyEndpointResponse400
from ...models.post_interface_apply_endpoint_response_401 import PostInterfaceApplyEndpointResponse401
from ...models.post_interface_apply_endpoint_response_403 import PostInterfaceApplyEndpointResponse403
from ...models.post_interface_apply_endpoint_response_404 import PostInterfaceApplyEndpointResponse404
from ...models.post_interface_apply_endpoint_response_405 import PostInterfaceApplyEndpointResponse405
from ...models.post_interface_apply_endpoint_response_406 import PostInterfaceApplyEndpointResponse406
from ...models.post_interface_apply_endpoint_response_409 import PostInterfaceApplyEndpointResponse409
from ...models.post_interface_apply_endpoint_response_415 import PostInterfaceApplyEndpointResponse415
from ...models.post_interface_apply_endpoint_response_422 import PostInterfaceApplyEndpointResponse422
from ...models.post_interface_apply_endpoint_response_424 import PostInterfaceApplyEndpointResponse424
from ...models.post_interface_apply_endpoint_response_500 import PostInterfaceApplyEndpointResponse500
from ...models.post_interface_apply_endpoint_response_503 import PostInterfaceApplyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostInterfaceApplyEndpointJsonBody | PostInterfaceApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/interface/apply",
    }

    if isinstance(body, PostInterfaceApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostInterfaceApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostInterfaceApplyEndpointResponse400
    | PostInterfaceApplyEndpointResponse401
    | PostInterfaceApplyEndpointResponse403
    | PostInterfaceApplyEndpointResponse404
    | PostInterfaceApplyEndpointResponse405
    | PostInterfaceApplyEndpointResponse406
    | PostInterfaceApplyEndpointResponse409
    | PostInterfaceApplyEndpointResponse415
    | PostInterfaceApplyEndpointResponse422
    | PostInterfaceApplyEndpointResponse424
    | PostInterfaceApplyEndpointResponse500
    | PostInterfaceApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostInterfaceApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostInterfaceApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostInterfaceApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostInterfaceApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostInterfaceApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostInterfaceApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostInterfaceApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostInterfaceApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostInterfaceApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostInterfaceApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostInterfaceApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostInterfaceApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostInterfaceApplyEndpointResponse400
    | PostInterfaceApplyEndpointResponse401
    | PostInterfaceApplyEndpointResponse403
    | PostInterfaceApplyEndpointResponse404
    | PostInterfaceApplyEndpointResponse405
    | PostInterfaceApplyEndpointResponse406
    | PostInterfaceApplyEndpointResponse409
    | PostInterfaceApplyEndpointResponse415
    | PostInterfaceApplyEndpointResponse422
    | PostInterfaceApplyEndpointResponse424
    | PostInterfaceApplyEndpointResponse500
    | PostInterfaceApplyEndpointResponse503
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
    body: PostInterfaceApplyEndpointJsonBody | PostInterfaceApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceApplyEndpointResponse400
    | PostInterfaceApplyEndpointResponse401
    | PostInterfaceApplyEndpointResponse403
    | PostInterfaceApplyEndpointResponse404
    | PostInterfaceApplyEndpointResponse405
    | PostInterfaceApplyEndpointResponse406
    | PostInterfaceApplyEndpointResponse409
    | PostInterfaceApplyEndpointResponse415
    | PostInterfaceApplyEndpointResponse422
    | PostInterfaceApplyEndpointResponse424
    | PostInterfaceApplyEndpointResponse500
    | PostInterfaceApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending interface changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceApplyEndpointJsonBody | Unset):
        body (PostInterfaceApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceApplyEndpointResponse400 | PostInterfaceApplyEndpointResponse401 | PostInterfaceApplyEndpointResponse403 | PostInterfaceApplyEndpointResponse404 | PostInterfaceApplyEndpointResponse405 | PostInterfaceApplyEndpointResponse406 | PostInterfaceApplyEndpointResponse409 | PostInterfaceApplyEndpointResponse415 | PostInterfaceApplyEndpointResponse422 | PostInterfaceApplyEndpointResponse424 | PostInterfaceApplyEndpointResponse500 | PostInterfaceApplyEndpointResponse503]
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
    body: PostInterfaceApplyEndpointJsonBody | PostInterfaceApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceApplyEndpointResponse400
    | PostInterfaceApplyEndpointResponse401
    | PostInterfaceApplyEndpointResponse403
    | PostInterfaceApplyEndpointResponse404
    | PostInterfaceApplyEndpointResponse405
    | PostInterfaceApplyEndpointResponse406
    | PostInterfaceApplyEndpointResponse409
    | PostInterfaceApplyEndpointResponse415
    | PostInterfaceApplyEndpointResponse422
    | PostInterfaceApplyEndpointResponse424
    | PostInterfaceApplyEndpointResponse500
    | PostInterfaceApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending interface changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceApplyEndpointJsonBody | Unset):
        body (PostInterfaceApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceApplyEndpointResponse400 | PostInterfaceApplyEndpointResponse401 | PostInterfaceApplyEndpointResponse403 | PostInterfaceApplyEndpointResponse404 | PostInterfaceApplyEndpointResponse405 | PostInterfaceApplyEndpointResponse406 | PostInterfaceApplyEndpointResponse409 | PostInterfaceApplyEndpointResponse415 | PostInterfaceApplyEndpointResponse422 | PostInterfaceApplyEndpointResponse424 | PostInterfaceApplyEndpointResponse500 | PostInterfaceApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceApplyEndpointJsonBody | PostInterfaceApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostInterfaceApplyEndpointResponse400
    | PostInterfaceApplyEndpointResponse401
    | PostInterfaceApplyEndpointResponse403
    | PostInterfaceApplyEndpointResponse404
    | PostInterfaceApplyEndpointResponse405
    | PostInterfaceApplyEndpointResponse406
    | PostInterfaceApplyEndpointResponse409
    | PostInterfaceApplyEndpointResponse415
    | PostInterfaceApplyEndpointResponse422
    | PostInterfaceApplyEndpointResponse424
    | PostInterfaceApplyEndpointResponse500
    | PostInterfaceApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending interface changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceApplyEndpointJsonBody | Unset):
        body (PostInterfaceApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostInterfaceApplyEndpointResponse400 | PostInterfaceApplyEndpointResponse401 | PostInterfaceApplyEndpointResponse403 | PostInterfaceApplyEndpointResponse404 | PostInterfaceApplyEndpointResponse405 | PostInterfaceApplyEndpointResponse406 | PostInterfaceApplyEndpointResponse409 | PostInterfaceApplyEndpointResponse415 | PostInterfaceApplyEndpointResponse422 | PostInterfaceApplyEndpointResponse424 | PostInterfaceApplyEndpointResponse500 | PostInterfaceApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostInterfaceApplyEndpointJsonBody | PostInterfaceApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostInterfaceApplyEndpointResponse400
    | PostInterfaceApplyEndpointResponse401
    | PostInterfaceApplyEndpointResponse403
    | PostInterfaceApplyEndpointResponse404
    | PostInterfaceApplyEndpointResponse405
    | PostInterfaceApplyEndpointResponse406
    | PostInterfaceApplyEndpointResponse409
    | PostInterfaceApplyEndpointResponse415
    | PostInterfaceApplyEndpointResponse422
    | PostInterfaceApplyEndpointResponse424
    | PostInterfaceApplyEndpointResponse500
    | PostInterfaceApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending interface changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostInterfaceApplyEndpointJsonBody | Unset):
        body (PostInterfaceApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostInterfaceApplyEndpointResponse400 | PostInterfaceApplyEndpointResponse401 | PostInterfaceApplyEndpointResponse403 | PostInterfaceApplyEndpointResponse404 | PostInterfaceApplyEndpointResponse405 | PostInterfaceApplyEndpointResponse406 | PostInterfaceApplyEndpointResponse409 | PostInterfaceApplyEndpointResponse415 | PostInterfaceApplyEndpointResponse422 | PostInterfaceApplyEndpointResponse424 | PostInterfaceApplyEndpointResponse500 | PostInterfaceApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
