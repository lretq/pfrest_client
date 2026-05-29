from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_diagnostics_tables_endpoint_query import GetDiagnosticsTablesEndpointQuery
from ...models.get_diagnostics_tables_endpoint_response_400 import GetDiagnosticsTablesEndpointResponse400
from ...models.get_diagnostics_tables_endpoint_response_401 import GetDiagnosticsTablesEndpointResponse401
from ...models.get_diagnostics_tables_endpoint_response_403 import GetDiagnosticsTablesEndpointResponse403
from ...models.get_diagnostics_tables_endpoint_response_404 import GetDiagnosticsTablesEndpointResponse404
from ...models.get_diagnostics_tables_endpoint_response_405 import GetDiagnosticsTablesEndpointResponse405
from ...models.get_diagnostics_tables_endpoint_response_406 import GetDiagnosticsTablesEndpointResponse406
from ...models.get_diagnostics_tables_endpoint_response_409 import GetDiagnosticsTablesEndpointResponse409
from ...models.get_diagnostics_tables_endpoint_response_415 import GetDiagnosticsTablesEndpointResponse415
from ...models.get_diagnostics_tables_endpoint_response_422 import GetDiagnosticsTablesEndpointResponse422
from ...models.get_diagnostics_tables_endpoint_response_424 import GetDiagnosticsTablesEndpointResponse424
from ...models.get_diagnostics_tables_endpoint_response_500 import GetDiagnosticsTablesEndpointResponse500
from ...models.get_diagnostics_tables_endpoint_response_503 import GetDiagnosticsTablesEndpointResponse503
from ...models.get_diagnostics_tables_endpoint_sort_flags import GetDiagnosticsTablesEndpointSortFlags
from ...models.get_diagnostics_tables_endpoint_sort_order import GetDiagnosticsTablesEndpointSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetDiagnosticsTablesEndpointSortOrder | Unset = UNSET,
    sort_flags: GetDiagnosticsTablesEndpointSortFlags | Unset = UNSET,
    query: GetDiagnosticsTablesEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/diagnostics/tables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetDiagnosticsTablesEndpointResponse400
    | GetDiagnosticsTablesEndpointResponse401
    | GetDiagnosticsTablesEndpointResponse403
    | GetDiagnosticsTablesEndpointResponse404
    | GetDiagnosticsTablesEndpointResponse405
    | GetDiagnosticsTablesEndpointResponse406
    | GetDiagnosticsTablesEndpointResponse409
    | GetDiagnosticsTablesEndpointResponse415
    | GetDiagnosticsTablesEndpointResponse422
    | GetDiagnosticsTablesEndpointResponse424
    | GetDiagnosticsTablesEndpointResponse500
    | GetDiagnosticsTablesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetDiagnosticsTablesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetDiagnosticsTablesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetDiagnosticsTablesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDiagnosticsTablesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetDiagnosticsTablesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetDiagnosticsTablesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetDiagnosticsTablesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetDiagnosticsTablesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetDiagnosticsTablesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetDiagnosticsTablesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetDiagnosticsTablesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetDiagnosticsTablesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetDiagnosticsTablesEndpointResponse400
    | GetDiagnosticsTablesEndpointResponse401
    | GetDiagnosticsTablesEndpointResponse403
    | GetDiagnosticsTablesEndpointResponse404
    | GetDiagnosticsTablesEndpointResponse405
    | GetDiagnosticsTablesEndpointResponse406
    | GetDiagnosticsTablesEndpointResponse409
    | GetDiagnosticsTablesEndpointResponse415
    | GetDiagnosticsTablesEndpointResponse422
    | GetDiagnosticsTablesEndpointResponse424
    | GetDiagnosticsTablesEndpointResponse500
    | GetDiagnosticsTablesEndpointResponse503
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
    sort_order: GetDiagnosticsTablesEndpointSortOrder | Unset = UNSET,
    sort_flags: GetDiagnosticsTablesEndpointSortFlags | Unset = UNSET,
    query: GetDiagnosticsTablesEndpointQuery | Unset = UNSET,
) -> Response[
    GetDiagnosticsTablesEndpointResponse400
    | GetDiagnosticsTablesEndpointResponse401
    | GetDiagnosticsTablesEndpointResponse403
    | GetDiagnosticsTablesEndpointResponse404
    | GetDiagnosticsTablesEndpointResponse405
    | GetDiagnosticsTablesEndpointResponse406
    | GetDiagnosticsTablesEndpointResponse409
    | GetDiagnosticsTablesEndpointResponse415
    | GetDiagnosticsTablesEndpointResponse422
    | GetDiagnosticsTablesEndpointResponse424
    | GetDiagnosticsTablesEndpointResponse500
    | GetDiagnosticsTablesEndpointResponse503
]:
    """<h3>Description:</h3>Retrieves the entries from all tables. For systems with a large number of
    tables or entries, it is recommended to use pagination and/or querying to limit the amount of data
    returned.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: Table<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-tables-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetDiagnosticsTablesEndpointSortOrder | Unset):
        sort_flags (GetDiagnosticsTablesEndpointSortFlags | Unset):
        query (GetDiagnosticsTablesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDiagnosticsTablesEndpointResponse400 | GetDiagnosticsTablesEndpointResponse401 | GetDiagnosticsTablesEndpointResponse403 | GetDiagnosticsTablesEndpointResponse404 | GetDiagnosticsTablesEndpointResponse405 | GetDiagnosticsTablesEndpointResponse406 | GetDiagnosticsTablesEndpointResponse409 | GetDiagnosticsTablesEndpointResponse415 | GetDiagnosticsTablesEndpointResponse422 | GetDiagnosticsTablesEndpointResponse424 | GetDiagnosticsTablesEndpointResponse500 | GetDiagnosticsTablesEndpointResponse503]
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
    sort_order: GetDiagnosticsTablesEndpointSortOrder | Unset = UNSET,
    sort_flags: GetDiagnosticsTablesEndpointSortFlags | Unset = UNSET,
    query: GetDiagnosticsTablesEndpointQuery | Unset = UNSET,
) -> (
    GetDiagnosticsTablesEndpointResponse400
    | GetDiagnosticsTablesEndpointResponse401
    | GetDiagnosticsTablesEndpointResponse403
    | GetDiagnosticsTablesEndpointResponse404
    | GetDiagnosticsTablesEndpointResponse405
    | GetDiagnosticsTablesEndpointResponse406
    | GetDiagnosticsTablesEndpointResponse409
    | GetDiagnosticsTablesEndpointResponse415
    | GetDiagnosticsTablesEndpointResponse422
    | GetDiagnosticsTablesEndpointResponse424
    | GetDiagnosticsTablesEndpointResponse500
    | GetDiagnosticsTablesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Retrieves the entries from all tables. For systems with a large number of
    tables or entries, it is recommended to use pagination and/or querying to limit the amount of data
    returned.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: Table<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-tables-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetDiagnosticsTablesEndpointSortOrder | Unset):
        sort_flags (GetDiagnosticsTablesEndpointSortFlags | Unset):
        query (GetDiagnosticsTablesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDiagnosticsTablesEndpointResponse400 | GetDiagnosticsTablesEndpointResponse401 | GetDiagnosticsTablesEndpointResponse403 | GetDiagnosticsTablesEndpointResponse404 | GetDiagnosticsTablesEndpointResponse405 | GetDiagnosticsTablesEndpointResponse406 | GetDiagnosticsTablesEndpointResponse409 | GetDiagnosticsTablesEndpointResponse415 | GetDiagnosticsTablesEndpointResponse422 | GetDiagnosticsTablesEndpointResponse424 | GetDiagnosticsTablesEndpointResponse500 | GetDiagnosticsTablesEndpointResponse503
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
    sort_order: GetDiagnosticsTablesEndpointSortOrder | Unset = UNSET,
    sort_flags: GetDiagnosticsTablesEndpointSortFlags | Unset = UNSET,
    query: GetDiagnosticsTablesEndpointQuery | Unset = UNSET,
) -> Response[
    GetDiagnosticsTablesEndpointResponse400
    | GetDiagnosticsTablesEndpointResponse401
    | GetDiagnosticsTablesEndpointResponse403
    | GetDiagnosticsTablesEndpointResponse404
    | GetDiagnosticsTablesEndpointResponse405
    | GetDiagnosticsTablesEndpointResponse406
    | GetDiagnosticsTablesEndpointResponse409
    | GetDiagnosticsTablesEndpointResponse415
    | GetDiagnosticsTablesEndpointResponse422
    | GetDiagnosticsTablesEndpointResponse424
    | GetDiagnosticsTablesEndpointResponse500
    | GetDiagnosticsTablesEndpointResponse503
]:
    """<h3>Description:</h3>Retrieves the entries from all tables. For systems with a large number of
    tables or entries, it is recommended to use pagination and/or querying to limit the amount of data
    returned.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: Table<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-tables-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetDiagnosticsTablesEndpointSortOrder | Unset):
        sort_flags (GetDiagnosticsTablesEndpointSortFlags | Unset):
        query (GetDiagnosticsTablesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDiagnosticsTablesEndpointResponse400 | GetDiagnosticsTablesEndpointResponse401 | GetDiagnosticsTablesEndpointResponse403 | GetDiagnosticsTablesEndpointResponse404 | GetDiagnosticsTablesEndpointResponse405 | GetDiagnosticsTablesEndpointResponse406 | GetDiagnosticsTablesEndpointResponse409 | GetDiagnosticsTablesEndpointResponse415 | GetDiagnosticsTablesEndpointResponse422 | GetDiagnosticsTablesEndpointResponse424 | GetDiagnosticsTablesEndpointResponse500 | GetDiagnosticsTablesEndpointResponse503]
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
    sort_order: GetDiagnosticsTablesEndpointSortOrder | Unset = UNSET,
    sort_flags: GetDiagnosticsTablesEndpointSortFlags | Unset = UNSET,
    query: GetDiagnosticsTablesEndpointQuery | Unset = UNSET,
) -> (
    GetDiagnosticsTablesEndpointResponse400
    | GetDiagnosticsTablesEndpointResponse401
    | GetDiagnosticsTablesEndpointResponse403
    | GetDiagnosticsTablesEndpointResponse404
    | GetDiagnosticsTablesEndpointResponse405
    | GetDiagnosticsTablesEndpointResponse406
    | GetDiagnosticsTablesEndpointResponse409
    | GetDiagnosticsTablesEndpointResponse415
    | GetDiagnosticsTablesEndpointResponse422
    | GetDiagnosticsTablesEndpointResponse424
    | GetDiagnosticsTablesEndpointResponse500
    | GetDiagnosticsTablesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Retrieves the entries from all tables. For systems with a large number of
    tables or entries, it is recommended to use pagination and/or querying to limit the amount of data
    returned.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: Table<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-tables-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetDiagnosticsTablesEndpointSortOrder | Unset):
        sort_flags (GetDiagnosticsTablesEndpointSortFlags | Unset):
        query (GetDiagnosticsTablesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDiagnosticsTablesEndpointResponse400 | GetDiagnosticsTablesEndpointResponse401 | GetDiagnosticsTablesEndpointResponse403 | GetDiagnosticsTablesEndpointResponse404 | GetDiagnosticsTablesEndpointResponse405 | GetDiagnosticsTablesEndpointResponse406 | GetDiagnosticsTablesEndpointResponse409 | GetDiagnosticsTablesEndpointResponse415 | GetDiagnosticsTablesEndpointResponse422 | GetDiagnosticsTablesEndpointResponse424 | GetDiagnosticsTablesEndpointResponse500 | GetDiagnosticsTablesEndpointResponse503
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
