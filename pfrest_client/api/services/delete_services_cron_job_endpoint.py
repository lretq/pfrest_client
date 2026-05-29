from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_cron_job_endpoint_response_400 import DeleteServicesCronJobEndpointResponse400
from ...models.delete_services_cron_job_endpoint_response_401 import DeleteServicesCronJobEndpointResponse401
from ...models.delete_services_cron_job_endpoint_response_403 import DeleteServicesCronJobEndpointResponse403
from ...models.delete_services_cron_job_endpoint_response_404 import DeleteServicesCronJobEndpointResponse404
from ...models.delete_services_cron_job_endpoint_response_405 import DeleteServicesCronJobEndpointResponse405
from ...models.delete_services_cron_job_endpoint_response_406 import DeleteServicesCronJobEndpointResponse406
from ...models.delete_services_cron_job_endpoint_response_409 import DeleteServicesCronJobEndpointResponse409
from ...models.delete_services_cron_job_endpoint_response_415 import DeleteServicesCronJobEndpointResponse415
from ...models.delete_services_cron_job_endpoint_response_422 import DeleteServicesCronJobEndpointResponse422
from ...models.delete_services_cron_job_endpoint_response_424 import DeleteServicesCronJobEndpointResponse424
from ...models.delete_services_cron_job_endpoint_response_500 import DeleteServicesCronJobEndpointResponse500
from ...models.delete_services_cron_job_endpoint_response_503 import DeleteServicesCronJobEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/cron/job",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesCronJobEndpointResponse400
    | DeleteServicesCronJobEndpointResponse401
    | DeleteServicesCronJobEndpointResponse403
    | DeleteServicesCronJobEndpointResponse404
    | DeleteServicesCronJobEndpointResponse405
    | DeleteServicesCronJobEndpointResponse406
    | DeleteServicesCronJobEndpointResponse409
    | DeleteServicesCronJobEndpointResponse415
    | DeleteServicesCronJobEndpointResponse422
    | DeleteServicesCronJobEndpointResponse424
    | DeleteServicesCronJobEndpointResponse500
    | DeleteServicesCronJobEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesCronJobEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesCronJobEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesCronJobEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesCronJobEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesCronJobEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesCronJobEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesCronJobEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesCronJobEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesCronJobEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesCronJobEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesCronJobEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesCronJobEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesCronJobEndpointResponse400
    | DeleteServicesCronJobEndpointResponse401
    | DeleteServicesCronJobEndpointResponse403
    | DeleteServicesCronJobEndpointResponse404
    | DeleteServicesCronJobEndpointResponse405
    | DeleteServicesCronJobEndpointResponse406
    | DeleteServicesCronJobEndpointResponse409
    | DeleteServicesCronJobEndpointResponse415
    | DeleteServicesCronJobEndpointResponse422
    | DeleteServicesCronJobEndpointResponse424
    | DeleteServicesCronJobEndpointResponse500
    | DeleteServicesCronJobEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteServicesCronJobEndpointResponse400
    | DeleteServicesCronJobEndpointResponse401
    | DeleteServicesCronJobEndpointResponse403
    | DeleteServicesCronJobEndpointResponse404
    | DeleteServicesCronJobEndpointResponse405
    | DeleteServicesCronJobEndpointResponse406
    | DeleteServicesCronJobEndpointResponse409
    | DeleteServicesCronJobEndpointResponse415
    | DeleteServicesCronJobEndpointResponse422
    | DeleteServicesCronJobEndpointResponse424
    | DeleteServicesCronJobEndpointResponse500
    | DeleteServicesCronJobEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-delete ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesCronJobEndpointResponse400 | DeleteServicesCronJobEndpointResponse401 | DeleteServicesCronJobEndpointResponse403 | DeleteServicesCronJobEndpointResponse404 | DeleteServicesCronJobEndpointResponse405 | DeleteServicesCronJobEndpointResponse406 | DeleteServicesCronJobEndpointResponse409 | DeleteServicesCronJobEndpointResponse415 | DeleteServicesCronJobEndpointResponse422 | DeleteServicesCronJobEndpointResponse424 | DeleteServicesCronJobEndpointResponse500 | DeleteServicesCronJobEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesCronJobEndpointResponse400
    | DeleteServicesCronJobEndpointResponse401
    | DeleteServicesCronJobEndpointResponse403
    | DeleteServicesCronJobEndpointResponse404
    | DeleteServicesCronJobEndpointResponse405
    | DeleteServicesCronJobEndpointResponse406
    | DeleteServicesCronJobEndpointResponse409
    | DeleteServicesCronJobEndpointResponse415
    | DeleteServicesCronJobEndpointResponse422
    | DeleteServicesCronJobEndpointResponse424
    | DeleteServicesCronJobEndpointResponse500
    | DeleteServicesCronJobEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-delete ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesCronJobEndpointResponse400 | DeleteServicesCronJobEndpointResponse401 | DeleteServicesCronJobEndpointResponse403 | DeleteServicesCronJobEndpointResponse404 | DeleteServicesCronJobEndpointResponse405 | DeleteServicesCronJobEndpointResponse406 | DeleteServicesCronJobEndpointResponse409 | DeleteServicesCronJobEndpointResponse415 | DeleteServicesCronJobEndpointResponse422 | DeleteServicesCronJobEndpointResponse424 | DeleteServicesCronJobEndpointResponse500 | DeleteServicesCronJobEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteServicesCronJobEndpointResponse400
    | DeleteServicesCronJobEndpointResponse401
    | DeleteServicesCronJobEndpointResponse403
    | DeleteServicesCronJobEndpointResponse404
    | DeleteServicesCronJobEndpointResponse405
    | DeleteServicesCronJobEndpointResponse406
    | DeleteServicesCronJobEndpointResponse409
    | DeleteServicesCronJobEndpointResponse415
    | DeleteServicesCronJobEndpointResponse422
    | DeleteServicesCronJobEndpointResponse424
    | DeleteServicesCronJobEndpointResponse500
    | DeleteServicesCronJobEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-delete ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesCronJobEndpointResponse400 | DeleteServicesCronJobEndpointResponse401 | DeleteServicesCronJobEndpointResponse403 | DeleteServicesCronJobEndpointResponse404 | DeleteServicesCronJobEndpointResponse405 | DeleteServicesCronJobEndpointResponse406 | DeleteServicesCronJobEndpointResponse409 | DeleteServicesCronJobEndpointResponse415 | DeleteServicesCronJobEndpointResponse422 | DeleteServicesCronJobEndpointResponse424 | DeleteServicesCronJobEndpointResponse500 | DeleteServicesCronJobEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesCronJobEndpointResponse400
    | DeleteServicesCronJobEndpointResponse401
    | DeleteServicesCronJobEndpointResponse403
    | DeleteServicesCronJobEndpointResponse404
    | DeleteServicesCronJobEndpointResponse405
    | DeleteServicesCronJobEndpointResponse406
    | DeleteServicesCronJobEndpointResponse409
    | DeleteServicesCronJobEndpointResponse415
    | DeleteServicesCronJobEndpointResponse422
    | DeleteServicesCronJobEndpointResponse424
    | DeleteServicesCronJobEndpointResponse500
    | DeleteServicesCronJobEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Cron Job.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CronJob<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-cron-job-delete ]<br>**Required packages**: [ pfSense-pkg-
    Cron ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesCronJobEndpointResponse400 | DeleteServicesCronJobEndpointResponse401 | DeleteServicesCronJobEndpointResponse403 | DeleteServicesCronJobEndpointResponse404 | DeleteServicesCronJobEndpointResponse405 | DeleteServicesCronJobEndpointResponse406 | DeleteServicesCronJobEndpointResponse409 | DeleteServicesCronJobEndpointResponse415 | DeleteServicesCronJobEndpointResponse422 | DeleteServicesCronJobEndpointResponse424 | DeleteServicesCronJobEndpointResponse500 | DeleteServicesCronJobEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
