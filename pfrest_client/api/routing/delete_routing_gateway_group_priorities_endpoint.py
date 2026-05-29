from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_routing_gateway_group_priorities_endpoint_query import (
    DeleteRoutingGatewayGroupPrioritiesEndpointQuery,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_400 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_401 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse401,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_403 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse403,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_404 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse404,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_405 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse405,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_406 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse406,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_409 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse409,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_415 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse415,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_422 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse422,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_424 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse424,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_500 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse500,
)
from ...models.delete_routing_gateway_group_priorities_endpoint_response_503 import (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/routing/gateway/group/priorities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteRoutingGatewayGroupPrioritiesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
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
    query: DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Routing Gateway Group Priorities using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priorities-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRoutingGatewayGroupPrioritiesEndpointResponse400 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503]
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
    query: DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset = UNSET,
) -> (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Routing Gateway Group Priorities using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priorities-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRoutingGatewayGroupPrioritiesEndpointResponse400 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
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
    query: DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Routing Gateway Group Priorities using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priorities-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRoutingGatewayGroupPrioritiesEndpointResponse400 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503]
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
    query: DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset = UNSET,
) -> (
    DeleteRoutingGatewayGroupPrioritiesEndpointResponse400
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500
    | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Routing Gateway Group Priorities using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priorities-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteRoutingGatewayGroupPrioritiesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRoutingGatewayGroupPrioritiesEndpointResponse400 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse401 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse403 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse404 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse405 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse406 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse409 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse415 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse422 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse424 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse500 | DeleteRoutingGatewayGroupPrioritiesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
