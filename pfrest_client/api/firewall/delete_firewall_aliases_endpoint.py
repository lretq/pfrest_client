from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_aliases_endpoint_query import DeleteFirewallAliasesEndpointQuery
from ...models.delete_firewall_aliases_endpoint_response_400 import DeleteFirewallAliasesEndpointResponse400
from ...models.delete_firewall_aliases_endpoint_response_401 import DeleteFirewallAliasesEndpointResponse401
from ...models.delete_firewall_aliases_endpoint_response_403 import DeleteFirewallAliasesEndpointResponse403
from ...models.delete_firewall_aliases_endpoint_response_404 import DeleteFirewallAliasesEndpointResponse404
from ...models.delete_firewall_aliases_endpoint_response_405 import DeleteFirewallAliasesEndpointResponse405
from ...models.delete_firewall_aliases_endpoint_response_406 import DeleteFirewallAliasesEndpointResponse406
from ...models.delete_firewall_aliases_endpoint_response_409 import DeleteFirewallAliasesEndpointResponse409
from ...models.delete_firewall_aliases_endpoint_response_415 import DeleteFirewallAliasesEndpointResponse415
from ...models.delete_firewall_aliases_endpoint_response_422 import DeleteFirewallAliasesEndpointResponse422
from ...models.delete_firewall_aliases_endpoint_response_424 import DeleteFirewallAliasesEndpointResponse424
from ...models.delete_firewall_aliases_endpoint_response_500 import DeleteFirewallAliasesEndpointResponse500
from ...models.delete_firewall_aliases_endpoint_response_503 import DeleteFirewallAliasesEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteFirewallAliasesEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/firewall/aliases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallAliasesEndpointResponse400
    | DeleteFirewallAliasesEndpointResponse401
    | DeleteFirewallAliasesEndpointResponse403
    | DeleteFirewallAliasesEndpointResponse404
    | DeleteFirewallAliasesEndpointResponse405
    | DeleteFirewallAliasesEndpointResponse406
    | DeleteFirewallAliasesEndpointResponse409
    | DeleteFirewallAliasesEndpointResponse415
    | DeleteFirewallAliasesEndpointResponse422
    | DeleteFirewallAliasesEndpointResponse424
    | DeleteFirewallAliasesEndpointResponse500
    | DeleteFirewallAliasesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallAliasesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallAliasesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallAliasesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallAliasesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallAliasesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallAliasesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallAliasesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallAliasesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallAliasesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallAliasesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallAliasesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallAliasesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallAliasesEndpointResponse400
    | DeleteFirewallAliasesEndpointResponse401
    | DeleteFirewallAliasesEndpointResponse403
    | DeleteFirewallAliasesEndpointResponse404
    | DeleteFirewallAliasesEndpointResponse405
    | DeleteFirewallAliasesEndpointResponse406
    | DeleteFirewallAliasesEndpointResponse409
    | DeleteFirewallAliasesEndpointResponse415
    | DeleteFirewallAliasesEndpointResponse422
    | DeleteFirewallAliasesEndpointResponse424
    | DeleteFirewallAliasesEndpointResponse500
    | DeleteFirewallAliasesEndpointResponse503
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
    query: DeleteFirewallAliasesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteFirewallAliasesEndpointResponse400
    | DeleteFirewallAliasesEndpointResponse401
    | DeleteFirewallAliasesEndpointResponse403
    | DeleteFirewallAliasesEndpointResponse404
    | DeleteFirewallAliasesEndpointResponse405
    | DeleteFirewallAliasesEndpointResponse406
    | DeleteFirewallAliasesEndpointResponse409
    | DeleteFirewallAliasesEndpointResponse415
    | DeleteFirewallAliasesEndpointResponse422
    | DeleteFirewallAliasesEndpointResponse424
    | DeleteFirewallAliasesEndpointResponse500
    | DeleteFirewallAliasesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Firewall Aliases using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-aliases-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallAliasesEndpointResponse400 | DeleteFirewallAliasesEndpointResponse401 | DeleteFirewallAliasesEndpointResponse403 | DeleteFirewallAliasesEndpointResponse404 | DeleteFirewallAliasesEndpointResponse405 | DeleteFirewallAliasesEndpointResponse406 | DeleteFirewallAliasesEndpointResponse409 | DeleteFirewallAliasesEndpointResponse415 | DeleteFirewallAliasesEndpointResponse422 | DeleteFirewallAliasesEndpointResponse424 | DeleteFirewallAliasesEndpointResponse500 | DeleteFirewallAliasesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
    query: DeleteFirewallAliasesEndpointQuery | Unset = UNSET,
) -> (
    DeleteFirewallAliasesEndpointResponse400
    | DeleteFirewallAliasesEndpointResponse401
    | DeleteFirewallAliasesEndpointResponse403
    | DeleteFirewallAliasesEndpointResponse404
    | DeleteFirewallAliasesEndpointResponse405
    | DeleteFirewallAliasesEndpointResponse406
    | DeleteFirewallAliasesEndpointResponse409
    | DeleteFirewallAliasesEndpointResponse415
    | DeleteFirewallAliasesEndpointResponse422
    | DeleteFirewallAliasesEndpointResponse424
    | DeleteFirewallAliasesEndpointResponse500
    | DeleteFirewallAliasesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Firewall Aliases using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-aliases-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallAliasesEndpointResponse400 | DeleteFirewallAliasesEndpointResponse401 | DeleteFirewallAliasesEndpointResponse403 | DeleteFirewallAliasesEndpointResponse404 | DeleteFirewallAliasesEndpointResponse405 | DeleteFirewallAliasesEndpointResponse406 | DeleteFirewallAliasesEndpointResponse409 | DeleteFirewallAliasesEndpointResponse415 | DeleteFirewallAliasesEndpointResponse422 | DeleteFirewallAliasesEndpointResponse424 | DeleteFirewallAliasesEndpointResponse500 | DeleteFirewallAliasesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteFirewallAliasesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteFirewallAliasesEndpointResponse400
    | DeleteFirewallAliasesEndpointResponse401
    | DeleteFirewallAliasesEndpointResponse403
    | DeleteFirewallAliasesEndpointResponse404
    | DeleteFirewallAliasesEndpointResponse405
    | DeleteFirewallAliasesEndpointResponse406
    | DeleteFirewallAliasesEndpointResponse409
    | DeleteFirewallAliasesEndpointResponse415
    | DeleteFirewallAliasesEndpointResponse422
    | DeleteFirewallAliasesEndpointResponse424
    | DeleteFirewallAliasesEndpointResponse500
    | DeleteFirewallAliasesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Firewall Aliases using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-aliases-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallAliasesEndpointResponse400 | DeleteFirewallAliasesEndpointResponse401 | DeleteFirewallAliasesEndpointResponse403 | DeleteFirewallAliasesEndpointResponse404 | DeleteFirewallAliasesEndpointResponse405 | DeleteFirewallAliasesEndpointResponse406 | DeleteFirewallAliasesEndpointResponse409 | DeleteFirewallAliasesEndpointResponse415 | DeleteFirewallAliasesEndpointResponse422 | DeleteFirewallAliasesEndpointResponse424 | DeleteFirewallAliasesEndpointResponse500 | DeleteFirewallAliasesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteFirewallAliasesEndpointQuery | Unset = UNSET,
) -> (
    DeleteFirewallAliasesEndpointResponse400
    | DeleteFirewallAliasesEndpointResponse401
    | DeleteFirewallAliasesEndpointResponse403
    | DeleteFirewallAliasesEndpointResponse404
    | DeleteFirewallAliasesEndpointResponse405
    | DeleteFirewallAliasesEndpointResponse406
    | DeleteFirewallAliasesEndpointResponse409
    | DeleteFirewallAliasesEndpointResponse415
    | DeleteFirewallAliasesEndpointResponse422
    | DeleteFirewallAliasesEndpointResponse424
    | DeleteFirewallAliasesEndpointResponse500
    | DeleteFirewallAliasesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Firewall Aliases using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-aliases-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallAliasesEndpointResponse400 | DeleteFirewallAliasesEndpointResponse401 | DeleteFirewallAliasesEndpointResponse403 | DeleteFirewallAliasesEndpointResponse404 | DeleteFirewallAliasesEndpointResponse405 | DeleteFirewallAliasesEndpointResponse406 | DeleteFirewallAliasesEndpointResponse409 | DeleteFirewallAliasesEndpointResponse415 | DeleteFirewallAliasesEndpointResponse422 | DeleteFirewallAliasesEndpointResponse424 | DeleteFirewallAliasesEndpointResponse500 | DeleteFirewallAliasesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
