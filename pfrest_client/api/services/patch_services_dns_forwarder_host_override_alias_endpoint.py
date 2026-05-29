from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_data_body import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_json_body import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_400 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_401 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_403 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_404 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_405 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_406 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_409 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_415 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_422 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_424 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_500 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500,
)
from ...models.patch_services_dns_forwarder_host_override_alias_endpoint_response_503 import (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody
    | PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dns_forwarder/host_override/alias",
    }

    if isinstance(body, PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
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
    body: PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody
    | PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Forwarder Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-alias-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody | Unset):
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503]
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
    body: PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody
    | PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Forwarder Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-alias-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody | Unset):
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody
    | PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DNS Forwarder Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-alias-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody | Unset):
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody
    | PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500
    | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DNS Forwarder Host Override
    Alias.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    DNSForwarderHostOverrideAlias<br>**Parent model**: DNSForwarderHostOverride<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-override-alias-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointJsonBody | Unset):
        body (PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDNSForwarderHostOverrideAliasEndpointResponse400 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse401 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse403 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse404 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse405 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse406 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse409 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse415 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse422 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse424 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse500 | PatchServicesDNSForwarderHostOverrideAliasEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
