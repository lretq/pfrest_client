from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dns_resolver_access_list_endpoint_data_body import (
    PatchServicesDNSResolverAccessListEndpointDataBody,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_json_body import (
    PatchServicesDNSResolverAccessListEndpointJsonBody,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_400 import (
    PatchServicesDNSResolverAccessListEndpointResponse400,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_401 import (
    PatchServicesDNSResolverAccessListEndpointResponse401,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_403 import (
    PatchServicesDNSResolverAccessListEndpointResponse403,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_404 import (
    PatchServicesDNSResolverAccessListEndpointResponse404,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_405 import (
    PatchServicesDNSResolverAccessListEndpointResponse405,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_406 import (
    PatchServicesDNSResolverAccessListEndpointResponse406,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_409 import (
    PatchServicesDNSResolverAccessListEndpointResponse409,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_415 import (
    PatchServicesDNSResolverAccessListEndpointResponse415,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_422 import (
    PatchServicesDNSResolverAccessListEndpointResponse422,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_424 import (
    PatchServicesDNSResolverAccessListEndpointResponse424,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_500 import (
    PatchServicesDNSResolverAccessListEndpointResponse500,
)
from ...models.patch_services_dns_resolver_access_list_endpoint_response_503 import (
    PatchServicesDNSResolverAccessListEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDNSResolverAccessListEndpointJsonBody
    | PatchServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dns_resolver/access_list",
    }

    if isinstance(body, PatchServicesDNSResolverAccessListEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDNSResolverAccessListEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDNSResolverAccessListEndpointResponse400
    | PatchServicesDNSResolverAccessListEndpointResponse401
    | PatchServicesDNSResolverAccessListEndpointResponse403
    | PatchServicesDNSResolverAccessListEndpointResponse404
    | PatchServicesDNSResolverAccessListEndpointResponse405
    | PatchServicesDNSResolverAccessListEndpointResponse406
    | PatchServicesDNSResolverAccessListEndpointResponse409
    | PatchServicesDNSResolverAccessListEndpointResponse415
    | PatchServicesDNSResolverAccessListEndpointResponse422
    | PatchServicesDNSResolverAccessListEndpointResponse424
    | PatchServicesDNSResolverAccessListEndpointResponse500
    | PatchServicesDNSResolverAccessListEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDNSResolverAccessListEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDNSResolverAccessListEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDNSResolverAccessListEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDNSResolverAccessListEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDNSResolverAccessListEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDNSResolverAccessListEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDNSResolverAccessListEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDNSResolverAccessListEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDNSResolverAccessListEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDNSResolverAccessListEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDNSResolverAccessListEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDNSResolverAccessListEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDNSResolverAccessListEndpointResponse400
    | PatchServicesDNSResolverAccessListEndpointResponse401
    | PatchServicesDNSResolverAccessListEndpointResponse403
    | PatchServicesDNSResolverAccessListEndpointResponse404
    | PatchServicesDNSResolverAccessListEndpointResponse405
    | PatchServicesDNSResolverAccessListEndpointResponse406
    | PatchServicesDNSResolverAccessListEndpointResponse409
    | PatchServicesDNSResolverAccessListEndpointResponse415
    | PatchServicesDNSResolverAccessListEndpointResponse422
    | PatchServicesDNSResolverAccessListEndpointResponse424
    | PatchServicesDNSResolverAccessListEndpointResponse500
    | PatchServicesDNSResolverAccessListEndpointResponse503
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
    body: PatchServicesDNSResolverAccessListEndpointJsonBody
    | PatchServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverAccessListEndpointResponse400
    | PatchServicesDNSResolverAccessListEndpointResponse401
    | PatchServicesDNSResolverAccessListEndpointResponse403
    | PatchServicesDNSResolverAccessListEndpointResponse404
    | PatchServicesDNSResolverAccessListEndpointResponse405
    | PatchServicesDNSResolverAccessListEndpointResponse406
    | PatchServicesDNSResolverAccessListEndpointResponse409
    | PatchServicesDNSResolverAccessListEndpointResponse415
    | PatchServicesDNSResolverAccessListEndpointResponse422
    | PatchServicesDNSResolverAccessListEndpointResponse424
    | PatchServicesDNSResolverAccessListEndpointResponse500
    | PatchServicesDNSResolverAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverAccessListEndpointResponse400 | PatchServicesDNSResolverAccessListEndpointResponse401 | PatchServicesDNSResolverAccessListEndpointResponse403 | PatchServicesDNSResolverAccessListEndpointResponse404 | PatchServicesDNSResolverAccessListEndpointResponse405 | PatchServicesDNSResolverAccessListEndpointResponse406 | PatchServicesDNSResolverAccessListEndpointResponse409 | PatchServicesDNSResolverAccessListEndpointResponse415 | PatchServicesDNSResolverAccessListEndpointResponse422 | PatchServicesDNSResolverAccessListEndpointResponse424 | PatchServicesDNSResolverAccessListEndpointResponse500 | PatchServicesDNSResolverAccessListEndpointResponse503]
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
    body: PatchServicesDNSResolverAccessListEndpointJsonBody
    | PatchServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverAccessListEndpointResponse400
    | PatchServicesDNSResolverAccessListEndpointResponse401
    | PatchServicesDNSResolverAccessListEndpointResponse403
    | PatchServicesDNSResolverAccessListEndpointResponse404
    | PatchServicesDNSResolverAccessListEndpointResponse405
    | PatchServicesDNSResolverAccessListEndpointResponse406
    | PatchServicesDNSResolverAccessListEndpointResponse409
    | PatchServicesDNSResolverAccessListEndpointResponse415
    | PatchServicesDNSResolverAccessListEndpointResponse422
    | PatchServicesDNSResolverAccessListEndpointResponse424
    | PatchServicesDNSResolverAccessListEndpointResponse500
    | PatchServicesDNSResolverAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverAccessListEndpointResponse400 | PatchServicesDNSResolverAccessListEndpointResponse401 | PatchServicesDNSResolverAccessListEndpointResponse403 | PatchServicesDNSResolverAccessListEndpointResponse404 | PatchServicesDNSResolverAccessListEndpointResponse405 | PatchServicesDNSResolverAccessListEndpointResponse406 | PatchServicesDNSResolverAccessListEndpointResponse409 | PatchServicesDNSResolverAccessListEndpointResponse415 | PatchServicesDNSResolverAccessListEndpointResponse422 | PatchServicesDNSResolverAccessListEndpointResponse424 | PatchServicesDNSResolverAccessListEndpointResponse500 | PatchServicesDNSResolverAccessListEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverAccessListEndpointJsonBody
    | PatchServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSResolverAccessListEndpointResponse400
    | PatchServicesDNSResolverAccessListEndpointResponse401
    | PatchServicesDNSResolverAccessListEndpointResponse403
    | PatchServicesDNSResolverAccessListEndpointResponse404
    | PatchServicesDNSResolverAccessListEndpointResponse405
    | PatchServicesDNSResolverAccessListEndpointResponse406
    | PatchServicesDNSResolverAccessListEndpointResponse409
    | PatchServicesDNSResolverAccessListEndpointResponse415
    | PatchServicesDNSResolverAccessListEndpointResponse422
    | PatchServicesDNSResolverAccessListEndpointResponse424
    | PatchServicesDNSResolverAccessListEndpointResponse500
    | PatchServicesDNSResolverAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSResolverAccessListEndpointResponse400 | PatchServicesDNSResolverAccessListEndpointResponse401 | PatchServicesDNSResolverAccessListEndpointResponse403 | PatchServicesDNSResolverAccessListEndpointResponse404 | PatchServicesDNSResolverAccessListEndpointResponse405 | PatchServicesDNSResolverAccessListEndpointResponse406 | PatchServicesDNSResolverAccessListEndpointResponse409 | PatchServicesDNSResolverAccessListEndpointResponse415 | PatchServicesDNSResolverAccessListEndpointResponse422 | PatchServicesDNSResolverAccessListEndpointResponse424 | PatchServicesDNSResolverAccessListEndpointResponse500 | PatchServicesDNSResolverAccessListEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSResolverAccessListEndpointJsonBody
    | PatchServicesDNSResolverAccessListEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSResolverAccessListEndpointResponse400
    | PatchServicesDNSResolverAccessListEndpointResponse401
    | PatchServicesDNSResolverAccessListEndpointResponse403
    | PatchServicesDNSResolverAccessListEndpointResponse404
    | PatchServicesDNSResolverAccessListEndpointResponse405
    | PatchServicesDNSResolverAccessListEndpointResponse406
    | PatchServicesDNSResolverAccessListEndpointResponse409
    | PatchServicesDNSResolverAccessListEndpointResponse415
    | PatchServicesDNSResolverAccessListEndpointResponse422
    | PatchServicesDNSResolverAccessListEndpointResponse424
    | PatchServicesDNSResolverAccessListEndpointResponse500
    | PatchServicesDNSResolverAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Resolver Access List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-list-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDNSResolverAccessListEndpointJsonBody | Unset):
        body (PatchServicesDNSResolverAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSResolverAccessListEndpointResponse400 | PatchServicesDNSResolverAccessListEndpointResponse401 | PatchServicesDNSResolverAccessListEndpointResponse403 | PatchServicesDNSResolverAccessListEndpointResponse404 | PatchServicesDNSResolverAccessListEndpointResponse405 | PatchServicesDNSResolverAccessListEndpointResponse406 | PatchServicesDNSResolverAccessListEndpointResponse409 | PatchServicesDNSResolverAccessListEndpointResponse415 | PatchServicesDNSResolverAccessListEndpointResponse422 | PatchServicesDNSResolverAccessListEndpointResponse424 | PatchServicesDNSResolverAccessListEndpointResponse500 | PatchServicesDNSResolverAccessListEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
