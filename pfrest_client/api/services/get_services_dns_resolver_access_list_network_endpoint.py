from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_400 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse400,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_401 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse401,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_403 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse403,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_404 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse404,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_405 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse405,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_406 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse406,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_409 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse409,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_415 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse415,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_422 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse422,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_424 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse424,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_500 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse500,
)
from ...models.get_services_dns_resolver_access_list_network_endpoint_response_503 import (
    GetServicesDNSResolverAccessListNetworkEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/dns_resolver/access_list/network",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDNSResolverAccessListNetworkEndpointResponse400
    | GetServicesDNSResolverAccessListNetworkEndpointResponse401
    | GetServicesDNSResolverAccessListNetworkEndpointResponse403
    | GetServicesDNSResolverAccessListNetworkEndpointResponse404
    | GetServicesDNSResolverAccessListNetworkEndpointResponse405
    | GetServicesDNSResolverAccessListNetworkEndpointResponse406
    | GetServicesDNSResolverAccessListNetworkEndpointResponse409
    | GetServicesDNSResolverAccessListNetworkEndpointResponse415
    | GetServicesDNSResolverAccessListNetworkEndpointResponse422
    | GetServicesDNSResolverAccessListNetworkEndpointResponse424
    | GetServicesDNSResolverAccessListNetworkEndpointResponse500
    | GetServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDNSResolverAccessListNetworkEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDNSResolverAccessListNetworkEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDNSResolverAccessListNetworkEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDNSResolverAccessListNetworkEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDNSResolverAccessListNetworkEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDNSResolverAccessListNetworkEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDNSResolverAccessListNetworkEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDNSResolverAccessListNetworkEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDNSResolverAccessListNetworkEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDNSResolverAccessListNetworkEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDNSResolverAccessListNetworkEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDNSResolverAccessListNetworkEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDNSResolverAccessListNetworkEndpointResponse400
    | GetServicesDNSResolverAccessListNetworkEndpointResponse401
    | GetServicesDNSResolverAccessListNetworkEndpointResponse403
    | GetServicesDNSResolverAccessListNetworkEndpointResponse404
    | GetServicesDNSResolverAccessListNetworkEndpointResponse405
    | GetServicesDNSResolverAccessListNetworkEndpointResponse406
    | GetServicesDNSResolverAccessListNetworkEndpointResponse409
    | GetServicesDNSResolverAccessListNetworkEndpointResponse415
    | GetServicesDNSResolverAccessListNetworkEndpointResponse422
    | GetServicesDNSResolverAccessListNetworkEndpointResponse424
    | GetServicesDNSResolverAccessListNetworkEndpointResponse500
    | GetServicesDNSResolverAccessListNetworkEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetServicesDNSResolverAccessListNetworkEndpointResponse400
    | GetServicesDNSResolverAccessListNetworkEndpointResponse401
    | GetServicesDNSResolverAccessListNetworkEndpointResponse403
    | GetServicesDNSResolverAccessListNetworkEndpointResponse404
    | GetServicesDNSResolverAccessListNetworkEndpointResponse405
    | GetServicesDNSResolverAccessListNetworkEndpointResponse406
    | GetServicesDNSResolverAccessListNetworkEndpointResponse409
    | GetServicesDNSResolverAccessListNetworkEndpointResponse415
    | GetServicesDNSResolverAccessListNetworkEndpointResponse422
    | GetServicesDNSResolverAccessListNetworkEndpointResponse424
    | GetServicesDNSResolverAccessListNetworkEndpointResponse500
    | GetServicesDNSResolverAccessListNetworkEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSResolverAccessListNetworkEndpointResponse400 | GetServicesDNSResolverAccessListNetworkEndpointResponse401 | GetServicesDNSResolverAccessListNetworkEndpointResponse403 | GetServicesDNSResolverAccessListNetworkEndpointResponse404 | GetServicesDNSResolverAccessListNetworkEndpointResponse405 | GetServicesDNSResolverAccessListNetworkEndpointResponse406 | GetServicesDNSResolverAccessListNetworkEndpointResponse409 | GetServicesDNSResolverAccessListNetworkEndpointResponse415 | GetServicesDNSResolverAccessListNetworkEndpointResponse422 | GetServicesDNSResolverAccessListNetworkEndpointResponse424 | GetServicesDNSResolverAccessListNetworkEndpointResponse500 | GetServicesDNSResolverAccessListNetworkEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetServicesDNSResolverAccessListNetworkEndpointResponse400
    | GetServicesDNSResolverAccessListNetworkEndpointResponse401
    | GetServicesDNSResolverAccessListNetworkEndpointResponse403
    | GetServicesDNSResolverAccessListNetworkEndpointResponse404
    | GetServicesDNSResolverAccessListNetworkEndpointResponse405
    | GetServicesDNSResolverAccessListNetworkEndpointResponse406
    | GetServicesDNSResolverAccessListNetworkEndpointResponse409
    | GetServicesDNSResolverAccessListNetworkEndpointResponse415
    | GetServicesDNSResolverAccessListNetworkEndpointResponse422
    | GetServicesDNSResolverAccessListNetworkEndpointResponse424
    | GetServicesDNSResolverAccessListNetworkEndpointResponse500
    | GetServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSResolverAccessListNetworkEndpointResponse400 | GetServicesDNSResolverAccessListNetworkEndpointResponse401 | GetServicesDNSResolverAccessListNetworkEndpointResponse403 | GetServicesDNSResolverAccessListNetworkEndpointResponse404 | GetServicesDNSResolverAccessListNetworkEndpointResponse405 | GetServicesDNSResolverAccessListNetworkEndpointResponse406 | GetServicesDNSResolverAccessListNetworkEndpointResponse409 | GetServicesDNSResolverAccessListNetworkEndpointResponse415 | GetServicesDNSResolverAccessListNetworkEndpointResponse422 | GetServicesDNSResolverAccessListNetworkEndpointResponse424 | GetServicesDNSResolverAccessListNetworkEndpointResponse500 | GetServicesDNSResolverAccessListNetworkEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetServicesDNSResolverAccessListNetworkEndpointResponse400
    | GetServicesDNSResolverAccessListNetworkEndpointResponse401
    | GetServicesDNSResolverAccessListNetworkEndpointResponse403
    | GetServicesDNSResolverAccessListNetworkEndpointResponse404
    | GetServicesDNSResolverAccessListNetworkEndpointResponse405
    | GetServicesDNSResolverAccessListNetworkEndpointResponse406
    | GetServicesDNSResolverAccessListNetworkEndpointResponse409
    | GetServicesDNSResolverAccessListNetworkEndpointResponse415
    | GetServicesDNSResolverAccessListNetworkEndpointResponse422
    | GetServicesDNSResolverAccessListNetworkEndpointResponse424
    | GetServicesDNSResolverAccessListNetworkEndpointResponse500
    | GetServicesDNSResolverAccessListNetworkEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSResolverAccessListNetworkEndpointResponse400 | GetServicesDNSResolverAccessListNetworkEndpointResponse401 | GetServicesDNSResolverAccessListNetworkEndpointResponse403 | GetServicesDNSResolverAccessListNetworkEndpointResponse404 | GetServicesDNSResolverAccessListNetworkEndpointResponse405 | GetServicesDNSResolverAccessListNetworkEndpointResponse406 | GetServicesDNSResolverAccessListNetworkEndpointResponse409 | GetServicesDNSResolverAccessListNetworkEndpointResponse415 | GetServicesDNSResolverAccessListNetworkEndpointResponse422 | GetServicesDNSResolverAccessListNetworkEndpointResponse424 | GetServicesDNSResolverAccessListNetworkEndpointResponse500 | GetServicesDNSResolverAccessListNetworkEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetServicesDNSResolverAccessListNetworkEndpointResponse400
    | GetServicesDNSResolverAccessListNetworkEndpointResponse401
    | GetServicesDNSResolverAccessListNetworkEndpointResponse403
    | GetServicesDNSResolverAccessListNetworkEndpointResponse404
    | GetServicesDNSResolverAccessListNetworkEndpointResponse405
    | GetServicesDNSResolverAccessListNetworkEndpointResponse406
    | GetServicesDNSResolverAccessListNetworkEndpointResponse409
    | GetServicesDNSResolverAccessListNetworkEndpointResponse415
    | GetServicesDNSResolverAccessListNetworkEndpointResponse422
    | GetServicesDNSResolverAccessListNetworkEndpointResponse424
    | GetServicesDNSResolverAccessListNetworkEndpointResponse500
    | GetServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSResolverAccessListNetworkEndpointResponse400 | GetServicesDNSResolverAccessListNetworkEndpointResponse401 | GetServicesDNSResolverAccessListNetworkEndpointResponse403 | GetServicesDNSResolverAccessListNetworkEndpointResponse404 | GetServicesDNSResolverAccessListNetworkEndpointResponse405 | GetServicesDNSResolverAccessListNetworkEndpointResponse406 | GetServicesDNSResolverAccessListNetworkEndpointResponse409 | GetServicesDNSResolverAccessListNetworkEndpointResponse415 | GetServicesDNSResolverAccessListNetworkEndpointResponse422 | GetServicesDNSResolverAccessListNetworkEndpointResponse424 | GetServicesDNSResolverAccessListNetworkEndpointResponse500 | GetServicesDNSResolverAccessListNetworkEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
