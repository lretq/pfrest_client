from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dhcp_server_custom_option_endpoint_data_body import (
    PatchServicesDHCPServerCustomOptionEndpointDataBody,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_json_body import (
    PatchServicesDHCPServerCustomOptionEndpointJsonBody,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_400 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse400,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_401 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse401,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_403 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse403,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_404 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse404,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_405 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse405,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_406 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse406,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_409 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse409,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_415 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse415,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_422 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse422,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_424 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse424,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_500 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse500,
)
from ...models.patch_services_dhcp_server_custom_option_endpoint_response_503 import (
    PatchServicesDHCPServerCustomOptionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDHCPServerCustomOptionEndpointJsonBody
    | PatchServicesDHCPServerCustomOptionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dhcp_server/custom_option",
    }

    if isinstance(body, PatchServicesDHCPServerCustomOptionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDHCPServerCustomOptionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDHCPServerCustomOptionEndpointResponse400
    | PatchServicesDHCPServerCustomOptionEndpointResponse401
    | PatchServicesDHCPServerCustomOptionEndpointResponse403
    | PatchServicesDHCPServerCustomOptionEndpointResponse404
    | PatchServicesDHCPServerCustomOptionEndpointResponse405
    | PatchServicesDHCPServerCustomOptionEndpointResponse406
    | PatchServicesDHCPServerCustomOptionEndpointResponse409
    | PatchServicesDHCPServerCustomOptionEndpointResponse415
    | PatchServicesDHCPServerCustomOptionEndpointResponse422
    | PatchServicesDHCPServerCustomOptionEndpointResponse424
    | PatchServicesDHCPServerCustomOptionEndpointResponse500
    | PatchServicesDHCPServerCustomOptionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDHCPServerCustomOptionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDHCPServerCustomOptionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDHCPServerCustomOptionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDHCPServerCustomOptionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDHCPServerCustomOptionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDHCPServerCustomOptionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDHCPServerCustomOptionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDHCPServerCustomOptionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDHCPServerCustomOptionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDHCPServerCustomOptionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDHCPServerCustomOptionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDHCPServerCustomOptionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDHCPServerCustomOptionEndpointResponse400
    | PatchServicesDHCPServerCustomOptionEndpointResponse401
    | PatchServicesDHCPServerCustomOptionEndpointResponse403
    | PatchServicesDHCPServerCustomOptionEndpointResponse404
    | PatchServicesDHCPServerCustomOptionEndpointResponse405
    | PatchServicesDHCPServerCustomOptionEndpointResponse406
    | PatchServicesDHCPServerCustomOptionEndpointResponse409
    | PatchServicesDHCPServerCustomOptionEndpointResponse415
    | PatchServicesDHCPServerCustomOptionEndpointResponse422
    | PatchServicesDHCPServerCustomOptionEndpointResponse424
    | PatchServicesDHCPServerCustomOptionEndpointResponse500
    | PatchServicesDHCPServerCustomOptionEndpointResponse503
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
    body: PatchServicesDHCPServerCustomOptionEndpointJsonBody
    | PatchServicesDHCPServerCustomOptionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerCustomOptionEndpointResponse400
    | PatchServicesDHCPServerCustomOptionEndpointResponse401
    | PatchServicesDHCPServerCustomOptionEndpointResponse403
    | PatchServicesDHCPServerCustomOptionEndpointResponse404
    | PatchServicesDHCPServerCustomOptionEndpointResponse405
    | PatchServicesDHCPServerCustomOptionEndpointResponse406
    | PatchServicesDHCPServerCustomOptionEndpointResponse409
    | PatchServicesDHCPServerCustomOptionEndpointResponse415
    | PatchServicesDHCPServerCustomOptionEndpointResponse422
    | PatchServicesDHCPServerCustomOptionEndpointResponse424
    | PatchServicesDHCPServerCustomOptionEndpointResponse500
    | PatchServicesDHCPServerCustomOptionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerCustomOptionEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerCustomOptionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerCustomOptionEndpointResponse400 | PatchServicesDHCPServerCustomOptionEndpointResponse401 | PatchServicesDHCPServerCustomOptionEndpointResponse403 | PatchServicesDHCPServerCustomOptionEndpointResponse404 | PatchServicesDHCPServerCustomOptionEndpointResponse405 | PatchServicesDHCPServerCustomOptionEndpointResponse406 | PatchServicesDHCPServerCustomOptionEndpointResponse409 | PatchServicesDHCPServerCustomOptionEndpointResponse415 | PatchServicesDHCPServerCustomOptionEndpointResponse422 | PatchServicesDHCPServerCustomOptionEndpointResponse424 | PatchServicesDHCPServerCustomOptionEndpointResponse500 | PatchServicesDHCPServerCustomOptionEndpointResponse503]
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
    body: PatchServicesDHCPServerCustomOptionEndpointJsonBody
    | PatchServicesDHCPServerCustomOptionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerCustomOptionEndpointResponse400
    | PatchServicesDHCPServerCustomOptionEndpointResponse401
    | PatchServicesDHCPServerCustomOptionEndpointResponse403
    | PatchServicesDHCPServerCustomOptionEndpointResponse404
    | PatchServicesDHCPServerCustomOptionEndpointResponse405
    | PatchServicesDHCPServerCustomOptionEndpointResponse406
    | PatchServicesDHCPServerCustomOptionEndpointResponse409
    | PatchServicesDHCPServerCustomOptionEndpointResponse415
    | PatchServicesDHCPServerCustomOptionEndpointResponse422
    | PatchServicesDHCPServerCustomOptionEndpointResponse424
    | PatchServicesDHCPServerCustomOptionEndpointResponse500
    | PatchServicesDHCPServerCustomOptionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerCustomOptionEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerCustomOptionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerCustomOptionEndpointResponse400 | PatchServicesDHCPServerCustomOptionEndpointResponse401 | PatchServicesDHCPServerCustomOptionEndpointResponse403 | PatchServicesDHCPServerCustomOptionEndpointResponse404 | PatchServicesDHCPServerCustomOptionEndpointResponse405 | PatchServicesDHCPServerCustomOptionEndpointResponse406 | PatchServicesDHCPServerCustomOptionEndpointResponse409 | PatchServicesDHCPServerCustomOptionEndpointResponse415 | PatchServicesDHCPServerCustomOptionEndpointResponse422 | PatchServicesDHCPServerCustomOptionEndpointResponse424 | PatchServicesDHCPServerCustomOptionEndpointResponse500 | PatchServicesDHCPServerCustomOptionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerCustomOptionEndpointJsonBody
    | PatchServicesDHCPServerCustomOptionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesDHCPServerCustomOptionEndpointResponse400
    | PatchServicesDHCPServerCustomOptionEndpointResponse401
    | PatchServicesDHCPServerCustomOptionEndpointResponse403
    | PatchServicesDHCPServerCustomOptionEndpointResponse404
    | PatchServicesDHCPServerCustomOptionEndpointResponse405
    | PatchServicesDHCPServerCustomOptionEndpointResponse406
    | PatchServicesDHCPServerCustomOptionEndpointResponse409
    | PatchServicesDHCPServerCustomOptionEndpointResponse415
    | PatchServicesDHCPServerCustomOptionEndpointResponse422
    | PatchServicesDHCPServerCustomOptionEndpointResponse424
    | PatchServicesDHCPServerCustomOptionEndpointResponse500
    | PatchServicesDHCPServerCustomOptionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerCustomOptionEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerCustomOptionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPServerCustomOptionEndpointResponse400 | PatchServicesDHCPServerCustomOptionEndpointResponse401 | PatchServicesDHCPServerCustomOptionEndpointResponse403 | PatchServicesDHCPServerCustomOptionEndpointResponse404 | PatchServicesDHCPServerCustomOptionEndpointResponse405 | PatchServicesDHCPServerCustomOptionEndpointResponse406 | PatchServicesDHCPServerCustomOptionEndpointResponse409 | PatchServicesDHCPServerCustomOptionEndpointResponse415 | PatchServicesDHCPServerCustomOptionEndpointResponse422 | PatchServicesDHCPServerCustomOptionEndpointResponse424 | PatchServicesDHCPServerCustomOptionEndpointResponse500 | PatchServicesDHCPServerCustomOptionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPServerCustomOptionEndpointJsonBody
    | PatchServicesDHCPServerCustomOptionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesDHCPServerCustomOptionEndpointResponse400
    | PatchServicesDHCPServerCustomOptionEndpointResponse401
    | PatchServicesDHCPServerCustomOptionEndpointResponse403
    | PatchServicesDHCPServerCustomOptionEndpointResponse404
    | PatchServicesDHCPServerCustomOptionEndpointResponse405
    | PatchServicesDHCPServerCustomOptionEndpointResponse406
    | PatchServicesDHCPServerCustomOptionEndpointResponse409
    | PatchServicesDHCPServerCustomOptionEndpointResponse415
    | PatchServicesDHCPServerCustomOptionEndpointResponse422
    | PatchServicesDHCPServerCustomOptionEndpointResponse424
    | PatchServicesDHCPServerCustomOptionEndpointResponse500
    | PatchServicesDHCPServerCustomOptionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesDHCPServerCustomOptionEndpointJsonBody | Unset):
        body (PatchServicesDHCPServerCustomOptionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPServerCustomOptionEndpointResponse400 | PatchServicesDHCPServerCustomOptionEndpointResponse401 | PatchServicesDHCPServerCustomOptionEndpointResponse403 | PatchServicesDHCPServerCustomOptionEndpointResponse404 | PatchServicesDHCPServerCustomOptionEndpointResponse405 | PatchServicesDHCPServerCustomOptionEndpointResponse406 | PatchServicesDHCPServerCustomOptionEndpointResponse409 | PatchServicesDHCPServerCustomOptionEndpointResponse415 | PatchServicesDHCPServerCustomOptionEndpointResponse422 | PatchServicesDHCPServerCustomOptionEndpointResponse424 | PatchServicesDHCPServerCustomOptionEndpointResponse500 | PatchServicesDHCPServerCustomOptionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
