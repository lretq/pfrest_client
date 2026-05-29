from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpni_psec_apply_endpoint_data_body import PostVPNIPsecApplyEndpointDataBody
from ...models.post_vpni_psec_apply_endpoint_json_body import PostVPNIPsecApplyEndpointJsonBody
from ...models.post_vpni_psec_apply_endpoint_response_400 import PostVPNIPsecApplyEndpointResponse400
from ...models.post_vpni_psec_apply_endpoint_response_401 import PostVPNIPsecApplyEndpointResponse401
from ...models.post_vpni_psec_apply_endpoint_response_403 import PostVPNIPsecApplyEndpointResponse403
from ...models.post_vpni_psec_apply_endpoint_response_404 import PostVPNIPsecApplyEndpointResponse404
from ...models.post_vpni_psec_apply_endpoint_response_405 import PostVPNIPsecApplyEndpointResponse405
from ...models.post_vpni_psec_apply_endpoint_response_406 import PostVPNIPsecApplyEndpointResponse406
from ...models.post_vpni_psec_apply_endpoint_response_409 import PostVPNIPsecApplyEndpointResponse409
from ...models.post_vpni_psec_apply_endpoint_response_415 import PostVPNIPsecApplyEndpointResponse415
from ...models.post_vpni_psec_apply_endpoint_response_422 import PostVPNIPsecApplyEndpointResponse422
from ...models.post_vpni_psec_apply_endpoint_response_424 import PostVPNIPsecApplyEndpointResponse424
from ...models.post_vpni_psec_apply_endpoint_response_500 import PostVPNIPsecApplyEndpointResponse500
from ...models.post_vpni_psec_apply_endpoint_response_503 import PostVPNIPsecApplyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNIPsecApplyEndpointJsonBody | PostVPNIPsecApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/ipsec/apply",
    }

    if isinstance(body, PostVPNIPsecApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNIPsecApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNIPsecApplyEndpointResponse400
    | PostVPNIPsecApplyEndpointResponse401
    | PostVPNIPsecApplyEndpointResponse403
    | PostVPNIPsecApplyEndpointResponse404
    | PostVPNIPsecApplyEndpointResponse405
    | PostVPNIPsecApplyEndpointResponse406
    | PostVPNIPsecApplyEndpointResponse409
    | PostVPNIPsecApplyEndpointResponse415
    | PostVPNIPsecApplyEndpointResponse422
    | PostVPNIPsecApplyEndpointResponse424
    | PostVPNIPsecApplyEndpointResponse500
    | PostVPNIPsecApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNIPsecApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNIPsecApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNIPsecApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNIPsecApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNIPsecApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNIPsecApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNIPsecApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNIPsecApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNIPsecApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNIPsecApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNIPsecApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNIPsecApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNIPsecApplyEndpointResponse400
    | PostVPNIPsecApplyEndpointResponse401
    | PostVPNIPsecApplyEndpointResponse403
    | PostVPNIPsecApplyEndpointResponse404
    | PostVPNIPsecApplyEndpointResponse405
    | PostVPNIPsecApplyEndpointResponse406
    | PostVPNIPsecApplyEndpointResponse409
    | PostVPNIPsecApplyEndpointResponse415
    | PostVPNIPsecApplyEndpointResponse422
    | PostVPNIPsecApplyEndpointResponse424
    | PostVPNIPsecApplyEndpointResponse500
    | PostVPNIPsecApplyEndpointResponse503
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
    body: PostVPNIPsecApplyEndpointJsonBody | PostVPNIPsecApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNIPsecApplyEndpointResponse400
    | PostVPNIPsecApplyEndpointResponse401
    | PostVPNIPsecApplyEndpointResponse403
    | PostVPNIPsecApplyEndpointResponse404
    | PostVPNIPsecApplyEndpointResponse405
    | PostVPNIPsecApplyEndpointResponse406
    | PostVPNIPsecApplyEndpointResponse409
    | PostVPNIPsecApplyEndpointResponse415
    | PostVPNIPsecApplyEndpointResponse422
    | PostVPNIPsecApplyEndpointResponse424
    | PostVPNIPsecApplyEndpointResponse500
    | PostVPNIPsecApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending IPsec changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecApplyEndpointJsonBody | Unset):
        body (PostVPNIPsecApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNIPsecApplyEndpointResponse400 | PostVPNIPsecApplyEndpointResponse401 | PostVPNIPsecApplyEndpointResponse403 | PostVPNIPsecApplyEndpointResponse404 | PostVPNIPsecApplyEndpointResponse405 | PostVPNIPsecApplyEndpointResponse406 | PostVPNIPsecApplyEndpointResponse409 | PostVPNIPsecApplyEndpointResponse415 | PostVPNIPsecApplyEndpointResponse422 | PostVPNIPsecApplyEndpointResponse424 | PostVPNIPsecApplyEndpointResponse500 | PostVPNIPsecApplyEndpointResponse503]
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
    body: PostVPNIPsecApplyEndpointJsonBody | PostVPNIPsecApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNIPsecApplyEndpointResponse400
    | PostVPNIPsecApplyEndpointResponse401
    | PostVPNIPsecApplyEndpointResponse403
    | PostVPNIPsecApplyEndpointResponse404
    | PostVPNIPsecApplyEndpointResponse405
    | PostVPNIPsecApplyEndpointResponse406
    | PostVPNIPsecApplyEndpointResponse409
    | PostVPNIPsecApplyEndpointResponse415
    | PostVPNIPsecApplyEndpointResponse422
    | PostVPNIPsecApplyEndpointResponse424
    | PostVPNIPsecApplyEndpointResponse500
    | PostVPNIPsecApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending IPsec changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecApplyEndpointJsonBody | Unset):
        body (PostVPNIPsecApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNIPsecApplyEndpointResponse400 | PostVPNIPsecApplyEndpointResponse401 | PostVPNIPsecApplyEndpointResponse403 | PostVPNIPsecApplyEndpointResponse404 | PostVPNIPsecApplyEndpointResponse405 | PostVPNIPsecApplyEndpointResponse406 | PostVPNIPsecApplyEndpointResponse409 | PostVPNIPsecApplyEndpointResponse415 | PostVPNIPsecApplyEndpointResponse422 | PostVPNIPsecApplyEndpointResponse424 | PostVPNIPsecApplyEndpointResponse500 | PostVPNIPsecApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNIPsecApplyEndpointJsonBody | PostVPNIPsecApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNIPsecApplyEndpointResponse400
    | PostVPNIPsecApplyEndpointResponse401
    | PostVPNIPsecApplyEndpointResponse403
    | PostVPNIPsecApplyEndpointResponse404
    | PostVPNIPsecApplyEndpointResponse405
    | PostVPNIPsecApplyEndpointResponse406
    | PostVPNIPsecApplyEndpointResponse409
    | PostVPNIPsecApplyEndpointResponse415
    | PostVPNIPsecApplyEndpointResponse422
    | PostVPNIPsecApplyEndpointResponse424
    | PostVPNIPsecApplyEndpointResponse500
    | PostVPNIPsecApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending IPsec changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecApplyEndpointJsonBody | Unset):
        body (PostVPNIPsecApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNIPsecApplyEndpointResponse400 | PostVPNIPsecApplyEndpointResponse401 | PostVPNIPsecApplyEndpointResponse403 | PostVPNIPsecApplyEndpointResponse404 | PostVPNIPsecApplyEndpointResponse405 | PostVPNIPsecApplyEndpointResponse406 | PostVPNIPsecApplyEndpointResponse409 | PostVPNIPsecApplyEndpointResponse415 | PostVPNIPsecApplyEndpointResponse422 | PostVPNIPsecApplyEndpointResponse424 | PostVPNIPsecApplyEndpointResponse500 | PostVPNIPsecApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNIPsecApplyEndpointJsonBody | PostVPNIPsecApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNIPsecApplyEndpointResponse400
    | PostVPNIPsecApplyEndpointResponse401
    | PostVPNIPsecApplyEndpointResponse403
    | PostVPNIPsecApplyEndpointResponse404
    | PostVPNIPsecApplyEndpointResponse405
    | PostVPNIPsecApplyEndpointResponse406
    | PostVPNIPsecApplyEndpointResponse409
    | PostVPNIPsecApplyEndpointResponse415
    | PostVPNIPsecApplyEndpointResponse422
    | PostVPNIPsecApplyEndpointResponse424
    | PostVPNIPsecApplyEndpointResponse500
    | PostVPNIPsecApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending IPsec changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-apply-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecApplyEndpointJsonBody | Unset):
        body (PostVPNIPsecApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNIPsecApplyEndpointResponse400 | PostVPNIPsecApplyEndpointResponse401 | PostVPNIPsecApplyEndpointResponse403 | PostVPNIPsecApplyEndpointResponse404 | PostVPNIPsecApplyEndpointResponse405 | PostVPNIPsecApplyEndpointResponse406 | PostVPNIPsecApplyEndpointResponse409 | PostVPNIPsecApplyEndpointResponse415 | PostVPNIPsecApplyEndpointResponse422 | PostVPNIPsecApplyEndpointResponse424 | PostVPNIPsecApplyEndpointResponse500 | PostVPNIPsecApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
