from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_400 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse400,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_401 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse401,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_403 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse403,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_404 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse404,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_405 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse405,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_406 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse406,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_409 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse409,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_415 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse415,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_422 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse422,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_424 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse424,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_500 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse500,
)
from ...models.delete_services_dhcp_server_custom_option_endpoint_response_503 import (
    DeleteServicesDHCPServerCustomOptionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/dhcp_server/custom_option",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDHCPServerCustomOptionEndpointResponse400
    | DeleteServicesDHCPServerCustomOptionEndpointResponse401
    | DeleteServicesDHCPServerCustomOptionEndpointResponse403
    | DeleteServicesDHCPServerCustomOptionEndpointResponse404
    | DeleteServicesDHCPServerCustomOptionEndpointResponse405
    | DeleteServicesDHCPServerCustomOptionEndpointResponse406
    | DeleteServicesDHCPServerCustomOptionEndpointResponse409
    | DeleteServicesDHCPServerCustomOptionEndpointResponse415
    | DeleteServicesDHCPServerCustomOptionEndpointResponse422
    | DeleteServicesDHCPServerCustomOptionEndpointResponse424
    | DeleteServicesDHCPServerCustomOptionEndpointResponse500
    | DeleteServicesDHCPServerCustomOptionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDHCPServerCustomOptionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDHCPServerCustomOptionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDHCPServerCustomOptionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDHCPServerCustomOptionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDHCPServerCustomOptionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDHCPServerCustomOptionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDHCPServerCustomOptionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDHCPServerCustomOptionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDHCPServerCustomOptionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDHCPServerCustomOptionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDHCPServerCustomOptionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDHCPServerCustomOptionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDHCPServerCustomOptionEndpointResponse400
    | DeleteServicesDHCPServerCustomOptionEndpointResponse401
    | DeleteServicesDHCPServerCustomOptionEndpointResponse403
    | DeleteServicesDHCPServerCustomOptionEndpointResponse404
    | DeleteServicesDHCPServerCustomOptionEndpointResponse405
    | DeleteServicesDHCPServerCustomOptionEndpointResponse406
    | DeleteServicesDHCPServerCustomOptionEndpointResponse409
    | DeleteServicesDHCPServerCustomOptionEndpointResponse415
    | DeleteServicesDHCPServerCustomOptionEndpointResponse422
    | DeleteServicesDHCPServerCustomOptionEndpointResponse424
    | DeleteServicesDHCPServerCustomOptionEndpointResponse500
    | DeleteServicesDHCPServerCustomOptionEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDHCPServerCustomOptionEndpointResponse400
    | DeleteServicesDHCPServerCustomOptionEndpointResponse401
    | DeleteServicesDHCPServerCustomOptionEndpointResponse403
    | DeleteServicesDHCPServerCustomOptionEndpointResponse404
    | DeleteServicesDHCPServerCustomOptionEndpointResponse405
    | DeleteServicesDHCPServerCustomOptionEndpointResponse406
    | DeleteServicesDHCPServerCustomOptionEndpointResponse409
    | DeleteServicesDHCPServerCustomOptionEndpointResponse415
    | DeleteServicesDHCPServerCustomOptionEndpointResponse422
    | DeleteServicesDHCPServerCustomOptionEndpointResponse424
    | DeleteServicesDHCPServerCustomOptionEndpointResponse500
    | DeleteServicesDHCPServerCustomOptionEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDHCPServerCustomOptionEndpointResponse400 | DeleteServicesDHCPServerCustomOptionEndpointResponse401 | DeleteServicesDHCPServerCustomOptionEndpointResponse403 | DeleteServicesDHCPServerCustomOptionEndpointResponse404 | DeleteServicesDHCPServerCustomOptionEndpointResponse405 | DeleteServicesDHCPServerCustomOptionEndpointResponse406 | DeleteServicesDHCPServerCustomOptionEndpointResponse409 | DeleteServicesDHCPServerCustomOptionEndpointResponse415 | DeleteServicesDHCPServerCustomOptionEndpointResponse422 | DeleteServicesDHCPServerCustomOptionEndpointResponse424 | DeleteServicesDHCPServerCustomOptionEndpointResponse500 | DeleteServicesDHCPServerCustomOptionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
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
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDHCPServerCustomOptionEndpointResponse400
    | DeleteServicesDHCPServerCustomOptionEndpointResponse401
    | DeleteServicesDHCPServerCustomOptionEndpointResponse403
    | DeleteServicesDHCPServerCustomOptionEndpointResponse404
    | DeleteServicesDHCPServerCustomOptionEndpointResponse405
    | DeleteServicesDHCPServerCustomOptionEndpointResponse406
    | DeleteServicesDHCPServerCustomOptionEndpointResponse409
    | DeleteServicesDHCPServerCustomOptionEndpointResponse415
    | DeleteServicesDHCPServerCustomOptionEndpointResponse422
    | DeleteServicesDHCPServerCustomOptionEndpointResponse424
    | DeleteServicesDHCPServerCustomOptionEndpointResponse500
    | DeleteServicesDHCPServerCustomOptionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDHCPServerCustomOptionEndpointResponse400 | DeleteServicesDHCPServerCustomOptionEndpointResponse401 | DeleteServicesDHCPServerCustomOptionEndpointResponse403 | DeleteServicesDHCPServerCustomOptionEndpointResponse404 | DeleteServicesDHCPServerCustomOptionEndpointResponse405 | DeleteServicesDHCPServerCustomOptionEndpointResponse406 | DeleteServicesDHCPServerCustomOptionEndpointResponse409 | DeleteServicesDHCPServerCustomOptionEndpointResponse415 | DeleteServicesDHCPServerCustomOptionEndpointResponse422 | DeleteServicesDHCPServerCustomOptionEndpointResponse424 | DeleteServicesDHCPServerCustomOptionEndpointResponse500 | DeleteServicesDHCPServerCustomOptionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDHCPServerCustomOptionEndpointResponse400
    | DeleteServicesDHCPServerCustomOptionEndpointResponse401
    | DeleteServicesDHCPServerCustomOptionEndpointResponse403
    | DeleteServicesDHCPServerCustomOptionEndpointResponse404
    | DeleteServicesDHCPServerCustomOptionEndpointResponse405
    | DeleteServicesDHCPServerCustomOptionEndpointResponse406
    | DeleteServicesDHCPServerCustomOptionEndpointResponse409
    | DeleteServicesDHCPServerCustomOptionEndpointResponse415
    | DeleteServicesDHCPServerCustomOptionEndpointResponse422
    | DeleteServicesDHCPServerCustomOptionEndpointResponse424
    | DeleteServicesDHCPServerCustomOptionEndpointResponse500
    | DeleteServicesDHCPServerCustomOptionEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDHCPServerCustomOptionEndpointResponse400 | DeleteServicesDHCPServerCustomOptionEndpointResponse401 | DeleteServicesDHCPServerCustomOptionEndpointResponse403 | DeleteServicesDHCPServerCustomOptionEndpointResponse404 | DeleteServicesDHCPServerCustomOptionEndpointResponse405 | DeleteServicesDHCPServerCustomOptionEndpointResponse406 | DeleteServicesDHCPServerCustomOptionEndpointResponse409 | DeleteServicesDHCPServerCustomOptionEndpointResponse415 | DeleteServicesDHCPServerCustomOptionEndpointResponse422 | DeleteServicesDHCPServerCustomOptionEndpointResponse424 | DeleteServicesDHCPServerCustomOptionEndpointResponse500 | DeleteServicesDHCPServerCustomOptionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDHCPServerCustomOptionEndpointResponse400
    | DeleteServicesDHCPServerCustomOptionEndpointResponse401
    | DeleteServicesDHCPServerCustomOptionEndpointResponse403
    | DeleteServicesDHCPServerCustomOptionEndpointResponse404
    | DeleteServicesDHCPServerCustomOptionEndpointResponse405
    | DeleteServicesDHCPServerCustomOptionEndpointResponse406
    | DeleteServicesDHCPServerCustomOptionEndpointResponse409
    | DeleteServicesDHCPServerCustomOptionEndpointResponse415
    | DeleteServicesDHCPServerCustomOptionEndpointResponse422
    | DeleteServicesDHCPServerCustomOptionEndpointResponse424
    | DeleteServicesDHCPServerCustomOptionEndpointResponse500
    | DeleteServicesDHCPServerCustomOptionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DHCP Server Custom Option.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerCustomOption<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-custom-option-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDHCPServerCustomOptionEndpointResponse400 | DeleteServicesDHCPServerCustomOptionEndpointResponse401 | DeleteServicesDHCPServerCustomOptionEndpointResponse403 | DeleteServicesDHCPServerCustomOptionEndpointResponse404 | DeleteServicesDHCPServerCustomOptionEndpointResponse405 | DeleteServicesDHCPServerCustomOptionEndpointResponse406 | DeleteServicesDHCPServerCustomOptionEndpointResponse409 | DeleteServicesDHCPServerCustomOptionEndpointResponse415 | DeleteServicesDHCPServerCustomOptionEndpointResponse422 | DeleteServicesDHCPServerCustomOptionEndpointResponse424 | DeleteServicesDHCPServerCustomOptionEndpointResponse500 | DeleteServicesDHCPServerCustomOptionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
            apply=apply,
        )
    ).parsed
