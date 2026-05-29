from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_frontend_address_endpoint_data_body import (
    PostServicesHAProxyFrontendAddressEndpointDataBody,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_json_body import (
    PostServicesHAProxyFrontendAddressEndpointJsonBody,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_400 import (
    PostServicesHAProxyFrontendAddressEndpointResponse400,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_401 import (
    PostServicesHAProxyFrontendAddressEndpointResponse401,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_403 import (
    PostServicesHAProxyFrontendAddressEndpointResponse403,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_404 import (
    PostServicesHAProxyFrontendAddressEndpointResponse404,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_405 import (
    PostServicesHAProxyFrontendAddressEndpointResponse405,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_406 import (
    PostServicesHAProxyFrontendAddressEndpointResponse406,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_409 import (
    PostServicesHAProxyFrontendAddressEndpointResponse409,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_415 import (
    PostServicesHAProxyFrontendAddressEndpointResponse415,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_422 import (
    PostServicesHAProxyFrontendAddressEndpointResponse422,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_424 import (
    PostServicesHAProxyFrontendAddressEndpointResponse424,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_500 import (
    PostServicesHAProxyFrontendAddressEndpointResponse500,
)
from ...models.post_services_ha_proxy_frontend_address_endpoint_response_503 import (
    PostServicesHAProxyFrontendAddressEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyFrontendAddressEndpointJsonBody
    | PostServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/frontend/address",
    }

    if isinstance(body, PostServicesHAProxyFrontendAddressEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyFrontendAddressEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyFrontendAddressEndpointResponse400
    | PostServicesHAProxyFrontendAddressEndpointResponse401
    | PostServicesHAProxyFrontendAddressEndpointResponse403
    | PostServicesHAProxyFrontendAddressEndpointResponse404
    | PostServicesHAProxyFrontendAddressEndpointResponse405
    | PostServicesHAProxyFrontendAddressEndpointResponse406
    | PostServicesHAProxyFrontendAddressEndpointResponse409
    | PostServicesHAProxyFrontendAddressEndpointResponse415
    | PostServicesHAProxyFrontendAddressEndpointResponse422
    | PostServicesHAProxyFrontendAddressEndpointResponse424
    | PostServicesHAProxyFrontendAddressEndpointResponse500
    | PostServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyFrontendAddressEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyFrontendAddressEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyFrontendAddressEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyFrontendAddressEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyFrontendAddressEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyFrontendAddressEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyFrontendAddressEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyFrontendAddressEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyFrontendAddressEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyFrontendAddressEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyFrontendAddressEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyFrontendAddressEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyFrontendAddressEndpointResponse400
    | PostServicesHAProxyFrontendAddressEndpointResponse401
    | PostServicesHAProxyFrontendAddressEndpointResponse403
    | PostServicesHAProxyFrontendAddressEndpointResponse404
    | PostServicesHAProxyFrontendAddressEndpointResponse405
    | PostServicesHAProxyFrontendAddressEndpointResponse406
    | PostServicesHAProxyFrontendAddressEndpointResponse409
    | PostServicesHAProxyFrontendAddressEndpointResponse415
    | PostServicesHAProxyFrontendAddressEndpointResponse422
    | PostServicesHAProxyFrontendAddressEndpointResponse424
    | PostServicesHAProxyFrontendAddressEndpointResponse500
    | PostServicesHAProxyFrontendAddressEndpointResponse503
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
    body: PostServicesHAProxyFrontendAddressEndpointJsonBody
    | PostServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendAddressEndpointResponse400
    | PostServicesHAProxyFrontendAddressEndpointResponse401
    | PostServicesHAProxyFrontendAddressEndpointResponse403
    | PostServicesHAProxyFrontendAddressEndpointResponse404
    | PostServicesHAProxyFrontendAddressEndpointResponse405
    | PostServicesHAProxyFrontendAddressEndpointResponse406
    | PostServicesHAProxyFrontendAddressEndpointResponse409
    | PostServicesHAProxyFrontendAddressEndpointResponse415
    | PostServicesHAProxyFrontendAddressEndpointResponse422
    | PostServicesHAProxyFrontendAddressEndpointResponse424
    | PostServicesHAProxyFrontendAddressEndpointResponse500
    | PostServicesHAProxyFrontendAddressEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendAddressEndpointResponse400 | PostServicesHAProxyFrontendAddressEndpointResponse401 | PostServicesHAProxyFrontendAddressEndpointResponse403 | PostServicesHAProxyFrontendAddressEndpointResponse404 | PostServicesHAProxyFrontendAddressEndpointResponse405 | PostServicesHAProxyFrontendAddressEndpointResponse406 | PostServicesHAProxyFrontendAddressEndpointResponse409 | PostServicesHAProxyFrontendAddressEndpointResponse415 | PostServicesHAProxyFrontendAddressEndpointResponse422 | PostServicesHAProxyFrontendAddressEndpointResponse424 | PostServicesHAProxyFrontendAddressEndpointResponse500 | PostServicesHAProxyFrontendAddressEndpointResponse503]
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
    body: PostServicesHAProxyFrontendAddressEndpointJsonBody
    | PostServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendAddressEndpointResponse400
    | PostServicesHAProxyFrontendAddressEndpointResponse401
    | PostServicesHAProxyFrontendAddressEndpointResponse403
    | PostServicesHAProxyFrontendAddressEndpointResponse404
    | PostServicesHAProxyFrontendAddressEndpointResponse405
    | PostServicesHAProxyFrontendAddressEndpointResponse406
    | PostServicesHAProxyFrontendAddressEndpointResponse409
    | PostServicesHAProxyFrontendAddressEndpointResponse415
    | PostServicesHAProxyFrontendAddressEndpointResponse422
    | PostServicesHAProxyFrontendAddressEndpointResponse424
    | PostServicesHAProxyFrontendAddressEndpointResponse500
    | PostServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendAddressEndpointResponse400 | PostServicesHAProxyFrontendAddressEndpointResponse401 | PostServicesHAProxyFrontendAddressEndpointResponse403 | PostServicesHAProxyFrontendAddressEndpointResponse404 | PostServicesHAProxyFrontendAddressEndpointResponse405 | PostServicesHAProxyFrontendAddressEndpointResponse406 | PostServicesHAProxyFrontendAddressEndpointResponse409 | PostServicesHAProxyFrontendAddressEndpointResponse415 | PostServicesHAProxyFrontendAddressEndpointResponse422 | PostServicesHAProxyFrontendAddressEndpointResponse424 | PostServicesHAProxyFrontendAddressEndpointResponse500 | PostServicesHAProxyFrontendAddressEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendAddressEndpointJsonBody
    | PostServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendAddressEndpointResponse400
    | PostServicesHAProxyFrontendAddressEndpointResponse401
    | PostServicesHAProxyFrontendAddressEndpointResponse403
    | PostServicesHAProxyFrontendAddressEndpointResponse404
    | PostServicesHAProxyFrontendAddressEndpointResponse405
    | PostServicesHAProxyFrontendAddressEndpointResponse406
    | PostServicesHAProxyFrontendAddressEndpointResponse409
    | PostServicesHAProxyFrontendAddressEndpointResponse415
    | PostServicesHAProxyFrontendAddressEndpointResponse422
    | PostServicesHAProxyFrontendAddressEndpointResponse424
    | PostServicesHAProxyFrontendAddressEndpointResponse500
    | PostServicesHAProxyFrontendAddressEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendAddressEndpointResponse400 | PostServicesHAProxyFrontendAddressEndpointResponse401 | PostServicesHAProxyFrontendAddressEndpointResponse403 | PostServicesHAProxyFrontendAddressEndpointResponse404 | PostServicesHAProxyFrontendAddressEndpointResponse405 | PostServicesHAProxyFrontendAddressEndpointResponse406 | PostServicesHAProxyFrontendAddressEndpointResponse409 | PostServicesHAProxyFrontendAddressEndpointResponse415 | PostServicesHAProxyFrontendAddressEndpointResponse422 | PostServicesHAProxyFrontendAddressEndpointResponse424 | PostServicesHAProxyFrontendAddressEndpointResponse500 | PostServicesHAProxyFrontendAddressEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendAddressEndpointJsonBody
    | PostServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendAddressEndpointResponse400
    | PostServicesHAProxyFrontendAddressEndpointResponse401
    | PostServicesHAProxyFrontendAddressEndpointResponse403
    | PostServicesHAProxyFrontendAddressEndpointResponse404
    | PostServicesHAProxyFrontendAddressEndpointResponse405
    | PostServicesHAProxyFrontendAddressEndpointResponse406
    | PostServicesHAProxyFrontendAddressEndpointResponse409
    | PostServicesHAProxyFrontendAddressEndpointResponse415
    | PostServicesHAProxyFrontendAddressEndpointResponse422
    | PostServicesHAProxyFrontendAddressEndpointResponse424
    | PostServicesHAProxyFrontendAddressEndpointResponse500
    | PostServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendAddressEndpointResponse400 | PostServicesHAProxyFrontendAddressEndpointResponse401 | PostServicesHAProxyFrontendAddressEndpointResponse403 | PostServicesHAProxyFrontendAddressEndpointResponse404 | PostServicesHAProxyFrontendAddressEndpointResponse405 | PostServicesHAProxyFrontendAddressEndpointResponse406 | PostServicesHAProxyFrontendAddressEndpointResponse409 | PostServicesHAProxyFrontendAddressEndpointResponse415 | PostServicesHAProxyFrontendAddressEndpointResponse422 | PostServicesHAProxyFrontendAddressEndpointResponse424 | PostServicesHAProxyFrontendAddressEndpointResponse500 | PostServicesHAProxyFrontendAddressEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
