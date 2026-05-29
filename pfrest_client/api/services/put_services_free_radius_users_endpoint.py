from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_free_radius_users_endpoint_data_body_item import (
    PutServicesFreeRADIUSUsersEndpointDataBodyItem,
)
from ...models.put_services_free_radius_users_endpoint_json_body_item import (
    PutServicesFreeRADIUSUsersEndpointJsonBodyItem,
)
from ...models.put_services_free_radius_users_endpoint_response_400 import PutServicesFreeRADIUSUsersEndpointResponse400
from ...models.put_services_free_radius_users_endpoint_response_401 import PutServicesFreeRADIUSUsersEndpointResponse401
from ...models.put_services_free_radius_users_endpoint_response_403 import PutServicesFreeRADIUSUsersEndpointResponse403
from ...models.put_services_free_radius_users_endpoint_response_404 import PutServicesFreeRADIUSUsersEndpointResponse404
from ...models.put_services_free_radius_users_endpoint_response_405 import PutServicesFreeRADIUSUsersEndpointResponse405
from ...models.put_services_free_radius_users_endpoint_response_406 import PutServicesFreeRADIUSUsersEndpointResponse406
from ...models.put_services_free_radius_users_endpoint_response_409 import PutServicesFreeRADIUSUsersEndpointResponse409
from ...models.put_services_free_radius_users_endpoint_response_415 import PutServicesFreeRADIUSUsersEndpointResponse415
from ...models.put_services_free_radius_users_endpoint_response_422 import PutServicesFreeRADIUSUsersEndpointResponse422
from ...models.put_services_free_radius_users_endpoint_response_424 import PutServicesFreeRADIUSUsersEndpointResponse424
from ...models.put_services_free_radius_users_endpoint_response_500 import PutServicesFreeRADIUSUsersEndpointResponse500
from ...models.put_services_free_radius_users_endpoint_response_503 import PutServicesFreeRADIUSUsersEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSUsersEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/freeradius/users",
    }

    if isinstance(body, list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesFreeRADIUSUsersEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesFreeRADIUSUsersEndpointResponse400
    | PutServicesFreeRADIUSUsersEndpointResponse401
    | PutServicesFreeRADIUSUsersEndpointResponse403
    | PutServicesFreeRADIUSUsersEndpointResponse404
    | PutServicesFreeRADIUSUsersEndpointResponse405
    | PutServicesFreeRADIUSUsersEndpointResponse406
    | PutServicesFreeRADIUSUsersEndpointResponse409
    | PutServicesFreeRADIUSUsersEndpointResponse415
    | PutServicesFreeRADIUSUsersEndpointResponse422
    | PutServicesFreeRADIUSUsersEndpointResponse424
    | PutServicesFreeRADIUSUsersEndpointResponse500
    | PutServicesFreeRADIUSUsersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesFreeRADIUSUsersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesFreeRADIUSUsersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesFreeRADIUSUsersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesFreeRADIUSUsersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesFreeRADIUSUsersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesFreeRADIUSUsersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesFreeRADIUSUsersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesFreeRADIUSUsersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesFreeRADIUSUsersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesFreeRADIUSUsersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesFreeRADIUSUsersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesFreeRADIUSUsersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesFreeRADIUSUsersEndpointResponse400
    | PutServicesFreeRADIUSUsersEndpointResponse401
    | PutServicesFreeRADIUSUsersEndpointResponse403
    | PutServicesFreeRADIUSUsersEndpointResponse404
    | PutServicesFreeRADIUSUsersEndpointResponse405
    | PutServicesFreeRADIUSUsersEndpointResponse406
    | PutServicesFreeRADIUSUsersEndpointResponse409
    | PutServicesFreeRADIUSUsersEndpointResponse415
    | PutServicesFreeRADIUSUsersEndpointResponse422
    | PutServicesFreeRADIUSUsersEndpointResponse424
    | PutServicesFreeRADIUSUsersEndpointResponse500
    | PutServicesFreeRADIUSUsersEndpointResponse503
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
    body: list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSUsersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesFreeRADIUSUsersEndpointResponse400
    | PutServicesFreeRADIUSUsersEndpointResponse401
    | PutServicesFreeRADIUSUsersEndpointResponse403
    | PutServicesFreeRADIUSUsersEndpointResponse404
    | PutServicesFreeRADIUSUsersEndpointResponse405
    | PutServicesFreeRADIUSUsersEndpointResponse406
    | PutServicesFreeRADIUSUsersEndpointResponse409
    | PutServicesFreeRADIUSUsersEndpointResponse415
    | PutServicesFreeRADIUSUsersEndpointResponse422
    | PutServicesFreeRADIUSUsersEndpointResponse424
    | PutServicesFreeRADIUSUsersEndpointResponse500
    | PutServicesFreeRADIUSUsersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSUsersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesFreeRADIUSUsersEndpointResponse400 | PutServicesFreeRADIUSUsersEndpointResponse401 | PutServicesFreeRADIUSUsersEndpointResponse403 | PutServicesFreeRADIUSUsersEndpointResponse404 | PutServicesFreeRADIUSUsersEndpointResponse405 | PutServicesFreeRADIUSUsersEndpointResponse406 | PutServicesFreeRADIUSUsersEndpointResponse409 | PutServicesFreeRADIUSUsersEndpointResponse415 | PutServicesFreeRADIUSUsersEndpointResponse422 | PutServicesFreeRADIUSUsersEndpointResponse424 | PutServicesFreeRADIUSUsersEndpointResponse500 | PutServicesFreeRADIUSUsersEndpointResponse503]
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
    body: list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSUsersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesFreeRADIUSUsersEndpointResponse400
    | PutServicesFreeRADIUSUsersEndpointResponse401
    | PutServicesFreeRADIUSUsersEndpointResponse403
    | PutServicesFreeRADIUSUsersEndpointResponse404
    | PutServicesFreeRADIUSUsersEndpointResponse405
    | PutServicesFreeRADIUSUsersEndpointResponse406
    | PutServicesFreeRADIUSUsersEndpointResponse409
    | PutServicesFreeRADIUSUsersEndpointResponse415
    | PutServicesFreeRADIUSUsersEndpointResponse422
    | PutServicesFreeRADIUSUsersEndpointResponse424
    | PutServicesFreeRADIUSUsersEndpointResponse500
    | PutServicesFreeRADIUSUsersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSUsersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesFreeRADIUSUsersEndpointResponse400 | PutServicesFreeRADIUSUsersEndpointResponse401 | PutServicesFreeRADIUSUsersEndpointResponse403 | PutServicesFreeRADIUSUsersEndpointResponse404 | PutServicesFreeRADIUSUsersEndpointResponse405 | PutServicesFreeRADIUSUsersEndpointResponse406 | PutServicesFreeRADIUSUsersEndpointResponse409 | PutServicesFreeRADIUSUsersEndpointResponse415 | PutServicesFreeRADIUSUsersEndpointResponse422 | PutServicesFreeRADIUSUsersEndpointResponse424 | PutServicesFreeRADIUSUsersEndpointResponse500 | PutServicesFreeRADIUSUsersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSUsersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesFreeRADIUSUsersEndpointResponse400
    | PutServicesFreeRADIUSUsersEndpointResponse401
    | PutServicesFreeRADIUSUsersEndpointResponse403
    | PutServicesFreeRADIUSUsersEndpointResponse404
    | PutServicesFreeRADIUSUsersEndpointResponse405
    | PutServicesFreeRADIUSUsersEndpointResponse406
    | PutServicesFreeRADIUSUsersEndpointResponse409
    | PutServicesFreeRADIUSUsersEndpointResponse415
    | PutServicesFreeRADIUSUsersEndpointResponse422
    | PutServicesFreeRADIUSUsersEndpointResponse424
    | PutServicesFreeRADIUSUsersEndpointResponse500
    | PutServicesFreeRADIUSUsersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSUsersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesFreeRADIUSUsersEndpointResponse400 | PutServicesFreeRADIUSUsersEndpointResponse401 | PutServicesFreeRADIUSUsersEndpointResponse403 | PutServicesFreeRADIUSUsersEndpointResponse404 | PutServicesFreeRADIUSUsersEndpointResponse405 | PutServicesFreeRADIUSUsersEndpointResponse406 | PutServicesFreeRADIUSUsersEndpointResponse409 | PutServicesFreeRADIUSUsersEndpointResponse415 | PutServicesFreeRADIUSUsersEndpointResponse422 | PutServicesFreeRADIUSUsersEndpointResponse424 | PutServicesFreeRADIUSUsersEndpointResponse500 | PutServicesFreeRADIUSUsersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSUsersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesFreeRADIUSUsersEndpointResponse400
    | PutServicesFreeRADIUSUsersEndpointResponse401
    | PutServicesFreeRADIUSUsersEndpointResponse403
    | PutServicesFreeRADIUSUsersEndpointResponse404
    | PutServicesFreeRADIUSUsersEndpointResponse405
    | PutServicesFreeRADIUSUsersEndpointResponse406
    | PutServicesFreeRADIUSUsersEndpointResponse409
    | PutServicesFreeRADIUSUsersEndpointResponse415
    | PutServicesFreeRADIUSUsersEndpointResponse422
    | PutServicesFreeRADIUSUsersEndpointResponse424
    | PutServicesFreeRADIUSUsersEndpointResponse500
    | PutServicesFreeRADIUSUsersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Users.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: FreeRADIUSUser<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-users-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSUsersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSUsersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesFreeRADIUSUsersEndpointResponse400 | PutServicesFreeRADIUSUsersEndpointResponse401 | PutServicesFreeRADIUSUsersEndpointResponse403 | PutServicesFreeRADIUSUsersEndpointResponse404 | PutServicesFreeRADIUSUsersEndpointResponse405 | PutServicesFreeRADIUSUsersEndpointResponse406 | PutServicesFreeRADIUSUsersEndpointResponse409 | PutServicesFreeRADIUSUsersEndpointResponse415 | PutServicesFreeRADIUSUsersEndpointResponse422 | PutServicesFreeRADIUSUsersEndpointResponse424 | PutServicesFreeRADIUSUsersEndpointResponse500 | PutServicesFreeRADIUSUsersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
