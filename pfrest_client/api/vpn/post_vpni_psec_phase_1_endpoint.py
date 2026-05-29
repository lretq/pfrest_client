from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpni_psec_phase_1_endpoint_data_body import PostVPNIPsecPhase1EndpointDataBody
from ...models.post_vpni_psec_phase_1_endpoint_json_body import PostVPNIPsecPhase1EndpointJsonBody
from ...models.post_vpni_psec_phase_1_endpoint_response_400 import PostVPNIPsecPhase1EndpointResponse400
from ...models.post_vpni_psec_phase_1_endpoint_response_401 import PostVPNIPsecPhase1EndpointResponse401
from ...models.post_vpni_psec_phase_1_endpoint_response_403 import PostVPNIPsecPhase1EndpointResponse403
from ...models.post_vpni_psec_phase_1_endpoint_response_404 import PostVPNIPsecPhase1EndpointResponse404
from ...models.post_vpni_psec_phase_1_endpoint_response_405 import PostVPNIPsecPhase1EndpointResponse405
from ...models.post_vpni_psec_phase_1_endpoint_response_406 import PostVPNIPsecPhase1EndpointResponse406
from ...models.post_vpni_psec_phase_1_endpoint_response_409 import PostVPNIPsecPhase1EndpointResponse409
from ...models.post_vpni_psec_phase_1_endpoint_response_415 import PostVPNIPsecPhase1EndpointResponse415
from ...models.post_vpni_psec_phase_1_endpoint_response_422 import PostVPNIPsecPhase1EndpointResponse422
from ...models.post_vpni_psec_phase_1_endpoint_response_424 import PostVPNIPsecPhase1EndpointResponse424
from ...models.post_vpni_psec_phase_1_endpoint_response_500 import PostVPNIPsecPhase1EndpointResponse500
from ...models.post_vpni_psec_phase_1_endpoint_response_503 import PostVPNIPsecPhase1EndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNIPsecPhase1EndpointJsonBody | PostVPNIPsecPhase1EndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/ipsec/phase1",
    }

    if isinstance(body, PostVPNIPsecPhase1EndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNIPsecPhase1EndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNIPsecPhase1EndpointResponse400
    | PostVPNIPsecPhase1EndpointResponse401
    | PostVPNIPsecPhase1EndpointResponse403
    | PostVPNIPsecPhase1EndpointResponse404
    | PostVPNIPsecPhase1EndpointResponse405
    | PostVPNIPsecPhase1EndpointResponse406
    | PostVPNIPsecPhase1EndpointResponse409
    | PostVPNIPsecPhase1EndpointResponse415
    | PostVPNIPsecPhase1EndpointResponse422
    | PostVPNIPsecPhase1EndpointResponse424
    | PostVPNIPsecPhase1EndpointResponse500
    | PostVPNIPsecPhase1EndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNIPsecPhase1EndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNIPsecPhase1EndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNIPsecPhase1EndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNIPsecPhase1EndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNIPsecPhase1EndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNIPsecPhase1EndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNIPsecPhase1EndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNIPsecPhase1EndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNIPsecPhase1EndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNIPsecPhase1EndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNIPsecPhase1EndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNIPsecPhase1EndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNIPsecPhase1EndpointResponse400
    | PostVPNIPsecPhase1EndpointResponse401
    | PostVPNIPsecPhase1EndpointResponse403
    | PostVPNIPsecPhase1EndpointResponse404
    | PostVPNIPsecPhase1EndpointResponse405
    | PostVPNIPsecPhase1EndpointResponse406
    | PostVPNIPsecPhase1EndpointResponse409
    | PostVPNIPsecPhase1EndpointResponse415
    | PostVPNIPsecPhase1EndpointResponse422
    | PostVPNIPsecPhase1EndpointResponse424
    | PostVPNIPsecPhase1EndpointResponse500
    | PostVPNIPsecPhase1EndpointResponse503
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
    body: PostVPNIPsecPhase1EndpointJsonBody | PostVPNIPsecPhase1EndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNIPsecPhase1EndpointResponse400
    | PostVPNIPsecPhase1EndpointResponse401
    | PostVPNIPsecPhase1EndpointResponse403
    | PostVPNIPsecPhase1EndpointResponse404
    | PostVPNIPsecPhase1EndpointResponse405
    | PostVPNIPsecPhase1EndpointResponse406
    | PostVPNIPsecPhase1EndpointResponse409
    | PostVPNIPsecPhase1EndpointResponse415
    | PostVPNIPsecPhase1EndpointResponse422
    | PostVPNIPsecPhase1EndpointResponse424
    | PostVPNIPsecPhase1EndpointResponse500
    | PostVPNIPsecPhase1EndpointResponse503
]:
    """<h3>Description:</h3>Creates a new IPsec Phase 1.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase1<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecPhase1EndpointJsonBody | Unset):
        body (PostVPNIPsecPhase1EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNIPsecPhase1EndpointResponse400 | PostVPNIPsecPhase1EndpointResponse401 | PostVPNIPsecPhase1EndpointResponse403 | PostVPNIPsecPhase1EndpointResponse404 | PostVPNIPsecPhase1EndpointResponse405 | PostVPNIPsecPhase1EndpointResponse406 | PostVPNIPsecPhase1EndpointResponse409 | PostVPNIPsecPhase1EndpointResponse415 | PostVPNIPsecPhase1EndpointResponse422 | PostVPNIPsecPhase1EndpointResponse424 | PostVPNIPsecPhase1EndpointResponse500 | PostVPNIPsecPhase1EndpointResponse503]
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
    body: PostVPNIPsecPhase1EndpointJsonBody | PostVPNIPsecPhase1EndpointDataBody | Unset = UNSET,
) -> (
    PostVPNIPsecPhase1EndpointResponse400
    | PostVPNIPsecPhase1EndpointResponse401
    | PostVPNIPsecPhase1EndpointResponse403
    | PostVPNIPsecPhase1EndpointResponse404
    | PostVPNIPsecPhase1EndpointResponse405
    | PostVPNIPsecPhase1EndpointResponse406
    | PostVPNIPsecPhase1EndpointResponse409
    | PostVPNIPsecPhase1EndpointResponse415
    | PostVPNIPsecPhase1EndpointResponse422
    | PostVPNIPsecPhase1EndpointResponse424
    | PostVPNIPsecPhase1EndpointResponse500
    | PostVPNIPsecPhase1EndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new IPsec Phase 1.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase1<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecPhase1EndpointJsonBody | Unset):
        body (PostVPNIPsecPhase1EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNIPsecPhase1EndpointResponse400 | PostVPNIPsecPhase1EndpointResponse401 | PostVPNIPsecPhase1EndpointResponse403 | PostVPNIPsecPhase1EndpointResponse404 | PostVPNIPsecPhase1EndpointResponse405 | PostVPNIPsecPhase1EndpointResponse406 | PostVPNIPsecPhase1EndpointResponse409 | PostVPNIPsecPhase1EndpointResponse415 | PostVPNIPsecPhase1EndpointResponse422 | PostVPNIPsecPhase1EndpointResponse424 | PostVPNIPsecPhase1EndpointResponse500 | PostVPNIPsecPhase1EndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNIPsecPhase1EndpointJsonBody | PostVPNIPsecPhase1EndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNIPsecPhase1EndpointResponse400
    | PostVPNIPsecPhase1EndpointResponse401
    | PostVPNIPsecPhase1EndpointResponse403
    | PostVPNIPsecPhase1EndpointResponse404
    | PostVPNIPsecPhase1EndpointResponse405
    | PostVPNIPsecPhase1EndpointResponse406
    | PostVPNIPsecPhase1EndpointResponse409
    | PostVPNIPsecPhase1EndpointResponse415
    | PostVPNIPsecPhase1EndpointResponse422
    | PostVPNIPsecPhase1EndpointResponse424
    | PostVPNIPsecPhase1EndpointResponse500
    | PostVPNIPsecPhase1EndpointResponse503
]:
    """<h3>Description:</h3>Creates a new IPsec Phase 1.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase1<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecPhase1EndpointJsonBody | Unset):
        body (PostVPNIPsecPhase1EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNIPsecPhase1EndpointResponse400 | PostVPNIPsecPhase1EndpointResponse401 | PostVPNIPsecPhase1EndpointResponse403 | PostVPNIPsecPhase1EndpointResponse404 | PostVPNIPsecPhase1EndpointResponse405 | PostVPNIPsecPhase1EndpointResponse406 | PostVPNIPsecPhase1EndpointResponse409 | PostVPNIPsecPhase1EndpointResponse415 | PostVPNIPsecPhase1EndpointResponse422 | PostVPNIPsecPhase1EndpointResponse424 | PostVPNIPsecPhase1EndpointResponse500 | PostVPNIPsecPhase1EndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNIPsecPhase1EndpointJsonBody | PostVPNIPsecPhase1EndpointDataBody | Unset = UNSET,
) -> (
    PostVPNIPsecPhase1EndpointResponse400
    | PostVPNIPsecPhase1EndpointResponse401
    | PostVPNIPsecPhase1EndpointResponse403
    | PostVPNIPsecPhase1EndpointResponse404
    | PostVPNIPsecPhase1EndpointResponse405
    | PostVPNIPsecPhase1EndpointResponse406
    | PostVPNIPsecPhase1EndpointResponse409
    | PostVPNIPsecPhase1EndpointResponse415
    | PostVPNIPsecPhase1EndpointResponse422
    | PostVPNIPsecPhase1EndpointResponse424
    | PostVPNIPsecPhase1EndpointResponse500
    | PostVPNIPsecPhase1EndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new IPsec Phase 1.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: IPsecPhase1<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNIPsecPhase1EndpointJsonBody | Unset):
        body (PostVPNIPsecPhase1EndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNIPsecPhase1EndpointResponse400 | PostVPNIPsecPhase1EndpointResponse401 | PostVPNIPsecPhase1EndpointResponse403 | PostVPNIPsecPhase1EndpointResponse404 | PostVPNIPsecPhase1EndpointResponse405 | PostVPNIPsecPhase1EndpointResponse406 | PostVPNIPsecPhase1EndpointResponse409 | PostVPNIPsecPhase1EndpointResponse415 | PostVPNIPsecPhase1EndpointResponse422 | PostVPNIPsecPhase1EndpointResponse424 | PostVPNIPsecPhase1EndpointResponse500 | PostVPNIPsecPhase1EndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
