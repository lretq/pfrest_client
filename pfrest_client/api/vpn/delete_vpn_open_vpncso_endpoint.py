from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_vpn_open_vpncso_endpoint_response_400 import DeleteVPNOpenVPNCSOEndpointResponse400
from ...models.delete_vpn_open_vpncso_endpoint_response_401 import DeleteVPNOpenVPNCSOEndpointResponse401
from ...models.delete_vpn_open_vpncso_endpoint_response_403 import DeleteVPNOpenVPNCSOEndpointResponse403
from ...models.delete_vpn_open_vpncso_endpoint_response_404 import DeleteVPNOpenVPNCSOEndpointResponse404
from ...models.delete_vpn_open_vpncso_endpoint_response_405 import DeleteVPNOpenVPNCSOEndpointResponse405
from ...models.delete_vpn_open_vpncso_endpoint_response_406 import DeleteVPNOpenVPNCSOEndpointResponse406
from ...models.delete_vpn_open_vpncso_endpoint_response_409 import DeleteVPNOpenVPNCSOEndpointResponse409
from ...models.delete_vpn_open_vpncso_endpoint_response_415 import DeleteVPNOpenVPNCSOEndpointResponse415
from ...models.delete_vpn_open_vpncso_endpoint_response_422 import DeleteVPNOpenVPNCSOEndpointResponse422
from ...models.delete_vpn_open_vpncso_endpoint_response_424 import DeleteVPNOpenVPNCSOEndpointResponse424
from ...models.delete_vpn_open_vpncso_endpoint_response_500 import DeleteVPNOpenVPNCSOEndpointResponse500
from ...models.delete_vpn_open_vpncso_endpoint_response_503 import DeleteVPNOpenVPNCSOEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/vpn/openvpn/cso",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteVPNOpenVPNCSOEndpointResponse400
    | DeleteVPNOpenVPNCSOEndpointResponse401
    | DeleteVPNOpenVPNCSOEndpointResponse403
    | DeleteVPNOpenVPNCSOEndpointResponse404
    | DeleteVPNOpenVPNCSOEndpointResponse405
    | DeleteVPNOpenVPNCSOEndpointResponse406
    | DeleteVPNOpenVPNCSOEndpointResponse409
    | DeleteVPNOpenVPNCSOEndpointResponse415
    | DeleteVPNOpenVPNCSOEndpointResponse422
    | DeleteVPNOpenVPNCSOEndpointResponse424
    | DeleteVPNOpenVPNCSOEndpointResponse500
    | DeleteVPNOpenVPNCSOEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteVPNOpenVPNCSOEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteVPNOpenVPNCSOEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteVPNOpenVPNCSOEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteVPNOpenVPNCSOEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteVPNOpenVPNCSOEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteVPNOpenVPNCSOEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteVPNOpenVPNCSOEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteVPNOpenVPNCSOEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteVPNOpenVPNCSOEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteVPNOpenVPNCSOEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteVPNOpenVPNCSOEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteVPNOpenVPNCSOEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteVPNOpenVPNCSOEndpointResponse400
    | DeleteVPNOpenVPNCSOEndpointResponse401
    | DeleteVPNOpenVPNCSOEndpointResponse403
    | DeleteVPNOpenVPNCSOEndpointResponse404
    | DeleteVPNOpenVPNCSOEndpointResponse405
    | DeleteVPNOpenVPNCSOEndpointResponse406
    | DeleteVPNOpenVPNCSOEndpointResponse409
    | DeleteVPNOpenVPNCSOEndpointResponse415
    | DeleteVPNOpenVPNCSOEndpointResponse422
    | DeleteVPNOpenVPNCSOEndpointResponse424
    | DeleteVPNOpenVPNCSOEndpointResponse500
    | DeleteVPNOpenVPNCSOEndpointResponse503
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
) -> Response[
    DeleteVPNOpenVPNCSOEndpointResponse400
    | DeleteVPNOpenVPNCSOEndpointResponse401
    | DeleteVPNOpenVPNCSOEndpointResponse403
    | DeleteVPNOpenVPNCSOEndpointResponse404
    | DeleteVPNOpenVPNCSOEndpointResponse405
    | DeleteVPNOpenVPNCSOEndpointResponse406
    | DeleteVPNOpenVPNCSOEndpointResponse409
    | DeleteVPNOpenVPNCSOEndpointResponse415
    | DeleteVPNOpenVPNCSOEndpointResponse422
    | DeleteVPNOpenVPNCSOEndpointResponse424
    | DeleteVPNOpenVPNCSOEndpointResponse500
    | DeleteVPNOpenVPNCSOEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNOpenVPNCSOEndpointResponse400 | DeleteVPNOpenVPNCSOEndpointResponse401 | DeleteVPNOpenVPNCSOEndpointResponse403 | DeleteVPNOpenVPNCSOEndpointResponse404 | DeleteVPNOpenVPNCSOEndpointResponse405 | DeleteVPNOpenVPNCSOEndpointResponse406 | DeleteVPNOpenVPNCSOEndpointResponse409 | DeleteVPNOpenVPNCSOEndpointResponse415 | DeleteVPNOpenVPNCSOEndpointResponse422 | DeleteVPNOpenVPNCSOEndpointResponse424 | DeleteVPNOpenVPNCSOEndpointResponse500 | DeleteVPNOpenVPNCSOEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteVPNOpenVPNCSOEndpointResponse400
    | DeleteVPNOpenVPNCSOEndpointResponse401
    | DeleteVPNOpenVPNCSOEndpointResponse403
    | DeleteVPNOpenVPNCSOEndpointResponse404
    | DeleteVPNOpenVPNCSOEndpointResponse405
    | DeleteVPNOpenVPNCSOEndpointResponse406
    | DeleteVPNOpenVPNCSOEndpointResponse409
    | DeleteVPNOpenVPNCSOEndpointResponse415
    | DeleteVPNOpenVPNCSOEndpointResponse422
    | DeleteVPNOpenVPNCSOEndpointResponse424
    | DeleteVPNOpenVPNCSOEndpointResponse500
    | DeleteVPNOpenVPNCSOEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNOpenVPNCSOEndpointResponse400 | DeleteVPNOpenVPNCSOEndpointResponse401 | DeleteVPNOpenVPNCSOEndpointResponse403 | DeleteVPNOpenVPNCSOEndpointResponse404 | DeleteVPNOpenVPNCSOEndpointResponse405 | DeleteVPNOpenVPNCSOEndpointResponse406 | DeleteVPNOpenVPNCSOEndpointResponse409 | DeleteVPNOpenVPNCSOEndpointResponse415 | DeleteVPNOpenVPNCSOEndpointResponse422 | DeleteVPNOpenVPNCSOEndpointResponse424 | DeleteVPNOpenVPNCSOEndpointResponse500 | DeleteVPNOpenVPNCSOEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteVPNOpenVPNCSOEndpointResponse400
    | DeleteVPNOpenVPNCSOEndpointResponse401
    | DeleteVPNOpenVPNCSOEndpointResponse403
    | DeleteVPNOpenVPNCSOEndpointResponse404
    | DeleteVPNOpenVPNCSOEndpointResponse405
    | DeleteVPNOpenVPNCSOEndpointResponse406
    | DeleteVPNOpenVPNCSOEndpointResponse409
    | DeleteVPNOpenVPNCSOEndpointResponse415
    | DeleteVPNOpenVPNCSOEndpointResponse422
    | DeleteVPNOpenVPNCSOEndpointResponse424
    | DeleteVPNOpenVPNCSOEndpointResponse500
    | DeleteVPNOpenVPNCSOEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNOpenVPNCSOEndpointResponse400 | DeleteVPNOpenVPNCSOEndpointResponse401 | DeleteVPNOpenVPNCSOEndpointResponse403 | DeleteVPNOpenVPNCSOEndpointResponse404 | DeleteVPNOpenVPNCSOEndpointResponse405 | DeleteVPNOpenVPNCSOEndpointResponse406 | DeleteVPNOpenVPNCSOEndpointResponse409 | DeleteVPNOpenVPNCSOEndpointResponse415 | DeleteVPNOpenVPNCSOEndpointResponse422 | DeleteVPNOpenVPNCSOEndpointResponse424 | DeleteVPNOpenVPNCSOEndpointResponse500 | DeleteVPNOpenVPNCSOEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteVPNOpenVPNCSOEndpointResponse400
    | DeleteVPNOpenVPNCSOEndpointResponse401
    | DeleteVPNOpenVPNCSOEndpointResponse403
    | DeleteVPNOpenVPNCSOEndpointResponse404
    | DeleteVPNOpenVPNCSOEndpointResponse405
    | DeleteVPNOpenVPNCSOEndpointResponse406
    | DeleteVPNOpenVPNCSOEndpointResponse409
    | DeleteVPNOpenVPNCSOEndpointResponse415
    | DeleteVPNOpenVPNCSOEndpointResponse422
    | DeleteVPNOpenVPNCSOEndpointResponse424
    | DeleteVPNOpenVPNCSOEndpointResponse500
    | DeleteVPNOpenVPNCSOEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNOpenVPNCSOEndpointResponse400 | DeleteVPNOpenVPNCSOEndpointResponse401 | DeleteVPNOpenVPNCSOEndpointResponse403 | DeleteVPNOpenVPNCSOEndpointResponse404 | DeleteVPNOpenVPNCSOEndpointResponse405 | DeleteVPNOpenVPNCSOEndpointResponse406 | DeleteVPNOpenVPNCSOEndpointResponse409 | DeleteVPNOpenVPNCSOEndpointResponse415 | DeleteVPNOpenVPNCSOEndpointResponse422 | DeleteVPNOpenVPNCSOEndpointResponse424 | DeleteVPNOpenVPNCSOEndpointResponse500 | DeleteVPNOpenVPNCSOEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
