from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_acme_certificate_action_endpoint_data_body import (
    PatchServicesACMECertificateActionEndpointDataBody,
)
from ...models.patch_services_acme_certificate_action_endpoint_json_body import (
    PatchServicesACMECertificateActionEndpointJsonBody,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_400 import (
    PatchServicesACMECertificateActionEndpointResponse400,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_401 import (
    PatchServicesACMECertificateActionEndpointResponse401,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_403 import (
    PatchServicesACMECertificateActionEndpointResponse403,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_404 import (
    PatchServicesACMECertificateActionEndpointResponse404,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_405 import (
    PatchServicesACMECertificateActionEndpointResponse405,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_406 import (
    PatchServicesACMECertificateActionEndpointResponse406,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_409 import (
    PatchServicesACMECertificateActionEndpointResponse409,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_415 import (
    PatchServicesACMECertificateActionEndpointResponse415,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_422 import (
    PatchServicesACMECertificateActionEndpointResponse422,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_424 import (
    PatchServicesACMECertificateActionEndpointResponse424,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_500 import (
    PatchServicesACMECertificateActionEndpointResponse500,
)
from ...models.patch_services_acme_certificate_action_endpoint_response_503 import (
    PatchServicesACMECertificateActionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesACMECertificateActionEndpointJsonBody
    | PatchServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/acme/certificate/action",
    }

    if isinstance(body, PatchServicesACMECertificateActionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesACMECertificateActionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesACMECertificateActionEndpointResponse400
    | PatchServicesACMECertificateActionEndpointResponse401
    | PatchServicesACMECertificateActionEndpointResponse403
    | PatchServicesACMECertificateActionEndpointResponse404
    | PatchServicesACMECertificateActionEndpointResponse405
    | PatchServicesACMECertificateActionEndpointResponse406
    | PatchServicesACMECertificateActionEndpointResponse409
    | PatchServicesACMECertificateActionEndpointResponse415
    | PatchServicesACMECertificateActionEndpointResponse422
    | PatchServicesACMECertificateActionEndpointResponse424
    | PatchServicesACMECertificateActionEndpointResponse500
    | PatchServicesACMECertificateActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesACMECertificateActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesACMECertificateActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesACMECertificateActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesACMECertificateActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesACMECertificateActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesACMECertificateActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesACMECertificateActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesACMECertificateActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesACMECertificateActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesACMECertificateActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesACMECertificateActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesACMECertificateActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesACMECertificateActionEndpointResponse400
    | PatchServicesACMECertificateActionEndpointResponse401
    | PatchServicesACMECertificateActionEndpointResponse403
    | PatchServicesACMECertificateActionEndpointResponse404
    | PatchServicesACMECertificateActionEndpointResponse405
    | PatchServicesACMECertificateActionEndpointResponse406
    | PatchServicesACMECertificateActionEndpointResponse409
    | PatchServicesACMECertificateActionEndpointResponse415
    | PatchServicesACMECertificateActionEndpointResponse422
    | PatchServicesACMECertificateActionEndpointResponse424
    | PatchServicesACMECertificateActionEndpointResponse500
    | PatchServicesACMECertificateActionEndpointResponse503
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
    body: PatchServicesACMECertificateActionEndpointJsonBody
    | PatchServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesACMECertificateActionEndpointResponse400
    | PatchServicesACMECertificateActionEndpointResponse401
    | PatchServicesACMECertificateActionEndpointResponse403
    | PatchServicesACMECertificateActionEndpointResponse404
    | PatchServicesACMECertificateActionEndpointResponse405
    | PatchServicesACMECertificateActionEndpointResponse406
    | PatchServicesACMECertificateActionEndpointResponse409
    | PatchServicesACMECertificateActionEndpointResponse415
    | PatchServicesACMECertificateActionEndpointResponse422
    | PatchServicesACMECertificateActionEndpointResponse424
    | PatchServicesACMECertificateActionEndpointResponse500
    | PatchServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMECertificateActionEndpointResponse400 | PatchServicesACMECertificateActionEndpointResponse401 | PatchServicesACMECertificateActionEndpointResponse403 | PatchServicesACMECertificateActionEndpointResponse404 | PatchServicesACMECertificateActionEndpointResponse405 | PatchServicesACMECertificateActionEndpointResponse406 | PatchServicesACMECertificateActionEndpointResponse409 | PatchServicesACMECertificateActionEndpointResponse415 | PatchServicesACMECertificateActionEndpointResponse422 | PatchServicesACMECertificateActionEndpointResponse424 | PatchServicesACMECertificateActionEndpointResponse500 | PatchServicesACMECertificateActionEndpointResponse503]
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
    body: PatchServicesACMECertificateActionEndpointJsonBody
    | PatchServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesACMECertificateActionEndpointResponse400
    | PatchServicesACMECertificateActionEndpointResponse401
    | PatchServicesACMECertificateActionEndpointResponse403
    | PatchServicesACMECertificateActionEndpointResponse404
    | PatchServicesACMECertificateActionEndpointResponse405
    | PatchServicesACMECertificateActionEndpointResponse406
    | PatchServicesACMECertificateActionEndpointResponse409
    | PatchServicesACMECertificateActionEndpointResponse415
    | PatchServicesACMECertificateActionEndpointResponse422
    | PatchServicesACMECertificateActionEndpointResponse424
    | PatchServicesACMECertificateActionEndpointResponse500
    | PatchServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMECertificateActionEndpointResponse400 | PatchServicesACMECertificateActionEndpointResponse401 | PatchServicesACMECertificateActionEndpointResponse403 | PatchServicesACMECertificateActionEndpointResponse404 | PatchServicesACMECertificateActionEndpointResponse405 | PatchServicesACMECertificateActionEndpointResponse406 | PatchServicesACMECertificateActionEndpointResponse409 | PatchServicesACMECertificateActionEndpointResponse415 | PatchServicesACMECertificateActionEndpointResponse422 | PatchServicesACMECertificateActionEndpointResponse424 | PatchServicesACMECertificateActionEndpointResponse500 | PatchServicesACMECertificateActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMECertificateActionEndpointJsonBody
    | PatchServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesACMECertificateActionEndpointResponse400
    | PatchServicesACMECertificateActionEndpointResponse401
    | PatchServicesACMECertificateActionEndpointResponse403
    | PatchServicesACMECertificateActionEndpointResponse404
    | PatchServicesACMECertificateActionEndpointResponse405
    | PatchServicesACMECertificateActionEndpointResponse406
    | PatchServicesACMECertificateActionEndpointResponse409
    | PatchServicesACMECertificateActionEndpointResponse415
    | PatchServicesACMECertificateActionEndpointResponse422
    | PatchServicesACMECertificateActionEndpointResponse424
    | PatchServicesACMECertificateActionEndpointResponse500
    | PatchServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMECertificateActionEndpointResponse400 | PatchServicesACMECertificateActionEndpointResponse401 | PatchServicesACMECertificateActionEndpointResponse403 | PatchServicesACMECertificateActionEndpointResponse404 | PatchServicesACMECertificateActionEndpointResponse405 | PatchServicesACMECertificateActionEndpointResponse406 | PatchServicesACMECertificateActionEndpointResponse409 | PatchServicesACMECertificateActionEndpointResponse415 | PatchServicesACMECertificateActionEndpointResponse422 | PatchServicesACMECertificateActionEndpointResponse424 | PatchServicesACMECertificateActionEndpointResponse500 | PatchServicesACMECertificateActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMECertificateActionEndpointJsonBody
    | PatchServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesACMECertificateActionEndpointResponse400
    | PatchServicesACMECertificateActionEndpointResponse401
    | PatchServicesACMECertificateActionEndpointResponse403
    | PatchServicesACMECertificateActionEndpointResponse404
    | PatchServicesACMECertificateActionEndpointResponse405
    | PatchServicesACMECertificateActionEndpointResponse406
    | PatchServicesACMECertificateActionEndpointResponse409
    | PatchServicesACMECertificateActionEndpointResponse415
    | PatchServicesACMECertificateActionEndpointResponse422
    | PatchServicesACMECertificateActionEndpointResponse424
    | PatchServicesACMECertificateActionEndpointResponse500
    | PatchServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-patch ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PatchServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMECertificateActionEndpointResponse400 | PatchServicesACMECertificateActionEndpointResponse401 | PatchServicesACMECertificateActionEndpointResponse403 | PatchServicesACMECertificateActionEndpointResponse404 | PatchServicesACMECertificateActionEndpointResponse405 | PatchServicesACMECertificateActionEndpointResponse406 | PatchServicesACMECertificateActionEndpointResponse409 | PatchServicesACMECertificateActionEndpointResponse415 | PatchServicesACMECertificateActionEndpointResponse422 | PatchServicesACMECertificateActionEndpointResponse424 | PatchServicesACMECertificateActionEndpointResponse500 | PatchServicesACMECertificateActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
