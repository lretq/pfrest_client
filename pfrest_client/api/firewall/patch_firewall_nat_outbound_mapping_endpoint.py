from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_nat_outbound_mapping_endpoint_data_body import (
    PatchFirewallNATOutboundMappingEndpointDataBody,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_json_body import (
    PatchFirewallNATOutboundMappingEndpointJsonBody,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_400 import (
    PatchFirewallNATOutboundMappingEndpointResponse400,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_401 import (
    PatchFirewallNATOutboundMappingEndpointResponse401,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_403 import (
    PatchFirewallNATOutboundMappingEndpointResponse403,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_404 import (
    PatchFirewallNATOutboundMappingEndpointResponse404,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_405 import (
    PatchFirewallNATOutboundMappingEndpointResponse405,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_406 import (
    PatchFirewallNATOutboundMappingEndpointResponse406,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_409 import (
    PatchFirewallNATOutboundMappingEndpointResponse409,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_415 import (
    PatchFirewallNATOutboundMappingEndpointResponse415,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_422 import (
    PatchFirewallNATOutboundMappingEndpointResponse422,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_424 import (
    PatchFirewallNATOutboundMappingEndpointResponse424,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_500 import (
    PatchFirewallNATOutboundMappingEndpointResponse500,
)
from ...models.patch_firewall_nat_outbound_mapping_endpoint_response_503 import (
    PatchFirewallNATOutboundMappingEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallNATOutboundMappingEndpointJsonBody
    | PatchFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/nat/outbound/mapping",
    }

    if isinstance(body, PatchFirewallNATOutboundMappingEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallNATOutboundMappingEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallNATOutboundMappingEndpointResponse400
    | PatchFirewallNATOutboundMappingEndpointResponse401
    | PatchFirewallNATOutboundMappingEndpointResponse403
    | PatchFirewallNATOutboundMappingEndpointResponse404
    | PatchFirewallNATOutboundMappingEndpointResponse405
    | PatchFirewallNATOutboundMappingEndpointResponse406
    | PatchFirewallNATOutboundMappingEndpointResponse409
    | PatchFirewallNATOutboundMappingEndpointResponse415
    | PatchFirewallNATOutboundMappingEndpointResponse422
    | PatchFirewallNATOutboundMappingEndpointResponse424
    | PatchFirewallNATOutboundMappingEndpointResponse500
    | PatchFirewallNATOutboundMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallNATOutboundMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallNATOutboundMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallNATOutboundMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallNATOutboundMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallNATOutboundMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallNATOutboundMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallNATOutboundMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallNATOutboundMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallNATOutboundMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallNATOutboundMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallNATOutboundMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallNATOutboundMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallNATOutboundMappingEndpointResponse400
    | PatchFirewallNATOutboundMappingEndpointResponse401
    | PatchFirewallNATOutboundMappingEndpointResponse403
    | PatchFirewallNATOutboundMappingEndpointResponse404
    | PatchFirewallNATOutboundMappingEndpointResponse405
    | PatchFirewallNATOutboundMappingEndpointResponse406
    | PatchFirewallNATOutboundMappingEndpointResponse409
    | PatchFirewallNATOutboundMappingEndpointResponse415
    | PatchFirewallNATOutboundMappingEndpointResponse422
    | PatchFirewallNATOutboundMappingEndpointResponse424
    | PatchFirewallNATOutboundMappingEndpointResponse500
    | PatchFirewallNATOutboundMappingEndpointResponse503
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
    body: PatchFirewallNATOutboundMappingEndpointJsonBody
    | PatchFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallNATOutboundMappingEndpointResponse400
    | PatchFirewallNATOutboundMappingEndpointResponse401
    | PatchFirewallNATOutboundMappingEndpointResponse403
    | PatchFirewallNATOutboundMappingEndpointResponse404
    | PatchFirewallNATOutboundMappingEndpointResponse405
    | PatchFirewallNATOutboundMappingEndpointResponse406
    | PatchFirewallNATOutboundMappingEndpointResponse409
    | PatchFirewallNATOutboundMappingEndpointResponse415
    | PatchFirewallNATOutboundMappingEndpointResponse422
    | PatchFirewallNATOutboundMappingEndpointResponse424
    | PatchFirewallNATOutboundMappingEndpointResponse500
    | PatchFirewallNATOutboundMappingEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallNATOutboundMappingEndpointResponse400 | PatchFirewallNATOutboundMappingEndpointResponse401 | PatchFirewallNATOutboundMappingEndpointResponse403 | PatchFirewallNATOutboundMappingEndpointResponse404 | PatchFirewallNATOutboundMappingEndpointResponse405 | PatchFirewallNATOutboundMappingEndpointResponse406 | PatchFirewallNATOutboundMappingEndpointResponse409 | PatchFirewallNATOutboundMappingEndpointResponse415 | PatchFirewallNATOutboundMappingEndpointResponse422 | PatchFirewallNATOutboundMappingEndpointResponse424 | PatchFirewallNATOutboundMappingEndpointResponse500 | PatchFirewallNATOutboundMappingEndpointResponse503]
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
    body: PatchFirewallNATOutboundMappingEndpointJsonBody
    | PatchFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallNATOutboundMappingEndpointResponse400
    | PatchFirewallNATOutboundMappingEndpointResponse401
    | PatchFirewallNATOutboundMappingEndpointResponse403
    | PatchFirewallNATOutboundMappingEndpointResponse404
    | PatchFirewallNATOutboundMappingEndpointResponse405
    | PatchFirewallNATOutboundMappingEndpointResponse406
    | PatchFirewallNATOutboundMappingEndpointResponse409
    | PatchFirewallNATOutboundMappingEndpointResponse415
    | PatchFirewallNATOutboundMappingEndpointResponse422
    | PatchFirewallNATOutboundMappingEndpointResponse424
    | PatchFirewallNATOutboundMappingEndpointResponse500
    | PatchFirewallNATOutboundMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallNATOutboundMappingEndpointResponse400 | PatchFirewallNATOutboundMappingEndpointResponse401 | PatchFirewallNATOutboundMappingEndpointResponse403 | PatchFirewallNATOutboundMappingEndpointResponse404 | PatchFirewallNATOutboundMappingEndpointResponse405 | PatchFirewallNATOutboundMappingEndpointResponse406 | PatchFirewallNATOutboundMappingEndpointResponse409 | PatchFirewallNATOutboundMappingEndpointResponse415 | PatchFirewallNATOutboundMappingEndpointResponse422 | PatchFirewallNATOutboundMappingEndpointResponse424 | PatchFirewallNATOutboundMappingEndpointResponse500 | PatchFirewallNATOutboundMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallNATOutboundMappingEndpointJsonBody
    | PatchFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallNATOutboundMappingEndpointResponse400
    | PatchFirewallNATOutboundMappingEndpointResponse401
    | PatchFirewallNATOutboundMappingEndpointResponse403
    | PatchFirewallNATOutboundMappingEndpointResponse404
    | PatchFirewallNATOutboundMappingEndpointResponse405
    | PatchFirewallNATOutboundMappingEndpointResponse406
    | PatchFirewallNATOutboundMappingEndpointResponse409
    | PatchFirewallNATOutboundMappingEndpointResponse415
    | PatchFirewallNATOutboundMappingEndpointResponse422
    | PatchFirewallNATOutboundMappingEndpointResponse424
    | PatchFirewallNATOutboundMappingEndpointResponse500
    | PatchFirewallNATOutboundMappingEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallNATOutboundMappingEndpointResponse400 | PatchFirewallNATOutboundMappingEndpointResponse401 | PatchFirewallNATOutboundMappingEndpointResponse403 | PatchFirewallNATOutboundMappingEndpointResponse404 | PatchFirewallNATOutboundMappingEndpointResponse405 | PatchFirewallNATOutboundMappingEndpointResponse406 | PatchFirewallNATOutboundMappingEndpointResponse409 | PatchFirewallNATOutboundMappingEndpointResponse415 | PatchFirewallNATOutboundMappingEndpointResponse422 | PatchFirewallNATOutboundMappingEndpointResponse424 | PatchFirewallNATOutboundMappingEndpointResponse500 | PatchFirewallNATOutboundMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallNATOutboundMappingEndpointJsonBody
    | PatchFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallNATOutboundMappingEndpointResponse400
    | PatchFirewallNATOutboundMappingEndpointResponse401
    | PatchFirewallNATOutboundMappingEndpointResponse403
    | PatchFirewallNATOutboundMappingEndpointResponse404
    | PatchFirewallNATOutboundMappingEndpointResponse405
    | PatchFirewallNATOutboundMappingEndpointResponse406
    | PatchFirewallNATOutboundMappingEndpointResponse409
    | PatchFirewallNATOutboundMappingEndpointResponse415
    | PatchFirewallNATOutboundMappingEndpointResponse422
    | PatchFirewallNATOutboundMappingEndpointResponse424
    | PatchFirewallNATOutboundMappingEndpointResponse500
    | PatchFirewallNATOutboundMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallNATOutboundMappingEndpointResponse400 | PatchFirewallNATOutboundMappingEndpointResponse401 | PatchFirewallNATOutboundMappingEndpointResponse403 | PatchFirewallNATOutboundMappingEndpointResponse404 | PatchFirewallNATOutboundMappingEndpointResponse405 | PatchFirewallNATOutboundMappingEndpointResponse406 | PatchFirewallNATOutboundMappingEndpointResponse409 | PatchFirewallNATOutboundMappingEndpointResponse415 | PatchFirewallNATOutboundMappingEndpointResponse422 | PatchFirewallNATOutboundMappingEndpointResponse424 | PatchFirewallNATOutboundMappingEndpointResponse500 | PatchFirewallNATOutboundMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
