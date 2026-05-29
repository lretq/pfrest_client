from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_query import GetServicesHAProxyFrontendACLsEndpointQuery
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_400 import (
    GetServicesHAProxyFrontendACLsEndpointResponse400,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_401 import (
    GetServicesHAProxyFrontendACLsEndpointResponse401,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_403 import (
    GetServicesHAProxyFrontendACLsEndpointResponse403,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_404 import (
    GetServicesHAProxyFrontendACLsEndpointResponse404,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_405 import (
    GetServicesHAProxyFrontendACLsEndpointResponse405,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_406 import (
    GetServicesHAProxyFrontendACLsEndpointResponse406,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_409 import (
    GetServicesHAProxyFrontendACLsEndpointResponse409,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_415 import (
    GetServicesHAProxyFrontendACLsEndpointResponse415,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_422 import (
    GetServicesHAProxyFrontendACLsEndpointResponse422,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_424 import (
    GetServicesHAProxyFrontendACLsEndpointResponse424,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_500 import (
    GetServicesHAProxyFrontendACLsEndpointResponse500,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_response_503 import (
    GetServicesHAProxyFrontendACLsEndpointResponse503,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_sort_flags import (
    GetServicesHAProxyFrontendACLsEndpointSortFlags,
)
from ...models.get_services_ha_proxy_frontend_ac_ls_endpoint_sort_order import (
    GetServicesHAProxyFrontendACLsEndpointSortOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset = UNSET,
    query: GetServicesHAProxyFrontendACLsEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/services/haproxy/frontend/acls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesHAProxyFrontendACLsEndpointResponse400
    | GetServicesHAProxyFrontendACLsEndpointResponse401
    | GetServicesHAProxyFrontendACLsEndpointResponse403
    | GetServicesHAProxyFrontendACLsEndpointResponse404
    | GetServicesHAProxyFrontendACLsEndpointResponse405
    | GetServicesHAProxyFrontendACLsEndpointResponse406
    | GetServicesHAProxyFrontendACLsEndpointResponse409
    | GetServicesHAProxyFrontendACLsEndpointResponse415
    | GetServicesHAProxyFrontendACLsEndpointResponse422
    | GetServicesHAProxyFrontendACLsEndpointResponse424
    | GetServicesHAProxyFrontendACLsEndpointResponse500
    | GetServicesHAProxyFrontendACLsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesHAProxyFrontendACLsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesHAProxyFrontendACLsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesHAProxyFrontendACLsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesHAProxyFrontendACLsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesHAProxyFrontendACLsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesHAProxyFrontendACLsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesHAProxyFrontendACLsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesHAProxyFrontendACLsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesHAProxyFrontendACLsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesHAProxyFrontendACLsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesHAProxyFrontendACLsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesHAProxyFrontendACLsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesHAProxyFrontendACLsEndpointResponse400
    | GetServicesHAProxyFrontendACLsEndpointResponse401
    | GetServicesHAProxyFrontendACLsEndpointResponse403
    | GetServicesHAProxyFrontendACLsEndpointResponse404
    | GetServicesHAProxyFrontendACLsEndpointResponse405
    | GetServicesHAProxyFrontendACLsEndpointResponse406
    | GetServicesHAProxyFrontendACLsEndpointResponse409
    | GetServicesHAProxyFrontendACLsEndpointResponse415
    | GetServicesHAProxyFrontendACLsEndpointResponse422
    | GetServicesHAProxyFrontendACLsEndpointResponse424
    | GetServicesHAProxyFrontendACLsEndpointResponse500
    | GetServicesHAProxyFrontendACLsEndpointResponse503
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
    sort_order: GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset = UNSET,
    query: GetServicesHAProxyFrontendACLsEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesHAProxyFrontendACLsEndpointResponse400
    | GetServicesHAProxyFrontendACLsEndpointResponse401
    | GetServicesHAProxyFrontendACLsEndpointResponse403
    | GetServicesHAProxyFrontendACLsEndpointResponse404
    | GetServicesHAProxyFrontendACLsEndpointResponse405
    | GetServicesHAProxyFrontendACLsEndpointResponse406
    | GetServicesHAProxyFrontendACLsEndpointResponse409
    | GetServicesHAProxyFrontendACLsEndpointResponse415
    | GetServicesHAProxyFrontendACLsEndpointResponse422
    | GetServicesHAProxyFrontendACLsEndpointResponse424
    | GetServicesHAProxyFrontendACLsEndpointResponse500
    | GetServicesHAProxyFrontendACLsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing HAProxy Frontend Access Control
    Lists.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acls-get ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset):
        sort_flags (GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset):
        query (GetServicesHAProxyFrontendACLsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyFrontendACLsEndpointResponse400 | GetServicesHAProxyFrontendACLsEndpointResponse401 | GetServicesHAProxyFrontendACLsEndpointResponse403 | GetServicesHAProxyFrontendACLsEndpointResponse404 | GetServicesHAProxyFrontendACLsEndpointResponse405 | GetServicesHAProxyFrontendACLsEndpointResponse406 | GetServicesHAProxyFrontendACLsEndpointResponse409 | GetServicesHAProxyFrontendACLsEndpointResponse415 | GetServicesHAProxyFrontendACLsEndpointResponse422 | GetServicesHAProxyFrontendACLsEndpointResponse424 | GetServicesHAProxyFrontendACLsEndpointResponse500 | GetServicesHAProxyFrontendACLsEndpointResponse503]
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
    sort_order: GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset = UNSET,
    query: GetServicesHAProxyFrontendACLsEndpointQuery | Unset = UNSET,
) -> (
    GetServicesHAProxyFrontendACLsEndpointResponse400
    | GetServicesHAProxyFrontendACLsEndpointResponse401
    | GetServicesHAProxyFrontendACLsEndpointResponse403
    | GetServicesHAProxyFrontendACLsEndpointResponse404
    | GetServicesHAProxyFrontendACLsEndpointResponse405
    | GetServicesHAProxyFrontendACLsEndpointResponse406
    | GetServicesHAProxyFrontendACLsEndpointResponse409
    | GetServicesHAProxyFrontendACLsEndpointResponse415
    | GetServicesHAProxyFrontendACLsEndpointResponse422
    | GetServicesHAProxyFrontendACLsEndpointResponse424
    | GetServicesHAProxyFrontendACLsEndpointResponse500
    | GetServicesHAProxyFrontendACLsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing HAProxy Frontend Access Control
    Lists.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acls-get ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset):
        sort_flags (GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset):
        query (GetServicesHAProxyFrontendACLsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyFrontendACLsEndpointResponse400 | GetServicesHAProxyFrontendACLsEndpointResponse401 | GetServicesHAProxyFrontendACLsEndpointResponse403 | GetServicesHAProxyFrontendACLsEndpointResponse404 | GetServicesHAProxyFrontendACLsEndpointResponse405 | GetServicesHAProxyFrontendACLsEndpointResponse406 | GetServicesHAProxyFrontendACLsEndpointResponse409 | GetServicesHAProxyFrontendACLsEndpointResponse415 | GetServicesHAProxyFrontendACLsEndpointResponse422 | GetServicesHAProxyFrontendACLsEndpointResponse424 | GetServicesHAProxyFrontendACLsEndpointResponse500 | GetServicesHAProxyFrontendACLsEndpointResponse503
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
    sort_order: GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset = UNSET,
    query: GetServicesHAProxyFrontendACLsEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesHAProxyFrontendACLsEndpointResponse400
    | GetServicesHAProxyFrontendACLsEndpointResponse401
    | GetServicesHAProxyFrontendACLsEndpointResponse403
    | GetServicesHAProxyFrontendACLsEndpointResponse404
    | GetServicesHAProxyFrontendACLsEndpointResponse405
    | GetServicesHAProxyFrontendACLsEndpointResponse406
    | GetServicesHAProxyFrontendACLsEndpointResponse409
    | GetServicesHAProxyFrontendACLsEndpointResponse415
    | GetServicesHAProxyFrontendACLsEndpointResponse422
    | GetServicesHAProxyFrontendACLsEndpointResponse424
    | GetServicesHAProxyFrontendACLsEndpointResponse500
    | GetServicesHAProxyFrontendACLsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing HAProxy Frontend Access Control
    Lists.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acls-get ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset):
        sort_flags (GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset):
        query (GetServicesHAProxyFrontendACLsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyFrontendACLsEndpointResponse400 | GetServicesHAProxyFrontendACLsEndpointResponse401 | GetServicesHAProxyFrontendACLsEndpointResponse403 | GetServicesHAProxyFrontendACLsEndpointResponse404 | GetServicesHAProxyFrontendACLsEndpointResponse405 | GetServicesHAProxyFrontendACLsEndpointResponse406 | GetServicesHAProxyFrontendACLsEndpointResponse409 | GetServicesHAProxyFrontendACLsEndpointResponse415 | GetServicesHAProxyFrontendACLsEndpointResponse422 | GetServicesHAProxyFrontendACLsEndpointResponse424 | GetServicesHAProxyFrontendACLsEndpointResponse500 | GetServicesHAProxyFrontendACLsEndpointResponse503]
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
    sort_order: GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset = UNSET,
    query: GetServicesHAProxyFrontendACLsEndpointQuery | Unset = UNSET,
) -> (
    GetServicesHAProxyFrontendACLsEndpointResponse400
    | GetServicesHAProxyFrontendACLsEndpointResponse401
    | GetServicesHAProxyFrontendACLsEndpointResponse403
    | GetServicesHAProxyFrontendACLsEndpointResponse404
    | GetServicesHAProxyFrontendACLsEndpointResponse405
    | GetServicesHAProxyFrontendACLsEndpointResponse406
    | GetServicesHAProxyFrontendACLsEndpointResponse409
    | GetServicesHAProxyFrontendACLsEndpointResponse415
    | GetServicesHAProxyFrontendACLsEndpointResponse422
    | GetServicesHAProxyFrontendACLsEndpointResponse424
    | GetServicesHAProxyFrontendACLsEndpointResponse500
    | GetServicesHAProxyFrontendACLsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing HAProxy Frontend Access Control
    Lists.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acls-get ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesHAProxyFrontendACLsEndpointSortOrder | Unset):
        sort_flags (GetServicesHAProxyFrontendACLsEndpointSortFlags | Unset):
        query (GetServicesHAProxyFrontendACLsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyFrontendACLsEndpointResponse400 | GetServicesHAProxyFrontendACLsEndpointResponse401 | GetServicesHAProxyFrontendACLsEndpointResponse403 | GetServicesHAProxyFrontendACLsEndpointResponse404 | GetServicesHAProxyFrontendACLsEndpointResponse405 | GetServicesHAProxyFrontendACLsEndpointResponse406 | GetServicesHAProxyFrontendACLsEndpointResponse409 | GetServicesHAProxyFrontendACLsEndpointResponse415 | GetServicesHAProxyFrontendACLsEndpointResponse422 | GetServicesHAProxyFrontendACLsEndpointResponse424 | GetServicesHAProxyFrontendACLsEndpointResponse500 | GetServicesHAProxyFrontendACLsEndpointResponse503
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
