from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_interface_bridge_endpoint_data_body import PatchInterfaceBridgeEndpointDataBody
from ...models.patch_interface_bridge_endpoint_json_body import PatchInterfaceBridgeEndpointJsonBody
from ...models.patch_interface_bridge_endpoint_response_400 import PatchInterfaceBridgeEndpointResponse400
from ...models.patch_interface_bridge_endpoint_response_401 import PatchInterfaceBridgeEndpointResponse401
from ...models.patch_interface_bridge_endpoint_response_403 import PatchInterfaceBridgeEndpointResponse403
from ...models.patch_interface_bridge_endpoint_response_404 import PatchInterfaceBridgeEndpointResponse404
from ...models.patch_interface_bridge_endpoint_response_405 import PatchInterfaceBridgeEndpointResponse405
from ...models.patch_interface_bridge_endpoint_response_406 import PatchInterfaceBridgeEndpointResponse406
from ...models.patch_interface_bridge_endpoint_response_409 import PatchInterfaceBridgeEndpointResponse409
from ...models.patch_interface_bridge_endpoint_response_415 import PatchInterfaceBridgeEndpointResponse415
from ...models.patch_interface_bridge_endpoint_response_422 import PatchInterfaceBridgeEndpointResponse422
from ...models.patch_interface_bridge_endpoint_response_424 import PatchInterfaceBridgeEndpointResponse424
from ...models.patch_interface_bridge_endpoint_response_500 import PatchInterfaceBridgeEndpointResponse500
from ...models.patch_interface_bridge_endpoint_response_503 import PatchInterfaceBridgeEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchInterfaceBridgeEndpointJsonBody | PatchInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/interface/bridge",
    }

    if isinstance(body, PatchInterfaceBridgeEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchInterfaceBridgeEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchInterfaceBridgeEndpointResponse400
    | PatchInterfaceBridgeEndpointResponse401
    | PatchInterfaceBridgeEndpointResponse403
    | PatchInterfaceBridgeEndpointResponse404
    | PatchInterfaceBridgeEndpointResponse405
    | PatchInterfaceBridgeEndpointResponse406
    | PatchInterfaceBridgeEndpointResponse409
    | PatchInterfaceBridgeEndpointResponse415
    | PatchInterfaceBridgeEndpointResponse422
    | PatchInterfaceBridgeEndpointResponse424
    | PatchInterfaceBridgeEndpointResponse500
    | PatchInterfaceBridgeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchInterfaceBridgeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchInterfaceBridgeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchInterfaceBridgeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchInterfaceBridgeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchInterfaceBridgeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchInterfaceBridgeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchInterfaceBridgeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchInterfaceBridgeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchInterfaceBridgeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchInterfaceBridgeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchInterfaceBridgeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchInterfaceBridgeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchInterfaceBridgeEndpointResponse400
    | PatchInterfaceBridgeEndpointResponse401
    | PatchInterfaceBridgeEndpointResponse403
    | PatchInterfaceBridgeEndpointResponse404
    | PatchInterfaceBridgeEndpointResponse405
    | PatchInterfaceBridgeEndpointResponse406
    | PatchInterfaceBridgeEndpointResponse409
    | PatchInterfaceBridgeEndpointResponse415
    | PatchInterfaceBridgeEndpointResponse422
    | PatchInterfaceBridgeEndpointResponse424
    | PatchInterfaceBridgeEndpointResponse500
    | PatchInterfaceBridgeEndpointResponse503
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
    body: PatchInterfaceBridgeEndpointJsonBody | PatchInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceBridgeEndpointResponse400
    | PatchInterfaceBridgeEndpointResponse401
    | PatchInterfaceBridgeEndpointResponse403
    | PatchInterfaceBridgeEndpointResponse404
    | PatchInterfaceBridgeEndpointResponse405
    | PatchInterfaceBridgeEndpointResponse406
    | PatchInterfaceBridgeEndpointResponse409
    | PatchInterfaceBridgeEndpointResponse415
    | PatchInterfaceBridgeEndpointResponse422
    | PatchInterfaceBridgeEndpointResponse424
    | PatchInterfaceBridgeEndpointResponse500
    | PatchInterfaceBridgeEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceBridgeEndpointJsonBody | Unset):
        body (PatchInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceBridgeEndpointResponse400 | PatchInterfaceBridgeEndpointResponse401 | PatchInterfaceBridgeEndpointResponse403 | PatchInterfaceBridgeEndpointResponse404 | PatchInterfaceBridgeEndpointResponse405 | PatchInterfaceBridgeEndpointResponse406 | PatchInterfaceBridgeEndpointResponse409 | PatchInterfaceBridgeEndpointResponse415 | PatchInterfaceBridgeEndpointResponse422 | PatchInterfaceBridgeEndpointResponse424 | PatchInterfaceBridgeEndpointResponse500 | PatchInterfaceBridgeEndpointResponse503]
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
    body: PatchInterfaceBridgeEndpointJsonBody | PatchInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceBridgeEndpointResponse400
    | PatchInterfaceBridgeEndpointResponse401
    | PatchInterfaceBridgeEndpointResponse403
    | PatchInterfaceBridgeEndpointResponse404
    | PatchInterfaceBridgeEndpointResponse405
    | PatchInterfaceBridgeEndpointResponse406
    | PatchInterfaceBridgeEndpointResponse409
    | PatchInterfaceBridgeEndpointResponse415
    | PatchInterfaceBridgeEndpointResponse422
    | PatchInterfaceBridgeEndpointResponse424
    | PatchInterfaceBridgeEndpointResponse500
    | PatchInterfaceBridgeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceBridgeEndpointJsonBody | Unset):
        body (PatchInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceBridgeEndpointResponse400 | PatchInterfaceBridgeEndpointResponse401 | PatchInterfaceBridgeEndpointResponse403 | PatchInterfaceBridgeEndpointResponse404 | PatchInterfaceBridgeEndpointResponse405 | PatchInterfaceBridgeEndpointResponse406 | PatchInterfaceBridgeEndpointResponse409 | PatchInterfaceBridgeEndpointResponse415 | PatchInterfaceBridgeEndpointResponse422 | PatchInterfaceBridgeEndpointResponse424 | PatchInterfaceBridgeEndpointResponse500 | PatchInterfaceBridgeEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceBridgeEndpointJsonBody | PatchInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceBridgeEndpointResponse400
    | PatchInterfaceBridgeEndpointResponse401
    | PatchInterfaceBridgeEndpointResponse403
    | PatchInterfaceBridgeEndpointResponse404
    | PatchInterfaceBridgeEndpointResponse405
    | PatchInterfaceBridgeEndpointResponse406
    | PatchInterfaceBridgeEndpointResponse409
    | PatchInterfaceBridgeEndpointResponse415
    | PatchInterfaceBridgeEndpointResponse422
    | PatchInterfaceBridgeEndpointResponse424
    | PatchInterfaceBridgeEndpointResponse500
    | PatchInterfaceBridgeEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceBridgeEndpointJsonBody | Unset):
        body (PatchInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceBridgeEndpointResponse400 | PatchInterfaceBridgeEndpointResponse401 | PatchInterfaceBridgeEndpointResponse403 | PatchInterfaceBridgeEndpointResponse404 | PatchInterfaceBridgeEndpointResponse405 | PatchInterfaceBridgeEndpointResponse406 | PatchInterfaceBridgeEndpointResponse409 | PatchInterfaceBridgeEndpointResponse415 | PatchInterfaceBridgeEndpointResponse422 | PatchInterfaceBridgeEndpointResponse424 | PatchInterfaceBridgeEndpointResponse500 | PatchInterfaceBridgeEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceBridgeEndpointJsonBody | PatchInterfaceBridgeEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceBridgeEndpointResponse400
    | PatchInterfaceBridgeEndpointResponse401
    | PatchInterfaceBridgeEndpointResponse403
    | PatchInterfaceBridgeEndpointResponse404
    | PatchInterfaceBridgeEndpointResponse405
    | PatchInterfaceBridgeEndpointResponse406
    | PatchInterfaceBridgeEndpointResponse409
    | PatchInterfaceBridgeEndpointResponse415
    | PatchInterfaceBridgeEndpointResponse422
    | PatchInterfaceBridgeEndpointResponse424
    | PatchInterfaceBridgeEndpointResponse500
    | PatchInterfaceBridgeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceBridgeEndpointJsonBody | Unset):
        body (PatchInterfaceBridgeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceBridgeEndpointResponse400 | PatchInterfaceBridgeEndpointResponse401 | PatchInterfaceBridgeEndpointResponse403 | PatchInterfaceBridgeEndpointResponse404 | PatchInterfaceBridgeEndpointResponse405 | PatchInterfaceBridgeEndpointResponse406 | PatchInterfaceBridgeEndpointResponse409 | PatchInterfaceBridgeEndpointResponse415 | PatchInterfaceBridgeEndpointResponse422 | PatchInterfaceBridgeEndpointResponse424 | PatchInterfaceBridgeEndpointResponse500 | PatchInterfaceBridgeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
