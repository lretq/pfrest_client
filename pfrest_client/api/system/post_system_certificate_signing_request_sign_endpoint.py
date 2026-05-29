from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_signing_request_sign_endpoint_data_body import (
    PostSystemCertificateSigningRequestSignEndpointDataBody,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_json_body import (
    PostSystemCertificateSigningRequestSignEndpointJsonBody,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_400 import (
    PostSystemCertificateSigningRequestSignEndpointResponse400,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_401 import (
    PostSystemCertificateSigningRequestSignEndpointResponse401,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_403 import (
    PostSystemCertificateSigningRequestSignEndpointResponse403,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_404 import (
    PostSystemCertificateSigningRequestSignEndpointResponse404,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_405 import (
    PostSystemCertificateSigningRequestSignEndpointResponse405,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_406 import (
    PostSystemCertificateSigningRequestSignEndpointResponse406,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_409 import (
    PostSystemCertificateSigningRequestSignEndpointResponse409,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_415 import (
    PostSystemCertificateSigningRequestSignEndpointResponse415,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_422 import (
    PostSystemCertificateSigningRequestSignEndpointResponse422,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_424 import (
    PostSystemCertificateSigningRequestSignEndpointResponse424,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_500 import (
    PostSystemCertificateSigningRequestSignEndpointResponse500,
)
from ...models.post_system_certificate_signing_request_sign_endpoint_response_503 import (
    PostSystemCertificateSigningRequestSignEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateSigningRequestSignEndpointJsonBody
    | PostSystemCertificateSigningRequestSignEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate/signing_request/sign",
    }

    if isinstance(body, PostSystemCertificateSigningRequestSignEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateSigningRequestSignEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateSigningRequestSignEndpointResponse400
    | PostSystemCertificateSigningRequestSignEndpointResponse401
    | PostSystemCertificateSigningRequestSignEndpointResponse403
    | PostSystemCertificateSigningRequestSignEndpointResponse404
    | PostSystemCertificateSigningRequestSignEndpointResponse405
    | PostSystemCertificateSigningRequestSignEndpointResponse406
    | PostSystemCertificateSigningRequestSignEndpointResponse409
    | PostSystemCertificateSigningRequestSignEndpointResponse415
    | PostSystemCertificateSigningRequestSignEndpointResponse422
    | PostSystemCertificateSigningRequestSignEndpointResponse424
    | PostSystemCertificateSigningRequestSignEndpointResponse500
    | PostSystemCertificateSigningRequestSignEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateSigningRequestSignEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateSigningRequestSignEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateSigningRequestSignEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateSigningRequestSignEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateSigningRequestSignEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateSigningRequestSignEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateSigningRequestSignEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateSigningRequestSignEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateSigningRequestSignEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateSigningRequestSignEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateSigningRequestSignEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateSigningRequestSignEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateSigningRequestSignEndpointResponse400
    | PostSystemCertificateSigningRequestSignEndpointResponse401
    | PostSystemCertificateSigningRequestSignEndpointResponse403
    | PostSystemCertificateSigningRequestSignEndpointResponse404
    | PostSystemCertificateSigningRequestSignEndpointResponse405
    | PostSystemCertificateSigningRequestSignEndpointResponse406
    | PostSystemCertificateSigningRequestSignEndpointResponse409
    | PostSystemCertificateSigningRequestSignEndpointResponse415
    | PostSystemCertificateSigningRequestSignEndpointResponse422
    | PostSystemCertificateSigningRequestSignEndpointResponse424
    | PostSystemCertificateSigningRequestSignEndpointResponse500
    | PostSystemCertificateSigningRequestSignEndpointResponse503
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
    body: PostSystemCertificateSigningRequestSignEndpointJsonBody
    | PostSystemCertificateSigningRequestSignEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateSigningRequestSignEndpointResponse400
    | PostSystemCertificateSigningRequestSignEndpointResponse401
    | PostSystemCertificateSigningRequestSignEndpointResponse403
    | PostSystemCertificateSigningRequestSignEndpointResponse404
    | PostSystemCertificateSigningRequestSignEndpointResponse405
    | PostSystemCertificateSigningRequestSignEndpointResponse406
    | PostSystemCertificateSigningRequestSignEndpointResponse409
    | PostSystemCertificateSigningRequestSignEndpointResponse415
    | PostSystemCertificateSigningRequestSignEndpointResponse422
    | PostSystemCertificateSigningRequestSignEndpointResponse424
    | PostSystemCertificateSigningRequestSignEndpointResponse500
    | PostSystemCertificateSigningRequestSignEndpointResponse503
]:
    """<h3>Description:</h3>Signs an existing Certificate Signing Request (CSR) with an existing
    Certificate Authority (CA).<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateSigningRequestSign<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-signing-request-sign-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateSigningRequestSignEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestSignEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateSigningRequestSignEndpointResponse400 | PostSystemCertificateSigningRequestSignEndpointResponse401 | PostSystemCertificateSigningRequestSignEndpointResponse403 | PostSystemCertificateSigningRequestSignEndpointResponse404 | PostSystemCertificateSigningRequestSignEndpointResponse405 | PostSystemCertificateSigningRequestSignEndpointResponse406 | PostSystemCertificateSigningRequestSignEndpointResponse409 | PostSystemCertificateSigningRequestSignEndpointResponse415 | PostSystemCertificateSigningRequestSignEndpointResponse422 | PostSystemCertificateSigningRequestSignEndpointResponse424 | PostSystemCertificateSigningRequestSignEndpointResponse500 | PostSystemCertificateSigningRequestSignEndpointResponse503]
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
    body: PostSystemCertificateSigningRequestSignEndpointJsonBody
    | PostSystemCertificateSigningRequestSignEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateSigningRequestSignEndpointResponse400
    | PostSystemCertificateSigningRequestSignEndpointResponse401
    | PostSystemCertificateSigningRequestSignEndpointResponse403
    | PostSystemCertificateSigningRequestSignEndpointResponse404
    | PostSystemCertificateSigningRequestSignEndpointResponse405
    | PostSystemCertificateSigningRequestSignEndpointResponse406
    | PostSystemCertificateSigningRequestSignEndpointResponse409
    | PostSystemCertificateSigningRequestSignEndpointResponse415
    | PostSystemCertificateSigningRequestSignEndpointResponse422
    | PostSystemCertificateSigningRequestSignEndpointResponse424
    | PostSystemCertificateSigningRequestSignEndpointResponse500
    | PostSystemCertificateSigningRequestSignEndpointResponse503
    | None
):
    """<h3>Description:</h3>Signs an existing Certificate Signing Request (CSR) with an existing
    Certificate Authority (CA).<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateSigningRequestSign<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-signing-request-sign-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateSigningRequestSignEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestSignEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateSigningRequestSignEndpointResponse400 | PostSystemCertificateSigningRequestSignEndpointResponse401 | PostSystemCertificateSigningRequestSignEndpointResponse403 | PostSystemCertificateSigningRequestSignEndpointResponse404 | PostSystemCertificateSigningRequestSignEndpointResponse405 | PostSystemCertificateSigningRequestSignEndpointResponse406 | PostSystemCertificateSigningRequestSignEndpointResponse409 | PostSystemCertificateSigningRequestSignEndpointResponse415 | PostSystemCertificateSigningRequestSignEndpointResponse422 | PostSystemCertificateSigningRequestSignEndpointResponse424 | PostSystemCertificateSigningRequestSignEndpointResponse500 | PostSystemCertificateSigningRequestSignEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateSigningRequestSignEndpointJsonBody
    | PostSystemCertificateSigningRequestSignEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateSigningRequestSignEndpointResponse400
    | PostSystemCertificateSigningRequestSignEndpointResponse401
    | PostSystemCertificateSigningRequestSignEndpointResponse403
    | PostSystemCertificateSigningRequestSignEndpointResponse404
    | PostSystemCertificateSigningRequestSignEndpointResponse405
    | PostSystemCertificateSigningRequestSignEndpointResponse406
    | PostSystemCertificateSigningRequestSignEndpointResponse409
    | PostSystemCertificateSigningRequestSignEndpointResponse415
    | PostSystemCertificateSigningRequestSignEndpointResponse422
    | PostSystemCertificateSigningRequestSignEndpointResponse424
    | PostSystemCertificateSigningRequestSignEndpointResponse500
    | PostSystemCertificateSigningRequestSignEndpointResponse503
]:
    """<h3>Description:</h3>Signs an existing Certificate Signing Request (CSR) with an existing
    Certificate Authority (CA).<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateSigningRequestSign<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-signing-request-sign-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateSigningRequestSignEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestSignEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateSigningRequestSignEndpointResponse400 | PostSystemCertificateSigningRequestSignEndpointResponse401 | PostSystemCertificateSigningRequestSignEndpointResponse403 | PostSystemCertificateSigningRequestSignEndpointResponse404 | PostSystemCertificateSigningRequestSignEndpointResponse405 | PostSystemCertificateSigningRequestSignEndpointResponse406 | PostSystemCertificateSigningRequestSignEndpointResponse409 | PostSystemCertificateSigningRequestSignEndpointResponse415 | PostSystemCertificateSigningRequestSignEndpointResponse422 | PostSystemCertificateSigningRequestSignEndpointResponse424 | PostSystemCertificateSigningRequestSignEndpointResponse500 | PostSystemCertificateSigningRequestSignEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateSigningRequestSignEndpointJsonBody
    | PostSystemCertificateSigningRequestSignEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateSigningRequestSignEndpointResponse400
    | PostSystemCertificateSigningRequestSignEndpointResponse401
    | PostSystemCertificateSigningRequestSignEndpointResponse403
    | PostSystemCertificateSigningRequestSignEndpointResponse404
    | PostSystemCertificateSigningRequestSignEndpointResponse405
    | PostSystemCertificateSigningRequestSignEndpointResponse406
    | PostSystemCertificateSigningRequestSignEndpointResponse409
    | PostSystemCertificateSigningRequestSignEndpointResponse415
    | PostSystemCertificateSigningRequestSignEndpointResponse422
    | PostSystemCertificateSigningRequestSignEndpointResponse424
    | PostSystemCertificateSigningRequestSignEndpointResponse500
    | PostSystemCertificateSigningRequestSignEndpointResponse503
    | None
):
    """<h3>Description:</h3>Signs an existing Certificate Signing Request (CSR) with an existing
    Certificate Authority (CA).<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateSigningRequestSign<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-signing-request-sign-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateSigningRequestSignEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestSignEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateSigningRequestSignEndpointResponse400 | PostSystemCertificateSigningRequestSignEndpointResponse401 | PostSystemCertificateSigningRequestSignEndpointResponse403 | PostSystemCertificateSigningRequestSignEndpointResponse404 | PostSystemCertificateSigningRequestSignEndpointResponse405 | PostSystemCertificateSigningRequestSignEndpointResponse406 | PostSystemCertificateSigningRequestSignEndpointResponse409 | PostSystemCertificateSigningRequestSignEndpointResponse415 | PostSystemCertificateSigningRequestSignEndpointResponse422 | PostSystemCertificateSigningRequestSignEndpointResponse424 | PostSystemCertificateSigningRequestSignEndpointResponse500 | PostSystemCertificateSigningRequestSignEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
