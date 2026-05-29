from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_nat_outbound_mapping_endpoint_data_body import (
    PostFirewallNATOutboundMappingEndpointDataBody,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_json_body import (
    PostFirewallNATOutboundMappingEndpointJsonBody,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_400 import (
    PostFirewallNATOutboundMappingEndpointResponse400,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_401 import (
    PostFirewallNATOutboundMappingEndpointResponse401,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_403 import (
    PostFirewallNATOutboundMappingEndpointResponse403,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_404 import (
    PostFirewallNATOutboundMappingEndpointResponse404,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_405 import (
    PostFirewallNATOutboundMappingEndpointResponse405,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_406 import (
    PostFirewallNATOutboundMappingEndpointResponse406,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_409 import (
    PostFirewallNATOutboundMappingEndpointResponse409,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_415 import (
    PostFirewallNATOutboundMappingEndpointResponse415,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_422 import (
    PostFirewallNATOutboundMappingEndpointResponse422,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_424 import (
    PostFirewallNATOutboundMappingEndpointResponse424,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_500 import (
    PostFirewallNATOutboundMappingEndpointResponse500,
)
from ...models.post_firewall_nat_outbound_mapping_endpoint_response_503 import (
    PostFirewallNATOutboundMappingEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallNATOutboundMappingEndpointJsonBody
    | PostFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/nat/outbound/mapping",
    }

    if isinstance(body, PostFirewallNATOutboundMappingEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallNATOutboundMappingEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallNATOutboundMappingEndpointResponse400
    | PostFirewallNATOutboundMappingEndpointResponse401
    | PostFirewallNATOutboundMappingEndpointResponse403
    | PostFirewallNATOutboundMappingEndpointResponse404
    | PostFirewallNATOutboundMappingEndpointResponse405
    | PostFirewallNATOutboundMappingEndpointResponse406
    | PostFirewallNATOutboundMappingEndpointResponse409
    | PostFirewallNATOutboundMappingEndpointResponse415
    | PostFirewallNATOutboundMappingEndpointResponse422
    | PostFirewallNATOutboundMappingEndpointResponse424
    | PostFirewallNATOutboundMappingEndpointResponse500
    | PostFirewallNATOutboundMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallNATOutboundMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallNATOutboundMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallNATOutboundMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallNATOutboundMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallNATOutboundMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallNATOutboundMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallNATOutboundMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallNATOutboundMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallNATOutboundMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallNATOutboundMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallNATOutboundMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallNATOutboundMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallNATOutboundMappingEndpointResponse400
    | PostFirewallNATOutboundMappingEndpointResponse401
    | PostFirewallNATOutboundMappingEndpointResponse403
    | PostFirewallNATOutboundMappingEndpointResponse404
    | PostFirewallNATOutboundMappingEndpointResponse405
    | PostFirewallNATOutboundMappingEndpointResponse406
    | PostFirewallNATOutboundMappingEndpointResponse409
    | PostFirewallNATOutboundMappingEndpointResponse415
    | PostFirewallNATOutboundMappingEndpointResponse422
    | PostFirewallNATOutboundMappingEndpointResponse424
    | PostFirewallNATOutboundMappingEndpointResponse500
    | PostFirewallNATOutboundMappingEndpointResponse503
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
    body: PostFirewallNATOutboundMappingEndpointJsonBody
    | PostFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallNATOutboundMappingEndpointResponse400
    | PostFirewallNATOutboundMappingEndpointResponse401
    | PostFirewallNATOutboundMappingEndpointResponse403
    | PostFirewallNATOutboundMappingEndpointResponse404
    | PostFirewallNATOutboundMappingEndpointResponse405
    | PostFirewallNATOutboundMappingEndpointResponse406
    | PostFirewallNATOutboundMappingEndpointResponse409
    | PostFirewallNATOutboundMappingEndpointResponse415
    | PostFirewallNATOutboundMappingEndpointResponse422
    | PostFirewallNATOutboundMappingEndpointResponse424
    | PostFirewallNATOutboundMappingEndpointResponse500
    | PostFirewallNATOutboundMappingEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PostFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallNATOutboundMappingEndpointResponse400 | PostFirewallNATOutboundMappingEndpointResponse401 | PostFirewallNATOutboundMappingEndpointResponse403 | PostFirewallNATOutboundMappingEndpointResponse404 | PostFirewallNATOutboundMappingEndpointResponse405 | PostFirewallNATOutboundMappingEndpointResponse406 | PostFirewallNATOutboundMappingEndpointResponse409 | PostFirewallNATOutboundMappingEndpointResponse415 | PostFirewallNATOutboundMappingEndpointResponse422 | PostFirewallNATOutboundMappingEndpointResponse424 | PostFirewallNATOutboundMappingEndpointResponse500 | PostFirewallNATOutboundMappingEndpointResponse503]
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
    body: PostFirewallNATOutboundMappingEndpointJsonBody
    | PostFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallNATOutboundMappingEndpointResponse400
    | PostFirewallNATOutboundMappingEndpointResponse401
    | PostFirewallNATOutboundMappingEndpointResponse403
    | PostFirewallNATOutboundMappingEndpointResponse404
    | PostFirewallNATOutboundMappingEndpointResponse405
    | PostFirewallNATOutboundMappingEndpointResponse406
    | PostFirewallNATOutboundMappingEndpointResponse409
    | PostFirewallNATOutboundMappingEndpointResponse415
    | PostFirewallNATOutboundMappingEndpointResponse422
    | PostFirewallNATOutboundMappingEndpointResponse424
    | PostFirewallNATOutboundMappingEndpointResponse500
    | PostFirewallNATOutboundMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PostFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallNATOutboundMappingEndpointResponse400 | PostFirewallNATOutboundMappingEndpointResponse401 | PostFirewallNATOutboundMappingEndpointResponse403 | PostFirewallNATOutboundMappingEndpointResponse404 | PostFirewallNATOutboundMappingEndpointResponse405 | PostFirewallNATOutboundMappingEndpointResponse406 | PostFirewallNATOutboundMappingEndpointResponse409 | PostFirewallNATOutboundMappingEndpointResponse415 | PostFirewallNATOutboundMappingEndpointResponse422 | PostFirewallNATOutboundMappingEndpointResponse424 | PostFirewallNATOutboundMappingEndpointResponse500 | PostFirewallNATOutboundMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallNATOutboundMappingEndpointJsonBody
    | PostFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallNATOutboundMappingEndpointResponse400
    | PostFirewallNATOutboundMappingEndpointResponse401
    | PostFirewallNATOutboundMappingEndpointResponse403
    | PostFirewallNATOutboundMappingEndpointResponse404
    | PostFirewallNATOutboundMappingEndpointResponse405
    | PostFirewallNATOutboundMappingEndpointResponse406
    | PostFirewallNATOutboundMappingEndpointResponse409
    | PostFirewallNATOutboundMappingEndpointResponse415
    | PostFirewallNATOutboundMappingEndpointResponse422
    | PostFirewallNATOutboundMappingEndpointResponse424
    | PostFirewallNATOutboundMappingEndpointResponse500
    | PostFirewallNATOutboundMappingEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PostFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallNATOutboundMappingEndpointResponse400 | PostFirewallNATOutboundMappingEndpointResponse401 | PostFirewallNATOutboundMappingEndpointResponse403 | PostFirewallNATOutboundMappingEndpointResponse404 | PostFirewallNATOutboundMappingEndpointResponse405 | PostFirewallNATOutboundMappingEndpointResponse406 | PostFirewallNATOutboundMappingEndpointResponse409 | PostFirewallNATOutboundMappingEndpointResponse415 | PostFirewallNATOutboundMappingEndpointResponse422 | PostFirewallNATOutboundMappingEndpointResponse424 | PostFirewallNATOutboundMappingEndpointResponse500 | PostFirewallNATOutboundMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallNATOutboundMappingEndpointJsonBody
    | PostFirewallNATOutboundMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallNATOutboundMappingEndpointResponse400
    | PostFirewallNATOutboundMappingEndpointResponse401
    | PostFirewallNATOutboundMappingEndpointResponse403
    | PostFirewallNATOutboundMappingEndpointResponse404
    | PostFirewallNATOutboundMappingEndpointResponse405
    | PostFirewallNATOutboundMappingEndpointResponse406
    | PostFirewallNATOutboundMappingEndpointResponse409
    | PostFirewallNATOutboundMappingEndpointResponse415
    | PostFirewallNATOutboundMappingEndpointResponse422
    | PostFirewallNATOutboundMappingEndpointResponse424
    | PostFirewallNATOutboundMappingEndpointResponse500
    | PostFirewallNATOutboundMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Outbound NAT Mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OutboundNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-outbound-mapping-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATOutboundMappingEndpointJsonBody | Unset):
        body (PostFirewallNATOutboundMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallNATOutboundMappingEndpointResponse400 | PostFirewallNATOutboundMappingEndpointResponse401 | PostFirewallNATOutboundMappingEndpointResponse403 | PostFirewallNATOutboundMappingEndpointResponse404 | PostFirewallNATOutboundMappingEndpointResponse405 | PostFirewallNATOutboundMappingEndpointResponse406 | PostFirewallNATOutboundMappingEndpointResponse409 | PostFirewallNATOutboundMappingEndpointResponse415 | PostFirewallNATOutboundMappingEndpointResponse422 | PostFirewallNATOutboundMappingEndpointResponse424 | PostFirewallNATOutboundMappingEndpointResponse500 | PostFirewallNATOutboundMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
