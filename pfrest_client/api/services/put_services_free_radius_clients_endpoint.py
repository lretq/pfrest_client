from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_free_radius_clients_endpoint_data_body_item import (
    PutServicesFreeRADIUSClientsEndpointDataBodyItem,
)
from ...models.put_services_free_radius_clients_endpoint_json_body_item import (
    PutServicesFreeRADIUSClientsEndpointJsonBodyItem,
)
from ...models.put_services_free_radius_clients_endpoint_response_400 import (
    PutServicesFreeRADIUSClientsEndpointResponse400,
)
from ...models.put_services_free_radius_clients_endpoint_response_401 import (
    PutServicesFreeRADIUSClientsEndpointResponse401,
)
from ...models.put_services_free_radius_clients_endpoint_response_403 import (
    PutServicesFreeRADIUSClientsEndpointResponse403,
)
from ...models.put_services_free_radius_clients_endpoint_response_404 import (
    PutServicesFreeRADIUSClientsEndpointResponse404,
)
from ...models.put_services_free_radius_clients_endpoint_response_405 import (
    PutServicesFreeRADIUSClientsEndpointResponse405,
)
from ...models.put_services_free_radius_clients_endpoint_response_406 import (
    PutServicesFreeRADIUSClientsEndpointResponse406,
)
from ...models.put_services_free_radius_clients_endpoint_response_409 import (
    PutServicesFreeRADIUSClientsEndpointResponse409,
)
from ...models.put_services_free_radius_clients_endpoint_response_415 import (
    PutServicesFreeRADIUSClientsEndpointResponse415,
)
from ...models.put_services_free_radius_clients_endpoint_response_422 import (
    PutServicesFreeRADIUSClientsEndpointResponse422,
)
from ...models.put_services_free_radius_clients_endpoint_response_424 import (
    PutServicesFreeRADIUSClientsEndpointResponse424,
)
from ...models.put_services_free_radius_clients_endpoint_response_500 import (
    PutServicesFreeRADIUSClientsEndpointResponse500,
)
from ...models.put_services_free_radius_clients_endpoint_response_503 import (
    PutServicesFreeRADIUSClientsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSClientsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/freeradius/clients",
    }

    if isinstance(body, list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesFreeRADIUSClientsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesFreeRADIUSClientsEndpointResponse400
    | PutServicesFreeRADIUSClientsEndpointResponse401
    | PutServicesFreeRADIUSClientsEndpointResponse403
    | PutServicesFreeRADIUSClientsEndpointResponse404
    | PutServicesFreeRADIUSClientsEndpointResponse405
    | PutServicesFreeRADIUSClientsEndpointResponse406
    | PutServicesFreeRADIUSClientsEndpointResponse409
    | PutServicesFreeRADIUSClientsEndpointResponse415
    | PutServicesFreeRADIUSClientsEndpointResponse422
    | PutServicesFreeRADIUSClientsEndpointResponse424
    | PutServicesFreeRADIUSClientsEndpointResponse500
    | PutServicesFreeRADIUSClientsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesFreeRADIUSClientsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesFreeRADIUSClientsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesFreeRADIUSClientsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesFreeRADIUSClientsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesFreeRADIUSClientsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesFreeRADIUSClientsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesFreeRADIUSClientsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesFreeRADIUSClientsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesFreeRADIUSClientsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesFreeRADIUSClientsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesFreeRADIUSClientsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesFreeRADIUSClientsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesFreeRADIUSClientsEndpointResponse400
    | PutServicesFreeRADIUSClientsEndpointResponse401
    | PutServicesFreeRADIUSClientsEndpointResponse403
    | PutServicesFreeRADIUSClientsEndpointResponse404
    | PutServicesFreeRADIUSClientsEndpointResponse405
    | PutServicesFreeRADIUSClientsEndpointResponse406
    | PutServicesFreeRADIUSClientsEndpointResponse409
    | PutServicesFreeRADIUSClientsEndpointResponse415
    | PutServicesFreeRADIUSClientsEndpointResponse422
    | PutServicesFreeRADIUSClientsEndpointResponse424
    | PutServicesFreeRADIUSClientsEndpointResponse500
    | PutServicesFreeRADIUSClientsEndpointResponse503
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
    body: list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSClientsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesFreeRADIUSClientsEndpointResponse400
    | PutServicesFreeRADIUSClientsEndpointResponse401
    | PutServicesFreeRADIUSClientsEndpointResponse403
    | PutServicesFreeRADIUSClientsEndpointResponse404
    | PutServicesFreeRADIUSClientsEndpointResponse405
    | PutServicesFreeRADIUSClientsEndpointResponse406
    | PutServicesFreeRADIUSClientsEndpointResponse409
    | PutServicesFreeRADIUSClientsEndpointResponse415
    | PutServicesFreeRADIUSClientsEndpointResponse422
    | PutServicesFreeRADIUSClientsEndpointResponse424
    | PutServicesFreeRADIUSClientsEndpointResponse500
    | PutServicesFreeRADIUSClientsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Clients.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-clients-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSClientsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesFreeRADIUSClientsEndpointResponse400 | PutServicesFreeRADIUSClientsEndpointResponse401 | PutServicesFreeRADIUSClientsEndpointResponse403 | PutServicesFreeRADIUSClientsEndpointResponse404 | PutServicesFreeRADIUSClientsEndpointResponse405 | PutServicesFreeRADIUSClientsEndpointResponse406 | PutServicesFreeRADIUSClientsEndpointResponse409 | PutServicesFreeRADIUSClientsEndpointResponse415 | PutServicesFreeRADIUSClientsEndpointResponse422 | PutServicesFreeRADIUSClientsEndpointResponse424 | PutServicesFreeRADIUSClientsEndpointResponse500 | PutServicesFreeRADIUSClientsEndpointResponse503]
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
    body: list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSClientsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesFreeRADIUSClientsEndpointResponse400
    | PutServicesFreeRADIUSClientsEndpointResponse401
    | PutServicesFreeRADIUSClientsEndpointResponse403
    | PutServicesFreeRADIUSClientsEndpointResponse404
    | PutServicesFreeRADIUSClientsEndpointResponse405
    | PutServicesFreeRADIUSClientsEndpointResponse406
    | PutServicesFreeRADIUSClientsEndpointResponse409
    | PutServicesFreeRADIUSClientsEndpointResponse415
    | PutServicesFreeRADIUSClientsEndpointResponse422
    | PutServicesFreeRADIUSClientsEndpointResponse424
    | PutServicesFreeRADIUSClientsEndpointResponse500
    | PutServicesFreeRADIUSClientsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Clients.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-clients-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSClientsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesFreeRADIUSClientsEndpointResponse400 | PutServicesFreeRADIUSClientsEndpointResponse401 | PutServicesFreeRADIUSClientsEndpointResponse403 | PutServicesFreeRADIUSClientsEndpointResponse404 | PutServicesFreeRADIUSClientsEndpointResponse405 | PutServicesFreeRADIUSClientsEndpointResponse406 | PutServicesFreeRADIUSClientsEndpointResponse409 | PutServicesFreeRADIUSClientsEndpointResponse415 | PutServicesFreeRADIUSClientsEndpointResponse422 | PutServicesFreeRADIUSClientsEndpointResponse424 | PutServicesFreeRADIUSClientsEndpointResponse500 | PutServicesFreeRADIUSClientsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSClientsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesFreeRADIUSClientsEndpointResponse400
    | PutServicesFreeRADIUSClientsEndpointResponse401
    | PutServicesFreeRADIUSClientsEndpointResponse403
    | PutServicesFreeRADIUSClientsEndpointResponse404
    | PutServicesFreeRADIUSClientsEndpointResponse405
    | PutServicesFreeRADIUSClientsEndpointResponse406
    | PutServicesFreeRADIUSClientsEndpointResponse409
    | PutServicesFreeRADIUSClientsEndpointResponse415
    | PutServicesFreeRADIUSClientsEndpointResponse422
    | PutServicesFreeRADIUSClientsEndpointResponse424
    | PutServicesFreeRADIUSClientsEndpointResponse500
    | PutServicesFreeRADIUSClientsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Clients.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-clients-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSClientsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesFreeRADIUSClientsEndpointResponse400 | PutServicesFreeRADIUSClientsEndpointResponse401 | PutServicesFreeRADIUSClientsEndpointResponse403 | PutServicesFreeRADIUSClientsEndpointResponse404 | PutServicesFreeRADIUSClientsEndpointResponse405 | PutServicesFreeRADIUSClientsEndpointResponse406 | PutServicesFreeRADIUSClientsEndpointResponse409 | PutServicesFreeRADIUSClientsEndpointResponse415 | PutServicesFreeRADIUSClientsEndpointResponse422 | PutServicesFreeRADIUSClientsEndpointResponse424 | PutServicesFreeRADIUSClientsEndpointResponse500 | PutServicesFreeRADIUSClientsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSClientsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesFreeRADIUSClientsEndpointResponse400
    | PutServicesFreeRADIUSClientsEndpointResponse401
    | PutServicesFreeRADIUSClientsEndpointResponse403
    | PutServicesFreeRADIUSClientsEndpointResponse404
    | PutServicesFreeRADIUSClientsEndpointResponse405
    | PutServicesFreeRADIUSClientsEndpointResponse406
    | PutServicesFreeRADIUSClientsEndpointResponse409
    | PutServicesFreeRADIUSClientsEndpointResponse415
    | PutServicesFreeRADIUSClientsEndpointResponse422
    | PutServicesFreeRADIUSClientsEndpointResponse424
    | PutServicesFreeRADIUSClientsEndpointResponse500
    | PutServicesFreeRADIUSClientsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Clients.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-clients-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSClientsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSClientsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesFreeRADIUSClientsEndpointResponse400 | PutServicesFreeRADIUSClientsEndpointResponse401 | PutServicesFreeRADIUSClientsEndpointResponse403 | PutServicesFreeRADIUSClientsEndpointResponse404 | PutServicesFreeRADIUSClientsEndpointResponse405 | PutServicesFreeRADIUSClientsEndpointResponse406 | PutServicesFreeRADIUSClientsEndpointResponse409 | PutServicesFreeRADIUSClientsEndpointResponse415 | PutServicesFreeRADIUSClientsEndpointResponse422 | PutServicesFreeRADIUSClientsEndpointResponse424 | PutServicesFreeRADIUSClientsEndpointResponse500 | PutServicesFreeRADIUSClientsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
