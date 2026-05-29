from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_acme_certificate_domain_endpoint_data_body import (
    PostServicesACMECertificateDomainEndpointDataBody,
)
from ...models.post_services_acme_certificate_domain_endpoint_json_body import (
    PostServicesACMECertificateDomainEndpointJsonBody,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_400 import (
    PostServicesACMECertificateDomainEndpointResponse400,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_401 import (
    PostServicesACMECertificateDomainEndpointResponse401,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_403 import (
    PostServicesACMECertificateDomainEndpointResponse403,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_404 import (
    PostServicesACMECertificateDomainEndpointResponse404,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_405 import (
    PostServicesACMECertificateDomainEndpointResponse405,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_406 import (
    PostServicesACMECertificateDomainEndpointResponse406,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_409 import (
    PostServicesACMECertificateDomainEndpointResponse409,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_415 import (
    PostServicesACMECertificateDomainEndpointResponse415,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_422 import (
    PostServicesACMECertificateDomainEndpointResponse422,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_424 import (
    PostServicesACMECertificateDomainEndpointResponse424,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_500 import (
    PostServicesACMECertificateDomainEndpointResponse500,
)
from ...models.post_services_acme_certificate_domain_endpoint_response_503 import (
    PostServicesACMECertificateDomainEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesACMECertificateDomainEndpointJsonBody
    | PostServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/acme/certificate/domain",
    }

    if isinstance(body, PostServicesACMECertificateDomainEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesACMECertificateDomainEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesACMECertificateDomainEndpointResponse400
    | PostServicesACMECertificateDomainEndpointResponse401
    | PostServicesACMECertificateDomainEndpointResponse403
    | PostServicesACMECertificateDomainEndpointResponse404
    | PostServicesACMECertificateDomainEndpointResponse405
    | PostServicesACMECertificateDomainEndpointResponse406
    | PostServicesACMECertificateDomainEndpointResponse409
    | PostServicesACMECertificateDomainEndpointResponse415
    | PostServicesACMECertificateDomainEndpointResponse422
    | PostServicesACMECertificateDomainEndpointResponse424
    | PostServicesACMECertificateDomainEndpointResponse500
    | PostServicesACMECertificateDomainEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesACMECertificateDomainEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesACMECertificateDomainEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesACMECertificateDomainEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesACMECertificateDomainEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesACMECertificateDomainEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesACMECertificateDomainEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesACMECertificateDomainEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesACMECertificateDomainEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesACMECertificateDomainEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesACMECertificateDomainEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesACMECertificateDomainEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesACMECertificateDomainEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesACMECertificateDomainEndpointResponse400
    | PostServicesACMECertificateDomainEndpointResponse401
    | PostServicesACMECertificateDomainEndpointResponse403
    | PostServicesACMECertificateDomainEndpointResponse404
    | PostServicesACMECertificateDomainEndpointResponse405
    | PostServicesACMECertificateDomainEndpointResponse406
    | PostServicesACMECertificateDomainEndpointResponse409
    | PostServicesACMECertificateDomainEndpointResponse415
    | PostServicesACMECertificateDomainEndpointResponse422
    | PostServicesACMECertificateDomainEndpointResponse424
    | PostServicesACMECertificateDomainEndpointResponse500
    | PostServicesACMECertificateDomainEndpointResponse503
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
    body: PostServicesACMECertificateDomainEndpointJsonBody
    | PostServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateDomainEndpointResponse400
    | PostServicesACMECertificateDomainEndpointResponse401
    | PostServicesACMECertificateDomainEndpointResponse403
    | PostServicesACMECertificateDomainEndpointResponse404
    | PostServicesACMECertificateDomainEndpointResponse405
    | PostServicesACMECertificateDomainEndpointResponse406
    | PostServicesACMECertificateDomainEndpointResponse409
    | PostServicesACMECertificateDomainEndpointResponse415
    | PostServicesACMECertificateDomainEndpointResponse422
    | PostServicesACMECertificateDomainEndpointResponse424
    | PostServicesACMECertificateDomainEndpointResponse500
    | PostServicesACMECertificateDomainEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PostServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateDomainEndpointResponse400 | PostServicesACMECertificateDomainEndpointResponse401 | PostServicesACMECertificateDomainEndpointResponse403 | PostServicesACMECertificateDomainEndpointResponse404 | PostServicesACMECertificateDomainEndpointResponse405 | PostServicesACMECertificateDomainEndpointResponse406 | PostServicesACMECertificateDomainEndpointResponse409 | PostServicesACMECertificateDomainEndpointResponse415 | PostServicesACMECertificateDomainEndpointResponse422 | PostServicesACMECertificateDomainEndpointResponse424 | PostServicesACMECertificateDomainEndpointResponse500 | PostServicesACMECertificateDomainEndpointResponse503]
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
    body: PostServicesACMECertificateDomainEndpointJsonBody
    | PostServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMECertificateDomainEndpointResponse400
    | PostServicesACMECertificateDomainEndpointResponse401
    | PostServicesACMECertificateDomainEndpointResponse403
    | PostServicesACMECertificateDomainEndpointResponse404
    | PostServicesACMECertificateDomainEndpointResponse405
    | PostServicesACMECertificateDomainEndpointResponse406
    | PostServicesACMECertificateDomainEndpointResponse409
    | PostServicesACMECertificateDomainEndpointResponse415
    | PostServicesACMECertificateDomainEndpointResponse422
    | PostServicesACMECertificateDomainEndpointResponse424
    | PostServicesACMECertificateDomainEndpointResponse500
    | PostServicesACMECertificateDomainEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PostServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateDomainEndpointResponse400 | PostServicesACMECertificateDomainEndpointResponse401 | PostServicesACMECertificateDomainEndpointResponse403 | PostServicesACMECertificateDomainEndpointResponse404 | PostServicesACMECertificateDomainEndpointResponse405 | PostServicesACMECertificateDomainEndpointResponse406 | PostServicesACMECertificateDomainEndpointResponse409 | PostServicesACMECertificateDomainEndpointResponse415 | PostServicesACMECertificateDomainEndpointResponse422 | PostServicesACMECertificateDomainEndpointResponse424 | PostServicesACMECertificateDomainEndpointResponse500 | PostServicesACMECertificateDomainEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateDomainEndpointJsonBody
    | PostServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateDomainEndpointResponse400
    | PostServicesACMECertificateDomainEndpointResponse401
    | PostServicesACMECertificateDomainEndpointResponse403
    | PostServicesACMECertificateDomainEndpointResponse404
    | PostServicesACMECertificateDomainEndpointResponse405
    | PostServicesACMECertificateDomainEndpointResponse406
    | PostServicesACMECertificateDomainEndpointResponse409
    | PostServicesACMECertificateDomainEndpointResponse415
    | PostServicesACMECertificateDomainEndpointResponse422
    | PostServicesACMECertificateDomainEndpointResponse424
    | PostServicesACMECertificateDomainEndpointResponse500
    | PostServicesACMECertificateDomainEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PostServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateDomainEndpointResponse400 | PostServicesACMECertificateDomainEndpointResponse401 | PostServicesACMECertificateDomainEndpointResponse403 | PostServicesACMECertificateDomainEndpointResponse404 | PostServicesACMECertificateDomainEndpointResponse405 | PostServicesACMECertificateDomainEndpointResponse406 | PostServicesACMECertificateDomainEndpointResponse409 | PostServicesACMECertificateDomainEndpointResponse415 | PostServicesACMECertificateDomainEndpointResponse422 | PostServicesACMECertificateDomainEndpointResponse424 | PostServicesACMECertificateDomainEndpointResponse500 | PostServicesACMECertificateDomainEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateDomainEndpointJsonBody
    | PostServicesACMECertificateDomainEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMECertificateDomainEndpointResponse400
    | PostServicesACMECertificateDomainEndpointResponse401
    | PostServicesACMECertificateDomainEndpointResponse403
    | PostServicesACMECertificateDomainEndpointResponse404
    | PostServicesACMECertificateDomainEndpointResponse405
    | PostServicesACMECertificateDomainEndpointResponse406
    | PostServicesACMECertificateDomainEndpointResponse409
    | PostServicesACMECertificateDomainEndpointResponse415
    | PostServicesACMECertificateDomainEndpointResponse422
    | PostServicesACMECertificateDomainEndpointResponse424
    | PostServicesACMECertificateDomainEndpointResponse500
    | PostServicesACMECertificateDomainEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Certificate Domain.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateDomain<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-domain-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateDomainEndpointJsonBody | Unset):
        body (PostServicesACMECertificateDomainEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateDomainEndpointResponse400 | PostServicesACMECertificateDomainEndpointResponse401 | PostServicesACMECertificateDomainEndpointResponse403 | PostServicesACMECertificateDomainEndpointResponse404 | PostServicesACMECertificateDomainEndpointResponse405 | PostServicesACMECertificateDomainEndpointResponse406 | PostServicesACMECertificateDomainEndpointResponse409 | PostServicesACMECertificateDomainEndpointResponse415 | PostServicesACMECertificateDomainEndpointResponse422 | PostServicesACMECertificateDomainEndpointResponse424 | PostServicesACMECertificateDomainEndpointResponse500 | PostServicesACMECertificateDomainEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
