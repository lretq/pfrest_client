from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dhcp_server_static_mapping_endpoint_data_body import (
    PatchServicesDHCPServerStaticMappingEndpointDataBody,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_json_body import (
    PatchServicesDHCPServerStaticMappingEndpointJsonBody,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_400 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse400,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_401 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse401,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_403 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse403,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_404 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse404,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_405 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse405,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_406 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse406,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_409 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse409,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_415 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse415,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_422 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse422,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_424 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse424,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_500 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse500,
)
from ...models.patch_services_dhcp_server_static_mapping_endpoint_response_503 import (
    PatchServicesDHCPServerStaticMappingEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDHCPServerStaticMappingEndpointJsonBody
    | PatchServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dhcp_server/static_mapping",
    }

    if isinstance(body, PatchServicesDHCPServerStaticMappingEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDHCPServerStaticMappingEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDHCPServerStaticMappingEndpointResponse400
    | PatchServicesDHCPServerStaticMappingEndpointResponse401
    | PatchServicesDHCPServerStaticMappingEndpointResponse403
    | PatchServicesDHCPServerStaticMappingEndpointResponse404
    | PatchServicesDHCPServerStaticMappingEndpointResponse405
    | PatchServicesDHCPServerStaticMappingEndpointResponse406
    | PatchServicesDHCPServerStaticMappingEndpointResponse409
    | PatchServicesDHCPServerStaticMappingEndpointResponse415
    | PatchServicesDHCPServerStaticMappingEndpointResponse422
    | PatchServicesDHCPServerStaticMappingEndpointResponse424
    | PatchServicesDHCPServerStaticMappingEndpointResponse500
    | PatchServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDHCPServerStaticMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDHCPServerStaticMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDHCPServerStaticMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDHCPServerStaticMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDHCPServerStaticMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDHCPServerStaticMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDHCPServerStaticMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDHCPServerStaticMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDHCPServerStaticMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDHCPServerStaticMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDHCPServerStaticMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDHCPServerStaticMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDHCPServerStaticMappingEndpointResponse400
    | PatchServicesDHCPServerStaticMappingEndpointResponse401
    | PatchServicesDHCPServerStaticMappingEndpointResponse403
    | PatchServicesDHCPServerStaticMappingEndpointResponse404
    | PatchServicesDHCPServerStaticMappingEndpointResponse405
    | PatchServicesDHCPServerStaticMappingEndpointResponse406
    | PatchServicesDHCPServerStaticMappingEndpointResponse409
    | PatchServicesDHCPServerStaticMappingEndpointResponse415
    | PatchServicesDHCPServerStaticMappingEndpointResponse422
    | PatchServicesDHCPServerStaticMappingEndpointResponse424
    | PatchServicesDHCPServerStaticMappingEndpointResponse500
    | PatchServicesDHCPServerStaticMappingEndpointResponse503
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
    body: PatchServicesDHCPServerStaticMappingEndpointJsonBody
    | PatchServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerStaticMappingEndpointResponse400
    | PatchServicesDHCPServerStaticMappingEndpointResponse401
    | PatchServicesDHCPServerStaticMappingEndpointResponse403
    | PatchServicesDHCPServerStaticMappingEndpointResponse404
    | PatchServicesDHCPServerStaticMappingEndpointResponse405
    | PatchServicesDHCPServerStaticMappingEndpointResponse406
    | PatchServicesDHCPServerStaticMappingEndpointResponse409
    | PatchServicesDHCPServerStaticMappingEndpointResponse415
    | PatchServicesDHCPServerStaticMappingEndpointResponse422
    | PatchServicesDHCPServerStaticMappingEndpointResponse424
    | PatchServicesDHCPServerStaticMappingEndpointResponse500
    | PatchServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerStaticMappingEndpointResponse400 | PatchServicesDHCPServerStaticMappingEndpointResponse401 | PatchServicesDHCPServerStaticMappingEndpointResponse403 | PatchServicesDHCPServerStaticMappingEndpointResponse404 | PatchServicesDHCPServerStaticMappingEndpointResponse405 | PatchServicesDHCPServerStaticMappingEndpointResponse406 | PatchServicesDHCPServerStaticMappingEndpointResponse409 | PatchServicesDHCPServerStaticMappingEndpointResponse415 | PatchServicesDHCPServerStaticMappingEndpointResponse422 | PatchServicesDHCPServerStaticMappingEndpointResponse424 | PatchServicesDHCPServerStaticMappingEndpointResponse500 | PatchServicesDHCPServerStaticMappingEndpointResponse503]
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
    body: PatchServicesDHCPServerStaticMappingEndpointJsonBody
    | PatchServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerStaticMappingEndpointResponse400
    | PatchServicesDHCPServerStaticMappingEndpointResponse401
    | PatchServicesDHCPServerStaticMappingEndpointResponse403
    | PatchServicesDHCPServerStaticMappingEndpointResponse404
    | PatchServicesDHCPServerStaticMappingEndpointResponse405
    | PatchServicesDHCPServerStaticMappingEndpointResponse406
    | PatchServicesDHCPServerStaticMappingEndpointResponse409
    | PatchServicesDHCPServerStaticMappingEndpointResponse415
    | PatchServicesDHCPServerStaticMappingEndpointResponse422
    | PatchServicesDHCPServerStaticMappingEndpointResponse424
    | PatchServicesDHCPServerStaticMappingEndpointResponse500
    | PatchServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerStaticMappingEndpointResponse400 | PatchServicesDHCPServerStaticMappingEndpointResponse401 | PatchServicesDHCPServerStaticMappingEndpointResponse403 | PatchServicesDHCPServerStaticMappingEndpointResponse404 | PatchServicesDHCPServerStaticMappingEndpointResponse405 | PatchServicesDHCPServerStaticMappingEndpointResponse406 | PatchServicesDHCPServerStaticMappingEndpointResponse409 | PatchServicesDHCPServerStaticMappingEndpointResponse415 | PatchServicesDHCPServerStaticMappingEndpointResponse422 | PatchServicesDHCPServerStaticMappingEndpointResponse424 | PatchServicesDHCPServerStaticMappingEndpointResponse500 | PatchServicesDHCPServerStaticMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerStaticMappingEndpointJsonBody
    | PatchServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerStaticMappingEndpointResponse400
    | PatchServicesDHCPServerStaticMappingEndpointResponse401
    | PatchServicesDHCPServerStaticMappingEndpointResponse403
    | PatchServicesDHCPServerStaticMappingEndpointResponse404
    | PatchServicesDHCPServerStaticMappingEndpointResponse405
    | PatchServicesDHCPServerStaticMappingEndpointResponse406
    | PatchServicesDHCPServerStaticMappingEndpointResponse409
    | PatchServicesDHCPServerStaticMappingEndpointResponse415
    | PatchServicesDHCPServerStaticMappingEndpointResponse422
    | PatchServicesDHCPServerStaticMappingEndpointResponse424
    | PatchServicesDHCPServerStaticMappingEndpointResponse500
    | PatchServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerStaticMappingEndpointResponse400 | PatchServicesDHCPServerStaticMappingEndpointResponse401 | PatchServicesDHCPServerStaticMappingEndpointResponse403 | PatchServicesDHCPServerStaticMappingEndpointResponse404 | PatchServicesDHCPServerStaticMappingEndpointResponse405 | PatchServicesDHCPServerStaticMappingEndpointResponse406 | PatchServicesDHCPServerStaticMappingEndpointResponse409 | PatchServicesDHCPServerStaticMappingEndpointResponse415 | PatchServicesDHCPServerStaticMappingEndpointResponse422 | PatchServicesDHCPServerStaticMappingEndpointResponse424 | PatchServicesDHCPServerStaticMappingEndpointResponse500 | PatchServicesDHCPServerStaticMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerStaticMappingEndpointJsonBody
    | PatchServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerStaticMappingEndpointResponse400
    | PatchServicesDHCPServerStaticMappingEndpointResponse401
    | PatchServicesDHCPServerStaticMappingEndpointResponse403
    | PatchServicesDHCPServerStaticMappingEndpointResponse404
    | PatchServicesDHCPServerStaticMappingEndpointResponse405
    | PatchServicesDHCPServerStaticMappingEndpointResponse406
    | PatchServicesDHCPServerStaticMappingEndpointResponse409
    | PatchServicesDHCPServerStaticMappingEndpointResponse415
    | PatchServicesDHCPServerStaticMappingEndpointResponse422
    | PatchServicesDHCPServerStaticMappingEndpointResponse424
    | PatchServicesDHCPServerStaticMappingEndpointResponse500
    | PatchServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerStaticMappingEndpointResponse400 | PatchServicesDHCPServerStaticMappingEndpointResponse401 | PatchServicesDHCPServerStaticMappingEndpointResponse403 | PatchServicesDHCPServerStaticMappingEndpointResponse404 | PatchServicesDHCPServerStaticMappingEndpointResponse405 | PatchServicesDHCPServerStaticMappingEndpointResponse406 | PatchServicesDHCPServerStaticMappingEndpointResponse409 | PatchServicesDHCPServerStaticMappingEndpointResponse415 | PatchServicesDHCPServerStaticMappingEndpointResponse422 | PatchServicesDHCPServerStaticMappingEndpointResponse424 | PatchServicesDHCPServerStaticMappingEndpointResponse500 | PatchServicesDHCPServerStaticMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
