from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_acme_certificate_endpoint_response_400 import (
    DeleteServicesACMECertificateEndpointResponse400,
)
from ...models.delete_services_acme_certificate_endpoint_response_401 import (
    DeleteServicesACMECertificateEndpointResponse401,
)
from ...models.delete_services_acme_certificate_endpoint_response_403 import (
    DeleteServicesACMECertificateEndpointResponse403,
)
from ...models.delete_services_acme_certificate_endpoint_response_404 import (
    DeleteServicesACMECertificateEndpointResponse404,
)
from ...models.delete_services_acme_certificate_endpoint_response_405 import (
    DeleteServicesACMECertificateEndpointResponse405,
)
from ...models.delete_services_acme_certificate_endpoint_response_406 import (
    DeleteServicesACMECertificateEndpointResponse406,
)
from ...models.delete_services_acme_certificate_endpoint_response_409 import (
    DeleteServicesACMECertificateEndpointResponse409,
)
from ...models.delete_services_acme_certificate_endpoint_response_415 import (
    DeleteServicesACMECertificateEndpointResponse415,
)
from ...models.delete_services_acme_certificate_endpoint_response_422 import (
    DeleteServicesACMECertificateEndpointResponse422,
)
from ...models.delete_services_acme_certificate_endpoint_response_424 import (
    DeleteServicesACMECertificateEndpointResponse424,
)
from ...models.delete_services_acme_certificate_endpoint_response_500 import (
    DeleteServicesACMECertificateEndpointResponse500,
)
from ...models.delete_services_acme_certificate_endpoint_response_503 import (
    DeleteServicesACMECertificateEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/acme/certificate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesACMECertificateEndpointResponse400
    | DeleteServicesACMECertificateEndpointResponse401
    | DeleteServicesACMECertificateEndpointResponse403
    | DeleteServicesACMECertificateEndpointResponse404
    | DeleteServicesACMECertificateEndpointResponse405
    | DeleteServicesACMECertificateEndpointResponse406
    | DeleteServicesACMECertificateEndpointResponse409
    | DeleteServicesACMECertificateEndpointResponse415
    | DeleteServicesACMECertificateEndpointResponse422
    | DeleteServicesACMECertificateEndpointResponse424
    | DeleteServicesACMECertificateEndpointResponse500
    | DeleteServicesACMECertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesACMECertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesACMECertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesACMECertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesACMECertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesACMECertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesACMECertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesACMECertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesACMECertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesACMECertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesACMECertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesACMECertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesACMECertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesACMECertificateEndpointResponse400
    | DeleteServicesACMECertificateEndpointResponse401
    | DeleteServicesACMECertificateEndpointResponse403
    | DeleteServicesACMECertificateEndpointResponse404
    | DeleteServicesACMECertificateEndpointResponse405
    | DeleteServicesACMECertificateEndpointResponse406
    | DeleteServicesACMECertificateEndpointResponse409
    | DeleteServicesACMECertificateEndpointResponse415
    | DeleteServicesACMECertificateEndpointResponse422
    | DeleteServicesACMECertificateEndpointResponse424
    | DeleteServicesACMECertificateEndpointResponse500
    | DeleteServicesACMECertificateEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteServicesACMECertificateEndpointResponse400
    | DeleteServicesACMECertificateEndpointResponse401
    | DeleteServicesACMECertificateEndpointResponse403
    | DeleteServicesACMECertificateEndpointResponse404
    | DeleteServicesACMECertificateEndpointResponse405
    | DeleteServicesACMECertificateEndpointResponse406
    | DeleteServicesACMECertificateEndpointResponse409
    | DeleteServicesACMECertificateEndpointResponse415
    | DeleteServicesACMECertificateEndpointResponse422
    | DeleteServicesACMECertificateEndpointResponse424
    | DeleteServicesACMECertificateEndpointResponse500
    | DeleteServicesACMECertificateEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMECertificateEndpointResponse400 | DeleteServicesACMECertificateEndpointResponse401 | DeleteServicesACMECertificateEndpointResponse403 | DeleteServicesACMECertificateEndpointResponse404 | DeleteServicesACMECertificateEndpointResponse405 | DeleteServicesACMECertificateEndpointResponse406 | DeleteServicesACMECertificateEndpointResponse409 | DeleteServicesACMECertificateEndpointResponse415 | DeleteServicesACMECertificateEndpointResponse422 | DeleteServicesACMECertificateEndpointResponse424 | DeleteServicesACMECertificateEndpointResponse500 | DeleteServicesACMECertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesACMECertificateEndpointResponse400
    | DeleteServicesACMECertificateEndpointResponse401
    | DeleteServicesACMECertificateEndpointResponse403
    | DeleteServicesACMECertificateEndpointResponse404
    | DeleteServicesACMECertificateEndpointResponse405
    | DeleteServicesACMECertificateEndpointResponse406
    | DeleteServicesACMECertificateEndpointResponse409
    | DeleteServicesACMECertificateEndpointResponse415
    | DeleteServicesACMECertificateEndpointResponse422
    | DeleteServicesACMECertificateEndpointResponse424
    | DeleteServicesACMECertificateEndpointResponse500
    | DeleteServicesACMECertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMECertificateEndpointResponse400 | DeleteServicesACMECertificateEndpointResponse401 | DeleteServicesACMECertificateEndpointResponse403 | DeleteServicesACMECertificateEndpointResponse404 | DeleteServicesACMECertificateEndpointResponse405 | DeleteServicesACMECertificateEndpointResponse406 | DeleteServicesACMECertificateEndpointResponse409 | DeleteServicesACMECertificateEndpointResponse415 | DeleteServicesACMECertificateEndpointResponse422 | DeleteServicesACMECertificateEndpointResponse424 | DeleteServicesACMECertificateEndpointResponse500 | DeleteServicesACMECertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteServicesACMECertificateEndpointResponse400
    | DeleteServicesACMECertificateEndpointResponse401
    | DeleteServicesACMECertificateEndpointResponse403
    | DeleteServicesACMECertificateEndpointResponse404
    | DeleteServicesACMECertificateEndpointResponse405
    | DeleteServicesACMECertificateEndpointResponse406
    | DeleteServicesACMECertificateEndpointResponse409
    | DeleteServicesACMECertificateEndpointResponse415
    | DeleteServicesACMECertificateEndpointResponse422
    | DeleteServicesACMECertificateEndpointResponse424
    | DeleteServicesACMECertificateEndpointResponse500
    | DeleteServicesACMECertificateEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMECertificateEndpointResponse400 | DeleteServicesACMECertificateEndpointResponse401 | DeleteServicesACMECertificateEndpointResponse403 | DeleteServicesACMECertificateEndpointResponse404 | DeleteServicesACMECertificateEndpointResponse405 | DeleteServicesACMECertificateEndpointResponse406 | DeleteServicesACMECertificateEndpointResponse409 | DeleteServicesACMECertificateEndpointResponse415 | DeleteServicesACMECertificateEndpointResponse422 | DeleteServicesACMECertificateEndpointResponse424 | DeleteServicesACMECertificateEndpointResponse500 | DeleteServicesACMECertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesACMECertificateEndpointResponse400
    | DeleteServicesACMECertificateEndpointResponse401
    | DeleteServicesACMECertificateEndpointResponse403
    | DeleteServicesACMECertificateEndpointResponse404
    | DeleteServicesACMECertificateEndpointResponse405
    | DeleteServicesACMECertificateEndpointResponse406
    | DeleteServicesACMECertificateEndpointResponse409
    | DeleteServicesACMECertificateEndpointResponse415
    | DeleteServicesACMECertificateEndpointResponse422
    | DeleteServicesACMECertificateEndpointResponse424
    | DeleteServicesACMECertificateEndpointResponse500
    | DeleteServicesACMECertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMECertificateEndpointResponse400 | DeleteServicesACMECertificateEndpointResponse401 | DeleteServicesACMECertificateEndpointResponse403 | DeleteServicesACMECertificateEndpointResponse404 | DeleteServicesACMECertificateEndpointResponse405 | DeleteServicesACMECertificateEndpointResponse406 | DeleteServicesACMECertificateEndpointResponse409 | DeleteServicesACMECertificateEndpointResponse415 | DeleteServicesACMECertificateEndpointResponse422 | DeleteServicesACMECertificateEndpointResponse424 | DeleteServicesACMECertificateEndpointResponse500 | DeleteServicesACMECertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
