from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpni_psec_phase_2_endpoint_data_body import PatchVPNIPsecPhase2EndpointDataBody
from ...models.patch_vpni_psec_phase_2_endpoint_json_body import PatchVPNIPsecPhase2EndpointJsonBody
from ...models.patch_vpni_psec_phase_2_endpoint_response_400 import PatchVPNIPsecPhase2EndpointResponse400
from ...models.patch_vpni_psec_phase_2_endpoint_response_401 import PatchVPNIPsecPhase2EndpointResponse401
from ...models.patch_vpni_psec_phase_2_endpoint_response_403 import PatchVPNIPsecPhase2EndpointResponse403
from ...models.patch_vpni_psec_phase_2_endpoint_response_404 import PatchVPNIPsecPhase2EndpointResponse404
from ...models.patch_vpni_psec_phase_2_endpoint_response_405 import PatchVPNIPsecPhase2EndpointResponse405
from ...models.patch_vpni_psec_phase_2_endpoint_response_406 import PatchVPNIPsecPhase2EndpointResponse406
from ...models.patch_vpni_psec_phase_2_endpoint_response_409 import PatchVPNIPsecPhase2EndpointResponse409
from ...models.patch_vpni_psec_phase_2_endpoint_response_415 import PatchVPNIPsecPhase2EndpointResponse415
from ...models.patch_vpni_psec_phase_2_endpoint_response_422 import PatchVPNIPsecPhase2EndpointResponse422
from ...models.patch_vpni_psec_phase_2_endpoint_response_424 import PatchVPNIPsecPhase2EndpointResponse424
from ...models.patch_vpni_psec_phase_2_endpoint_response_500 import PatchVPNIPsecPhase2EndpointResponse500
from ...models.patch_vpni_psec_phase_2_endpoint_response_503 import PatchVPNIPsecPhase2EndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNIPsecPhase2EndpointJsonBody | PatchVPNIPsecPhase2EndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/ipsec/phase2",
    }

    if isinstance(body, PatchVPNIPsecPhase2EndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNIPsecPhase2EndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNIPsecPhase2EndpointResponse400
    | PatchVPNIPsecPhase2EndpointResponse401
    | PatchVPNIPsecPhase2EndpointResponse403
    | PatchVPNIPsecPhase2EndpointResponse404
    | PatchVPNIPsecPhase2EndpointResponse405
    | PatchVPNIPsecPhase2EndpointResponse406
    | PatchVPNIPsecPhase2EndpointResponse409
    | PatchVPNIPsecPhase2EndpointResponse415
    | PatchVPNIPsecPhase2EndpointResponse422
    | PatchVPNIPsecPhase2EndpointResponse424
    | PatchVPNIPsecPhase2EndpointResponse500
    | PatchVPNIPsecPhase2EndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNIPsecPhase2EndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNIPsecPhase2EndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNIPsecPhase2EndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNIPsecPhase2EndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNIPsecPhase2EndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNIPsecPhase2EndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNIPsecPhase2EndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNIPsecPhase2EndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNIPsecPhase2EndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNIPsecPhase2EndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNIPsecPhase2EndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNIPsecPhase2EndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNIPsecPhase2EndpointResponse400
    | PatchVPNIPsecPhase2EndpointResponse401
    | PatchVPNIPsecPhase2EndpointResponse403
    | PatchVPNIPsecPhase2EndpointResponse404
    | PatchVPNIPsecPhase2EndpointResponse405
    | PatchVPNIPsecPhase2EndpointResponse406
    | PatchVPNIPsecPhase2EndpointResponse409
    | PatchVPNIPsecPhase2EndpointResponse415
    | PatchVPNIPsecPhase2EndpointResponse422
    | PatchVPNIPsecPhase2EndpointResponse424
    | PatchVPNIPsecPhase2EndpointResponse500
    | PatchVPNIPsecPhase2EndpointResponse503
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
    body: PatchVPNIPsecPhase2EndpointJsonBody | PatchVPNIPsecPhase2EndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNIPsecPhase2EndpointResponse400
    | PatchVPNIPsecPhase2EndpointResponse401
    | PatchVPNIPsecPhase2EndpointResponse403
    | PatchVPNIPsecPhase2EndpointResponse404
    | PatchVPNIPsecPhase2EndpointResponse405
    | PatchVPNIPsecPhase2EndpointResponse406
    | PatchVPNIPsecPhase2EndpointResponse409
    | PatchVPNIPsecPhase2EndpointResponse415
    | PatchVPNIPsecPhase2EndpointResponse422
    | PatchVPNIPsecPhase2EndpointResponse424
    | PatchVPNIPsecPhase2EndpointResponse500
    | PatchVPNIPsecPhase2EndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNIPsecPhase2EndpointJsonBody | Unset):
        body (PatchVPNIPsecPhase2EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNIPsecPhase2EndpointResponse400 | PatchVPNIPsecPhase2EndpointResponse401 | PatchVPNIPsecPhase2EndpointResponse403 | PatchVPNIPsecPhase2EndpointResponse404 | PatchVPNIPsecPhase2EndpointResponse405 | PatchVPNIPsecPhase2EndpointResponse406 | PatchVPNIPsecPhase2EndpointResponse409 | PatchVPNIPsecPhase2EndpointResponse415 | PatchVPNIPsecPhase2EndpointResponse422 | PatchVPNIPsecPhase2EndpointResponse424 | PatchVPNIPsecPhase2EndpointResponse500 | PatchVPNIPsecPhase2EndpointResponse503]
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
    body: PatchVPNIPsecPhase2EndpointJsonBody | PatchVPNIPsecPhase2EndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNIPsecPhase2EndpointResponse400
    | PatchVPNIPsecPhase2EndpointResponse401
    | PatchVPNIPsecPhase2EndpointResponse403
    | PatchVPNIPsecPhase2EndpointResponse404
    | PatchVPNIPsecPhase2EndpointResponse405
    | PatchVPNIPsecPhase2EndpointResponse406
    | PatchVPNIPsecPhase2EndpointResponse409
    | PatchVPNIPsecPhase2EndpointResponse415
    | PatchVPNIPsecPhase2EndpointResponse422
    | PatchVPNIPsecPhase2EndpointResponse424
    | PatchVPNIPsecPhase2EndpointResponse500
    | PatchVPNIPsecPhase2EndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNIPsecPhase2EndpointJsonBody | Unset):
        body (PatchVPNIPsecPhase2EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNIPsecPhase2EndpointResponse400 | PatchVPNIPsecPhase2EndpointResponse401 | PatchVPNIPsecPhase2EndpointResponse403 | PatchVPNIPsecPhase2EndpointResponse404 | PatchVPNIPsecPhase2EndpointResponse405 | PatchVPNIPsecPhase2EndpointResponse406 | PatchVPNIPsecPhase2EndpointResponse409 | PatchVPNIPsecPhase2EndpointResponse415 | PatchVPNIPsecPhase2EndpointResponse422 | PatchVPNIPsecPhase2EndpointResponse424 | PatchVPNIPsecPhase2EndpointResponse500 | PatchVPNIPsecPhase2EndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNIPsecPhase2EndpointJsonBody | PatchVPNIPsecPhase2EndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNIPsecPhase2EndpointResponse400
    | PatchVPNIPsecPhase2EndpointResponse401
    | PatchVPNIPsecPhase2EndpointResponse403
    | PatchVPNIPsecPhase2EndpointResponse404
    | PatchVPNIPsecPhase2EndpointResponse405
    | PatchVPNIPsecPhase2EndpointResponse406
    | PatchVPNIPsecPhase2EndpointResponse409
    | PatchVPNIPsecPhase2EndpointResponse415
    | PatchVPNIPsecPhase2EndpointResponse422
    | PatchVPNIPsecPhase2EndpointResponse424
    | PatchVPNIPsecPhase2EndpointResponse500
    | PatchVPNIPsecPhase2EndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNIPsecPhase2EndpointJsonBody | Unset):
        body (PatchVPNIPsecPhase2EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNIPsecPhase2EndpointResponse400 | PatchVPNIPsecPhase2EndpointResponse401 | PatchVPNIPsecPhase2EndpointResponse403 | PatchVPNIPsecPhase2EndpointResponse404 | PatchVPNIPsecPhase2EndpointResponse405 | PatchVPNIPsecPhase2EndpointResponse406 | PatchVPNIPsecPhase2EndpointResponse409 | PatchVPNIPsecPhase2EndpointResponse415 | PatchVPNIPsecPhase2EndpointResponse422 | PatchVPNIPsecPhase2EndpointResponse424 | PatchVPNIPsecPhase2EndpointResponse500 | PatchVPNIPsecPhase2EndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNIPsecPhase2EndpointJsonBody | PatchVPNIPsecPhase2EndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNIPsecPhase2EndpointResponse400
    | PatchVPNIPsecPhase2EndpointResponse401
    | PatchVPNIPsecPhase2EndpointResponse403
    | PatchVPNIPsecPhase2EndpointResponse404
    | PatchVPNIPsecPhase2EndpointResponse405
    | PatchVPNIPsecPhase2EndpointResponse406
    | PatchVPNIPsecPhase2EndpointResponse409
    | PatchVPNIPsecPhase2EndpointResponse415
    | PatchVPNIPsecPhase2EndpointResponse422
    | PatchVPNIPsecPhase2EndpointResponse424
    | PatchVPNIPsecPhase2EndpointResponse500
    | PatchVPNIPsecPhase2EndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing IPsec Phase 2.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNIPsecPhase2EndpointJsonBody | Unset):
        body (PatchVPNIPsecPhase2EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNIPsecPhase2EndpointResponse400 | PatchVPNIPsecPhase2EndpointResponse401 | PatchVPNIPsecPhase2EndpointResponse403 | PatchVPNIPsecPhase2EndpointResponse404 | PatchVPNIPsecPhase2EndpointResponse405 | PatchVPNIPsecPhase2EndpointResponse406 | PatchVPNIPsecPhase2EndpointResponse409 | PatchVPNIPsecPhase2EndpointResponse415 | PatchVPNIPsecPhase2EndpointResponse422 | PatchVPNIPsecPhase2EndpointResponse424 | PatchVPNIPsecPhase2EndpointResponse500 | PatchVPNIPsecPhase2EndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
