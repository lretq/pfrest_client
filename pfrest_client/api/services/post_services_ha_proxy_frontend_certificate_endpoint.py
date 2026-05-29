from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_data_body import (
    PostServicesHAProxyFrontendCertificateEndpointDataBody,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_json_body import (
    PostServicesHAProxyFrontendCertificateEndpointJsonBody,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_400 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse400,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_401 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse401,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_403 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse403,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_404 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse404,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_405 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse405,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_406 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse406,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_409 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse409,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_415 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse415,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_422 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse422,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_424 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse424,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_500 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse500,
)
from ...models.post_services_ha_proxy_frontend_certificate_endpoint_response_503 import (
    PostServicesHAProxyFrontendCertificateEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyFrontendCertificateEndpointJsonBody
    | PostServicesHAProxyFrontendCertificateEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/frontend/certificate",
    }

    if isinstance(body, PostServicesHAProxyFrontendCertificateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyFrontendCertificateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyFrontendCertificateEndpointResponse400
    | PostServicesHAProxyFrontendCertificateEndpointResponse401
    | PostServicesHAProxyFrontendCertificateEndpointResponse403
    | PostServicesHAProxyFrontendCertificateEndpointResponse404
    | PostServicesHAProxyFrontendCertificateEndpointResponse405
    | PostServicesHAProxyFrontendCertificateEndpointResponse406
    | PostServicesHAProxyFrontendCertificateEndpointResponse409
    | PostServicesHAProxyFrontendCertificateEndpointResponse415
    | PostServicesHAProxyFrontendCertificateEndpointResponse422
    | PostServicesHAProxyFrontendCertificateEndpointResponse424
    | PostServicesHAProxyFrontendCertificateEndpointResponse500
    | PostServicesHAProxyFrontendCertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyFrontendCertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyFrontendCertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyFrontendCertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyFrontendCertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyFrontendCertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyFrontendCertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyFrontendCertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyFrontendCertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyFrontendCertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyFrontendCertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyFrontendCertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyFrontendCertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyFrontendCertificateEndpointResponse400
    | PostServicesHAProxyFrontendCertificateEndpointResponse401
    | PostServicesHAProxyFrontendCertificateEndpointResponse403
    | PostServicesHAProxyFrontendCertificateEndpointResponse404
    | PostServicesHAProxyFrontendCertificateEndpointResponse405
    | PostServicesHAProxyFrontendCertificateEndpointResponse406
    | PostServicesHAProxyFrontendCertificateEndpointResponse409
    | PostServicesHAProxyFrontendCertificateEndpointResponse415
    | PostServicesHAProxyFrontendCertificateEndpointResponse422
    | PostServicesHAProxyFrontendCertificateEndpointResponse424
    | PostServicesHAProxyFrontendCertificateEndpointResponse500
    | PostServicesHAProxyFrontendCertificateEndpointResponse503
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
    body: PostServicesHAProxyFrontendCertificateEndpointJsonBody
    | PostServicesHAProxyFrontendCertificateEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendCertificateEndpointResponse400
    | PostServicesHAProxyFrontendCertificateEndpointResponse401
    | PostServicesHAProxyFrontendCertificateEndpointResponse403
    | PostServicesHAProxyFrontendCertificateEndpointResponse404
    | PostServicesHAProxyFrontendCertificateEndpointResponse405
    | PostServicesHAProxyFrontendCertificateEndpointResponse406
    | PostServicesHAProxyFrontendCertificateEndpointResponse409
    | PostServicesHAProxyFrontendCertificateEndpointResponse415
    | PostServicesHAProxyFrontendCertificateEndpointResponse422
    | PostServicesHAProxyFrontendCertificateEndpointResponse424
    | PostServicesHAProxyFrontendCertificateEndpointResponse500
    | PostServicesHAProxyFrontendCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend Certificates.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendCertificate<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-certificate-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendCertificateEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendCertificateEndpointResponse400 | PostServicesHAProxyFrontendCertificateEndpointResponse401 | PostServicesHAProxyFrontendCertificateEndpointResponse403 | PostServicesHAProxyFrontendCertificateEndpointResponse404 | PostServicesHAProxyFrontendCertificateEndpointResponse405 | PostServicesHAProxyFrontendCertificateEndpointResponse406 | PostServicesHAProxyFrontendCertificateEndpointResponse409 | PostServicesHAProxyFrontendCertificateEndpointResponse415 | PostServicesHAProxyFrontendCertificateEndpointResponse422 | PostServicesHAProxyFrontendCertificateEndpointResponse424 | PostServicesHAProxyFrontendCertificateEndpointResponse500 | PostServicesHAProxyFrontendCertificateEndpointResponse503]
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
    body: PostServicesHAProxyFrontendCertificateEndpointJsonBody
    | PostServicesHAProxyFrontendCertificateEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendCertificateEndpointResponse400
    | PostServicesHAProxyFrontendCertificateEndpointResponse401
    | PostServicesHAProxyFrontendCertificateEndpointResponse403
    | PostServicesHAProxyFrontendCertificateEndpointResponse404
    | PostServicesHAProxyFrontendCertificateEndpointResponse405
    | PostServicesHAProxyFrontendCertificateEndpointResponse406
    | PostServicesHAProxyFrontendCertificateEndpointResponse409
    | PostServicesHAProxyFrontendCertificateEndpointResponse415
    | PostServicesHAProxyFrontendCertificateEndpointResponse422
    | PostServicesHAProxyFrontendCertificateEndpointResponse424
    | PostServicesHAProxyFrontendCertificateEndpointResponse500
    | PostServicesHAProxyFrontendCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend Certificates.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendCertificate<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-certificate-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendCertificateEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendCertificateEndpointResponse400 | PostServicesHAProxyFrontendCertificateEndpointResponse401 | PostServicesHAProxyFrontendCertificateEndpointResponse403 | PostServicesHAProxyFrontendCertificateEndpointResponse404 | PostServicesHAProxyFrontendCertificateEndpointResponse405 | PostServicesHAProxyFrontendCertificateEndpointResponse406 | PostServicesHAProxyFrontendCertificateEndpointResponse409 | PostServicesHAProxyFrontendCertificateEndpointResponse415 | PostServicesHAProxyFrontendCertificateEndpointResponse422 | PostServicesHAProxyFrontendCertificateEndpointResponse424 | PostServicesHAProxyFrontendCertificateEndpointResponse500 | PostServicesHAProxyFrontendCertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendCertificateEndpointJsonBody
    | PostServicesHAProxyFrontendCertificateEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendCertificateEndpointResponse400
    | PostServicesHAProxyFrontendCertificateEndpointResponse401
    | PostServicesHAProxyFrontendCertificateEndpointResponse403
    | PostServicesHAProxyFrontendCertificateEndpointResponse404
    | PostServicesHAProxyFrontendCertificateEndpointResponse405
    | PostServicesHAProxyFrontendCertificateEndpointResponse406
    | PostServicesHAProxyFrontendCertificateEndpointResponse409
    | PostServicesHAProxyFrontendCertificateEndpointResponse415
    | PostServicesHAProxyFrontendCertificateEndpointResponse422
    | PostServicesHAProxyFrontendCertificateEndpointResponse424
    | PostServicesHAProxyFrontendCertificateEndpointResponse500
    | PostServicesHAProxyFrontendCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend Certificates.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendCertificate<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-certificate-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendCertificateEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendCertificateEndpointResponse400 | PostServicesHAProxyFrontendCertificateEndpointResponse401 | PostServicesHAProxyFrontendCertificateEndpointResponse403 | PostServicesHAProxyFrontendCertificateEndpointResponse404 | PostServicesHAProxyFrontendCertificateEndpointResponse405 | PostServicesHAProxyFrontendCertificateEndpointResponse406 | PostServicesHAProxyFrontendCertificateEndpointResponse409 | PostServicesHAProxyFrontendCertificateEndpointResponse415 | PostServicesHAProxyFrontendCertificateEndpointResponse422 | PostServicesHAProxyFrontendCertificateEndpointResponse424 | PostServicesHAProxyFrontendCertificateEndpointResponse500 | PostServicesHAProxyFrontendCertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendCertificateEndpointJsonBody
    | PostServicesHAProxyFrontendCertificateEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendCertificateEndpointResponse400
    | PostServicesHAProxyFrontendCertificateEndpointResponse401
    | PostServicesHAProxyFrontendCertificateEndpointResponse403
    | PostServicesHAProxyFrontendCertificateEndpointResponse404
    | PostServicesHAProxyFrontendCertificateEndpointResponse405
    | PostServicesHAProxyFrontendCertificateEndpointResponse406
    | PostServicesHAProxyFrontendCertificateEndpointResponse409
    | PostServicesHAProxyFrontendCertificateEndpointResponse415
    | PostServicesHAProxyFrontendCertificateEndpointResponse422
    | PostServicesHAProxyFrontendCertificateEndpointResponse424
    | PostServicesHAProxyFrontendCertificateEndpointResponse500
    | PostServicesHAProxyFrontendCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend Certificates.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendCertificate<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-certificate-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendCertificateEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendCertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendCertificateEndpointResponse400 | PostServicesHAProxyFrontendCertificateEndpointResponse401 | PostServicesHAProxyFrontendCertificateEndpointResponse403 | PostServicesHAProxyFrontendCertificateEndpointResponse404 | PostServicesHAProxyFrontendCertificateEndpointResponse405 | PostServicesHAProxyFrontendCertificateEndpointResponse406 | PostServicesHAProxyFrontendCertificateEndpointResponse409 | PostServicesHAProxyFrontendCertificateEndpointResponse415 | PostServicesHAProxyFrontendCertificateEndpointResponse422 | PostServicesHAProxyFrontendCertificateEndpointResponse424 | PostServicesHAProxyFrontendCertificateEndpointResponse500 | PostServicesHAProxyFrontendCertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
