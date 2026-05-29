from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_interface_vlan_endpoint_data_body import PatchInterfaceVLANEndpointDataBody
from ...models.patch_interface_vlan_endpoint_json_body import PatchInterfaceVLANEndpointJsonBody
from ...models.patch_interface_vlan_endpoint_response_400 import PatchInterfaceVLANEndpointResponse400
from ...models.patch_interface_vlan_endpoint_response_401 import PatchInterfaceVLANEndpointResponse401
from ...models.patch_interface_vlan_endpoint_response_403 import PatchInterfaceVLANEndpointResponse403
from ...models.patch_interface_vlan_endpoint_response_404 import PatchInterfaceVLANEndpointResponse404
from ...models.patch_interface_vlan_endpoint_response_405 import PatchInterfaceVLANEndpointResponse405
from ...models.patch_interface_vlan_endpoint_response_406 import PatchInterfaceVLANEndpointResponse406
from ...models.patch_interface_vlan_endpoint_response_409 import PatchInterfaceVLANEndpointResponse409
from ...models.patch_interface_vlan_endpoint_response_415 import PatchInterfaceVLANEndpointResponse415
from ...models.patch_interface_vlan_endpoint_response_422 import PatchInterfaceVLANEndpointResponse422
from ...models.patch_interface_vlan_endpoint_response_424 import PatchInterfaceVLANEndpointResponse424
from ...models.patch_interface_vlan_endpoint_response_500 import PatchInterfaceVLANEndpointResponse500
from ...models.patch_interface_vlan_endpoint_response_503 import PatchInterfaceVLANEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchInterfaceVLANEndpointJsonBody | PatchInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/interface/vlan",
    }

    if isinstance(body, PatchInterfaceVLANEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchInterfaceVLANEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchInterfaceVLANEndpointResponse400
    | PatchInterfaceVLANEndpointResponse401
    | PatchInterfaceVLANEndpointResponse403
    | PatchInterfaceVLANEndpointResponse404
    | PatchInterfaceVLANEndpointResponse405
    | PatchInterfaceVLANEndpointResponse406
    | PatchInterfaceVLANEndpointResponse409
    | PatchInterfaceVLANEndpointResponse415
    | PatchInterfaceVLANEndpointResponse422
    | PatchInterfaceVLANEndpointResponse424
    | PatchInterfaceVLANEndpointResponse500
    | PatchInterfaceVLANEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchInterfaceVLANEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchInterfaceVLANEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchInterfaceVLANEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchInterfaceVLANEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchInterfaceVLANEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchInterfaceVLANEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchInterfaceVLANEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchInterfaceVLANEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchInterfaceVLANEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchInterfaceVLANEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchInterfaceVLANEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchInterfaceVLANEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchInterfaceVLANEndpointResponse400
    | PatchInterfaceVLANEndpointResponse401
    | PatchInterfaceVLANEndpointResponse403
    | PatchInterfaceVLANEndpointResponse404
    | PatchInterfaceVLANEndpointResponse405
    | PatchInterfaceVLANEndpointResponse406
    | PatchInterfaceVLANEndpointResponse409
    | PatchInterfaceVLANEndpointResponse415
    | PatchInterfaceVLANEndpointResponse422
    | PatchInterfaceVLANEndpointResponse424
    | PatchInterfaceVLANEndpointResponse500
    | PatchInterfaceVLANEndpointResponse503
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
    body: PatchInterfaceVLANEndpointJsonBody | PatchInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceVLANEndpointResponse400
    | PatchInterfaceVLANEndpointResponse401
    | PatchInterfaceVLANEndpointResponse403
    | PatchInterfaceVLANEndpointResponse404
    | PatchInterfaceVLANEndpointResponse405
    | PatchInterfaceVLANEndpointResponse406
    | PatchInterfaceVLANEndpointResponse409
    | PatchInterfaceVLANEndpointResponse415
    | PatchInterfaceVLANEndpointResponse422
    | PatchInterfaceVLANEndpointResponse424
    | PatchInterfaceVLANEndpointResponse500
    | PatchInterfaceVLANEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceVLANEndpointJsonBody | Unset):
        body (PatchInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceVLANEndpointResponse400 | PatchInterfaceVLANEndpointResponse401 | PatchInterfaceVLANEndpointResponse403 | PatchInterfaceVLANEndpointResponse404 | PatchInterfaceVLANEndpointResponse405 | PatchInterfaceVLANEndpointResponse406 | PatchInterfaceVLANEndpointResponse409 | PatchInterfaceVLANEndpointResponse415 | PatchInterfaceVLANEndpointResponse422 | PatchInterfaceVLANEndpointResponse424 | PatchInterfaceVLANEndpointResponse500 | PatchInterfaceVLANEndpointResponse503]
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
    body: PatchInterfaceVLANEndpointJsonBody | PatchInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceVLANEndpointResponse400
    | PatchInterfaceVLANEndpointResponse401
    | PatchInterfaceVLANEndpointResponse403
    | PatchInterfaceVLANEndpointResponse404
    | PatchInterfaceVLANEndpointResponse405
    | PatchInterfaceVLANEndpointResponse406
    | PatchInterfaceVLANEndpointResponse409
    | PatchInterfaceVLANEndpointResponse415
    | PatchInterfaceVLANEndpointResponse422
    | PatchInterfaceVLANEndpointResponse424
    | PatchInterfaceVLANEndpointResponse500
    | PatchInterfaceVLANEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceVLANEndpointJsonBody | Unset):
        body (PatchInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceVLANEndpointResponse400 | PatchInterfaceVLANEndpointResponse401 | PatchInterfaceVLANEndpointResponse403 | PatchInterfaceVLANEndpointResponse404 | PatchInterfaceVLANEndpointResponse405 | PatchInterfaceVLANEndpointResponse406 | PatchInterfaceVLANEndpointResponse409 | PatchInterfaceVLANEndpointResponse415 | PatchInterfaceVLANEndpointResponse422 | PatchInterfaceVLANEndpointResponse424 | PatchInterfaceVLANEndpointResponse500 | PatchInterfaceVLANEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceVLANEndpointJsonBody | PatchInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceVLANEndpointResponse400
    | PatchInterfaceVLANEndpointResponse401
    | PatchInterfaceVLANEndpointResponse403
    | PatchInterfaceVLANEndpointResponse404
    | PatchInterfaceVLANEndpointResponse405
    | PatchInterfaceVLANEndpointResponse406
    | PatchInterfaceVLANEndpointResponse409
    | PatchInterfaceVLANEndpointResponse415
    | PatchInterfaceVLANEndpointResponse422
    | PatchInterfaceVLANEndpointResponse424
    | PatchInterfaceVLANEndpointResponse500
    | PatchInterfaceVLANEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceVLANEndpointJsonBody | Unset):
        body (PatchInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceVLANEndpointResponse400 | PatchInterfaceVLANEndpointResponse401 | PatchInterfaceVLANEndpointResponse403 | PatchInterfaceVLANEndpointResponse404 | PatchInterfaceVLANEndpointResponse405 | PatchInterfaceVLANEndpointResponse406 | PatchInterfaceVLANEndpointResponse409 | PatchInterfaceVLANEndpointResponse415 | PatchInterfaceVLANEndpointResponse422 | PatchInterfaceVLANEndpointResponse424 | PatchInterfaceVLANEndpointResponse500 | PatchInterfaceVLANEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceVLANEndpointJsonBody | PatchInterfaceVLANEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceVLANEndpointResponse400
    | PatchInterfaceVLANEndpointResponse401
    | PatchInterfaceVLANEndpointResponse403
    | PatchInterfaceVLANEndpointResponse404
    | PatchInterfaceVLANEndpointResponse405
    | PatchInterfaceVLANEndpointResponse406
    | PatchInterfaceVLANEndpointResponse409
    | PatchInterfaceVLANEndpointResponse415
    | PatchInterfaceVLANEndpointResponse422
    | PatchInterfaceVLANEndpointResponse424
    | PatchInterfaceVLANEndpointResponse500
    | PatchInterfaceVLANEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceVLANEndpointJsonBody | Unset):
        body (PatchInterfaceVLANEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceVLANEndpointResponse400 | PatchInterfaceVLANEndpointResponse401 | PatchInterfaceVLANEndpointResponse403 | PatchInterfaceVLANEndpointResponse404 | PatchInterfaceVLANEndpointResponse405 | PatchInterfaceVLANEndpointResponse406 | PatchInterfaceVLANEndpointResponse409 | PatchInterfaceVLANEndpointResponse415 | PatchInterfaceVLANEndpointResponse422 | PatchInterfaceVLANEndpointResponse424 | PatchInterfaceVLANEndpointResponse500 | PatchInterfaceVLANEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
