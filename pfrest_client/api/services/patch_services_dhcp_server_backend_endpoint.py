from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dhcp_server_backend_endpoint_data_body import (
    PatchServicesDHCPServerBackendEndpointDataBody,
)
from ...models.patch_services_dhcp_server_backend_endpoint_json_body import (
    PatchServicesDHCPServerBackendEndpointJsonBody,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_400 import (
    PatchServicesDHCPServerBackendEndpointResponse400,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_401 import (
    PatchServicesDHCPServerBackendEndpointResponse401,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_403 import (
    PatchServicesDHCPServerBackendEndpointResponse403,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_404 import (
    PatchServicesDHCPServerBackendEndpointResponse404,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_405 import (
    PatchServicesDHCPServerBackendEndpointResponse405,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_406 import (
    PatchServicesDHCPServerBackendEndpointResponse406,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_409 import (
    PatchServicesDHCPServerBackendEndpointResponse409,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_415 import (
    PatchServicesDHCPServerBackendEndpointResponse415,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_422 import (
    PatchServicesDHCPServerBackendEndpointResponse422,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_424 import (
    PatchServicesDHCPServerBackendEndpointResponse424,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_500 import (
    PatchServicesDHCPServerBackendEndpointResponse500,
)
from ...models.patch_services_dhcp_server_backend_endpoint_response_503 import (
    PatchServicesDHCPServerBackendEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDHCPServerBackendEndpointJsonBody
    | PatchServicesDHCPServerBackendEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dhcp_server/backend",
    }

    if isinstance(body, PatchServicesDHCPServerBackendEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDHCPServerBackendEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDHCPServerBackendEndpointResponse400
    | PatchServicesDHCPServerBackendEndpointResponse401
    | PatchServicesDHCPServerBackendEndpointResponse403
    | PatchServicesDHCPServerBackendEndpointResponse404
    | PatchServicesDHCPServerBackendEndpointResponse405
    | PatchServicesDHCPServerBackendEndpointResponse406
    | PatchServicesDHCPServerBackendEndpointResponse409
    | PatchServicesDHCPServerBackendEndpointResponse415
    | PatchServicesDHCPServerBackendEndpointResponse422
    | PatchServicesDHCPServerBackendEndpointResponse424
    | PatchServicesDHCPServerBackendEndpointResponse500
    | PatchServicesDHCPServerBackendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDHCPServerBackendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDHCPServerBackendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDHCPServerBackendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDHCPServerBackendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDHCPServerBackendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDHCPServerBackendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDHCPServerBackendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDHCPServerBackendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDHCPServerBackendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDHCPServerBackendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDHCPServerBackendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDHCPServerBackendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDHCPServerBackendEndpointResponse400
    | PatchServicesDHCPServerBackendEndpointResponse401
    | PatchServicesDHCPServerBackendEndpointResponse403
    | PatchServicesDHCPServerBackendEndpointResponse404
    | PatchServicesDHCPServerBackendEndpointResponse405
    | PatchServicesDHCPServerBackendEndpointResponse406
    | PatchServicesDHCPServerBackendEndpointResponse409
    | PatchServicesDHCPServerBackendEndpointResponse415
    | PatchServicesDHCPServerBackendEndpointResponse422
    | PatchServicesDHCPServerBackendEndpointResponse424
    | PatchServicesDHCPServerBackendEndpointResponse500
    | PatchServicesDHCPServerBackendEndpointResponse503
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
    body: PatchServicesDHCPServerBackendEndpointJsonBody
    | PatchServicesDHCPServerBackendEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerBackendEndpointResponse400
    | PatchServicesDHCPServerBackendEndpointResponse401
    | PatchServicesDHCPServerBackendEndpointResponse403
    | PatchServicesDHCPServerBackendEndpointResponse404
    | PatchServicesDHCPServerBackendEndpointResponse405
    | PatchServicesDHCPServerBackendEndpointResponse406
    | PatchServicesDHCPServerBackendEndpointResponse409
    | PatchServicesDHCPServerBackendEndpointResponse415
    | PatchServicesDHCPServerBackendEndpointResponse422
    | PatchServicesDHCPServerBackendEndpointResponse424
    | PatchServicesDHCPServerBackendEndpointResponse500
    | PatchServicesDHCPServerBackendEndpointResponse503
]:
    """<h3>Description:</h3>Select the DHCP Server Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-backend-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerBackendEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerBackendEndpointResponse400 | PatchServicesDHCPServerBackendEndpointResponse401 | PatchServicesDHCPServerBackendEndpointResponse403 | PatchServicesDHCPServerBackendEndpointResponse404 | PatchServicesDHCPServerBackendEndpointResponse405 | PatchServicesDHCPServerBackendEndpointResponse406 | PatchServicesDHCPServerBackendEndpointResponse409 | PatchServicesDHCPServerBackendEndpointResponse415 | PatchServicesDHCPServerBackendEndpointResponse422 | PatchServicesDHCPServerBackendEndpointResponse424 | PatchServicesDHCPServerBackendEndpointResponse500 | PatchServicesDHCPServerBackendEndpointResponse503]
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
    body: PatchServicesDHCPServerBackendEndpointJsonBody
    | PatchServicesDHCPServerBackendEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerBackendEndpointResponse400
    | PatchServicesDHCPServerBackendEndpointResponse401
    | PatchServicesDHCPServerBackendEndpointResponse403
    | PatchServicesDHCPServerBackendEndpointResponse404
    | PatchServicesDHCPServerBackendEndpointResponse405
    | PatchServicesDHCPServerBackendEndpointResponse406
    | PatchServicesDHCPServerBackendEndpointResponse409
    | PatchServicesDHCPServerBackendEndpointResponse415
    | PatchServicesDHCPServerBackendEndpointResponse422
    | PatchServicesDHCPServerBackendEndpointResponse424
    | PatchServicesDHCPServerBackendEndpointResponse500
    | PatchServicesDHCPServerBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Select the DHCP Server Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-backend-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerBackendEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerBackendEndpointResponse400 | PatchServicesDHCPServerBackendEndpointResponse401 | PatchServicesDHCPServerBackendEndpointResponse403 | PatchServicesDHCPServerBackendEndpointResponse404 | PatchServicesDHCPServerBackendEndpointResponse405 | PatchServicesDHCPServerBackendEndpointResponse406 | PatchServicesDHCPServerBackendEndpointResponse409 | PatchServicesDHCPServerBackendEndpointResponse415 | PatchServicesDHCPServerBackendEndpointResponse422 | PatchServicesDHCPServerBackendEndpointResponse424 | PatchServicesDHCPServerBackendEndpointResponse500 | PatchServicesDHCPServerBackendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerBackendEndpointJsonBody
    | PatchServicesDHCPServerBackendEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerBackendEndpointResponse400
    | PatchServicesDHCPServerBackendEndpointResponse401
    | PatchServicesDHCPServerBackendEndpointResponse403
    | PatchServicesDHCPServerBackendEndpointResponse404
    | PatchServicesDHCPServerBackendEndpointResponse405
    | PatchServicesDHCPServerBackendEndpointResponse406
    | PatchServicesDHCPServerBackendEndpointResponse409
    | PatchServicesDHCPServerBackendEndpointResponse415
    | PatchServicesDHCPServerBackendEndpointResponse422
    | PatchServicesDHCPServerBackendEndpointResponse424
    | PatchServicesDHCPServerBackendEndpointResponse500
    | PatchServicesDHCPServerBackendEndpointResponse503
]:
    """<h3>Description:</h3>Select the DHCP Server Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-backend-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerBackendEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerBackendEndpointResponse400 | PatchServicesDHCPServerBackendEndpointResponse401 | PatchServicesDHCPServerBackendEndpointResponse403 | PatchServicesDHCPServerBackendEndpointResponse404 | PatchServicesDHCPServerBackendEndpointResponse405 | PatchServicesDHCPServerBackendEndpointResponse406 | PatchServicesDHCPServerBackendEndpointResponse409 | PatchServicesDHCPServerBackendEndpointResponse415 | PatchServicesDHCPServerBackendEndpointResponse422 | PatchServicesDHCPServerBackendEndpointResponse424 | PatchServicesDHCPServerBackendEndpointResponse500 | PatchServicesDHCPServerBackendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerBackendEndpointJsonBody
    | PatchServicesDHCPServerBackendEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerBackendEndpointResponse400
    | PatchServicesDHCPServerBackendEndpointResponse401
    | PatchServicesDHCPServerBackendEndpointResponse403
    | PatchServicesDHCPServerBackendEndpointResponse404
    | PatchServicesDHCPServerBackendEndpointResponse405
    | PatchServicesDHCPServerBackendEndpointResponse406
    | PatchServicesDHCPServerBackendEndpointResponse409
    | PatchServicesDHCPServerBackendEndpointResponse415
    | PatchServicesDHCPServerBackendEndpointResponse422
    | PatchServicesDHCPServerBackendEndpointResponse424
    | PatchServicesDHCPServerBackendEndpointResponse500
    | PatchServicesDHCPServerBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Select the DHCP Server Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-backend-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPServerBackendEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerBackendEndpointResponse400 | PatchServicesDHCPServerBackendEndpointResponse401 | PatchServicesDHCPServerBackendEndpointResponse403 | PatchServicesDHCPServerBackendEndpointResponse404 | PatchServicesDHCPServerBackendEndpointResponse405 | PatchServicesDHCPServerBackendEndpointResponse406 | PatchServicesDHCPServerBackendEndpointResponse409 | PatchServicesDHCPServerBackendEndpointResponse415 | PatchServicesDHCPServerBackendEndpointResponse422 | PatchServicesDHCPServerBackendEndpointResponse424 | PatchServicesDHCPServerBackendEndpointResponse500 | PatchServicesDHCPServerBackendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
