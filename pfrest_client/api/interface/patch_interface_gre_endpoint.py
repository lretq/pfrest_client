from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_interface_gre_endpoint_data_body import PatchInterfaceGREEndpointDataBody
from ...models.patch_interface_gre_endpoint_json_body import PatchInterfaceGREEndpointJsonBody
from ...models.patch_interface_gre_endpoint_response_400 import PatchInterfaceGREEndpointResponse400
from ...models.patch_interface_gre_endpoint_response_401 import PatchInterfaceGREEndpointResponse401
from ...models.patch_interface_gre_endpoint_response_403 import PatchInterfaceGREEndpointResponse403
from ...models.patch_interface_gre_endpoint_response_404 import PatchInterfaceGREEndpointResponse404
from ...models.patch_interface_gre_endpoint_response_405 import PatchInterfaceGREEndpointResponse405
from ...models.patch_interface_gre_endpoint_response_406 import PatchInterfaceGREEndpointResponse406
from ...models.patch_interface_gre_endpoint_response_409 import PatchInterfaceGREEndpointResponse409
from ...models.patch_interface_gre_endpoint_response_415 import PatchInterfaceGREEndpointResponse415
from ...models.patch_interface_gre_endpoint_response_422 import PatchInterfaceGREEndpointResponse422
from ...models.patch_interface_gre_endpoint_response_424 import PatchInterfaceGREEndpointResponse424
from ...models.patch_interface_gre_endpoint_response_500 import PatchInterfaceGREEndpointResponse500
from ...models.patch_interface_gre_endpoint_response_503 import PatchInterfaceGREEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchInterfaceGREEndpointJsonBody | PatchInterfaceGREEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/interface/gre",
    }

    if isinstance(body, PatchInterfaceGREEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchInterfaceGREEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchInterfaceGREEndpointResponse400
    | PatchInterfaceGREEndpointResponse401
    | PatchInterfaceGREEndpointResponse403
    | PatchInterfaceGREEndpointResponse404
    | PatchInterfaceGREEndpointResponse405
    | PatchInterfaceGREEndpointResponse406
    | PatchInterfaceGREEndpointResponse409
    | PatchInterfaceGREEndpointResponse415
    | PatchInterfaceGREEndpointResponse422
    | PatchInterfaceGREEndpointResponse424
    | PatchInterfaceGREEndpointResponse500
    | PatchInterfaceGREEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchInterfaceGREEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchInterfaceGREEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchInterfaceGREEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchInterfaceGREEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchInterfaceGREEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchInterfaceGREEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchInterfaceGREEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchInterfaceGREEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchInterfaceGREEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchInterfaceGREEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchInterfaceGREEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchInterfaceGREEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchInterfaceGREEndpointResponse400
    | PatchInterfaceGREEndpointResponse401
    | PatchInterfaceGREEndpointResponse403
    | PatchInterfaceGREEndpointResponse404
    | PatchInterfaceGREEndpointResponse405
    | PatchInterfaceGREEndpointResponse406
    | PatchInterfaceGREEndpointResponse409
    | PatchInterfaceGREEndpointResponse415
    | PatchInterfaceGREEndpointResponse422
    | PatchInterfaceGREEndpointResponse424
    | PatchInterfaceGREEndpointResponse500
    | PatchInterfaceGREEndpointResponse503
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
    body: PatchInterfaceGREEndpointJsonBody | PatchInterfaceGREEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceGREEndpointResponse400
    | PatchInterfaceGREEndpointResponse401
    | PatchInterfaceGREEndpointResponse403
    | PatchInterfaceGREEndpointResponse404
    | PatchInterfaceGREEndpointResponse405
    | PatchInterfaceGREEndpointResponse406
    | PatchInterfaceGREEndpointResponse409
    | PatchInterfaceGREEndpointResponse415
    | PatchInterfaceGREEndpointResponse422
    | PatchInterfaceGREEndpointResponse424
    | PatchInterfaceGREEndpointResponse500
    | PatchInterfaceGREEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGREEndpointJsonBody | Unset):
        body (PatchInterfaceGREEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceGREEndpointResponse400 | PatchInterfaceGREEndpointResponse401 | PatchInterfaceGREEndpointResponse403 | PatchInterfaceGREEndpointResponse404 | PatchInterfaceGREEndpointResponse405 | PatchInterfaceGREEndpointResponse406 | PatchInterfaceGREEndpointResponse409 | PatchInterfaceGREEndpointResponse415 | PatchInterfaceGREEndpointResponse422 | PatchInterfaceGREEndpointResponse424 | PatchInterfaceGREEndpointResponse500 | PatchInterfaceGREEndpointResponse503]
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
    body: PatchInterfaceGREEndpointJsonBody | PatchInterfaceGREEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceGREEndpointResponse400
    | PatchInterfaceGREEndpointResponse401
    | PatchInterfaceGREEndpointResponse403
    | PatchInterfaceGREEndpointResponse404
    | PatchInterfaceGREEndpointResponse405
    | PatchInterfaceGREEndpointResponse406
    | PatchInterfaceGREEndpointResponse409
    | PatchInterfaceGREEndpointResponse415
    | PatchInterfaceGREEndpointResponse422
    | PatchInterfaceGREEndpointResponse424
    | PatchInterfaceGREEndpointResponse500
    | PatchInterfaceGREEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGREEndpointJsonBody | Unset):
        body (PatchInterfaceGREEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceGREEndpointResponse400 | PatchInterfaceGREEndpointResponse401 | PatchInterfaceGREEndpointResponse403 | PatchInterfaceGREEndpointResponse404 | PatchInterfaceGREEndpointResponse405 | PatchInterfaceGREEndpointResponse406 | PatchInterfaceGREEndpointResponse409 | PatchInterfaceGREEndpointResponse415 | PatchInterfaceGREEndpointResponse422 | PatchInterfaceGREEndpointResponse424 | PatchInterfaceGREEndpointResponse500 | PatchInterfaceGREEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceGREEndpointJsonBody | PatchInterfaceGREEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceGREEndpointResponse400
    | PatchInterfaceGREEndpointResponse401
    | PatchInterfaceGREEndpointResponse403
    | PatchInterfaceGREEndpointResponse404
    | PatchInterfaceGREEndpointResponse405
    | PatchInterfaceGREEndpointResponse406
    | PatchInterfaceGREEndpointResponse409
    | PatchInterfaceGREEndpointResponse415
    | PatchInterfaceGREEndpointResponse422
    | PatchInterfaceGREEndpointResponse424
    | PatchInterfaceGREEndpointResponse500
    | PatchInterfaceGREEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGREEndpointJsonBody | Unset):
        body (PatchInterfaceGREEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceGREEndpointResponse400 | PatchInterfaceGREEndpointResponse401 | PatchInterfaceGREEndpointResponse403 | PatchInterfaceGREEndpointResponse404 | PatchInterfaceGREEndpointResponse405 | PatchInterfaceGREEndpointResponse406 | PatchInterfaceGREEndpointResponse409 | PatchInterfaceGREEndpointResponse415 | PatchInterfaceGREEndpointResponse422 | PatchInterfaceGREEndpointResponse424 | PatchInterfaceGREEndpointResponse500 | PatchInterfaceGREEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceGREEndpointJsonBody | PatchInterfaceGREEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceGREEndpointResponse400
    | PatchInterfaceGREEndpointResponse401
    | PatchInterfaceGREEndpointResponse403
    | PatchInterfaceGREEndpointResponse404
    | PatchInterfaceGREEndpointResponse405
    | PatchInterfaceGREEndpointResponse406
    | PatchInterfaceGREEndpointResponse409
    | PatchInterfaceGREEndpointResponse415
    | PatchInterfaceGREEndpointResponse422
    | PatchInterfaceGREEndpointResponse424
    | PatchInterfaceGREEndpointResponse500
    | PatchInterfaceGREEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGREEndpointJsonBody | Unset):
        body (PatchInterfaceGREEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceGREEndpointResponse400 | PatchInterfaceGREEndpointResponse401 | PatchInterfaceGREEndpointResponse403 | PatchInterfaceGREEndpointResponse404 | PatchInterfaceGREEndpointResponse405 | PatchInterfaceGREEndpointResponse406 | PatchInterfaceGREEndpointResponse409 | PatchInterfaceGREEndpointResponse415 | PatchInterfaceGREEndpointResponse422 | PatchInterfaceGREEndpointResponse424 | PatchInterfaceGREEndpointResponse500 | PatchInterfaceGREEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
