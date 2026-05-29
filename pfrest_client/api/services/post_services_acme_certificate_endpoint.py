from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_acme_certificate_endpoint_data_body import PostServicesACMECertificateEndpointDataBody
from ...models.post_services_acme_certificate_endpoint_json_body import PostServicesACMECertificateEndpointJsonBody
from ...models.post_services_acme_certificate_endpoint_response_400 import (
    PostServicesACMECertificateEndpointResponse400,
)
from ...models.post_services_acme_certificate_endpoint_response_401 import (
    PostServicesACMECertificateEndpointResponse401,
)
from ...models.post_services_acme_certificate_endpoint_response_403 import (
    PostServicesACMECertificateEndpointResponse403,
)
from ...models.post_services_acme_certificate_endpoint_response_404 import (
    PostServicesACMECertificateEndpointResponse404,
)
from ...models.post_services_acme_certificate_endpoint_response_405 import (
    PostServicesACMECertificateEndpointResponse405,
)
from ...models.post_services_acme_certificate_endpoint_response_406 import (
    PostServicesACMECertificateEndpointResponse406,
)
from ...models.post_services_acme_certificate_endpoint_response_409 import (
    PostServicesACMECertificateEndpointResponse409,
)
from ...models.post_services_acme_certificate_endpoint_response_415 import (
    PostServicesACMECertificateEndpointResponse415,
)
from ...models.post_services_acme_certificate_endpoint_response_422 import (
    PostServicesACMECertificateEndpointResponse422,
)
from ...models.post_services_acme_certificate_endpoint_response_424 import (
    PostServicesACMECertificateEndpointResponse424,
)
from ...models.post_services_acme_certificate_endpoint_response_500 import (
    PostServicesACMECertificateEndpointResponse500,
)
from ...models.post_services_acme_certificate_endpoint_response_503 import (
    PostServicesACMECertificateEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesACMECertificateEndpointJsonBody | PostServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/acme/certificate",
    }

    if isinstance(body, PostServicesACMECertificateEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesACMECertificateEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesACMECertificateEndpointResponse400
    | PostServicesACMECertificateEndpointResponse401
    | PostServicesACMECertificateEndpointResponse403
    | PostServicesACMECertificateEndpointResponse404
    | PostServicesACMECertificateEndpointResponse405
    | PostServicesACMECertificateEndpointResponse406
    | PostServicesACMECertificateEndpointResponse409
    | PostServicesACMECertificateEndpointResponse415
    | PostServicesACMECertificateEndpointResponse422
    | PostServicesACMECertificateEndpointResponse424
    | PostServicesACMECertificateEndpointResponse500
    | PostServicesACMECertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesACMECertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesACMECertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesACMECertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesACMECertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesACMECertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesACMECertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesACMECertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesACMECertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesACMECertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesACMECertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesACMECertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesACMECertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesACMECertificateEndpointResponse400
    | PostServicesACMECertificateEndpointResponse401
    | PostServicesACMECertificateEndpointResponse403
    | PostServicesACMECertificateEndpointResponse404
    | PostServicesACMECertificateEndpointResponse405
    | PostServicesACMECertificateEndpointResponse406
    | PostServicesACMECertificateEndpointResponse409
    | PostServicesACMECertificateEndpointResponse415
    | PostServicesACMECertificateEndpointResponse422
    | PostServicesACMECertificateEndpointResponse424
    | PostServicesACMECertificateEndpointResponse500
    | PostServicesACMECertificateEndpointResponse503
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
    body: PostServicesACMECertificateEndpointJsonBody | PostServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateEndpointResponse400
    | PostServicesACMECertificateEndpointResponse401
    | PostServicesACMECertificateEndpointResponse403
    | PostServicesACMECertificateEndpointResponse404
    | PostServicesACMECertificateEndpointResponse405
    | PostServicesACMECertificateEndpointResponse406
    | PostServicesACMECertificateEndpointResponse409
    | PostServicesACMECertificateEndpointResponse415
    | PostServicesACMECertificateEndpointResponse422
    | PostServicesACMECertificateEndpointResponse424
    | PostServicesACMECertificateEndpointResponse500
    | PostServicesACMECertificateEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateEndpointJsonBody | Unset):
        body (PostServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateEndpointResponse400 | PostServicesACMECertificateEndpointResponse401 | PostServicesACMECertificateEndpointResponse403 | PostServicesACMECertificateEndpointResponse404 | PostServicesACMECertificateEndpointResponse405 | PostServicesACMECertificateEndpointResponse406 | PostServicesACMECertificateEndpointResponse409 | PostServicesACMECertificateEndpointResponse415 | PostServicesACMECertificateEndpointResponse422 | PostServicesACMECertificateEndpointResponse424 | PostServicesACMECertificateEndpointResponse500 | PostServicesACMECertificateEndpointResponse503]
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
    body: PostServicesACMECertificateEndpointJsonBody | PostServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesACMECertificateEndpointResponse400
    | PostServicesACMECertificateEndpointResponse401
    | PostServicesACMECertificateEndpointResponse403
    | PostServicesACMECertificateEndpointResponse404
    | PostServicesACMECertificateEndpointResponse405
    | PostServicesACMECertificateEndpointResponse406
    | PostServicesACMECertificateEndpointResponse409
    | PostServicesACMECertificateEndpointResponse415
    | PostServicesACMECertificateEndpointResponse422
    | PostServicesACMECertificateEndpointResponse424
    | PostServicesACMECertificateEndpointResponse500
    | PostServicesACMECertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateEndpointJsonBody | Unset):
        body (PostServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateEndpointResponse400 | PostServicesACMECertificateEndpointResponse401 | PostServicesACMECertificateEndpointResponse403 | PostServicesACMECertificateEndpointResponse404 | PostServicesACMECertificateEndpointResponse405 | PostServicesACMECertificateEndpointResponse406 | PostServicesACMECertificateEndpointResponse409 | PostServicesACMECertificateEndpointResponse415 | PostServicesACMECertificateEndpointResponse422 | PostServicesACMECertificateEndpointResponse424 | PostServicesACMECertificateEndpointResponse500 | PostServicesACMECertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateEndpointJsonBody | PostServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateEndpointResponse400
    | PostServicesACMECertificateEndpointResponse401
    | PostServicesACMECertificateEndpointResponse403
    | PostServicesACMECertificateEndpointResponse404
    | PostServicesACMECertificateEndpointResponse405
    | PostServicesACMECertificateEndpointResponse406
    | PostServicesACMECertificateEndpointResponse409
    | PostServicesACMECertificateEndpointResponse415
    | PostServicesACMECertificateEndpointResponse422
    | PostServicesACMECertificateEndpointResponse424
    | PostServicesACMECertificateEndpointResponse500
    | PostServicesACMECertificateEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateEndpointJsonBody | Unset):
        body (PostServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateEndpointResponse400 | PostServicesACMECertificateEndpointResponse401 | PostServicesACMECertificateEndpointResponse403 | PostServicesACMECertificateEndpointResponse404 | PostServicesACMECertificateEndpointResponse405 | PostServicesACMECertificateEndpointResponse406 | PostServicesACMECertificateEndpointResponse409 | PostServicesACMECertificateEndpointResponse415 | PostServicesACMECertificateEndpointResponse422 | PostServicesACMECertificateEndpointResponse424 | PostServicesACMECertificateEndpointResponse500 | PostServicesACMECertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateEndpointJsonBody | PostServicesACMECertificateEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesACMECertificateEndpointResponse400
    | PostServicesACMECertificateEndpointResponse401
    | PostServicesACMECertificateEndpointResponse403
    | PostServicesACMECertificateEndpointResponse404
    | PostServicesACMECertificateEndpointResponse405
    | PostServicesACMECertificateEndpointResponse406
    | PostServicesACMECertificateEndpointResponse409
    | PostServicesACMECertificateEndpointResponse415
    | PostServicesACMECertificateEndpointResponse422
    | PostServicesACMECertificateEndpointResponse424
    | PostServicesACMECertificateEndpointResponse500
    | PostServicesACMECertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateEndpointJsonBody | Unset):
        body (PostServicesACMECertificateEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateEndpointResponse400 | PostServicesACMECertificateEndpointResponse401 | PostServicesACMECertificateEndpointResponse403 | PostServicesACMECertificateEndpointResponse404 | PostServicesACMECertificateEndpointResponse405 | PostServicesACMECertificateEndpointResponse406 | PostServicesACMECertificateEndpointResponse409 | PostServicesACMECertificateEndpointResponse415 | PostServicesACMECertificateEndpointResponse422 | PostServicesACMECertificateEndpointResponse424 | PostServicesACMECertificateEndpointResponse500 | PostServicesACMECertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
