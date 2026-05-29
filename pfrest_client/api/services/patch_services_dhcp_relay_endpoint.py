from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_dhcp_relay_endpoint_data_body import PatchServicesDHCPRelayEndpointDataBody
from ...models.patch_services_dhcp_relay_endpoint_json_body import PatchServicesDHCPRelayEndpointJsonBody
from ...models.patch_services_dhcp_relay_endpoint_response_400 import PatchServicesDHCPRelayEndpointResponse400
from ...models.patch_services_dhcp_relay_endpoint_response_401 import PatchServicesDHCPRelayEndpointResponse401
from ...models.patch_services_dhcp_relay_endpoint_response_403 import PatchServicesDHCPRelayEndpointResponse403
from ...models.patch_services_dhcp_relay_endpoint_response_404 import PatchServicesDHCPRelayEndpointResponse404
from ...models.patch_services_dhcp_relay_endpoint_response_405 import PatchServicesDHCPRelayEndpointResponse405
from ...models.patch_services_dhcp_relay_endpoint_response_406 import PatchServicesDHCPRelayEndpointResponse406
from ...models.patch_services_dhcp_relay_endpoint_response_409 import PatchServicesDHCPRelayEndpointResponse409
from ...models.patch_services_dhcp_relay_endpoint_response_415 import PatchServicesDHCPRelayEndpointResponse415
from ...models.patch_services_dhcp_relay_endpoint_response_422 import PatchServicesDHCPRelayEndpointResponse422
from ...models.patch_services_dhcp_relay_endpoint_response_424 import PatchServicesDHCPRelayEndpointResponse424
from ...models.patch_services_dhcp_relay_endpoint_response_500 import PatchServicesDHCPRelayEndpointResponse500
from ...models.patch_services_dhcp_relay_endpoint_response_503 import PatchServicesDHCPRelayEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesDHCPRelayEndpointJsonBody | PatchServicesDHCPRelayEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/dhcp_relay",
    }

    if isinstance(body, PatchServicesDHCPRelayEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesDHCPRelayEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesDHCPRelayEndpointResponse400
    | PatchServicesDHCPRelayEndpointResponse401
    | PatchServicesDHCPRelayEndpointResponse403
    | PatchServicesDHCPRelayEndpointResponse404
    | PatchServicesDHCPRelayEndpointResponse405
    | PatchServicesDHCPRelayEndpointResponse406
    | PatchServicesDHCPRelayEndpointResponse409
    | PatchServicesDHCPRelayEndpointResponse415
    | PatchServicesDHCPRelayEndpointResponse422
    | PatchServicesDHCPRelayEndpointResponse424
    | PatchServicesDHCPRelayEndpointResponse500
    | PatchServicesDHCPRelayEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesDHCPRelayEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesDHCPRelayEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesDHCPRelayEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesDHCPRelayEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesDHCPRelayEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesDHCPRelayEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesDHCPRelayEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesDHCPRelayEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesDHCPRelayEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesDHCPRelayEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesDHCPRelayEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesDHCPRelayEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesDHCPRelayEndpointResponse400
    | PatchServicesDHCPRelayEndpointResponse401
    | PatchServicesDHCPRelayEndpointResponse403
    | PatchServicesDHCPRelayEndpointResponse404
    | PatchServicesDHCPRelayEndpointResponse405
    | PatchServicesDHCPRelayEndpointResponse406
    | PatchServicesDHCPRelayEndpointResponse409
    | PatchServicesDHCPRelayEndpointResponse415
    | PatchServicesDHCPRelayEndpointResponse422
    | PatchServicesDHCPRelayEndpointResponse424
    | PatchServicesDHCPRelayEndpointResponse500
    | PatchServicesDHCPRelayEndpointResponse503
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
    body: PatchServicesDHCPRelayEndpointJsonBody | PatchServicesDHCPRelayEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesDHCPRelayEndpointResponse400
    | PatchServicesDHCPRelayEndpointResponse401
    | PatchServicesDHCPRelayEndpointResponse403
    | PatchServicesDHCPRelayEndpointResponse404
    | PatchServicesDHCPRelayEndpointResponse405
    | PatchServicesDHCPRelayEndpointResponse406
    | PatchServicesDHCPRelayEndpointResponse409
    | PatchServicesDHCPRelayEndpointResponse415
    | PatchServicesDHCPRelayEndpointResponse422
    | PatchServicesDHCPRelayEndpointResponse424
    | PatchServicesDHCPRelayEndpointResponse500
    | PatchServicesDHCPRelayEndpointResponse503
]:
    """<h3>Description:</h3>Updates current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPRelayEndpointJsonBody | Unset):
        body (PatchServicesDHCPRelayEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPRelayEndpointResponse400 | PatchServicesDHCPRelayEndpointResponse401 | PatchServicesDHCPRelayEndpointResponse403 | PatchServicesDHCPRelayEndpointResponse404 | PatchServicesDHCPRelayEndpointResponse405 | PatchServicesDHCPRelayEndpointResponse406 | PatchServicesDHCPRelayEndpointResponse409 | PatchServicesDHCPRelayEndpointResponse415 | PatchServicesDHCPRelayEndpointResponse422 | PatchServicesDHCPRelayEndpointResponse424 | PatchServicesDHCPRelayEndpointResponse500 | PatchServicesDHCPRelayEndpointResponse503]
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
    body: PatchServicesDHCPRelayEndpointJsonBody | PatchServicesDHCPRelayEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesDHCPRelayEndpointResponse400
    | PatchServicesDHCPRelayEndpointResponse401
    | PatchServicesDHCPRelayEndpointResponse403
    | PatchServicesDHCPRelayEndpointResponse404
    | PatchServicesDHCPRelayEndpointResponse405
    | PatchServicesDHCPRelayEndpointResponse406
    | PatchServicesDHCPRelayEndpointResponse409
    | PatchServicesDHCPRelayEndpointResponse415
    | PatchServicesDHCPRelayEndpointResponse422
    | PatchServicesDHCPRelayEndpointResponse424
    | PatchServicesDHCPRelayEndpointResponse500
    | PatchServicesDHCPRelayEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPRelayEndpointJsonBody | Unset):
        body (PatchServicesDHCPRelayEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPRelayEndpointResponse400 | PatchServicesDHCPRelayEndpointResponse401 | PatchServicesDHCPRelayEndpointResponse403 | PatchServicesDHCPRelayEndpointResponse404 | PatchServicesDHCPRelayEndpointResponse405 | PatchServicesDHCPRelayEndpointResponse406 | PatchServicesDHCPRelayEndpointResponse409 | PatchServicesDHCPRelayEndpointResponse415 | PatchServicesDHCPRelayEndpointResponse422 | PatchServicesDHCPRelayEndpointResponse424 | PatchServicesDHCPRelayEndpointResponse500 | PatchServicesDHCPRelayEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPRelayEndpointJsonBody | PatchServicesDHCPRelayEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesDHCPRelayEndpointResponse400
    | PatchServicesDHCPRelayEndpointResponse401
    | PatchServicesDHCPRelayEndpointResponse403
    | PatchServicesDHCPRelayEndpointResponse404
    | PatchServicesDHCPRelayEndpointResponse405
    | PatchServicesDHCPRelayEndpointResponse406
    | PatchServicesDHCPRelayEndpointResponse409
    | PatchServicesDHCPRelayEndpointResponse415
    | PatchServicesDHCPRelayEndpointResponse422
    | PatchServicesDHCPRelayEndpointResponse424
    | PatchServicesDHCPRelayEndpointResponse500
    | PatchServicesDHCPRelayEndpointResponse503
]:
    """<h3>Description:</h3>Updates current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPRelayEndpointJsonBody | Unset):
        body (PatchServicesDHCPRelayEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesDHCPRelayEndpointResponse400 | PatchServicesDHCPRelayEndpointResponse401 | PatchServicesDHCPRelayEndpointResponse403 | PatchServicesDHCPRelayEndpointResponse404 | PatchServicesDHCPRelayEndpointResponse405 | PatchServicesDHCPRelayEndpointResponse406 | PatchServicesDHCPRelayEndpointResponse409 | PatchServicesDHCPRelayEndpointResponse415 | PatchServicesDHCPRelayEndpointResponse422 | PatchServicesDHCPRelayEndpointResponse424 | PatchServicesDHCPRelayEndpointResponse500 | PatchServicesDHCPRelayEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesDHCPRelayEndpointJsonBody | PatchServicesDHCPRelayEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesDHCPRelayEndpointResponse400
    | PatchServicesDHCPRelayEndpointResponse401
    | PatchServicesDHCPRelayEndpointResponse403
    | PatchServicesDHCPRelayEndpointResponse404
    | PatchServicesDHCPRelayEndpointResponse405
    | PatchServicesDHCPRelayEndpointResponse406
    | PatchServicesDHCPRelayEndpointResponse409
    | PatchServicesDHCPRelayEndpointResponse415
    | PatchServicesDHCPRelayEndpointResponse422
    | PatchServicesDHCPRelayEndpointResponse424
    | PatchServicesDHCPRelayEndpointResponse500
    | PatchServicesDHCPRelayEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesDHCPRelayEndpointJsonBody | Unset):
        body (PatchServicesDHCPRelayEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesDHCPRelayEndpointResponse400 | PatchServicesDHCPRelayEndpointResponse401 | PatchServicesDHCPRelayEndpointResponse403 | PatchServicesDHCPRelayEndpointResponse404 | PatchServicesDHCPRelayEndpointResponse405 | PatchServicesDHCPRelayEndpointResponse406 | PatchServicesDHCPRelayEndpointResponse409 | PatchServicesDHCPRelayEndpointResponse415 | PatchServicesDHCPRelayEndpointResponse422 | PatchServicesDHCPRelayEndpointResponse424 | PatchServicesDHCPRelayEndpointResponse500 | PatchServicesDHCPRelayEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
