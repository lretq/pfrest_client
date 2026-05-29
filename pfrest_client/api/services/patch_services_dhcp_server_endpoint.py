from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dhcp_server_endpoint_data_body import PatchServicesDHCPServerEndpointDataBody
from ...models.patch_services_dhcp_server_endpoint_json_body import PatchServicesDHCPServerEndpointJsonBody
from ...models.patch_services_dhcp_server_endpoint_response_400 import PatchServicesDHCPServerEndpointResponse400
from ...models.patch_services_dhcp_server_endpoint_response_401 import PatchServicesDHCPServerEndpointResponse401
from ...models.patch_services_dhcp_server_endpoint_response_403 import PatchServicesDHCPServerEndpointResponse403
from ...models.patch_services_dhcp_server_endpoint_response_404 import PatchServicesDHCPServerEndpointResponse404
from ...models.patch_services_dhcp_server_endpoint_response_405 import PatchServicesDHCPServerEndpointResponse405
from ...models.patch_services_dhcp_server_endpoint_response_406 import PatchServicesDHCPServerEndpointResponse406
from ...models.patch_services_dhcp_server_endpoint_response_409 import PatchServicesDHCPServerEndpointResponse409
from ...models.patch_services_dhcp_server_endpoint_response_415 import PatchServicesDHCPServerEndpointResponse415
from ...models.patch_services_dhcp_server_endpoint_response_422 import PatchServicesDHCPServerEndpointResponse422
from ...models.patch_services_dhcp_server_endpoint_response_424 import PatchServicesDHCPServerEndpointResponse424
from ...models.patch_services_dhcp_server_endpoint_response_500 import PatchServicesDHCPServerEndpointResponse500
from ...models.patch_services_dhcp_server_endpoint_response_503 import PatchServicesDHCPServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDHCPServerEndpointJsonBody | PatchServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dhcp_server",
    }

    if isinstance(body, PatchServicesDHCPServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDHCPServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDHCPServerEndpointResponse400
    | PatchServicesDHCPServerEndpointResponse401
    | PatchServicesDHCPServerEndpointResponse403
    | PatchServicesDHCPServerEndpointResponse404
    | PatchServicesDHCPServerEndpointResponse405
    | PatchServicesDHCPServerEndpointResponse406
    | PatchServicesDHCPServerEndpointResponse409
    | PatchServicesDHCPServerEndpointResponse415
    | PatchServicesDHCPServerEndpointResponse422
    | PatchServicesDHCPServerEndpointResponse424
    | PatchServicesDHCPServerEndpointResponse500
    | PatchServicesDHCPServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDHCPServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDHCPServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDHCPServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDHCPServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDHCPServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDHCPServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDHCPServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDHCPServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDHCPServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDHCPServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDHCPServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDHCPServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDHCPServerEndpointResponse400
    | PatchServicesDHCPServerEndpointResponse401
    | PatchServicesDHCPServerEndpointResponse403
    | PatchServicesDHCPServerEndpointResponse404
    | PatchServicesDHCPServerEndpointResponse405
    | PatchServicesDHCPServerEndpointResponse406
    | PatchServicesDHCPServerEndpointResponse409
    | PatchServicesDHCPServerEndpointResponse415
    | PatchServicesDHCPServerEndpointResponse422
    | PatchServicesDHCPServerEndpointResponse424
    | PatchServicesDHCPServerEndpointResponse500
    | PatchServicesDHCPServerEndpointResponse503
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
    body: PatchServicesDHCPServerEndpointJsonBody | PatchServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerEndpointResponse400
    | PatchServicesDHCPServerEndpointResponse401
    | PatchServicesDHCPServerEndpointResponse403
    | PatchServicesDHCPServerEndpointResponse404
    | PatchServicesDHCPServerEndpointResponse405
    | PatchServicesDHCPServerEndpointResponse406
    | PatchServicesDHCPServerEndpointResponse409
    | PatchServicesDHCPServerEndpointResponse415
    | PatchServicesDHCPServerEndpointResponse422
    | PatchServicesDHCPServerEndpointResponse424
    | PatchServicesDHCPServerEndpointResponse500
    | PatchServicesDHCPServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerEndpointResponse400 | PatchServicesDHCPServerEndpointResponse401 | PatchServicesDHCPServerEndpointResponse403 | PatchServicesDHCPServerEndpointResponse404 | PatchServicesDHCPServerEndpointResponse405 | PatchServicesDHCPServerEndpointResponse406 | PatchServicesDHCPServerEndpointResponse409 | PatchServicesDHCPServerEndpointResponse415 | PatchServicesDHCPServerEndpointResponse422 | PatchServicesDHCPServerEndpointResponse424 | PatchServicesDHCPServerEndpointResponse500 | PatchServicesDHCPServerEndpointResponse503]
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
    body: PatchServicesDHCPServerEndpointJsonBody | PatchServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesDHCPServerEndpointResponse400
    | PatchServicesDHCPServerEndpointResponse401
    | PatchServicesDHCPServerEndpointResponse403
    | PatchServicesDHCPServerEndpointResponse404
    | PatchServicesDHCPServerEndpointResponse405
    | PatchServicesDHCPServerEndpointResponse406
    | PatchServicesDHCPServerEndpointResponse409
    | PatchServicesDHCPServerEndpointResponse415
    | PatchServicesDHCPServerEndpointResponse422
    | PatchServicesDHCPServerEndpointResponse424
    | PatchServicesDHCPServerEndpointResponse500
    | PatchServicesDHCPServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerEndpointResponse400 | PatchServicesDHCPServerEndpointResponse401 | PatchServicesDHCPServerEndpointResponse403 | PatchServicesDHCPServerEndpointResponse404 | PatchServicesDHCPServerEndpointResponse405 | PatchServicesDHCPServerEndpointResponse406 | PatchServicesDHCPServerEndpointResponse409 | PatchServicesDHCPServerEndpointResponse415 | PatchServicesDHCPServerEndpointResponse422 | PatchServicesDHCPServerEndpointResponse424 | PatchServicesDHCPServerEndpointResponse500 | PatchServicesDHCPServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerEndpointJsonBody | PatchServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerEndpointResponse400
    | PatchServicesDHCPServerEndpointResponse401
    | PatchServicesDHCPServerEndpointResponse403
    | PatchServicesDHCPServerEndpointResponse404
    | PatchServicesDHCPServerEndpointResponse405
    | PatchServicesDHCPServerEndpointResponse406
    | PatchServicesDHCPServerEndpointResponse409
    | PatchServicesDHCPServerEndpointResponse415
    | PatchServicesDHCPServerEndpointResponse422
    | PatchServicesDHCPServerEndpointResponse424
    | PatchServicesDHCPServerEndpointResponse500
    | PatchServicesDHCPServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerEndpointResponse400 | PatchServicesDHCPServerEndpointResponse401 | PatchServicesDHCPServerEndpointResponse403 | PatchServicesDHCPServerEndpointResponse404 | PatchServicesDHCPServerEndpointResponse405 | PatchServicesDHCPServerEndpointResponse406 | PatchServicesDHCPServerEndpointResponse409 | PatchServicesDHCPServerEndpointResponse415 | PatchServicesDHCPServerEndpointResponse422 | PatchServicesDHCPServerEndpointResponse424 | PatchServicesDHCPServerEndpointResponse500 | PatchServicesDHCPServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerEndpointJsonBody | PatchServicesDHCPServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesDHCPServerEndpointResponse400
    | PatchServicesDHCPServerEndpointResponse401
    | PatchServicesDHCPServerEndpointResponse403
    | PatchServicesDHCPServerEndpointResponse404
    | PatchServicesDHCPServerEndpointResponse405
    | PatchServicesDHCPServerEndpointResponse406
    | PatchServicesDHCPServerEndpointResponse409
    | PatchServicesDHCPServerEndpointResponse415
    | PatchServicesDHCPServerEndpointResponse422
    | PatchServicesDHCPServerEndpointResponse424
    | PatchServicesDHCPServerEndpointResponse500
    | PatchServicesDHCPServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerEndpointResponse400 | PatchServicesDHCPServerEndpointResponse401 | PatchServicesDHCPServerEndpointResponse403 | PatchServicesDHCPServerEndpointResponse404 | PatchServicesDHCPServerEndpointResponse405 | PatchServicesDHCPServerEndpointResponse406 | PatchServicesDHCPServerEndpointResponse409 | PatchServicesDHCPServerEndpointResponse415 | PatchServicesDHCPServerEndpointResponse422 | PatchServicesDHCPServerEndpointResponse424 | PatchServicesDHCPServerEndpointResponse500 | PatchServicesDHCPServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
