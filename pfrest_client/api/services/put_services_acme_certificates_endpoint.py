from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_acme_certificates_endpoint_data_body_item import (
    PutServicesACMECertificatesEndpointDataBodyItem,
)
from ...models.put_services_acme_certificates_endpoint_json_body_item import (
    PutServicesACMECertificatesEndpointJsonBodyItem,
)
from ...models.put_services_acme_certificates_endpoint_response_400 import (
    PutServicesACMECertificatesEndpointResponse400,
)
from ...models.put_services_acme_certificates_endpoint_response_401 import (
    PutServicesACMECertificatesEndpointResponse401,
)
from ...models.put_services_acme_certificates_endpoint_response_403 import (
    PutServicesACMECertificatesEndpointResponse403,
)
from ...models.put_services_acme_certificates_endpoint_response_404 import (
    PutServicesACMECertificatesEndpointResponse404,
)
from ...models.put_services_acme_certificates_endpoint_response_405 import (
    PutServicesACMECertificatesEndpointResponse405,
)
from ...models.put_services_acme_certificates_endpoint_response_406 import (
    PutServicesACMECertificatesEndpointResponse406,
)
from ...models.put_services_acme_certificates_endpoint_response_409 import (
    PutServicesACMECertificatesEndpointResponse409,
)
from ...models.put_services_acme_certificates_endpoint_response_415 import (
    PutServicesACMECertificatesEndpointResponse415,
)
from ...models.put_services_acme_certificates_endpoint_response_422 import (
    PutServicesACMECertificatesEndpointResponse422,
)
from ...models.put_services_acme_certificates_endpoint_response_424 import (
    PutServicesACMECertificatesEndpointResponse424,
)
from ...models.put_services_acme_certificates_endpoint_response_500 import (
    PutServicesACMECertificatesEndpointResponse500,
)
from ...models.put_services_acme_certificates_endpoint_response_503 import (
    PutServicesACMECertificatesEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesACMECertificatesEndpointJsonBodyItem]
    | list[PutServicesACMECertificatesEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/acme/certificates",
    }

    if isinstance(body, list[PutServicesACMECertificatesEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesACMECertificatesEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesACMECertificatesEndpointResponse400
    | PutServicesACMECertificatesEndpointResponse401
    | PutServicesACMECertificatesEndpointResponse403
    | PutServicesACMECertificatesEndpointResponse404
    | PutServicesACMECertificatesEndpointResponse405
    | PutServicesACMECertificatesEndpointResponse406
    | PutServicesACMECertificatesEndpointResponse409
    | PutServicesACMECertificatesEndpointResponse415
    | PutServicesACMECertificatesEndpointResponse422
    | PutServicesACMECertificatesEndpointResponse424
    | PutServicesACMECertificatesEndpointResponse500
    | PutServicesACMECertificatesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesACMECertificatesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesACMECertificatesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesACMECertificatesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesACMECertificatesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesACMECertificatesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesACMECertificatesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesACMECertificatesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesACMECertificatesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesACMECertificatesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesACMECertificatesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesACMECertificatesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesACMECertificatesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesACMECertificatesEndpointResponse400
    | PutServicesACMECertificatesEndpointResponse401
    | PutServicesACMECertificatesEndpointResponse403
    | PutServicesACMECertificatesEndpointResponse404
    | PutServicesACMECertificatesEndpointResponse405
    | PutServicesACMECertificatesEndpointResponse406
    | PutServicesACMECertificatesEndpointResponse409
    | PutServicesACMECertificatesEndpointResponse415
    | PutServicesACMECertificatesEndpointResponse422
    | PutServicesACMECertificatesEndpointResponse424
    | PutServicesACMECertificatesEndpointResponse500
    | PutServicesACMECertificatesEndpointResponse503
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
    body: list[PutServicesACMECertificatesEndpointJsonBodyItem]
    | list[PutServicesACMECertificatesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesACMECertificatesEndpointResponse400
    | PutServicesACMECertificatesEndpointResponse401
    | PutServicesACMECertificatesEndpointResponse403
    | PutServicesACMECertificatesEndpointResponse404
    | PutServicesACMECertificatesEndpointResponse405
    | PutServicesACMECertificatesEndpointResponse406
    | PutServicesACMECertificatesEndpointResponse409
    | PutServicesACMECertificatesEndpointResponse415
    | PutServicesACMECertificatesEndpointResponse422
    | PutServicesACMECertificatesEndpointResponse424
    | PutServicesACMECertificatesEndpointResponse500
    | PutServicesACMECertificatesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing ACME Certificates.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificates-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMECertificatesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMECertificatesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesACMECertificatesEndpointResponse400 | PutServicesACMECertificatesEndpointResponse401 | PutServicesACMECertificatesEndpointResponse403 | PutServicesACMECertificatesEndpointResponse404 | PutServicesACMECertificatesEndpointResponse405 | PutServicesACMECertificatesEndpointResponse406 | PutServicesACMECertificatesEndpointResponse409 | PutServicesACMECertificatesEndpointResponse415 | PutServicesACMECertificatesEndpointResponse422 | PutServicesACMECertificatesEndpointResponse424 | PutServicesACMECertificatesEndpointResponse500 | PutServicesACMECertificatesEndpointResponse503]
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
    body: list[PutServicesACMECertificatesEndpointJsonBodyItem]
    | list[PutServicesACMECertificatesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesACMECertificatesEndpointResponse400
    | PutServicesACMECertificatesEndpointResponse401
    | PutServicesACMECertificatesEndpointResponse403
    | PutServicesACMECertificatesEndpointResponse404
    | PutServicesACMECertificatesEndpointResponse405
    | PutServicesACMECertificatesEndpointResponse406
    | PutServicesACMECertificatesEndpointResponse409
    | PutServicesACMECertificatesEndpointResponse415
    | PutServicesACMECertificatesEndpointResponse422
    | PutServicesACMECertificatesEndpointResponse424
    | PutServicesACMECertificatesEndpointResponse500
    | PutServicesACMECertificatesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing ACME Certificates.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificates-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMECertificatesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMECertificatesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesACMECertificatesEndpointResponse400 | PutServicesACMECertificatesEndpointResponse401 | PutServicesACMECertificatesEndpointResponse403 | PutServicesACMECertificatesEndpointResponse404 | PutServicesACMECertificatesEndpointResponse405 | PutServicesACMECertificatesEndpointResponse406 | PutServicesACMECertificatesEndpointResponse409 | PutServicesACMECertificatesEndpointResponse415 | PutServicesACMECertificatesEndpointResponse422 | PutServicesACMECertificatesEndpointResponse424 | PutServicesACMECertificatesEndpointResponse500 | PutServicesACMECertificatesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesACMECertificatesEndpointJsonBodyItem]
    | list[PutServicesACMECertificatesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesACMECertificatesEndpointResponse400
    | PutServicesACMECertificatesEndpointResponse401
    | PutServicesACMECertificatesEndpointResponse403
    | PutServicesACMECertificatesEndpointResponse404
    | PutServicesACMECertificatesEndpointResponse405
    | PutServicesACMECertificatesEndpointResponse406
    | PutServicesACMECertificatesEndpointResponse409
    | PutServicesACMECertificatesEndpointResponse415
    | PutServicesACMECertificatesEndpointResponse422
    | PutServicesACMECertificatesEndpointResponse424
    | PutServicesACMECertificatesEndpointResponse500
    | PutServicesACMECertificatesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing ACME Certificates.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificates-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMECertificatesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMECertificatesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesACMECertificatesEndpointResponse400 | PutServicesACMECertificatesEndpointResponse401 | PutServicesACMECertificatesEndpointResponse403 | PutServicesACMECertificatesEndpointResponse404 | PutServicesACMECertificatesEndpointResponse405 | PutServicesACMECertificatesEndpointResponse406 | PutServicesACMECertificatesEndpointResponse409 | PutServicesACMECertificatesEndpointResponse415 | PutServicesACMECertificatesEndpointResponse422 | PutServicesACMECertificatesEndpointResponse424 | PutServicesACMECertificatesEndpointResponse500 | PutServicesACMECertificatesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesACMECertificatesEndpointJsonBodyItem]
    | list[PutServicesACMECertificatesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesACMECertificatesEndpointResponse400
    | PutServicesACMECertificatesEndpointResponse401
    | PutServicesACMECertificatesEndpointResponse403
    | PutServicesACMECertificatesEndpointResponse404
    | PutServicesACMECertificatesEndpointResponse405
    | PutServicesACMECertificatesEndpointResponse406
    | PutServicesACMECertificatesEndpointResponse409
    | PutServicesACMECertificatesEndpointResponse415
    | PutServicesACMECertificatesEndpointResponse422
    | PutServicesACMECertificatesEndpointResponse424
    | PutServicesACMECertificatesEndpointResponse500
    | PutServicesACMECertificatesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing ACME Certificates.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificates-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMECertificatesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMECertificatesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesACMECertificatesEndpointResponse400 | PutServicesACMECertificatesEndpointResponse401 | PutServicesACMECertificatesEndpointResponse403 | PutServicesACMECertificatesEndpointResponse404 | PutServicesACMECertificatesEndpointResponse405 | PutServicesACMECertificatesEndpointResponse406 | PutServicesACMECertificatesEndpointResponse409 | PutServicesACMECertificatesEndpointResponse415 | PutServicesACMECertificatesEndpointResponse422 | PutServicesACMECertificatesEndpointResponse424 | PutServicesACMECertificatesEndpointResponse500 | PutServicesACMECertificatesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
