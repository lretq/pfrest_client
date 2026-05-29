from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_cron_job_endpoint_data_body import PatchServicesCronJobEndpointDataBody
from ...models.patch_services_cron_job_endpoint_json_body import PatchServicesCronJobEndpointJsonBody
from ...models.patch_services_cron_job_endpoint_response_400 import PatchServicesCronJobEndpointResponse400
from ...models.patch_services_cron_job_endpoint_response_401 import PatchServicesCronJobEndpointResponse401
from ...models.patch_services_cron_job_endpoint_response_403 import PatchServicesCronJobEndpointResponse403
from ...models.patch_services_cron_job_endpoint_response_404 import PatchServicesCronJobEndpointResponse404
from ...models.patch_services_cron_job_endpoint_response_405 import PatchServicesCronJobEndpointResponse405
from ...models.patch_services_cron_job_endpoint_response_406 import PatchServicesCronJobEndpointResponse406
from ...models.patch_services_cron_job_endpoint_response_409 import PatchServicesCronJobEndpointResponse409
from ...models.patch_services_cron_job_endpoint_response_415 import PatchServicesCronJobEndpointResponse415
from ...models.patch_services_cron_job_endpoint_response_422 import PatchServicesCronJobEndpointResponse422
from ...models.patch_services_cron_job_endpoint_response_424 import PatchServicesCronJobEndpointResponse424
from ...models.patch_services_cron_job_endpoint_response_500 import PatchServicesCronJobEndpointResponse500
from ...models.patch_services_cron_job_endpoint_response_503 import PatchServicesCronJobEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesCronJobEndpointJsonBody | PatchServicesCronJobEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/cron/job",
    }

    if isinstance(body, PatchServicesCronJobEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesCronJobEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesCronJobEndpointResponse400
    | PatchServicesCronJobEndpointResponse401
    | PatchServicesCronJobEndpointResponse403
    | PatchServicesCronJobEndpointResponse404
    | PatchServicesCronJobEndpointResponse405
    | PatchServicesCronJobEndpointResponse406
    | PatchServicesCronJobEndpointResponse409
    | PatchServicesCronJobEndpointResponse415
    | PatchServicesCronJobEndpointResponse422
    | PatchServicesCronJobEndpointResponse424
    | PatchServicesCronJobEndpointResponse500
    | PatchServicesCronJobEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesCronJobEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesCronJobEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesCronJobEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesCronJobEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesCronJobEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesCronJobEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesCronJobEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesCronJobEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesCronJobEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesCronJobEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesCronJobEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesCronJobEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesCronJobEndpointResponse400
    | PatchServicesCronJobEndpointResponse401
    | PatchServicesCronJobEndpointResponse403
    | PatchServicesCronJobEndpointResponse404
    | PatchServicesCronJobEndpointResponse405
    | PatchServicesCronJobEndpointResponse406
    | PatchServicesCronJobEndpointResponse409
    | PatchServicesCronJobEndpointResponse415
    | PatchServicesCronJobEndpointResponse422
    | PatchServicesCronJobEndpointResponse424
    | PatchServicesCronJobEndpointResponse500
    | PatchServicesCronJobEndpointResponse503
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
    body: PatchServicesCronJobEndpointJsonBody | PatchServicesCronJobEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesCronJobEndpointResponse400
    | PatchServicesCronJobEndpointResponse401
    | PatchServicesCronJobEndpointResponse403
    | PatchServicesCronJobEndpointResponse404
    | PatchServicesCronJobEndpointResponse405
    | PatchServicesCronJobEndpointResponse406
    | PatchServicesCronJobEndpointResponse409
    | PatchServicesCronJobEndpointResponse415
    | PatchServicesCronJobEndpointResponse422
    | PatchServicesCronJobEndpointResponse424
    | PatchServicesCronJobEndpointResponse500
    | PatchServicesCronJobEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-patch ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesCronJobEndpointJsonBody | Unset):
        body (PatchServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesCronJobEndpointResponse400 | PatchServicesCronJobEndpointResponse401 | PatchServicesCronJobEndpointResponse403 | PatchServicesCronJobEndpointResponse404 | PatchServicesCronJobEndpointResponse405 | PatchServicesCronJobEndpointResponse406 | PatchServicesCronJobEndpointResponse409 | PatchServicesCronJobEndpointResponse415 | PatchServicesCronJobEndpointResponse422 | PatchServicesCronJobEndpointResponse424 | PatchServicesCronJobEndpointResponse500 | PatchServicesCronJobEndpointResponse503]
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
    body: PatchServicesCronJobEndpointJsonBody | PatchServicesCronJobEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesCronJobEndpointResponse400
    | PatchServicesCronJobEndpointResponse401
    | PatchServicesCronJobEndpointResponse403
    | PatchServicesCronJobEndpointResponse404
    | PatchServicesCronJobEndpointResponse405
    | PatchServicesCronJobEndpointResponse406
    | PatchServicesCronJobEndpointResponse409
    | PatchServicesCronJobEndpointResponse415
    | PatchServicesCronJobEndpointResponse422
    | PatchServicesCronJobEndpointResponse424
    | PatchServicesCronJobEndpointResponse500
    | PatchServicesCronJobEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-patch ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesCronJobEndpointJsonBody | Unset):
        body (PatchServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesCronJobEndpointResponse400 | PatchServicesCronJobEndpointResponse401 | PatchServicesCronJobEndpointResponse403 | PatchServicesCronJobEndpointResponse404 | PatchServicesCronJobEndpointResponse405 | PatchServicesCronJobEndpointResponse406 | PatchServicesCronJobEndpointResponse409 | PatchServicesCronJobEndpointResponse415 | PatchServicesCronJobEndpointResponse422 | PatchServicesCronJobEndpointResponse424 | PatchServicesCronJobEndpointResponse500 | PatchServicesCronJobEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesCronJobEndpointJsonBody | PatchServicesCronJobEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesCronJobEndpointResponse400
    | PatchServicesCronJobEndpointResponse401
    | PatchServicesCronJobEndpointResponse403
    | PatchServicesCronJobEndpointResponse404
    | PatchServicesCronJobEndpointResponse405
    | PatchServicesCronJobEndpointResponse406
    | PatchServicesCronJobEndpointResponse409
    | PatchServicesCronJobEndpointResponse415
    | PatchServicesCronJobEndpointResponse422
    | PatchServicesCronJobEndpointResponse424
    | PatchServicesCronJobEndpointResponse500
    | PatchServicesCronJobEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-patch ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesCronJobEndpointJsonBody | Unset):
        body (PatchServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesCronJobEndpointResponse400 | PatchServicesCronJobEndpointResponse401 | PatchServicesCronJobEndpointResponse403 | PatchServicesCronJobEndpointResponse404 | PatchServicesCronJobEndpointResponse405 | PatchServicesCronJobEndpointResponse406 | PatchServicesCronJobEndpointResponse409 | PatchServicesCronJobEndpointResponse415 | PatchServicesCronJobEndpointResponse422 | PatchServicesCronJobEndpointResponse424 | PatchServicesCronJobEndpointResponse500 | PatchServicesCronJobEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesCronJobEndpointJsonBody | PatchServicesCronJobEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesCronJobEndpointResponse400
    | PatchServicesCronJobEndpointResponse401
    | PatchServicesCronJobEndpointResponse403
    | PatchServicesCronJobEndpointResponse404
    | PatchServicesCronJobEndpointResponse405
    | PatchServicesCronJobEndpointResponse406
    | PatchServicesCronJobEndpointResponse409
    | PatchServicesCronJobEndpointResponse415
    | PatchServicesCronJobEndpointResponse422
    | PatchServicesCronJobEndpointResponse424
    | PatchServicesCronJobEndpointResponse500
    | PatchServicesCronJobEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-patch ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesCronJobEndpointJsonBody | Unset):
        body (PatchServicesCronJobEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesCronJobEndpointResponse400 | PatchServicesCronJobEndpointResponse401 | PatchServicesCronJobEndpointResponse403 | PatchServicesCronJobEndpointResponse404 | PatchServicesCronJobEndpointResponse405 | PatchServicesCronJobEndpointResponse406 | PatchServicesCronJobEndpointResponse409 | PatchServicesCronJobEndpointResponse415 | PatchServicesCronJobEndpointResponse422 | PatchServicesCronJobEndpointResponse424 | PatchServicesCronJobEndpointResponse500 | PatchServicesCronJobEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
