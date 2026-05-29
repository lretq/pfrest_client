from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dns_resolver_domain_override_endpoint_data_body import (
    PatchServicesDNSResolverDomainOverrideEndpointDataBody,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_json_body import (
    PatchServicesDNSResolverDomainOverrideEndpointJsonBody,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_400 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse400,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_401 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse401,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_403 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse403,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_404 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse404,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_405 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse405,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_406 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse406,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_409 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse409,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_415 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse415,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_422 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse422,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_424 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse424,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_500 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse500,
)
from ...models.patch_services_dns_resolver_domain_override_endpoint_response_503 import (
    PatchServicesDNSResolverDomainOverrideEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDNSResolverDomainOverrideEndpointJsonBody
    | PatchServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dns_resolver/domain_override",
    }

    if isinstance(body, PatchServicesDNSResolverDomainOverrideEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDNSResolverDomainOverrideEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDNSResolverDomainOverrideEndpointResponse400
    | PatchServicesDNSResolverDomainOverrideEndpointResponse401
    | PatchServicesDNSResolverDomainOverrideEndpointResponse403
    | PatchServicesDNSResolverDomainOverrideEndpointResponse404
    | PatchServicesDNSResolverDomainOverrideEndpointResponse405
    | PatchServicesDNSResolverDomainOverrideEndpointResponse406
    | PatchServicesDNSResolverDomainOverrideEndpointResponse409
    | PatchServicesDNSResolverDomainOverrideEndpointResponse415
    | PatchServicesDNSResolverDomainOverrideEndpointResponse422
    | PatchServicesDNSResolverDomainOverrideEndpointResponse424
    | PatchServicesDNSResolverDomainOverrideEndpointResponse500
    | PatchServicesDNSResolverDomainOverrideEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDNSResolverDomainOverrideEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDNSResolverDomainOverrideEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDNSResolverDomainOverrideEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDNSResolverDomainOverrideEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDNSResolverDomainOverrideEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDNSResolverDomainOverrideEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDNSResolverDomainOverrideEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDNSResolverDomainOverrideEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDNSResolverDomainOverrideEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDNSResolverDomainOverrideEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDNSResolverDomainOverrideEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDNSResolverDomainOverrideEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDNSResolverDomainOverrideEndpointResponse400
    | PatchServicesDNSResolverDomainOverrideEndpointResponse401
    | PatchServicesDNSResolverDomainOverrideEndpointResponse403
    | PatchServicesDNSResolverDomainOverrideEndpointResponse404
    | PatchServicesDNSResolverDomainOverrideEndpointResponse405
    | PatchServicesDNSResolverDomainOverrideEndpointResponse406
    | PatchServicesDNSResolverDomainOverrideEndpointResponse409
    | PatchServicesDNSResolverDomainOverrideEndpointResponse415
    | PatchServicesDNSResolverDomainOverrideEndpointResponse422
    | PatchServicesDNSResolverDomainOverrideEndpointResponse424
    | PatchServicesDNSResolverDomainOverrideEndpointResponse500
    | PatchServicesDNSResolverDomainOverrideEndpointResponse503
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
    body: PatchServicesDNSResolverDomainOverrideEndpointJsonBody
    | PatchServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverDomainOverrideEndpointResponse400
    | PatchServicesDNSResolverDomainOverrideEndpointResponse401
    | PatchServicesDNSResolverDomainOverrideEndpointResponse403
    | PatchServicesDNSResolverDomainOverrideEndpointResponse404
    | PatchServicesDNSResolverDomainOverrideEndpointResponse405
    | PatchServicesDNSResolverDomainOverrideEndpointResponse406
    | PatchServicesDNSResolverDomainOverrideEndpointResponse409
    | PatchServicesDNSResolverDomainOverrideEndpointResponse415
    | PatchServicesDNSResolverDomainOverrideEndpointResponse422
    | PatchServicesDNSResolverDomainOverrideEndpointResponse424
    | PatchServicesDNSResolverDomainOverrideEndpointResponse500
    | PatchServicesDNSResolverDomainOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Domain
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-override-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverDomainOverrideEndpointResponse400 | PatchServicesDNSResolverDomainOverrideEndpointResponse401 | PatchServicesDNSResolverDomainOverrideEndpointResponse403 | PatchServicesDNSResolverDomainOverrideEndpointResponse404 | PatchServicesDNSResolverDomainOverrideEndpointResponse405 | PatchServicesDNSResolverDomainOverrideEndpointResponse406 | PatchServicesDNSResolverDomainOverrideEndpointResponse409 | PatchServicesDNSResolverDomainOverrideEndpointResponse415 | PatchServicesDNSResolverDomainOverrideEndpointResponse422 | PatchServicesDNSResolverDomainOverrideEndpointResponse424 | PatchServicesDNSResolverDomainOverrideEndpointResponse500 | PatchServicesDNSResolverDomainOverrideEndpointResponse503]
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
    body: PatchServicesDNSResolverDomainOverrideEndpointJsonBody
    | PatchServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverDomainOverrideEndpointResponse400
    | PatchServicesDNSResolverDomainOverrideEndpointResponse401
    | PatchServicesDNSResolverDomainOverrideEndpointResponse403
    | PatchServicesDNSResolverDomainOverrideEndpointResponse404
    | PatchServicesDNSResolverDomainOverrideEndpointResponse405
    | PatchServicesDNSResolverDomainOverrideEndpointResponse406
    | PatchServicesDNSResolverDomainOverrideEndpointResponse409
    | PatchServicesDNSResolverDomainOverrideEndpointResponse415
    | PatchServicesDNSResolverDomainOverrideEndpointResponse422
    | PatchServicesDNSResolverDomainOverrideEndpointResponse424
    | PatchServicesDNSResolverDomainOverrideEndpointResponse500
    | PatchServicesDNSResolverDomainOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Domain
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-override-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverDomainOverrideEndpointResponse400 | PatchServicesDNSResolverDomainOverrideEndpointResponse401 | PatchServicesDNSResolverDomainOverrideEndpointResponse403 | PatchServicesDNSResolverDomainOverrideEndpointResponse404 | PatchServicesDNSResolverDomainOverrideEndpointResponse405 | PatchServicesDNSResolverDomainOverrideEndpointResponse406 | PatchServicesDNSResolverDomainOverrideEndpointResponse409 | PatchServicesDNSResolverDomainOverrideEndpointResponse415 | PatchServicesDNSResolverDomainOverrideEndpointResponse422 | PatchServicesDNSResolverDomainOverrideEndpointResponse424 | PatchServicesDNSResolverDomainOverrideEndpointResponse500 | PatchServicesDNSResolverDomainOverrideEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverDomainOverrideEndpointJsonBody
    | PatchServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverDomainOverrideEndpointResponse400
    | PatchServicesDNSResolverDomainOverrideEndpointResponse401
    | PatchServicesDNSResolverDomainOverrideEndpointResponse403
    | PatchServicesDNSResolverDomainOverrideEndpointResponse404
    | PatchServicesDNSResolverDomainOverrideEndpointResponse405
    | PatchServicesDNSResolverDomainOverrideEndpointResponse406
    | PatchServicesDNSResolverDomainOverrideEndpointResponse409
    | PatchServicesDNSResolverDomainOverrideEndpointResponse415
    | PatchServicesDNSResolverDomainOverrideEndpointResponse422
    | PatchServicesDNSResolverDomainOverrideEndpointResponse424
    | PatchServicesDNSResolverDomainOverrideEndpointResponse500
    | PatchServicesDNSResolverDomainOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Domain
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-override-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverDomainOverrideEndpointResponse400 | PatchServicesDNSResolverDomainOverrideEndpointResponse401 | PatchServicesDNSResolverDomainOverrideEndpointResponse403 | PatchServicesDNSResolverDomainOverrideEndpointResponse404 | PatchServicesDNSResolverDomainOverrideEndpointResponse405 | PatchServicesDNSResolverDomainOverrideEndpointResponse406 | PatchServicesDNSResolverDomainOverrideEndpointResponse409 | PatchServicesDNSResolverDomainOverrideEndpointResponse415 | PatchServicesDNSResolverDomainOverrideEndpointResponse422 | PatchServicesDNSResolverDomainOverrideEndpointResponse424 | PatchServicesDNSResolverDomainOverrideEndpointResponse500 | PatchServicesDNSResolverDomainOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverDomainOverrideEndpointJsonBody
    | PatchServicesDNSResolverDomainOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverDomainOverrideEndpointResponse400
    | PatchServicesDNSResolverDomainOverrideEndpointResponse401
    | PatchServicesDNSResolverDomainOverrideEndpointResponse403
    | PatchServicesDNSResolverDomainOverrideEndpointResponse404
    | PatchServicesDNSResolverDomainOverrideEndpointResponse405
    | PatchServicesDNSResolverDomainOverrideEndpointResponse406
    | PatchServicesDNSResolverDomainOverrideEndpointResponse409
    | PatchServicesDNSResolverDomainOverrideEndpointResponse415
    | PatchServicesDNSResolverDomainOverrideEndpointResponse422
    | PatchServicesDNSResolverDomainOverrideEndpointResponse424
    | PatchServicesDNSResolverDomainOverrideEndpointResponse500
    | PatchServicesDNSResolverDomainOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Domain
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-override-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSResolverDomainOverrideEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverDomainOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverDomainOverrideEndpointResponse400 | PatchServicesDNSResolverDomainOverrideEndpointResponse401 | PatchServicesDNSResolverDomainOverrideEndpointResponse403 | PatchServicesDNSResolverDomainOverrideEndpointResponse404 | PatchServicesDNSResolverDomainOverrideEndpointResponse405 | PatchServicesDNSResolverDomainOverrideEndpointResponse406 | PatchServicesDNSResolverDomainOverrideEndpointResponse409 | PatchServicesDNSResolverDomainOverrideEndpointResponse415 | PatchServicesDNSResolverDomainOverrideEndpointResponse422 | PatchServicesDNSResolverDomainOverrideEndpointResponse424 | PatchServicesDNSResolverDomainOverrideEndpointResponse500 | PatchServicesDNSResolverDomainOverrideEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
