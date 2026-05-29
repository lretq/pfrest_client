from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_status_carp_endpoint_data_body import PatchStatusCARPEndpointDataBody
from ...models.patch_status_carp_endpoint_json_body import PatchStatusCARPEndpointJsonBody
from ...models.patch_status_carp_endpoint_response_400 import PatchStatusCARPEndpointResponse400
from ...models.patch_status_carp_endpoint_response_401 import PatchStatusCARPEndpointResponse401
from ...models.patch_status_carp_endpoint_response_403 import PatchStatusCARPEndpointResponse403
from ...models.patch_status_carp_endpoint_response_404 import PatchStatusCARPEndpointResponse404
from ...models.patch_status_carp_endpoint_response_405 import PatchStatusCARPEndpointResponse405
from ...models.patch_status_carp_endpoint_response_406 import PatchStatusCARPEndpointResponse406
from ...models.patch_status_carp_endpoint_response_409 import PatchStatusCARPEndpointResponse409
from ...models.patch_status_carp_endpoint_response_415 import PatchStatusCARPEndpointResponse415
from ...models.patch_status_carp_endpoint_response_422 import PatchStatusCARPEndpointResponse422
from ...models.patch_status_carp_endpoint_response_424 import PatchStatusCARPEndpointResponse424
from ...models.patch_status_carp_endpoint_response_500 import PatchStatusCARPEndpointResponse500
from ...models.patch_status_carp_endpoint_response_503 import PatchStatusCARPEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchStatusCARPEndpointJsonBody | PatchStatusCARPEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/status/carp",
    }

    if isinstance(body, PatchStatusCARPEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchStatusCARPEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchStatusCARPEndpointResponse400
    | PatchStatusCARPEndpointResponse401
    | PatchStatusCARPEndpointResponse403
    | PatchStatusCARPEndpointResponse404
    | PatchStatusCARPEndpointResponse405
    | PatchStatusCARPEndpointResponse406
    | PatchStatusCARPEndpointResponse409
    | PatchStatusCARPEndpointResponse415
    | PatchStatusCARPEndpointResponse422
    | PatchStatusCARPEndpointResponse424
    | PatchStatusCARPEndpointResponse500
    | PatchStatusCARPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchStatusCARPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchStatusCARPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchStatusCARPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchStatusCARPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchStatusCARPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchStatusCARPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchStatusCARPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchStatusCARPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchStatusCARPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchStatusCARPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchStatusCARPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchStatusCARPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchStatusCARPEndpointResponse400
    | PatchStatusCARPEndpointResponse401
    | PatchStatusCARPEndpointResponse403
    | PatchStatusCARPEndpointResponse404
    | PatchStatusCARPEndpointResponse405
    | PatchStatusCARPEndpointResponse406
    | PatchStatusCARPEndpointResponse409
    | PatchStatusCARPEndpointResponse415
    | PatchStatusCARPEndpointResponse422
    | PatchStatusCARPEndpointResponse424
    | PatchStatusCARPEndpointResponse500
    | PatchStatusCARPEndpointResponse503
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
    body: PatchStatusCARPEndpointJsonBody | PatchStatusCARPEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchStatusCARPEndpointResponse400
    | PatchStatusCARPEndpointResponse401
    | PatchStatusCARPEndpointResponse403
    | PatchStatusCARPEndpointResponse404
    | PatchStatusCARPEndpointResponse405
    | PatchStatusCARPEndpointResponse406
    | PatchStatusCARPEndpointResponse409
    | PatchStatusCARPEndpointResponse415
    | PatchStatusCARPEndpointResponse422
    | PatchStatusCARPEndpointResponse424
    | PatchStatusCARPEndpointResponse500
    | PatchStatusCARPEndpointResponse503
]:
    """<h3>Description:</h3>Updates current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchStatusCARPEndpointJsonBody | Unset):
        body (PatchStatusCARPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchStatusCARPEndpointResponse400 | PatchStatusCARPEndpointResponse401 | PatchStatusCARPEndpointResponse403 | PatchStatusCARPEndpointResponse404 | PatchStatusCARPEndpointResponse405 | PatchStatusCARPEndpointResponse406 | PatchStatusCARPEndpointResponse409 | PatchStatusCARPEndpointResponse415 | PatchStatusCARPEndpointResponse422 | PatchStatusCARPEndpointResponse424 | PatchStatusCARPEndpointResponse500 | PatchStatusCARPEndpointResponse503]
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
    body: PatchStatusCARPEndpointJsonBody | PatchStatusCARPEndpointDataBody | Unset = UNSET,
) -> (
    PatchStatusCARPEndpointResponse400
    | PatchStatusCARPEndpointResponse401
    | PatchStatusCARPEndpointResponse403
    | PatchStatusCARPEndpointResponse404
    | PatchStatusCARPEndpointResponse405
    | PatchStatusCARPEndpointResponse406
    | PatchStatusCARPEndpointResponse409
    | PatchStatusCARPEndpointResponse415
    | PatchStatusCARPEndpointResponse422
    | PatchStatusCARPEndpointResponse424
    | PatchStatusCARPEndpointResponse500
    | PatchStatusCARPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchStatusCARPEndpointJsonBody | Unset):
        body (PatchStatusCARPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchStatusCARPEndpointResponse400 | PatchStatusCARPEndpointResponse401 | PatchStatusCARPEndpointResponse403 | PatchStatusCARPEndpointResponse404 | PatchStatusCARPEndpointResponse405 | PatchStatusCARPEndpointResponse406 | PatchStatusCARPEndpointResponse409 | PatchStatusCARPEndpointResponse415 | PatchStatusCARPEndpointResponse422 | PatchStatusCARPEndpointResponse424 | PatchStatusCARPEndpointResponse500 | PatchStatusCARPEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchStatusCARPEndpointJsonBody | PatchStatusCARPEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchStatusCARPEndpointResponse400
    | PatchStatusCARPEndpointResponse401
    | PatchStatusCARPEndpointResponse403
    | PatchStatusCARPEndpointResponse404
    | PatchStatusCARPEndpointResponse405
    | PatchStatusCARPEndpointResponse406
    | PatchStatusCARPEndpointResponse409
    | PatchStatusCARPEndpointResponse415
    | PatchStatusCARPEndpointResponse422
    | PatchStatusCARPEndpointResponse424
    | PatchStatusCARPEndpointResponse500
    | PatchStatusCARPEndpointResponse503
]:
    """<h3>Description:</h3>Updates current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchStatusCARPEndpointJsonBody | Unset):
        body (PatchStatusCARPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchStatusCARPEndpointResponse400 | PatchStatusCARPEndpointResponse401 | PatchStatusCARPEndpointResponse403 | PatchStatusCARPEndpointResponse404 | PatchStatusCARPEndpointResponse405 | PatchStatusCARPEndpointResponse406 | PatchStatusCARPEndpointResponse409 | PatchStatusCARPEndpointResponse415 | PatchStatusCARPEndpointResponse422 | PatchStatusCARPEndpointResponse424 | PatchStatusCARPEndpointResponse500 | PatchStatusCARPEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchStatusCARPEndpointJsonBody | PatchStatusCARPEndpointDataBody | Unset = UNSET,
) -> (
    PatchStatusCARPEndpointResponse400
    | PatchStatusCARPEndpointResponse401
    | PatchStatusCARPEndpointResponse403
    | PatchStatusCARPEndpointResponse404
    | PatchStatusCARPEndpointResponse405
    | PatchStatusCARPEndpointResponse406
    | PatchStatusCARPEndpointResponse409
    | PatchStatusCARPEndpointResponse415
    | PatchStatusCARPEndpointResponse422
    | PatchStatusCARPEndpointResponse424
    | PatchStatusCARPEndpointResponse500
    | PatchStatusCARPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchStatusCARPEndpointJsonBody | Unset):
        body (PatchStatusCARPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchStatusCARPEndpointResponse400 | PatchStatusCARPEndpointResponse401 | PatchStatusCARPEndpointResponse403 | PatchStatusCARPEndpointResponse404 | PatchStatusCARPEndpointResponse405 | PatchStatusCARPEndpointResponse406 | PatchStatusCARPEndpointResponse409 | PatchStatusCARPEndpointResponse415 | PatchStatusCARPEndpointResponse422 | PatchStatusCARPEndpointResponse424 | PatchStatusCARPEndpointResponse500 | PatchStatusCARPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
