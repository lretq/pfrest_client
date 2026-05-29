from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_endpoint_query import GetUsersEndpointQuery
from ...models.get_users_endpoint_response_400 import GetUsersEndpointResponse400
from ...models.get_users_endpoint_response_401 import GetUsersEndpointResponse401
from ...models.get_users_endpoint_response_403 import GetUsersEndpointResponse403
from ...models.get_users_endpoint_response_404 import GetUsersEndpointResponse404
from ...models.get_users_endpoint_response_405 import GetUsersEndpointResponse405
from ...models.get_users_endpoint_response_406 import GetUsersEndpointResponse406
from ...models.get_users_endpoint_response_409 import GetUsersEndpointResponse409
from ...models.get_users_endpoint_response_415 import GetUsersEndpointResponse415
from ...models.get_users_endpoint_response_422 import GetUsersEndpointResponse422
from ...models.get_users_endpoint_response_424 import GetUsersEndpointResponse424
from ...models.get_users_endpoint_response_500 import GetUsersEndpointResponse500
from ...models.get_users_endpoint_response_503 import GetUsersEndpointResponse503
from ...models.get_users_endpoint_sort_flags import GetUsersEndpointSortFlags
from ...models.get_users_endpoint_sort_order import GetUsersEndpointSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetUsersEndpointSortFlags | Unset = UNSET,
    query: GetUsersEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort_by: list[str] | None | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, list):
        json_sort_by = sort_by

    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    json_sort_flags: str | Unset = UNSET
    if not isinstance(sort_flags, Unset):
        json_sort_flags = sort_flags.value

    params["sort_flags"] = json_sort_flags

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsersEndpointResponse400
    | GetUsersEndpointResponse401
    | GetUsersEndpointResponse403
    | GetUsersEndpointResponse404
    | GetUsersEndpointResponse405
    | GetUsersEndpointResponse406
    | GetUsersEndpointResponse409
    | GetUsersEndpointResponse415
    | GetUsersEndpointResponse422
    | GetUsersEndpointResponse424
    | GetUsersEndpointResponse500
    | GetUsersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetUsersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetUsersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUsersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetUsersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetUsersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetUsersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetUsersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetUsersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetUsersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetUsersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetUsersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsersEndpointResponse400
    | GetUsersEndpointResponse401
    | GetUsersEndpointResponse403
    | GetUsersEndpointResponse404
    | GetUsersEndpointResponse405
    | GetUsersEndpointResponse406
    | GetUsersEndpointResponse409
    | GetUsersEndpointResponse415
    | GetUsersEndpointResponse422
    | GetUsersEndpointResponse424
    | GetUsersEndpointResponse500
    | GetUsersEndpointResponse503
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
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetUsersEndpointSortFlags | Unset = UNSET,
    query: GetUsersEndpointQuery | Unset = UNSET,
) -> Response[
    GetUsersEndpointResponse400
    | GetUsersEndpointResponse401
    | GetUsersEndpointResponse403
    | GetUsersEndpointResponse404
    | GetUsersEndpointResponse405
    | GetUsersEndpointResponse406
    | GetUsersEndpointResponse409
    | GetUsersEndpointResponse415
    | GetUsersEndpointResponse422
    | GetUsersEndpointResponse424
    | GetUsersEndpointResponse500
    | GetUsersEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-users-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetUsersEndpointSortOrder | Unset):
        sort_flags (GetUsersEndpointSortFlags | Unset):
        query (GetUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersEndpointResponse400 | GetUsersEndpointResponse401 | GetUsersEndpointResponse403 | GetUsersEndpointResponse404 | GetUsersEndpointResponse405 | GetUsersEndpointResponse406 | GetUsersEndpointResponse409 | GetUsersEndpointResponse415 | GetUsersEndpointResponse422 | GetUsersEndpointResponse424 | GetUsersEndpointResponse500 | GetUsersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetUsersEndpointSortFlags | Unset = UNSET,
    query: GetUsersEndpointQuery | Unset = UNSET,
) -> (
    GetUsersEndpointResponse400
    | GetUsersEndpointResponse401
    | GetUsersEndpointResponse403
    | GetUsersEndpointResponse404
    | GetUsersEndpointResponse405
    | GetUsersEndpointResponse406
    | GetUsersEndpointResponse409
    | GetUsersEndpointResponse415
    | GetUsersEndpointResponse422
    | GetUsersEndpointResponse424
    | GetUsersEndpointResponse500
    | GetUsersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-users-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetUsersEndpointSortOrder | Unset):
        sort_flags (GetUsersEndpointSortFlags | Unset):
        query (GetUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersEndpointResponse400 | GetUsersEndpointResponse401 | GetUsersEndpointResponse403 | GetUsersEndpointResponse404 | GetUsersEndpointResponse405 | GetUsersEndpointResponse406 | GetUsersEndpointResponse409 | GetUsersEndpointResponse415 | GetUsersEndpointResponse422 | GetUsersEndpointResponse424 | GetUsersEndpointResponse500 | GetUsersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetUsersEndpointSortFlags | Unset = UNSET,
    query: GetUsersEndpointQuery | Unset = UNSET,
) -> Response[
    GetUsersEndpointResponse400
    | GetUsersEndpointResponse401
    | GetUsersEndpointResponse403
    | GetUsersEndpointResponse404
    | GetUsersEndpointResponse405
    | GetUsersEndpointResponse406
    | GetUsersEndpointResponse409
    | GetUsersEndpointResponse415
    | GetUsersEndpointResponse422
    | GetUsersEndpointResponse424
    | GetUsersEndpointResponse500
    | GetUsersEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-users-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetUsersEndpointSortOrder | Unset):
        sort_flags (GetUsersEndpointSortFlags | Unset):
        query (GetUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersEndpointResponse400 | GetUsersEndpointResponse401 | GetUsersEndpointResponse403 | GetUsersEndpointResponse404 | GetUsersEndpointResponse405 | GetUsersEndpointResponse406 | GetUsersEndpointResponse409 | GetUsersEndpointResponse415 | GetUsersEndpointResponse422 | GetUsersEndpointResponse424 | GetUsersEndpointResponse500 | GetUsersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetUsersEndpointSortFlags | Unset = UNSET,
    query: GetUsersEndpointQuery | Unset = UNSET,
) -> (
    GetUsersEndpointResponse400
    | GetUsersEndpointResponse401
    | GetUsersEndpointResponse403
    | GetUsersEndpointResponse404
    | GetUsersEndpointResponse405
    | GetUsersEndpointResponse406
    | GetUsersEndpointResponse409
    | GetUsersEndpointResponse415
    | GetUsersEndpointResponse422
    | GetUsersEndpointResponse424
    | GetUsersEndpointResponse500
    | GetUsersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-users-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetUsersEndpointSortOrder | Unset):
        sort_flags (GetUsersEndpointSortFlags | Unset):
        query (GetUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersEndpointResponse400 | GetUsersEndpointResponse401 | GetUsersEndpointResponse403 | GetUsersEndpointResponse404 | GetUsersEndpointResponse405 | GetUsersEndpointResponse406 | GetUsersEndpointResponse409 | GetUsersEndpointResponse415 | GetUsersEndpointResponse422 | GetUsersEndpointResponse424 | GetUsersEndpointResponse500 | GetUsersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            sort_flags=sort_flags,
            query=query,
        )
    ).parsed
