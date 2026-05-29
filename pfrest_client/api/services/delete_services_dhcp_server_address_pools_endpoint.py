from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dhcp_server_address_pools_endpoint_query import (
    DeleteServicesDHCPServerAddressPoolsEndpointQuery,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_400 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_401 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse401,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_403 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse403,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_404 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse404,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_405 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse405,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_406 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse406,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_409 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse409,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_415 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse415,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_422 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse422,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_424 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse424,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_500 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse500,
)
from ...models.delete_services_dhcp_server_address_pools_endpoint_response_503 import (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/services/dhcp_server/address_pools",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse401
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse403
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse404
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse405
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse406
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse409
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse415
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse422
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse424
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse500
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDHCPServerAddressPoolsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDHCPServerAddressPoolsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDHCPServerAddressPoolsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDHCPServerAddressPoolsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDHCPServerAddressPoolsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDHCPServerAddressPoolsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDHCPServerAddressPoolsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDHCPServerAddressPoolsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDHCPServerAddressPoolsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDHCPServerAddressPoolsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDHCPServerAddressPoolsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDHCPServerAddressPoolsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse401
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse403
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse404
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse405
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse406
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse409
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse415
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse422
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse424
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse500
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
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
    query: DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse401
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse403
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse404
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse405
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse406
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse409
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse415
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse422
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse424
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse500
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing DHCP Server Address Pools using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DHCPServerAddressPool<br>**Parent model**: DHCPServer<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dhcp-server-address-pools-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDHCPServerAddressPoolsEndpointResponse400 | DeleteServicesDHCPServerAddressPoolsEndpointResponse401 | DeleteServicesDHCPServerAddressPoolsEndpointResponse403 | DeleteServicesDHCPServerAddressPoolsEndpointResponse404 | DeleteServicesDHCPServerAddressPoolsEndpointResponse405 | DeleteServicesDHCPServerAddressPoolsEndpointResponse406 | DeleteServicesDHCPServerAddressPoolsEndpointResponse409 | DeleteServicesDHCPServerAddressPoolsEndpointResponse415 | DeleteServicesDHCPServerAddressPoolsEndpointResponse422 | DeleteServicesDHCPServerAddressPoolsEndpointResponse424 | DeleteServicesDHCPServerAddressPoolsEndpointResponse500 | DeleteServicesDHCPServerAddressPoolsEndpointResponse503]
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
    query: DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset = UNSET,
) -> (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse401
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse403
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse404
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse405
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse406
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse409
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse415
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse422
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse424
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse500
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing DHCP Server Address Pools using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DHCPServerAddressPool<br>**Parent model**: DHCPServer<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dhcp-server-address-pools-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDHCPServerAddressPoolsEndpointResponse400 | DeleteServicesDHCPServerAddressPoolsEndpointResponse401 | DeleteServicesDHCPServerAddressPoolsEndpointResponse403 | DeleteServicesDHCPServerAddressPoolsEndpointResponse404 | DeleteServicesDHCPServerAddressPoolsEndpointResponse405 | DeleteServicesDHCPServerAddressPoolsEndpointResponse406 | DeleteServicesDHCPServerAddressPoolsEndpointResponse409 | DeleteServicesDHCPServerAddressPoolsEndpointResponse415 | DeleteServicesDHCPServerAddressPoolsEndpointResponse422 | DeleteServicesDHCPServerAddressPoolsEndpointResponse424 | DeleteServicesDHCPServerAddressPoolsEndpointResponse500 | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
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
    query: DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse401
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse403
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse404
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse405
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse406
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse409
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse415
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse422
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse424
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse500
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing DHCP Server Address Pools using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DHCPServerAddressPool<br>**Parent model**: DHCPServer<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dhcp-server-address-pools-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDHCPServerAddressPoolsEndpointResponse400 | DeleteServicesDHCPServerAddressPoolsEndpointResponse401 | DeleteServicesDHCPServerAddressPoolsEndpointResponse403 | DeleteServicesDHCPServerAddressPoolsEndpointResponse404 | DeleteServicesDHCPServerAddressPoolsEndpointResponse405 | DeleteServicesDHCPServerAddressPoolsEndpointResponse406 | DeleteServicesDHCPServerAddressPoolsEndpointResponse409 | DeleteServicesDHCPServerAddressPoolsEndpointResponse415 | DeleteServicesDHCPServerAddressPoolsEndpointResponse422 | DeleteServicesDHCPServerAddressPoolsEndpointResponse424 | DeleteServicesDHCPServerAddressPoolsEndpointResponse500 | DeleteServicesDHCPServerAddressPoolsEndpointResponse503]
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
    query: DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset = UNSET,
) -> (
    DeleteServicesDHCPServerAddressPoolsEndpointResponse400
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse401
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse403
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse404
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse405
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse406
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse409
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse415
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse422
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse424
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse500
    | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing DHCP Server Address Pools using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DHCPServerAddressPool<br>**Parent model**: DHCPServer<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dhcp-server-address-pools-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDHCPServerAddressPoolsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDHCPServerAddressPoolsEndpointResponse400 | DeleteServicesDHCPServerAddressPoolsEndpointResponse401 | DeleteServicesDHCPServerAddressPoolsEndpointResponse403 | DeleteServicesDHCPServerAddressPoolsEndpointResponse404 | DeleteServicesDHCPServerAddressPoolsEndpointResponse405 | DeleteServicesDHCPServerAddressPoolsEndpointResponse406 | DeleteServicesDHCPServerAddressPoolsEndpointResponse409 | DeleteServicesDHCPServerAddressPoolsEndpointResponse415 | DeleteServicesDHCPServerAddressPoolsEndpointResponse422 | DeleteServicesDHCPServerAddressPoolsEndpointResponse424 | DeleteServicesDHCPServerAddressPoolsEndpointResponse500 | DeleteServicesDHCPServerAddressPoolsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
