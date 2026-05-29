from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dns_forwarder_host_override_endpoint_data_body import (
    PostServicesDNSForwarderHostOverrideEndpointDataBody,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_json_body import (
    PostServicesDNSForwarderHostOverrideEndpointJsonBody,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_400 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse400,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_401 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse401,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_403 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse403,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_404 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse404,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_405 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse405,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_406 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse406,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_409 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse409,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_415 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse415,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_422 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse422,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_424 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse424,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_500 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse500,
)
from ...models.post_services_dns_forwarder_host_override_endpoint_response_503 import (
    PostServicesDNSForwarderHostOverrideEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDNSForwarderHostOverrideEndpointJsonBody
    | PostServicesDNSForwarderHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dns_forwarder/host_override",
    }

    if isinstance(body, PostServicesDNSForwarderHostOverrideEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDNSForwarderHostOverrideEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDNSForwarderHostOverrideEndpointResponse400
    | PostServicesDNSForwarderHostOverrideEndpointResponse401
    | PostServicesDNSForwarderHostOverrideEndpointResponse403
    | PostServicesDNSForwarderHostOverrideEndpointResponse404
    | PostServicesDNSForwarderHostOverrideEndpointResponse405
    | PostServicesDNSForwarderHostOverrideEndpointResponse406
    | PostServicesDNSForwarderHostOverrideEndpointResponse409
    | PostServicesDNSForwarderHostOverrideEndpointResponse415
    | PostServicesDNSForwarderHostOverrideEndpointResponse422
    | PostServicesDNSForwarderHostOverrideEndpointResponse424
    | PostServicesDNSForwarderHostOverrideEndpointResponse500
    | PostServicesDNSForwarderHostOverrideEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDNSForwarderHostOverrideEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDNSForwarderHostOverrideEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDNSForwarderHostOverrideEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDNSForwarderHostOverrideEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDNSForwarderHostOverrideEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDNSForwarderHostOverrideEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDNSForwarderHostOverrideEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDNSForwarderHostOverrideEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDNSForwarderHostOverrideEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDNSForwarderHostOverrideEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDNSForwarderHostOverrideEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDNSForwarderHostOverrideEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDNSForwarderHostOverrideEndpointResponse400
    | PostServicesDNSForwarderHostOverrideEndpointResponse401
    | PostServicesDNSForwarderHostOverrideEndpointResponse403
    | PostServicesDNSForwarderHostOverrideEndpointResponse404
    | PostServicesDNSForwarderHostOverrideEndpointResponse405
    | PostServicesDNSForwarderHostOverrideEndpointResponse406
    | PostServicesDNSForwarderHostOverrideEndpointResponse409
    | PostServicesDNSForwarderHostOverrideEndpointResponse415
    | PostServicesDNSForwarderHostOverrideEndpointResponse422
    | PostServicesDNSForwarderHostOverrideEndpointResponse424
    | PostServicesDNSForwarderHostOverrideEndpointResponse500
    | PostServicesDNSForwarderHostOverrideEndpointResponse503
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
    body: PostServicesDNSForwarderHostOverrideEndpointJsonBody
    | PostServicesDNSForwarderHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSForwarderHostOverrideEndpointResponse400
    | PostServicesDNSForwarderHostOverrideEndpointResponse401
    | PostServicesDNSForwarderHostOverrideEndpointResponse403
    | PostServicesDNSForwarderHostOverrideEndpointResponse404
    | PostServicesDNSForwarderHostOverrideEndpointResponse405
    | PostServicesDNSForwarderHostOverrideEndpointResponse406
    | PostServicesDNSForwarderHostOverrideEndpointResponse409
    | PostServicesDNSForwarderHostOverrideEndpointResponse415
    | PostServicesDNSForwarderHostOverrideEndpointResponse422
    | PostServicesDNSForwarderHostOverrideEndpointResponse424
    | PostServicesDNSForwarderHostOverrideEndpointResponse500
    | PostServicesDNSForwarderHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSForwarderHostOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSForwarderHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSForwarderHostOverrideEndpointResponse400 | PostServicesDNSForwarderHostOverrideEndpointResponse401 | PostServicesDNSForwarderHostOverrideEndpointResponse403 | PostServicesDNSForwarderHostOverrideEndpointResponse404 | PostServicesDNSForwarderHostOverrideEndpointResponse405 | PostServicesDNSForwarderHostOverrideEndpointResponse406 | PostServicesDNSForwarderHostOverrideEndpointResponse409 | PostServicesDNSForwarderHostOverrideEndpointResponse415 | PostServicesDNSForwarderHostOverrideEndpointResponse422 | PostServicesDNSForwarderHostOverrideEndpointResponse424 | PostServicesDNSForwarderHostOverrideEndpointResponse500 | PostServicesDNSForwarderHostOverrideEndpointResponse503]
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
    body: PostServicesDNSForwarderHostOverrideEndpointJsonBody
    | PostServicesDNSForwarderHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSForwarderHostOverrideEndpointResponse400
    | PostServicesDNSForwarderHostOverrideEndpointResponse401
    | PostServicesDNSForwarderHostOverrideEndpointResponse403
    | PostServicesDNSForwarderHostOverrideEndpointResponse404
    | PostServicesDNSForwarderHostOverrideEndpointResponse405
    | PostServicesDNSForwarderHostOverrideEndpointResponse406
    | PostServicesDNSForwarderHostOverrideEndpointResponse409
    | PostServicesDNSForwarderHostOverrideEndpointResponse415
    | PostServicesDNSForwarderHostOverrideEndpointResponse422
    | PostServicesDNSForwarderHostOverrideEndpointResponse424
    | PostServicesDNSForwarderHostOverrideEndpointResponse500
    | PostServicesDNSForwarderHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSForwarderHostOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSForwarderHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSForwarderHostOverrideEndpointResponse400 | PostServicesDNSForwarderHostOverrideEndpointResponse401 | PostServicesDNSForwarderHostOverrideEndpointResponse403 | PostServicesDNSForwarderHostOverrideEndpointResponse404 | PostServicesDNSForwarderHostOverrideEndpointResponse405 | PostServicesDNSForwarderHostOverrideEndpointResponse406 | PostServicesDNSForwarderHostOverrideEndpointResponse409 | PostServicesDNSForwarderHostOverrideEndpointResponse415 | PostServicesDNSForwarderHostOverrideEndpointResponse422 | PostServicesDNSForwarderHostOverrideEndpointResponse424 | PostServicesDNSForwarderHostOverrideEndpointResponse500 | PostServicesDNSForwarderHostOverrideEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSForwarderHostOverrideEndpointJsonBody
    | PostServicesDNSForwarderHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDNSForwarderHostOverrideEndpointResponse400
    | PostServicesDNSForwarderHostOverrideEndpointResponse401
    | PostServicesDNSForwarderHostOverrideEndpointResponse403
    | PostServicesDNSForwarderHostOverrideEndpointResponse404
    | PostServicesDNSForwarderHostOverrideEndpointResponse405
    | PostServicesDNSForwarderHostOverrideEndpointResponse406
    | PostServicesDNSForwarderHostOverrideEndpointResponse409
    | PostServicesDNSForwarderHostOverrideEndpointResponse415
    | PostServicesDNSForwarderHostOverrideEndpointResponse422
    | PostServicesDNSForwarderHostOverrideEndpointResponse424
    | PostServicesDNSForwarderHostOverrideEndpointResponse500
    | PostServicesDNSForwarderHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSForwarderHostOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSForwarderHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDNSForwarderHostOverrideEndpointResponse400 | PostServicesDNSForwarderHostOverrideEndpointResponse401 | PostServicesDNSForwarderHostOverrideEndpointResponse403 | PostServicesDNSForwarderHostOverrideEndpointResponse404 | PostServicesDNSForwarderHostOverrideEndpointResponse405 | PostServicesDNSForwarderHostOverrideEndpointResponse406 | PostServicesDNSForwarderHostOverrideEndpointResponse409 | PostServicesDNSForwarderHostOverrideEndpointResponse415 | PostServicesDNSForwarderHostOverrideEndpointResponse422 | PostServicesDNSForwarderHostOverrideEndpointResponse424 | PostServicesDNSForwarderHostOverrideEndpointResponse500 | PostServicesDNSForwarderHostOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDNSForwarderHostOverrideEndpointJsonBody
    | PostServicesDNSForwarderHostOverrideEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDNSForwarderHostOverrideEndpointResponse400
    | PostServicesDNSForwarderHostOverrideEndpointResponse401
    | PostServicesDNSForwarderHostOverrideEndpointResponse403
    | PostServicesDNSForwarderHostOverrideEndpointResponse404
    | PostServicesDNSForwarderHostOverrideEndpointResponse405
    | PostServicesDNSForwarderHostOverrideEndpointResponse406
    | PostServicesDNSForwarderHostOverrideEndpointResponse409
    | PostServicesDNSForwarderHostOverrideEndpointResponse415
    | PostServicesDNSForwarderHostOverrideEndpointResponse422
    | PostServicesDNSForwarderHostOverrideEndpointResponse424
    | PostServicesDNSForwarderHostOverrideEndpointResponse500
    | PostServicesDNSForwarderHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDNSForwarderHostOverrideEndpointJsonBody | Unset):
        body (PostServicesDNSForwarderHostOverrideEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDNSForwarderHostOverrideEndpointResponse400 | PostServicesDNSForwarderHostOverrideEndpointResponse401 | PostServicesDNSForwarderHostOverrideEndpointResponse403 | PostServicesDNSForwarderHostOverrideEndpointResponse404 | PostServicesDNSForwarderHostOverrideEndpointResponse405 | PostServicesDNSForwarderHostOverrideEndpointResponse406 | PostServicesDNSForwarderHostOverrideEndpointResponse409 | PostServicesDNSForwarderHostOverrideEndpointResponse415 | PostServicesDNSForwarderHostOverrideEndpointResponse422 | PostServicesDNSForwarderHostOverrideEndpointResponse424 | PostServicesDNSForwarderHostOverrideEndpointResponse500 | PostServicesDNSForwarderHostOverrideEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
