from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_free_radius_users_endpoint_query import GetServicesFreeRADIUSUsersEndpointQuery
from ...models.get_services_free_radius_users_endpoint_response_400 import GetServicesFreeRADIUSUsersEndpointResponse400
from ...models.get_services_free_radius_users_endpoint_response_401 import GetServicesFreeRADIUSUsersEndpointResponse401
from ...models.get_services_free_radius_users_endpoint_response_403 import GetServicesFreeRADIUSUsersEndpointResponse403
from ...models.get_services_free_radius_users_endpoint_response_404 import GetServicesFreeRADIUSUsersEndpointResponse404
from ...models.get_services_free_radius_users_endpoint_response_405 import GetServicesFreeRADIUSUsersEndpointResponse405
from ...models.get_services_free_radius_users_endpoint_response_406 import GetServicesFreeRADIUSUsersEndpointResponse406
from ...models.get_services_free_radius_users_endpoint_response_409 import GetServicesFreeRADIUSUsersEndpointResponse409
from ...models.get_services_free_radius_users_endpoint_response_415 import GetServicesFreeRADIUSUsersEndpointResponse415
from ...models.get_services_free_radius_users_endpoint_response_422 import GetServicesFreeRADIUSUsersEndpointResponse422
from ...models.get_services_free_radius_users_endpoint_response_424 import GetServicesFreeRADIUSUsersEndpointResponse424
from ...models.get_services_free_radius_users_endpoint_response_500 import GetServicesFreeRADIUSUsersEndpointResponse500
from ...models.get_services_free_radius_users_endpoint_response_503 import GetServicesFreeRADIUSUsersEndpointResponse503
from ...models.get_services_free_radius_users_endpoint_sort_flags import GetServicesFreeRADIUSUsersEndpointSortFlags
from ...models.get_services_free_radius_users_endpoint_sort_order import GetServicesFreeRADIUSUsersEndpointSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesFreeRADIUSUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesFreeRADIUSUsersEndpointSortFlags | Unset = UNSET,
    query: GetServicesFreeRADIUSUsersEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/services/freeradius/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesFreeRADIUSUsersEndpointResponse400
    | GetServicesFreeRADIUSUsersEndpointResponse401
    | GetServicesFreeRADIUSUsersEndpointResponse403
    | GetServicesFreeRADIUSUsersEndpointResponse404
    | GetServicesFreeRADIUSUsersEndpointResponse405
    | GetServicesFreeRADIUSUsersEndpointResponse406
    | GetServicesFreeRADIUSUsersEndpointResponse409
    | GetServicesFreeRADIUSUsersEndpointResponse415
    | GetServicesFreeRADIUSUsersEndpointResponse422
    | GetServicesFreeRADIUSUsersEndpointResponse424
    | GetServicesFreeRADIUSUsersEndpointResponse500
    | GetServicesFreeRADIUSUsersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesFreeRADIUSUsersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesFreeRADIUSUsersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesFreeRADIUSUsersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesFreeRADIUSUsersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesFreeRADIUSUsersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesFreeRADIUSUsersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesFreeRADIUSUsersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesFreeRADIUSUsersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesFreeRADIUSUsersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesFreeRADIUSUsersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesFreeRADIUSUsersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesFreeRADIUSUsersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesFreeRADIUSUsersEndpointResponse400
    | GetServicesFreeRADIUSUsersEndpointResponse401
    | GetServicesFreeRADIUSUsersEndpointResponse403
    | GetServicesFreeRADIUSUsersEndpointResponse404
    | GetServicesFreeRADIUSUsersEndpointResponse405
    | GetServicesFreeRADIUSUsersEndpointResponse406
    | GetServicesFreeRADIUSUsersEndpointResponse409
    | GetServicesFreeRADIUSUsersEndpointResponse415
    | GetServicesFreeRADIUSUsersEndpointResponse422
    | GetServicesFreeRADIUSUsersEndpointResponse424
    | GetServicesFreeRADIUSUsersEndpointResponse500
    | GetServicesFreeRADIUSUsersEndpointResponse503
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
    sort_order: GetServicesFreeRADIUSUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesFreeRADIUSUsersEndpointSortFlags | Unset = UNSET,
    query: GetServicesFreeRADIUSUsersEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesFreeRADIUSUsersEndpointResponse400
    | GetServicesFreeRADIUSUsersEndpointResponse401
    | GetServicesFreeRADIUSUsersEndpointResponse403
    | GetServicesFreeRADIUSUsersEndpointResponse404
    | GetServicesFreeRADIUSUsersEndpointResponse405
    | GetServicesFreeRADIUSUsersEndpointResponse406
    | GetServicesFreeRADIUSUsersEndpointResponse409
    | GetServicesFreeRADIUSUsersEndpointResponse415
    | GetServicesFreeRADIUSUsersEndpointResponse422
    | GetServicesFreeRADIUSUsersEndpointResponse424
    | GetServicesFreeRADIUSUsersEndpointResponse500
    | GetServicesFreeRADIUSUsersEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesFreeRADIUSUsersEndpointSortOrder | Unset):
        sort_flags (GetServicesFreeRADIUSUsersEndpointSortFlags | Unset):
        query (GetServicesFreeRADIUSUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesFreeRADIUSUsersEndpointResponse400 | GetServicesFreeRADIUSUsersEndpointResponse401 | GetServicesFreeRADIUSUsersEndpointResponse403 | GetServicesFreeRADIUSUsersEndpointResponse404 | GetServicesFreeRADIUSUsersEndpointResponse405 | GetServicesFreeRADIUSUsersEndpointResponse406 | GetServicesFreeRADIUSUsersEndpointResponse409 | GetServicesFreeRADIUSUsersEndpointResponse415 | GetServicesFreeRADIUSUsersEndpointResponse422 | GetServicesFreeRADIUSUsersEndpointResponse424 | GetServicesFreeRADIUSUsersEndpointResponse500 | GetServicesFreeRADIUSUsersEndpointResponse503]
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
    sort_order: GetServicesFreeRADIUSUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesFreeRADIUSUsersEndpointSortFlags | Unset = UNSET,
    query: GetServicesFreeRADIUSUsersEndpointQuery | Unset = UNSET,
) -> (
    GetServicesFreeRADIUSUsersEndpointResponse400
    | GetServicesFreeRADIUSUsersEndpointResponse401
    | GetServicesFreeRADIUSUsersEndpointResponse403
    | GetServicesFreeRADIUSUsersEndpointResponse404
    | GetServicesFreeRADIUSUsersEndpointResponse405
    | GetServicesFreeRADIUSUsersEndpointResponse406
    | GetServicesFreeRADIUSUsersEndpointResponse409
    | GetServicesFreeRADIUSUsersEndpointResponse415
    | GetServicesFreeRADIUSUsersEndpointResponse422
    | GetServicesFreeRADIUSUsersEndpointResponse424
    | GetServicesFreeRADIUSUsersEndpointResponse500
    | GetServicesFreeRADIUSUsersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesFreeRADIUSUsersEndpointSortOrder | Unset):
        sort_flags (GetServicesFreeRADIUSUsersEndpointSortFlags | Unset):
        query (GetServicesFreeRADIUSUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesFreeRADIUSUsersEndpointResponse400 | GetServicesFreeRADIUSUsersEndpointResponse401 | GetServicesFreeRADIUSUsersEndpointResponse403 | GetServicesFreeRADIUSUsersEndpointResponse404 | GetServicesFreeRADIUSUsersEndpointResponse405 | GetServicesFreeRADIUSUsersEndpointResponse406 | GetServicesFreeRADIUSUsersEndpointResponse409 | GetServicesFreeRADIUSUsersEndpointResponse415 | GetServicesFreeRADIUSUsersEndpointResponse422 | GetServicesFreeRADIUSUsersEndpointResponse424 | GetServicesFreeRADIUSUsersEndpointResponse500 | GetServicesFreeRADIUSUsersEndpointResponse503
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
    sort_order: GetServicesFreeRADIUSUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesFreeRADIUSUsersEndpointSortFlags | Unset = UNSET,
    query: GetServicesFreeRADIUSUsersEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesFreeRADIUSUsersEndpointResponse400
    | GetServicesFreeRADIUSUsersEndpointResponse401
    | GetServicesFreeRADIUSUsersEndpointResponse403
    | GetServicesFreeRADIUSUsersEndpointResponse404
    | GetServicesFreeRADIUSUsersEndpointResponse405
    | GetServicesFreeRADIUSUsersEndpointResponse406
    | GetServicesFreeRADIUSUsersEndpointResponse409
    | GetServicesFreeRADIUSUsersEndpointResponse415
    | GetServicesFreeRADIUSUsersEndpointResponse422
    | GetServicesFreeRADIUSUsersEndpointResponse424
    | GetServicesFreeRADIUSUsersEndpointResponse500
    | GetServicesFreeRADIUSUsersEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesFreeRADIUSUsersEndpointSortOrder | Unset):
        sort_flags (GetServicesFreeRADIUSUsersEndpointSortFlags | Unset):
        query (GetServicesFreeRADIUSUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesFreeRADIUSUsersEndpointResponse400 | GetServicesFreeRADIUSUsersEndpointResponse401 | GetServicesFreeRADIUSUsersEndpointResponse403 | GetServicesFreeRADIUSUsersEndpointResponse404 | GetServicesFreeRADIUSUsersEndpointResponse405 | GetServicesFreeRADIUSUsersEndpointResponse406 | GetServicesFreeRADIUSUsersEndpointResponse409 | GetServicesFreeRADIUSUsersEndpointResponse415 | GetServicesFreeRADIUSUsersEndpointResponse422 | GetServicesFreeRADIUSUsersEndpointResponse424 | GetServicesFreeRADIUSUsersEndpointResponse500 | GetServicesFreeRADIUSUsersEndpointResponse503]
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
    sort_order: GetServicesFreeRADIUSUsersEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesFreeRADIUSUsersEndpointSortFlags | Unset = UNSET,
    query: GetServicesFreeRADIUSUsersEndpointQuery | Unset = UNSET,
) -> (
    GetServicesFreeRADIUSUsersEndpointResponse400
    | GetServicesFreeRADIUSUsersEndpointResponse401
    | GetServicesFreeRADIUSUsersEndpointResponse403
    | GetServicesFreeRADIUSUsersEndpointResponse404
    | GetServicesFreeRADIUSUsersEndpointResponse405
    | GetServicesFreeRADIUSUsersEndpointResponse406
    | GetServicesFreeRADIUSUsersEndpointResponse409
    | GetServicesFreeRADIUSUsersEndpointResponse415
    | GetServicesFreeRADIUSUsersEndpointResponse422
    | GetServicesFreeRADIUSUsersEndpointResponse424
    | GetServicesFreeRADIUSUsersEndpointResponse500
    | GetServicesFreeRADIUSUsersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesFreeRADIUSUsersEndpointSortOrder | Unset):
        sort_flags (GetServicesFreeRADIUSUsersEndpointSortFlags | Unset):
        query (GetServicesFreeRADIUSUsersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesFreeRADIUSUsersEndpointResponse400 | GetServicesFreeRADIUSUsersEndpointResponse401 | GetServicesFreeRADIUSUsersEndpointResponse403 | GetServicesFreeRADIUSUsersEndpointResponse404 | GetServicesFreeRADIUSUsersEndpointResponse405 | GetServicesFreeRADIUSUsersEndpointResponse406 | GetServicesFreeRADIUSUsersEndpointResponse409 | GetServicesFreeRADIUSUsersEndpointResponse415 | GetServicesFreeRADIUSUsersEndpointResponse422 | GetServicesFreeRADIUSUsersEndpointResponse424 | GetServicesFreeRADIUSUsersEndpointResponse500 | GetServicesFreeRADIUSUsersEndpointResponse503
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
