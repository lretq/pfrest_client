from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dns_resolver_access_list_network_endpoint_data_body import (
    PatchServicesDNSResolverAccessListNetworkEndpointDataBody,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_json_body import (
    PatchServicesDNSResolverAccessListNetworkEndpointJsonBody,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_400 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_401 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse401,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_403 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse403,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_404 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse404,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_405 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse405,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_406 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse406,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_409 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse409,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_415 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse415,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_422 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse422,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_424 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse424,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_500 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse500,
)
from ...models.patch_services_dns_resolver_access_list_network_endpoint_response_503 import (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PatchServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dns_resolver/access_list/network",
    }

    if isinstance(body, PatchServicesDNSResolverAccessListNetworkEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDNSResolverAccessListNetworkEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse401
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse403
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse404
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse405
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse406
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse409
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse415
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse422
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse424
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse500
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDNSResolverAccessListNetworkEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDNSResolverAccessListNetworkEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDNSResolverAccessListNetworkEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDNSResolverAccessListNetworkEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDNSResolverAccessListNetworkEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDNSResolverAccessListNetworkEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDNSResolverAccessListNetworkEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDNSResolverAccessListNetworkEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDNSResolverAccessListNetworkEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDNSResolverAccessListNetworkEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDNSResolverAccessListNetworkEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDNSResolverAccessListNetworkEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse401
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse403
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse404
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse405
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse406
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse409
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse415
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse422
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse424
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse500
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
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
    body: PatchServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PatchServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse401
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse403
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse404
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse405
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse406
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse409
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse415
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse422
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse424
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse500
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverAccessListNetworkEndpointResponse400 | PatchServicesDNSResolverAccessListNetworkEndpointResponse401 | PatchServicesDNSResolverAccessListNetworkEndpointResponse403 | PatchServicesDNSResolverAccessListNetworkEndpointResponse404 | PatchServicesDNSResolverAccessListNetworkEndpointResponse405 | PatchServicesDNSResolverAccessListNetworkEndpointResponse406 | PatchServicesDNSResolverAccessListNetworkEndpointResponse409 | PatchServicesDNSResolverAccessListNetworkEndpointResponse415 | PatchServicesDNSResolverAccessListNetworkEndpointResponse422 | PatchServicesDNSResolverAccessListNetworkEndpointResponse424 | PatchServicesDNSResolverAccessListNetworkEndpointResponse500 | PatchServicesDNSResolverAccessListNetworkEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PatchServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse401
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse403
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse404
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse405
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse406
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse409
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse415
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse422
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse424
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse500
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverAccessListNetworkEndpointResponse400 | PatchServicesDNSResolverAccessListNetworkEndpointResponse401 | PatchServicesDNSResolverAccessListNetworkEndpointResponse403 | PatchServicesDNSResolverAccessListNetworkEndpointResponse404 | PatchServicesDNSResolverAccessListNetworkEndpointResponse405 | PatchServicesDNSResolverAccessListNetworkEndpointResponse406 | PatchServicesDNSResolverAccessListNetworkEndpointResponse409 | PatchServicesDNSResolverAccessListNetworkEndpointResponse415 | PatchServicesDNSResolverAccessListNetworkEndpointResponse422 | PatchServicesDNSResolverAccessListNetworkEndpointResponse424 | PatchServicesDNSResolverAccessListNetworkEndpointResponse500 | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PatchServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse401
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse403
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse404
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse405
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse406
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse409
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse415
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse422
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse424
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse500
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverAccessListNetworkEndpointResponse400 | PatchServicesDNSResolverAccessListNetworkEndpointResponse401 | PatchServicesDNSResolverAccessListNetworkEndpointResponse403 | PatchServicesDNSResolverAccessListNetworkEndpointResponse404 | PatchServicesDNSResolverAccessListNetworkEndpointResponse405 | PatchServicesDNSResolverAccessListNetworkEndpointResponse406 | PatchServicesDNSResolverAccessListNetworkEndpointResponse409 | PatchServicesDNSResolverAccessListNetworkEndpointResponse415 | PatchServicesDNSResolverAccessListNetworkEndpointResponse422 | PatchServicesDNSResolverAccessListNetworkEndpointResponse424 | PatchServicesDNSResolverAccessListNetworkEndpointResponse500 | PatchServicesDNSResolverAccessListNetworkEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverAccessListNetworkEndpointJsonBody
    | PatchServicesDNSResolverAccessListNetworkEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverAccessListNetworkEndpointResponse400
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse401
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse403
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse404
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse405
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse406
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse409
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse415
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse422
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse424
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse500
    | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List
    Network.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverAccessListNetwork<br>**Parent model**: DNSResolverAccessList<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-network-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverAccessListNetworkEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListNetworkEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverAccessListNetworkEndpointResponse400 | PatchServicesDNSResolverAccessListNetworkEndpointResponse401 | PatchServicesDNSResolverAccessListNetworkEndpointResponse403 | PatchServicesDNSResolverAccessListNetworkEndpointResponse404 | PatchServicesDNSResolverAccessListNetworkEndpointResponse405 | PatchServicesDNSResolverAccessListNetworkEndpointResponse406 | PatchServicesDNSResolverAccessListNetworkEndpointResponse409 | PatchServicesDNSResolverAccessListNetworkEndpointResponse415 | PatchServicesDNSResolverAccessListNetworkEndpointResponse422 | PatchServicesDNSResolverAccessListNetworkEndpointResponse424 | PatchServicesDNSResolverAccessListNetworkEndpointResponse500 | PatchServicesDNSResolverAccessListNetworkEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
