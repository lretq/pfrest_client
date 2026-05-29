from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_certificate_endpoint_data_body import PostSystemCertificateEndpointDataBody
from ...models.post_system_certificate_endpoint_json_body import PostSystemCertificateEndpointJsonBody
from ...models.post_system_certificate_endpoint_response_400 import PostSystemCertificateEndpointResponse400
from ...models.post_system_certificate_endpoint_response_401 import PostSystemCertificateEndpointResponse401
from ...models.post_system_certificate_endpoint_response_403 import PostSystemCertificateEndpointResponse403
from ...models.post_system_certificate_endpoint_response_404 import PostSystemCertificateEndpointResponse404
from ...models.post_system_certificate_endpoint_response_405 import PostSystemCertificateEndpointResponse405
from ...models.post_system_certificate_endpoint_response_406 import PostSystemCertificateEndpointResponse406
from ...models.post_system_certificate_endpoint_response_409 import PostSystemCertificateEndpointResponse409
from ...models.post_system_certificate_endpoint_response_415 import PostSystemCertificateEndpointResponse415
from ...models.post_system_certificate_endpoint_response_422 import PostSystemCertificateEndpointResponse422
from ...models.post_system_certificate_endpoint_response_424 import PostSystemCertificateEndpointResponse424
from ...models.post_system_certificate_endpoint_response_500 import PostSystemCertificateEndpointResponse500
from ...models.post_system_certificate_endpoint_response_503 import PostSystemCertificateEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCertificateEndpointJsonBody | PostSystemCertificateEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/certificate",
    }

    if isinstance(body, PostSystemCertificateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCertificateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCertificateEndpointResponse400
    | PostSystemCertificateEndpointResponse401
    | PostSystemCertificateEndpointResponse403
    | PostSystemCertificateEndpointResponse404
    | PostSystemCertificateEndpointResponse405
    | PostSystemCertificateEndpointResponse406
    | PostSystemCertificateEndpointResponse409
    | PostSystemCertificateEndpointResponse415
    | PostSystemCertificateEndpointResponse422
    | PostSystemCertificateEndpointResponse424
    | PostSystemCertificateEndpointResponse500
    | PostSystemCertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCertificateEndpointResponse400
    | PostSystemCertificateEndpointResponse401
    | PostSystemCertificateEndpointResponse403
    | PostSystemCertificateEndpointResponse404
    | PostSystemCertificateEndpointResponse405
    | PostSystemCertificateEndpointResponse406
    | PostSystemCertificateEndpointResponse409
    | PostSystemCertificateEndpointResponse415
    | PostSystemCertificateEndpointResponse422
    | PostSystemCertificateEndpointResponse424
    | PostSystemCertificateEndpointResponse500
    | PostSystemCertificateEndpointResponse503
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
    body: PostSystemCertificateEndpointJsonBody | PostSystemCertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemCertificateEndpointResponse400
    | PostSystemCertificateEndpointResponse401
    | PostSystemCertificateEndpointResponse403
    | PostSystemCertificateEndpointResponse404
    | PostSystemCertificateEndpointResponse405
    | PostSystemCertificateEndpointResponse406
    | PostSystemCertificateEndpointResponse409
    | PostSystemCertificateEndpointResponse415
    | PostSystemCertificateEndpointResponse422
    | PostSystemCertificateEndpointResponse424
    | PostSystemCertificateEndpointResponse500
    | PostSystemCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateEndpointJsonBody | Unset):
        body (PostSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateEndpointResponse400 | PostSystemCertificateEndpointResponse401 | PostSystemCertificateEndpointResponse403 | PostSystemCertificateEndpointResponse404 | PostSystemCertificateEndpointResponse405 | PostSystemCertificateEndpointResponse406 | PostSystemCertificateEndpointResponse409 | PostSystemCertificateEndpointResponse415 | PostSystemCertificateEndpointResponse422 | PostSystemCertificateEndpointResponse424 | PostSystemCertificateEndpointResponse500 | PostSystemCertificateEndpointResponse503]
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
    body: PostSystemCertificateEndpointJsonBody | PostSystemCertificateEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemCertificateEndpointResponse400
    | PostSystemCertificateEndpointResponse401
    | PostSystemCertificateEndpointResponse403
    | PostSystemCertificateEndpointResponse404
    | PostSystemCertificateEndpointResponse405
    | PostSystemCertificateEndpointResponse406
    | PostSystemCertificateEndpointResponse409
    | PostSystemCertificateEndpointResponse415
    | PostSystemCertificateEndpointResponse422
    | PostSystemCertificateEndpointResponse424
    | PostSystemCertificateEndpointResponse500
    | PostSystemCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateEndpointJsonBody | Unset):
        body (PostSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateEndpointResponse400 | PostSystemCertificateEndpointResponse401 | PostSystemCertificateEndpointResponse403 | PostSystemCertificateEndpointResponse404 | PostSystemCertificateEndpointResponse405 | PostSystemCertificateEndpointResponse406 | PostSystemCertificateEndpointResponse409 | PostSystemCertificateEndpointResponse415 | PostSystemCertificateEndpointResponse422 | PostSystemCertificateEndpointResponse424 | PostSystemCertificateEndpointResponse500 | PostSystemCertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateEndpointJsonBody | PostSystemCertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemCertificateEndpointResponse400
    | PostSystemCertificateEndpointResponse401
    | PostSystemCertificateEndpointResponse403
    | PostSystemCertificateEndpointResponse404
    | PostSystemCertificateEndpointResponse405
    | PostSystemCertificateEndpointResponse406
    | PostSystemCertificateEndpointResponse409
    | PostSystemCertificateEndpointResponse415
    | PostSystemCertificateEndpointResponse422
    | PostSystemCertificateEndpointResponse424
    | PostSystemCertificateEndpointResponse500
    | PostSystemCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateEndpointJsonBody | Unset):
        body (PostSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCertificateEndpointResponse400 | PostSystemCertificateEndpointResponse401 | PostSystemCertificateEndpointResponse403 | PostSystemCertificateEndpointResponse404 | PostSystemCertificateEndpointResponse405 | PostSystemCertificateEndpointResponse406 | PostSystemCertificateEndpointResponse409 | PostSystemCertificateEndpointResponse415 | PostSystemCertificateEndpointResponse422 | PostSystemCertificateEndpointResponse424 | PostSystemCertificateEndpointResponse500 | PostSystemCertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCertificateEndpointJsonBody | PostSystemCertificateEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemCertificateEndpointResponse400
    | PostSystemCertificateEndpointResponse401
    | PostSystemCertificateEndpointResponse403
    | PostSystemCertificateEndpointResponse404
    | PostSystemCertificateEndpointResponse405
    | PostSystemCertificateEndpointResponse406
    | PostSystemCertificateEndpointResponse409
    | PostSystemCertificateEndpointResponse415
    | PostSystemCertificateEndpointResponse422
    | PostSystemCertificateEndpointResponse424
    | PostSystemCertificateEndpointResponse500
    | PostSystemCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemCertificateEndpointJsonBody | Unset):
        body (PostSystemCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCertificateEndpointResponse400 | PostSystemCertificateEndpointResponse401 | PostSystemCertificateEndpointResponse403 | PostSystemCertificateEndpointResponse404 | PostSystemCertificateEndpointResponse405 | PostSystemCertificateEndpointResponse406 | PostSystemCertificateEndpointResponse409 | PostSystemCertificateEndpointResponse415 | PostSystemCertificateEndpointResponse422 | PostSystemCertificateEndpointResponse424 | PostSystemCertificateEndpointResponse500 | PostSystemCertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
