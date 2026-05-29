from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_bind_access_lists_endpoint_data_body_item import (
    PutServicesBINDAccessListsEndpointDataBodyItem,
)
from ...models.put_services_bind_access_lists_endpoint_json_body_item import (
    PutServicesBINDAccessListsEndpointJsonBodyItem,
)
from ...models.put_services_bind_access_lists_endpoint_response_400 import PutServicesBINDAccessListsEndpointResponse400
from ...models.put_services_bind_access_lists_endpoint_response_401 import PutServicesBINDAccessListsEndpointResponse401
from ...models.put_services_bind_access_lists_endpoint_response_403 import PutServicesBINDAccessListsEndpointResponse403
from ...models.put_services_bind_access_lists_endpoint_response_404 import PutServicesBINDAccessListsEndpointResponse404
from ...models.put_services_bind_access_lists_endpoint_response_405 import PutServicesBINDAccessListsEndpointResponse405
from ...models.put_services_bind_access_lists_endpoint_response_406 import PutServicesBINDAccessListsEndpointResponse406
from ...models.put_services_bind_access_lists_endpoint_response_409 import PutServicesBINDAccessListsEndpointResponse409
from ...models.put_services_bind_access_lists_endpoint_response_415 import PutServicesBINDAccessListsEndpointResponse415
from ...models.put_services_bind_access_lists_endpoint_response_422 import PutServicesBINDAccessListsEndpointResponse422
from ...models.put_services_bind_access_lists_endpoint_response_424 import PutServicesBINDAccessListsEndpointResponse424
from ...models.put_services_bind_access_lists_endpoint_response_500 import PutServicesBINDAccessListsEndpointResponse500
from ...models.put_services_bind_access_lists_endpoint_response_503 import PutServicesBINDAccessListsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesBINDAccessListsEndpointJsonBodyItem]
    | list[PutServicesBINDAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/bind/access_lists",
    }

    if isinstance(body, list[PutServicesBINDAccessListsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesBINDAccessListsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesBINDAccessListsEndpointResponse400
    | PutServicesBINDAccessListsEndpointResponse401
    | PutServicesBINDAccessListsEndpointResponse403
    | PutServicesBINDAccessListsEndpointResponse404
    | PutServicesBINDAccessListsEndpointResponse405
    | PutServicesBINDAccessListsEndpointResponse406
    | PutServicesBINDAccessListsEndpointResponse409
    | PutServicesBINDAccessListsEndpointResponse415
    | PutServicesBINDAccessListsEndpointResponse422
    | PutServicesBINDAccessListsEndpointResponse424
    | PutServicesBINDAccessListsEndpointResponse500
    | PutServicesBINDAccessListsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesBINDAccessListsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesBINDAccessListsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesBINDAccessListsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesBINDAccessListsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesBINDAccessListsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesBINDAccessListsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesBINDAccessListsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesBINDAccessListsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesBINDAccessListsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesBINDAccessListsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesBINDAccessListsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesBINDAccessListsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesBINDAccessListsEndpointResponse400
    | PutServicesBINDAccessListsEndpointResponse401
    | PutServicesBINDAccessListsEndpointResponse403
    | PutServicesBINDAccessListsEndpointResponse404
    | PutServicesBINDAccessListsEndpointResponse405
    | PutServicesBINDAccessListsEndpointResponse406
    | PutServicesBINDAccessListsEndpointResponse409
    | PutServicesBINDAccessListsEndpointResponse415
    | PutServicesBINDAccessListsEndpointResponse422
    | PutServicesBINDAccessListsEndpointResponse424
    | PutServicesBINDAccessListsEndpointResponse500
    | PutServicesBINDAccessListsEndpointResponse503
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
    body: list[PutServicesBINDAccessListsEndpointJsonBodyItem]
    | list[PutServicesBINDAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesBINDAccessListsEndpointResponse400
    | PutServicesBINDAccessListsEndpointResponse401
    | PutServicesBINDAccessListsEndpointResponse403
    | PutServicesBINDAccessListsEndpointResponse404
    | PutServicesBINDAccessListsEndpointResponse405
    | PutServicesBINDAccessListsEndpointResponse406
    | PutServicesBINDAccessListsEndpointResponse409
    | PutServicesBINDAccessListsEndpointResponse415
    | PutServicesBINDAccessListsEndpointResponse422
    | PutServicesBINDAccessListsEndpointResponse424
    | PutServicesBINDAccessListsEndpointResponse500
    | PutServicesBINDAccessListsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing BIND Access Lists.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-lists-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesBINDAccessListsEndpointResponse400 | PutServicesBINDAccessListsEndpointResponse401 | PutServicesBINDAccessListsEndpointResponse403 | PutServicesBINDAccessListsEndpointResponse404 | PutServicesBINDAccessListsEndpointResponse405 | PutServicesBINDAccessListsEndpointResponse406 | PutServicesBINDAccessListsEndpointResponse409 | PutServicesBINDAccessListsEndpointResponse415 | PutServicesBINDAccessListsEndpointResponse422 | PutServicesBINDAccessListsEndpointResponse424 | PutServicesBINDAccessListsEndpointResponse500 | PutServicesBINDAccessListsEndpointResponse503]
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
    body: list[PutServicesBINDAccessListsEndpointJsonBodyItem]
    | list[PutServicesBINDAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesBINDAccessListsEndpointResponse400
    | PutServicesBINDAccessListsEndpointResponse401
    | PutServicesBINDAccessListsEndpointResponse403
    | PutServicesBINDAccessListsEndpointResponse404
    | PutServicesBINDAccessListsEndpointResponse405
    | PutServicesBINDAccessListsEndpointResponse406
    | PutServicesBINDAccessListsEndpointResponse409
    | PutServicesBINDAccessListsEndpointResponse415
    | PutServicesBINDAccessListsEndpointResponse422
    | PutServicesBINDAccessListsEndpointResponse424
    | PutServicesBINDAccessListsEndpointResponse500
    | PutServicesBINDAccessListsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing BIND Access Lists.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-lists-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesBINDAccessListsEndpointResponse400 | PutServicesBINDAccessListsEndpointResponse401 | PutServicesBINDAccessListsEndpointResponse403 | PutServicesBINDAccessListsEndpointResponse404 | PutServicesBINDAccessListsEndpointResponse405 | PutServicesBINDAccessListsEndpointResponse406 | PutServicesBINDAccessListsEndpointResponse409 | PutServicesBINDAccessListsEndpointResponse415 | PutServicesBINDAccessListsEndpointResponse422 | PutServicesBINDAccessListsEndpointResponse424 | PutServicesBINDAccessListsEndpointResponse500 | PutServicesBINDAccessListsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesBINDAccessListsEndpointJsonBodyItem]
    | list[PutServicesBINDAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesBINDAccessListsEndpointResponse400
    | PutServicesBINDAccessListsEndpointResponse401
    | PutServicesBINDAccessListsEndpointResponse403
    | PutServicesBINDAccessListsEndpointResponse404
    | PutServicesBINDAccessListsEndpointResponse405
    | PutServicesBINDAccessListsEndpointResponse406
    | PutServicesBINDAccessListsEndpointResponse409
    | PutServicesBINDAccessListsEndpointResponse415
    | PutServicesBINDAccessListsEndpointResponse422
    | PutServicesBINDAccessListsEndpointResponse424
    | PutServicesBINDAccessListsEndpointResponse500
    | PutServicesBINDAccessListsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing BIND Access Lists.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-lists-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesBINDAccessListsEndpointResponse400 | PutServicesBINDAccessListsEndpointResponse401 | PutServicesBINDAccessListsEndpointResponse403 | PutServicesBINDAccessListsEndpointResponse404 | PutServicesBINDAccessListsEndpointResponse405 | PutServicesBINDAccessListsEndpointResponse406 | PutServicesBINDAccessListsEndpointResponse409 | PutServicesBINDAccessListsEndpointResponse415 | PutServicesBINDAccessListsEndpointResponse422 | PutServicesBINDAccessListsEndpointResponse424 | PutServicesBINDAccessListsEndpointResponse500 | PutServicesBINDAccessListsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesBINDAccessListsEndpointJsonBodyItem]
    | list[PutServicesBINDAccessListsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesBINDAccessListsEndpointResponse400
    | PutServicesBINDAccessListsEndpointResponse401
    | PutServicesBINDAccessListsEndpointResponse403
    | PutServicesBINDAccessListsEndpointResponse404
    | PutServicesBINDAccessListsEndpointResponse405
    | PutServicesBINDAccessListsEndpointResponse406
    | PutServicesBINDAccessListsEndpointResponse409
    | PutServicesBINDAccessListsEndpointResponse415
    | PutServicesBINDAccessListsEndpointResponse422
    | PutServicesBINDAccessListsEndpointResponse424
    | PutServicesBINDAccessListsEndpointResponse500
    | PutServicesBINDAccessListsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing BIND Access Lists.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-lists-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDAccessListsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDAccessListsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesBINDAccessListsEndpointResponse400 | PutServicesBINDAccessListsEndpointResponse401 | PutServicesBINDAccessListsEndpointResponse403 | PutServicesBINDAccessListsEndpointResponse404 | PutServicesBINDAccessListsEndpointResponse405 | PutServicesBINDAccessListsEndpointResponse406 | PutServicesBINDAccessListsEndpointResponse409 | PutServicesBINDAccessListsEndpointResponse415 | PutServicesBINDAccessListsEndpointResponse422 | PutServicesBINDAccessListsEndpointResponse424 | PutServicesBINDAccessListsEndpointResponse500 | PutServicesBINDAccessListsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
