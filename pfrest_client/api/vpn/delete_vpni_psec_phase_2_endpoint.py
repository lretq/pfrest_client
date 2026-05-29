from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_vpni_psec_phase_2_endpoint_response_400 import DeleteVPNIPsecPhase2EndpointResponse400
from ...models.delete_vpni_psec_phase_2_endpoint_response_401 import DeleteVPNIPsecPhase2EndpointResponse401
from ...models.delete_vpni_psec_phase_2_endpoint_response_403 import DeleteVPNIPsecPhase2EndpointResponse403
from ...models.delete_vpni_psec_phase_2_endpoint_response_404 import DeleteVPNIPsecPhase2EndpointResponse404
from ...models.delete_vpni_psec_phase_2_endpoint_response_405 import DeleteVPNIPsecPhase2EndpointResponse405
from ...models.delete_vpni_psec_phase_2_endpoint_response_406 import DeleteVPNIPsecPhase2EndpointResponse406
from ...models.delete_vpni_psec_phase_2_endpoint_response_409 import DeleteVPNIPsecPhase2EndpointResponse409
from ...models.delete_vpni_psec_phase_2_endpoint_response_415 import DeleteVPNIPsecPhase2EndpointResponse415
from ...models.delete_vpni_psec_phase_2_endpoint_response_422 import DeleteVPNIPsecPhase2EndpointResponse422
from ...models.delete_vpni_psec_phase_2_endpoint_response_424 import DeleteVPNIPsecPhase2EndpointResponse424
from ...models.delete_vpni_psec_phase_2_endpoint_response_500 import DeleteVPNIPsecPhase2EndpointResponse500
from ...models.delete_vpni_psec_phase_2_endpoint_response_503 import DeleteVPNIPsecPhase2EndpointResponse503
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
        "url": "/api/v2/vpn/ipsec/phase2",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteVPNIPsecPhase2EndpointResponse400
    | DeleteVPNIPsecPhase2EndpointResponse401
    | DeleteVPNIPsecPhase2EndpointResponse403
    | DeleteVPNIPsecPhase2EndpointResponse404
    | DeleteVPNIPsecPhase2EndpointResponse405
    | DeleteVPNIPsecPhase2EndpointResponse406
    | DeleteVPNIPsecPhase2EndpointResponse409
    | DeleteVPNIPsecPhase2EndpointResponse415
    | DeleteVPNIPsecPhase2EndpointResponse422
    | DeleteVPNIPsecPhase2EndpointResponse424
    | DeleteVPNIPsecPhase2EndpointResponse500
    | DeleteVPNIPsecPhase2EndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteVPNIPsecPhase2EndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteVPNIPsecPhase2EndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteVPNIPsecPhase2EndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteVPNIPsecPhase2EndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteVPNIPsecPhase2EndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteVPNIPsecPhase2EndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteVPNIPsecPhase2EndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteVPNIPsecPhase2EndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteVPNIPsecPhase2EndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteVPNIPsecPhase2EndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteVPNIPsecPhase2EndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteVPNIPsecPhase2EndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteVPNIPsecPhase2EndpointResponse400
    | DeleteVPNIPsecPhase2EndpointResponse401
    | DeleteVPNIPsecPhase2EndpointResponse403
    | DeleteVPNIPsecPhase2EndpointResponse404
    | DeleteVPNIPsecPhase2EndpointResponse405
    | DeleteVPNIPsecPhase2EndpointResponse406
    | DeleteVPNIPsecPhase2EndpointResponse409
    | DeleteVPNIPsecPhase2EndpointResponse415
    | DeleteVPNIPsecPhase2EndpointResponse422
    | DeleteVPNIPsecPhase2EndpointResponse424
    | DeleteVPNIPsecPhase2EndpointResponse500
    | DeleteVPNIPsecPhase2EndpointResponse503
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
    DeleteVPNIPsecPhase2EndpointResponse400
    | DeleteVPNIPsecPhase2EndpointResponse401
    | DeleteVPNIPsecPhase2EndpointResponse403
    | DeleteVPNIPsecPhase2EndpointResponse404
    | DeleteVPNIPsecPhase2EndpointResponse405
    | DeleteVPNIPsecPhase2EndpointResponse406
    | DeleteVPNIPsecPhase2EndpointResponse409
    | DeleteVPNIPsecPhase2EndpointResponse415
    | DeleteVPNIPsecPhase2EndpointResponse422
    | DeleteVPNIPsecPhase2EndpointResponse424
    | DeleteVPNIPsecPhase2EndpointResponse500
    | DeleteVPNIPsecPhase2EndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNIPsecPhase2EndpointResponse400 | DeleteVPNIPsecPhase2EndpointResponse401 | DeleteVPNIPsecPhase2EndpointResponse403 | DeleteVPNIPsecPhase2EndpointResponse404 | DeleteVPNIPsecPhase2EndpointResponse405 | DeleteVPNIPsecPhase2EndpointResponse406 | DeleteVPNIPsecPhase2EndpointResponse409 | DeleteVPNIPsecPhase2EndpointResponse415 | DeleteVPNIPsecPhase2EndpointResponse422 | DeleteVPNIPsecPhase2EndpointResponse424 | DeleteVPNIPsecPhase2EndpointResponse500 | DeleteVPNIPsecPhase2EndpointResponse503]
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
    DeleteVPNIPsecPhase2EndpointResponse400
    | DeleteVPNIPsecPhase2EndpointResponse401
    | DeleteVPNIPsecPhase2EndpointResponse403
    | DeleteVPNIPsecPhase2EndpointResponse404
    | DeleteVPNIPsecPhase2EndpointResponse405
    | DeleteVPNIPsecPhase2EndpointResponse406
    | DeleteVPNIPsecPhase2EndpointResponse409
    | DeleteVPNIPsecPhase2EndpointResponse415
    | DeleteVPNIPsecPhase2EndpointResponse422
    | DeleteVPNIPsecPhase2EndpointResponse424
    | DeleteVPNIPsecPhase2EndpointResponse500
    | DeleteVPNIPsecPhase2EndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNIPsecPhase2EndpointResponse400 | DeleteVPNIPsecPhase2EndpointResponse401 | DeleteVPNIPsecPhase2EndpointResponse403 | DeleteVPNIPsecPhase2EndpointResponse404 | DeleteVPNIPsecPhase2EndpointResponse405 | DeleteVPNIPsecPhase2EndpointResponse406 | DeleteVPNIPsecPhase2EndpointResponse409 | DeleteVPNIPsecPhase2EndpointResponse415 | DeleteVPNIPsecPhase2EndpointResponse422 | DeleteVPNIPsecPhase2EndpointResponse424 | DeleteVPNIPsecPhase2EndpointResponse500 | DeleteVPNIPsecPhase2EndpointResponse503
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
    DeleteVPNIPsecPhase2EndpointResponse400
    | DeleteVPNIPsecPhase2EndpointResponse401
    | DeleteVPNIPsecPhase2EndpointResponse403
    | DeleteVPNIPsecPhase2EndpointResponse404
    | DeleteVPNIPsecPhase2EndpointResponse405
    | DeleteVPNIPsecPhase2EndpointResponse406
    | DeleteVPNIPsecPhase2EndpointResponse409
    | DeleteVPNIPsecPhase2EndpointResponse415
    | DeleteVPNIPsecPhase2EndpointResponse422
    | DeleteVPNIPsecPhase2EndpointResponse424
    | DeleteVPNIPsecPhase2EndpointResponse500
    | DeleteVPNIPsecPhase2EndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNIPsecPhase2EndpointResponse400 | DeleteVPNIPsecPhase2EndpointResponse401 | DeleteVPNIPsecPhase2EndpointResponse403 | DeleteVPNIPsecPhase2EndpointResponse404 | DeleteVPNIPsecPhase2EndpointResponse405 | DeleteVPNIPsecPhase2EndpointResponse406 | DeleteVPNIPsecPhase2EndpointResponse409 | DeleteVPNIPsecPhase2EndpointResponse415 | DeleteVPNIPsecPhase2EndpointResponse422 | DeleteVPNIPsecPhase2EndpointResponse424 | DeleteVPNIPsecPhase2EndpointResponse500 | DeleteVPNIPsecPhase2EndpointResponse503]
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
    DeleteVPNIPsecPhase2EndpointResponse400
    | DeleteVPNIPsecPhase2EndpointResponse401
    | DeleteVPNIPsecPhase2EndpointResponse403
    | DeleteVPNIPsecPhase2EndpointResponse404
    | DeleteVPNIPsecPhase2EndpointResponse405
    | DeleteVPNIPsecPhase2EndpointResponse406
    | DeleteVPNIPsecPhase2EndpointResponse409
    | DeleteVPNIPsecPhase2EndpointResponse415
    | DeleteVPNIPsecPhase2EndpointResponse422
    | DeleteVPNIPsecPhase2EndpointResponse424
    | DeleteVPNIPsecPhase2EndpointResponse500
    | DeleteVPNIPsecPhase2EndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-delete ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNIPsecPhase2EndpointResponse400 | DeleteVPNIPsecPhase2EndpointResponse401 | DeleteVPNIPsecPhase2EndpointResponse403 | DeleteVPNIPsecPhase2EndpointResponse404 | DeleteVPNIPsecPhase2EndpointResponse405 | DeleteVPNIPsecPhase2EndpointResponse406 | DeleteVPNIPsecPhase2EndpointResponse409 | DeleteVPNIPsecPhase2EndpointResponse415 | DeleteVPNIPsecPhase2EndpointResponse422 | DeleteVPNIPsecPhase2EndpointResponse424 | DeleteVPNIPsecPhase2EndpointResponse500 | DeleteVPNIPsecPhase2EndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            apply=apply,
        )
    ).parsed
