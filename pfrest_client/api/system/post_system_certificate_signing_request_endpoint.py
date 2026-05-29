from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_signing_request_endpoint_data_body import (
    PostSystemCertificateSigningRequestEndpointDataBody,
)
from ...models.post_system_certificate_signing_request_endpoint_json_body import (
    PostSystemCertificateSigningRequestEndpointJsonBody,
)
from ...models.post_system_certificate_signing_request_endpoint_response_400 import (
    PostSystemCertificateSigningRequestEndpointResponse400,
)
from ...models.post_system_certificate_signing_request_endpoint_response_401 import (
    PostSystemCertificateSigningRequestEndpointResponse401,
)
from ...models.post_system_certificate_signing_request_endpoint_response_403 import (
    PostSystemCertificateSigningRequestEndpointResponse403,
)
from ...models.post_system_certificate_signing_request_endpoint_response_404 import (
    PostSystemCertificateSigningRequestEndpointResponse404,
)
from ...models.post_system_certificate_signing_request_endpoint_response_405 import (
    PostSystemCertificateSigningRequestEndpointResponse405,
)
from ...models.post_system_certificate_signing_request_endpoint_response_406 import (
    PostSystemCertificateSigningRequestEndpointResponse406,
)
from ...models.post_system_certificate_signing_request_endpoint_response_409 import (
    PostSystemCertificateSigningRequestEndpointResponse409,
)
from ...models.post_system_certificate_signing_request_endpoint_response_415 import (
    PostSystemCertificateSigningRequestEndpointResponse415,
)
from ...models.post_system_certificate_signing_request_endpoint_response_422 import (
    PostSystemCertificateSigningRequestEndpointResponse422,
)
from ...models.post_system_certificate_signing_request_endpoint_response_424 import (
    PostSystemCertificateSigningRequestEndpointResponse424,
)
from ...models.post_system_certificate_signing_request_endpoint_response_500 import (
    PostSystemCertificateSigningRequestEndpointResponse500,
)
from ...models.post_system_certificate_signing_request_endpoint_response_503 import (
    PostSystemCertificateSigningRequestEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateSigningRequestEndpointJsonBody
    | PostSystemCertificateSigningRequestEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate/signing_request",
    }

    if isinstance(body, PostSystemCertificateSigningRequestEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateSigningRequestEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateSigningRequestEndpointResponse400
    | PostSystemCertificateSigningRequestEndpointResponse401
    | PostSystemCertificateSigningRequestEndpointResponse403
    | PostSystemCertificateSigningRequestEndpointResponse404
    | PostSystemCertificateSigningRequestEndpointResponse405
    | PostSystemCertificateSigningRequestEndpointResponse406
    | PostSystemCertificateSigningRequestEndpointResponse409
    | PostSystemCertificateSigningRequestEndpointResponse415
    | PostSystemCertificateSigningRequestEndpointResponse422
    | PostSystemCertificateSigningRequestEndpointResponse424
    | PostSystemCertificateSigningRequestEndpointResponse500
    | PostSystemCertificateSigningRequestEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateSigningRequestEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateSigningRequestEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateSigningRequestEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateSigningRequestEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateSigningRequestEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateSigningRequestEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateSigningRequestEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateSigningRequestEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateSigningRequestEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateSigningRequestEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateSigningRequestEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateSigningRequestEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateSigningRequestEndpointResponse400
    | PostSystemCertificateSigningRequestEndpointResponse401
    | PostSystemCertificateSigningRequestEndpointResponse403
    | PostSystemCertificateSigningRequestEndpointResponse404
    | PostSystemCertificateSigningRequestEndpointResponse405
    | PostSystemCertificateSigningRequestEndpointResponse406
    | PostSystemCertificateSigningRequestEndpointResponse409
    | PostSystemCertificateSigningRequestEndpointResponse415
    | PostSystemCertificateSigningRequestEndpointResponse422
    | PostSystemCertificateSigningRequestEndpointResponse424
    | PostSystemCertificateSigningRequestEndpointResponse500
    | PostSystemCertificateSigningRequestEndpointResponse503
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
    body: PostSystemCertificateSigningRequestEndpointJsonBody
    | PostSystemCertificateSigningRequestEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateSigningRequestEndpointResponse400
    | PostSystemCertificateSigningRequestEndpointResponse401
    | PostSystemCertificateSigningRequestEndpointResponse403
    | PostSystemCertificateSigningRequestEndpointResponse404
    | PostSystemCertificateSigningRequestEndpointResponse405
    | PostSystemCertificateSigningRequestEndpointResponse406
    | PostSystemCertificateSigningRequestEndpointResponse409
    | PostSystemCertificateSigningRequestEndpointResponse415
    | PostSystemCertificateSigningRequestEndpointResponse422
    | PostSystemCertificateSigningRequestEndpointResponse424
    | PostSystemCertificateSigningRequestEndpointResponse500
    | PostSystemCertificateSigningRequestEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate Signing Request.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateSigningRequest<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-signing-request-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostSystemCertificateSigningRequestEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateSigningRequestEndpointResponse400 | PostSystemCertificateSigningRequestEndpointResponse401 | PostSystemCertificateSigningRequestEndpointResponse403 | PostSystemCertificateSigningRequestEndpointResponse404 | PostSystemCertificateSigningRequestEndpointResponse405 | PostSystemCertificateSigningRequestEndpointResponse406 | PostSystemCertificateSigningRequestEndpointResponse409 | PostSystemCertificateSigningRequestEndpointResponse415 | PostSystemCertificateSigningRequestEndpointResponse422 | PostSystemCertificateSigningRequestEndpointResponse424 | PostSystemCertificateSigningRequestEndpointResponse500 | PostSystemCertificateSigningRequestEndpointResponse503]
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
    body: PostSystemCertificateSigningRequestEndpointJsonBody
    | PostSystemCertificateSigningRequestEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateSigningRequestEndpointResponse400
    | PostSystemCertificateSigningRequestEndpointResponse401
    | PostSystemCertificateSigningRequestEndpointResponse403
    | PostSystemCertificateSigningRequestEndpointResponse404
    | PostSystemCertificateSigningRequestEndpointResponse405
    | PostSystemCertificateSigningRequestEndpointResponse406
    | PostSystemCertificateSigningRequestEndpointResponse409
    | PostSystemCertificateSigningRequestEndpointResponse415
    | PostSystemCertificateSigningRequestEndpointResponse422
    | PostSystemCertificateSigningRequestEndpointResponse424
    | PostSystemCertificateSigningRequestEndpointResponse500
    | PostSystemCertificateSigningRequestEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate Signing Request.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateSigningRequest<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-signing-request-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostSystemCertificateSigningRequestEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateSigningRequestEndpointResponse400 | PostSystemCertificateSigningRequestEndpointResponse401 | PostSystemCertificateSigningRequestEndpointResponse403 | PostSystemCertificateSigningRequestEndpointResponse404 | PostSystemCertificateSigningRequestEndpointResponse405 | PostSystemCertificateSigningRequestEndpointResponse406 | PostSystemCertificateSigningRequestEndpointResponse409 | PostSystemCertificateSigningRequestEndpointResponse415 | PostSystemCertificateSigningRequestEndpointResponse422 | PostSystemCertificateSigningRequestEndpointResponse424 | PostSystemCertificateSigningRequestEndpointResponse500 | PostSystemCertificateSigningRequestEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateSigningRequestEndpointJsonBody
    | PostSystemCertificateSigningRequestEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateSigningRequestEndpointResponse400
    | PostSystemCertificateSigningRequestEndpointResponse401
    | PostSystemCertificateSigningRequestEndpointResponse403
    | PostSystemCertificateSigningRequestEndpointResponse404
    | PostSystemCertificateSigningRequestEndpointResponse405
    | PostSystemCertificateSigningRequestEndpointResponse406
    | PostSystemCertificateSigningRequestEndpointResponse409
    | PostSystemCertificateSigningRequestEndpointResponse415
    | PostSystemCertificateSigningRequestEndpointResponse422
    | PostSystemCertificateSigningRequestEndpointResponse424
    | PostSystemCertificateSigningRequestEndpointResponse500
    | PostSystemCertificateSigningRequestEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate Signing Request.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateSigningRequest<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-signing-request-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostSystemCertificateSigningRequestEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateSigningRequestEndpointResponse400 | PostSystemCertificateSigningRequestEndpointResponse401 | PostSystemCertificateSigningRequestEndpointResponse403 | PostSystemCertificateSigningRequestEndpointResponse404 | PostSystemCertificateSigningRequestEndpointResponse405 | PostSystemCertificateSigningRequestEndpointResponse406 | PostSystemCertificateSigningRequestEndpointResponse409 | PostSystemCertificateSigningRequestEndpointResponse415 | PostSystemCertificateSigningRequestEndpointResponse422 | PostSystemCertificateSigningRequestEndpointResponse424 | PostSystemCertificateSigningRequestEndpointResponse500 | PostSystemCertificateSigningRequestEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateSigningRequestEndpointJsonBody
    | PostSystemCertificateSigningRequestEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateSigningRequestEndpointResponse400
    | PostSystemCertificateSigningRequestEndpointResponse401
    | PostSystemCertificateSigningRequestEndpointResponse403
    | PostSystemCertificateSigningRequestEndpointResponse404
    | PostSystemCertificateSigningRequestEndpointResponse405
    | PostSystemCertificateSigningRequestEndpointResponse406
    | PostSystemCertificateSigningRequestEndpointResponse409
    | PostSystemCertificateSigningRequestEndpointResponse415
    | PostSystemCertificateSigningRequestEndpointResponse422
    | PostSystemCertificateSigningRequestEndpointResponse424
    | PostSystemCertificateSigningRequestEndpointResponse500
    | PostSystemCertificateSigningRequestEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate Signing Request.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateSigningRequest<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-signing-request-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostSystemCertificateSigningRequestEndpointJsonBody | Unset):
        body (PostSystemCertificateSigningRequestEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateSigningRequestEndpointResponse400 | PostSystemCertificateSigningRequestEndpointResponse401 | PostSystemCertificateSigningRequestEndpointResponse403 | PostSystemCertificateSigningRequestEndpointResponse404 | PostSystemCertificateSigningRequestEndpointResponse405 | PostSystemCertificateSigningRequestEndpointResponse406 | PostSystemCertificateSigningRequestEndpointResponse409 | PostSystemCertificateSigningRequestEndpointResponse415 | PostSystemCertificateSigningRequestEndpointResponse422 | PostSystemCertificateSigningRequestEndpointResponse424 | PostSystemCertificateSigningRequestEndpointResponse500 | PostSystemCertificateSigningRequestEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
