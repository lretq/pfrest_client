from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dns_resolver_host_override_endpoint_data_body import (
    PatchServicesDNSResolverHostOverrideEndpointDataBody,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_json_body import (
    PatchServicesDNSResolverHostOverrideEndpointJsonBody,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_400 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse400,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_401 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse401,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_403 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse403,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_404 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse404,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_405 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse405,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_406 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse406,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_409 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse409,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_415 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse415,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_422 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse422,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_424 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse424,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_500 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse500,
)
from ...models.patch_services_dns_resolver_host_override_endpoint_response_503 import (
    PatchServicesDNSResolverHostOverrideEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDNSResolverHostOverrideEndpointJsonBody
    | PatchServicesDNSResolverHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dns_resolver/host_override",
    }

    if isinstance(body, PatchServicesDNSResolverHostOverrideEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDNSResolverHostOverrideEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDNSResolverHostOverrideEndpointResponse400
    | PatchServicesDNSResolverHostOverrideEndpointResponse401
    | PatchServicesDNSResolverHostOverrideEndpointResponse403
    | PatchServicesDNSResolverHostOverrideEndpointResponse404
    | PatchServicesDNSResolverHostOverrideEndpointResponse405
    | PatchServicesDNSResolverHostOverrideEndpointResponse406
    | PatchServicesDNSResolverHostOverrideEndpointResponse409
    | PatchServicesDNSResolverHostOverrideEndpointResponse415
    | PatchServicesDNSResolverHostOverrideEndpointResponse422
    | PatchServicesDNSResolverHostOverrideEndpointResponse424
    | PatchServicesDNSResolverHostOverrideEndpointResponse500
    | PatchServicesDNSResolverHostOverrideEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDNSResolverHostOverrideEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDNSResolverHostOverrideEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDNSResolverHostOverrideEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDNSResolverHostOverrideEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDNSResolverHostOverrideEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDNSResolverHostOverrideEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDNSResolverHostOverrideEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDNSResolverHostOverrideEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDNSResolverHostOverrideEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDNSResolverHostOverrideEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDNSResolverHostOverrideEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDNSResolverHostOverrideEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDNSResolverHostOverrideEndpointResponse400
    | PatchServicesDNSResolverHostOverrideEndpointResponse401
    | PatchServicesDNSResolverHostOverrideEndpointResponse403
    | PatchServicesDNSResolverHostOverrideEndpointResponse404
    | PatchServicesDNSResolverHostOverrideEndpointResponse405
    | PatchServicesDNSResolverHostOverrideEndpointResponse406
    | PatchServicesDNSResolverHostOverrideEndpointResponse409
    | PatchServicesDNSResolverHostOverrideEndpointResponse415
    | PatchServicesDNSResolverHostOverrideEndpointResponse422
    | PatchServicesDNSResolverHostOverrideEndpointResponse424
    | PatchServicesDNSResolverHostOverrideEndpointResponse500
    | PatchServicesDNSResolverHostOverrideEndpointResponse503
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
    body: PatchServicesDNSResolverHostOverrideEndpointJsonBody
    | PatchServicesDNSResolverHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverHostOverrideEndpointResponse400
    | PatchServicesDNSResolverHostOverrideEndpointResponse401
    | PatchServicesDNSResolverHostOverrideEndpointResponse403
    | PatchServicesDNSResolverHostOverrideEndpointResponse404
    | PatchServicesDNSResolverHostOverrideEndpointResponse405
    | PatchServicesDNSResolverHostOverrideEndpointResponse406
    | PatchServicesDNSResolverHostOverrideEndpointResponse409
    | PatchServicesDNSResolverHostOverrideEndpointResponse415
    | PatchServicesDNSResolverHostOverrideEndpointResponse422
    | PatchServicesDNSResolverHostOverrideEndpointResponse424
    | PatchServicesDNSResolverHostOverrideEndpointResponse500
    | PatchServicesDNSResolverHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDNSResolverHostOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverHostOverrideEndpointResponse400 | PatchServicesDNSResolverHostOverrideEndpointResponse401 | PatchServicesDNSResolverHostOverrideEndpointResponse403 | PatchServicesDNSResolverHostOverrideEndpointResponse404 | PatchServicesDNSResolverHostOverrideEndpointResponse405 | PatchServicesDNSResolverHostOverrideEndpointResponse406 | PatchServicesDNSResolverHostOverrideEndpointResponse409 | PatchServicesDNSResolverHostOverrideEndpointResponse415 | PatchServicesDNSResolverHostOverrideEndpointResponse422 | PatchServicesDNSResolverHostOverrideEndpointResponse424 | PatchServicesDNSResolverHostOverrideEndpointResponse500 | PatchServicesDNSResolverHostOverrideEndpointResponse503]
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
    body: PatchServicesDNSResolverHostOverrideEndpointJsonBody
    | PatchServicesDNSResolverHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverHostOverrideEndpointResponse400
    | PatchServicesDNSResolverHostOverrideEndpointResponse401
    | PatchServicesDNSResolverHostOverrideEndpointResponse403
    | PatchServicesDNSResolverHostOverrideEndpointResponse404
    | PatchServicesDNSResolverHostOverrideEndpointResponse405
    | PatchServicesDNSResolverHostOverrideEndpointResponse406
    | PatchServicesDNSResolverHostOverrideEndpointResponse409
    | PatchServicesDNSResolverHostOverrideEndpointResponse415
    | PatchServicesDNSResolverHostOverrideEndpointResponse422
    | PatchServicesDNSResolverHostOverrideEndpointResponse424
    | PatchServicesDNSResolverHostOverrideEndpointResponse500
    | PatchServicesDNSResolverHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDNSResolverHostOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverHostOverrideEndpointResponse400 | PatchServicesDNSResolverHostOverrideEndpointResponse401 | PatchServicesDNSResolverHostOverrideEndpointResponse403 | PatchServicesDNSResolverHostOverrideEndpointResponse404 | PatchServicesDNSResolverHostOverrideEndpointResponse405 | PatchServicesDNSResolverHostOverrideEndpointResponse406 | PatchServicesDNSResolverHostOverrideEndpointResponse409 | PatchServicesDNSResolverHostOverrideEndpointResponse415 | PatchServicesDNSResolverHostOverrideEndpointResponse422 | PatchServicesDNSResolverHostOverrideEndpointResponse424 | PatchServicesDNSResolverHostOverrideEndpointResponse500 | PatchServicesDNSResolverHostOverrideEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverHostOverrideEndpointJsonBody
    | PatchServicesDNSResolverHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverHostOverrideEndpointResponse400
    | PatchServicesDNSResolverHostOverrideEndpointResponse401
    | PatchServicesDNSResolverHostOverrideEndpointResponse403
    | PatchServicesDNSResolverHostOverrideEndpointResponse404
    | PatchServicesDNSResolverHostOverrideEndpointResponse405
    | PatchServicesDNSResolverHostOverrideEndpointResponse406
    | PatchServicesDNSResolverHostOverrideEndpointResponse409
    | PatchServicesDNSResolverHostOverrideEndpointResponse415
    | PatchServicesDNSResolverHostOverrideEndpointResponse422
    | PatchServicesDNSResolverHostOverrideEndpointResponse424
    | PatchServicesDNSResolverHostOverrideEndpointResponse500
    | PatchServicesDNSResolverHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDNSResolverHostOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverHostOverrideEndpointResponse400 | PatchServicesDNSResolverHostOverrideEndpointResponse401 | PatchServicesDNSResolverHostOverrideEndpointResponse403 | PatchServicesDNSResolverHostOverrideEndpointResponse404 | PatchServicesDNSResolverHostOverrideEndpointResponse405 | PatchServicesDNSResolverHostOverrideEndpointResponse406 | PatchServicesDNSResolverHostOverrideEndpointResponse409 | PatchServicesDNSResolverHostOverrideEndpointResponse415 | PatchServicesDNSResolverHostOverrideEndpointResponse422 | PatchServicesDNSResolverHostOverrideEndpointResponse424 | PatchServicesDNSResolverHostOverrideEndpointResponse500 | PatchServicesDNSResolverHostOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverHostOverrideEndpointJsonBody
    | PatchServicesDNSResolverHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverHostOverrideEndpointResponse400
    | PatchServicesDNSResolverHostOverrideEndpointResponse401
    | PatchServicesDNSResolverHostOverrideEndpointResponse403
    | PatchServicesDNSResolverHostOverrideEndpointResponse404
    | PatchServicesDNSResolverHostOverrideEndpointResponse405
    | PatchServicesDNSResolverHostOverrideEndpointResponse406
    | PatchServicesDNSResolverHostOverrideEndpointResponse409
    | PatchServicesDNSResolverHostOverrideEndpointResponse415
    | PatchServicesDNSResolverHostOverrideEndpointResponse422
    | PatchServicesDNSResolverHostOverrideEndpointResponse424
    | PatchServicesDNSResolverHostOverrideEndpointResponse500
    | PatchServicesDNSResolverHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDNSResolverHostOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverHostOverrideEndpointResponse400 | PatchServicesDNSResolverHostOverrideEndpointResponse401 | PatchServicesDNSResolverHostOverrideEndpointResponse403 | PatchServicesDNSResolverHostOverrideEndpointResponse404 | PatchServicesDNSResolverHostOverrideEndpointResponse405 | PatchServicesDNSResolverHostOverrideEndpointResponse406 | PatchServicesDNSResolverHostOverrideEndpointResponse409 | PatchServicesDNSResolverHostOverrideEndpointResponse415 | PatchServicesDNSResolverHostOverrideEndpointResponse422 | PatchServicesDNSResolverHostOverrideEndpointResponse424 | PatchServicesDNSResolverHostOverrideEndpointResponse500 | PatchServicesDNSResolverHostOverrideEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
