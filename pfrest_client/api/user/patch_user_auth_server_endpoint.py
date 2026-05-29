from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_user_auth_server_endpoint_data_body import PatchUserAuthServerEndpointDataBody
from ...models.patch_user_auth_server_endpoint_json_body import PatchUserAuthServerEndpointJsonBody
from ...models.patch_user_auth_server_endpoint_response_400 import PatchUserAuthServerEndpointResponse400
from ...models.patch_user_auth_server_endpoint_response_401 import PatchUserAuthServerEndpointResponse401
from ...models.patch_user_auth_server_endpoint_response_403 import PatchUserAuthServerEndpointResponse403
from ...models.patch_user_auth_server_endpoint_response_404 import PatchUserAuthServerEndpointResponse404
from ...models.patch_user_auth_server_endpoint_response_405 import PatchUserAuthServerEndpointResponse405
from ...models.patch_user_auth_server_endpoint_response_406 import PatchUserAuthServerEndpointResponse406
from ...models.patch_user_auth_server_endpoint_response_409 import PatchUserAuthServerEndpointResponse409
from ...models.patch_user_auth_server_endpoint_response_415 import PatchUserAuthServerEndpointResponse415
from ...models.patch_user_auth_server_endpoint_response_422 import PatchUserAuthServerEndpointResponse422
from ...models.patch_user_auth_server_endpoint_response_424 import PatchUserAuthServerEndpointResponse424
from ...models.patch_user_auth_server_endpoint_response_500 import PatchUserAuthServerEndpointResponse500
from ...models.patch_user_auth_server_endpoint_response_503 import PatchUserAuthServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchUserAuthServerEndpointJsonBody | PatchUserAuthServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/user/auth_server",
    }

    if isinstance(body, PatchUserAuthServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchUserAuthServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchUserAuthServerEndpointResponse400
    | PatchUserAuthServerEndpointResponse401
    | PatchUserAuthServerEndpointResponse403
    | PatchUserAuthServerEndpointResponse404
    | PatchUserAuthServerEndpointResponse405
    | PatchUserAuthServerEndpointResponse406
    | PatchUserAuthServerEndpointResponse409
    | PatchUserAuthServerEndpointResponse415
    | PatchUserAuthServerEndpointResponse422
    | PatchUserAuthServerEndpointResponse424
    | PatchUserAuthServerEndpointResponse500
    | PatchUserAuthServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchUserAuthServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchUserAuthServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchUserAuthServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchUserAuthServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchUserAuthServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchUserAuthServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchUserAuthServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchUserAuthServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchUserAuthServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchUserAuthServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchUserAuthServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchUserAuthServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchUserAuthServerEndpointResponse400
    | PatchUserAuthServerEndpointResponse401
    | PatchUserAuthServerEndpointResponse403
    | PatchUserAuthServerEndpointResponse404
    | PatchUserAuthServerEndpointResponse405
    | PatchUserAuthServerEndpointResponse406
    | PatchUserAuthServerEndpointResponse409
    | PatchUserAuthServerEndpointResponse415
    | PatchUserAuthServerEndpointResponse422
    | PatchUserAuthServerEndpointResponse424
    | PatchUserAuthServerEndpointResponse500
    | PatchUserAuthServerEndpointResponse503
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
    body: PatchUserAuthServerEndpointJsonBody | PatchUserAuthServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchUserAuthServerEndpointResponse400
    | PatchUserAuthServerEndpointResponse401
    | PatchUserAuthServerEndpointResponse403
    | PatchUserAuthServerEndpointResponse404
    | PatchUserAuthServerEndpointResponse405
    | PatchUserAuthServerEndpointResponse406
    | PatchUserAuthServerEndpointResponse409
    | PatchUserAuthServerEndpointResponse415
    | PatchUserAuthServerEndpointResponse422
    | PatchUserAuthServerEndpointResponse424
    | PatchUserAuthServerEndpointResponse500
    | PatchUserAuthServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing authentication server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchUserAuthServerEndpointJsonBody | Unset):
        body (PatchUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUserAuthServerEndpointResponse400 | PatchUserAuthServerEndpointResponse401 | PatchUserAuthServerEndpointResponse403 | PatchUserAuthServerEndpointResponse404 | PatchUserAuthServerEndpointResponse405 | PatchUserAuthServerEndpointResponse406 | PatchUserAuthServerEndpointResponse409 | PatchUserAuthServerEndpointResponse415 | PatchUserAuthServerEndpointResponse422 | PatchUserAuthServerEndpointResponse424 | PatchUserAuthServerEndpointResponse500 | PatchUserAuthServerEndpointResponse503]
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
    body: PatchUserAuthServerEndpointJsonBody | PatchUserAuthServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchUserAuthServerEndpointResponse400
    | PatchUserAuthServerEndpointResponse401
    | PatchUserAuthServerEndpointResponse403
    | PatchUserAuthServerEndpointResponse404
    | PatchUserAuthServerEndpointResponse405
    | PatchUserAuthServerEndpointResponse406
    | PatchUserAuthServerEndpointResponse409
    | PatchUserAuthServerEndpointResponse415
    | PatchUserAuthServerEndpointResponse422
    | PatchUserAuthServerEndpointResponse424
    | PatchUserAuthServerEndpointResponse500
    | PatchUserAuthServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing authentication server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchUserAuthServerEndpointJsonBody | Unset):
        body (PatchUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUserAuthServerEndpointResponse400 | PatchUserAuthServerEndpointResponse401 | PatchUserAuthServerEndpointResponse403 | PatchUserAuthServerEndpointResponse404 | PatchUserAuthServerEndpointResponse405 | PatchUserAuthServerEndpointResponse406 | PatchUserAuthServerEndpointResponse409 | PatchUserAuthServerEndpointResponse415 | PatchUserAuthServerEndpointResponse422 | PatchUserAuthServerEndpointResponse424 | PatchUserAuthServerEndpointResponse500 | PatchUserAuthServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchUserAuthServerEndpointJsonBody | PatchUserAuthServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchUserAuthServerEndpointResponse400
    | PatchUserAuthServerEndpointResponse401
    | PatchUserAuthServerEndpointResponse403
    | PatchUserAuthServerEndpointResponse404
    | PatchUserAuthServerEndpointResponse405
    | PatchUserAuthServerEndpointResponse406
    | PatchUserAuthServerEndpointResponse409
    | PatchUserAuthServerEndpointResponse415
    | PatchUserAuthServerEndpointResponse422
    | PatchUserAuthServerEndpointResponse424
    | PatchUserAuthServerEndpointResponse500
    | PatchUserAuthServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing authentication server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchUserAuthServerEndpointJsonBody | Unset):
        body (PatchUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUserAuthServerEndpointResponse400 | PatchUserAuthServerEndpointResponse401 | PatchUserAuthServerEndpointResponse403 | PatchUserAuthServerEndpointResponse404 | PatchUserAuthServerEndpointResponse405 | PatchUserAuthServerEndpointResponse406 | PatchUserAuthServerEndpointResponse409 | PatchUserAuthServerEndpointResponse415 | PatchUserAuthServerEndpointResponse422 | PatchUserAuthServerEndpointResponse424 | PatchUserAuthServerEndpointResponse500 | PatchUserAuthServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchUserAuthServerEndpointJsonBody | PatchUserAuthServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchUserAuthServerEndpointResponse400
    | PatchUserAuthServerEndpointResponse401
    | PatchUserAuthServerEndpointResponse403
    | PatchUserAuthServerEndpointResponse404
    | PatchUserAuthServerEndpointResponse405
    | PatchUserAuthServerEndpointResponse406
    | PatchUserAuthServerEndpointResponse409
    | PatchUserAuthServerEndpointResponse415
    | PatchUserAuthServerEndpointResponse422
    | PatchUserAuthServerEndpointResponse424
    | PatchUserAuthServerEndpointResponse500
    | PatchUserAuthServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing authentication server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchUserAuthServerEndpointJsonBody | Unset):
        body (PatchUserAuthServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUserAuthServerEndpointResponse400 | PatchUserAuthServerEndpointResponse401 | PatchUserAuthServerEndpointResponse403 | PatchUserAuthServerEndpointResponse404 | PatchUserAuthServerEndpointResponse405 | PatchUserAuthServerEndpointResponse406 | PatchUserAuthServerEndpointResponse409 | PatchUserAuthServerEndpointResponse415 | PatchUserAuthServerEndpointResponse422 | PatchUserAuthServerEndpointResponse424 | PatchUserAuthServerEndpointResponse500 | PatchUserAuthServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
