from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_acme_certificate_domain_endpoint_data_body import (
    PatchServicesACMECertificateDomainEndpointDataBody,
)
from ...models.patch_services_acme_certificate_domain_endpoint_json_body import (
    PatchServicesACMECertificateDomainEndpointJsonBody,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_400 import (
    PatchServicesACMECertificateDomainEndpointResponse400,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_401 import (
    PatchServicesACMECertificateDomainEndpointResponse401,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_403 import (
    PatchServicesACMECertificateDomainEndpointResponse403,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_404 import (
    PatchServicesACMECertificateDomainEndpointResponse404,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_405 import (
    PatchServicesACMECertificateDomainEndpointResponse405,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_406 import (
    PatchServicesACMECertificateDomainEndpointResponse406,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_409 import (
    PatchServicesACMECertificateDomainEndpointResponse409,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_415 import (
    PatchServicesACMECertificateDomainEndpointResponse415,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_422 import (
    PatchServicesACMECertificateDomainEndpointResponse422,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_424 import (
    PatchServicesACMECertificateDomainEndpointResponse424,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_500 import (
    PatchServicesACMECertificateDomainEndpointResponse500,
)
from ...models.patch_services_acme_certificate_domain_endpoint_response_503 import (
    PatchServicesACMECertificateDomainEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesACMECertificateDomainEndpointJsonBody
    | PatchServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/acme/certificate/domain",
    }

    if isinstance(body, PatchServicesACMECertificateDomainEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesACMECertificateDomainEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesACMECertificateDomainEndpointResponse400
    | PatchServicesACMECertificateDomainEndpointResponse401
    | PatchServicesACMECertificateDomainEndpointResponse403
    | PatchServicesACMECertificateDomainEndpointResponse404
    | PatchServicesACMECertificateDomainEndpointResponse405
    | PatchServicesACMECertificateDomainEndpointResponse406
    | PatchServicesACMECertificateDomainEndpointResponse409
    | PatchServicesACMECertificateDomainEndpointResponse415
    | PatchServicesACMECertificateDomainEndpointResponse422
    | PatchServicesACMECertificateDomainEndpointResponse424
    | PatchServicesACMECertificateDomainEndpointResponse500
    | PatchServicesACMECertificateDomainEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesACMECertificateDomainEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesACMECertificateDomainEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesACMECertificateDomainEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesACMECertificateDomainEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesACMECertificateDomainEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesACMECertificateDomainEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesACMECertificateDomainEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesACMECertificateDomainEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesACMECertificateDomainEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesACMECertificateDomainEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesACMECertificateDomainEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesACMECertificateDomainEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesACMECertificateDomainEndpointResponse400
    | PatchServicesACMECertificateDomainEndpointResponse401
    | PatchServicesACMECertificateDomainEndpointResponse403
    | PatchServicesACMECertificateDomainEndpointResponse404
    | PatchServicesACMECertificateDomainEndpointResponse405
    | PatchServicesACMECertificateDomainEndpointResponse406
    | PatchServicesACMECertificateDomainEndpointResponse409
    | PatchServicesACMECertificateDomainEndpointResponse415
    | PatchServicesACMECertificateDomainEndpointResponse422
    | PatchServicesACMECertificateDomainEndpointResponse424
    | PatchServicesACMECertificateDomainEndpointResponse500
    | PatchServicesACMECertificateDomainEndpointResponse503
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
    body: PatchServicesACMECertificateDomainEndpointJsonBody
    | PatchServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesACMECertificateDomainEndpointResponse400
    | PatchServicesACMECertificateDomainEndpointResponse401
    | PatchServicesACMECertificateDomainEndpointResponse403
    | PatchServicesACMECertificateDomainEndpointResponse404
    | PatchServicesACMECertificateDomainEndpointResponse405
    | PatchServicesACMECertificateDomainEndpointResponse406
    | PatchServicesACMECertificateDomainEndpointResponse409
    | PatchServicesACMECertificateDomainEndpointResponse415
    | PatchServicesACMECertificateDomainEndpointResponse422
    | PatchServicesACMECertificateDomainEndpointResponse424
    | PatchServicesACMECertificateDomainEndpointResponse500
    | PatchServicesACMECertificateDomainEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMECertificateDomainEndpointResponse400 | PatchServicesACMECertificateDomainEndpointResponse401 | PatchServicesACMECertificateDomainEndpointResponse403 | PatchServicesACMECertificateDomainEndpointResponse404 | PatchServicesACMECertificateDomainEndpointResponse405 | PatchServicesACMECertificateDomainEndpointResponse406 | PatchServicesACMECertificateDomainEndpointResponse409 | PatchServicesACMECertificateDomainEndpointResponse415 | PatchServicesACMECertificateDomainEndpointResponse422 | PatchServicesACMECertificateDomainEndpointResponse424 | PatchServicesACMECertificateDomainEndpointResponse500 | PatchServicesACMECertificateDomainEndpointResponse503]
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
    body: PatchServicesACMECertificateDomainEndpointJsonBody
    | PatchServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesACMECertificateDomainEndpointResponse400
    | PatchServicesACMECertificateDomainEndpointResponse401
    | PatchServicesACMECertificateDomainEndpointResponse403
    | PatchServicesACMECertificateDomainEndpointResponse404
    | PatchServicesACMECertificateDomainEndpointResponse405
    | PatchServicesACMECertificateDomainEndpointResponse406
    | PatchServicesACMECertificateDomainEndpointResponse409
    | PatchServicesACMECertificateDomainEndpointResponse415
    | PatchServicesACMECertificateDomainEndpointResponse422
    | PatchServicesACMECertificateDomainEndpointResponse424
    | PatchServicesACMECertificateDomainEndpointResponse500
    | PatchServicesACMECertificateDomainEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMECertificateDomainEndpointResponse400 | PatchServicesACMECertificateDomainEndpointResponse401 | PatchServicesACMECertificateDomainEndpointResponse403 | PatchServicesACMECertificateDomainEndpointResponse404 | PatchServicesACMECertificateDomainEndpointResponse405 | PatchServicesACMECertificateDomainEndpointResponse406 | PatchServicesACMECertificateDomainEndpointResponse409 | PatchServicesACMECertificateDomainEndpointResponse415 | PatchServicesACMECertificateDomainEndpointResponse422 | PatchServicesACMECertificateDomainEndpointResponse424 | PatchServicesACMECertificateDomainEndpointResponse500 | PatchServicesACMECertificateDomainEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMECertificateDomainEndpointJsonBody
    | PatchServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesACMECertificateDomainEndpointResponse400
    | PatchServicesACMECertificateDomainEndpointResponse401
    | PatchServicesACMECertificateDomainEndpointResponse403
    | PatchServicesACMECertificateDomainEndpointResponse404
    | PatchServicesACMECertificateDomainEndpointResponse405
    | PatchServicesACMECertificateDomainEndpointResponse406
    | PatchServicesACMECertificateDomainEndpointResponse409
    | PatchServicesACMECertificateDomainEndpointResponse415
    | PatchServicesACMECertificateDomainEndpointResponse422
    | PatchServicesACMECertificateDomainEndpointResponse424
    | PatchServicesACMECertificateDomainEndpointResponse500
    | PatchServicesACMECertificateDomainEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMECertificateDomainEndpointResponse400 | PatchServicesACMECertificateDomainEndpointResponse401 | PatchServicesACMECertificateDomainEndpointResponse403 | PatchServicesACMECertificateDomainEndpointResponse404 | PatchServicesACMECertificateDomainEndpointResponse405 | PatchServicesACMECertificateDomainEndpointResponse406 | PatchServicesACMECertificateDomainEndpointResponse409 | PatchServicesACMECertificateDomainEndpointResponse415 | PatchServicesACMECertificateDomainEndpointResponse422 | PatchServicesACMECertificateDomainEndpointResponse424 | PatchServicesACMECertificateDomainEndpointResponse500 | PatchServicesACMECertificateDomainEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMECertificateDomainEndpointJsonBody
    | PatchServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesACMECertificateDomainEndpointResponse400
    | PatchServicesACMECertificateDomainEndpointResponse401
    | PatchServicesACMECertificateDomainEndpointResponse403
    | PatchServicesACMECertificateDomainEndpointResponse404
    | PatchServicesACMECertificateDomainEndpointResponse405
    | PatchServicesACMECertificateDomainEndpointResponse406
    | PatchServicesACMECertificateDomainEndpointResponse409
    | PatchServicesACMECertificateDomainEndpointResponse415
    | PatchServicesACMECertificateDomainEndpointResponse422
    | PatchServicesACMECertificateDomainEndpointResponse424
    | PatchServicesACMECertificateDomainEndpointResponse500
    | PatchServicesACMECertificateDomainEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMECertificateDomainEndpointResponse400 | PatchServicesACMECertificateDomainEndpointResponse401 | PatchServicesACMECertificateDomainEndpointResponse403 | PatchServicesACMECertificateDomainEndpointResponse404 | PatchServicesACMECertificateDomainEndpointResponse405 | PatchServicesACMECertificateDomainEndpointResponse406 | PatchServicesACMECertificateDomainEndpointResponse409 | PatchServicesACMECertificateDomainEndpointResponse415 | PatchServicesACMECertificateDomainEndpointResponse422 | PatchServicesACMECertificateDomainEndpointResponse424 | PatchServicesACMECertificateDomainEndpointResponse500 | PatchServicesACMECertificateDomainEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
