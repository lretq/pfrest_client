from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_acme_certificate_domain_endpoint_response_400 import (
    DeleteServicesACMECertificateDomainEndpointResponse400,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_401 import (
    DeleteServicesACMECertificateDomainEndpointResponse401,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_403 import (
    DeleteServicesACMECertificateDomainEndpointResponse403,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_404 import (
    DeleteServicesACMECertificateDomainEndpointResponse404,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_405 import (
    DeleteServicesACMECertificateDomainEndpointResponse405,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_406 import (
    DeleteServicesACMECertificateDomainEndpointResponse406,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_409 import (
    DeleteServicesACMECertificateDomainEndpointResponse409,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_415 import (
    DeleteServicesACMECertificateDomainEndpointResponse415,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_422 import (
    DeleteServicesACMECertificateDomainEndpointResponse422,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_424 import (
    DeleteServicesACMECertificateDomainEndpointResponse424,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_500 import (
    DeleteServicesACMECertificateDomainEndpointResponse500,
)
from ...models.delete_services_acme_certificate_domain_endpoint_response_503 import (
    DeleteServicesACMECertificateDomainEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/acme/certificate/domain",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesACMECertificateDomainEndpointResponse400
    | DeleteServicesACMECertificateDomainEndpointResponse401
    | DeleteServicesACMECertificateDomainEndpointResponse403
    | DeleteServicesACMECertificateDomainEndpointResponse404
    | DeleteServicesACMECertificateDomainEndpointResponse405
    | DeleteServicesACMECertificateDomainEndpointResponse406
    | DeleteServicesACMECertificateDomainEndpointResponse409
    | DeleteServicesACMECertificateDomainEndpointResponse415
    | DeleteServicesACMECertificateDomainEndpointResponse422
    | DeleteServicesACMECertificateDomainEndpointResponse424
    | DeleteServicesACMECertificateDomainEndpointResponse500
    | DeleteServicesACMECertificateDomainEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesACMECertificateDomainEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesACMECertificateDomainEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesACMECertificateDomainEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesACMECertificateDomainEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesACMECertificateDomainEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesACMECertificateDomainEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesACMECertificateDomainEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesACMECertificateDomainEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesACMECertificateDomainEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesACMECertificateDomainEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesACMECertificateDomainEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesACMECertificateDomainEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesACMECertificateDomainEndpointResponse400
    | DeleteServicesACMECertificateDomainEndpointResponse401
    | DeleteServicesACMECertificateDomainEndpointResponse403
    | DeleteServicesACMECertificateDomainEndpointResponse404
    | DeleteServicesACMECertificateDomainEndpointResponse405
    | DeleteServicesACMECertificateDomainEndpointResponse406
    | DeleteServicesACMECertificateDomainEndpointResponse409
    | DeleteServicesACMECertificateDomainEndpointResponse415
    | DeleteServicesACMECertificateDomainEndpointResponse422
    | DeleteServicesACMECertificateDomainEndpointResponse424
    | DeleteServicesACMECertificateDomainEndpointResponse500
    | DeleteServicesACMECertificateDomainEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesACMECertificateDomainEndpointResponse400
    | DeleteServicesACMECertificateDomainEndpointResponse401
    | DeleteServicesACMECertificateDomainEndpointResponse403
    | DeleteServicesACMECertificateDomainEndpointResponse404
    | DeleteServicesACMECertificateDomainEndpointResponse405
    | DeleteServicesACMECertificateDomainEndpointResponse406
    | DeleteServicesACMECertificateDomainEndpointResponse409
    | DeleteServicesACMECertificateDomainEndpointResponse415
    | DeleteServicesACMECertificateDomainEndpointResponse422
    | DeleteServicesACMECertificateDomainEndpointResponse424
    | DeleteServicesACMECertificateDomainEndpointResponse500
    | DeleteServicesACMECertificateDomainEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMECertificateDomainEndpointResponse400 | DeleteServicesACMECertificateDomainEndpointResponse401 | DeleteServicesACMECertificateDomainEndpointResponse403 | DeleteServicesACMECertificateDomainEndpointResponse404 | DeleteServicesACMECertificateDomainEndpointResponse405 | DeleteServicesACMECertificateDomainEndpointResponse406 | DeleteServicesACMECertificateDomainEndpointResponse409 | DeleteServicesACMECertificateDomainEndpointResponse415 | DeleteServicesACMECertificateDomainEndpointResponse422 | DeleteServicesACMECertificateDomainEndpointResponse424 | DeleteServicesACMECertificateDomainEndpointResponse500 | DeleteServicesACMECertificateDomainEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesACMECertificateDomainEndpointResponse400
    | DeleteServicesACMECertificateDomainEndpointResponse401
    | DeleteServicesACMECertificateDomainEndpointResponse403
    | DeleteServicesACMECertificateDomainEndpointResponse404
    | DeleteServicesACMECertificateDomainEndpointResponse405
    | DeleteServicesACMECertificateDomainEndpointResponse406
    | DeleteServicesACMECertificateDomainEndpointResponse409
    | DeleteServicesACMECertificateDomainEndpointResponse415
    | DeleteServicesACMECertificateDomainEndpointResponse422
    | DeleteServicesACMECertificateDomainEndpointResponse424
    | DeleteServicesACMECertificateDomainEndpointResponse500
    | DeleteServicesACMECertificateDomainEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMECertificateDomainEndpointResponse400 | DeleteServicesACMECertificateDomainEndpointResponse401 | DeleteServicesACMECertificateDomainEndpointResponse403 | DeleteServicesACMECertificateDomainEndpointResponse404 | DeleteServicesACMECertificateDomainEndpointResponse405 | DeleteServicesACMECertificateDomainEndpointResponse406 | DeleteServicesACMECertificateDomainEndpointResponse409 | DeleteServicesACMECertificateDomainEndpointResponse415 | DeleteServicesACMECertificateDomainEndpointResponse422 | DeleteServicesACMECertificateDomainEndpointResponse424 | DeleteServicesACMECertificateDomainEndpointResponse500 | DeleteServicesACMECertificateDomainEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesACMECertificateDomainEndpointResponse400
    | DeleteServicesACMECertificateDomainEndpointResponse401
    | DeleteServicesACMECertificateDomainEndpointResponse403
    | DeleteServicesACMECertificateDomainEndpointResponse404
    | DeleteServicesACMECertificateDomainEndpointResponse405
    | DeleteServicesACMECertificateDomainEndpointResponse406
    | DeleteServicesACMECertificateDomainEndpointResponse409
    | DeleteServicesACMECertificateDomainEndpointResponse415
    | DeleteServicesACMECertificateDomainEndpointResponse422
    | DeleteServicesACMECertificateDomainEndpointResponse424
    | DeleteServicesACMECertificateDomainEndpointResponse500
    | DeleteServicesACMECertificateDomainEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMECertificateDomainEndpointResponse400 | DeleteServicesACMECertificateDomainEndpointResponse401 | DeleteServicesACMECertificateDomainEndpointResponse403 | DeleteServicesACMECertificateDomainEndpointResponse404 | DeleteServicesACMECertificateDomainEndpointResponse405 | DeleteServicesACMECertificateDomainEndpointResponse406 | DeleteServicesACMECertificateDomainEndpointResponse409 | DeleteServicesACMECertificateDomainEndpointResponse415 | DeleteServicesACMECertificateDomainEndpointResponse422 | DeleteServicesACMECertificateDomainEndpointResponse424 | DeleteServicesACMECertificateDomainEndpointResponse500 | DeleteServicesACMECertificateDomainEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesACMECertificateDomainEndpointResponse400
    | DeleteServicesACMECertificateDomainEndpointResponse401
    | DeleteServicesACMECertificateDomainEndpointResponse403
    | DeleteServicesACMECertificateDomainEndpointResponse404
    | DeleteServicesACMECertificateDomainEndpointResponse405
    | DeleteServicesACMECertificateDomainEndpointResponse406
    | DeleteServicesACMECertificateDomainEndpointResponse409
    | DeleteServicesACMECertificateDomainEndpointResponse415
    | DeleteServicesACMECertificateDomainEndpointResponse422
    | DeleteServicesACMECertificateDomainEndpointResponse424
    | DeleteServicesACMECertificateDomainEndpointResponse500
    | DeleteServicesACMECertificateDomainEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMECertificateDomainEndpointResponse400 | DeleteServicesACMECertificateDomainEndpointResponse401 | DeleteServicesACMECertificateDomainEndpointResponse403 | DeleteServicesACMECertificateDomainEndpointResponse404 | DeleteServicesACMECertificateDomainEndpointResponse405 | DeleteServicesACMECertificateDomainEndpointResponse406 | DeleteServicesACMECertificateDomainEndpointResponse409 | DeleteServicesACMECertificateDomainEndpointResponse415 | DeleteServicesACMECertificateDomainEndpointResponse422 | DeleteServicesACMECertificateDomainEndpointResponse424 | DeleteServicesACMECertificateDomainEndpointResponse500 | DeleteServicesACMECertificateDomainEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
