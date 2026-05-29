from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpn_open_vpncso_endpoint_data_body import PatchVPNOpenVPNCSOEndpointDataBody
from ...models.patch_vpn_open_vpncso_endpoint_json_body import PatchVPNOpenVPNCSOEndpointJsonBody
from ...models.patch_vpn_open_vpncso_endpoint_response_400 import PatchVPNOpenVPNCSOEndpointResponse400
from ...models.patch_vpn_open_vpncso_endpoint_response_401 import PatchVPNOpenVPNCSOEndpointResponse401
from ...models.patch_vpn_open_vpncso_endpoint_response_403 import PatchVPNOpenVPNCSOEndpointResponse403
from ...models.patch_vpn_open_vpncso_endpoint_response_404 import PatchVPNOpenVPNCSOEndpointResponse404
from ...models.patch_vpn_open_vpncso_endpoint_response_405 import PatchVPNOpenVPNCSOEndpointResponse405
from ...models.patch_vpn_open_vpncso_endpoint_response_406 import PatchVPNOpenVPNCSOEndpointResponse406
from ...models.patch_vpn_open_vpncso_endpoint_response_409 import PatchVPNOpenVPNCSOEndpointResponse409
from ...models.patch_vpn_open_vpncso_endpoint_response_415 import PatchVPNOpenVPNCSOEndpointResponse415
from ...models.patch_vpn_open_vpncso_endpoint_response_422 import PatchVPNOpenVPNCSOEndpointResponse422
from ...models.patch_vpn_open_vpncso_endpoint_response_424 import PatchVPNOpenVPNCSOEndpointResponse424
from ...models.patch_vpn_open_vpncso_endpoint_response_500 import PatchVPNOpenVPNCSOEndpointResponse500
from ...models.patch_vpn_open_vpncso_endpoint_response_503 import PatchVPNOpenVPNCSOEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNOpenVPNCSOEndpointJsonBody | PatchVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/openvpn/cso",
    }

    if isinstance(body, PatchVPNOpenVPNCSOEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNOpenVPNCSOEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNOpenVPNCSOEndpointResponse400
    | PatchVPNOpenVPNCSOEndpointResponse401
    | PatchVPNOpenVPNCSOEndpointResponse403
    | PatchVPNOpenVPNCSOEndpointResponse404
    | PatchVPNOpenVPNCSOEndpointResponse405
    | PatchVPNOpenVPNCSOEndpointResponse406
    | PatchVPNOpenVPNCSOEndpointResponse409
    | PatchVPNOpenVPNCSOEndpointResponse415
    | PatchVPNOpenVPNCSOEndpointResponse422
    | PatchVPNOpenVPNCSOEndpointResponse424
    | PatchVPNOpenVPNCSOEndpointResponse500
    | PatchVPNOpenVPNCSOEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNOpenVPNCSOEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNOpenVPNCSOEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNOpenVPNCSOEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNOpenVPNCSOEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNOpenVPNCSOEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNOpenVPNCSOEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNOpenVPNCSOEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNOpenVPNCSOEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNOpenVPNCSOEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNOpenVPNCSOEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNOpenVPNCSOEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNOpenVPNCSOEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNOpenVPNCSOEndpointResponse400
    | PatchVPNOpenVPNCSOEndpointResponse401
    | PatchVPNOpenVPNCSOEndpointResponse403
    | PatchVPNOpenVPNCSOEndpointResponse404
    | PatchVPNOpenVPNCSOEndpointResponse405
    | PatchVPNOpenVPNCSOEndpointResponse406
    | PatchVPNOpenVPNCSOEndpointResponse409
    | PatchVPNOpenVPNCSOEndpointResponse415
    | PatchVPNOpenVPNCSOEndpointResponse422
    | PatchVPNOpenVPNCSOEndpointResponse424
    | PatchVPNOpenVPNCSOEndpointResponse500
    | PatchVPNOpenVPNCSOEndpointResponse503
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
    body: PatchVPNOpenVPNCSOEndpointJsonBody | PatchVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNOpenVPNCSOEndpointResponse400
    | PatchVPNOpenVPNCSOEndpointResponse401
    | PatchVPNOpenVPNCSOEndpointResponse403
    | PatchVPNOpenVPNCSOEndpointResponse404
    | PatchVPNOpenVPNCSOEndpointResponse405
    | PatchVPNOpenVPNCSOEndpointResponse406
    | PatchVPNOpenVPNCSOEndpointResponse409
    | PatchVPNOpenVPNCSOEndpointResponse415
    | PatchVPNOpenVPNCSOEndpointResponse422
    | PatchVPNOpenVPNCSOEndpointResponse424
    | PatchVPNOpenVPNCSOEndpointResponse500
    | PatchVPNOpenVPNCSOEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNOpenVPNCSOEndpointResponse400 | PatchVPNOpenVPNCSOEndpointResponse401 | PatchVPNOpenVPNCSOEndpointResponse403 | PatchVPNOpenVPNCSOEndpointResponse404 | PatchVPNOpenVPNCSOEndpointResponse405 | PatchVPNOpenVPNCSOEndpointResponse406 | PatchVPNOpenVPNCSOEndpointResponse409 | PatchVPNOpenVPNCSOEndpointResponse415 | PatchVPNOpenVPNCSOEndpointResponse422 | PatchVPNOpenVPNCSOEndpointResponse424 | PatchVPNOpenVPNCSOEndpointResponse500 | PatchVPNOpenVPNCSOEndpointResponse503]
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
    body: PatchVPNOpenVPNCSOEndpointJsonBody | PatchVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNOpenVPNCSOEndpointResponse400
    | PatchVPNOpenVPNCSOEndpointResponse401
    | PatchVPNOpenVPNCSOEndpointResponse403
    | PatchVPNOpenVPNCSOEndpointResponse404
    | PatchVPNOpenVPNCSOEndpointResponse405
    | PatchVPNOpenVPNCSOEndpointResponse406
    | PatchVPNOpenVPNCSOEndpointResponse409
    | PatchVPNOpenVPNCSOEndpointResponse415
    | PatchVPNOpenVPNCSOEndpointResponse422
    | PatchVPNOpenVPNCSOEndpointResponse424
    | PatchVPNOpenVPNCSOEndpointResponse500
    | PatchVPNOpenVPNCSOEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNOpenVPNCSOEndpointResponse400 | PatchVPNOpenVPNCSOEndpointResponse401 | PatchVPNOpenVPNCSOEndpointResponse403 | PatchVPNOpenVPNCSOEndpointResponse404 | PatchVPNOpenVPNCSOEndpointResponse405 | PatchVPNOpenVPNCSOEndpointResponse406 | PatchVPNOpenVPNCSOEndpointResponse409 | PatchVPNOpenVPNCSOEndpointResponse415 | PatchVPNOpenVPNCSOEndpointResponse422 | PatchVPNOpenVPNCSOEndpointResponse424 | PatchVPNOpenVPNCSOEndpointResponse500 | PatchVPNOpenVPNCSOEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNOpenVPNCSOEndpointJsonBody | PatchVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNOpenVPNCSOEndpointResponse400
    | PatchVPNOpenVPNCSOEndpointResponse401
    | PatchVPNOpenVPNCSOEndpointResponse403
    | PatchVPNOpenVPNCSOEndpointResponse404
    | PatchVPNOpenVPNCSOEndpointResponse405
    | PatchVPNOpenVPNCSOEndpointResponse406
    | PatchVPNOpenVPNCSOEndpointResponse409
    | PatchVPNOpenVPNCSOEndpointResponse415
    | PatchVPNOpenVPNCSOEndpointResponse422
    | PatchVPNOpenVPNCSOEndpointResponse424
    | PatchVPNOpenVPNCSOEndpointResponse500
    | PatchVPNOpenVPNCSOEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNOpenVPNCSOEndpointResponse400 | PatchVPNOpenVPNCSOEndpointResponse401 | PatchVPNOpenVPNCSOEndpointResponse403 | PatchVPNOpenVPNCSOEndpointResponse404 | PatchVPNOpenVPNCSOEndpointResponse405 | PatchVPNOpenVPNCSOEndpointResponse406 | PatchVPNOpenVPNCSOEndpointResponse409 | PatchVPNOpenVPNCSOEndpointResponse415 | PatchVPNOpenVPNCSOEndpointResponse422 | PatchVPNOpenVPNCSOEndpointResponse424 | PatchVPNOpenVPNCSOEndpointResponse500 | PatchVPNOpenVPNCSOEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNOpenVPNCSOEndpointJsonBody | PatchVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNOpenVPNCSOEndpointResponse400
    | PatchVPNOpenVPNCSOEndpointResponse401
    | PatchVPNOpenVPNCSOEndpointResponse403
    | PatchVPNOpenVPNCSOEndpointResponse404
    | PatchVPNOpenVPNCSOEndpointResponse405
    | PatchVPNOpenVPNCSOEndpointResponse406
    | PatchVPNOpenVPNCSOEndpointResponse409
    | PatchVPNOpenVPNCSOEndpointResponse415
    | PatchVPNOpenVPNCSOEndpointResponse422
    | PatchVPNOpenVPNCSOEndpointResponse424
    | PatchVPNOpenVPNCSOEndpointResponse500
    | PatchVPNOpenVPNCSOEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing OpenVPN Client Specific
    Override.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    OpenVPNClientSpecificOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-cso-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNOpenVPNCSOEndpointResponse400 | PatchVPNOpenVPNCSOEndpointResponse401 | PatchVPNOpenVPNCSOEndpointResponse403 | PatchVPNOpenVPNCSOEndpointResponse404 | PatchVPNOpenVPNCSOEndpointResponse405 | PatchVPNOpenVPNCSOEndpointResponse406 | PatchVPNOpenVPNCSOEndpointResponse409 | PatchVPNOpenVPNCSOEndpointResponse415 | PatchVPNOpenVPNCSOEndpointResponse422 | PatchVPNOpenVPNCSOEndpointResponse424 | PatchVPNOpenVPNCSOEndpointResponse500 | PatchVPNOpenVPNCSOEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
