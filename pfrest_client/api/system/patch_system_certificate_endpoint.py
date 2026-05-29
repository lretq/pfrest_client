from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_certificate_endpoint_data_body import PatchSystemCertificateEndpointDataBody
from ...models.patch_system_certificate_endpoint_json_body import PatchSystemCertificateEndpointJsonBody
from ...models.patch_system_certificate_endpoint_response_400 import PatchSystemCertificateEndpointResponse400
from ...models.patch_system_certificate_endpoint_response_401 import PatchSystemCertificateEndpointResponse401
from ...models.patch_system_certificate_endpoint_response_403 import PatchSystemCertificateEndpointResponse403
from ...models.patch_system_certificate_endpoint_response_404 import PatchSystemCertificateEndpointResponse404
from ...models.patch_system_certificate_endpoint_response_405 import PatchSystemCertificateEndpointResponse405
from ...models.patch_system_certificate_endpoint_response_406 import PatchSystemCertificateEndpointResponse406
from ...models.patch_system_certificate_endpoint_response_409 import PatchSystemCertificateEndpointResponse409
from ...models.patch_system_certificate_endpoint_response_415 import PatchSystemCertificateEndpointResponse415
from ...models.patch_system_certificate_endpoint_response_422 import PatchSystemCertificateEndpointResponse422
from ...models.patch_system_certificate_endpoint_response_424 import PatchSystemCertificateEndpointResponse424
from ...models.patch_system_certificate_endpoint_response_500 import PatchSystemCertificateEndpointResponse500
from ...models.patch_system_certificate_endpoint_response_503 import PatchSystemCertificateEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemCertificateEndpointJsonBody | PatchSystemCertificateEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/certificate",
    }

    if isinstance(body, PatchSystemCertificateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemCertificateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemCertificateEndpointResponse400
    | PatchSystemCertificateEndpointResponse401
    | PatchSystemCertificateEndpointResponse403
    | PatchSystemCertificateEndpointResponse404
    | PatchSystemCertificateEndpointResponse405
    | PatchSystemCertificateEndpointResponse406
    | PatchSystemCertificateEndpointResponse409
    | PatchSystemCertificateEndpointResponse415
    | PatchSystemCertificateEndpointResponse422
    | PatchSystemCertificateEndpointResponse424
    | PatchSystemCertificateEndpointResponse500
    | PatchSystemCertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemCertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemCertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemCertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemCertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemCertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemCertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemCertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemCertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemCertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemCertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemCertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemCertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemCertificateEndpointResponse400
    | PatchSystemCertificateEndpointResponse401
    | PatchSystemCertificateEndpointResponse403
    | PatchSystemCertificateEndpointResponse404
    | PatchSystemCertificateEndpointResponse405
    | PatchSystemCertificateEndpointResponse406
    | PatchSystemCertificateEndpointResponse409
    | PatchSystemCertificateEndpointResponse415
    | PatchSystemCertificateEndpointResponse422
    | PatchSystemCertificateEndpointResponse424
    | PatchSystemCertificateEndpointResponse500
    | PatchSystemCertificateEndpointResponse503
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
    body: PatchSystemCertificateEndpointJsonBody | PatchSystemCertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemCertificateEndpointResponse400
    | PatchSystemCertificateEndpointResponse401
    | PatchSystemCertificateEndpointResponse403
    | PatchSystemCertificateEndpointResponse404
    | PatchSystemCertificateEndpointResponse405
    | PatchSystemCertificateEndpointResponse406
    | PatchSystemCertificateEndpointResponse409
    | PatchSystemCertificateEndpointResponse415
    | PatchSystemCertificateEndpointResponse422
    | PatchSystemCertificateEndpointResponse424
    | PatchSystemCertificateEndpointResponse500
    | PatchSystemCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateEndpointJsonBody | Unset):
        body (PatchSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemCertificateEndpointResponse400 | PatchSystemCertificateEndpointResponse401 | PatchSystemCertificateEndpointResponse403 | PatchSystemCertificateEndpointResponse404 | PatchSystemCertificateEndpointResponse405 | PatchSystemCertificateEndpointResponse406 | PatchSystemCertificateEndpointResponse409 | PatchSystemCertificateEndpointResponse415 | PatchSystemCertificateEndpointResponse422 | PatchSystemCertificateEndpointResponse424 | PatchSystemCertificateEndpointResponse500 | PatchSystemCertificateEndpointResponse503]
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
    body: PatchSystemCertificateEndpointJsonBody | PatchSystemCertificateEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemCertificateEndpointResponse400
    | PatchSystemCertificateEndpointResponse401
    | PatchSystemCertificateEndpointResponse403
    | PatchSystemCertificateEndpointResponse404
    | PatchSystemCertificateEndpointResponse405
    | PatchSystemCertificateEndpointResponse406
    | PatchSystemCertificateEndpointResponse409
    | PatchSystemCertificateEndpointResponse415
    | PatchSystemCertificateEndpointResponse422
    | PatchSystemCertificateEndpointResponse424
    | PatchSystemCertificateEndpointResponse500
    | PatchSystemCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateEndpointJsonBody | Unset):
        body (PatchSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemCertificateEndpointResponse400 | PatchSystemCertificateEndpointResponse401 | PatchSystemCertificateEndpointResponse403 | PatchSystemCertificateEndpointResponse404 | PatchSystemCertificateEndpointResponse405 | PatchSystemCertificateEndpointResponse406 | PatchSystemCertificateEndpointResponse409 | PatchSystemCertificateEndpointResponse415 | PatchSystemCertificateEndpointResponse422 | PatchSystemCertificateEndpointResponse424 | PatchSystemCertificateEndpointResponse500 | PatchSystemCertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemCertificateEndpointJsonBody | PatchSystemCertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemCertificateEndpointResponse400
    | PatchSystemCertificateEndpointResponse401
    | PatchSystemCertificateEndpointResponse403
    | PatchSystemCertificateEndpointResponse404
    | PatchSystemCertificateEndpointResponse405
    | PatchSystemCertificateEndpointResponse406
    | PatchSystemCertificateEndpointResponse409
    | PatchSystemCertificateEndpointResponse415
    | PatchSystemCertificateEndpointResponse422
    | PatchSystemCertificateEndpointResponse424
    | PatchSystemCertificateEndpointResponse500
    | PatchSystemCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateEndpointJsonBody | Unset):
        body (PatchSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemCertificateEndpointResponse400 | PatchSystemCertificateEndpointResponse401 | PatchSystemCertificateEndpointResponse403 | PatchSystemCertificateEndpointResponse404 | PatchSystemCertificateEndpointResponse405 | PatchSystemCertificateEndpointResponse406 | PatchSystemCertificateEndpointResponse409 | PatchSystemCertificateEndpointResponse415 | PatchSystemCertificateEndpointResponse422 | PatchSystemCertificateEndpointResponse424 | PatchSystemCertificateEndpointResponse500 | PatchSystemCertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemCertificateEndpointJsonBody | PatchSystemCertificateEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemCertificateEndpointResponse400
    | PatchSystemCertificateEndpointResponse401
    | PatchSystemCertificateEndpointResponse403
    | PatchSystemCertificateEndpointResponse404
    | PatchSystemCertificateEndpointResponse405
    | PatchSystemCertificateEndpointResponse406
    | PatchSystemCertificateEndpointResponse409
    | PatchSystemCertificateEndpointResponse415
    | PatchSystemCertificateEndpointResponse422
    | PatchSystemCertificateEndpointResponse424
    | PatchSystemCertificateEndpointResponse500
    | PatchSystemCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateEndpointJsonBody | Unset):
        body (PatchSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemCertificateEndpointResponse400 | PatchSystemCertificateEndpointResponse401 | PatchSystemCertificateEndpointResponse403 | PatchSystemCertificateEndpointResponse404 | PatchSystemCertificateEndpointResponse405 | PatchSystemCertificateEndpointResponse406 | PatchSystemCertificateEndpointResponse409 | PatchSystemCertificateEndpointResponse415 | PatchSystemCertificateEndpointResponse422 | PatchSystemCertificateEndpointResponse424 | PatchSystemCertificateEndpointResponse500 | PatchSystemCertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
