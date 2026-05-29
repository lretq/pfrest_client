from http import HTTPStatus
from io import BytesIO
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_pkcs12_export_endpoint_data_body import (
    PostSystemCertificatePKCS12ExportEndpointDataBody,
)
from ...models.post_system_certificate_pkcs12_export_endpoint_json_body import (
    PostSystemCertificatePKCS12ExportEndpointJsonBody,
)
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificatePKCS12ExportEndpointJsonBody
    | PostSystemCertificatePKCS12ExportEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate/pkcs12/export",
    }

    if isinstance(body, PostSystemCertificatePKCS12ExportEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificatePKCS12ExportEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 400:
        response_400 = File(payload=BytesIO(response.content))

        return response_400

    if response.status_code == 401:
        response_401 = File(payload=BytesIO(response.content))

        return response_401

    if response.status_code == 403:
        response_403 = File(payload=BytesIO(response.content))

        return response_403

    if response.status_code == 404:
        response_404 = File(payload=BytesIO(response.content))

        return response_404

    if response.status_code == 405:
        response_405 = File(payload=BytesIO(response.content))

        return response_405

    if response.status_code == 406:
        response_406 = File(payload=BytesIO(response.content))

        return response_406

    if response.status_code == 409:
        response_409 = File(payload=BytesIO(response.content))

        return response_409

    if response.status_code == 415:
        response_415 = File(payload=BytesIO(response.content))

        return response_415

    if response.status_code == 422:
        response_422 = File(payload=BytesIO(response.content))

        return response_422

    if response.status_code == 424:
        response_424 = File(payload=BytesIO(response.content))

        return response_424

    if response.status_code == 500:
        response_500 = File(payload=BytesIO(response.content))

        return response_500

    if response.status_code == 503:
        response_503 = File(payload=BytesIO(response.content))

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificatePKCS12ExportEndpointJsonBody
    | PostSystemCertificatePKCS12ExportEndpointDataBody
    | Unset = UNSET,
) -> Response[File]:
    """<h3>Description:</h3>Exports an existing certificate as a PKCS#12 archive. Please note this endpoint
    will return the PKCS#12 archive as a binary download.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificatePKCS12Export<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-pkcs12-export-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificatePKCS12ExportEndpointJsonBody | Unset):
        body (PostSystemCertificatePKCS12ExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
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
    body: PostSystemCertificatePKCS12ExportEndpointJsonBody
    | PostSystemCertificatePKCS12ExportEndpointDataBody
    | Unset = UNSET,
) -> File | None:
    """<h3>Description:</h3>Exports an existing certificate as a PKCS#12 archive. Please note this endpoint
    will return the PKCS#12 archive as a binary download.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificatePKCS12Export<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-pkcs12-export-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificatePKCS12ExportEndpointJsonBody | Unset):
        body (PostSystemCertificatePKCS12ExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificatePKCS12ExportEndpointJsonBody
    | PostSystemCertificatePKCS12ExportEndpointDataBody
    | Unset = UNSET,
) -> Response[File]:
    """<h3>Description:</h3>Exports an existing certificate as a PKCS#12 archive. Please note this endpoint
    will return the PKCS#12 archive as a binary download.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificatePKCS12Export<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-pkcs12-export-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificatePKCS12ExportEndpointJsonBody | Unset):
        body (PostSystemCertificatePKCS12ExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificatePKCS12ExportEndpointJsonBody
    | PostSystemCertificatePKCS12ExportEndpointDataBody
    | Unset = UNSET,
) -> File | None:
    """<h3>Description:</h3>Exports an existing certificate as a PKCS#12 archive. Please note this endpoint
    will return the PKCS#12 archive as a binary download.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificatePKCS12Export<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-pkcs12-export-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificatePKCS12ExportEndpointJsonBody | Unset):
        body (PostSystemCertificatePKCS12ExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
