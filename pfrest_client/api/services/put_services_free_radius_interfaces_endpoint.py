from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_free_radius_interfaces_endpoint_data_body_item import (
    PutServicesFreeRADIUSInterfacesEndpointDataBodyItem,
)
from ...models.put_services_free_radius_interfaces_endpoint_json_body_item import (
    PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_400 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse400,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_401 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse401,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_403 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse403,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_404 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse404,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_405 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse405,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_406 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse406,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_409 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse409,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_415 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse415,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_422 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse422,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_424 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse424,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_500 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse500,
)
from ...models.put_services_free_radius_interfaces_endpoint_response_503 import (
    PutServicesFreeRADIUSInterfacesEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/freeradius/interfaces",
    }

    if isinstance(body, list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesFreeRADIUSInterfacesEndpointResponse400
    | PutServicesFreeRADIUSInterfacesEndpointResponse401
    | PutServicesFreeRADIUSInterfacesEndpointResponse403
    | PutServicesFreeRADIUSInterfacesEndpointResponse404
    | PutServicesFreeRADIUSInterfacesEndpointResponse405
    | PutServicesFreeRADIUSInterfacesEndpointResponse406
    | PutServicesFreeRADIUSInterfacesEndpointResponse409
    | PutServicesFreeRADIUSInterfacesEndpointResponse415
    | PutServicesFreeRADIUSInterfacesEndpointResponse422
    | PutServicesFreeRADIUSInterfacesEndpointResponse424
    | PutServicesFreeRADIUSInterfacesEndpointResponse500
    | PutServicesFreeRADIUSInterfacesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesFreeRADIUSInterfacesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesFreeRADIUSInterfacesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesFreeRADIUSInterfacesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesFreeRADIUSInterfacesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesFreeRADIUSInterfacesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesFreeRADIUSInterfacesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesFreeRADIUSInterfacesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesFreeRADIUSInterfacesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesFreeRADIUSInterfacesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesFreeRADIUSInterfacesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesFreeRADIUSInterfacesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesFreeRADIUSInterfacesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesFreeRADIUSInterfacesEndpointResponse400
    | PutServicesFreeRADIUSInterfacesEndpointResponse401
    | PutServicesFreeRADIUSInterfacesEndpointResponse403
    | PutServicesFreeRADIUSInterfacesEndpointResponse404
    | PutServicesFreeRADIUSInterfacesEndpointResponse405
    | PutServicesFreeRADIUSInterfacesEndpointResponse406
    | PutServicesFreeRADIUSInterfacesEndpointResponse409
    | PutServicesFreeRADIUSInterfacesEndpointResponse415
    | PutServicesFreeRADIUSInterfacesEndpointResponse422
    | PutServicesFreeRADIUSInterfacesEndpointResponse424
    | PutServicesFreeRADIUSInterfacesEndpointResponse500
    | PutServicesFreeRADIUSInterfacesEndpointResponse503
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
    body: list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesFreeRADIUSInterfacesEndpointResponse400
    | PutServicesFreeRADIUSInterfacesEndpointResponse401
    | PutServicesFreeRADIUSInterfacesEndpointResponse403
    | PutServicesFreeRADIUSInterfacesEndpointResponse404
    | PutServicesFreeRADIUSInterfacesEndpointResponse405
    | PutServicesFreeRADIUSInterfacesEndpointResponse406
    | PutServicesFreeRADIUSInterfacesEndpointResponse409
    | PutServicesFreeRADIUSInterfacesEndpointResponse415
    | PutServicesFreeRADIUSInterfacesEndpointResponse422
    | PutServicesFreeRADIUSInterfacesEndpointResponse424
    | PutServicesFreeRADIUSInterfacesEndpointResponse500
    | PutServicesFreeRADIUSInterfacesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Interfaces.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interfaces-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesFreeRADIUSInterfacesEndpointResponse400 | PutServicesFreeRADIUSInterfacesEndpointResponse401 | PutServicesFreeRADIUSInterfacesEndpointResponse403 | PutServicesFreeRADIUSInterfacesEndpointResponse404 | PutServicesFreeRADIUSInterfacesEndpointResponse405 | PutServicesFreeRADIUSInterfacesEndpointResponse406 | PutServicesFreeRADIUSInterfacesEndpointResponse409 | PutServicesFreeRADIUSInterfacesEndpointResponse415 | PutServicesFreeRADIUSInterfacesEndpointResponse422 | PutServicesFreeRADIUSInterfacesEndpointResponse424 | PutServicesFreeRADIUSInterfacesEndpointResponse500 | PutServicesFreeRADIUSInterfacesEndpointResponse503]
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
    body: list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesFreeRADIUSInterfacesEndpointResponse400
    | PutServicesFreeRADIUSInterfacesEndpointResponse401
    | PutServicesFreeRADIUSInterfacesEndpointResponse403
    | PutServicesFreeRADIUSInterfacesEndpointResponse404
    | PutServicesFreeRADIUSInterfacesEndpointResponse405
    | PutServicesFreeRADIUSInterfacesEndpointResponse406
    | PutServicesFreeRADIUSInterfacesEndpointResponse409
    | PutServicesFreeRADIUSInterfacesEndpointResponse415
    | PutServicesFreeRADIUSInterfacesEndpointResponse422
    | PutServicesFreeRADIUSInterfacesEndpointResponse424
    | PutServicesFreeRADIUSInterfacesEndpointResponse500
    | PutServicesFreeRADIUSInterfacesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Interfaces.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interfaces-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesFreeRADIUSInterfacesEndpointResponse400 | PutServicesFreeRADIUSInterfacesEndpointResponse401 | PutServicesFreeRADIUSInterfacesEndpointResponse403 | PutServicesFreeRADIUSInterfacesEndpointResponse404 | PutServicesFreeRADIUSInterfacesEndpointResponse405 | PutServicesFreeRADIUSInterfacesEndpointResponse406 | PutServicesFreeRADIUSInterfacesEndpointResponse409 | PutServicesFreeRADIUSInterfacesEndpointResponse415 | PutServicesFreeRADIUSInterfacesEndpointResponse422 | PutServicesFreeRADIUSInterfacesEndpointResponse424 | PutServicesFreeRADIUSInterfacesEndpointResponse500 | PutServicesFreeRADIUSInterfacesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesFreeRADIUSInterfacesEndpointResponse400
    | PutServicesFreeRADIUSInterfacesEndpointResponse401
    | PutServicesFreeRADIUSInterfacesEndpointResponse403
    | PutServicesFreeRADIUSInterfacesEndpointResponse404
    | PutServicesFreeRADIUSInterfacesEndpointResponse405
    | PutServicesFreeRADIUSInterfacesEndpointResponse406
    | PutServicesFreeRADIUSInterfacesEndpointResponse409
    | PutServicesFreeRADIUSInterfacesEndpointResponse415
    | PutServicesFreeRADIUSInterfacesEndpointResponse422
    | PutServicesFreeRADIUSInterfacesEndpointResponse424
    | PutServicesFreeRADIUSInterfacesEndpointResponse500
    | PutServicesFreeRADIUSInterfacesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Interfaces.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interfaces-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesFreeRADIUSInterfacesEndpointResponse400 | PutServicesFreeRADIUSInterfacesEndpointResponse401 | PutServicesFreeRADIUSInterfacesEndpointResponse403 | PutServicesFreeRADIUSInterfacesEndpointResponse404 | PutServicesFreeRADIUSInterfacesEndpointResponse405 | PutServicesFreeRADIUSInterfacesEndpointResponse406 | PutServicesFreeRADIUSInterfacesEndpointResponse409 | PutServicesFreeRADIUSInterfacesEndpointResponse415 | PutServicesFreeRADIUSInterfacesEndpointResponse422 | PutServicesFreeRADIUSInterfacesEndpointResponse424 | PutServicesFreeRADIUSInterfacesEndpointResponse500 | PutServicesFreeRADIUSInterfacesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem]
    | list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesFreeRADIUSInterfacesEndpointResponse400
    | PutServicesFreeRADIUSInterfacesEndpointResponse401
    | PutServicesFreeRADIUSInterfacesEndpointResponse403
    | PutServicesFreeRADIUSInterfacesEndpointResponse404
    | PutServicesFreeRADIUSInterfacesEndpointResponse405
    | PutServicesFreeRADIUSInterfacesEndpointResponse406
    | PutServicesFreeRADIUSInterfacesEndpointResponse409
    | PutServicesFreeRADIUSInterfacesEndpointResponse415
    | PutServicesFreeRADIUSInterfacesEndpointResponse422
    | PutServicesFreeRADIUSInterfacesEndpointResponse424
    | PutServicesFreeRADIUSInterfacesEndpointResponse500
    | PutServicesFreeRADIUSInterfacesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing FreeRADIUS Interfaces.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FreeRADIUSInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-interfaces-put ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesFreeRADIUSInterfacesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesFreeRADIUSInterfacesEndpointResponse400 | PutServicesFreeRADIUSInterfacesEndpointResponse401 | PutServicesFreeRADIUSInterfacesEndpointResponse403 | PutServicesFreeRADIUSInterfacesEndpointResponse404 | PutServicesFreeRADIUSInterfacesEndpointResponse405 | PutServicesFreeRADIUSInterfacesEndpointResponse406 | PutServicesFreeRADIUSInterfacesEndpointResponse409 | PutServicesFreeRADIUSInterfacesEndpointResponse415 | PutServicesFreeRADIUSInterfacesEndpointResponse422 | PutServicesFreeRADIUSInterfacesEndpointResponse424 | PutServicesFreeRADIUSInterfacesEndpointResponse500 | PutServicesFreeRADIUSInterfacesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
