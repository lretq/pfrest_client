from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_bind_zone_record_endpoint_response_400 import (
    DeleteServicesBINDZoneRecordEndpointResponse400,
)
from ...models.delete_services_bind_zone_record_endpoint_response_401 import (
    DeleteServicesBINDZoneRecordEndpointResponse401,
)
from ...models.delete_services_bind_zone_record_endpoint_response_403 import (
    DeleteServicesBINDZoneRecordEndpointResponse403,
)
from ...models.delete_services_bind_zone_record_endpoint_response_404 import (
    DeleteServicesBINDZoneRecordEndpointResponse404,
)
from ...models.delete_services_bind_zone_record_endpoint_response_405 import (
    DeleteServicesBINDZoneRecordEndpointResponse405,
)
from ...models.delete_services_bind_zone_record_endpoint_response_406 import (
    DeleteServicesBINDZoneRecordEndpointResponse406,
)
from ...models.delete_services_bind_zone_record_endpoint_response_409 import (
    DeleteServicesBINDZoneRecordEndpointResponse409,
)
from ...models.delete_services_bind_zone_record_endpoint_response_415 import (
    DeleteServicesBINDZoneRecordEndpointResponse415,
)
from ...models.delete_services_bind_zone_record_endpoint_response_422 import (
    DeleteServicesBINDZoneRecordEndpointResponse422,
)
from ...models.delete_services_bind_zone_record_endpoint_response_424 import (
    DeleteServicesBINDZoneRecordEndpointResponse424,
)
from ...models.delete_services_bind_zone_record_endpoint_response_500 import (
    DeleteServicesBINDZoneRecordEndpointResponse500,
)
from ...models.delete_services_bind_zone_record_endpoint_response_503 import (
    DeleteServicesBINDZoneRecordEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/bind/zone/record",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesBINDZoneRecordEndpointResponse400
    | DeleteServicesBINDZoneRecordEndpointResponse401
    | DeleteServicesBINDZoneRecordEndpointResponse403
    | DeleteServicesBINDZoneRecordEndpointResponse404
    | DeleteServicesBINDZoneRecordEndpointResponse405
    | DeleteServicesBINDZoneRecordEndpointResponse406
    | DeleteServicesBINDZoneRecordEndpointResponse409
    | DeleteServicesBINDZoneRecordEndpointResponse415
    | DeleteServicesBINDZoneRecordEndpointResponse422
    | DeleteServicesBINDZoneRecordEndpointResponse424
    | DeleteServicesBINDZoneRecordEndpointResponse500
    | DeleteServicesBINDZoneRecordEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesBINDZoneRecordEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesBINDZoneRecordEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesBINDZoneRecordEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesBINDZoneRecordEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesBINDZoneRecordEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesBINDZoneRecordEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesBINDZoneRecordEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesBINDZoneRecordEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesBINDZoneRecordEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesBINDZoneRecordEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesBINDZoneRecordEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesBINDZoneRecordEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesBINDZoneRecordEndpointResponse400
    | DeleteServicesBINDZoneRecordEndpointResponse401
    | DeleteServicesBINDZoneRecordEndpointResponse403
    | DeleteServicesBINDZoneRecordEndpointResponse404
    | DeleteServicesBINDZoneRecordEndpointResponse405
    | DeleteServicesBINDZoneRecordEndpointResponse406
    | DeleteServicesBINDZoneRecordEndpointResponse409
    | DeleteServicesBINDZoneRecordEndpointResponse415
    | DeleteServicesBINDZoneRecordEndpointResponse422
    | DeleteServicesBINDZoneRecordEndpointResponse424
    | DeleteServicesBINDZoneRecordEndpointResponse500
    | DeleteServicesBINDZoneRecordEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesBINDZoneRecordEndpointResponse400
    | DeleteServicesBINDZoneRecordEndpointResponse401
    | DeleteServicesBINDZoneRecordEndpointResponse403
    | DeleteServicesBINDZoneRecordEndpointResponse404
    | DeleteServicesBINDZoneRecordEndpointResponse405
    | DeleteServicesBINDZoneRecordEndpointResponse406
    | DeleteServicesBINDZoneRecordEndpointResponse409
    | DeleteServicesBINDZoneRecordEndpointResponse415
    | DeleteServicesBINDZoneRecordEndpointResponse422
    | DeleteServicesBINDZoneRecordEndpointResponse424
    | DeleteServicesBINDZoneRecordEndpointResponse500
    | DeleteServicesBINDZoneRecordEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing BIND Zone Record.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZoneRecord<br>**Parent model**: BINDZone<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-zone-record-delete ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesBINDZoneRecordEndpointResponse400 | DeleteServicesBINDZoneRecordEndpointResponse401 | DeleteServicesBINDZoneRecordEndpointResponse403 | DeleteServicesBINDZoneRecordEndpointResponse404 | DeleteServicesBINDZoneRecordEndpointResponse405 | DeleteServicesBINDZoneRecordEndpointResponse406 | DeleteServicesBINDZoneRecordEndpointResponse409 | DeleteServicesBINDZoneRecordEndpointResponse415 | DeleteServicesBINDZoneRecordEndpointResponse422 | DeleteServicesBINDZoneRecordEndpointResponse424 | DeleteServicesBINDZoneRecordEndpointResponse500 | DeleteServicesBINDZoneRecordEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesBINDZoneRecordEndpointResponse400
    | DeleteServicesBINDZoneRecordEndpointResponse401
    | DeleteServicesBINDZoneRecordEndpointResponse403
    | DeleteServicesBINDZoneRecordEndpointResponse404
    | DeleteServicesBINDZoneRecordEndpointResponse405
    | DeleteServicesBINDZoneRecordEndpointResponse406
    | DeleteServicesBINDZoneRecordEndpointResponse409
    | DeleteServicesBINDZoneRecordEndpointResponse415
    | DeleteServicesBINDZoneRecordEndpointResponse422
    | DeleteServicesBINDZoneRecordEndpointResponse424
    | DeleteServicesBINDZoneRecordEndpointResponse500
    | DeleteServicesBINDZoneRecordEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing BIND Zone Record.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZoneRecord<br>**Parent model**: BINDZone<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-zone-record-delete ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesBINDZoneRecordEndpointResponse400 | DeleteServicesBINDZoneRecordEndpointResponse401 | DeleteServicesBINDZoneRecordEndpointResponse403 | DeleteServicesBINDZoneRecordEndpointResponse404 | DeleteServicesBINDZoneRecordEndpointResponse405 | DeleteServicesBINDZoneRecordEndpointResponse406 | DeleteServicesBINDZoneRecordEndpointResponse409 | DeleteServicesBINDZoneRecordEndpointResponse415 | DeleteServicesBINDZoneRecordEndpointResponse422 | DeleteServicesBINDZoneRecordEndpointResponse424 | DeleteServicesBINDZoneRecordEndpointResponse500 | DeleteServicesBINDZoneRecordEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesBINDZoneRecordEndpointResponse400
    | DeleteServicesBINDZoneRecordEndpointResponse401
    | DeleteServicesBINDZoneRecordEndpointResponse403
    | DeleteServicesBINDZoneRecordEndpointResponse404
    | DeleteServicesBINDZoneRecordEndpointResponse405
    | DeleteServicesBINDZoneRecordEndpointResponse406
    | DeleteServicesBINDZoneRecordEndpointResponse409
    | DeleteServicesBINDZoneRecordEndpointResponse415
    | DeleteServicesBINDZoneRecordEndpointResponse422
    | DeleteServicesBINDZoneRecordEndpointResponse424
    | DeleteServicesBINDZoneRecordEndpointResponse500
    | DeleteServicesBINDZoneRecordEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing BIND Zone Record.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZoneRecord<br>**Parent model**: BINDZone<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-zone-record-delete ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesBINDZoneRecordEndpointResponse400 | DeleteServicesBINDZoneRecordEndpointResponse401 | DeleteServicesBINDZoneRecordEndpointResponse403 | DeleteServicesBINDZoneRecordEndpointResponse404 | DeleteServicesBINDZoneRecordEndpointResponse405 | DeleteServicesBINDZoneRecordEndpointResponse406 | DeleteServicesBINDZoneRecordEndpointResponse409 | DeleteServicesBINDZoneRecordEndpointResponse415 | DeleteServicesBINDZoneRecordEndpointResponse422 | DeleteServicesBINDZoneRecordEndpointResponse424 | DeleteServicesBINDZoneRecordEndpointResponse500 | DeleteServicesBINDZoneRecordEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesBINDZoneRecordEndpointResponse400
    | DeleteServicesBINDZoneRecordEndpointResponse401
    | DeleteServicesBINDZoneRecordEndpointResponse403
    | DeleteServicesBINDZoneRecordEndpointResponse404
    | DeleteServicesBINDZoneRecordEndpointResponse405
    | DeleteServicesBINDZoneRecordEndpointResponse406
    | DeleteServicesBINDZoneRecordEndpointResponse409
    | DeleteServicesBINDZoneRecordEndpointResponse415
    | DeleteServicesBINDZoneRecordEndpointResponse422
    | DeleteServicesBINDZoneRecordEndpointResponse424
    | DeleteServicesBINDZoneRecordEndpointResponse500
    | DeleteServicesBINDZoneRecordEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing BIND Zone Record.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZoneRecord<br>**Parent model**: BINDZone<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-zone-record-delete ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesBINDZoneRecordEndpointResponse400 | DeleteServicesBINDZoneRecordEndpointResponse401 | DeleteServicesBINDZoneRecordEndpointResponse403 | DeleteServicesBINDZoneRecordEndpointResponse404 | DeleteServicesBINDZoneRecordEndpointResponse405 | DeleteServicesBINDZoneRecordEndpointResponse406 | DeleteServicesBINDZoneRecordEndpointResponse409 | DeleteServicesBINDZoneRecordEndpointResponse415 | DeleteServicesBINDZoneRecordEndpointResponse422 | DeleteServicesBINDZoneRecordEndpointResponse424 | DeleteServicesBINDZoneRecordEndpointResponse500 | DeleteServicesBINDZoneRecordEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
