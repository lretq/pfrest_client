from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dns_resolver_access_list_endpoint_response_400 import (
    GetServicesDNSResolverAccessListEndpointResponse400,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_401 import (
    GetServicesDNSResolverAccessListEndpointResponse401,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_403 import (
    GetServicesDNSResolverAccessListEndpointResponse403,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_404 import (
    GetServicesDNSResolverAccessListEndpointResponse404,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_405 import (
    GetServicesDNSResolverAccessListEndpointResponse405,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_406 import (
    GetServicesDNSResolverAccessListEndpointResponse406,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_409 import (
    GetServicesDNSResolverAccessListEndpointResponse409,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_415 import (
    GetServicesDNSResolverAccessListEndpointResponse415,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_422 import (
    GetServicesDNSResolverAccessListEndpointResponse422,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_424 import (
    GetServicesDNSResolverAccessListEndpointResponse424,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_500 import (
    GetServicesDNSResolverAccessListEndpointResponse500,
)
from ...models.get_services_dns_resolver_access_list_endpoint_response_503 import (
    GetServicesDNSResolverAccessListEndpointResponse503,
)
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
        "url": "/api/v2/services/dns_resolver/access_list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDNSResolverAccessListEndpointResponse400
    | GetServicesDNSResolverAccessListEndpointResponse401
    | GetServicesDNSResolverAccessListEndpointResponse403
    | GetServicesDNSResolverAccessListEndpointResponse404
    | GetServicesDNSResolverAccessListEndpointResponse405
    | GetServicesDNSResolverAccessListEndpointResponse406
    | GetServicesDNSResolverAccessListEndpointResponse409
    | GetServicesDNSResolverAccessListEndpointResponse415
    | GetServicesDNSResolverAccessListEndpointResponse422
    | GetServicesDNSResolverAccessListEndpointResponse424
    | GetServicesDNSResolverAccessListEndpointResponse500
    | GetServicesDNSResolverAccessListEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDNSResolverAccessListEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDNSResolverAccessListEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDNSResolverAccessListEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDNSResolverAccessListEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDNSResolverAccessListEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDNSResolverAccessListEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDNSResolverAccessListEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDNSResolverAccessListEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDNSResolverAccessListEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDNSResolverAccessListEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDNSResolverAccessListEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDNSResolverAccessListEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDNSResolverAccessListEndpointResponse400
    | GetServicesDNSResolverAccessListEndpointResponse401
    | GetServicesDNSResolverAccessListEndpointResponse403
    | GetServicesDNSResolverAccessListEndpointResponse404
    | GetServicesDNSResolverAccessListEndpointResponse405
    | GetServicesDNSResolverAccessListEndpointResponse406
    | GetServicesDNSResolverAccessListEndpointResponse409
    | GetServicesDNSResolverAccessListEndpointResponse415
    | GetServicesDNSResolverAccessListEndpointResponse422
    | GetServicesDNSResolverAccessListEndpointResponse424
    | GetServicesDNSResolverAccessListEndpointResponse500
    | GetServicesDNSResolverAccessListEndpointResponse503
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
    GetServicesDNSResolverAccessListEndpointResponse400
    | GetServicesDNSResolverAccessListEndpointResponse401
    | GetServicesDNSResolverAccessListEndpointResponse403
    | GetServicesDNSResolverAccessListEndpointResponse404
    | GetServicesDNSResolverAccessListEndpointResponse405
    | GetServicesDNSResolverAccessListEndpointResponse406
    | GetServicesDNSResolverAccessListEndpointResponse409
    | GetServicesDNSResolverAccessListEndpointResponse415
    | GetServicesDNSResolverAccessListEndpointResponse422
    | GetServicesDNSResolverAccessListEndpointResponse424
    | GetServicesDNSResolverAccessListEndpointResponse500
    | GetServicesDNSResolverAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSResolverAccessListEndpointResponse400 | GetServicesDNSResolverAccessListEndpointResponse401 | GetServicesDNSResolverAccessListEndpointResponse403 | GetServicesDNSResolverAccessListEndpointResponse404 | GetServicesDNSResolverAccessListEndpointResponse405 | GetServicesDNSResolverAccessListEndpointResponse406 | GetServicesDNSResolverAccessListEndpointResponse409 | GetServicesDNSResolverAccessListEndpointResponse415 | GetServicesDNSResolverAccessListEndpointResponse422 | GetServicesDNSResolverAccessListEndpointResponse424 | GetServicesDNSResolverAccessListEndpointResponse500 | GetServicesDNSResolverAccessListEndpointResponse503]
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
    GetServicesDNSResolverAccessListEndpointResponse400
    | GetServicesDNSResolverAccessListEndpointResponse401
    | GetServicesDNSResolverAccessListEndpointResponse403
    | GetServicesDNSResolverAccessListEndpointResponse404
    | GetServicesDNSResolverAccessListEndpointResponse405
    | GetServicesDNSResolverAccessListEndpointResponse406
    | GetServicesDNSResolverAccessListEndpointResponse409
    | GetServicesDNSResolverAccessListEndpointResponse415
    | GetServicesDNSResolverAccessListEndpointResponse422
    | GetServicesDNSResolverAccessListEndpointResponse424
    | GetServicesDNSResolverAccessListEndpointResponse500
    | GetServicesDNSResolverAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSResolverAccessListEndpointResponse400 | GetServicesDNSResolverAccessListEndpointResponse401 | GetServicesDNSResolverAccessListEndpointResponse403 | GetServicesDNSResolverAccessListEndpointResponse404 | GetServicesDNSResolverAccessListEndpointResponse405 | GetServicesDNSResolverAccessListEndpointResponse406 | GetServicesDNSResolverAccessListEndpointResponse409 | GetServicesDNSResolverAccessListEndpointResponse415 | GetServicesDNSResolverAccessListEndpointResponse422 | GetServicesDNSResolverAccessListEndpointResponse424 | GetServicesDNSResolverAccessListEndpointResponse500 | GetServicesDNSResolverAccessListEndpointResponse503
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
    GetServicesDNSResolverAccessListEndpointResponse400
    | GetServicesDNSResolverAccessListEndpointResponse401
    | GetServicesDNSResolverAccessListEndpointResponse403
    | GetServicesDNSResolverAccessListEndpointResponse404
    | GetServicesDNSResolverAccessListEndpointResponse405
    | GetServicesDNSResolverAccessListEndpointResponse406
    | GetServicesDNSResolverAccessListEndpointResponse409
    | GetServicesDNSResolverAccessListEndpointResponse415
    | GetServicesDNSResolverAccessListEndpointResponse422
    | GetServicesDNSResolverAccessListEndpointResponse424
    | GetServicesDNSResolverAccessListEndpointResponse500
    | GetServicesDNSResolverAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSResolverAccessListEndpointResponse400 | GetServicesDNSResolverAccessListEndpointResponse401 | GetServicesDNSResolverAccessListEndpointResponse403 | GetServicesDNSResolverAccessListEndpointResponse404 | GetServicesDNSResolverAccessListEndpointResponse405 | GetServicesDNSResolverAccessListEndpointResponse406 | GetServicesDNSResolverAccessListEndpointResponse409 | GetServicesDNSResolverAccessListEndpointResponse415 | GetServicesDNSResolverAccessListEndpointResponse422 | GetServicesDNSResolverAccessListEndpointResponse424 | GetServicesDNSResolverAccessListEndpointResponse500 | GetServicesDNSResolverAccessListEndpointResponse503]
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
    GetServicesDNSResolverAccessListEndpointResponse400
    | GetServicesDNSResolverAccessListEndpointResponse401
    | GetServicesDNSResolverAccessListEndpointResponse403
    | GetServicesDNSResolverAccessListEndpointResponse404
    | GetServicesDNSResolverAccessListEndpointResponse405
    | GetServicesDNSResolverAccessListEndpointResponse406
    | GetServicesDNSResolverAccessListEndpointResponse409
    | GetServicesDNSResolverAccessListEndpointResponse415
    | GetServicesDNSResolverAccessListEndpointResponse422
    | GetServicesDNSResolverAccessListEndpointResponse424
    | GetServicesDNSResolverAccessListEndpointResponse500
    | GetServicesDNSResolverAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSResolverAccessListEndpointResponse400 | GetServicesDNSResolverAccessListEndpointResponse401 | GetServicesDNSResolverAccessListEndpointResponse403 | GetServicesDNSResolverAccessListEndpointResponse404 | GetServicesDNSResolverAccessListEndpointResponse405 | GetServicesDNSResolverAccessListEndpointResponse406 | GetServicesDNSResolverAccessListEndpointResponse409 | GetServicesDNSResolverAccessListEndpointResponse415 | GetServicesDNSResolverAccessListEndpointResponse422 | GetServicesDNSResolverAccessListEndpointResponse424 | GetServicesDNSResolverAccessListEndpointResponse500 | GetServicesDNSResolverAccessListEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
