from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_group_endpoint_response_400 import DeleteUserGroupEndpointResponse400
from ...models.delete_user_group_endpoint_response_401 import DeleteUserGroupEndpointResponse401
from ...models.delete_user_group_endpoint_response_403 import DeleteUserGroupEndpointResponse403
from ...models.delete_user_group_endpoint_response_404 import DeleteUserGroupEndpointResponse404
from ...models.delete_user_group_endpoint_response_405 import DeleteUserGroupEndpointResponse405
from ...models.delete_user_group_endpoint_response_406 import DeleteUserGroupEndpointResponse406
from ...models.delete_user_group_endpoint_response_409 import DeleteUserGroupEndpointResponse409
from ...models.delete_user_group_endpoint_response_415 import DeleteUserGroupEndpointResponse415
from ...models.delete_user_group_endpoint_response_422 import DeleteUserGroupEndpointResponse422
from ...models.delete_user_group_endpoint_response_424 import DeleteUserGroupEndpointResponse424
from ...models.delete_user_group_endpoint_response_500 import DeleteUserGroupEndpointResponse500
from ...models.delete_user_group_endpoint_response_503 import DeleteUserGroupEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/user/group",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteUserGroupEndpointResponse400
    | DeleteUserGroupEndpointResponse401
    | DeleteUserGroupEndpointResponse403
    | DeleteUserGroupEndpointResponse404
    | DeleteUserGroupEndpointResponse405
    | DeleteUserGroupEndpointResponse406
    | DeleteUserGroupEndpointResponse409
    | DeleteUserGroupEndpointResponse415
    | DeleteUserGroupEndpointResponse422
    | DeleteUserGroupEndpointResponse424
    | DeleteUserGroupEndpointResponse500
    | DeleteUserGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteUserGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteUserGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteUserGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteUserGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteUserGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteUserGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteUserGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteUserGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteUserGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteUserGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteUserGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteUserGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteUserGroupEndpointResponse400
    | DeleteUserGroupEndpointResponse401
    | DeleteUserGroupEndpointResponse403
    | DeleteUserGroupEndpointResponse404
    | DeleteUserGroupEndpointResponse405
    | DeleteUserGroupEndpointResponse406
    | DeleteUserGroupEndpointResponse409
    | DeleteUserGroupEndpointResponse415
    | DeleteUserGroupEndpointResponse422
    | DeleteUserGroupEndpointResponse424
    | DeleteUserGroupEndpointResponse500
    | DeleteUserGroupEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteUserGroupEndpointResponse400
    | DeleteUserGroupEndpointResponse401
    | DeleteUserGroupEndpointResponse403
    | DeleteUserGroupEndpointResponse404
    | DeleteUserGroupEndpointResponse405
    | DeleteUserGroupEndpointResponse406
    | DeleteUserGroupEndpointResponse409
    | DeleteUserGroupEndpointResponse415
    | DeleteUserGroupEndpointResponse422
    | DeleteUserGroupEndpointResponse424
    | DeleteUserGroupEndpointResponse500
    | DeleteUserGroupEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserGroupEndpointResponse400 | DeleteUserGroupEndpointResponse401 | DeleteUserGroupEndpointResponse403 | DeleteUserGroupEndpointResponse404 | DeleteUserGroupEndpointResponse405 | DeleteUserGroupEndpointResponse406 | DeleteUserGroupEndpointResponse409 | DeleteUserGroupEndpointResponse415 | DeleteUserGroupEndpointResponse422 | DeleteUserGroupEndpointResponse424 | DeleteUserGroupEndpointResponse500 | DeleteUserGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteUserGroupEndpointResponse400
    | DeleteUserGroupEndpointResponse401
    | DeleteUserGroupEndpointResponse403
    | DeleteUserGroupEndpointResponse404
    | DeleteUserGroupEndpointResponse405
    | DeleteUserGroupEndpointResponse406
    | DeleteUserGroupEndpointResponse409
    | DeleteUserGroupEndpointResponse415
    | DeleteUserGroupEndpointResponse422
    | DeleteUserGroupEndpointResponse424
    | DeleteUserGroupEndpointResponse500
    | DeleteUserGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserGroupEndpointResponse400 | DeleteUserGroupEndpointResponse401 | DeleteUserGroupEndpointResponse403 | DeleteUserGroupEndpointResponse404 | DeleteUserGroupEndpointResponse405 | DeleteUserGroupEndpointResponse406 | DeleteUserGroupEndpointResponse409 | DeleteUserGroupEndpointResponse415 | DeleteUserGroupEndpointResponse422 | DeleteUserGroupEndpointResponse424 | DeleteUserGroupEndpointResponse500 | DeleteUserGroupEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteUserGroupEndpointResponse400
    | DeleteUserGroupEndpointResponse401
    | DeleteUserGroupEndpointResponse403
    | DeleteUserGroupEndpointResponse404
    | DeleteUserGroupEndpointResponse405
    | DeleteUserGroupEndpointResponse406
    | DeleteUserGroupEndpointResponse409
    | DeleteUserGroupEndpointResponse415
    | DeleteUserGroupEndpointResponse422
    | DeleteUserGroupEndpointResponse424
    | DeleteUserGroupEndpointResponse500
    | DeleteUserGroupEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserGroupEndpointResponse400 | DeleteUserGroupEndpointResponse401 | DeleteUserGroupEndpointResponse403 | DeleteUserGroupEndpointResponse404 | DeleteUserGroupEndpointResponse405 | DeleteUserGroupEndpointResponse406 | DeleteUserGroupEndpointResponse409 | DeleteUserGroupEndpointResponse415 | DeleteUserGroupEndpointResponse422 | DeleteUserGroupEndpointResponse424 | DeleteUserGroupEndpointResponse500 | DeleteUserGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteUserGroupEndpointResponse400
    | DeleteUserGroupEndpointResponse401
    | DeleteUserGroupEndpointResponse403
    | DeleteUserGroupEndpointResponse404
    | DeleteUserGroupEndpointResponse405
    | DeleteUserGroupEndpointResponse406
    | DeleteUserGroupEndpointResponse409
    | DeleteUserGroupEndpointResponse415
    | DeleteUserGroupEndpointResponse422
    | DeleteUserGroupEndpointResponse424
    | DeleteUserGroupEndpointResponse500
    | DeleteUserGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserGroupEndpointResponse400 | DeleteUserGroupEndpointResponse401 | DeleteUserGroupEndpointResponse403 | DeleteUserGroupEndpointResponse404 | DeleteUserGroupEndpointResponse405 | DeleteUserGroupEndpointResponse406 | DeleteUserGroupEndpointResponse409 | DeleteUserGroupEndpointResponse415 | DeleteUserGroupEndpointResponse422 | DeleteUserGroupEndpointResponse424 | DeleteUserGroupEndpointResponse500 | DeleteUserGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
