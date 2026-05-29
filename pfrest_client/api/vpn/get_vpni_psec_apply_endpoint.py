from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpni_psec_apply_endpoint_response_400 import GetVPNIPsecApplyEndpointResponse400
from ...models.get_vpni_psec_apply_endpoint_response_401 import GetVPNIPsecApplyEndpointResponse401
from ...models.get_vpni_psec_apply_endpoint_response_403 import GetVPNIPsecApplyEndpointResponse403
from ...models.get_vpni_psec_apply_endpoint_response_404 import GetVPNIPsecApplyEndpointResponse404
from ...models.get_vpni_psec_apply_endpoint_response_405 import GetVPNIPsecApplyEndpointResponse405
from ...models.get_vpni_psec_apply_endpoint_response_406 import GetVPNIPsecApplyEndpointResponse406
from ...models.get_vpni_psec_apply_endpoint_response_409 import GetVPNIPsecApplyEndpointResponse409
from ...models.get_vpni_psec_apply_endpoint_response_415 import GetVPNIPsecApplyEndpointResponse415
from ...models.get_vpni_psec_apply_endpoint_response_422 import GetVPNIPsecApplyEndpointResponse422
from ...models.get_vpni_psec_apply_endpoint_response_424 import GetVPNIPsecApplyEndpointResponse424
from ...models.get_vpni_psec_apply_endpoint_response_500 import GetVPNIPsecApplyEndpointResponse500
from ...models.get_vpni_psec_apply_endpoint_response_503 import GetVPNIPsecApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/vpn/ipsec/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNIPsecApplyEndpointResponse400
    | GetVPNIPsecApplyEndpointResponse401
    | GetVPNIPsecApplyEndpointResponse403
    | GetVPNIPsecApplyEndpointResponse404
    | GetVPNIPsecApplyEndpointResponse405
    | GetVPNIPsecApplyEndpointResponse406
    | GetVPNIPsecApplyEndpointResponse409
    | GetVPNIPsecApplyEndpointResponse415
    | GetVPNIPsecApplyEndpointResponse422
    | GetVPNIPsecApplyEndpointResponse424
    | GetVPNIPsecApplyEndpointResponse500
    | GetVPNIPsecApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNIPsecApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNIPsecApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNIPsecApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNIPsecApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNIPsecApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNIPsecApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNIPsecApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNIPsecApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNIPsecApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNIPsecApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNIPsecApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNIPsecApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNIPsecApplyEndpointResponse400
    | GetVPNIPsecApplyEndpointResponse401
    | GetVPNIPsecApplyEndpointResponse403
    | GetVPNIPsecApplyEndpointResponse404
    | GetVPNIPsecApplyEndpointResponse405
    | GetVPNIPsecApplyEndpointResponse406
    | GetVPNIPsecApplyEndpointResponse409
    | GetVPNIPsecApplyEndpointResponse415
    | GetVPNIPsecApplyEndpointResponse422
    | GetVPNIPsecApplyEndpointResponse424
    | GetVPNIPsecApplyEndpointResponse500
    | GetVPNIPsecApplyEndpointResponse503
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
) -> Response[
    GetVPNIPsecApplyEndpointResponse400
    | GetVPNIPsecApplyEndpointResponse401
    | GetVPNIPsecApplyEndpointResponse403
    | GetVPNIPsecApplyEndpointResponse404
    | GetVPNIPsecApplyEndpointResponse405
    | GetVPNIPsecApplyEndpointResponse406
    | GetVPNIPsecApplyEndpointResponse409
    | GetVPNIPsecApplyEndpointResponse415
    | GetVPNIPsecApplyEndpointResponse422
    | GetVPNIPsecApplyEndpointResponse424
    | GetVPNIPsecApplyEndpointResponse500
    | GetVPNIPsecApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending IPsec change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNIPsecApplyEndpointResponse400 | GetVPNIPsecApplyEndpointResponse401 | GetVPNIPsecApplyEndpointResponse403 | GetVPNIPsecApplyEndpointResponse404 | GetVPNIPsecApplyEndpointResponse405 | GetVPNIPsecApplyEndpointResponse406 | GetVPNIPsecApplyEndpointResponse409 | GetVPNIPsecApplyEndpointResponse415 | GetVPNIPsecApplyEndpointResponse422 | GetVPNIPsecApplyEndpointResponse424 | GetVPNIPsecApplyEndpointResponse500 | GetVPNIPsecApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetVPNIPsecApplyEndpointResponse400
    | GetVPNIPsecApplyEndpointResponse401
    | GetVPNIPsecApplyEndpointResponse403
    | GetVPNIPsecApplyEndpointResponse404
    | GetVPNIPsecApplyEndpointResponse405
    | GetVPNIPsecApplyEndpointResponse406
    | GetVPNIPsecApplyEndpointResponse409
    | GetVPNIPsecApplyEndpointResponse415
    | GetVPNIPsecApplyEndpointResponse422
    | GetVPNIPsecApplyEndpointResponse424
    | GetVPNIPsecApplyEndpointResponse500
    | GetVPNIPsecApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending IPsec change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNIPsecApplyEndpointResponse400 | GetVPNIPsecApplyEndpointResponse401 | GetVPNIPsecApplyEndpointResponse403 | GetVPNIPsecApplyEndpointResponse404 | GetVPNIPsecApplyEndpointResponse405 | GetVPNIPsecApplyEndpointResponse406 | GetVPNIPsecApplyEndpointResponse409 | GetVPNIPsecApplyEndpointResponse415 | GetVPNIPsecApplyEndpointResponse422 | GetVPNIPsecApplyEndpointResponse424 | GetVPNIPsecApplyEndpointResponse500 | GetVPNIPsecApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetVPNIPsecApplyEndpointResponse400
    | GetVPNIPsecApplyEndpointResponse401
    | GetVPNIPsecApplyEndpointResponse403
    | GetVPNIPsecApplyEndpointResponse404
    | GetVPNIPsecApplyEndpointResponse405
    | GetVPNIPsecApplyEndpointResponse406
    | GetVPNIPsecApplyEndpointResponse409
    | GetVPNIPsecApplyEndpointResponse415
    | GetVPNIPsecApplyEndpointResponse422
    | GetVPNIPsecApplyEndpointResponse424
    | GetVPNIPsecApplyEndpointResponse500
    | GetVPNIPsecApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending IPsec change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNIPsecApplyEndpointResponse400 | GetVPNIPsecApplyEndpointResponse401 | GetVPNIPsecApplyEndpointResponse403 | GetVPNIPsecApplyEndpointResponse404 | GetVPNIPsecApplyEndpointResponse405 | GetVPNIPsecApplyEndpointResponse406 | GetVPNIPsecApplyEndpointResponse409 | GetVPNIPsecApplyEndpointResponse415 | GetVPNIPsecApplyEndpointResponse422 | GetVPNIPsecApplyEndpointResponse424 | GetVPNIPsecApplyEndpointResponse500 | GetVPNIPsecApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetVPNIPsecApplyEndpointResponse400
    | GetVPNIPsecApplyEndpointResponse401
    | GetVPNIPsecApplyEndpointResponse403
    | GetVPNIPsecApplyEndpointResponse404
    | GetVPNIPsecApplyEndpointResponse405
    | GetVPNIPsecApplyEndpointResponse406
    | GetVPNIPsecApplyEndpointResponse409
    | GetVPNIPsecApplyEndpointResponse415
    | GetVPNIPsecApplyEndpointResponse422
    | GetVPNIPsecApplyEndpointResponse424
    | GetVPNIPsecApplyEndpointResponse500
    | GetVPNIPsecApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending IPsec change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNIPsecApplyEndpointResponse400 | GetVPNIPsecApplyEndpointResponse401 | GetVPNIPsecApplyEndpointResponse403 | GetVPNIPsecApplyEndpointResponse404 | GetVPNIPsecApplyEndpointResponse405 | GetVPNIPsecApplyEndpointResponse406 | GetVPNIPsecApplyEndpointResponse409 | GetVPNIPsecApplyEndpointResponse415 | GetVPNIPsecApplyEndpointResponse422 | GetVPNIPsecApplyEndpointResponse424 | GetVPNIPsecApplyEndpointResponse500 | GetVPNIPsecApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
