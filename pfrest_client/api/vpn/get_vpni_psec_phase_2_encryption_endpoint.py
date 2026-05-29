from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_400 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse400,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_401 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse401,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_403 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse403,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_404 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse404,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_405 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse405,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_406 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse406,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_409 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse409,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_415 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse415,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_422 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse422,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_424 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse424,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_500 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse500,
)
from ...models.get_vpni_psec_phase_2_encryption_endpoint_response_503 import (
    GetVPNIPsecPhase2EncryptionEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/vpn/ipsec/phase2/encryption",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNIPsecPhase2EncryptionEndpointResponse400
    | GetVPNIPsecPhase2EncryptionEndpointResponse401
    | GetVPNIPsecPhase2EncryptionEndpointResponse403
    | GetVPNIPsecPhase2EncryptionEndpointResponse404
    | GetVPNIPsecPhase2EncryptionEndpointResponse405
    | GetVPNIPsecPhase2EncryptionEndpointResponse406
    | GetVPNIPsecPhase2EncryptionEndpointResponse409
    | GetVPNIPsecPhase2EncryptionEndpointResponse415
    | GetVPNIPsecPhase2EncryptionEndpointResponse422
    | GetVPNIPsecPhase2EncryptionEndpointResponse424
    | GetVPNIPsecPhase2EncryptionEndpointResponse500
    | GetVPNIPsecPhase2EncryptionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNIPsecPhase2EncryptionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNIPsecPhase2EncryptionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNIPsecPhase2EncryptionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNIPsecPhase2EncryptionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNIPsecPhase2EncryptionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNIPsecPhase2EncryptionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNIPsecPhase2EncryptionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNIPsecPhase2EncryptionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNIPsecPhase2EncryptionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNIPsecPhase2EncryptionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNIPsecPhase2EncryptionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNIPsecPhase2EncryptionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNIPsecPhase2EncryptionEndpointResponse400
    | GetVPNIPsecPhase2EncryptionEndpointResponse401
    | GetVPNIPsecPhase2EncryptionEndpointResponse403
    | GetVPNIPsecPhase2EncryptionEndpointResponse404
    | GetVPNIPsecPhase2EncryptionEndpointResponse405
    | GetVPNIPsecPhase2EncryptionEndpointResponse406
    | GetVPNIPsecPhase2EncryptionEndpointResponse409
    | GetVPNIPsecPhase2EncryptionEndpointResponse415
    | GetVPNIPsecPhase2EncryptionEndpointResponse422
    | GetVPNIPsecPhase2EncryptionEndpointResponse424
    | GetVPNIPsecPhase2EncryptionEndpointResponse500
    | GetVPNIPsecPhase2EncryptionEndpointResponse503
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
) -> Response[
    GetVPNIPsecPhase2EncryptionEndpointResponse400
    | GetVPNIPsecPhase2EncryptionEndpointResponse401
    | GetVPNIPsecPhase2EncryptionEndpointResponse403
    | GetVPNIPsecPhase2EncryptionEndpointResponse404
    | GetVPNIPsecPhase2EncryptionEndpointResponse405
    | GetVPNIPsecPhase2EncryptionEndpointResponse406
    | GetVPNIPsecPhase2EncryptionEndpointResponse409
    | GetVPNIPsecPhase2EncryptionEndpointResponse415
    | GetVPNIPsecPhase2EncryptionEndpointResponse422
    | GetVPNIPsecPhase2EncryptionEndpointResponse424
    | GetVPNIPsecPhase2EncryptionEndpointResponse500
    | GetVPNIPsecPhase2EncryptionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing IPsec Phase 2 Encryption.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: IPsecPhase2Encryption<br>**Parent model**:
    IPsecPhase2<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-encryption-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNIPsecPhase2EncryptionEndpointResponse400 | GetVPNIPsecPhase2EncryptionEndpointResponse401 | GetVPNIPsecPhase2EncryptionEndpointResponse403 | GetVPNIPsecPhase2EncryptionEndpointResponse404 | GetVPNIPsecPhase2EncryptionEndpointResponse405 | GetVPNIPsecPhase2EncryptionEndpointResponse406 | GetVPNIPsecPhase2EncryptionEndpointResponse409 | GetVPNIPsecPhase2EncryptionEndpointResponse415 | GetVPNIPsecPhase2EncryptionEndpointResponse422 | GetVPNIPsecPhase2EncryptionEndpointResponse424 | GetVPNIPsecPhase2EncryptionEndpointResponse500 | GetVPNIPsecPhase2EncryptionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
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
) -> (
    GetVPNIPsecPhase2EncryptionEndpointResponse400
    | GetVPNIPsecPhase2EncryptionEndpointResponse401
    | GetVPNIPsecPhase2EncryptionEndpointResponse403
    | GetVPNIPsecPhase2EncryptionEndpointResponse404
    | GetVPNIPsecPhase2EncryptionEndpointResponse405
    | GetVPNIPsecPhase2EncryptionEndpointResponse406
    | GetVPNIPsecPhase2EncryptionEndpointResponse409
    | GetVPNIPsecPhase2EncryptionEndpointResponse415
    | GetVPNIPsecPhase2EncryptionEndpointResponse422
    | GetVPNIPsecPhase2EncryptionEndpointResponse424
    | GetVPNIPsecPhase2EncryptionEndpointResponse500
    | GetVPNIPsecPhase2EncryptionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing IPsec Phase 2 Encryption.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: IPsecPhase2Encryption<br>**Parent model**:
    IPsecPhase2<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-encryption-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNIPsecPhase2EncryptionEndpointResponse400 | GetVPNIPsecPhase2EncryptionEndpointResponse401 | GetVPNIPsecPhase2EncryptionEndpointResponse403 | GetVPNIPsecPhase2EncryptionEndpointResponse404 | GetVPNIPsecPhase2EncryptionEndpointResponse405 | GetVPNIPsecPhase2EncryptionEndpointResponse406 | GetVPNIPsecPhase2EncryptionEndpointResponse409 | GetVPNIPsecPhase2EncryptionEndpointResponse415 | GetVPNIPsecPhase2EncryptionEndpointResponse422 | GetVPNIPsecPhase2EncryptionEndpointResponse424 | GetVPNIPsecPhase2EncryptionEndpointResponse500 | GetVPNIPsecPhase2EncryptionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetVPNIPsecPhase2EncryptionEndpointResponse400
    | GetVPNIPsecPhase2EncryptionEndpointResponse401
    | GetVPNIPsecPhase2EncryptionEndpointResponse403
    | GetVPNIPsecPhase2EncryptionEndpointResponse404
    | GetVPNIPsecPhase2EncryptionEndpointResponse405
    | GetVPNIPsecPhase2EncryptionEndpointResponse406
    | GetVPNIPsecPhase2EncryptionEndpointResponse409
    | GetVPNIPsecPhase2EncryptionEndpointResponse415
    | GetVPNIPsecPhase2EncryptionEndpointResponse422
    | GetVPNIPsecPhase2EncryptionEndpointResponse424
    | GetVPNIPsecPhase2EncryptionEndpointResponse500
    | GetVPNIPsecPhase2EncryptionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing IPsec Phase 2 Encryption.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: IPsecPhase2Encryption<br>**Parent model**:
    IPsecPhase2<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-encryption-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNIPsecPhase2EncryptionEndpointResponse400 | GetVPNIPsecPhase2EncryptionEndpointResponse401 | GetVPNIPsecPhase2EncryptionEndpointResponse403 | GetVPNIPsecPhase2EncryptionEndpointResponse404 | GetVPNIPsecPhase2EncryptionEndpointResponse405 | GetVPNIPsecPhase2EncryptionEndpointResponse406 | GetVPNIPsecPhase2EncryptionEndpointResponse409 | GetVPNIPsecPhase2EncryptionEndpointResponse415 | GetVPNIPsecPhase2EncryptionEndpointResponse422 | GetVPNIPsecPhase2EncryptionEndpointResponse424 | GetVPNIPsecPhase2EncryptionEndpointResponse500 | GetVPNIPsecPhase2EncryptionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetVPNIPsecPhase2EncryptionEndpointResponse400
    | GetVPNIPsecPhase2EncryptionEndpointResponse401
    | GetVPNIPsecPhase2EncryptionEndpointResponse403
    | GetVPNIPsecPhase2EncryptionEndpointResponse404
    | GetVPNIPsecPhase2EncryptionEndpointResponse405
    | GetVPNIPsecPhase2EncryptionEndpointResponse406
    | GetVPNIPsecPhase2EncryptionEndpointResponse409
    | GetVPNIPsecPhase2EncryptionEndpointResponse415
    | GetVPNIPsecPhase2EncryptionEndpointResponse422
    | GetVPNIPsecPhase2EncryptionEndpointResponse424
    | GetVPNIPsecPhase2EncryptionEndpointResponse500
    | GetVPNIPsecPhase2EncryptionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing IPsec Phase 2 Encryption.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: IPsecPhase2Encryption<br>**Parent model**:
    IPsecPhase2<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-encryption-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNIPsecPhase2EncryptionEndpointResponse400 | GetVPNIPsecPhase2EncryptionEndpointResponse401 | GetVPNIPsecPhase2EncryptionEndpointResponse403 | GetVPNIPsecPhase2EncryptionEndpointResponse404 | GetVPNIPsecPhase2EncryptionEndpointResponse405 | GetVPNIPsecPhase2EncryptionEndpointResponse406 | GetVPNIPsecPhase2EncryptionEndpointResponse409 | GetVPNIPsecPhase2EncryptionEndpointResponse415 | GetVPNIPsecPhase2EncryptionEndpointResponse422 | GetVPNIPsecPhase2EncryptionEndpointResponse424 | GetVPNIPsecPhase2EncryptionEndpointResponse500 | GetVPNIPsecPhase2EncryptionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
