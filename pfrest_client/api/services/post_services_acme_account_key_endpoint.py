from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_acme_account_key_endpoint_data_body import PostServicesACMEAccountKeyEndpointDataBody
from ...models.post_services_acme_account_key_endpoint_json_body import PostServicesACMEAccountKeyEndpointJsonBody
from ...models.post_services_acme_account_key_endpoint_response_400 import PostServicesACMEAccountKeyEndpointResponse400
from ...models.post_services_acme_account_key_endpoint_response_401 import PostServicesACMEAccountKeyEndpointResponse401
from ...models.post_services_acme_account_key_endpoint_response_403 import PostServicesACMEAccountKeyEndpointResponse403
from ...models.post_services_acme_account_key_endpoint_response_404 import PostServicesACMEAccountKeyEndpointResponse404
from ...models.post_services_acme_account_key_endpoint_response_405 import PostServicesACMEAccountKeyEndpointResponse405
from ...models.post_services_acme_account_key_endpoint_response_406 import PostServicesACMEAccountKeyEndpointResponse406
from ...models.post_services_acme_account_key_endpoint_response_409 import PostServicesACMEAccountKeyEndpointResponse409
from ...models.post_services_acme_account_key_endpoint_response_415 import PostServicesACMEAccountKeyEndpointResponse415
from ...models.post_services_acme_account_key_endpoint_response_422 import PostServicesACMEAccountKeyEndpointResponse422
from ...models.post_services_acme_account_key_endpoint_response_424 import PostServicesACMEAccountKeyEndpointResponse424
from ...models.post_services_acme_account_key_endpoint_response_500 import PostServicesACMEAccountKeyEndpointResponse500
from ...models.post_services_acme_account_key_endpoint_response_503 import PostServicesACMEAccountKeyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesACMEAccountKeyEndpointJsonBody | PostServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/acme/account_key",
    }

    if isinstance(body, PostServicesACMEAccountKeyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesACMEAccountKeyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesACMEAccountKeyEndpointResponse400
    | PostServicesACMEAccountKeyEndpointResponse401
    | PostServicesACMEAccountKeyEndpointResponse403
    | PostServicesACMEAccountKeyEndpointResponse404
    | PostServicesACMEAccountKeyEndpointResponse405
    | PostServicesACMEAccountKeyEndpointResponse406
    | PostServicesACMEAccountKeyEndpointResponse409
    | PostServicesACMEAccountKeyEndpointResponse415
    | PostServicesACMEAccountKeyEndpointResponse422
    | PostServicesACMEAccountKeyEndpointResponse424
    | PostServicesACMEAccountKeyEndpointResponse500
    | PostServicesACMEAccountKeyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesACMEAccountKeyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesACMEAccountKeyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesACMEAccountKeyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesACMEAccountKeyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesACMEAccountKeyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesACMEAccountKeyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesACMEAccountKeyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesACMEAccountKeyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesACMEAccountKeyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesACMEAccountKeyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesACMEAccountKeyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesACMEAccountKeyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesACMEAccountKeyEndpointResponse400
    | PostServicesACMEAccountKeyEndpointResponse401
    | PostServicesACMEAccountKeyEndpointResponse403
    | PostServicesACMEAccountKeyEndpointResponse404
    | PostServicesACMEAccountKeyEndpointResponse405
    | PostServicesACMEAccountKeyEndpointResponse406
    | PostServicesACMEAccountKeyEndpointResponse409
    | PostServicesACMEAccountKeyEndpointResponse415
    | PostServicesACMEAccountKeyEndpointResponse422
    | PostServicesACMEAccountKeyEndpointResponse424
    | PostServicesACMEAccountKeyEndpointResponse500
    | PostServicesACMEAccountKeyEndpointResponse503
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
    body: PostServicesACMEAccountKeyEndpointJsonBody | PostServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesACMEAccountKeyEndpointResponse400
    | PostServicesACMEAccountKeyEndpointResponse401
    | PostServicesACMEAccountKeyEndpointResponse403
    | PostServicesACMEAccountKeyEndpointResponse404
    | PostServicesACMEAccountKeyEndpointResponse405
    | PostServicesACMEAccountKeyEndpointResponse406
    | PostServicesACMEAccountKeyEndpointResponse409
    | PostServicesACMEAccountKeyEndpointResponse415
    | PostServicesACMEAccountKeyEndpointResponse422
    | PostServicesACMEAccountKeyEndpointResponse424
    | PostServicesACMEAccountKeyEndpointResponse500
    | PostServicesACMEAccountKeyEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Account Key.<br><br>Note: You must register the account key
    with the ACME server after creating it. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMEAccountKeyEndpointResponse400 | PostServicesACMEAccountKeyEndpointResponse401 | PostServicesACMEAccountKeyEndpointResponse403 | PostServicesACMEAccountKeyEndpointResponse404 | PostServicesACMEAccountKeyEndpointResponse405 | PostServicesACMEAccountKeyEndpointResponse406 | PostServicesACMEAccountKeyEndpointResponse409 | PostServicesACMEAccountKeyEndpointResponse415 | PostServicesACMEAccountKeyEndpointResponse422 | PostServicesACMEAccountKeyEndpointResponse424 | PostServicesACMEAccountKeyEndpointResponse500 | PostServicesACMEAccountKeyEndpointResponse503]
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
    body: PostServicesACMEAccountKeyEndpointJsonBody | PostServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesACMEAccountKeyEndpointResponse400
    | PostServicesACMEAccountKeyEndpointResponse401
    | PostServicesACMEAccountKeyEndpointResponse403
    | PostServicesACMEAccountKeyEndpointResponse404
    | PostServicesACMEAccountKeyEndpointResponse405
    | PostServicesACMEAccountKeyEndpointResponse406
    | PostServicesACMEAccountKeyEndpointResponse409
    | PostServicesACMEAccountKeyEndpointResponse415
    | PostServicesACMEAccountKeyEndpointResponse422
    | PostServicesACMEAccountKeyEndpointResponse424
    | PostServicesACMEAccountKeyEndpointResponse500
    | PostServicesACMEAccountKeyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Account Key.<br><br>Note: You must register the account key
    with the ACME server after creating it. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMEAccountKeyEndpointResponse400 | PostServicesACMEAccountKeyEndpointResponse401 | PostServicesACMEAccountKeyEndpointResponse403 | PostServicesACMEAccountKeyEndpointResponse404 | PostServicesACMEAccountKeyEndpointResponse405 | PostServicesACMEAccountKeyEndpointResponse406 | PostServicesACMEAccountKeyEndpointResponse409 | PostServicesACMEAccountKeyEndpointResponse415 | PostServicesACMEAccountKeyEndpointResponse422 | PostServicesACMEAccountKeyEndpointResponse424 | PostServicesACMEAccountKeyEndpointResponse500 | PostServicesACMEAccountKeyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMEAccountKeyEndpointJsonBody | PostServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesACMEAccountKeyEndpointResponse400
    | PostServicesACMEAccountKeyEndpointResponse401
    | PostServicesACMEAccountKeyEndpointResponse403
    | PostServicesACMEAccountKeyEndpointResponse404
    | PostServicesACMEAccountKeyEndpointResponse405
    | PostServicesACMEAccountKeyEndpointResponse406
    | PostServicesACMEAccountKeyEndpointResponse409
    | PostServicesACMEAccountKeyEndpointResponse415
    | PostServicesACMEAccountKeyEndpointResponse422
    | PostServicesACMEAccountKeyEndpointResponse424
    | PostServicesACMEAccountKeyEndpointResponse500
    | PostServicesACMEAccountKeyEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new ACME Account Key.<br><br>Note: You must register the account key
    with the ACME server after creating it. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMEAccountKeyEndpointResponse400 | PostServicesACMEAccountKeyEndpointResponse401 | PostServicesACMEAccountKeyEndpointResponse403 | PostServicesACMEAccountKeyEndpointResponse404 | PostServicesACMEAccountKeyEndpointResponse405 | PostServicesACMEAccountKeyEndpointResponse406 | PostServicesACMEAccountKeyEndpointResponse409 | PostServicesACMEAccountKeyEndpointResponse415 | PostServicesACMEAccountKeyEndpointResponse422 | PostServicesACMEAccountKeyEndpointResponse424 | PostServicesACMEAccountKeyEndpointResponse500 | PostServicesACMEAccountKeyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMEAccountKeyEndpointJsonBody | PostServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesACMEAccountKeyEndpointResponse400
    | PostServicesACMEAccountKeyEndpointResponse401
    | PostServicesACMEAccountKeyEndpointResponse403
    | PostServicesACMEAccountKeyEndpointResponse404
    | PostServicesACMEAccountKeyEndpointResponse405
    | PostServicesACMEAccountKeyEndpointResponse406
    | PostServicesACMEAccountKeyEndpointResponse409
    | PostServicesACMEAccountKeyEndpointResponse415
    | PostServicesACMEAccountKeyEndpointResponse422
    | PostServicesACMEAccountKeyEndpointResponse424
    | PostServicesACMEAccountKeyEndpointResponse500
    | PostServicesACMEAccountKeyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new ACME Account Key.<br><br>Note: You must register the account key
    with the ACME server after creating it. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-post ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMEAccountKeyEndpointResponse400 | PostServicesACMEAccountKeyEndpointResponse401 | PostServicesACMEAccountKeyEndpointResponse403 | PostServicesACMEAccountKeyEndpointResponse404 | PostServicesACMEAccountKeyEndpointResponse405 | PostServicesACMEAccountKeyEndpointResponse406 | PostServicesACMEAccountKeyEndpointResponse409 | PostServicesACMEAccountKeyEndpointResponse415 | PostServicesACMEAccountKeyEndpointResponse422 | PostServicesACMEAccountKeyEndpointResponse424 | PostServicesACMEAccountKeyEndpointResponse500 | PostServicesACMEAccountKeyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
