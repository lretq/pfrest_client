from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_acme_certificate_issue_endpoint_data_body import (
    PostServicesACMECertificateIssueEndpointDataBody,
)
from ...models.post_services_acme_certificate_issue_endpoint_json_body import (
    PostServicesACMECertificateIssueEndpointJsonBody,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_400 import (
    PostServicesACMECertificateIssueEndpointResponse400,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_401 import (
    PostServicesACMECertificateIssueEndpointResponse401,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_403 import (
    PostServicesACMECertificateIssueEndpointResponse403,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_404 import (
    PostServicesACMECertificateIssueEndpointResponse404,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_405 import (
    PostServicesACMECertificateIssueEndpointResponse405,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_406 import (
    PostServicesACMECertificateIssueEndpointResponse406,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_409 import (
    PostServicesACMECertificateIssueEndpointResponse409,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_415 import (
    PostServicesACMECertificateIssueEndpointResponse415,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_422 import (
    PostServicesACMECertificateIssueEndpointResponse422,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_424 import (
    PostServicesACMECertificateIssueEndpointResponse424,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_500 import (
    PostServicesACMECertificateIssueEndpointResponse500,
)
from ...models.post_services_acme_certificate_issue_endpoint_response_503 import (
    PostServicesACMECertificateIssueEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesACMECertificateIssueEndpointJsonBody
    | PostServicesACMECertificateIssueEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/acme/certificate/issue",
    }

    if isinstance(body, PostServicesACMECertificateIssueEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesACMECertificateIssueEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesACMECertificateIssueEndpointResponse400
    | PostServicesACMECertificateIssueEndpointResponse401
    | PostServicesACMECertificateIssueEndpointResponse403
    | PostServicesACMECertificateIssueEndpointResponse404
    | PostServicesACMECertificateIssueEndpointResponse405
    | PostServicesACMECertificateIssueEndpointResponse406
    | PostServicesACMECertificateIssueEndpointResponse409
    | PostServicesACMECertificateIssueEndpointResponse415
    | PostServicesACMECertificateIssueEndpointResponse422
    | PostServicesACMECertificateIssueEndpointResponse424
    | PostServicesACMECertificateIssueEndpointResponse500
    | PostServicesACMECertificateIssueEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesACMECertificateIssueEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesACMECertificateIssueEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesACMECertificateIssueEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesACMECertificateIssueEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesACMECertificateIssueEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesACMECertificateIssueEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesACMECertificateIssueEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesACMECertificateIssueEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesACMECertificateIssueEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesACMECertificateIssueEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesACMECertificateIssueEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesACMECertificateIssueEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesACMECertificateIssueEndpointResponse400
    | PostServicesACMECertificateIssueEndpointResponse401
    | PostServicesACMECertificateIssueEndpointResponse403
    | PostServicesACMECertificateIssueEndpointResponse404
    | PostServicesACMECertificateIssueEndpointResponse405
    | PostServicesACMECertificateIssueEndpointResponse406
    | PostServicesACMECertificateIssueEndpointResponse409
    | PostServicesACMECertificateIssueEndpointResponse415
    | PostServicesACMECertificateIssueEndpointResponse422
    | PostServicesACMECertificateIssueEndpointResponse424
    | PostServicesACMECertificateIssueEndpointResponse500
    | PostServicesACMECertificateIssueEndpointResponse503
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
    body: PostServicesACMECertificateIssueEndpointJsonBody
    | PostServicesACMECertificateIssueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateIssueEndpointResponse400
    | PostServicesACMECertificateIssueEndpointResponse401
    | PostServicesACMECertificateIssueEndpointResponse403
    | PostServicesACMECertificateIssueEndpointResponse404
    | PostServicesACMECertificateIssueEndpointResponse405
    | PostServicesACMECertificateIssueEndpointResponse406
    | PostServicesACMECertificateIssueEndpointResponse409
    | PostServicesACMECertificateIssueEndpointResponse415
    | PostServicesACMECertificateIssueEndpointResponse422
    | PostServicesACMECertificateIssueEndpointResponse424
    | PostServicesACMECertificateIssueEndpointResponse500
    | PostServicesACMECertificateIssueEndpointResponse503
]:
    """<h3>Description:</h3>Issue an ACME Certificate.<br><br>Note: This endpoint simply starts the issue
    process but does not attempt to determine whether the outcome was successful. You must manually
    parse the result to determine the outcome.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateIssue<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-issue-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesACMECertificateIssueEndpointJsonBody | Unset):
        body (PostServicesACMECertificateIssueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateIssueEndpointResponse400 | PostServicesACMECertificateIssueEndpointResponse401 | PostServicesACMECertificateIssueEndpointResponse403 | PostServicesACMECertificateIssueEndpointResponse404 | PostServicesACMECertificateIssueEndpointResponse405 | PostServicesACMECertificateIssueEndpointResponse406 | PostServicesACMECertificateIssueEndpointResponse409 | PostServicesACMECertificateIssueEndpointResponse415 | PostServicesACMECertificateIssueEndpointResponse422 | PostServicesACMECertificateIssueEndpointResponse424 | PostServicesACMECertificateIssueEndpointResponse500 | PostServicesACMECertificateIssueEndpointResponse503]
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
    body: PostServicesACMECertificateIssueEndpointJsonBody
    | PostServicesACMECertificateIssueEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMECertificateIssueEndpointResponse400
    | PostServicesACMECertificateIssueEndpointResponse401
    | PostServicesACMECertificateIssueEndpointResponse403
    | PostServicesACMECertificateIssueEndpointResponse404
    | PostServicesACMECertificateIssueEndpointResponse405
    | PostServicesACMECertificateIssueEndpointResponse406
    | PostServicesACMECertificateIssueEndpointResponse409
    | PostServicesACMECertificateIssueEndpointResponse415
    | PostServicesACMECertificateIssueEndpointResponse422
    | PostServicesACMECertificateIssueEndpointResponse424
    | PostServicesACMECertificateIssueEndpointResponse500
    | PostServicesACMECertificateIssueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Issue an ACME Certificate.<br><br>Note: This endpoint simply starts the issue
    process but does not attempt to determine whether the outcome was successful. You must manually
    parse the result to determine the outcome.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateIssue<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-issue-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesACMECertificateIssueEndpointJsonBody | Unset):
        body (PostServicesACMECertificateIssueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateIssueEndpointResponse400 | PostServicesACMECertificateIssueEndpointResponse401 | PostServicesACMECertificateIssueEndpointResponse403 | PostServicesACMECertificateIssueEndpointResponse404 | PostServicesACMECertificateIssueEndpointResponse405 | PostServicesACMECertificateIssueEndpointResponse406 | PostServicesACMECertificateIssueEndpointResponse409 | PostServicesACMECertificateIssueEndpointResponse415 | PostServicesACMECertificateIssueEndpointResponse422 | PostServicesACMECertificateIssueEndpointResponse424 | PostServicesACMECertificateIssueEndpointResponse500 | PostServicesACMECertificateIssueEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateIssueEndpointJsonBody
    | PostServicesACMECertificateIssueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMECertificateIssueEndpointResponse400
    | PostServicesACMECertificateIssueEndpointResponse401
    | PostServicesACMECertificateIssueEndpointResponse403
    | PostServicesACMECertificateIssueEndpointResponse404
    | PostServicesACMECertificateIssueEndpointResponse405
    | PostServicesACMECertificateIssueEndpointResponse406
    | PostServicesACMECertificateIssueEndpointResponse409
    | PostServicesACMECertificateIssueEndpointResponse415
    | PostServicesACMECertificateIssueEndpointResponse422
    | PostServicesACMECertificateIssueEndpointResponse424
    | PostServicesACMECertificateIssueEndpointResponse500
    | PostServicesACMECertificateIssueEndpointResponse503
]:
    """<h3>Description:</h3>Issue an ACME Certificate.<br><br>Note: This endpoint simply starts the issue
    process but does not attempt to determine whether the outcome was successful. You must manually
    parse the result to determine the outcome.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateIssue<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-issue-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesACMECertificateIssueEndpointJsonBody | Unset):
        body (PostServicesACMECertificateIssueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMECertificateIssueEndpointResponse400 | PostServicesACMECertificateIssueEndpointResponse401 | PostServicesACMECertificateIssueEndpointResponse403 | PostServicesACMECertificateIssueEndpointResponse404 | PostServicesACMECertificateIssueEndpointResponse405 | PostServicesACMECertificateIssueEndpointResponse406 | PostServicesACMECertificateIssueEndpointResponse409 | PostServicesACMECertificateIssueEndpointResponse415 | PostServicesACMECertificateIssueEndpointResponse422 | PostServicesACMECertificateIssueEndpointResponse424 | PostServicesACMECertificateIssueEndpointResponse500 | PostServicesACMECertificateIssueEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMECertificateIssueEndpointJsonBody
    | PostServicesACMECertificateIssueEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMECertificateIssueEndpointResponse400
    | PostServicesACMECertificateIssueEndpointResponse401
    | PostServicesACMECertificateIssueEndpointResponse403
    | PostServicesACMECertificateIssueEndpointResponse404
    | PostServicesACMECertificateIssueEndpointResponse405
    | PostServicesACMECertificateIssueEndpointResponse406
    | PostServicesACMECertificateIssueEndpointResponse409
    | PostServicesACMECertificateIssueEndpointResponse415
    | PostServicesACMECertificateIssueEndpointResponse422
    | PostServicesACMECertificateIssueEndpointResponse424
    | PostServicesACMECertificateIssueEndpointResponse500
    | PostServicesACMECertificateIssueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Issue an ACME Certificate.<br><br>Note: This endpoint simply starts the issue
    process but does not attempt to determine whether the outcome was successful. You must manually
    parse the result to determine the outcome.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMECertificateIssue<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-certificate-issue-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesACMECertificateIssueEndpointJsonBody | Unset):
        body (PostServicesACMECertificateIssueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMECertificateIssueEndpointResponse400 | PostServicesACMECertificateIssueEndpointResponse401 | PostServicesACMECertificateIssueEndpointResponse403 | PostServicesACMECertificateIssueEndpointResponse404 | PostServicesACMECertificateIssueEndpointResponse405 | PostServicesACMECertificateIssueEndpointResponse406 | PostServicesACMECertificateIssueEndpointResponse409 | PostServicesACMECertificateIssueEndpointResponse415 | PostServicesACMECertificateIssueEndpointResponse422 | PostServicesACMECertificateIssueEndpointResponse424 | PostServicesACMECertificateIssueEndpointResponse500 | PostServicesACMECertificateIssueEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
