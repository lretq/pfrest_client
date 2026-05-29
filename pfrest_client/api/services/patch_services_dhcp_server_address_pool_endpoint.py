from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dhcp_server_address_pool_endpoint_data_body import (
    PatchServicesDHCPServerAddressPoolEndpointDataBody,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_json_body import (
    PatchServicesDHCPServerAddressPoolEndpointJsonBody,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_400 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse400,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_401 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse401,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_403 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse403,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_404 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse404,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_405 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse405,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_406 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse406,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_409 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse409,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_415 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse415,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_422 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse422,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_424 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse424,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_500 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse500,
)
from ...models.patch_services_dhcp_server_address_pool_endpoint_response_503 import (
    PatchServicesDHCPServerAddressPoolEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDHCPServerAddressPoolEndpointJsonBody
    | PatchServicesDHCPServerAddressPoolEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dhcp_server/address_pool",
    }

    if isinstance(body, PatchServicesDHCPServerAddressPoolEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDHCPServerAddressPoolEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDHCPServerAddressPoolEndpointResponse400
    | PatchServicesDHCPServerAddressPoolEndpointResponse401
    | PatchServicesDHCPServerAddressPoolEndpointResponse403
    | PatchServicesDHCPServerAddressPoolEndpointResponse404
    | PatchServicesDHCPServerAddressPoolEndpointResponse405
    | PatchServicesDHCPServerAddressPoolEndpointResponse406
    | PatchServicesDHCPServerAddressPoolEndpointResponse409
    | PatchServicesDHCPServerAddressPoolEndpointResponse415
    | PatchServicesDHCPServerAddressPoolEndpointResponse422
    | PatchServicesDHCPServerAddressPoolEndpointResponse424
    | PatchServicesDHCPServerAddressPoolEndpointResponse500
    | PatchServicesDHCPServerAddressPoolEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDHCPServerAddressPoolEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDHCPServerAddressPoolEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDHCPServerAddressPoolEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDHCPServerAddressPoolEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDHCPServerAddressPoolEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDHCPServerAddressPoolEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDHCPServerAddressPoolEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDHCPServerAddressPoolEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDHCPServerAddressPoolEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDHCPServerAddressPoolEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDHCPServerAddressPoolEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDHCPServerAddressPoolEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDHCPServerAddressPoolEndpointResponse400
    | PatchServicesDHCPServerAddressPoolEndpointResponse401
    | PatchServicesDHCPServerAddressPoolEndpointResponse403
    | PatchServicesDHCPServerAddressPoolEndpointResponse404
    | PatchServicesDHCPServerAddressPoolEndpointResponse405
    | PatchServicesDHCPServerAddressPoolEndpointResponse406
    | PatchServicesDHCPServerAddressPoolEndpointResponse409
    | PatchServicesDHCPServerAddressPoolEndpointResponse415
    | PatchServicesDHCPServerAddressPoolEndpointResponse422
    | PatchServicesDHCPServerAddressPoolEndpointResponse424
    | PatchServicesDHCPServerAddressPoolEndpointResponse500
    | PatchServicesDHCPServerAddressPoolEndpointResponse503
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
    body: PatchServicesDHCPServerAddressPoolEndpointJsonBody
    | PatchServicesDHCPServerAddressPoolEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerAddressPoolEndpointResponse400
    | PatchServicesDHCPServerAddressPoolEndpointResponse401
    | PatchServicesDHCPServerAddressPoolEndpointResponse403
    | PatchServicesDHCPServerAddressPoolEndpointResponse404
    | PatchServicesDHCPServerAddressPoolEndpointResponse405
    | PatchServicesDHCPServerAddressPoolEndpointResponse406
    | PatchServicesDHCPServerAddressPoolEndpointResponse409
    | PatchServicesDHCPServerAddressPoolEndpointResponse415
    | PatchServicesDHCPServerAddressPoolEndpointResponse422
    | PatchServicesDHCPServerAddressPoolEndpointResponse424
    | PatchServicesDHCPServerAddressPoolEndpointResponse500
    | PatchServicesDHCPServerAddressPoolEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server Address Pool.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerAddressPool<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-address-pool-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerAddressPoolEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerAddressPoolEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerAddressPoolEndpointResponse400 | PatchServicesDHCPServerAddressPoolEndpointResponse401 | PatchServicesDHCPServerAddressPoolEndpointResponse403 | PatchServicesDHCPServerAddressPoolEndpointResponse404 | PatchServicesDHCPServerAddressPoolEndpointResponse405 | PatchServicesDHCPServerAddressPoolEndpointResponse406 | PatchServicesDHCPServerAddressPoolEndpointResponse409 | PatchServicesDHCPServerAddressPoolEndpointResponse415 | PatchServicesDHCPServerAddressPoolEndpointResponse422 | PatchServicesDHCPServerAddressPoolEndpointResponse424 | PatchServicesDHCPServerAddressPoolEndpointResponse500 | PatchServicesDHCPServerAddressPoolEndpointResponse503]
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
    body: PatchServicesDHCPServerAddressPoolEndpointJsonBody
    | PatchServicesDHCPServerAddressPoolEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerAddressPoolEndpointResponse400
    | PatchServicesDHCPServerAddressPoolEndpointResponse401
    | PatchServicesDHCPServerAddressPoolEndpointResponse403
    | PatchServicesDHCPServerAddressPoolEndpointResponse404
    | PatchServicesDHCPServerAddressPoolEndpointResponse405
    | PatchServicesDHCPServerAddressPoolEndpointResponse406
    | PatchServicesDHCPServerAddressPoolEndpointResponse409
    | PatchServicesDHCPServerAddressPoolEndpointResponse415
    | PatchServicesDHCPServerAddressPoolEndpointResponse422
    | PatchServicesDHCPServerAddressPoolEndpointResponse424
    | PatchServicesDHCPServerAddressPoolEndpointResponse500
    | PatchServicesDHCPServerAddressPoolEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server Address Pool.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerAddressPool<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-address-pool-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerAddressPoolEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerAddressPoolEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerAddressPoolEndpointResponse400 | PatchServicesDHCPServerAddressPoolEndpointResponse401 | PatchServicesDHCPServerAddressPoolEndpointResponse403 | PatchServicesDHCPServerAddressPoolEndpointResponse404 | PatchServicesDHCPServerAddressPoolEndpointResponse405 | PatchServicesDHCPServerAddressPoolEndpointResponse406 | PatchServicesDHCPServerAddressPoolEndpointResponse409 | PatchServicesDHCPServerAddressPoolEndpointResponse415 | PatchServicesDHCPServerAddressPoolEndpointResponse422 | PatchServicesDHCPServerAddressPoolEndpointResponse424 | PatchServicesDHCPServerAddressPoolEndpointResponse500 | PatchServicesDHCPServerAddressPoolEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerAddressPoolEndpointJsonBody
    | PatchServicesDHCPServerAddressPoolEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerAddressPoolEndpointResponse400
    | PatchServicesDHCPServerAddressPoolEndpointResponse401
    | PatchServicesDHCPServerAddressPoolEndpointResponse403
    | PatchServicesDHCPServerAddressPoolEndpointResponse404
    | PatchServicesDHCPServerAddressPoolEndpointResponse405
    | PatchServicesDHCPServerAddressPoolEndpointResponse406
    | PatchServicesDHCPServerAddressPoolEndpointResponse409
    | PatchServicesDHCPServerAddressPoolEndpointResponse415
    | PatchServicesDHCPServerAddressPoolEndpointResponse422
    | PatchServicesDHCPServerAddressPoolEndpointResponse424
    | PatchServicesDHCPServerAddressPoolEndpointResponse500
    | PatchServicesDHCPServerAddressPoolEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server Address Pool.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerAddressPool<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-address-pool-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerAddressPoolEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerAddressPoolEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerAddressPoolEndpointResponse400 | PatchServicesDHCPServerAddressPoolEndpointResponse401 | PatchServicesDHCPServerAddressPoolEndpointResponse403 | PatchServicesDHCPServerAddressPoolEndpointResponse404 | PatchServicesDHCPServerAddressPoolEndpointResponse405 | PatchServicesDHCPServerAddressPoolEndpointResponse406 | PatchServicesDHCPServerAddressPoolEndpointResponse409 | PatchServicesDHCPServerAddressPoolEndpointResponse415 | PatchServicesDHCPServerAddressPoolEndpointResponse422 | PatchServicesDHCPServerAddressPoolEndpointResponse424 | PatchServicesDHCPServerAddressPoolEndpointResponse500 | PatchServicesDHCPServerAddressPoolEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerAddressPoolEndpointJsonBody
    | PatchServicesDHCPServerAddressPoolEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerAddressPoolEndpointResponse400
    | PatchServicesDHCPServerAddressPoolEndpointResponse401
    | PatchServicesDHCPServerAddressPoolEndpointResponse403
    | PatchServicesDHCPServerAddressPoolEndpointResponse404
    | PatchServicesDHCPServerAddressPoolEndpointResponse405
    | PatchServicesDHCPServerAddressPoolEndpointResponse406
    | PatchServicesDHCPServerAddressPoolEndpointResponse409
    | PatchServicesDHCPServerAddressPoolEndpointResponse415
    | PatchServicesDHCPServerAddressPoolEndpointResponse422
    | PatchServicesDHCPServerAddressPoolEndpointResponse424
    | PatchServicesDHCPServerAddressPoolEndpointResponse500
    | PatchServicesDHCPServerAddressPoolEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server Address Pool.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerAddressPool<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-address-pool-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerAddressPoolEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerAddressPoolEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerAddressPoolEndpointResponse400 | PatchServicesDHCPServerAddressPoolEndpointResponse401 | PatchServicesDHCPServerAddressPoolEndpointResponse403 | PatchServicesDHCPServerAddressPoolEndpointResponse404 | PatchServicesDHCPServerAddressPoolEndpointResponse405 | PatchServicesDHCPServerAddressPoolEndpointResponse406 | PatchServicesDHCPServerAddressPoolEndpointResponse409 | PatchServicesDHCPServerAddressPoolEndpointResponse415 | PatchServicesDHCPServerAddressPoolEndpointResponse422 | PatchServicesDHCPServerAddressPoolEndpointResponse424 | PatchServicesDHCPServerAddressPoolEndpointResponse500 | PatchServicesDHCPServerAddressPoolEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
