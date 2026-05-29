from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_group_endpoint_response_400 import GetUserGroupEndpointResponse400
from ...models.get_user_group_endpoint_response_401 import GetUserGroupEndpointResponse401
from ...models.get_user_group_endpoint_response_403 import GetUserGroupEndpointResponse403
from ...models.get_user_group_endpoint_response_404 import GetUserGroupEndpointResponse404
from ...models.get_user_group_endpoint_response_405 import GetUserGroupEndpointResponse405
from ...models.get_user_group_endpoint_response_406 import GetUserGroupEndpointResponse406
from ...models.get_user_group_endpoint_response_409 import GetUserGroupEndpointResponse409
from ...models.get_user_group_endpoint_response_415 import GetUserGroupEndpointResponse415
from ...models.get_user_group_endpoint_response_422 import GetUserGroupEndpointResponse422
from ...models.get_user_group_endpoint_response_424 import GetUserGroupEndpointResponse424
from ...models.get_user_group_endpoint_response_500 import GetUserGroupEndpointResponse500
from ...models.get_user_group_endpoint_response_503 import GetUserGroupEndpointResponse503
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
        "method": "get",
        "url": "/api/v2/user/group",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUserGroupEndpointResponse400
    | GetUserGroupEndpointResponse401
    | GetUserGroupEndpointResponse403
    | GetUserGroupEndpointResponse404
    | GetUserGroupEndpointResponse405
    | GetUserGroupEndpointResponse406
    | GetUserGroupEndpointResponse409
    | GetUserGroupEndpointResponse415
    | GetUserGroupEndpointResponse422
    | GetUserGroupEndpointResponse424
    | GetUserGroupEndpointResponse500
    | GetUserGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetUserGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetUserGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUserGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUserGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetUserGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetUserGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetUserGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetUserGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetUserGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetUserGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetUserGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetUserGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUserGroupEndpointResponse400
    | GetUserGroupEndpointResponse401
    | GetUserGroupEndpointResponse403
    | GetUserGroupEndpointResponse404
    | GetUserGroupEndpointResponse405
    | GetUserGroupEndpointResponse406
    | GetUserGroupEndpointResponse409
    | GetUserGroupEndpointResponse415
    | GetUserGroupEndpointResponse422
    | GetUserGroupEndpointResponse424
    | GetUserGroupEndpointResponse500
    | GetUserGroupEndpointResponse503
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
    GetUserGroupEndpointResponse400
    | GetUserGroupEndpointResponse401
    | GetUserGroupEndpointResponse403
    | GetUserGroupEndpointResponse404
    | GetUserGroupEndpointResponse405
    | GetUserGroupEndpointResponse406
    | GetUserGroupEndpointResponse409
    | GetUserGroupEndpointResponse415
    | GetUserGroupEndpointResponse422
    | GetUserGroupEndpointResponse424
    | GetUserGroupEndpointResponse500
    | GetUserGroupEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserGroupEndpointResponse400 | GetUserGroupEndpointResponse401 | GetUserGroupEndpointResponse403 | GetUserGroupEndpointResponse404 | GetUserGroupEndpointResponse405 | GetUserGroupEndpointResponse406 | GetUserGroupEndpointResponse409 | GetUserGroupEndpointResponse415 | GetUserGroupEndpointResponse422 | GetUserGroupEndpointResponse424 | GetUserGroupEndpointResponse500 | GetUserGroupEndpointResponse503]
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
    GetUserGroupEndpointResponse400
    | GetUserGroupEndpointResponse401
    | GetUserGroupEndpointResponse403
    | GetUserGroupEndpointResponse404
    | GetUserGroupEndpointResponse405
    | GetUserGroupEndpointResponse406
    | GetUserGroupEndpointResponse409
    | GetUserGroupEndpointResponse415
    | GetUserGroupEndpointResponse422
    | GetUserGroupEndpointResponse424
    | GetUserGroupEndpointResponse500
    | GetUserGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserGroupEndpointResponse400 | GetUserGroupEndpointResponse401 | GetUserGroupEndpointResponse403 | GetUserGroupEndpointResponse404 | GetUserGroupEndpointResponse405 | GetUserGroupEndpointResponse406 | GetUserGroupEndpointResponse409 | GetUserGroupEndpointResponse415 | GetUserGroupEndpointResponse422 | GetUserGroupEndpointResponse424 | GetUserGroupEndpointResponse500 | GetUserGroupEndpointResponse503
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
    GetUserGroupEndpointResponse400
    | GetUserGroupEndpointResponse401
    | GetUserGroupEndpointResponse403
    | GetUserGroupEndpointResponse404
    | GetUserGroupEndpointResponse405
    | GetUserGroupEndpointResponse406
    | GetUserGroupEndpointResponse409
    | GetUserGroupEndpointResponse415
    | GetUserGroupEndpointResponse422
    | GetUserGroupEndpointResponse424
    | GetUserGroupEndpointResponse500
    | GetUserGroupEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserGroupEndpointResponse400 | GetUserGroupEndpointResponse401 | GetUserGroupEndpointResponse403 | GetUserGroupEndpointResponse404 | GetUserGroupEndpointResponse405 | GetUserGroupEndpointResponse406 | GetUserGroupEndpointResponse409 | GetUserGroupEndpointResponse415 | GetUserGroupEndpointResponse422 | GetUserGroupEndpointResponse424 | GetUserGroupEndpointResponse500 | GetUserGroupEndpointResponse503]
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
    GetUserGroupEndpointResponse400
    | GetUserGroupEndpointResponse401
    | GetUserGroupEndpointResponse403
    | GetUserGroupEndpointResponse404
    | GetUserGroupEndpointResponse405
    | GetUserGroupEndpointResponse406
    | GetUserGroupEndpointResponse409
    | GetUserGroupEndpointResponse415
    | GetUserGroupEndpointResponse422
    | GetUserGroupEndpointResponse424
    | GetUserGroupEndpointResponse500
    | GetUserGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing User Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserGroupEndpointResponse400 | GetUserGroupEndpointResponse401 | GetUserGroupEndpointResponse403 | GetUserGroupEndpointResponse404 | GetUserGroupEndpointResponse405 | GetUserGroupEndpointResponse406 | GetUserGroupEndpointResponse409 | GetUserGroupEndpointResponse415 | GetUserGroupEndpointResponse422 | GetUserGroupEndpointResponse424 | GetUserGroupEndpointResponse500 | GetUserGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
