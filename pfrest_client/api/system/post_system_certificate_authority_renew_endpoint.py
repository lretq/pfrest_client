from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_authority_renew_endpoint_data_body import (
    PostSystemCertificateAuthorityRenewEndpointDataBody,
)
from ...models.post_system_certificate_authority_renew_endpoint_json_body import (
    PostSystemCertificateAuthorityRenewEndpointJsonBody,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_400 import (
    PostSystemCertificateAuthorityRenewEndpointResponse400,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_401 import (
    PostSystemCertificateAuthorityRenewEndpointResponse401,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_403 import (
    PostSystemCertificateAuthorityRenewEndpointResponse403,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_404 import (
    PostSystemCertificateAuthorityRenewEndpointResponse404,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_405 import (
    PostSystemCertificateAuthorityRenewEndpointResponse405,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_406 import (
    PostSystemCertificateAuthorityRenewEndpointResponse406,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_409 import (
    PostSystemCertificateAuthorityRenewEndpointResponse409,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_415 import (
    PostSystemCertificateAuthorityRenewEndpointResponse415,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_422 import (
    PostSystemCertificateAuthorityRenewEndpointResponse422,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_424 import (
    PostSystemCertificateAuthorityRenewEndpointResponse424,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_500 import (
    PostSystemCertificateAuthorityRenewEndpointResponse500,
)
from ...models.post_system_certificate_authority_renew_endpoint_response_503 import (
    PostSystemCertificateAuthorityRenewEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateAuthorityRenewEndpointJsonBody
    | PostSystemCertificateAuthorityRenewEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate_authority/renew",
    }

    if isinstance(body, PostSystemCertificateAuthorityRenewEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateAuthorityRenewEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateAuthorityRenewEndpointResponse400
    | PostSystemCertificateAuthorityRenewEndpointResponse401
    | PostSystemCertificateAuthorityRenewEndpointResponse403
    | PostSystemCertificateAuthorityRenewEndpointResponse404
    | PostSystemCertificateAuthorityRenewEndpointResponse405
    | PostSystemCertificateAuthorityRenewEndpointResponse406
    | PostSystemCertificateAuthorityRenewEndpointResponse409
    | PostSystemCertificateAuthorityRenewEndpointResponse415
    | PostSystemCertificateAuthorityRenewEndpointResponse422
    | PostSystemCertificateAuthorityRenewEndpointResponse424
    | PostSystemCertificateAuthorityRenewEndpointResponse500
    | PostSystemCertificateAuthorityRenewEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateAuthorityRenewEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateAuthorityRenewEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateAuthorityRenewEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateAuthorityRenewEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateAuthorityRenewEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateAuthorityRenewEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateAuthorityRenewEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateAuthorityRenewEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateAuthorityRenewEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateAuthorityRenewEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateAuthorityRenewEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateAuthorityRenewEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateAuthorityRenewEndpointResponse400
    | PostSystemCertificateAuthorityRenewEndpointResponse401
    | PostSystemCertificateAuthorityRenewEndpointResponse403
    | PostSystemCertificateAuthorityRenewEndpointResponse404
    | PostSystemCertificateAuthorityRenewEndpointResponse405
    | PostSystemCertificateAuthorityRenewEndpointResponse406
    | PostSystemCertificateAuthorityRenewEndpointResponse409
    | PostSystemCertificateAuthorityRenewEndpointResponse415
    | PostSystemCertificateAuthorityRenewEndpointResponse422
    | PostSystemCertificateAuthorityRenewEndpointResponse424
    | PostSystemCertificateAuthorityRenewEndpointResponse500
    | PostSystemCertificateAuthorityRenewEndpointResponse503
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
    body: PostSystemCertificateAuthorityRenewEndpointJsonBody
    | PostSystemCertificateAuthorityRenewEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateAuthorityRenewEndpointResponse400
    | PostSystemCertificateAuthorityRenewEndpointResponse401
    | PostSystemCertificateAuthorityRenewEndpointResponse403
    | PostSystemCertificateAuthorityRenewEndpointResponse404
    | PostSystemCertificateAuthorityRenewEndpointResponse405
    | PostSystemCertificateAuthorityRenewEndpointResponse406
    | PostSystemCertificateAuthorityRenewEndpointResponse409
    | PostSystemCertificateAuthorityRenewEndpointResponse415
    | PostSystemCertificateAuthorityRenewEndpointResponse422
    | PostSystemCertificateAuthorityRenewEndpointResponse424
    | PostSystemCertificateAuthorityRenewEndpointResponse500
    | PostSystemCertificateAuthorityRenewEndpointResponse503
]:
    """<h3>Description:</h3>Renews an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthorityRenew<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-renew-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificateAuthorityRenewEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityRenewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateAuthorityRenewEndpointResponse400 | PostSystemCertificateAuthorityRenewEndpointResponse401 | PostSystemCertificateAuthorityRenewEndpointResponse403 | PostSystemCertificateAuthorityRenewEndpointResponse404 | PostSystemCertificateAuthorityRenewEndpointResponse405 | PostSystemCertificateAuthorityRenewEndpointResponse406 | PostSystemCertificateAuthorityRenewEndpointResponse409 | PostSystemCertificateAuthorityRenewEndpointResponse415 | PostSystemCertificateAuthorityRenewEndpointResponse422 | PostSystemCertificateAuthorityRenewEndpointResponse424 | PostSystemCertificateAuthorityRenewEndpointResponse500 | PostSystemCertificateAuthorityRenewEndpointResponse503]
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
    body: PostSystemCertificateAuthorityRenewEndpointJsonBody
    | PostSystemCertificateAuthorityRenewEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateAuthorityRenewEndpointResponse400
    | PostSystemCertificateAuthorityRenewEndpointResponse401
    | PostSystemCertificateAuthorityRenewEndpointResponse403
    | PostSystemCertificateAuthorityRenewEndpointResponse404
    | PostSystemCertificateAuthorityRenewEndpointResponse405
    | PostSystemCertificateAuthorityRenewEndpointResponse406
    | PostSystemCertificateAuthorityRenewEndpointResponse409
    | PostSystemCertificateAuthorityRenewEndpointResponse415
    | PostSystemCertificateAuthorityRenewEndpointResponse422
    | PostSystemCertificateAuthorityRenewEndpointResponse424
    | PostSystemCertificateAuthorityRenewEndpointResponse500
    | PostSystemCertificateAuthorityRenewEndpointResponse503
    | None
):
    """<h3>Description:</h3>Renews an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthorityRenew<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-renew-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificateAuthorityRenewEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityRenewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateAuthorityRenewEndpointResponse400 | PostSystemCertificateAuthorityRenewEndpointResponse401 | PostSystemCertificateAuthorityRenewEndpointResponse403 | PostSystemCertificateAuthorityRenewEndpointResponse404 | PostSystemCertificateAuthorityRenewEndpointResponse405 | PostSystemCertificateAuthorityRenewEndpointResponse406 | PostSystemCertificateAuthorityRenewEndpointResponse409 | PostSystemCertificateAuthorityRenewEndpointResponse415 | PostSystemCertificateAuthorityRenewEndpointResponse422 | PostSystemCertificateAuthorityRenewEndpointResponse424 | PostSystemCertificateAuthorityRenewEndpointResponse500 | PostSystemCertificateAuthorityRenewEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateAuthorityRenewEndpointJsonBody
    | PostSystemCertificateAuthorityRenewEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateAuthorityRenewEndpointResponse400
    | PostSystemCertificateAuthorityRenewEndpointResponse401
    | PostSystemCertificateAuthorityRenewEndpointResponse403
    | PostSystemCertificateAuthorityRenewEndpointResponse404
    | PostSystemCertificateAuthorityRenewEndpointResponse405
    | PostSystemCertificateAuthorityRenewEndpointResponse406
    | PostSystemCertificateAuthorityRenewEndpointResponse409
    | PostSystemCertificateAuthorityRenewEndpointResponse415
    | PostSystemCertificateAuthorityRenewEndpointResponse422
    | PostSystemCertificateAuthorityRenewEndpointResponse424
    | PostSystemCertificateAuthorityRenewEndpointResponse500
    | PostSystemCertificateAuthorityRenewEndpointResponse503
]:
    """<h3>Description:</h3>Renews an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthorityRenew<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-renew-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificateAuthorityRenewEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityRenewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateAuthorityRenewEndpointResponse400 | PostSystemCertificateAuthorityRenewEndpointResponse401 | PostSystemCertificateAuthorityRenewEndpointResponse403 | PostSystemCertificateAuthorityRenewEndpointResponse404 | PostSystemCertificateAuthorityRenewEndpointResponse405 | PostSystemCertificateAuthorityRenewEndpointResponse406 | PostSystemCertificateAuthorityRenewEndpointResponse409 | PostSystemCertificateAuthorityRenewEndpointResponse415 | PostSystemCertificateAuthorityRenewEndpointResponse422 | PostSystemCertificateAuthorityRenewEndpointResponse424 | PostSystemCertificateAuthorityRenewEndpointResponse500 | PostSystemCertificateAuthorityRenewEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateAuthorityRenewEndpointJsonBody
    | PostSystemCertificateAuthorityRenewEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateAuthorityRenewEndpointResponse400
    | PostSystemCertificateAuthorityRenewEndpointResponse401
    | PostSystemCertificateAuthorityRenewEndpointResponse403
    | PostSystemCertificateAuthorityRenewEndpointResponse404
    | PostSystemCertificateAuthorityRenewEndpointResponse405
    | PostSystemCertificateAuthorityRenewEndpointResponse406
    | PostSystemCertificateAuthorityRenewEndpointResponse409
    | PostSystemCertificateAuthorityRenewEndpointResponse415
    | PostSystemCertificateAuthorityRenewEndpointResponse422
    | PostSystemCertificateAuthorityRenewEndpointResponse424
    | PostSystemCertificateAuthorityRenewEndpointResponse500
    | PostSystemCertificateAuthorityRenewEndpointResponse503
    | None
):
    """<h3>Description:</h3>Renews an existing Certificate Authority.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateAuthorityRenew<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-renew-
    post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostSystemCertificateAuthorityRenewEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityRenewEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateAuthorityRenewEndpointResponse400 | PostSystemCertificateAuthorityRenewEndpointResponse401 | PostSystemCertificateAuthorityRenewEndpointResponse403 | PostSystemCertificateAuthorityRenewEndpointResponse404 | PostSystemCertificateAuthorityRenewEndpointResponse405 | PostSystemCertificateAuthorityRenewEndpointResponse406 | PostSystemCertificateAuthorityRenewEndpointResponse409 | PostSystemCertificateAuthorityRenewEndpointResponse415 | PostSystemCertificateAuthorityRenewEndpointResponse422 | PostSystemCertificateAuthorityRenewEndpointResponse424 | PostSystemCertificateAuthorityRenewEndpointResponse500 | PostSystemCertificateAuthorityRenewEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
