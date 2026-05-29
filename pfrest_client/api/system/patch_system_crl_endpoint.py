from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_crl_endpoint_data_body import PatchSystemCRLEndpointDataBody
from ...models.patch_system_crl_endpoint_json_body import PatchSystemCRLEndpointJsonBody
from ...models.patch_system_crl_endpoint_response_400 import PatchSystemCRLEndpointResponse400
from ...models.patch_system_crl_endpoint_response_401 import PatchSystemCRLEndpointResponse401
from ...models.patch_system_crl_endpoint_response_403 import PatchSystemCRLEndpointResponse403
from ...models.patch_system_crl_endpoint_response_404 import PatchSystemCRLEndpointResponse404
from ...models.patch_system_crl_endpoint_response_405 import PatchSystemCRLEndpointResponse405
from ...models.patch_system_crl_endpoint_response_406 import PatchSystemCRLEndpointResponse406
from ...models.patch_system_crl_endpoint_response_409 import PatchSystemCRLEndpointResponse409
from ...models.patch_system_crl_endpoint_response_415 import PatchSystemCRLEndpointResponse415
from ...models.patch_system_crl_endpoint_response_422 import PatchSystemCRLEndpointResponse422
from ...models.patch_system_crl_endpoint_response_424 import PatchSystemCRLEndpointResponse424
from ...models.patch_system_crl_endpoint_response_500 import PatchSystemCRLEndpointResponse500
from ...models.patch_system_crl_endpoint_response_503 import PatchSystemCRLEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemCRLEndpointJsonBody | PatchSystemCRLEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/crl",
    }

    if isinstance(body, PatchSystemCRLEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemCRLEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemCRLEndpointResponse400
    | PatchSystemCRLEndpointResponse401
    | PatchSystemCRLEndpointResponse403
    | PatchSystemCRLEndpointResponse404
    | PatchSystemCRLEndpointResponse405
    | PatchSystemCRLEndpointResponse406
    | PatchSystemCRLEndpointResponse409
    | PatchSystemCRLEndpointResponse415
    | PatchSystemCRLEndpointResponse422
    | PatchSystemCRLEndpointResponse424
    | PatchSystemCRLEndpointResponse500
    | PatchSystemCRLEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemCRLEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemCRLEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemCRLEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemCRLEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemCRLEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemCRLEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemCRLEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemCRLEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemCRLEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemCRLEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemCRLEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemCRLEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemCRLEndpointResponse400
    | PatchSystemCRLEndpointResponse401
    | PatchSystemCRLEndpointResponse403
    | PatchSystemCRLEndpointResponse404
    | PatchSystemCRLEndpointResponse405
    | PatchSystemCRLEndpointResponse406
    | PatchSystemCRLEndpointResponse409
    | PatchSystemCRLEndpointResponse415
    | PatchSystemCRLEndpointResponse422
    | PatchSystemCRLEndpointResponse424
    | PatchSystemCRLEndpointResponse500
    | PatchSystemCRLEndpointResponse503
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
    body: PatchSystemCRLEndpointJsonBody | PatchSystemCRLEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemCRLEndpointResponse400
    | PatchSystemCRLEndpointResponse401
    | PatchSystemCRLEndpointResponse403
    | PatchSystemCRLEndpointResponse404
    | PatchSystemCRLEndpointResponse405
    | PatchSystemCRLEndpointResponse406
    | PatchSystemCRLEndpointResponse409
    | PatchSystemCRLEndpointResponse415
    | PatchSystemCRLEndpointResponse422
    | PatchSystemCRLEndpointResponse424
    | PatchSystemCRLEndpointResponse500
    | PatchSystemCRLEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCRLEndpointJsonBody | Unset):
        body (PatchSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemCRLEndpointResponse400 | PatchSystemCRLEndpointResponse401 | PatchSystemCRLEndpointResponse403 | PatchSystemCRLEndpointResponse404 | PatchSystemCRLEndpointResponse405 | PatchSystemCRLEndpointResponse406 | PatchSystemCRLEndpointResponse409 | PatchSystemCRLEndpointResponse415 | PatchSystemCRLEndpointResponse422 | PatchSystemCRLEndpointResponse424 | PatchSystemCRLEndpointResponse500 | PatchSystemCRLEndpointResponse503]
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
    body: PatchSystemCRLEndpointJsonBody | PatchSystemCRLEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemCRLEndpointResponse400
    | PatchSystemCRLEndpointResponse401
    | PatchSystemCRLEndpointResponse403
    | PatchSystemCRLEndpointResponse404
    | PatchSystemCRLEndpointResponse405
    | PatchSystemCRLEndpointResponse406
    | PatchSystemCRLEndpointResponse409
    | PatchSystemCRLEndpointResponse415
    | PatchSystemCRLEndpointResponse422
    | PatchSystemCRLEndpointResponse424
    | PatchSystemCRLEndpointResponse500
    | PatchSystemCRLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCRLEndpointJsonBody | Unset):
        body (PatchSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemCRLEndpointResponse400 | PatchSystemCRLEndpointResponse401 | PatchSystemCRLEndpointResponse403 | PatchSystemCRLEndpointResponse404 | PatchSystemCRLEndpointResponse405 | PatchSystemCRLEndpointResponse406 | PatchSystemCRLEndpointResponse409 | PatchSystemCRLEndpointResponse415 | PatchSystemCRLEndpointResponse422 | PatchSystemCRLEndpointResponse424 | PatchSystemCRLEndpointResponse500 | PatchSystemCRLEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemCRLEndpointJsonBody | PatchSystemCRLEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemCRLEndpointResponse400
    | PatchSystemCRLEndpointResponse401
    | PatchSystemCRLEndpointResponse403
    | PatchSystemCRLEndpointResponse404
    | PatchSystemCRLEndpointResponse405
    | PatchSystemCRLEndpointResponse406
    | PatchSystemCRLEndpointResponse409
    | PatchSystemCRLEndpointResponse415
    | PatchSystemCRLEndpointResponse422
    | PatchSystemCRLEndpointResponse424
    | PatchSystemCRLEndpointResponse500
    | PatchSystemCRLEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCRLEndpointJsonBody | Unset):
        body (PatchSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemCRLEndpointResponse400 | PatchSystemCRLEndpointResponse401 | PatchSystemCRLEndpointResponse403 | PatchSystemCRLEndpointResponse404 | PatchSystemCRLEndpointResponse405 | PatchSystemCRLEndpointResponse406 | PatchSystemCRLEndpointResponse409 | PatchSystemCRLEndpointResponse415 | PatchSystemCRLEndpointResponse422 | PatchSystemCRLEndpointResponse424 | PatchSystemCRLEndpointResponse500 | PatchSystemCRLEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemCRLEndpointJsonBody | PatchSystemCRLEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemCRLEndpointResponse400
    | PatchSystemCRLEndpointResponse401
    | PatchSystemCRLEndpointResponse403
    | PatchSystemCRLEndpointResponse404
    | PatchSystemCRLEndpointResponse405
    | PatchSystemCRLEndpointResponse406
    | PatchSystemCRLEndpointResponse409
    | PatchSystemCRLEndpointResponse415
    | PatchSystemCRLEndpointResponse422
    | PatchSystemCRLEndpointResponse424
    | PatchSystemCRLEndpointResponse500
    | PatchSystemCRLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCRLEndpointJsonBody | Unset):
        body (PatchSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemCRLEndpointResponse400 | PatchSystemCRLEndpointResponse401 | PatchSystemCRLEndpointResponse403 | PatchSystemCRLEndpointResponse404 | PatchSystemCRLEndpointResponse405 | PatchSystemCRLEndpointResponse406 | PatchSystemCRLEndpointResponse409 | PatchSystemCRLEndpointResponse415 | PatchSystemCRLEndpointResponse422 | PatchSystemCRLEndpointResponse424 | PatchSystemCRLEndpointResponse500 | PatchSystemCRLEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
