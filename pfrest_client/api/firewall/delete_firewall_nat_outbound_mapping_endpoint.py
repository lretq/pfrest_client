from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_400 import (
    DeleteFirewallNATOutboundMappingEndpointResponse400,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_401 import (
    DeleteFirewallNATOutboundMappingEndpointResponse401,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_403 import (
    DeleteFirewallNATOutboundMappingEndpointResponse403,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_404 import (
    DeleteFirewallNATOutboundMappingEndpointResponse404,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_405 import (
    DeleteFirewallNATOutboundMappingEndpointResponse405,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_406 import (
    DeleteFirewallNATOutboundMappingEndpointResponse406,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_409 import (
    DeleteFirewallNATOutboundMappingEndpointResponse409,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_415 import (
    DeleteFirewallNATOutboundMappingEndpointResponse415,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_422 import (
    DeleteFirewallNATOutboundMappingEndpointResponse422,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_424 import (
    DeleteFirewallNATOutboundMappingEndpointResponse424,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_500 import (
    DeleteFirewallNATOutboundMappingEndpointResponse500,
)
from ...models.delete_firewall_nat_outbound_mapping_endpoint_response_503 import (
    DeleteFirewallNATOutboundMappingEndpointResponse503,
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
        "url": "/api/v2/firewall/nat/outbound/mapping",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallNATOutboundMappingEndpointResponse400
    | DeleteFirewallNATOutboundMappingEndpointResponse401
    | DeleteFirewallNATOutboundMappingEndpointResponse403
    | DeleteFirewallNATOutboundMappingEndpointResponse404
    | DeleteFirewallNATOutboundMappingEndpointResponse405
    | DeleteFirewallNATOutboundMappingEndpointResponse406
    | DeleteFirewallNATOutboundMappingEndpointResponse409
    | DeleteFirewallNATOutboundMappingEndpointResponse415
    | DeleteFirewallNATOutboundMappingEndpointResponse422
    | DeleteFirewallNATOutboundMappingEndpointResponse424
    | DeleteFirewallNATOutboundMappingEndpointResponse500
    | DeleteFirewallNATOutboundMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallNATOutboundMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallNATOutboundMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallNATOutboundMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallNATOutboundMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallNATOutboundMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallNATOutboundMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallNATOutboundMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallNATOutboundMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallNATOutboundMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallNATOutboundMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallNATOutboundMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallNATOutboundMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallNATOutboundMappingEndpointResponse400
    | DeleteFirewallNATOutboundMappingEndpointResponse401
    | DeleteFirewallNATOutboundMappingEndpointResponse403
    | DeleteFirewallNATOutboundMappingEndpointResponse404
    | DeleteFirewallNATOutboundMappingEndpointResponse405
    | DeleteFirewallNATOutboundMappingEndpointResponse406
    | DeleteFirewallNATOutboundMappingEndpointResponse409
    | DeleteFirewallNATOutboundMappingEndpointResponse415
    | DeleteFirewallNATOutboundMappingEndpointResponse422
    | DeleteFirewallNATOutboundMappingEndpointResponse424
    | DeleteFirewallNATOutboundMappingEndpointResponse500
    | DeleteFirewallNATOutboundMappingEndpointResponse503
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
    DeleteFirewallNATOutboundMappingEndpointResponse400
    | DeleteFirewallNATOutboundMappingEndpointResponse401
    | DeleteFirewallNATOutboundMappingEndpointResponse403
    | DeleteFirewallNATOutboundMappingEndpointResponse404
    | DeleteFirewallNATOutboundMappingEndpointResponse405
    | DeleteFirewallNATOutboundMappingEndpointResponse406
    | DeleteFirewallNATOutboundMappingEndpointResponse409
    | DeleteFirewallNATOutboundMappingEndpointResponse415
    | DeleteFirewallNATOutboundMappingEndpointResponse422
    | DeleteFirewallNATOutboundMappingEndpointResponse424
    | DeleteFirewallNATOutboundMappingEndpointResponse500
    | DeleteFirewallNATOutboundMappingEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallNATOutboundMappingEndpointResponse400 | DeleteFirewallNATOutboundMappingEndpointResponse401 | DeleteFirewallNATOutboundMappingEndpointResponse403 | DeleteFirewallNATOutboundMappingEndpointResponse404 | DeleteFirewallNATOutboundMappingEndpointResponse405 | DeleteFirewallNATOutboundMappingEndpointResponse406 | DeleteFirewallNATOutboundMappingEndpointResponse409 | DeleteFirewallNATOutboundMappingEndpointResponse415 | DeleteFirewallNATOutboundMappingEndpointResponse422 | DeleteFirewallNATOutboundMappingEndpointResponse424 | DeleteFirewallNATOutboundMappingEndpointResponse500 | DeleteFirewallNATOutboundMappingEndpointResponse503]
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
    DeleteFirewallNATOutboundMappingEndpointResponse400
    | DeleteFirewallNATOutboundMappingEndpointResponse401
    | DeleteFirewallNATOutboundMappingEndpointResponse403
    | DeleteFirewallNATOutboundMappingEndpointResponse404
    | DeleteFirewallNATOutboundMappingEndpointResponse405
    | DeleteFirewallNATOutboundMappingEndpointResponse406
    | DeleteFirewallNATOutboundMappingEndpointResponse409
    | DeleteFirewallNATOutboundMappingEndpointResponse415
    | DeleteFirewallNATOutboundMappingEndpointResponse422
    | DeleteFirewallNATOutboundMappingEndpointResponse424
    | DeleteFirewallNATOutboundMappingEndpointResponse500
    | DeleteFirewallNATOutboundMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallNATOutboundMappingEndpointResponse400 | DeleteFirewallNATOutboundMappingEndpointResponse401 | DeleteFirewallNATOutboundMappingEndpointResponse403 | DeleteFirewallNATOutboundMappingEndpointResponse404 | DeleteFirewallNATOutboundMappingEndpointResponse405 | DeleteFirewallNATOutboundMappingEndpointResponse406 | DeleteFirewallNATOutboundMappingEndpointResponse409 | DeleteFirewallNATOutboundMappingEndpointResponse415 | DeleteFirewallNATOutboundMappingEndpointResponse422 | DeleteFirewallNATOutboundMappingEndpointResponse424 | DeleteFirewallNATOutboundMappingEndpointResponse500 | DeleteFirewallNATOutboundMappingEndpointResponse503
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
    DeleteFirewallNATOutboundMappingEndpointResponse400
    | DeleteFirewallNATOutboundMappingEndpointResponse401
    | DeleteFirewallNATOutboundMappingEndpointResponse403
    | DeleteFirewallNATOutboundMappingEndpointResponse404
    | DeleteFirewallNATOutboundMappingEndpointResponse405
    | DeleteFirewallNATOutboundMappingEndpointResponse406
    | DeleteFirewallNATOutboundMappingEndpointResponse409
    | DeleteFirewallNATOutboundMappingEndpointResponse415
    | DeleteFirewallNATOutboundMappingEndpointResponse422
    | DeleteFirewallNATOutboundMappingEndpointResponse424
    | DeleteFirewallNATOutboundMappingEndpointResponse500
    | DeleteFirewallNATOutboundMappingEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallNATOutboundMappingEndpointResponse400 | DeleteFirewallNATOutboundMappingEndpointResponse401 | DeleteFirewallNATOutboundMappingEndpointResponse403 | DeleteFirewallNATOutboundMappingEndpointResponse404 | DeleteFirewallNATOutboundMappingEndpointResponse405 | DeleteFirewallNATOutboundMappingEndpointResponse406 | DeleteFirewallNATOutboundMappingEndpointResponse409 | DeleteFirewallNATOutboundMappingEndpointResponse415 | DeleteFirewallNATOutboundMappingEndpointResponse422 | DeleteFirewallNATOutboundMappingEndpointResponse424 | DeleteFirewallNATOutboundMappingEndpointResponse500 | DeleteFirewallNATOutboundMappingEndpointResponse503]
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
    DeleteFirewallNATOutboundMappingEndpointResponse400
    | DeleteFirewallNATOutboundMappingEndpointResponse401
    | DeleteFirewallNATOutboundMappingEndpointResponse403
    | DeleteFirewallNATOutboundMappingEndpointResponse404
    | DeleteFirewallNATOutboundMappingEndpointResponse405
    | DeleteFirewallNATOutboundMappingEndpointResponse406
    | DeleteFirewallNATOutboundMappingEndpointResponse409
    | DeleteFirewallNATOutboundMappingEndpointResponse415
    | DeleteFirewallNATOutboundMappingEndpointResponse422
    | DeleteFirewallNATOutboundMappingEndpointResponse424
    | DeleteFirewallNATOutboundMappingEndpointResponse500
    | DeleteFirewallNATOutboundMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallNATOutboundMappingEndpointResponse400 | DeleteFirewallNATOutboundMappingEndpointResponse401 | DeleteFirewallNATOutboundMappingEndpointResponse403 | DeleteFirewallNATOutboundMappingEndpointResponse404 | DeleteFirewallNATOutboundMappingEndpointResponse405 | DeleteFirewallNATOutboundMappingEndpointResponse406 | DeleteFirewallNATOutboundMappingEndpointResponse409 | DeleteFirewallNATOutboundMappingEndpointResponse415 | DeleteFirewallNATOutboundMappingEndpointResponse422 | DeleteFirewallNATOutboundMappingEndpointResponse424 | DeleteFirewallNATOutboundMappingEndpointResponse500 | DeleteFirewallNATOutboundMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            apply=apply,
        )
    ).parsed
