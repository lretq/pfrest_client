from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_cron_job_endpoint_data_body import PostServicesCronJobEndpointDataBody
from ...models.post_services_cron_job_endpoint_json_body import PostServicesCronJobEndpointJsonBody
from ...models.post_services_cron_job_endpoint_response_400 import PostServicesCronJobEndpointResponse400
from ...models.post_services_cron_job_endpoint_response_401 import PostServicesCronJobEndpointResponse401
from ...models.post_services_cron_job_endpoint_response_403 import PostServicesCronJobEndpointResponse403
from ...models.post_services_cron_job_endpoint_response_404 import PostServicesCronJobEndpointResponse404
from ...models.post_services_cron_job_endpoint_response_405 import PostServicesCronJobEndpointResponse405
from ...models.post_services_cron_job_endpoint_response_406 import PostServicesCronJobEndpointResponse406
from ...models.post_services_cron_job_endpoint_response_409 import PostServicesCronJobEndpointResponse409
from ...models.post_services_cron_job_endpoint_response_415 import PostServicesCronJobEndpointResponse415
from ...models.post_services_cron_job_endpoint_response_422 import PostServicesCronJobEndpointResponse422
from ...models.post_services_cron_job_endpoint_response_424 import PostServicesCronJobEndpointResponse424
from ...models.post_services_cron_job_endpoint_response_500 import PostServicesCronJobEndpointResponse500
from ...models.post_services_cron_job_endpoint_response_503 import PostServicesCronJobEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesCronJobEndpointJsonBody | PostServicesCronJobEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/cron/job",
    }

    if isinstance(body, PostServicesCronJobEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesCronJobEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesCronJobEndpointResponse400
    | PostServicesCronJobEndpointResponse401
    | PostServicesCronJobEndpointResponse403
    | PostServicesCronJobEndpointResponse404
    | PostServicesCronJobEndpointResponse405
    | PostServicesCronJobEndpointResponse406
    | PostServicesCronJobEndpointResponse409
    | PostServicesCronJobEndpointResponse415
    | PostServicesCronJobEndpointResponse422
    | PostServicesCronJobEndpointResponse424
    | PostServicesCronJobEndpointResponse500
    | PostServicesCronJobEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesCronJobEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesCronJobEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesCronJobEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesCronJobEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesCronJobEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesCronJobEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesCronJobEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesCronJobEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesCronJobEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesCronJobEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesCronJobEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesCronJobEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesCronJobEndpointResponse400
    | PostServicesCronJobEndpointResponse401
    | PostServicesCronJobEndpointResponse403
    | PostServicesCronJobEndpointResponse404
    | PostServicesCronJobEndpointResponse405
    | PostServicesCronJobEndpointResponse406
    | PostServicesCronJobEndpointResponse409
    | PostServicesCronJobEndpointResponse415
    | PostServicesCronJobEndpointResponse422
    | PostServicesCronJobEndpointResponse424
    | PostServicesCronJobEndpointResponse500
    | PostServicesCronJobEndpointResponse503
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
    body: PostServicesCronJobEndpointJsonBody | PostServicesCronJobEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesCronJobEndpointResponse400
    | PostServicesCronJobEndpointResponse401
    | PostServicesCronJobEndpointResponse403
    | PostServicesCronJobEndpointResponse404
    | PostServicesCronJobEndpointResponse405
    | PostServicesCronJobEndpointResponse406
    | PostServicesCronJobEndpointResponse409
    | PostServicesCronJobEndpointResponse415
    | PostServicesCronJobEndpointResponse422
    | PostServicesCronJobEndpointResponse424
    | PostServicesCronJobEndpointResponse500
    | PostServicesCronJobEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-post ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesCronJobEndpointJsonBody | Unset):
        body (PostServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesCronJobEndpointResponse400 | PostServicesCronJobEndpointResponse401 | PostServicesCronJobEndpointResponse403 | PostServicesCronJobEndpointResponse404 | PostServicesCronJobEndpointResponse405 | PostServicesCronJobEndpointResponse406 | PostServicesCronJobEndpointResponse409 | PostServicesCronJobEndpointResponse415 | PostServicesCronJobEndpointResponse422 | PostServicesCronJobEndpointResponse424 | PostServicesCronJobEndpointResponse500 | PostServicesCronJobEndpointResponse503]
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
    body: PostServicesCronJobEndpointJsonBody | PostServicesCronJobEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesCronJobEndpointResponse400
    | PostServicesCronJobEndpointResponse401
    | PostServicesCronJobEndpointResponse403
    | PostServicesCronJobEndpointResponse404
    | PostServicesCronJobEndpointResponse405
    | PostServicesCronJobEndpointResponse406
    | PostServicesCronJobEndpointResponse409
    | PostServicesCronJobEndpointResponse415
    | PostServicesCronJobEndpointResponse422
    | PostServicesCronJobEndpointResponse424
    | PostServicesCronJobEndpointResponse500
    | PostServicesCronJobEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-post ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesCronJobEndpointJsonBody | Unset):
        body (PostServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesCronJobEndpointResponse400 | PostServicesCronJobEndpointResponse401 | PostServicesCronJobEndpointResponse403 | PostServicesCronJobEndpointResponse404 | PostServicesCronJobEndpointResponse405 | PostServicesCronJobEndpointResponse406 | PostServicesCronJobEndpointResponse409 | PostServicesCronJobEndpointResponse415 | PostServicesCronJobEndpointResponse422 | PostServicesCronJobEndpointResponse424 | PostServicesCronJobEndpointResponse500 | PostServicesCronJobEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesCronJobEndpointJsonBody | PostServicesCronJobEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesCronJobEndpointResponse400
    | PostServicesCronJobEndpointResponse401
    | PostServicesCronJobEndpointResponse403
    | PostServicesCronJobEndpointResponse404
    | PostServicesCronJobEndpointResponse405
    | PostServicesCronJobEndpointResponse406
    | PostServicesCronJobEndpointResponse409
    | PostServicesCronJobEndpointResponse415
    | PostServicesCronJobEndpointResponse422
    | PostServicesCronJobEndpointResponse424
    | PostServicesCronJobEndpointResponse500
    | PostServicesCronJobEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-post ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesCronJobEndpointJsonBody | Unset):
        body (PostServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesCronJobEndpointResponse400 | PostServicesCronJobEndpointResponse401 | PostServicesCronJobEndpointResponse403 | PostServicesCronJobEndpointResponse404 | PostServicesCronJobEndpointResponse405 | PostServicesCronJobEndpointResponse406 | PostServicesCronJobEndpointResponse409 | PostServicesCronJobEndpointResponse415 | PostServicesCronJobEndpointResponse422 | PostServicesCronJobEndpointResponse424 | PostServicesCronJobEndpointResponse500 | PostServicesCronJobEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesCronJobEndpointJsonBody | PostServicesCronJobEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesCronJobEndpointResponse400
    | PostServicesCronJobEndpointResponse401
    | PostServicesCronJobEndpointResponse403
    | PostServicesCronJobEndpointResponse404
    | PostServicesCronJobEndpointResponse405
    | PostServicesCronJobEndpointResponse406
    | PostServicesCronJobEndpointResponse409
    | PostServicesCronJobEndpointResponse415
    | PostServicesCronJobEndpointResponse422
    | PostServicesCronJobEndpointResponse424
    | PostServicesCronJobEndpointResponse500
    | PostServicesCronJobEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-post ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostServicesCronJobEndpointJsonBody | Unset):
        body (PostServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesCronJobEndpointResponse400 | PostServicesCronJobEndpointResponse401 | PostServicesCronJobEndpointResponse403 | PostServicesCronJobEndpointResponse404 | PostServicesCronJobEndpointResponse405 | PostServicesCronJobEndpointResponse406 | PostServicesCronJobEndpointResponse409 | PostServicesCronJobEndpointResponse415 | PostServicesCronJobEndpointResponse422 | PostServicesCronJobEndpointResponse424 | PostServicesCronJobEndpointResponse500 | PostServicesCronJobEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
