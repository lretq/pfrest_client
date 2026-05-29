from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dns_resolver_apply_endpoint_response_400 import (
    GetServicesDNSResolverApplyEndpointResponse400,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_401 import (
    GetServicesDNSResolverApplyEndpointResponse401,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_403 import (
    GetServicesDNSResolverApplyEndpointResponse403,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_404 import (
    GetServicesDNSResolverApplyEndpointResponse404,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_405 import (
    GetServicesDNSResolverApplyEndpointResponse405,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_406 import (
    GetServicesDNSResolverApplyEndpointResponse406,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_409 import (
    GetServicesDNSResolverApplyEndpointResponse409,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_415 import (
    GetServicesDNSResolverApplyEndpointResponse415,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_422 import (
    GetServicesDNSResolverApplyEndpointResponse422,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_424 import (
    GetServicesDNSResolverApplyEndpointResponse424,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_500 import (
    GetServicesDNSResolverApplyEndpointResponse500,
)
from ...models.get_services_dns_resolver_apply_endpoint_response_503 import (
    GetServicesDNSResolverApplyEndpointResponse503,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/dns_resolver/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDNSResolverApplyEndpointResponse400
    | GetServicesDNSResolverApplyEndpointResponse401
    | GetServicesDNSResolverApplyEndpointResponse403
    | GetServicesDNSResolverApplyEndpointResponse404
    | GetServicesDNSResolverApplyEndpointResponse405
    | GetServicesDNSResolverApplyEndpointResponse406
    | GetServicesDNSResolverApplyEndpointResponse409
    | GetServicesDNSResolverApplyEndpointResponse415
    | GetServicesDNSResolverApplyEndpointResponse422
    | GetServicesDNSResolverApplyEndpointResponse424
    | GetServicesDNSResolverApplyEndpointResponse500
    | GetServicesDNSResolverApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDNSResolverApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDNSResolverApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDNSResolverApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDNSResolverApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDNSResolverApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDNSResolverApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDNSResolverApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDNSResolverApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDNSResolverApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDNSResolverApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDNSResolverApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDNSResolverApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDNSResolverApplyEndpointResponse400
    | GetServicesDNSResolverApplyEndpointResponse401
    | GetServicesDNSResolverApplyEndpointResponse403
    | GetServicesDNSResolverApplyEndpointResponse404
    | GetServicesDNSResolverApplyEndpointResponse405
    | GetServicesDNSResolverApplyEndpointResponse406
    | GetServicesDNSResolverApplyEndpointResponse409
    | GetServicesDNSResolverApplyEndpointResponse415
    | GetServicesDNSResolverApplyEndpointResponse422
    | GetServicesDNSResolverApplyEndpointResponse424
    | GetServicesDNSResolverApplyEndpointResponse500
    | GetServicesDNSResolverApplyEndpointResponse503
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
) -> Response[
    GetServicesDNSResolverApplyEndpointResponse400
    | GetServicesDNSResolverApplyEndpointResponse401
    | GetServicesDNSResolverApplyEndpointResponse403
    | GetServicesDNSResolverApplyEndpointResponse404
    | GetServicesDNSResolverApplyEndpointResponse405
    | GetServicesDNSResolverApplyEndpointResponse406
    | GetServicesDNSResolverApplyEndpointResponse409
    | GetServicesDNSResolverApplyEndpointResponse415
    | GetServicesDNSResolverApplyEndpointResponse422
    | GetServicesDNSResolverApplyEndpointResponse424
    | GetServicesDNSResolverApplyEndpointResponse500
    | GetServicesDNSResolverApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending DNS Resolver change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSResolverApplyEndpointResponse400 | GetServicesDNSResolverApplyEndpointResponse401 | GetServicesDNSResolverApplyEndpointResponse403 | GetServicesDNSResolverApplyEndpointResponse404 | GetServicesDNSResolverApplyEndpointResponse405 | GetServicesDNSResolverApplyEndpointResponse406 | GetServicesDNSResolverApplyEndpointResponse409 | GetServicesDNSResolverApplyEndpointResponse415 | GetServicesDNSResolverApplyEndpointResponse422 | GetServicesDNSResolverApplyEndpointResponse424 | GetServicesDNSResolverApplyEndpointResponse500 | GetServicesDNSResolverApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesDNSResolverApplyEndpointResponse400
    | GetServicesDNSResolverApplyEndpointResponse401
    | GetServicesDNSResolverApplyEndpointResponse403
    | GetServicesDNSResolverApplyEndpointResponse404
    | GetServicesDNSResolverApplyEndpointResponse405
    | GetServicesDNSResolverApplyEndpointResponse406
    | GetServicesDNSResolverApplyEndpointResponse409
    | GetServicesDNSResolverApplyEndpointResponse415
    | GetServicesDNSResolverApplyEndpointResponse422
    | GetServicesDNSResolverApplyEndpointResponse424
    | GetServicesDNSResolverApplyEndpointResponse500
    | GetServicesDNSResolverApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending DNS Resolver change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSResolverApplyEndpointResponse400 | GetServicesDNSResolverApplyEndpointResponse401 | GetServicesDNSResolverApplyEndpointResponse403 | GetServicesDNSResolverApplyEndpointResponse404 | GetServicesDNSResolverApplyEndpointResponse405 | GetServicesDNSResolverApplyEndpointResponse406 | GetServicesDNSResolverApplyEndpointResponse409 | GetServicesDNSResolverApplyEndpointResponse415 | GetServicesDNSResolverApplyEndpointResponse422 | GetServicesDNSResolverApplyEndpointResponse424 | GetServicesDNSResolverApplyEndpointResponse500 | GetServicesDNSResolverApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesDNSResolverApplyEndpointResponse400
    | GetServicesDNSResolverApplyEndpointResponse401
    | GetServicesDNSResolverApplyEndpointResponse403
    | GetServicesDNSResolverApplyEndpointResponse404
    | GetServicesDNSResolverApplyEndpointResponse405
    | GetServicesDNSResolverApplyEndpointResponse406
    | GetServicesDNSResolverApplyEndpointResponse409
    | GetServicesDNSResolverApplyEndpointResponse415
    | GetServicesDNSResolverApplyEndpointResponse422
    | GetServicesDNSResolverApplyEndpointResponse424
    | GetServicesDNSResolverApplyEndpointResponse500
    | GetServicesDNSResolverApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending DNS Resolver change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSResolverApplyEndpointResponse400 | GetServicesDNSResolverApplyEndpointResponse401 | GetServicesDNSResolverApplyEndpointResponse403 | GetServicesDNSResolverApplyEndpointResponse404 | GetServicesDNSResolverApplyEndpointResponse405 | GetServicesDNSResolverApplyEndpointResponse406 | GetServicesDNSResolverApplyEndpointResponse409 | GetServicesDNSResolverApplyEndpointResponse415 | GetServicesDNSResolverApplyEndpointResponse422 | GetServicesDNSResolverApplyEndpointResponse424 | GetServicesDNSResolverApplyEndpointResponse500 | GetServicesDNSResolverApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesDNSResolverApplyEndpointResponse400
    | GetServicesDNSResolverApplyEndpointResponse401
    | GetServicesDNSResolverApplyEndpointResponse403
    | GetServicesDNSResolverApplyEndpointResponse404
    | GetServicesDNSResolverApplyEndpointResponse405
    | GetServicesDNSResolverApplyEndpointResponse406
    | GetServicesDNSResolverApplyEndpointResponse409
    | GetServicesDNSResolverApplyEndpointResponse415
    | GetServicesDNSResolverApplyEndpointResponse422
    | GetServicesDNSResolverApplyEndpointResponse424
    | GetServicesDNSResolverApplyEndpointResponse500
    | GetServicesDNSResolverApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending DNS Resolver change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DNSResolverApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSResolverApplyEndpointResponse400 | GetServicesDNSResolverApplyEndpointResponse401 | GetServicesDNSResolverApplyEndpointResponse403 | GetServicesDNSResolverApplyEndpointResponse404 | GetServicesDNSResolverApplyEndpointResponse405 | GetServicesDNSResolverApplyEndpointResponse406 | GetServicesDNSResolverApplyEndpointResponse409 | GetServicesDNSResolverApplyEndpointResponse415 | GetServicesDNSResolverApplyEndpointResponse422 | GetServicesDNSResolverApplyEndpointResponse424 | GetServicesDNSResolverApplyEndpointResponse500 | GetServicesDNSResolverApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
