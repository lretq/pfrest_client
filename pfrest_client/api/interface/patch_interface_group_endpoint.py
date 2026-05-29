from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_interface_group_endpoint_data_body import PatchInterfaceGroupEndpointDataBody
from ...models.patch_interface_group_endpoint_json_body import PatchInterfaceGroupEndpointJsonBody
from ...models.patch_interface_group_endpoint_response_400 import PatchInterfaceGroupEndpointResponse400
from ...models.patch_interface_group_endpoint_response_401 import PatchInterfaceGroupEndpointResponse401
from ...models.patch_interface_group_endpoint_response_403 import PatchInterfaceGroupEndpointResponse403
from ...models.patch_interface_group_endpoint_response_404 import PatchInterfaceGroupEndpointResponse404
from ...models.patch_interface_group_endpoint_response_405 import PatchInterfaceGroupEndpointResponse405
from ...models.patch_interface_group_endpoint_response_406 import PatchInterfaceGroupEndpointResponse406
from ...models.patch_interface_group_endpoint_response_409 import PatchInterfaceGroupEndpointResponse409
from ...models.patch_interface_group_endpoint_response_415 import PatchInterfaceGroupEndpointResponse415
from ...models.patch_interface_group_endpoint_response_422 import PatchInterfaceGroupEndpointResponse422
from ...models.patch_interface_group_endpoint_response_424 import PatchInterfaceGroupEndpointResponse424
from ...models.patch_interface_group_endpoint_response_500 import PatchInterfaceGroupEndpointResponse500
from ...models.patch_interface_group_endpoint_response_503 import PatchInterfaceGroupEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchInterfaceGroupEndpointJsonBody | PatchInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/interface/group",
    }

    if isinstance(body, PatchInterfaceGroupEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchInterfaceGroupEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchInterfaceGroupEndpointResponse400
    | PatchInterfaceGroupEndpointResponse401
    | PatchInterfaceGroupEndpointResponse403
    | PatchInterfaceGroupEndpointResponse404
    | PatchInterfaceGroupEndpointResponse405
    | PatchInterfaceGroupEndpointResponse406
    | PatchInterfaceGroupEndpointResponse409
    | PatchInterfaceGroupEndpointResponse415
    | PatchInterfaceGroupEndpointResponse422
    | PatchInterfaceGroupEndpointResponse424
    | PatchInterfaceGroupEndpointResponse500
    | PatchInterfaceGroupEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchInterfaceGroupEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchInterfaceGroupEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchInterfaceGroupEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchInterfaceGroupEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchInterfaceGroupEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchInterfaceGroupEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchInterfaceGroupEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchInterfaceGroupEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchInterfaceGroupEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchInterfaceGroupEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchInterfaceGroupEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchInterfaceGroupEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchInterfaceGroupEndpointResponse400
    | PatchInterfaceGroupEndpointResponse401
    | PatchInterfaceGroupEndpointResponse403
    | PatchInterfaceGroupEndpointResponse404
    | PatchInterfaceGroupEndpointResponse405
    | PatchInterfaceGroupEndpointResponse406
    | PatchInterfaceGroupEndpointResponse409
    | PatchInterfaceGroupEndpointResponse415
    | PatchInterfaceGroupEndpointResponse422
    | PatchInterfaceGroupEndpointResponse424
    | PatchInterfaceGroupEndpointResponse500
    | PatchInterfaceGroupEndpointResponse503
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
    body: PatchInterfaceGroupEndpointJsonBody | PatchInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceGroupEndpointResponse400
    | PatchInterfaceGroupEndpointResponse401
    | PatchInterfaceGroupEndpointResponse403
    | PatchInterfaceGroupEndpointResponse404
    | PatchInterfaceGroupEndpointResponse405
    | PatchInterfaceGroupEndpointResponse406
    | PatchInterfaceGroupEndpointResponse409
    | PatchInterfaceGroupEndpointResponse415
    | PatchInterfaceGroupEndpointResponse422
    | PatchInterfaceGroupEndpointResponse424
    | PatchInterfaceGroupEndpointResponse500
    | PatchInterfaceGroupEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGroupEndpointJsonBody | Unset):
        body (PatchInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceGroupEndpointResponse400 | PatchInterfaceGroupEndpointResponse401 | PatchInterfaceGroupEndpointResponse403 | PatchInterfaceGroupEndpointResponse404 | PatchInterfaceGroupEndpointResponse405 | PatchInterfaceGroupEndpointResponse406 | PatchInterfaceGroupEndpointResponse409 | PatchInterfaceGroupEndpointResponse415 | PatchInterfaceGroupEndpointResponse422 | PatchInterfaceGroupEndpointResponse424 | PatchInterfaceGroupEndpointResponse500 | PatchInterfaceGroupEndpointResponse503]
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
    body: PatchInterfaceGroupEndpointJsonBody | PatchInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceGroupEndpointResponse400
    | PatchInterfaceGroupEndpointResponse401
    | PatchInterfaceGroupEndpointResponse403
    | PatchInterfaceGroupEndpointResponse404
    | PatchInterfaceGroupEndpointResponse405
    | PatchInterfaceGroupEndpointResponse406
    | PatchInterfaceGroupEndpointResponse409
    | PatchInterfaceGroupEndpointResponse415
    | PatchInterfaceGroupEndpointResponse422
    | PatchInterfaceGroupEndpointResponse424
    | PatchInterfaceGroupEndpointResponse500
    | PatchInterfaceGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGroupEndpointJsonBody | Unset):
        body (PatchInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceGroupEndpointResponse400 | PatchInterfaceGroupEndpointResponse401 | PatchInterfaceGroupEndpointResponse403 | PatchInterfaceGroupEndpointResponse404 | PatchInterfaceGroupEndpointResponse405 | PatchInterfaceGroupEndpointResponse406 | PatchInterfaceGroupEndpointResponse409 | PatchInterfaceGroupEndpointResponse415 | PatchInterfaceGroupEndpointResponse422 | PatchInterfaceGroupEndpointResponse424 | PatchInterfaceGroupEndpointResponse500 | PatchInterfaceGroupEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceGroupEndpointJsonBody | PatchInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceGroupEndpointResponse400
    | PatchInterfaceGroupEndpointResponse401
    | PatchInterfaceGroupEndpointResponse403
    | PatchInterfaceGroupEndpointResponse404
    | PatchInterfaceGroupEndpointResponse405
    | PatchInterfaceGroupEndpointResponse406
    | PatchInterfaceGroupEndpointResponse409
    | PatchInterfaceGroupEndpointResponse415
    | PatchInterfaceGroupEndpointResponse422
    | PatchInterfaceGroupEndpointResponse424
    | PatchInterfaceGroupEndpointResponse500
    | PatchInterfaceGroupEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGroupEndpointJsonBody | Unset):
        body (PatchInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceGroupEndpointResponse400 | PatchInterfaceGroupEndpointResponse401 | PatchInterfaceGroupEndpointResponse403 | PatchInterfaceGroupEndpointResponse404 | PatchInterfaceGroupEndpointResponse405 | PatchInterfaceGroupEndpointResponse406 | PatchInterfaceGroupEndpointResponse409 | PatchInterfaceGroupEndpointResponse415 | PatchInterfaceGroupEndpointResponse422 | PatchInterfaceGroupEndpointResponse424 | PatchInterfaceGroupEndpointResponse500 | PatchInterfaceGroupEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceGroupEndpointJsonBody | PatchInterfaceGroupEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceGroupEndpointResponse400
    | PatchInterfaceGroupEndpointResponse401
    | PatchInterfaceGroupEndpointResponse403
    | PatchInterfaceGroupEndpointResponse404
    | PatchInterfaceGroupEndpointResponse405
    | PatchInterfaceGroupEndpointResponse406
    | PatchInterfaceGroupEndpointResponse409
    | PatchInterfaceGroupEndpointResponse415
    | PatchInterfaceGroupEndpointResponse422
    | PatchInterfaceGroupEndpointResponse424
    | PatchInterfaceGroupEndpointResponse500
    | PatchInterfaceGroupEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceGroupEndpointJsonBody | Unset):
        body (PatchInterfaceGroupEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceGroupEndpointResponse400 | PatchInterfaceGroupEndpointResponse401 | PatchInterfaceGroupEndpointResponse403 | PatchInterfaceGroupEndpointResponse404 | PatchInterfaceGroupEndpointResponse405 | PatchInterfaceGroupEndpointResponse406 | PatchInterfaceGroupEndpointResponse409 | PatchInterfaceGroupEndpointResponse415 | PatchInterfaceGroupEndpointResponse422 | PatchInterfaceGroupEndpointResponse424 | PatchInterfaceGroupEndpointResponse500 | PatchInterfaceGroupEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
