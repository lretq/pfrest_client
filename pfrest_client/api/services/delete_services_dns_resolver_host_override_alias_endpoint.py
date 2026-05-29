from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_400 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_401 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_403 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_404 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_405 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_406 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_409 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_415 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_422 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_424 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_500 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500,
)
from ...models.delete_services_dns_resolver_host_override_alias_endpoint_response_503 import (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/dns_resolver/host_override/alias",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
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
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverHostOverrideAlias<br>**Parent model**: DNSResolverHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-override-alias-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
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
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverHostOverrideAlias<br>**Parent model**: DNSResolverHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-override-alias-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverHostOverrideAlias<br>**Parent model**: DNSResolverHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-override-alias-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500
    | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DNS Resolver Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSResolverHostOverrideAlias<br>**Parent model**: DNSResolverHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-host-override-alias-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSResolverHostOverrideAliasEndpointResponse400 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse401 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse403 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse404 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse405 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse406 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse409 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse415 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse422 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse424 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse500 | DeleteServicesDNSResolverHostOverrideAliasEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
            apply=apply,
        )
    ).parsed
