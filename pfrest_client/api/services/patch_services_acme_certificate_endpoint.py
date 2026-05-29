from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_acme_certificate_endpoint_data_body import PatchServicesACMECertificateEndpointDataBody
from ...models.patch_services_acme_certificate_endpoint_json_body import PatchServicesACMECertificateEndpointJsonBody
from ...models.patch_services_acme_certificate_endpoint_response_400 import (
    PatchServicesACMECertificateEndpointResponse400,
)
from ...models.patch_services_acme_certificate_endpoint_response_401 import (
    PatchServicesACMECertificateEndpointResponse401,
)
from ...models.patch_services_acme_certificate_endpoint_response_403 import (
    PatchServicesACMECertificateEndpointResponse403,
)
from ...models.patch_services_acme_certificate_endpoint_response_404 import (
    PatchServicesACMECertificateEndpointResponse404,
)
from ...models.patch_services_acme_certificate_endpoint_response_405 import (
    PatchServicesACMECertificateEndpointResponse405,
)
from ...models.patch_services_acme_certificate_endpoint_response_406 import (
    PatchServicesACMECertificateEndpointResponse406,
)
from ...models.patch_services_acme_certificate_endpoint_response_409 import (
    PatchServicesACMECertificateEndpointResponse409,
)
from ...models.patch_services_acme_certificate_endpoint_response_415 import (
    PatchServicesACMECertificateEndpointResponse415,
)
from ...models.patch_services_acme_certificate_endpoint_response_422 import (
    PatchServicesACMECertificateEndpointResponse422,
)
from ...models.patch_services_acme_certificate_endpoint_response_424 import (
    PatchServicesACMECertificateEndpointResponse424,
)
from ...models.patch_services_acme_certificate_endpoint_response_500 import (
    PatchServicesACMECertificateEndpointResponse500,
)
from ...models.patch_services_acme_certificate_endpoint_response_503 import (
    PatchServicesACMECertificateEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesACMECertificateEndpointJsonBody | PatchServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/acme/certificate",
    }

    if isinstance(body, PatchServicesACMECertificateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesACMECertificateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesACMECertificateEndpointResponse400
    | PatchServicesACMECertificateEndpointResponse401
    | PatchServicesACMECertificateEndpointResponse403
    | PatchServicesACMECertificateEndpointResponse404
    | PatchServicesACMECertificateEndpointResponse405
    | PatchServicesACMECertificateEndpointResponse406
    | PatchServicesACMECertificateEndpointResponse409
    | PatchServicesACMECertificateEndpointResponse415
    | PatchServicesACMECertificateEndpointResponse422
    | PatchServicesACMECertificateEndpointResponse424
    | PatchServicesACMECertificateEndpointResponse500
    | PatchServicesACMECertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesACMECertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesACMECertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesACMECertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesACMECertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesACMECertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesACMECertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesACMECertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesACMECertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesACMECertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesACMECertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesACMECertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesACMECertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesACMECertificateEndpointResponse400
    | PatchServicesACMECertificateEndpointResponse401
    | PatchServicesACMECertificateEndpointResponse403
    | PatchServicesACMECertificateEndpointResponse404
    | PatchServicesACMECertificateEndpointResponse405
    | PatchServicesACMECertificateEndpointResponse406
    | PatchServicesACMECertificateEndpointResponse409
    | PatchServicesACMECertificateEndpointResponse415
    | PatchServicesACMECertificateEndpointResponse422
    | PatchServicesACMECertificateEndpointResponse424
    | PatchServicesACMECertificateEndpointResponse500
    | PatchServicesACMECertificateEndpointResponse503
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
    body: PatchServicesACMECertificateEndpointJsonBody | PatchServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesACMECertificateEndpointResponse400
    | PatchServicesACMECertificateEndpointResponse401
    | PatchServicesACMECertificateEndpointResponse403
    | PatchServicesACMECertificateEndpointResponse404
    | PatchServicesACMECertificateEndpointResponse405
    | PatchServicesACMECertificateEndpointResponse406
    | PatchServicesACMECertificateEndpointResponse409
    | PatchServicesACMECertificateEndpointResponse415
    | PatchServicesACMECertificateEndpointResponse422
    | PatchServicesACMECertificateEndpointResponse424
    | PatchServicesACMECertificateEndpointResponse500
    | PatchServicesACMECertificateEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMECertificateEndpointResponse400 | PatchServicesACMECertificateEndpointResponse401 | PatchServicesACMECertificateEndpointResponse403 | PatchServicesACMECertificateEndpointResponse404 | PatchServicesACMECertificateEndpointResponse405 | PatchServicesACMECertificateEndpointResponse406 | PatchServicesACMECertificateEndpointResponse409 | PatchServicesACMECertificateEndpointResponse415 | PatchServicesACMECertificateEndpointResponse422 | PatchServicesACMECertificateEndpointResponse424 | PatchServicesACMECertificateEndpointResponse500 | PatchServicesACMECertificateEndpointResponse503]
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
    body: PatchServicesACMECertificateEndpointJsonBody | PatchServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesACMECertificateEndpointResponse400
    | PatchServicesACMECertificateEndpointResponse401
    | PatchServicesACMECertificateEndpointResponse403
    | PatchServicesACMECertificateEndpointResponse404
    | PatchServicesACMECertificateEndpointResponse405
    | PatchServicesACMECertificateEndpointResponse406
    | PatchServicesACMECertificateEndpointResponse409
    | PatchServicesACMECertificateEndpointResponse415
    | PatchServicesACMECertificateEndpointResponse422
    | PatchServicesACMECertificateEndpointResponse424
    | PatchServicesACMECertificateEndpointResponse500
    | PatchServicesACMECertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMECertificateEndpointResponse400 | PatchServicesACMECertificateEndpointResponse401 | PatchServicesACMECertificateEndpointResponse403 | PatchServicesACMECertificateEndpointResponse404 | PatchServicesACMECertificateEndpointResponse405 | PatchServicesACMECertificateEndpointResponse406 | PatchServicesACMECertificateEndpointResponse409 | PatchServicesACMECertificateEndpointResponse415 | PatchServicesACMECertificateEndpointResponse422 | PatchServicesACMECertificateEndpointResponse424 | PatchServicesACMECertificateEndpointResponse500 | PatchServicesACMECertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMECertificateEndpointJsonBody | PatchServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesACMECertificateEndpointResponse400
    | PatchServicesACMECertificateEndpointResponse401
    | PatchServicesACMECertificateEndpointResponse403
    | PatchServicesACMECertificateEndpointResponse404
    | PatchServicesACMECertificateEndpointResponse405
    | PatchServicesACMECertificateEndpointResponse406
    | PatchServicesACMECertificateEndpointResponse409
    | PatchServicesACMECertificateEndpointResponse415
    | PatchServicesACMECertificateEndpointResponse422
    | PatchServicesACMECertificateEndpointResponse424
    | PatchServicesACMECertificateEndpointResponse500
    | PatchServicesACMECertificateEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMECertificateEndpointResponse400 | PatchServicesACMECertificateEndpointResponse401 | PatchServicesACMECertificateEndpointResponse403 | PatchServicesACMECertificateEndpointResponse404 | PatchServicesACMECertificateEndpointResponse405 | PatchServicesACMECertificateEndpointResponse406 | PatchServicesACMECertificateEndpointResponse409 | PatchServicesACMECertificateEndpointResponse415 | PatchServicesACMECertificateEndpointResponse422 | PatchServicesACMECertificateEndpointResponse424 | PatchServicesACMECertificateEndpointResponse500 | PatchServicesACMECertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMECertificateEndpointJsonBody | PatchServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesACMECertificateEndpointResponse400
    | PatchServicesACMECertificateEndpointResponse401
    | PatchServicesACMECertificateEndpointResponse403
    | PatchServicesACMECertificateEndpointResponse404
    | PatchServicesACMECertificateEndpointResponse405
    | PatchServicesACMECertificateEndpointResponse406
    | PatchServicesACMECertificateEndpointResponse409
    | PatchServicesACMECertificateEndpointResponse415
    | PatchServicesACMECertificateEndpointResponse422
    | PatchServicesACMECertificateEndpointResponse424
    | PatchServicesACMECertificateEndpointResponse500
    | PatchServicesACMECertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMECertificateEndpointResponse400 | PatchServicesACMECertificateEndpointResponse401 | PatchServicesACMECertificateEndpointResponse403 | PatchServicesACMECertificateEndpointResponse404 | PatchServicesACMECertificateEndpointResponse405 | PatchServicesACMECertificateEndpointResponse406 | PatchServicesACMECertificateEndpointResponse409 | PatchServicesACMECertificateEndpointResponse415 | PatchServicesACMECertificateEndpointResponse422 | PatchServicesACMECertificateEndpointResponse424 | PatchServicesACMECertificateEndpointResponse500 | PatchServicesACMECertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
