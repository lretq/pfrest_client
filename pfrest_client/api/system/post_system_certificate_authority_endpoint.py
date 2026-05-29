from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_authority_endpoint_data_body import (
    PostSystemCertificateAuthorityEndpointDataBody,
)
from ...models.post_system_certificate_authority_endpoint_json_body import (
    PostSystemCertificateAuthorityEndpointJsonBody,
)
from ...models.post_system_certificate_authority_endpoint_response_400 import (
    PostSystemCertificateAuthorityEndpointResponse400,
)
from ...models.post_system_certificate_authority_endpoint_response_401 import (
    PostSystemCertificateAuthorityEndpointResponse401,
)
from ...models.post_system_certificate_authority_endpoint_response_403 import (
    PostSystemCertificateAuthorityEndpointResponse403,
)
from ...models.post_system_certificate_authority_endpoint_response_404 import (
    PostSystemCertificateAuthorityEndpointResponse404,
)
from ...models.post_system_certificate_authority_endpoint_response_405 import (
    PostSystemCertificateAuthorityEndpointResponse405,
)
from ...models.post_system_certificate_authority_endpoint_response_406 import (
    PostSystemCertificateAuthorityEndpointResponse406,
)
from ...models.post_system_certificate_authority_endpoint_response_409 import (
    PostSystemCertificateAuthorityEndpointResponse409,
)
from ...models.post_system_certificate_authority_endpoint_response_415 import (
    PostSystemCertificateAuthorityEndpointResponse415,
)
from ...models.post_system_certificate_authority_endpoint_response_422 import (
    PostSystemCertificateAuthorityEndpointResponse422,
)
from ...models.post_system_certificate_authority_endpoint_response_424 import (
    PostSystemCertificateAuthorityEndpointResponse424,
)
from ...models.post_system_certificate_authority_endpoint_response_500 import (
    PostSystemCertificateAuthorityEndpointResponse500,
)
from ...models.post_system_certificate_authority_endpoint_response_503 import (
    PostSystemCertificateAuthorityEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateAuthorityEndpointJsonBody
    | PostSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate_authority",
    }

    if isinstance(body, PostSystemCertificateAuthorityEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateAuthorityEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateAuthorityEndpointResponse400
    | PostSystemCertificateAuthorityEndpointResponse401
    | PostSystemCertificateAuthorityEndpointResponse403
    | PostSystemCertificateAuthorityEndpointResponse404
    | PostSystemCertificateAuthorityEndpointResponse405
    | PostSystemCertificateAuthorityEndpointResponse406
    | PostSystemCertificateAuthorityEndpointResponse409
    | PostSystemCertificateAuthorityEndpointResponse415
    | PostSystemCertificateAuthorityEndpointResponse422
    | PostSystemCertificateAuthorityEndpointResponse424
    | PostSystemCertificateAuthorityEndpointResponse500
    | PostSystemCertificateAuthorityEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateAuthorityEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateAuthorityEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateAuthorityEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateAuthorityEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateAuthorityEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateAuthorityEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateAuthorityEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateAuthorityEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateAuthorityEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateAuthorityEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateAuthorityEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateAuthorityEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateAuthorityEndpointResponse400
    | PostSystemCertificateAuthorityEndpointResponse401
    | PostSystemCertificateAuthorityEndpointResponse403
    | PostSystemCertificateAuthorityEndpointResponse404
    | PostSystemCertificateAuthorityEndpointResponse405
    | PostSystemCertificateAuthorityEndpointResponse406
    | PostSystemCertificateAuthorityEndpointResponse409
    | PostSystemCertificateAuthorityEndpointResponse415
    | PostSystemCertificateAuthorityEndpointResponse422
    | PostSystemCertificateAuthorityEndpointResponse424
    | PostSystemCertificateAuthorityEndpointResponse500
    | PostSystemCertificateAuthorityEndpointResponse503
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
    body: PostSystemCertificateAuthorityEndpointJsonBody
    | PostSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateAuthorityEndpointResponse400
    | PostSystemCertificateAuthorityEndpointResponse401
    | PostSystemCertificateAuthorityEndpointResponse403
    | PostSystemCertificateAuthorityEndpointResponse404
    | PostSystemCertificateAuthorityEndpointResponse405
    | PostSystemCertificateAuthorityEndpointResponse406
    | PostSystemCertificateAuthorityEndpointResponse409
    | PostSystemCertificateAuthorityEndpointResponse415
    | PostSystemCertificateAuthorityEndpointResponse422
    | PostSystemCertificateAuthorityEndpointResponse424
    | PostSystemCertificateAuthorityEndpointResponse500
    | PostSystemCertificateAuthorityEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate Authority.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateAuthorityEndpointResponse400 | PostSystemCertificateAuthorityEndpointResponse401 | PostSystemCertificateAuthorityEndpointResponse403 | PostSystemCertificateAuthorityEndpointResponse404 | PostSystemCertificateAuthorityEndpointResponse405 | PostSystemCertificateAuthorityEndpointResponse406 | PostSystemCertificateAuthorityEndpointResponse409 | PostSystemCertificateAuthorityEndpointResponse415 | PostSystemCertificateAuthorityEndpointResponse422 | PostSystemCertificateAuthorityEndpointResponse424 | PostSystemCertificateAuthorityEndpointResponse500 | PostSystemCertificateAuthorityEndpointResponse503]
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
    body: PostSystemCertificateAuthorityEndpointJsonBody
    | PostSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateAuthorityEndpointResponse400
    | PostSystemCertificateAuthorityEndpointResponse401
    | PostSystemCertificateAuthorityEndpointResponse403
    | PostSystemCertificateAuthorityEndpointResponse404
    | PostSystemCertificateAuthorityEndpointResponse405
    | PostSystemCertificateAuthorityEndpointResponse406
    | PostSystemCertificateAuthorityEndpointResponse409
    | PostSystemCertificateAuthorityEndpointResponse415
    | PostSystemCertificateAuthorityEndpointResponse422
    | PostSystemCertificateAuthorityEndpointResponse424
    | PostSystemCertificateAuthorityEndpointResponse500
    | PostSystemCertificateAuthorityEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate Authority.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateAuthorityEndpointResponse400 | PostSystemCertificateAuthorityEndpointResponse401 | PostSystemCertificateAuthorityEndpointResponse403 | PostSystemCertificateAuthorityEndpointResponse404 | PostSystemCertificateAuthorityEndpointResponse405 | PostSystemCertificateAuthorityEndpointResponse406 | PostSystemCertificateAuthorityEndpointResponse409 | PostSystemCertificateAuthorityEndpointResponse415 | PostSystemCertificateAuthorityEndpointResponse422 | PostSystemCertificateAuthorityEndpointResponse424 | PostSystemCertificateAuthorityEndpointResponse500 | PostSystemCertificateAuthorityEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateAuthorityEndpointJsonBody
    | PostSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateAuthorityEndpointResponse400
    | PostSystemCertificateAuthorityEndpointResponse401
    | PostSystemCertificateAuthorityEndpointResponse403
    | PostSystemCertificateAuthorityEndpointResponse404
    | PostSystemCertificateAuthorityEndpointResponse405
    | PostSystemCertificateAuthorityEndpointResponse406
    | PostSystemCertificateAuthorityEndpointResponse409
    | PostSystemCertificateAuthorityEndpointResponse415
    | PostSystemCertificateAuthorityEndpointResponse422
    | PostSystemCertificateAuthorityEndpointResponse424
    | PostSystemCertificateAuthorityEndpointResponse500
    | PostSystemCertificateAuthorityEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate Authority.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateAuthorityEndpointResponse400 | PostSystemCertificateAuthorityEndpointResponse401 | PostSystemCertificateAuthorityEndpointResponse403 | PostSystemCertificateAuthorityEndpointResponse404 | PostSystemCertificateAuthorityEndpointResponse405 | PostSystemCertificateAuthorityEndpointResponse406 | PostSystemCertificateAuthorityEndpointResponse409 | PostSystemCertificateAuthorityEndpointResponse415 | PostSystemCertificateAuthorityEndpointResponse422 | PostSystemCertificateAuthorityEndpointResponse424 | PostSystemCertificateAuthorityEndpointResponse500 | PostSystemCertificateAuthorityEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateAuthorityEndpointJsonBody
    | PostSystemCertificateAuthorityEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateAuthorityEndpointResponse400
    | PostSystemCertificateAuthorityEndpointResponse401
    | PostSystemCertificateAuthorityEndpointResponse403
    | PostSystemCertificateAuthorityEndpointResponse404
    | PostSystemCertificateAuthorityEndpointResponse405
    | PostSystemCertificateAuthorityEndpointResponse406
    | PostSystemCertificateAuthorityEndpointResponse409
    | PostSystemCertificateAuthorityEndpointResponse415
    | PostSystemCertificateAuthorityEndpointResponse422
    | PostSystemCertificateAuthorityEndpointResponse424
    | PostSystemCertificateAuthorityEndpointResponse500
    | PostSystemCertificateAuthorityEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate Authority.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateAuthority<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-authority-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateAuthorityEndpointResponse400 | PostSystemCertificateAuthorityEndpointResponse401 | PostSystemCertificateAuthorityEndpointResponse403 | PostSystemCertificateAuthorityEndpointResponse404 | PostSystemCertificateAuthorityEndpointResponse405 | PostSystemCertificateAuthorityEndpointResponse406 | PostSystemCertificateAuthorityEndpointResponse409 | PostSystemCertificateAuthorityEndpointResponse415 | PostSystemCertificateAuthorityEndpointResponse422 | PostSystemCertificateAuthorityEndpointResponse424 | PostSystemCertificateAuthorityEndpointResponse500 | PostSystemCertificateAuthorityEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
