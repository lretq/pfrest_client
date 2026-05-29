from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_authority_generate_endpoint_data_body import (
    PostSystemCertificateAuthorityGenerateEndpointDataBody,
)
from ...models.post_system_certificate_authority_generate_endpoint_json_body import (
    PostSystemCertificateAuthorityGenerateEndpointJsonBody,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_400 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse400,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_401 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse401,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_403 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse403,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_404 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse404,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_405 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse405,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_406 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse406,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_409 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse409,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_415 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse415,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_422 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse422,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_424 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse424,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_500 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse500,
)
from ...models.post_system_certificate_authority_generate_endpoint_response_503 import (
    PostSystemCertificateAuthorityGenerateEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateAuthorityGenerateEndpointJsonBody
    | PostSystemCertificateAuthorityGenerateEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate_authority/generate",
    }

    if isinstance(body, PostSystemCertificateAuthorityGenerateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateAuthorityGenerateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateAuthorityGenerateEndpointResponse400
    | PostSystemCertificateAuthorityGenerateEndpointResponse401
    | PostSystemCertificateAuthorityGenerateEndpointResponse403
    | PostSystemCertificateAuthorityGenerateEndpointResponse404
    | PostSystemCertificateAuthorityGenerateEndpointResponse405
    | PostSystemCertificateAuthorityGenerateEndpointResponse406
    | PostSystemCertificateAuthorityGenerateEndpointResponse409
    | PostSystemCertificateAuthorityGenerateEndpointResponse415
    | PostSystemCertificateAuthorityGenerateEndpointResponse422
    | PostSystemCertificateAuthorityGenerateEndpointResponse424
    | PostSystemCertificateAuthorityGenerateEndpointResponse500
    | PostSystemCertificateAuthorityGenerateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateAuthorityGenerateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateAuthorityGenerateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateAuthorityGenerateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateAuthorityGenerateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateAuthorityGenerateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateAuthorityGenerateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateAuthorityGenerateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateAuthorityGenerateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateAuthorityGenerateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateAuthorityGenerateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateAuthorityGenerateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateAuthorityGenerateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateAuthorityGenerateEndpointResponse400
    | PostSystemCertificateAuthorityGenerateEndpointResponse401
    | PostSystemCertificateAuthorityGenerateEndpointResponse403
    | PostSystemCertificateAuthorityGenerateEndpointResponse404
    | PostSystemCertificateAuthorityGenerateEndpointResponse405
    | PostSystemCertificateAuthorityGenerateEndpointResponse406
    | PostSystemCertificateAuthorityGenerateEndpointResponse409
    | PostSystemCertificateAuthorityGenerateEndpointResponse415
    | PostSystemCertificateAuthorityGenerateEndpointResponse422
    | PostSystemCertificateAuthorityGenerateEndpointResponse424
    | PostSystemCertificateAuthorityGenerateEndpointResponse500
    | PostSystemCertificateAuthorityGenerateEndpointResponse503
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
    body: PostSystemCertificateAuthorityGenerateEndpointJsonBody
    | PostSystemCertificateAuthorityGenerateEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateAuthorityGenerateEndpointResponse400
    | PostSystemCertificateAuthorityGenerateEndpointResponse401
    | PostSystemCertificateAuthorityGenerateEndpointResponse403
    | PostSystemCertificateAuthorityGenerateEndpointResponse404
    | PostSystemCertificateAuthorityGenerateEndpointResponse405
    | PostSystemCertificateAuthorityGenerateEndpointResponse406
    | PostSystemCertificateAuthorityGenerateEndpointResponse409
    | PostSystemCertificateAuthorityGenerateEndpointResponse415
    | PostSystemCertificateAuthorityGenerateEndpointResponse422
    | PostSystemCertificateAuthorityGenerateEndpointResponse424
    | PostSystemCertificateAuthorityGenerateEndpointResponse500
    | PostSystemCertificateAuthorityGenerateEndpointResponse503
]:
    """<h3>Description:</h3>Generate a new internal or intermediate
    certificate.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateAuthorityGenerate<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-authority-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateAuthorityGenerateEndpointResponse400 | PostSystemCertificateAuthorityGenerateEndpointResponse401 | PostSystemCertificateAuthorityGenerateEndpointResponse403 | PostSystemCertificateAuthorityGenerateEndpointResponse404 | PostSystemCertificateAuthorityGenerateEndpointResponse405 | PostSystemCertificateAuthorityGenerateEndpointResponse406 | PostSystemCertificateAuthorityGenerateEndpointResponse409 | PostSystemCertificateAuthorityGenerateEndpointResponse415 | PostSystemCertificateAuthorityGenerateEndpointResponse422 | PostSystemCertificateAuthorityGenerateEndpointResponse424 | PostSystemCertificateAuthorityGenerateEndpointResponse500 | PostSystemCertificateAuthorityGenerateEndpointResponse503]
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
    body: PostSystemCertificateAuthorityGenerateEndpointJsonBody
    | PostSystemCertificateAuthorityGenerateEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateAuthorityGenerateEndpointResponse400
    | PostSystemCertificateAuthorityGenerateEndpointResponse401
    | PostSystemCertificateAuthorityGenerateEndpointResponse403
    | PostSystemCertificateAuthorityGenerateEndpointResponse404
    | PostSystemCertificateAuthorityGenerateEndpointResponse405
    | PostSystemCertificateAuthorityGenerateEndpointResponse406
    | PostSystemCertificateAuthorityGenerateEndpointResponse409
    | PostSystemCertificateAuthorityGenerateEndpointResponse415
    | PostSystemCertificateAuthorityGenerateEndpointResponse422
    | PostSystemCertificateAuthorityGenerateEndpointResponse424
    | PostSystemCertificateAuthorityGenerateEndpointResponse500
    | PostSystemCertificateAuthorityGenerateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Generate a new internal or intermediate
    certificate.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateAuthorityGenerate<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-authority-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateAuthorityGenerateEndpointResponse400 | PostSystemCertificateAuthorityGenerateEndpointResponse401 | PostSystemCertificateAuthorityGenerateEndpointResponse403 | PostSystemCertificateAuthorityGenerateEndpointResponse404 | PostSystemCertificateAuthorityGenerateEndpointResponse405 | PostSystemCertificateAuthorityGenerateEndpointResponse406 | PostSystemCertificateAuthorityGenerateEndpointResponse409 | PostSystemCertificateAuthorityGenerateEndpointResponse415 | PostSystemCertificateAuthorityGenerateEndpointResponse422 | PostSystemCertificateAuthorityGenerateEndpointResponse424 | PostSystemCertificateAuthorityGenerateEndpointResponse500 | PostSystemCertificateAuthorityGenerateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateAuthorityGenerateEndpointJsonBody
    | PostSystemCertificateAuthorityGenerateEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemCertificateAuthorityGenerateEndpointResponse400
    | PostSystemCertificateAuthorityGenerateEndpointResponse401
    | PostSystemCertificateAuthorityGenerateEndpointResponse403
    | PostSystemCertificateAuthorityGenerateEndpointResponse404
    | PostSystemCertificateAuthorityGenerateEndpointResponse405
    | PostSystemCertificateAuthorityGenerateEndpointResponse406
    | PostSystemCertificateAuthorityGenerateEndpointResponse409
    | PostSystemCertificateAuthorityGenerateEndpointResponse415
    | PostSystemCertificateAuthorityGenerateEndpointResponse422
    | PostSystemCertificateAuthorityGenerateEndpointResponse424
    | PostSystemCertificateAuthorityGenerateEndpointResponse500
    | PostSystemCertificateAuthorityGenerateEndpointResponse503
]:
    """<h3>Description:</h3>Generate a new internal or intermediate
    certificate.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateAuthorityGenerate<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-authority-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateAuthorityGenerateEndpointResponse400 | PostSystemCertificateAuthorityGenerateEndpointResponse401 | PostSystemCertificateAuthorityGenerateEndpointResponse403 | PostSystemCertificateAuthorityGenerateEndpointResponse404 | PostSystemCertificateAuthorityGenerateEndpointResponse405 | PostSystemCertificateAuthorityGenerateEndpointResponse406 | PostSystemCertificateAuthorityGenerateEndpointResponse409 | PostSystemCertificateAuthorityGenerateEndpointResponse415 | PostSystemCertificateAuthorityGenerateEndpointResponse422 | PostSystemCertificateAuthorityGenerateEndpointResponse424 | PostSystemCertificateAuthorityGenerateEndpointResponse500 | PostSystemCertificateAuthorityGenerateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateAuthorityGenerateEndpointJsonBody
    | PostSystemCertificateAuthorityGenerateEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemCertificateAuthorityGenerateEndpointResponse400
    | PostSystemCertificateAuthorityGenerateEndpointResponse401
    | PostSystemCertificateAuthorityGenerateEndpointResponse403
    | PostSystemCertificateAuthorityGenerateEndpointResponse404
    | PostSystemCertificateAuthorityGenerateEndpointResponse405
    | PostSystemCertificateAuthorityGenerateEndpointResponse406
    | PostSystemCertificateAuthorityGenerateEndpointResponse409
    | PostSystemCertificateAuthorityGenerateEndpointResponse415
    | PostSystemCertificateAuthorityGenerateEndpointResponse422
    | PostSystemCertificateAuthorityGenerateEndpointResponse424
    | PostSystemCertificateAuthorityGenerateEndpointResponse500
    | PostSystemCertificateAuthorityGenerateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Generate a new internal or intermediate
    certificate.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    CertificateAuthorityGenerate<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-certificate-authority-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateAuthorityGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateAuthorityGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateAuthorityGenerateEndpointResponse400 | PostSystemCertificateAuthorityGenerateEndpointResponse401 | PostSystemCertificateAuthorityGenerateEndpointResponse403 | PostSystemCertificateAuthorityGenerateEndpointResponse404 | PostSystemCertificateAuthorityGenerateEndpointResponse405 | PostSystemCertificateAuthorityGenerateEndpointResponse406 | PostSystemCertificateAuthorityGenerateEndpointResponse409 | PostSystemCertificateAuthorityGenerateEndpointResponse415 | PostSystemCertificateAuthorityGenerateEndpointResponse422 | PostSystemCertificateAuthorityGenerateEndpointResponse424 | PostSystemCertificateAuthorityGenerateEndpointResponse500 | PostSystemCertificateAuthorityGenerateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
