from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_crl_endpoint_data_body import PostSystemCRLEndpointDataBody
from ...models.post_system_crl_endpoint_json_body import PostSystemCRLEndpointJsonBody
from ...models.post_system_crl_endpoint_response_400 import PostSystemCRLEndpointResponse400
from ...models.post_system_crl_endpoint_response_401 import PostSystemCRLEndpointResponse401
from ...models.post_system_crl_endpoint_response_403 import PostSystemCRLEndpointResponse403
from ...models.post_system_crl_endpoint_response_404 import PostSystemCRLEndpointResponse404
from ...models.post_system_crl_endpoint_response_405 import PostSystemCRLEndpointResponse405
from ...models.post_system_crl_endpoint_response_406 import PostSystemCRLEndpointResponse406
from ...models.post_system_crl_endpoint_response_409 import PostSystemCRLEndpointResponse409
from ...models.post_system_crl_endpoint_response_415 import PostSystemCRLEndpointResponse415
from ...models.post_system_crl_endpoint_response_422 import PostSystemCRLEndpointResponse422
from ...models.post_system_crl_endpoint_response_424 import PostSystemCRLEndpointResponse424
from ...models.post_system_crl_endpoint_response_500 import PostSystemCRLEndpointResponse500
from ...models.post_system_crl_endpoint_response_503 import PostSystemCRLEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemCRLEndpointJsonBody | PostSystemCRLEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/crl",
    }

    if isinstance(body, PostSystemCRLEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemCRLEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemCRLEndpointResponse400
    | PostSystemCRLEndpointResponse401
    | PostSystemCRLEndpointResponse403
    | PostSystemCRLEndpointResponse404
    | PostSystemCRLEndpointResponse405
    | PostSystemCRLEndpointResponse406
    | PostSystemCRLEndpointResponse409
    | PostSystemCRLEndpointResponse415
    | PostSystemCRLEndpointResponse422
    | PostSystemCRLEndpointResponse424
    | PostSystemCRLEndpointResponse500
    | PostSystemCRLEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemCRLEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemCRLEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemCRLEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemCRLEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemCRLEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemCRLEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemCRLEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemCRLEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemCRLEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemCRLEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemCRLEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemCRLEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemCRLEndpointResponse400
    | PostSystemCRLEndpointResponse401
    | PostSystemCRLEndpointResponse403
    | PostSystemCRLEndpointResponse404
    | PostSystemCRLEndpointResponse405
    | PostSystemCRLEndpointResponse406
    | PostSystemCRLEndpointResponse409
    | PostSystemCRLEndpointResponse415
    | PostSystemCRLEndpointResponse422
    | PostSystemCRLEndpointResponse424
    | PostSystemCRLEndpointResponse500
    | PostSystemCRLEndpointResponse503
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
    body: PostSystemCRLEndpointJsonBody | PostSystemCRLEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemCRLEndpointResponse400
    | PostSystemCRLEndpointResponse401
    | PostSystemCRLEndpointResponse403
    | PostSystemCRLEndpointResponse404
    | PostSystemCRLEndpointResponse405
    | PostSystemCRLEndpointResponse406
    | PostSystemCRLEndpointResponse409
    | PostSystemCRLEndpointResponse415
    | PostSystemCRLEndpointResponse422
    | PostSystemCRLEndpointResponse424
    | PostSystemCRLEndpointResponse500
    | PostSystemCRLEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCRLEndpointJsonBody | Unset):
        body (PostSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCRLEndpointResponse400 | PostSystemCRLEndpointResponse401 | PostSystemCRLEndpointResponse403 | PostSystemCRLEndpointResponse404 | PostSystemCRLEndpointResponse405 | PostSystemCRLEndpointResponse406 | PostSystemCRLEndpointResponse409 | PostSystemCRLEndpointResponse415 | PostSystemCRLEndpointResponse422 | PostSystemCRLEndpointResponse424 | PostSystemCRLEndpointResponse500 | PostSystemCRLEndpointResponse503]
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
    body: PostSystemCRLEndpointJsonBody | PostSystemCRLEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemCRLEndpointResponse400
    | PostSystemCRLEndpointResponse401
    | PostSystemCRLEndpointResponse403
    | PostSystemCRLEndpointResponse404
    | PostSystemCRLEndpointResponse405
    | PostSystemCRLEndpointResponse406
    | PostSystemCRLEndpointResponse409
    | PostSystemCRLEndpointResponse415
    | PostSystemCRLEndpointResponse422
    | PostSystemCRLEndpointResponse424
    | PostSystemCRLEndpointResponse500
    | PostSystemCRLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCRLEndpointJsonBody | Unset):
        body (PostSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCRLEndpointResponse400 | PostSystemCRLEndpointResponse401 | PostSystemCRLEndpointResponse403 | PostSystemCRLEndpointResponse404 | PostSystemCRLEndpointResponse405 | PostSystemCRLEndpointResponse406 | PostSystemCRLEndpointResponse409 | PostSystemCRLEndpointResponse415 | PostSystemCRLEndpointResponse422 | PostSystemCRLEndpointResponse424 | PostSystemCRLEndpointResponse500 | PostSystemCRLEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCRLEndpointJsonBody | PostSystemCRLEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemCRLEndpointResponse400
    | PostSystemCRLEndpointResponse401
    | PostSystemCRLEndpointResponse403
    | PostSystemCRLEndpointResponse404
    | PostSystemCRLEndpointResponse405
    | PostSystemCRLEndpointResponse406
    | PostSystemCRLEndpointResponse409
    | PostSystemCRLEndpointResponse415
    | PostSystemCRLEndpointResponse422
    | PostSystemCRLEndpointResponse424
    | PostSystemCRLEndpointResponse500
    | PostSystemCRLEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCRLEndpointJsonBody | Unset):
        body (PostSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemCRLEndpointResponse400 | PostSystemCRLEndpointResponse401 | PostSystemCRLEndpointResponse403 | PostSystemCRLEndpointResponse404 | PostSystemCRLEndpointResponse405 | PostSystemCRLEndpointResponse406 | PostSystemCRLEndpointResponse409 | PostSystemCRLEndpointResponse415 | PostSystemCRLEndpointResponse422 | PostSystemCRLEndpointResponse424 | PostSystemCRLEndpointResponse500 | PostSystemCRLEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemCRLEndpointJsonBody | PostSystemCRLEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemCRLEndpointResponse400
    | PostSystemCRLEndpointResponse401
    | PostSystemCRLEndpointResponse403
    | PostSystemCRLEndpointResponse404
    | PostSystemCRLEndpointResponse405
    | PostSystemCRLEndpointResponse406
    | PostSystemCRLEndpointResponse409
    | PostSystemCRLEndpointResponse415
    | PostSystemCRLEndpointResponse422
    | PostSystemCRLEndpointResponse424
    | PostSystemCRLEndpointResponse500
    | PostSystemCRLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostSystemCRLEndpointJsonBody | Unset):
        body (PostSystemCRLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemCRLEndpointResponse400 | PostSystemCRLEndpointResponse401 | PostSystemCRLEndpointResponse403 | PostSystemCRLEndpointResponse404 | PostSystemCRLEndpointResponse405 | PostSystemCRLEndpointResponse406 | PostSystemCRLEndpointResponse409 | PostSystemCRLEndpointResponse415 | PostSystemCRLEndpointResponse422 | PostSystemCRLEndpointResponse424 | PostSystemCRLEndpointResponse500 | PostSystemCRLEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
