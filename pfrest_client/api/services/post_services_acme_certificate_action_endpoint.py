from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_acme_certificate_action_endpoint_data_body import (
    PostServicesACMECertificateActionEndpointDataBody,
)
from ...models.post_services_acme_certificate_action_endpoint_json_body import (
    PostServicesACMECertificateActionEndpointJsonBody,
)
from ...models.post_services_acme_certificate_action_endpoint_response_400 import (
    PostServicesACMECertificateActionEndpointResponse400,
)
from ...models.post_services_acme_certificate_action_endpoint_response_401 import (
    PostServicesACMECertificateActionEndpointResponse401,
)
from ...models.post_services_acme_certificate_action_endpoint_response_403 import (
    PostServicesACMECertificateActionEndpointResponse403,
)
from ...models.post_services_acme_certificate_action_endpoint_response_404 import (
    PostServicesACMECertificateActionEndpointResponse404,
)
from ...models.post_services_acme_certificate_action_endpoint_response_405 import (
    PostServicesACMECertificateActionEndpointResponse405,
)
from ...models.post_services_acme_certificate_action_endpoint_response_406 import (
    PostServicesACMECertificateActionEndpointResponse406,
)
from ...models.post_services_acme_certificate_action_endpoint_response_409 import (
    PostServicesACMECertificateActionEndpointResponse409,
)
from ...models.post_services_acme_certificate_action_endpoint_response_415 import (
    PostServicesACMECertificateActionEndpointResponse415,
)
from ...models.post_services_acme_certificate_action_endpoint_response_422 import (
    PostServicesACMECertificateActionEndpointResponse422,
)
from ...models.post_services_acme_certificate_action_endpoint_response_424 import (
    PostServicesACMECertificateActionEndpointResponse424,
)
from ...models.post_services_acme_certificate_action_endpoint_response_500 import (
    PostServicesACMECertificateActionEndpointResponse500,
)
from ...models.post_services_acme_certificate_action_endpoint_response_503 import (
    PostServicesACMECertificateActionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesACMECertificateActionEndpointJsonBody
    | PostServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/acme/certificate/action",
    }

    if isinstance(body, PostServicesACMECertificateActionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesACMECertificateActionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesACMECertificateActionEndpointResponse400
    | PostServicesACMECertificateActionEndpointResponse401
    | PostServicesACMECertificateActionEndpointResponse403
    | PostServicesACMECertificateActionEndpointResponse404
    | PostServicesACMECertificateActionEndpointResponse405
    | PostServicesACMECertificateActionEndpointResponse406
    | PostServicesACMECertificateActionEndpointResponse409
    | PostServicesACMECertificateActionEndpointResponse415
    | PostServicesACMECertificateActionEndpointResponse422
    | PostServicesACMECertificateActionEndpointResponse424
    | PostServicesACMECertificateActionEndpointResponse500
    | PostServicesACMECertificateActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesACMECertificateActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesACMECertificateActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesACMECertificateActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesACMECertificateActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesACMECertificateActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesACMECertificateActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesACMECertificateActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesACMECertificateActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesACMECertificateActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesACMECertificateActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesACMECertificateActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesACMECertificateActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesACMECertificateActionEndpointResponse400
    | PostServicesACMECertificateActionEndpointResponse401
    | PostServicesACMECertificateActionEndpointResponse403
    | PostServicesACMECertificateActionEndpointResponse404
    | PostServicesACMECertificateActionEndpointResponse405
    | PostServicesACMECertificateActionEndpointResponse406
    | PostServicesACMECertificateActionEndpointResponse409
    | PostServicesACMECertificateActionEndpointResponse415
    | PostServicesACMECertificateActionEndpointResponse422
    | PostServicesACMECertificateActionEndpointResponse424
    | PostServicesACMECertificateActionEndpointResponse500
    | PostServicesACMECertificateActionEndpointResponse503
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
    body: PostServicesACMECertificateActionEndpointJsonBody
    | PostServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateActionEndpointResponse400
    | PostServicesACMECertificateActionEndpointResponse401
    | PostServicesACMECertificateActionEndpointResponse403
    | PostServicesACMECertificateActionEndpointResponse404
    | PostServicesACMECertificateActionEndpointResponse405
    | PostServicesACMECertificateActionEndpointResponse406
    | PostServicesACMECertificateActionEndpointResponse409
    | PostServicesACMECertificateActionEndpointResponse415
    | PostServicesACMECertificateActionEndpointResponse422
    | PostServicesACMECertificateActionEndpointResponse424
    | PostServicesACMECertificateActionEndpointResponse500
    | PostServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Certificate Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PostServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateActionEndpointResponse400 | PostServicesACMECertificateActionEndpointResponse401 | PostServicesACMECertificateActionEndpointResponse403 | PostServicesACMECertificateActionEndpointResponse404 | PostServicesACMECertificateActionEndpointResponse405 | PostServicesACMECertificateActionEndpointResponse406 | PostServicesACMECertificateActionEndpointResponse409 | PostServicesACMECertificateActionEndpointResponse415 | PostServicesACMECertificateActionEndpointResponse422 | PostServicesACMECertificateActionEndpointResponse424 | PostServicesACMECertificateActionEndpointResponse500 | PostServicesACMECertificateActionEndpointResponse503]
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
    body: PostServicesACMECertificateActionEndpointJsonBody
    | PostServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMECertificateActionEndpointResponse400
    | PostServicesACMECertificateActionEndpointResponse401
    | PostServicesACMECertificateActionEndpointResponse403
    | PostServicesACMECertificateActionEndpointResponse404
    | PostServicesACMECertificateActionEndpointResponse405
    | PostServicesACMECertificateActionEndpointResponse406
    | PostServicesACMECertificateActionEndpointResponse409
    | PostServicesACMECertificateActionEndpointResponse415
    | PostServicesACMECertificateActionEndpointResponse422
    | PostServicesACMECertificateActionEndpointResponse424
    | PostServicesACMECertificateActionEndpointResponse500
    | PostServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Certificate Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PostServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateActionEndpointResponse400 | PostServicesACMECertificateActionEndpointResponse401 | PostServicesACMECertificateActionEndpointResponse403 | PostServicesACMECertificateActionEndpointResponse404 | PostServicesACMECertificateActionEndpointResponse405 | PostServicesACMECertificateActionEndpointResponse406 | PostServicesACMECertificateActionEndpointResponse409 | PostServicesACMECertificateActionEndpointResponse415 | PostServicesACMECertificateActionEndpointResponse422 | PostServicesACMECertificateActionEndpointResponse424 | PostServicesACMECertificateActionEndpointResponse500 | PostServicesACMECertificateActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateActionEndpointJsonBody
    | PostServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateActionEndpointResponse400
    | PostServicesACMECertificateActionEndpointResponse401
    | PostServicesACMECertificateActionEndpointResponse403
    | PostServicesACMECertificateActionEndpointResponse404
    | PostServicesACMECertificateActionEndpointResponse405
    | PostServicesACMECertificateActionEndpointResponse406
    | PostServicesACMECertificateActionEndpointResponse409
    | PostServicesACMECertificateActionEndpointResponse415
    | PostServicesACMECertificateActionEndpointResponse422
    | PostServicesACMECertificateActionEndpointResponse424
    | PostServicesACMECertificateActionEndpointResponse500
    | PostServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Certificate Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PostServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateActionEndpointResponse400 | PostServicesACMECertificateActionEndpointResponse401 | PostServicesACMECertificateActionEndpointResponse403 | PostServicesACMECertificateActionEndpointResponse404 | PostServicesACMECertificateActionEndpointResponse405 | PostServicesACMECertificateActionEndpointResponse406 | PostServicesACMECertificateActionEndpointResponse409 | PostServicesACMECertificateActionEndpointResponse415 | PostServicesACMECertificateActionEndpointResponse422 | PostServicesACMECertificateActionEndpointResponse424 | PostServicesACMECertificateActionEndpointResponse500 | PostServicesACMECertificateActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateActionEndpointJsonBody
    | PostServicesACMECertificateActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMECertificateActionEndpointResponse400
    | PostServicesACMECertificateActionEndpointResponse401
    | PostServicesACMECertificateActionEndpointResponse403
    | PostServicesACMECertificateActionEndpointResponse404
    | PostServicesACMECertificateActionEndpointResponse405
    | PostServicesACMECertificateActionEndpointResponse406
    | PostServicesACMECertificateActionEndpointResponse409
    | PostServicesACMECertificateActionEndpointResponse415
    | PostServicesACMECertificateActionEndpointResponse422
    | PostServicesACMECertificateActionEndpointResponse424
    | PostServicesACMECertificateActionEndpointResponse500
    | PostServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Certificate Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-post ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMECertificateActionEndpointJsonBody | Unset):
        body (PostServicesACMECertificateActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateActionEndpointResponse400 | PostServicesACMECertificateActionEndpointResponse401 | PostServicesACMECertificateActionEndpointResponse403 | PostServicesACMECertificateActionEndpointResponse404 | PostServicesACMECertificateActionEndpointResponse405 | PostServicesACMECertificateActionEndpointResponse406 | PostServicesACMECertificateActionEndpointResponse409 | PostServicesACMECertificateActionEndpointResponse415 | PostServicesACMECertificateActionEndpointResponse422 | PostServicesACMECertificateActionEndpointResponse424 | PostServicesACMECertificateActionEndpointResponse500 | PostServicesACMECertificateActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
