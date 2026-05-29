from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dns_resolver_host_override_endpoint_response_400 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse400,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_401 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse401,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_403 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse403,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_404 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse404,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_405 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse405,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_406 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse406,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_409 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse409,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_415 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse415,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_422 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse422,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_424 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse424,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_500 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse500,
)
from ...models.delete_services_dns_resolver_host_override_endpoint_response_503 import (
    DeleteServicesDNSResolverHostOverrideEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/dns_resolver/host_override",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDNSResolverHostOverrideEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDNSResolverHostOverrideEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDNSResolverHostOverrideEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDNSResolverHostOverrideEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDNSResolverHostOverrideEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDNSResolverHostOverrideEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDNSResolverHostOverrideEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDNSResolverHostOverrideEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDNSResolverHostOverrideEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDNSResolverHostOverrideEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDNSResolverHostOverrideEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDNSResolverHostOverrideEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDNSResolverHostOverrideEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDNSResolverHostOverrideEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideEndpointResponse503
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
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDNSResolverHostOverrideEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSResolverHostOverrideEndpointResponse400 | DeleteServicesDNSResolverHostOverrideEndpointResponse401 | DeleteServicesDNSResolverHostOverrideEndpointResponse403 | DeleteServicesDNSResolverHostOverrideEndpointResponse404 | DeleteServicesDNSResolverHostOverrideEndpointResponse405 | DeleteServicesDNSResolverHostOverrideEndpointResponse406 | DeleteServicesDNSResolverHostOverrideEndpointResponse409 | DeleteServicesDNSResolverHostOverrideEndpointResponse415 | DeleteServicesDNSResolverHostOverrideEndpointResponse422 | DeleteServicesDNSResolverHostOverrideEndpointResponse424 | DeleteServicesDNSResolverHostOverrideEndpointResponse500 | DeleteServicesDNSResolverHostOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDNSResolverHostOverrideEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSResolverHostOverrideEndpointResponse400 | DeleteServicesDNSResolverHostOverrideEndpointResponse401 | DeleteServicesDNSResolverHostOverrideEndpointResponse403 | DeleteServicesDNSResolverHostOverrideEndpointResponse404 | DeleteServicesDNSResolverHostOverrideEndpointResponse405 | DeleteServicesDNSResolverHostOverrideEndpointResponse406 | DeleteServicesDNSResolverHostOverrideEndpointResponse409 | DeleteServicesDNSResolverHostOverrideEndpointResponse415 | DeleteServicesDNSResolverHostOverrideEndpointResponse422 | DeleteServicesDNSResolverHostOverrideEndpointResponse424 | DeleteServicesDNSResolverHostOverrideEndpointResponse500 | DeleteServicesDNSResolverHostOverrideEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDNSResolverHostOverrideEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSResolverHostOverrideEndpointResponse400 | DeleteServicesDNSResolverHostOverrideEndpointResponse401 | DeleteServicesDNSResolverHostOverrideEndpointResponse403 | DeleteServicesDNSResolverHostOverrideEndpointResponse404 | DeleteServicesDNSResolverHostOverrideEndpointResponse405 | DeleteServicesDNSResolverHostOverrideEndpointResponse406 | DeleteServicesDNSResolverHostOverrideEndpointResponse409 | DeleteServicesDNSResolverHostOverrideEndpointResponse415 | DeleteServicesDNSResolverHostOverrideEndpointResponse422 | DeleteServicesDNSResolverHostOverrideEndpointResponse424 | DeleteServicesDNSResolverHostOverrideEndpointResponse500 | DeleteServicesDNSResolverHostOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDNSResolverHostOverrideEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSResolverHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSResolverHostOverrideEndpointResponse400 | DeleteServicesDNSResolverHostOverrideEndpointResponse401 | DeleteServicesDNSResolverHostOverrideEndpointResponse403 | DeleteServicesDNSResolverHostOverrideEndpointResponse404 | DeleteServicesDNSResolverHostOverrideEndpointResponse405 | DeleteServicesDNSResolverHostOverrideEndpointResponse406 | DeleteServicesDNSResolverHostOverrideEndpointResponse409 | DeleteServicesDNSResolverHostOverrideEndpointResponse415 | DeleteServicesDNSResolverHostOverrideEndpointResponse422 | DeleteServicesDNSResolverHostOverrideEndpointResponse424 | DeleteServicesDNSResolverHostOverrideEndpointResponse500 | DeleteServicesDNSResolverHostOverrideEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            apply=apply,
        )
    ).parsed
