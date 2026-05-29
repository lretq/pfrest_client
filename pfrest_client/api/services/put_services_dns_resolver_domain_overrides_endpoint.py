from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_dns_resolver_domain_overrides_endpoint_data_body_item import (
    PutServicesDNSResolverDomainOverridesEndpointDataBodyItem,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_json_body_item import (
    PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_400 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse400,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_401 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse401,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_403 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse403,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_404 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse404,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_405 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse405,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_406 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse406,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_409 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse409,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_415 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse415,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_422 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse422,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_424 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse424,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_500 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse500,
)
from ...models.put_services_dns_resolver_domain_overrides_endpoint_response_503 import (
    PutServicesDNSResolverDomainOverridesEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/dns_resolver/domain_overrides",
    }

    if isinstance(body, list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesDNSResolverDomainOverridesEndpointResponse400
    | PutServicesDNSResolverDomainOverridesEndpointResponse401
    | PutServicesDNSResolverDomainOverridesEndpointResponse403
    | PutServicesDNSResolverDomainOverridesEndpointResponse404
    | PutServicesDNSResolverDomainOverridesEndpointResponse405
    | PutServicesDNSResolverDomainOverridesEndpointResponse406
    | PutServicesDNSResolverDomainOverridesEndpointResponse409
    | PutServicesDNSResolverDomainOverridesEndpointResponse415
    | PutServicesDNSResolverDomainOverridesEndpointResponse422
    | PutServicesDNSResolverDomainOverridesEndpointResponse424
    | PutServicesDNSResolverDomainOverridesEndpointResponse500
    | PutServicesDNSResolverDomainOverridesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesDNSResolverDomainOverridesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesDNSResolverDomainOverridesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesDNSResolverDomainOverridesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesDNSResolverDomainOverridesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesDNSResolverDomainOverridesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesDNSResolverDomainOverridesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesDNSResolverDomainOverridesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesDNSResolverDomainOverridesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesDNSResolverDomainOverridesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesDNSResolverDomainOverridesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesDNSResolverDomainOverridesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesDNSResolverDomainOverridesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesDNSResolverDomainOverridesEndpointResponse400
    | PutServicesDNSResolverDomainOverridesEndpointResponse401
    | PutServicesDNSResolverDomainOverridesEndpointResponse403
    | PutServicesDNSResolverDomainOverridesEndpointResponse404
    | PutServicesDNSResolverDomainOverridesEndpointResponse405
    | PutServicesDNSResolverDomainOverridesEndpointResponse406
    | PutServicesDNSResolverDomainOverridesEndpointResponse409
    | PutServicesDNSResolverDomainOverridesEndpointResponse415
    | PutServicesDNSResolverDomainOverridesEndpointResponse422
    | PutServicesDNSResolverDomainOverridesEndpointResponse424
    | PutServicesDNSResolverDomainOverridesEndpointResponse500
    | PutServicesDNSResolverDomainOverridesEndpointResponse503
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
    body: list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesDNSResolverDomainOverridesEndpointResponse400
    | PutServicesDNSResolverDomainOverridesEndpointResponse401
    | PutServicesDNSResolverDomainOverridesEndpointResponse403
    | PutServicesDNSResolverDomainOverridesEndpointResponse404
    | PutServicesDNSResolverDomainOverridesEndpointResponse405
    | PutServicesDNSResolverDomainOverridesEndpointResponse406
    | PutServicesDNSResolverDomainOverridesEndpointResponse409
    | PutServicesDNSResolverDomainOverridesEndpointResponse415
    | PutServicesDNSResolverDomainOverridesEndpointResponse422
    | PutServicesDNSResolverDomainOverridesEndpointResponse424
    | PutServicesDNSResolverDomainOverridesEndpointResponse500
    | PutServicesDNSResolverDomainOverridesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing DNS Resolver Domain
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesDNSResolverDomainOverridesEndpointResponse400 | PutServicesDNSResolverDomainOverridesEndpointResponse401 | PutServicesDNSResolverDomainOverridesEndpointResponse403 | PutServicesDNSResolverDomainOverridesEndpointResponse404 | PutServicesDNSResolverDomainOverridesEndpointResponse405 | PutServicesDNSResolverDomainOverridesEndpointResponse406 | PutServicesDNSResolverDomainOverridesEndpointResponse409 | PutServicesDNSResolverDomainOverridesEndpointResponse415 | PutServicesDNSResolverDomainOverridesEndpointResponse422 | PutServicesDNSResolverDomainOverridesEndpointResponse424 | PutServicesDNSResolverDomainOverridesEndpointResponse500 | PutServicesDNSResolverDomainOverridesEndpointResponse503]
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
    body: list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesDNSResolverDomainOverridesEndpointResponse400
    | PutServicesDNSResolverDomainOverridesEndpointResponse401
    | PutServicesDNSResolverDomainOverridesEndpointResponse403
    | PutServicesDNSResolverDomainOverridesEndpointResponse404
    | PutServicesDNSResolverDomainOverridesEndpointResponse405
    | PutServicesDNSResolverDomainOverridesEndpointResponse406
    | PutServicesDNSResolverDomainOverridesEndpointResponse409
    | PutServicesDNSResolverDomainOverridesEndpointResponse415
    | PutServicesDNSResolverDomainOverridesEndpointResponse422
    | PutServicesDNSResolverDomainOverridesEndpointResponse424
    | PutServicesDNSResolverDomainOverridesEndpointResponse500
    | PutServicesDNSResolverDomainOverridesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing DNS Resolver Domain
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesDNSResolverDomainOverridesEndpointResponse400 | PutServicesDNSResolverDomainOverridesEndpointResponse401 | PutServicesDNSResolverDomainOverridesEndpointResponse403 | PutServicesDNSResolverDomainOverridesEndpointResponse404 | PutServicesDNSResolverDomainOverridesEndpointResponse405 | PutServicesDNSResolverDomainOverridesEndpointResponse406 | PutServicesDNSResolverDomainOverridesEndpointResponse409 | PutServicesDNSResolverDomainOverridesEndpointResponse415 | PutServicesDNSResolverDomainOverridesEndpointResponse422 | PutServicesDNSResolverDomainOverridesEndpointResponse424 | PutServicesDNSResolverDomainOverridesEndpointResponse500 | PutServicesDNSResolverDomainOverridesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesDNSResolverDomainOverridesEndpointResponse400
    | PutServicesDNSResolverDomainOverridesEndpointResponse401
    | PutServicesDNSResolverDomainOverridesEndpointResponse403
    | PutServicesDNSResolverDomainOverridesEndpointResponse404
    | PutServicesDNSResolverDomainOverridesEndpointResponse405
    | PutServicesDNSResolverDomainOverridesEndpointResponse406
    | PutServicesDNSResolverDomainOverridesEndpointResponse409
    | PutServicesDNSResolverDomainOverridesEndpointResponse415
    | PutServicesDNSResolverDomainOverridesEndpointResponse422
    | PutServicesDNSResolverDomainOverridesEndpointResponse424
    | PutServicesDNSResolverDomainOverridesEndpointResponse500
    | PutServicesDNSResolverDomainOverridesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing DNS Resolver Domain
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesDNSResolverDomainOverridesEndpointResponse400 | PutServicesDNSResolverDomainOverridesEndpointResponse401 | PutServicesDNSResolverDomainOverridesEndpointResponse403 | PutServicesDNSResolverDomainOverridesEndpointResponse404 | PutServicesDNSResolverDomainOverridesEndpointResponse405 | PutServicesDNSResolverDomainOverridesEndpointResponse406 | PutServicesDNSResolverDomainOverridesEndpointResponse409 | PutServicesDNSResolverDomainOverridesEndpointResponse415 | PutServicesDNSResolverDomainOverridesEndpointResponse422 | PutServicesDNSResolverDomainOverridesEndpointResponse424 | PutServicesDNSResolverDomainOverridesEndpointResponse500 | PutServicesDNSResolverDomainOverridesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesDNSResolverDomainOverridesEndpointResponse400
    | PutServicesDNSResolverDomainOverridesEndpointResponse401
    | PutServicesDNSResolverDomainOverridesEndpointResponse403
    | PutServicesDNSResolverDomainOverridesEndpointResponse404
    | PutServicesDNSResolverDomainOverridesEndpointResponse405
    | PutServicesDNSResolverDomainOverridesEndpointResponse406
    | PutServicesDNSResolverDomainOverridesEndpointResponse409
    | PutServicesDNSResolverDomainOverridesEndpointResponse415
    | PutServicesDNSResolverDomainOverridesEndpointResponse422
    | PutServicesDNSResolverDomainOverridesEndpointResponse424
    | PutServicesDNSResolverDomainOverridesEndpointResponse500
    | PutServicesDNSResolverDomainOverridesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing DNS Resolver Domain
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSResolverDomainOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-resolver-domain-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSResolverDomainOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSResolverDomainOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesDNSResolverDomainOverridesEndpointResponse400 | PutServicesDNSResolverDomainOverridesEndpointResponse401 | PutServicesDNSResolverDomainOverridesEndpointResponse403 | PutServicesDNSResolverDomainOverridesEndpointResponse404 | PutServicesDNSResolverDomainOverridesEndpointResponse405 | PutServicesDNSResolverDomainOverridesEndpointResponse406 | PutServicesDNSResolverDomainOverridesEndpointResponse409 | PutServicesDNSResolverDomainOverridesEndpointResponse415 | PutServicesDNSResolverDomainOverridesEndpointResponse422 | PutServicesDNSResolverDomainOverridesEndpointResponse424 | PutServicesDNSResolverDomainOverridesEndpointResponse500 | PutServicesDNSResolverDomainOverridesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
