from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dns_forwarder_apply_endpoint_response_400 import (
    GetServicesDNSForwarderApplyEndpointResponse400,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_401 import (
    GetServicesDNSForwarderApplyEndpointResponse401,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_403 import (
    GetServicesDNSForwarderApplyEndpointResponse403,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_404 import (
    GetServicesDNSForwarderApplyEndpointResponse404,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_405 import (
    GetServicesDNSForwarderApplyEndpointResponse405,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_406 import (
    GetServicesDNSForwarderApplyEndpointResponse406,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_409 import (
    GetServicesDNSForwarderApplyEndpointResponse409,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_415 import (
    GetServicesDNSForwarderApplyEndpointResponse415,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_422 import (
    GetServicesDNSForwarderApplyEndpointResponse422,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_424 import (
    GetServicesDNSForwarderApplyEndpointResponse424,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_500 import (
    GetServicesDNSForwarderApplyEndpointResponse500,
)
from ...models.get_services_dns_forwarder_apply_endpoint_response_503 import (
    GetServicesDNSForwarderApplyEndpointResponse503,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/dns_forwarder/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDNSForwarderApplyEndpointResponse400
    | GetServicesDNSForwarderApplyEndpointResponse401
    | GetServicesDNSForwarderApplyEndpointResponse403
    | GetServicesDNSForwarderApplyEndpointResponse404
    | GetServicesDNSForwarderApplyEndpointResponse405
    | GetServicesDNSForwarderApplyEndpointResponse406
    | GetServicesDNSForwarderApplyEndpointResponse409
    | GetServicesDNSForwarderApplyEndpointResponse415
    | GetServicesDNSForwarderApplyEndpointResponse422
    | GetServicesDNSForwarderApplyEndpointResponse424
    | GetServicesDNSForwarderApplyEndpointResponse500
    | GetServicesDNSForwarderApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDNSForwarderApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDNSForwarderApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDNSForwarderApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDNSForwarderApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDNSForwarderApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDNSForwarderApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDNSForwarderApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDNSForwarderApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDNSForwarderApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDNSForwarderApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDNSForwarderApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDNSForwarderApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDNSForwarderApplyEndpointResponse400
    | GetServicesDNSForwarderApplyEndpointResponse401
    | GetServicesDNSForwarderApplyEndpointResponse403
    | GetServicesDNSForwarderApplyEndpointResponse404
    | GetServicesDNSForwarderApplyEndpointResponse405
    | GetServicesDNSForwarderApplyEndpointResponse406
    | GetServicesDNSForwarderApplyEndpointResponse409
    | GetServicesDNSForwarderApplyEndpointResponse415
    | GetServicesDNSForwarderApplyEndpointResponse422
    | GetServicesDNSForwarderApplyEndpointResponse424
    | GetServicesDNSForwarderApplyEndpointResponse500
    | GetServicesDNSForwarderApplyEndpointResponse503
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
    GetServicesDNSForwarderApplyEndpointResponse400
    | GetServicesDNSForwarderApplyEndpointResponse401
    | GetServicesDNSForwarderApplyEndpointResponse403
    | GetServicesDNSForwarderApplyEndpointResponse404
    | GetServicesDNSForwarderApplyEndpointResponse405
    | GetServicesDNSForwarderApplyEndpointResponse406
    | GetServicesDNSForwarderApplyEndpointResponse409
    | GetServicesDNSForwarderApplyEndpointResponse415
    | GetServicesDNSForwarderApplyEndpointResponse422
    | GetServicesDNSForwarderApplyEndpointResponse424
    | GetServicesDNSForwarderApplyEndpointResponse500
    | GetServicesDNSForwarderApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending DNS Forwarder change status.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSForwarderApplyEndpointResponse400 | GetServicesDNSForwarderApplyEndpointResponse401 | GetServicesDNSForwarderApplyEndpointResponse403 | GetServicesDNSForwarderApplyEndpointResponse404 | GetServicesDNSForwarderApplyEndpointResponse405 | GetServicesDNSForwarderApplyEndpointResponse406 | GetServicesDNSForwarderApplyEndpointResponse409 | GetServicesDNSForwarderApplyEndpointResponse415 | GetServicesDNSForwarderApplyEndpointResponse422 | GetServicesDNSForwarderApplyEndpointResponse424 | GetServicesDNSForwarderApplyEndpointResponse500 | GetServicesDNSForwarderApplyEndpointResponse503]
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
    GetServicesDNSForwarderApplyEndpointResponse400
    | GetServicesDNSForwarderApplyEndpointResponse401
    | GetServicesDNSForwarderApplyEndpointResponse403
    | GetServicesDNSForwarderApplyEndpointResponse404
    | GetServicesDNSForwarderApplyEndpointResponse405
    | GetServicesDNSForwarderApplyEndpointResponse406
    | GetServicesDNSForwarderApplyEndpointResponse409
    | GetServicesDNSForwarderApplyEndpointResponse415
    | GetServicesDNSForwarderApplyEndpointResponse422
    | GetServicesDNSForwarderApplyEndpointResponse424
    | GetServicesDNSForwarderApplyEndpointResponse500
    | GetServicesDNSForwarderApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending DNS Forwarder change status.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSForwarderApplyEndpointResponse400 | GetServicesDNSForwarderApplyEndpointResponse401 | GetServicesDNSForwarderApplyEndpointResponse403 | GetServicesDNSForwarderApplyEndpointResponse404 | GetServicesDNSForwarderApplyEndpointResponse405 | GetServicesDNSForwarderApplyEndpointResponse406 | GetServicesDNSForwarderApplyEndpointResponse409 | GetServicesDNSForwarderApplyEndpointResponse415 | GetServicesDNSForwarderApplyEndpointResponse422 | GetServicesDNSForwarderApplyEndpointResponse424 | GetServicesDNSForwarderApplyEndpointResponse500 | GetServicesDNSForwarderApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesDNSForwarderApplyEndpointResponse400
    | GetServicesDNSForwarderApplyEndpointResponse401
    | GetServicesDNSForwarderApplyEndpointResponse403
    | GetServicesDNSForwarderApplyEndpointResponse404
    | GetServicesDNSForwarderApplyEndpointResponse405
    | GetServicesDNSForwarderApplyEndpointResponse406
    | GetServicesDNSForwarderApplyEndpointResponse409
    | GetServicesDNSForwarderApplyEndpointResponse415
    | GetServicesDNSForwarderApplyEndpointResponse422
    | GetServicesDNSForwarderApplyEndpointResponse424
    | GetServicesDNSForwarderApplyEndpointResponse500
    | GetServicesDNSForwarderApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending DNS Forwarder change status.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDNSForwarderApplyEndpointResponse400 | GetServicesDNSForwarderApplyEndpointResponse401 | GetServicesDNSForwarderApplyEndpointResponse403 | GetServicesDNSForwarderApplyEndpointResponse404 | GetServicesDNSForwarderApplyEndpointResponse405 | GetServicesDNSForwarderApplyEndpointResponse406 | GetServicesDNSForwarderApplyEndpointResponse409 | GetServicesDNSForwarderApplyEndpointResponse415 | GetServicesDNSForwarderApplyEndpointResponse422 | GetServicesDNSForwarderApplyEndpointResponse424 | GetServicesDNSForwarderApplyEndpointResponse500 | GetServicesDNSForwarderApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesDNSForwarderApplyEndpointResponse400
    | GetServicesDNSForwarderApplyEndpointResponse401
    | GetServicesDNSForwarderApplyEndpointResponse403
    | GetServicesDNSForwarderApplyEndpointResponse404
    | GetServicesDNSForwarderApplyEndpointResponse405
    | GetServicesDNSForwarderApplyEndpointResponse406
    | GetServicesDNSForwarderApplyEndpointResponse409
    | GetServicesDNSForwarderApplyEndpointResponse415
    | GetServicesDNSForwarderApplyEndpointResponse422
    | GetServicesDNSForwarderApplyEndpointResponse424
    | GetServicesDNSForwarderApplyEndpointResponse500
    | GetServicesDNSForwarderApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending DNS Forwarder change status.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDNSForwarderApplyEndpointResponse400 | GetServicesDNSForwarderApplyEndpointResponse401 | GetServicesDNSForwarderApplyEndpointResponse403 | GetServicesDNSForwarderApplyEndpointResponse404 | GetServicesDNSForwarderApplyEndpointResponse405 | GetServicesDNSForwarderApplyEndpointResponse406 | GetServicesDNSForwarderApplyEndpointResponse409 | GetServicesDNSForwarderApplyEndpointResponse415 | GetServicesDNSForwarderApplyEndpointResponse422 | GetServicesDNSForwarderApplyEndpointResponse424 | GetServicesDNSForwarderApplyEndpointResponse500 | GetServicesDNSForwarderApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
