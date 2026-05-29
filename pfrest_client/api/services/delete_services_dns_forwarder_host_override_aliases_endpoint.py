from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_query import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_400 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_401 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_403 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_404 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_405 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_406 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_409 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_415 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_422 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_424 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_500 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500,
)
from ...models.delete_services_dns_forwarder_host_override_aliases_endpoint_response_503 import (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/dns_forwarder/host_override/aliases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
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
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing DNS Forwarder Host Override Aliases using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-aliases-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset = UNSET,
) -> (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing DNS Forwarder Host Override Aliases using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-aliases-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing DNS Forwarder Host Override Aliases using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-aliases-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset = UNSET,
) -> (
    DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing DNS Forwarder Host Override Aliases using a
    query.<br><br>WARNING: This will delete all objects that match the query, use with
    caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-aliases-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesDNSForwarderHostOverrideAliasesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideAliasesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
