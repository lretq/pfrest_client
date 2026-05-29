from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_apply_endpoint_data_body import PostServicesHAProxyApplyEndpointDataBody
from ...models.post_services_ha_proxy_apply_endpoint_json_body import PostServicesHAProxyApplyEndpointJsonBody
from ...models.post_services_ha_proxy_apply_endpoint_response_400 import PostServicesHAProxyApplyEndpointResponse400
from ...models.post_services_ha_proxy_apply_endpoint_response_401 import PostServicesHAProxyApplyEndpointResponse401
from ...models.post_services_ha_proxy_apply_endpoint_response_403 import PostServicesHAProxyApplyEndpointResponse403
from ...models.post_services_ha_proxy_apply_endpoint_response_404 import PostServicesHAProxyApplyEndpointResponse404
from ...models.post_services_ha_proxy_apply_endpoint_response_405 import PostServicesHAProxyApplyEndpointResponse405
from ...models.post_services_ha_proxy_apply_endpoint_response_406 import PostServicesHAProxyApplyEndpointResponse406
from ...models.post_services_ha_proxy_apply_endpoint_response_409 import PostServicesHAProxyApplyEndpointResponse409
from ...models.post_services_ha_proxy_apply_endpoint_response_415 import PostServicesHAProxyApplyEndpointResponse415
from ...models.post_services_ha_proxy_apply_endpoint_response_422 import PostServicesHAProxyApplyEndpointResponse422
from ...models.post_services_ha_proxy_apply_endpoint_response_424 import PostServicesHAProxyApplyEndpointResponse424
from ...models.post_services_ha_proxy_apply_endpoint_response_500 import PostServicesHAProxyApplyEndpointResponse500
from ...models.post_services_ha_proxy_apply_endpoint_response_503 import PostServicesHAProxyApplyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyApplyEndpointJsonBody | PostServicesHAProxyApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/apply",
    }

    if isinstance(body, PostServicesHAProxyApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyApplyEndpointResponse400
    | PostServicesHAProxyApplyEndpointResponse401
    | PostServicesHAProxyApplyEndpointResponse403
    | PostServicesHAProxyApplyEndpointResponse404
    | PostServicesHAProxyApplyEndpointResponse405
    | PostServicesHAProxyApplyEndpointResponse406
    | PostServicesHAProxyApplyEndpointResponse409
    | PostServicesHAProxyApplyEndpointResponse415
    | PostServicesHAProxyApplyEndpointResponse422
    | PostServicesHAProxyApplyEndpointResponse424
    | PostServicesHAProxyApplyEndpointResponse500
    | PostServicesHAProxyApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyApplyEndpointResponse400
    | PostServicesHAProxyApplyEndpointResponse401
    | PostServicesHAProxyApplyEndpointResponse403
    | PostServicesHAProxyApplyEndpointResponse404
    | PostServicesHAProxyApplyEndpointResponse405
    | PostServicesHAProxyApplyEndpointResponse406
    | PostServicesHAProxyApplyEndpointResponse409
    | PostServicesHAProxyApplyEndpointResponse415
    | PostServicesHAProxyApplyEndpointResponse422
    | PostServicesHAProxyApplyEndpointResponse424
    | PostServicesHAProxyApplyEndpointResponse500
    | PostServicesHAProxyApplyEndpointResponse503
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
    body: PostServicesHAProxyApplyEndpointJsonBody | PostServicesHAProxyApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyApplyEndpointResponse400
    | PostServicesHAProxyApplyEndpointResponse401
    | PostServicesHAProxyApplyEndpointResponse403
    | PostServicesHAProxyApplyEndpointResponse404
    | PostServicesHAProxyApplyEndpointResponse405
    | PostServicesHAProxyApplyEndpointResponse406
    | PostServicesHAProxyApplyEndpointResponse409
    | PostServicesHAProxyApplyEndpointResponse415
    | PostServicesHAProxyApplyEndpointResponse422
    | PostServicesHAProxyApplyEndpointResponse424
    | PostServicesHAProxyApplyEndpointResponse500
    | PostServicesHAProxyApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending HAProxy changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesHAProxyApplyEndpointJsonBody | Unset):
        body (PostServicesHAProxyApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyApplyEndpointResponse400 | PostServicesHAProxyApplyEndpointResponse401 | PostServicesHAProxyApplyEndpointResponse403 | PostServicesHAProxyApplyEndpointResponse404 | PostServicesHAProxyApplyEndpointResponse405 | PostServicesHAProxyApplyEndpointResponse406 | PostServicesHAProxyApplyEndpointResponse409 | PostServicesHAProxyApplyEndpointResponse415 | PostServicesHAProxyApplyEndpointResponse422 | PostServicesHAProxyApplyEndpointResponse424 | PostServicesHAProxyApplyEndpointResponse500 | PostServicesHAProxyApplyEndpointResponse503]
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
    body: PostServicesHAProxyApplyEndpointJsonBody | PostServicesHAProxyApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyApplyEndpointResponse400
    | PostServicesHAProxyApplyEndpointResponse401
    | PostServicesHAProxyApplyEndpointResponse403
    | PostServicesHAProxyApplyEndpointResponse404
    | PostServicesHAProxyApplyEndpointResponse405
    | PostServicesHAProxyApplyEndpointResponse406
    | PostServicesHAProxyApplyEndpointResponse409
    | PostServicesHAProxyApplyEndpointResponse415
    | PostServicesHAProxyApplyEndpointResponse422
    | PostServicesHAProxyApplyEndpointResponse424
    | PostServicesHAProxyApplyEndpointResponse500
    | PostServicesHAProxyApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending HAProxy changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesHAProxyApplyEndpointJsonBody | Unset):
        body (PostServicesHAProxyApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyApplyEndpointResponse400 | PostServicesHAProxyApplyEndpointResponse401 | PostServicesHAProxyApplyEndpointResponse403 | PostServicesHAProxyApplyEndpointResponse404 | PostServicesHAProxyApplyEndpointResponse405 | PostServicesHAProxyApplyEndpointResponse406 | PostServicesHAProxyApplyEndpointResponse409 | PostServicesHAProxyApplyEndpointResponse415 | PostServicesHAProxyApplyEndpointResponse422 | PostServicesHAProxyApplyEndpointResponse424 | PostServicesHAProxyApplyEndpointResponse500 | PostServicesHAProxyApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyApplyEndpointJsonBody | PostServicesHAProxyApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyApplyEndpointResponse400
    | PostServicesHAProxyApplyEndpointResponse401
    | PostServicesHAProxyApplyEndpointResponse403
    | PostServicesHAProxyApplyEndpointResponse404
    | PostServicesHAProxyApplyEndpointResponse405
    | PostServicesHAProxyApplyEndpointResponse406
    | PostServicesHAProxyApplyEndpointResponse409
    | PostServicesHAProxyApplyEndpointResponse415
    | PostServicesHAProxyApplyEndpointResponse422
    | PostServicesHAProxyApplyEndpointResponse424
    | PostServicesHAProxyApplyEndpointResponse500
    | PostServicesHAProxyApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending HAProxy changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesHAProxyApplyEndpointJsonBody | Unset):
        body (PostServicesHAProxyApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyApplyEndpointResponse400 | PostServicesHAProxyApplyEndpointResponse401 | PostServicesHAProxyApplyEndpointResponse403 | PostServicesHAProxyApplyEndpointResponse404 | PostServicesHAProxyApplyEndpointResponse405 | PostServicesHAProxyApplyEndpointResponse406 | PostServicesHAProxyApplyEndpointResponse409 | PostServicesHAProxyApplyEndpointResponse415 | PostServicesHAProxyApplyEndpointResponse422 | PostServicesHAProxyApplyEndpointResponse424 | PostServicesHAProxyApplyEndpointResponse500 | PostServicesHAProxyApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyApplyEndpointJsonBody | PostServicesHAProxyApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyApplyEndpointResponse400
    | PostServicesHAProxyApplyEndpointResponse401
    | PostServicesHAProxyApplyEndpointResponse403
    | PostServicesHAProxyApplyEndpointResponse404
    | PostServicesHAProxyApplyEndpointResponse405
    | PostServicesHAProxyApplyEndpointResponse406
    | PostServicesHAProxyApplyEndpointResponse409
    | PostServicesHAProxyApplyEndpointResponse415
    | PostServicesHAProxyApplyEndpointResponse422
    | PostServicesHAProxyApplyEndpointResponse424
    | PostServicesHAProxyApplyEndpointResponse500
    | PostServicesHAProxyApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending HAProxy changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesHAProxyApplyEndpointJsonBody | Unset):
        body (PostServicesHAProxyApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyApplyEndpointResponse400 | PostServicesHAProxyApplyEndpointResponse401 | PostServicesHAProxyApplyEndpointResponse403 | PostServicesHAProxyApplyEndpointResponse404 | PostServicesHAProxyApplyEndpointResponse405 | PostServicesHAProxyApplyEndpointResponse406 | PostServicesHAProxyApplyEndpointResponse409 | PostServicesHAProxyApplyEndpointResponse415 | PostServicesHAProxyApplyEndpointResponse422 | PostServicesHAProxyApplyEndpointResponse424 | PostServicesHAProxyApplyEndpointResponse500 | PostServicesHAProxyApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
