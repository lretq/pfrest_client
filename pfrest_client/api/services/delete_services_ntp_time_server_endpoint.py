from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ntp_time_server_endpoint_response_400 import (
    DeleteServicesNTPTimeServerEndpointResponse400,
)
from ...models.delete_services_ntp_time_server_endpoint_response_401 import (
    DeleteServicesNTPTimeServerEndpointResponse401,
)
from ...models.delete_services_ntp_time_server_endpoint_response_403 import (
    DeleteServicesNTPTimeServerEndpointResponse403,
)
from ...models.delete_services_ntp_time_server_endpoint_response_404 import (
    DeleteServicesNTPTimeServerEndpointResponse404,
)
from ...models.delete_services_ntp_time_server_endpoint_response_405 import (
    DeleteServicesNTPTimeServerEndpointResponse405,
)
from ...models.delete_services_ntp_time_server_endpoint_response_406 import (
    DeleteServicesNTPTimeServerEndpointResponse406,
)
from ...models.delete_services_ntp_time_server_endpoint_response_409 import (
    DeleteServicesNTPTimeServerEndpointResponse409,
)
from ...models.delete_services_ntp_time_server_endpoint_response_415 import (
    DeleteServicesNTPTimeServerEndpointResponse415,
)
from ...models.delete_services_ntp_time_server_endpoint_response_422 import (
    DeleteServicesNTPTimeServerEndpointResponse422,
)
from ...models.delete_services_ntp_time_server_endpoint_response_424 import (
    DeleteServicesNTPTimeServerEndpointResponse424,
)
from ...models.delete_services_ntp_time_server_endpoint_response_500 import (
    DeleteServicesNTPTimeServerEndpointResponse500,
)
from ...models.delete_services_ntp_time_server_endpoint_response_503 import (
    DeleteServicesNTPTimeServerEndpointResponse503,
)
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
        "url": "/api/v2/services/ntp/time_server",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesNTPTimeServerEndpointResponse400
    | DeleteServicesNTPTimeServerEndpointResponse401
    | DeleteServicesNTPTimeServerEndpointResponse403
    | DeleteServicesNTPTimeServerEndpointResponse404
    | DeleteServicesNTPTimeServerEndpointResponse405
    | DeleteServicesNTPTimeServerEndpointResponse406
    | DeleteServicesNTPTimeServerEndpointResponse409
    | DeleteServicesNTPTimeServerEndpointResponse415
    | DeleteServicesNTPTimeServerEndpointResponse422
    | DeleteServicesNTPTimeServerEndpointResponse424
    | DeleteServicesNTPTimeServerEndpointResponse500
    | DeleteServicesNTPTimeServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesNTPTimeServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesNTPTimeServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesNTPTimeServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesNTPTimeServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesNTPTimeServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesNTPTimeServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesNTPTimeServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesNTPTimeServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesNTPTimeServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesNTPTimeServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesNTPTimeServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesNTPTimeServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesNTPTimeServerEndpointResponse400
    | DeleteServicesNTPTimeServerEndpointResponse401
    | DeleteServicesNTPTimeServerEndpointResponse403
    | DeleteServicesNTPTimeServerEndpointResponse404
    | DeleteServicesNTPTimeServerEndpointResponse405
    | DeleteServicesNTPTimeServerEndpointResponse406
    | DeleteServicesNTPTimeServerEndpointResponse409
    | DeleteServicesNTPTimeServerEndpointResponse415
    | DeleteServicesNTPTimeServerEndpointResponse422
    | DeleteServicesNTPTimeServerEndpointResponse424
    | DeleteServicesNTPTimeServerEndpointResponse500
    | DeleteServicesNTPTimeServerEndpointResponse503
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
    DeleteServicesNTPTimeServerEndpointResponse400
    | DeleteServicesNTPTimeServerEndpointResponse401
    | DeleteServicesNTPTimeServerEndpointResponse403
    | DeleteServicesNTPTimeServerEndpointResponse404
    | DeleteServicesNTPTimeServerEndpointResponse405
    | DeleteServicesNTPTimeServerEndpointResponse406
    | DeleteServicesNTPTimeServerEndpointResponse409
    | DeleteServicesNTPTimeServerEndpointResponse415
    | DeleteServicesNTPTimeServerEndpointResponse422
    | DeleteServicesNTPTimeServerEndpointResponse424
    | DeleteServicesNTPTimeServerEndpointResponse500
    | DeleteServicesNTPTimeServerEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesNTPTimeServerEndpointResponse400 | DeleteServicesNTPTimeServerEndpointResponse401 | DeleteServicesNTPTimeServerEndpointResponse403 | DeleteServicesNTPTimeServerEndpointResponse404 | DeleteServicesNTPTimeServerEndpointResponse405 | DeleteServicesNTPTimeServerEndpointResponse406 | DeleteServicesNTPTimeServerEndpointResponse409 | DeleteServicesNTPTimeServerEndpointResponse415 | DeleteServicesNTPTimeServerEndpointResponse422 | DeleteServicesNTPTimeServerEndpointResponse424 | DeleteServicesNTPTimeServerEndpointResponse500 | DeleteServicesNTPTimeServerEndpointResponse503]
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
    DeleteServicesNTPTimeServerEndpointResponse400
    | DeleteServicesNTPTimeServerEndpointResponse401
    | DeleteServicesNTPTimeServerEndpointResponse403
    | DeleteServicesNTPTimeServerEndpointResponse404
    | DeleteServicesNTPTimeServerEndpointResponse405
    | DeleteServicesNTPTimeServerEndpointResponse406
    | DeleteServicesNTPTimeServerEndpointResponse409
    | DeleteServicesNTPTimeServerEndpointResponse415
    | DeleteServicesNTPTimeServerEndpointResponse422
    | DeleteServicesNTPTimeServerEndpointResponse424
    | DeleteServicesNTPTimeServerEndpointResponse500
    | DeleteServicesNTPTimeServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesNTPTimeServerEndpointResponse400 | DeleteServicesNTPTimeServerEndpointResponse401 | DeleteServicesNTPTimeServerEndpointResponse403 | DeleteServicesNTPTimeServerEndpointResponse404 | DeleteServicesNTPTimeServerEndpointResponse405 | DeleteServicesNTPTimeServerEndpointResponse406 | DeleteServicesNTPTimeServerEndpointResponse409 | DeleteServicesNTPTimeServerEndpointResponse415 | DeleteServicesNTPTimeServerEndpointResponse422 | DeleteServicesNTPTimeServerEndpointResponse424 | DeleteServicesNTPTimeServerEndpointResponse500 | DeleteServicesNTPTimeServerEndpointResponse503
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
    DeleteServicesNTPTimeServerEndpointResponse400
    | DeleteServicesNTPTimeServerEndpointResponse401
    | DeleteServicesNTPTimeServerEndpointResponse403
    | DeleteServicesNTPTimeServerEndpointResponse404
    | DeleteServicesNTPTimeServerEndpointResponse405
    | DeleteServicesNTPTimeServerEndpointResponse406
    | DeleteServicesNTPTimeServerEndpointResponse409
    | DeleteServicesNTPTimeServerEndpointResponse415
    | DeleteServicesNTPTimeServerEndpointResponse422
    | DeleteServicesNTPTimeServerEndpointResponse424
    | DeleteServicesNTPTimeServerEndpointResponse500
    | DeleteServicesNTPTimeServerEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesNTPTimeServerEndpointResponse400 | DeleteServicesNTPTimeServerEndpointResponse401 | DeleteServicesNTPTimeServerEndpointResponse403 | DeleteServicesNTPTimeServerEndpointResponse404 | DeleteServicesNTPTimeServerEndpointResponse405 | DeleteServicesNTPTimeServerEndpointResponse406 | DeleteServicesNTPTimeServerEndpointResponse409 | DeleteServicesNTPTimeServerEndpointResponse415 | DeleteServicesNTPTimeServerEndpointResponse422 | DeleteServicesNTPTimeServerEndpointResponse424 | DeleteServicesNTPTimeServerEndpointResponse500 | DeleteServicesNTPTimeServerEndpointResponse503]
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
    DeleteServicesNTPTimeServerEndpointResponse400
    | DeleteServicesNTPTimeServerEndpointResponse401
    | DeleteServicesNTPTimeServerEndpointResponse403
    | DeleteServicesNTPTimeServerEndpointResponse404
    | DeleteServicesNTPTimeServerEndpointResponse405
    | DeleteServicesNTPTimeServerEndpointResponse406
    | DeleteServicesNTPTimeServerEndpointResponse409
    | DeleteServicesNTPTimeServerEndpointResponse415
    | DeleteServicesNTPTimeServerEndpointResponse422
    | DeleteServicesNTPTimeServerEndpointResponse424
    | DeleteServicesNTPTimeServerEndpointResponse500
    | DeleteServicesNTPTimeServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesNTPTimeServerEndpointResponse400 | DeleteServicesNTPTimeServerEndpointResponse401 | DeleteServicesNTPTimeServerEndpointResponse403 | DeleteServicesNTPTimeServerEndpointResponse404 | DeleteServicesNTPTimeServerEndpointResponse405 | DeleteServicesNTPTimeServerEndpointResponse406 | DeleteServicesNTPTimeServerEndpointResponse409 | DeleteServicesNTPTimeServerEndpointResponse415 | DeleteServicesNTPTimeServerEndpointResponse422 | DeleteServicesNTPTimeServerEndpointResponse424 | DeleteServicesNTPTimeServerEndpointResponse500 | DeleteServicesNTPTimeServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
