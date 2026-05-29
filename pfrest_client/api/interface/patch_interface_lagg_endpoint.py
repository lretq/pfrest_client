from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_interface_lagg_endpoint_data_body import PatchInterfaceLAGGEndpointDataBody
from ...models.patch_interface_lagg_endpoint_json_body import PatchInterfaceLAGGEndpointJsonBody
from ...models.patch_interface_lagg_endpoint_response_400 import PatchInterfaceLAGGEndpointResponse400
from ...models.patch_interface_lagg_endpoint_response_401 import PatchInterfaceLAGGEndpointResponse401
from ...models.patch_interface_lagg_endpoint_response_403 import PatchInterfaceLAGGEndpointResponse403
from ...models.patch_interface_lagg_endpoint_response_404 import PatchInterfaceLAGGEndpointResponse404
from ...models.patch_interface_lagg_endpoint_response_405 import PatchInterfaceLAGGEndpointResponse405
from ...models.patch_interface_lagg_endpoint_response_406 import PatchInterfaceLAGGEndpointResponse406
from ...models.patch_interface_lagg_endpoint_response_409 import PatchInterfaceLAGGEndpointResponse409
from ...models.patch_interface_lagg_endpoint_response_415 import PatchInterfaceLAGGEndpointResponse415
from ...models.patch_interface_lagg_endpoint_response_422 import PatchInterfaceLAGGEndpointResponse422
from ...models.patch_interface_lagg_endpoint_response_424 import PatchInterfaceLAGGEndpointResponse424
from ...models.patch_interface_lagg_endpoint_response_500 import PatchInterfaceLAGGEndpointResponse500
from ...models.patch_interface_lagg_endpoint_response_503 import PatchInterfaceLAGGEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchInterfaceLAGGEndpointJsonBody | PatchInterfaceLAGGEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/interface/lagg",
    }

    if isinstance(body, PatchInterfaceLAGGEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchInterfaceLAGGEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchInterfaceLAGGEndpointResponse400
    | PatchInterfaceLAGGEndpointResponse401
    | PatchInterfaceLAGGEndpointResponse403
    | PatchInterfaceLAGGEndpointResponse404
    | PatchInterfaceLAGGEndpointResponse405
    | PatchInterfaceLAGGEndpointResponse406
    | PatchInterfaceLAGGEndpointResponse409
    | PatchInterfaceLAGGEndpointResponse415
    | PatchInterfaceLAGGEndpointResponse422
    | PatchInterfaceLAGGEndpointResponse424
    | PatchInterfaceLAGGEndpointResponse500
    | PatchInterfaceLAGGEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchInterfaceLAGGEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchInterfaceLAGGEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchInterfaceLAGGEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchInterfaceLAGGEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchInterfaceLAGGEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchInterfaceLAGGEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchInterfaceLAGGEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchInterfaceLAGGEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchInterfaceLAGGEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchInterfaceLAGGEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchInterfaceLAGGEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchInterfaceLAGGEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchInterfaceLAGGEndpointResponse400
    | PatchInterfaceLAGGEndpointResponse401
    | PatchInterfaceLAGGEndpointResponse403
    | PatchInterfaceLAGGEndpointResponse404
    | PatchInterfaceLAGGEndpointResponse405
    | PatchInterfaceLAGGEndpointResponse406
    | PatchInterfaceLAGGEndpointResponse409
    | PatchInterfaceLAGGEndpointResponse415
    | PatchInterfaceLAGGEndpointResponse422
    | PatchInterfaceLAGGEndpointResponse424
    | PatchInterfaceLAGGEndpointResponse500
    | PatchInterfaceLAGGEndpointResponse503
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
    body: PatchInterfaceLAGGEndpointJsonBody | PatchInterfaceLAGGEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceLAGGEndpointResponse400
    | PatchInterfaceLAGGEndpointResponse401
    | PatchInterfaceLAGGEndpointResponse403
    | PatchInterfaceLAGGEndpointResponse404
    | PatchInterfaceLAGGEndpointResponse405
    | PatchInterfaceLAGGEndpointResponse406
    | PatchInterfaceLAGGEndpointResponse409
    | PatchInterfaceLAGGEndpointResponse415
    | PatchInterfaceLAGGEndpointResponse422
    | PatchInterfaceLAGGEndpointResponse424
    | PatchInterfaceLAGGEndpointResponse500
    | PatchInterfaceLAGGEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceLAGGEndpointJsonBody | Unset):
        body (PatchInterfaceLAGGEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceLAGGEndpointResponse400 | PatchInterfaceLAGGEndpointResponse401 | PatchInterfaceLAGGEndpointResponse403 | PatchInterfaceLAGGEndpointResponse404 | PatchInterfaceLAGGEndpointResponse405 | PatchInterfaceLAGGEndpointResponse406 | PatchInterfaceLAGGEndpointResponse409 | PatchInterfaceLAGGEndpointResponse415 | PatchInterfaceLAGGEndpointResponse422 | PatchInterfaceLAGGEndpointResponse424 | PatchInterfaceLAGGEndpointResponse500 | PatchInterfaceLAGGEndpointResponse503]
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
    body: PatchInterfaceLAGGEndpointJsonBody | PatchInterfaceLAGGEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceLAGGEndpointResponse400
    | PatchInterfaceLAGGEndpointResponse401
    | PatchInterfaceLAGGEndpointResponse403
    | PatchInterfaceLAGGEndpointResponse404
    | PatchInterfaceLAGGEndpointResponse405
    | PatchInterfaceLAGGEndpointResponse406
    | PatchInterfaceLAGGEndpointResponse409
    | PatchInterfaceLAGGEndpointResponse415
    | PatchInterfaceLAGGEndpointResponse422
    | PatchInterfaceLAGGEndpointResponse424
    | PatchInterfaceLAGGEndpointResponse500
    | PatchInterfaceLAGGEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceLAGGEndpointJsonBody | Unset):
        body (PatchInterfaceLAGGEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceLAGGEndpointResponse400 | PatchInterfaceLAGGEndpointResponse401 | PatchInterfaceLAGGEndpointResponse403 | PatchInterfaceLAGGEndpointResponse404 | PatchInterfaceLAGGEndpointResponse405 | PatchInterfaceLAGGEndpointResponse406 | PatchInterfaceLAGGEndpointResponse409 | PatchInterfaceLAGGEndpointResponse415 | PatchInterfaceLAGGEndpointResponse422 | PatchInterfaceLAGGEndpointResponse424 | PatchInterfaceLAGGEndpointResponse500 | PatchInterfaceLAGGEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceLAGGEndpointJsonBody | PatchInterfaceLAGGEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchInterfaceLAGGEndpointResponse400
    | PatchInterfaceLAGGEndpointResponse401
    | PatchInterfaceLAGGEndpointResponse403
    | PatchInterfaceLAGGEndpointResponse404
    | PatchInterfaceLAGGEndpointResponse405
    | PatchInterfaceLAGGEndpointResponse406
    | PatchInterfaceLAGGEndpointResponse409
    | PatchInterfaceLAGGEndpointResponse415
    | PatchInterfaceLAGGEndpointResponse422
    | PatchInterfaceLAGGEndpointResponse424
    | PatchInterfaceLAGGEndpointResponse500
    | PatchInterfaceLAGGEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceLAGGEndpointJsonBody | Unset):
        body (PatchInterfaceLAGGEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchInterfaceLAGGEndpointResponse400 | PatchInterfaceLAGGEndpointResponse401 | PatchInterfaceLAGGEndpointResponse403 | PatchInterfaceLAGGEndpointResponse404 | PatchInterfaceLAGGEndpointResponse405 | PatchInterfaceLAGGEndpointResponse406 | PatchInterfaceLAGGEndpointResponse409 | PatchInterfaceLAGGEndpointResponse415 | PatchInterfaceLAGGEndpointResponse422 | PatchInterfaceLAGGEndpointResponse424 | PatchInterfaceLAGGEndpointResponse500 | PatchInterfaceLAGGEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchInterfaceLAGGEndpointJsonBody | PatchInterfaceLAGGEndpointDataBody | Unset = UNSET,
) -> (
    PatchInterfaceLAGGEndpointResponse400
    | PatchInterfaceLAGGEndpointResponse401
    | PatchInterfaceLAGGEndpointResponse403
    | PatchInterfaceLAGGEndpointResponse404
    | PatchInterfaceLAGGEndpointResponse405
    | PatchInterfaceLAGGEndpointResponse406
    | PatchInterfaceLAGGEndpointResponse409
    | PatchInterfaceLAGGEndpointResponse415
    | PatchInterfaceLAGGEndpointResponse422
    | PatchInterfaceLAGGEndpointResponse424
    | PatchInterfaceLAGGEndpointResponse500
    | PatchInterfaceLAGGEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchInterfaceLAGGEndpointJsonBody | Unset):
        body (PatchInterfaceLAGGEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchInterfaceLAGGEndpointResponse400 | PatchInterfaceLAGGEndpointResponse401 | PatchInterfaceLAGGEndpointResponse403 | PatchInterfaceLAGGEndpointResponse404 | PatchInterfaceLAGGEndpointResponse405 | PatchInterfaceLAGGEndpointResponse406 | PatchInterfaceLAGGEndpointResponse409 | PatchInterfaceLAGGEndpointResponse415 | PatchInterfaceLAGGEndpointResponse422 | PatchInterfaceLAGGEndpointResponse424 | PatchInterfaceLAGGEndpointResponse500 | PatchInterfaceLAGGEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
