from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_generate_endpoint_data_body import PostSystemCertificateGenerateEndpointDataBody
from ...models.post_system_certificate_generate_endpoint_json_body import PostSystemCertificateGenerateEndpointJsonBody
from ...models.post_system_certificate_generate_endpoint_response_400 import (
    PostSystemCertificateGenerateEndpointResponse400,
)
from ...models.post_system_certificate_generate_endpoint_response_401 import (
    PostSystemCertificateGenerateEndpointResponse401,
)
from ...models.post_system_certificate_generate_endpoint_response_403 import (
    PostSystemCertificateGenerateEndpointResponse403,
)
from ...models.post_system_certificate_generate_endpoint_response_404 import (
    PostSystemCertificateGenerateEndpointResponse404,
)
from ...models.post_system_certificate_generate_endpoint_response_405 import (
    PostSystemCertificateGenerateEndpointResponse405,
)
from ...models.post_system_certificate_generate_endpoint_response_406 import (
    PostSystemCertificateGenerateEndpointResponse406,
)
from ...models.post_system_certificate_generate_endpoint_response_409 import (
    PostSystemCertificateGenerateEndpointResponse409,
)
from ...models.post_system_certificate_generate_endpoint_response_415 import (
    PostSystemCertificateGenerateEndpointResponse415,
)
from ...models.post_system_certificate_generate_endpoint_response_422 import (
    PostSystemCertificateGenerateEndpointResponse422,
)
from ...models.post_system_certificate_generate_endpoint_response_424 import (
    PostSystemCertificateGenerateEndpointResponse424,
)
from ...models.post_system_certificate_generate_endpoint_response_500 import (
    PostSystemCertificateGenerateEndpointResponse500,
)
from ...models.post_system_certificate_generate_endpoint_response_503 import (
    PostSystemCertificateGenerateEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateGenerateEndpointJsonBody | PostSystemCertificateGenerateEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate/generate",
    }

    if isinstance(body, PostSystemCertificateGenerateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateGenerateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateGenerateEndpointResponse400
    | PostSystemCertificateGenerateEndpointResponse401
    | PostSystemCertificateGenerateEndpointResponse403
    | PostSystemCertificateGenerateEndpointResponse404
    | PostSystemCertificateGenerateEndpointResponse405
    | PostSystemCertificateGenerateEndpointResponse406
    | PostSystemCertificateGenerateEndpointResponse409
    | PostSystemCertificateGenerateEndpointResponse415
    | PostSystemCertificateGenerateEndpointResponse422
    | PostSystemCertificateGenerateEndpointResponse424
    | PostSystemCertificateGenerateEndpointResponse500
    | PostSystemCertificateGenerateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateGenerateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateGenerateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateGenerateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateGenerateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateGenerateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateGenerateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateGenerateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateGenerateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateGenerateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateGenerateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateGenerateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateGenerateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateGenerateEndpointResponse400
    | PostSystemCertificateGenerateEndpointResponse401
    | PostSystemCertificateGenerateEndpointResponse403
    | PostSystemCertificateGenerateEndpointResponse404
    | PostSystemCertificateGenerateEndpointResponse405
    | PostSystemCertificateGenerateEndpointResponse406
    | PostSystemCertificateGenerateEndpointResponse409
    | PostSystemCertificateGenerateEndpointResponse415
    | PostSystemCertificateGenerateEndpointResponse422
    | PostSystemCertificateGenerateEndpointResponse424
    | PostSystemCertificateGenerateEndpointResponse500
    | PostSystemCertificateGenerateEndpointResponse503
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
    body: PostSystemCertificateGenerateEndpointJsonBody | PostSystemCertificateGenerateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemCertificateGenerateEndpointResponse400
    | PostSystemCertificateGenerateEndpointResponse401
    | PostSystemCertificateGenerateEndpointResponse403
    | PostSystemCertificateGenerateEndpointResponse404
    | PostSystemCertificateGenerateEndpointResponse405
    | PostSystemCertificateGenerateEndpointResponse406
    | PostSystemCertificateGenerateEndpointResponse409
    | PostSystemCertificateGenerateEndpointResponse415
    | PostSystemCertificateGenerateEndpointResponse422
    | PostSystemCertificateGenerateEndpointResponse424
    | PostSystemCertificateGenerateEndpointResponse500
    | PostSystemCertificateGenerateEndpointResponse503
]:
    """<h3>Description:</h3>Generate a new internal certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateGenerate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateGenerateEndpointResponse400 | PostSystemCertificateGenerateEndpointResponse401 | PostSystemCertificateGenerateEndpointResponse403 | PostSystemCertificateGenerateEndpointResponse404 | PostSystemCertificateGenerateEndpointResponse405 | PostSystemCertificateGenerateEndpointResponse406 | PostSystemCertificateGenerateEndpointResponse409 | PostSystemCertificateGenerateEndpointResponse415 | PostSystemCertificateGenerateEndpointResponse422 | PostSystemCertificateGenerateEndpointResponse424 | PostSystemCertificateGenerateEndpointResponse500 | PostSystemCertificateGenerateEndpointResponse503]
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
    body: PostSystemCertificateGenerateEndpointJsonBody | PostSystemCertificateGenerateEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemCertificateGenerateEndpointResponse400
    | PostSystemCertificateGenerateEndpointResponse401
    | PostSystemCertificateGenerateEndpointResponse403
    | PostSystemCertificateGenerateEndpointResponse404
    | PostSystemCertificateGenerateEndpointResponse405
    | PostSystemCertificateGenerateEndpointResponse406
    | PostSystemCertificateGenerateEndpointResponse409
    | PostSystemCertificateGenerateEndpointResponse415
    | PostSystemCertificateGenerateEndpointResponse422
    | PostSystemCertificateGenerateEndpointResponse424
    | PostSystemCertificateGenerateEndpointResponse500
    | PostSystemCertificateGenerateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Generate a new internal certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateGenerate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateGenerateEndpointResponse400 | PostSystemCertificateGenerateEndpointResponse401 | PostSystemCertificateGenerateEndpointResponse403 | PostSystemCertificateGenerateEndpointResponse404 | PostSystemCertificateGenerateEndpointResponse405 | PostSystemCertificateGenerateEndpointResponse406 | PostSystemCertificateGenerateEndpointResponse409 | PostSystemCertificateGenerateEndpointResponse415 | PostSystemCertificateGenerateEndpointResponse422 | PostSystemCertificateGenerateEndpointResponse424 | PostSystemCertificateGenerateEndpointResponse500 | PostSystemCertificateGenerateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateGenerateEndpointJsonBody | PostSystemCertificateGenerateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemCertificateGenerateEndpointResponse400
    | PostSystemCertificateGenerateEndpointResponse401
    | PostSystemCertificateGenerateEndpointResponse403
    | PostSystemCertificateGenerateEndpointResponse404
    | PostSystemCertificateGenerateEndpointResponse405
    | PostSystemCertificateGenerateEndpointResponse406
    | PostSystemCertificateGenerateEndpointResponse409
    | PostSystemCertificateGenerateEndpointResponse415
    | PostSystemCertificateGenerateEndpointResponse422
    | PostSystemCertificateGenerateEndpointResponse424
    | PostSystemCertificateGenerateEndpointResponse500
    | PostSystemCertificateGenerateEndpointResponse503
]:
    """<h3>Description:</h3>Generate a new internal certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateGenerate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateGenerateEndpointResponse400 | PostSystemCertificateGenerateEndpointResponse401 | PostSystemCertificateGenerateEndpointResponse403 | PostSystemCertificateGenerateEndpointResponse404 | PostSystemCertificateGenerateEndpointResponse405 | PostSystemCertificateGenerateEndpointResponse406 | PostSystemCertificateGenerateEndpointResponse409 | PostSystemCertificateGenerateEndpointResponse415 | PostSystemCertificateGenerateEndpointResponse422 | PostSystemCertificateGenerateEndpointResponse424 | PostSystemCertificateGenerateEndpointResponse500 | PostSystemCertificateGenerateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateGenerateEndpointJsonBody | PostSystemCertificateGenerateEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemCertificateGenerateEndpointResponse400
    | PostSystemCertificateGenerateEndpointResponse401
    | PostSystemCertificateGenerateEndpointResponse403
    | PostSystemCertificateGenerateEndpointResponse404
    | PostSystemCertificateGenerateEndpointResponse405
    | PostSystemCertificateGenerateEndpointResponse406
    | PostSystemCertificateGenerateEndpointResponse409
    | PostSystemCertificateGenerateEndpointResponse415
    | PostSystemCertificateGenerateEndpointResponse422
    | PostSystemCertificateGenerateEndpointResponse424
    | PostSystemCertificateGenerateEndpointResponse500
    | PostSystemCertificateGenerateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Generate a new internal certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CertificateGenerate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-generate-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateGenerateEndpointJsonBody | Unset):
        body (PostSystemCertificateGenerateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateGenerateEndpointResponse400 | PostSystemCertificateGenerateEndpointResponse401 | PostSystemCertificateGenerateEndpointResponse403 | PostSystemCertificateGenerateEndpointResponse404 | PostSystemCertificateGenerateEndpointResponse405 | PostSystemCertificateGenerateEndpointResponse406 | PostSystemCertificateGenerateEndpointResponse409 | PostSystemCertificateGenerateEndpointResponse415 | PostSystemCertificateGenerateEndpointResponse422 | PostSystemCertificateGenerateEndpointResponse424 | PostSystemCertificateGenerateEndpointResponse500 | PostSystemCertificateGenerateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
