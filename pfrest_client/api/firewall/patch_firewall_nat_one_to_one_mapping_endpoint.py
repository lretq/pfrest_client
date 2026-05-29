from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_data_body import (
    PatchFirewallNATOneToOneMappingEndpointDataBody,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_json_body import (
    PatchFirewallNATOneToOneMappingEndpointJsonBody,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_400 import (
    PatchFirewallNATOneToOneMappingEndpointResponse400,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_401 import (
    PatchFirewallNATOneToOneMappingEndpointResponse401,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_403 import (
    PatchFirewallNATOneToOneMappingEndpointResponse403,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_404 import (
    PatchFirewallNATOneToOneMappingEndpointResponse404,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_405 import (
    PatchFirewallNATOneToOneMappingEndpointResponse405,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_406 import (
    PatchFirewallNATOneToOneMappingEndpointResponse406,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_409 import (
    PatchFirewallNATOneToOneMappingEndpointResponse409,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_415 import (
    PatchFirewallNATOneToOneMappingEndpointResponse415,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_422 import (
    PatchFirewallNATOneToOneMappingEndpointResponse422,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_424 import (
    PatchFirewallNATOneToOneMappingEndpointResponse424,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_500 import (
    PatchFirewallNATOneToOneMappingEndpointResponse500,
)
from ...models.patch_firewall_nat_one_to_one_mapping_endpoint_response_503 import (
    PatchFirewallNATOneToOneMappingEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallNATOneToOneMappingEndpointJsonBody
    | PatchFirewallNATOneToOneMappingEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/nat/one_to_one/mapping",
    }

    if isinstance(body, PatchFirewallNATOneToOneMappingEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallNATOneToOneMappingEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallNATOneToOneMappingEndpointResponse400
    | PatchFirewallNATOneToOneMappingEndpointResponse401
    | PatchFirewallNATOneToOneMappingEndpointResponse403
    | PatchFirewallNATOneToOneMappingEndpointResponse404
    | PatchFirewallNATOneToOneMappingEndpointResponse405
    | PatchFirewallNATOneToOneMappingEndpointResponse406
    | PatchFirewallNATOneToOneMappingEndpointResponse409
    | PatchFirewallNATOneToOneMappingEndpointResponse415
    | PatchFirewallNATOneToOneMappingEndpointResponse422
    | PatchFirewallNATOneToOneMappingEndpointResponse424
    | PatchFirewallNATOneToOneMappingEndpointResponse500
    | PatchFirewallNATOneToOneMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallNATOneToOneMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallNATOneToOneMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallNATOneToOneMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallNATOneToOneMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallNATOneToOneMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallNATOneToOneMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallNATOneToOneMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallNATOneToOneMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallNATOneToOneMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallNATOneToOneMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallNATOneToOneMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallNATOneToOneMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallNATOneToOneMappingEndpointResponse400
    | PatchFirewallNATOneToOneMappingEndpointResponse401
    | PatchFirewallNATOneToOneMappingEndpointResponse403
    | PatchFirewallNATOneToOneMappingEndpointResponse404
    | PatchFirewallNATOneToOneMappingEndpointResponse405
    | PatchFirewallNATOneToOneMappingEndpointResponse406
    | PatchFirewallNATOneToOneMappingEndpointResponse409
    | PatchFirewallNATOneToOneMappingEndpointResponse415
    | PatchFirewallNATOneToOneMappingEndpointResponse422
    | PatchFirewallNATOneToOneMappingEndpointResponse424
    | PatchFirewallNATOneToOneMappingEndpointResponse500
    | PatchFirewallNATOneToOneMappingEndpointResponse503
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
    body: PatchFirewallNATOneToOneMappingEndpointJsonBody
    | PatchFirewallNATOneToOneMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallNATOneToOneMappingEndpointResponse400
    | PatchFirewallNATOneToOneMappingEndpointResponse401
    | PatchFirewallNATOneToOneMappingEndpointResponse403
    | PatchFirewallNATOneToOneMappingEndpointResponse404
    | PatchFirewallNATOneToOneMappingEndpointResponse405
    | PatchFirewallNATOneToOneMappingEndpointResponse406
    | PatchFirewallNATOneToOneMappingEndpointResponse409
    | PatchFirewallNATOneToOneMappingEndpointResponse415
    | PatchFirewallNATOneToOneMappingEndpointResponse422
    | PatchFirewallNATOneToOneMappingEndpointResponse424
    | PatchFirewallNATOneToOneMappingEndpointResponse500
    | PatchFirewallNATOneToOneMappingEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing 1:1 NAT mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OneToOneNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-one-to-one-mapping-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOneToOneMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOneToOneMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallNATOneToOneMappingEndpointResponse400 | PatchFirewallNATOneToOneMappingEndpointResponse401 | PatchFirewallNATOneToOneMappingEndpointResponse403 | PatchFirewallNATOneToOneMappingEndpointResponse404 | PatchFirewallNATOneToOneMappingEndpointResponse405 | PatchFirewallNATOneToOneMappingEndpointResponse406 | PatchFirewallNATOneToOneMappingEndpointResponse409 | PatchFirewallNATOneToOneMappingEndpointResponse415 | PatchFirewallNATOneToOneMappingEndpointResponse422 | PatchFirewallNATOneToOneMappingEndpointResponse424 | PatchFirewallNATOneToOneMappingEndpointResponse500 | PatchFirewallNATOneToOneMappingEndpointResponse503]
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
    body: PatchFirewallNATOneToOneMappingEndpointJsonBody
    | PatchFirewallNATOneToOneMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallNATOneToOneMappingEndpointResponse400
    | PatchFirewallNATOneToOneMappingEndpointResponse401
    | PatchFirewallNATOneToOneMappingEndpointResponse403
    | PatchFirewallNATOneToOneMappingEndpointResponse404
    | PatchFirewallNATOneToOneMappingEndpointResponse405
    | PatchFirewallNATOneToOneMappingEndpointResponse406
    | PatchFirewallNATOneToOneMappingEndpointResponse409
    | PatchFirewallNATOneToOneMappingEndpointResponse415
    | PatchFirewallNATOneToOneMappingEndpointResponse422
    | PatchFirewallNATOneToOneMappingEndpointResponse424
    | PatchFirewallNATOneToOneMappingEndpointResponse500
    | PatchFirewallNATOneToOneMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing 1:1 NAT mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OneToOneNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-one-to-one-mapping-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOneToOneMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOneToOneMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallNATOneToOneMappingEndpointResponse400 | PatchFirewallNATOneToOneMappingEndpointResponse401 | PatchFirewallNATOneToOneMappingEndpointResponse403 | PatchFirewallNATOneToOneMappingEndpointResponse404 | PatchFirewallNATOneToOneMappingEndpointResponse405 | PatchFirewallNATOneToOneMappingEndpointResponse406 | PatchFirewallNATOneToOneMappingEndpointResponse409 | PatchFirewallNATOneToOneMappingEndpointResponse415 | PatchFirewallNATOneToOneMappingEndpointResponse422 | PatchFirewallNATOneToOneMappingEndpointResponse424 | PatchFirewallNATOneToOneMappingEndpointResponse500 | PatchFirewallNATOneToOneMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallNATOneToOneMappingEndpointJsonBody
    | PatchFirewallNATOneToOneMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallNATOneToOneMappingEndpointResponse400
    | PatchFirewallNATOneToOneMappingEndpointResponse401
    | PatchFirewallNATOneToOneMappingEndpointResponse403
    | PatchFirewallNATOneToOneMappingEndpointResponse404
    | PatchFirewallNATOneToOneMappingEndpointResponse405
    | PatchFirewallNATOneToOneMappingEndpointResponse406
    | PatchFirewallNATOneToOneMappingEndpointResponse409
    | PatchFirewallNATOneToOneMappingEndpointResponse415
    | PatchFirewallNATOneToOneMappingEndpointResponse422
    | PatchFirewallNATOneToOneMappingEndpointResponse424
    | PatchFirewallNATOneToOneMappingEndpointResponse500
    | PatchFirewallNATOneToOneMappingEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing 1:1 NAT mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OneToOneNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-one-to-one-mapping-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOneToOneMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOneToOneMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallNATOneToOneMappingEndpointResponse400 | PatchFirewallNATOneToOneMappingEndpointResponse401 | PatchFirewallNATOneToOneMappingEndpointResponse403 | PatchFirewallNATOneToOneMappingEndpointResponse404 | PatchFirewallNATOneToOneMappingEndpointResponse405 | PatchFirewallNATOneToOneMappingEndpointResponse406 | PatchFirewallNATOneToOneMappingEndpointResponse409 | PatchFirewallNATOneToOneMappingEndpointResponse415 | PatchFirewallNATOneToOneMappingEndpointResponse422 | PatchFirewallNATOneToOneMappingEndpointResponse424 | PatchFirewallNATOneToOneMappingEndpointResponse500 | PatchFirewallNATOneToOneMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallNATOneToOneMappingEndpointJsonBody
    | PatchFirewallNATOneToOneMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallNATOneToOneMappingEndpointResponse400
    | PatchFirewallNATOneToOneMappingEndpointResponse401
    | PatchFirewallNATOneToOneMappingEndpointResponse403
    | PatchFirewallNATOneToOneMappingEndpointResponse404
    | PatchFirewallNATOneToOneMappingEndpointResponse405
    | PatchFirewallNATOneToOneMappingEndpointResponse406
    | PatchFirewallNATOneToOneMappingEndpointResponse409
    | PatchFirewallNATOneToOneMappingEndpointResponse415
    | PatchFirewallNATOneToOneMappingEndpointResponse422
    | PatchFirewallNATOneToOneMappingEndpointResponse424
    | PatchFirewallNATOneToOneMappingEndpointResponse500
    | PatchFirewallNATOneToOneMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing 1:1 NAT mapping.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OneToOneNATMapping<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-one-to-one-mapping-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATOneToOneMappingEndpointJsonBody | Unset):
        body (PatchFirewallNATOneToOneMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallNATOneToOneMappingEndpointResponse400 | PatchFirewallNATOneToOneMappingEndpointResponse401 | PatchFirewallNATOneToOneMappingEndpointResponse403 | PatchFirewallNATOneToOneMappingEndpointResponse404 | PatchFirewallNATOneToOneMappingEndpointResponse405 | PatchFirewallNATOneToOneMappingEndpointResponse406 | PatchFirewallNATOneToOneMappingEndpointResponse409 | PatchFirewallNATOneToOneMappingEndpointResponse415 | PatchFirewallNATOneToOneMappingEndpointResponse422 | PatchFirewallNATOneToOneMappingEndpointResponse424 | PatchFirewallNATOneToOneMappingEndpointResponse500 | PatchFirewallNATOneToOneMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
