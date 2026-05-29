from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_dns_resolver_access_lists_endpoint_data_body_item import (
    PutServicesDNSResolverAccessListsEndpointDataBodyItem,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_json_body_item import (
    PutServicesDNSResolverAccessListsEndpointJsonBodyItem,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_400 import (
    PutServicesDNSResolverAccessListsEndpointResponse400,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_401 import (
    PutServicesDNSResolverAccessListsEndpointResponse401,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_403 import (
    PutServicesDNSResolverAccessListsEndpointResponse403,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_404 import (
    PutServicesDNSResolverAccessListsEndpointResponse404,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_405 import (
    PutServicesDNSResolverAccessListsEndpointResponse405,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_406 import (
    PutServicesDNSResolverAccessListsEndpointResponse406,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_409 import (
    PutServicesDNSResolverAccessListsEndpointResponse409,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_415 import (
    PutServicesDNSResolverAccessListsEndpointResponse415,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_422 import (
    PutServicesDNSResolverAccessListsEndpointResponse422,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_424 import (
    PutServicesDNSResolverAccessListsEndpointResponse424,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_500 import (
    PutServicesDNSResolverAccessListsEndpointResponse500,
)
from ...models.put_services_dns_resolver_access_lists_endpoint_response_503 import (
    PutServicesDNSResolverAccessListsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem]
    | list[PutServicesDNSResolverAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/dns_resolver/access_lists",
    }

    if isinstance(body, list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesDNSResolverAccessListsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesDNSResolverAccessListsEndpointResponse400
    | PutServicesDNSResolverAccessListsEndpointResponse401
    | PutServicesDNSResolverAccessListsEndpointResponse403
    | PutServicesDNSResolverAccessListsEndpointResponse404
    | PutServicesDNSResolverAccessListsEndpointResponse405
    | PutServicesDNSResolverAccessListsEndpointResponse406
    | PutServicesDNSResolverAccessListsEndpointResponse409
    | PutServicesDNSResolverAccessListsEndpointResponse415
    | PutServicesDNSResolverAccessListsEndpointResponse422
    | PutServicesDNSResolverAccessListsEndpointResponse424
    | PutServicesDNSResolverAccessListsEndpointResponse500
    | PutServicesDNSResolverAccessListsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesDNSResolverAccessListsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesDNSResolverAccessListsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesDNSResolverAccessListsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesDNSResolverAccessListsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesDNSResolverAccessListsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesDNSResolverAccessListsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesDNSResolverAccessListsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesDNSResolverAccessListsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesDNSResolverAccessListsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesDNSResolverAccessListsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesDNSResolverAccessListsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesDNSResolverAccessListsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesDNSResolverAccessListsEndpointResponse400
    | PutServicesDNSResolverAccessListsEndpointResponse401
    | PutServicesDNSResolverAccessListsEndpointResponse403
    | PutServicesDNSResolverAccessListsEndpointResponse404
    | PutServicesDNSResolverAccessListsEndpointResponse405
    | PutServicesDNSResolverAccessListsEndpointResponse406
    | PutServicesDNSResolverAccessListsEndpointResponse409
    | PutServicesDNSResolverAccessListsEndpointResponse415
    | PutServicesDNSResolverAccessListsEndpointResponse422
    | PutServicesDNSResolverAccessListsEndpointResponse424
    | PutServicesDNSResolverAccessListsEndpointResponse500
    | PutServicesDNSResolverAccessListsEndpointResponse503
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
    body: list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem]
    | list[PutServicesDNSResolverAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesDNSResolverAccessListsEndpointResponse400
    | PutServicesDNSResolverAccessListsEndpointResponse401
    | PutServicesDNSResolverAccessListsEndpointResponse403
    | PutServicesDNSResolverAccessListsEndpointResponse404
    | PutServicesDNSResolverAccessListsEndpointResponse405
    | PutServicesDNSResolverAccessListsEndpointResponse406
    | PutServicesDNSResolverAccessListsEndpointResponse409
    | PutServicesDNSResolverAccessListsEndpointResponse415
    | PutServicesDNSResolverAccessListsEndpointResponse422
    | PutServicesDNSResolverAccessListsEndpointResponse424
    | PutServicesDNSResolverAccessListsEndpointResponse500
    | PutServicesDNSResolverAccessListsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing DNS Resolver Access Lists.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-lists-
    put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesDNSResolverAccessListsEndpointResponse400 | PutServicesDNSResolverAccessListsEndpointResponse401 | PutServicesDNSResolverAccessListsEndpointResponse403 | PutServicesDNSResolverAccessListsEndpointResponse404 | PutServicesDNSResolverAccessListsEndpointResponse405 | PutServicesDNSResolverAccessListsEndpointResponse406 | PutServicesDNSResolverAccessListsEndpointResponse409 | PutServicesDNSResolverAccessListsEndpointResponse415 | PutServicesDNSResolverAccessListsEndpointResponse422 | PutServicesDNSResolverAccessListsEndpointResponse424 | PutServicesDNSResolverAccessListsEndpointResponse500 | PutServicesDNSResolverAccessListsEndpointResponse503]
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
    body: list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem]
    | list[PutServicesDNSResolverAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesDNSResolverAccessListsEndpointResponse400
    | PutServicesDNSResolverAccessListsEndpointResponse401
    | PutServicesDNSResolverAccessListsEndpointResponse403
    | PutServicesDNSResolverAccessListsEndpointResponse404
    | PutServicesDNSResolverAccessListsEndpointResponse405
    | PutServicesDNSResolverAccessListsEndpointResponse406
    | PutServicesDNSResolverAccessListsEndpointResponse409
    | PutServicesDNSResolverAccessListsEndpointResponse415
    | PutServicesDNSResolverAccessListsEndpointResponse422
    | PutServicesDNSResolverAccessListsEndpointResponse424
    | PutServicesDNSResolverAccessListsEndpointResponse500
    | PutServicesDNSResolverAccessListsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing DNS Resolver Access Lists.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-lists-
    put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesDNSResolverAccessListsEndpointResponse400 | PutServicesDNSResolverAccessListsEndpointResponse401 | PutServicesDNSResolverAccessListsEndpointResponse403 | PutServicesDNSResolverAccessListsEndpointResponse404 | PutServicesDNSResolverAccessListsEndpointResponse405 | PutServicesDNSResolverAccessListsEndpointResponse406 | PutServicesDNSResolverAccessListsEndpointResponse409 | PutServicesDNSResolverAccessListsEndpointResponse415 | PutServicesDNSResolverAccessListsEndpointResponse422 | PutServicesDNSResolverAccessListsEndpointResponse424 | PutServicesDNSResolverAccessListsEndpointResponse500 | PutServicesDNSResolverAccessListsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem]
    | list[PutServicesDNSResolverAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesDNSResolverAccessListsEndpointResponse400
    | PutServicesDNSResolverAccessListsEndpointResponse401
    | PutServicesDNSResolverAccessListsEndpointResponse403
    | PutServicesDNSResolverAccessListsEndpointResponse404
    | PutServicesDNSResolverAccessListsEndpointResponse405
    | PutServicesDNSResolverAccessListsEndpointResponse406
    | PutServicesDNSResolverAccessListsEndpointResponse409
    | PutServicesDNSResolverAccessListsEndpointResponse415
    | PutServicesDNSResolverAccessListsEndpointResponse422
    | PutServicesDNSResolverAccessListsEndpointResponse424
    | PutServicesDNSResolverAccessListsEndpointResponse500
    | PutServicesDNSResolverAccessListsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing DNS Resolver Access Lists.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-lists-
    put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesDNSResolverAccessListsEndpointResponse400 | PutServicesDNSResolverAccessListsEndpointResponse401 | PutServicesDNSResolverAccessListsEndpointResponse403 | PutServicesDNSResolverAccessListsEndpointResponse404 | PutServicesDNSResolverAccessListsEndpointResponse405 | PutServicesDNSResolverAccessListsEndpointResponse406 | PutServicesDNSResolverAccessListsEndpointResponse409 | PutServicesDNSResolverAccessListsEndpointResponse415 | PutServicesDNSResolverAccessListsEndpointResponse422 | PutServicesDNSResolverAccessListsEndpointResponse424 | PutServicesDNSResolverAccessListsEndpointResponse500 | PutServicesDNSResolverAccessListsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem]
    | list[PutServicesDNSResolverAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesDNSResolverAccessListsEndpointResponse400
    | PutServicesDNSResolverAccessListsEndpointResponse401
    | PutServicesDNSResolverAccessListsEndpointResponse403
    | PutServicesDNSResolverAccessListsEndpointResponse404
    | PutServicesDNSResolverAccessListsEndpointResponse405
    | PutServicesDNSResolverAccessListsEndpointResponse406
    | PutServicesDNSResolverAccessListsEndpointResponse409
    | PutServicesDNSResolverAccessListsEndpointResponse415
    | PutServicesDNSResolverAccessListsEndpointResponse422
    | PutServicesDNSResolverAccessListsEndpointResponse424
    | PutServicesDNSResolverAccessListsEndpointResponse500
    | PutServicesDNSResolverAccessListsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing DNS Resolver Access Lists.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: DNSResolverAccessList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-resolver-access-lists-
    put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesDNSResolverAccessListsEndpointResponse400 | PutServicesDNSResolverAccessListsEndpointResponse401 | PutServicesDNSResolverAccessListsEndpointResponse403 | PutServicesDNSResolverAccessListsEndpointResponse404 | PutServicesDNSResolverAccessListsEndpointResponse405 | PutServicesDNSResolverAccessListsEndpointResponse406 | PutServicesDNSResolverAccessListsEndpointResponse409 | PutServicesDNSResolverAccessListsEndpointResponse415 | PutServicesDNSResolverAccessListsEndpointResponse422 | PutServicesDNSResolverAccessListsEndpointResponse424 | PutServicesDNSResolverAccessListsEndpointResponse500 | PutServicesDNSResolverAccessListsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
