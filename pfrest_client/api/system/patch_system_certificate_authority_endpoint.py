from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_certificate_authority_endpoint_data_body import (
    PatchSystemCertificateAuthorityEndpointDataBody,
)
from ...models.patch_system_certificate_authority_endpoint_json_body import (
    PatchSystemCertificateAuthorityEndpointJsonBody,
)
from ...models.patch_system_certificate_authority_endpoint_response_400 import (
    PatchSystemCertificateAuthorityEndpointResponse400,
)
from ...models.patch_system_certificate_authority_endpoint_response_401 import (
    PatchSystemCertificateAuthorityEndpointResponse401,
)
from ...models.patch_system_certificate_authority_endpoint_response_403 import (
    PatchSystemCertificateAuthorityEndpointResponse403,
)
from ...models.patch_system_certificate_authority_endpoint_response_404 import (
    PatchSystemCertificateAuthorityEndpointResponse404,
)
from ...models.patch_system_certificate_authority_endpoint_response_405 import (
    PatchSystemCertificateAuthorityEndpointResponse405,
)
from ...models.patch_system_certificate_authority_endpoint_response_406 import (
    PatchSystemCertificateAuthorityEndpointResponse406,
)
from ...models.patch_system_certificate_authority_endpoint_response_409 import (
    PatchSystemCertificateAuthorityEndpointResponse409,
)
from ...models.patch_system_certificate_authority_endpoint_response_415 import (
    PatchSystemCertificateAuthorityEndpointResponse415,
)
from ...models.patch_system_certificate_authority_endpoint_response_422 import (
    PatchSystemCertificateAuthorityEndpointResponse422,
)
from ...models.patch_system_certificate_authority_endpoint_response_424 import (
    PatchSystemCertificateAuthorityEndpointResponse424,
)
from ...models.patch_system_certificate_authority_endpoint_response_500 import (
    PatchSystemCertificateAuthorityEndpointResponse500,
)
from ...models.patch_system_certificate_authority_endpoint_response_503 import (
    PatchSystemCertificateAuthorityEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemCertificateAuthorityEndpointJsonBody
    | PatchSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/certificate_authority",
    }

    if isinstance(body, PatchSystemCertificateAuthorityEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemCertificateAuthorityEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemCertificateAuthorityEndpointResponse400
    | PatchSystemCertificateAuthorityEndpointResponse401
    | PatchSystemCertificateAuthorityEndpointResponse403
    | PatchSystemCertificateAuthorityEndpointResponse404
    | PatchSystemCertificateAuthorityEndpointResponse405
    | PatchSystemCertificateAuthorityEndpointResponse406
    | PatchSystemCertificateAuthorityEndpointResponse409
    | PatchSystemCertificateAuthorityEndpointResponse415
    | PatchSystemCertificateAuthorityEndpointResponse422
    | PatchSystemCertificateAuthorityEndpointResponse424
    | PatchSystemCertificateAuthorityEndpointResponse500
    | PatchSystemCertificateAuthorityEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemCertificateAuthorityEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemCertificateAuthorityEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemCertificateAuthorityEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemCertificateAuthorityEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemCertificateAuthorityEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemCertificateAuthorityEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemCertificateAuthorityEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemCertificateAuthorityEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemCertificateAuthorityEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemCertificateAuthorityEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemCertificateAuthorityEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemCertificateAuthorityEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemCertificateAuthorityEndpointResponse400
    | PatchSystemCertificateAuthorityEndpointResponse401
    | PatchSystemCertificateAuthorityEndpointResponse403
    | PatchSystemCertificateAuthorityEndpointResponse404
    | PatchSystemCertificateAuthorityEndpointResponse405
    | PatchSystemCertificateAuthorityEndpointResponse406
    | PatchSystemCertificateAuthorityEndpointResponse409
    | PatchSystemCertificateAuthorityEndpointResponse415
    | PatchSystemCertificateAuthorityEndpointResponse422
    | PatchSystemCertificateAuthorityEndpointResponse424
    | PatchSystemCertificateAuthorityEndpointResponse500
    | PatchSystemCertificateAuthorityEndpointResponse503
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
    body: PatchSystemCertificateAuthorityEndpointJsonBody
    | PatchSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchSystemCertificateAuthorityEndpointResponse400
    | PatchSystemCertificateAuthorityEndpointResponse401
    | PatchSystemCertificateAuthorityEndpointResponse403
    | PatchSystemCertificateAuthorityEndpointResponse404
    | PatchSystemCertificateAuthorityEndpointResponse405
    | PatchSystemCertificateAuthorityEndpointResponse406
    | PatchSystemCertificateAuthorityEndpointResponse409
    | PatchSystemCertificateAuthorityEndpointResponse415
    | PatchSystemCertificateAuthorityEndpointResponse422
    | PatchSystemCertificateAuthorityEndpointResponse424
    | PatchSystemCertificateAuthorityEndpointResponse500
    | PatchSystemCertificateAuthorityEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PatchSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemCertificateAuthorityEndpointResponse400 | PatchSystemCertificateAuthorityEndpointResponse401 | PatchSystemCertificateAuthorityEndpointResponse403 | PatchSystemCertificateAuthorityEndpointResponse404 | PatchSystemCertificateAuthorityEndpointResponse405 | PatchSystemCertificateAuthorityEndpointResponse406 | PatchSystemCertificateAuthorityEndpointResponse409 | PatchSystemCertificateAuthorityEndpointResponse415 | PatchSystemCertificateAuthorityEndpointResponse422 | PatchSystemCertificateAuthorityEndpointResponse424 | PatchSystemCertificateAuthorityEndpointResponse500 | PatchSystemCertificateAuthorityEndpointResponse503]
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
    body: PatchSystemCertificateAuthorityEndpointJsonBody
    | PatchSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchSystemCertificateAuthorityEndpointResponse400
    | PatchSystemCertificateAuthorityEndpointResponse401
    | PatchSystemCertificateAuthorityEndpointResponse403
    | PatchSystemCertificateAuthorityEndpointResponse404
    | PatchSystemCertificateAuthorityEndpointResponse405
    | PatchSystemCertificateAuthorityEndpointResponse406
    | PatchSystemCertificateAuthorityEndpointResponse409
    | PatchSystemCertificateAuthorityEndpointResponse415
    | PatchSystemCertificateAuthorityEndpointResponse422
    | PatchSystemCertificateAuthorityEndpointResponse424
    | PatchSystemCertificateAuthorityEndpointResponse500
    | PatchSystemCertificateAuthorityEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PatchSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemCertificateAuthorityEndpointResponse400 | PatchSystemCertificateAuthorityEndpointResponse401 | PatchSystemCertificateAuthorityEndpointResponse403 | PatchSystemCertificateAuthorityEndpointResponse404 | PatchSystemCertificateAuthorityEndpointResponse405 | PatchSystemCertificateAuthorityEndpointResponse406 | PatchSystemCertificateAuthorityEndpointResponse409 | PatchSystemCertificateAuthorityEndpointResponse415 | PatchSystemCertificateAuthorityEndpointResponse422 | PatchSystemCertificateAuthorityEndpointResponse424 | PatchSystemCertificateAuthorityEndpointResponse500 | PatchSystemCertificateAuthorityEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemCertificateAuthorityEndpointJsonBody
    | PatchSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchSystemCertificateAuthorityEndpointResponse400
    | PatchSystemCertificateAuthorityEndpointResponse401
    | PatchSystemCertificateAuthorityEndpointResponse403
    | PatchSystemCertificateAuthorityEndpointResponse404
    | PatchSystemCertificateAuthorityEndpointResponse405
    | PatchSystemCertificateAuthorityEndpointResponse406
    | PatchSystemCertificateAuthorityEndpointResponse409
    | PatchSystemCertificateAuthorityEndpointResponse415
    | PatchSystemCertificateAuthorityEndpointResponse422
    | PatchSystemCertificateAuthorityEndpointResponse424
    | PatchSystemCertificateAuthorityEndpointResponse500
    | PatchSystemCertificateAuthorityEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PatchSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemCertificateAuthorityEndpointResponse400 | PatchSystemCertificateAuthorityEndpointResponse401 | PatchSystemCertificateAuthorityEndpointResponse403 | PatchSystemCertificateAuthorityEndpointResponse404 | PatchSystemCertificateAuthorityEndpointResponse405 | PatchSystemCertificateAuthorityEndpointResponse406 | PatchSystemCertificateAuthorityEndpointResponse409 | PatchSystemCertificateAuthorityEndpointResponse415 | PatchSystemCertificateAuthorityEndpointResponse422 | PatchSystemCertificateAuthorityEndpointResponse424 | PatchSystemCertificateAuthorityEndpointResponse500 | PatchSystemCertificateAuthorityEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemCertificateAuthorityEndpointJsonBody
    | PatchSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchSystemCertificateAuthorityEndpointResponse400
    | PatchSystemCertificateAuthorityEndpointResponse401
    | PatchSystemCertificateAuthorityEndpointResponse403
    | PatchSystemCertificateAuthorityEndpointResponse404
    | PatchSystemCertificateAuthorityEndpointResponse405
    | PatchSystemCertificateAuthorityEndpointResponse406
    | PatchSystemCertificateAuthorityEndpointResponse409
    | PatchSystemCertificateAuthorityEndpointResponse415
    | PatchSystemCertificateAuthorityEndpointResponse422
    | PatchSystemCertificateAuthorityEndpointResponse424
    | PatchSystemCertificateAuthorityEndpointResponse500
    | PatchSystemCertificateAuthorityEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PatchSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemCertificateAuthorityEndpointResponse400 | PatchSystemCertificateAuthorityEndpointResponse401 | PatchSystemCertificateAuthorityEndpointResponse403 | PatchSystemCertificateAuthorityEndpointResponse404 | PatchSystemCertificateAuthorityEndpointResponse405 | PatchSystemCertificateAuthorityEndpointResponse406 | PatchSystemCertificateAuthorityEndpointResponse409 | PatchSystemCertificateAuthorityEndpointResponse415 | PatchSystemCertificateAuthorityEndpointResponse422 | PatchSystemCertificateAuthorityEndpointResponse424 | PatchSystemCertificateAuthorityEndpointResponse500 | PatchSystemCertificateAuthorityEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
