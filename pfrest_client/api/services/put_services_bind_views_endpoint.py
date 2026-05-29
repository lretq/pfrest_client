from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_bind_views_endpoint_data_body_item import PutServicesBINDViewsEndpointDataBodyItem
from ...models.put_services_bind_views_endpoint_json_body_item import PutServicesBINDViewsEndpointJsonBodyItem
from ...models.put_services_bind_views_endpoint_response_400 import PutServicesBINDViewsEndpointResponse400
from ...models.put_services_bind_views_endpoint_response_401 import PutServicesBINDViewsEndpointResponse401
from ...models.put_services_bind_views_endpoint_response_403 import PutServicesBINDViewsEndpointResponse403
from ...models.put_services_bind_views_endpoint_response_404 import PutServicesBINDViewsEndpointResponse404
from ...models.put_services_bind_views_endpoint_response_405 import PutServicesBINDViewsEndpointResponse405
from ...models.put_services_bind_views_endpoint_response_406 import PutServicesBINDViewsEndpointResponse406
from ...models.put_services_bind_views_endpoint_response_409 import PutServicesBINDViewsEndpointResponse409
from ...models.put_services_bind_views_endpoint_response_415 import PutServicesBINDViewsEndpointResponse415
from ...models.put_services_bind_views_endpoint_response_422 import PutServicesBINDViewsEndpointResponse422
from ...models.put_services_bind_views_endpoint_response_424 import PutServicesBINDViewsEndpointResponse424
from ...models.put_services_bind_views_endpoint_response_500 import PutServicesBINDViewsEndpointResponse500
from ...models.put_services_bind_views_endpoint_response_503 import PutServicesBINDViewsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesBINDViewsEndpointJsonBodyItem]
    | list[PutServicesBINDViewsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/bind/views",
    }

    if isinstance(body, list[PutServicesBINDViewsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesBINDViewsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesBINDViewsEndpointResponse400
    | PutServicesBINDViewsEndpointResponse401
    | PutServicesBINDViewsEndpointResponse403
    | PutServicesBINDViewsEndpointResponse404
    | PutServicesBINDViewsEndpointResponse405
    | PutServicesBINDViewsEndpointResponse406
    | PutServicesBINDViewsEndpointResponse409
    | PutServicesBINDViewsEndpointResponse415
    | PutServicesBINDViewsEndpointResponse422
    | PutServicesBINDViewsEndpointResponse424
    | PutServicesBINDViewsEndpointResponse500
    | PutServicesBINDViewsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesBINDViewsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesBINDViewsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesBINDViewsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesBINDViewsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesBINDViewsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesBINDViewsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesBINDViewsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesBINDViewsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesBINDViewsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesBINDViewsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesBINDViewsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesBINDViewsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesBINDViewsEndpointResponse400
    | PutServicesBINDViewsEndpointResponse401
    | PutServicesBINDViewsEndpointResponse403
    | PutServicesBINDViewsEndpointResponse404
    | PutServicesBINDViewsEndpointResponse405
    | PutServicesBINDViewsEndpointResponse406
    | PutServicesBINDViewsEndpointResponse409
    | PutServicesBINDViewsEndpointResponse415
    | PutServicesBINDViewsEndpointResponse422
    | PutServicesBINDViewsEndpointResponse424
    | PutServicesBINDViewsEndpointResponse500
    | PutServicesBINDViewsEndpointResponse503
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
    body: list[PutServicesBINDViewsEndpointJsonBodyItem]
    | list[PutServicesBINDViewsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesBINDViewsEndpointResponse400
    | PutServicesBINDViewsEndpointResponse401
    | PutServicesBINDViewsEndpointResponse403
    | PutServicesBINDViewsEndpointResponse404
    | PutServicesBINDViewsEndpointResponse405
    | PutServicesBINDViewsEndpointResponse406
    | PutServicesBINDViewsEndpointResponse409
    | PutServicesBINDViewsEndpointResponse415
    | PutServicesBINDViewsEndpointResponse422
    | PutServicesBINDViewsEndpointResponse424
    | PutServicesBINDViewsEndpointResponse500
    | PutServicesBINDViewsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing BIND Views.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-views-put ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDViewsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDViewsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesBINDViewsEndpointResponse400 | PutServicesBINDViewsEndpointResponse401 | PutServicesBINDViewsEndpointResponse403 | PutServicesBINDViewsEndpointResponse404 | PutServicesBINDViewsEndpointResponse405 | PutServicesBINDViewsEndpointResponse406 | PutServicesBINDViewsEndpointResponse409 | PutServicesBINDViewsEndpointResponse415 | PutServicesBINDViewsEndpointResponse422 | PutServicesBINDViewsEndpointResponse424 | PutServicesBINDViewsEndpointResponse500 | PutServicesBINDViewsEndpointResponse503]
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
    body: list[PutServicesBINDViewsEndpointJsonBodyItem]
    | list[PutServicesBINDViewsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesBINDViewsEndpointResponse400
    | PutServicesBINDViewsEndpointResponse401
    | PutServicesBINDViewsEndpointResponse403
    | PutServicesBINDViewsEndpointResponse404
    | PutServicesBINDViewsEndpointResponse405
    | PutServicesBINDViewsEndpointResponse406
    | PutServicesBINDViewsEndpointResponse409
    | PutServicesBINDViewsEndpointResponse415
    | PutServicesBINDViewsEndpointResponse422
    | PutServicesBINDViewsEndpointResponse424
    | PutServicesBINDViewsEndpointResponse500
    | PutServicesBINDViewsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing BIND Views.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-views-put ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDViewsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDViewsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesBINDViewsEndpointResponse400 | PutServicesBINDViewsEndpointResponse401 | PutServicesBINDViewsEndpointResponse403 | PutServicesBINDViewsEndpointResponse404 | PutServicesBINDViewsEndpointResponse405 | PutServicesBINDViewsEndpointResponse406 | PutServicesBINDViewsEndpointResponse409 | PutServicesBINDViewsEndpointResponse415 | PutServicesBINDViewsEndpointResponse422 | PutServicesBINDViewsEndpointResponse424 | PutServicesBINDViewsEndpointResponse500 | PutServicesBINDViewsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesBINDViewsEndpointJsonBodyItem]
    | list[PutServicesBINDViewsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesBINDViewsEndpointResponse400
    | PutServicesBINDViewsEndpointResponse401
    | PutServicesBINDViewsEndpointResponse403
    | PutServicesBINDViewsEndpointResponse404
    | PutServicesBINDViewsEndpointResponse405
    | PutServicesBINDViewsEndpointResponse406
    | PutServicesBINDViewsEndpointResponse409
    | PutServicesBINDViewsEndpointResponse415
    | PutServicesBINDViewsEndpointResponse422
    | PutServicesBINDViewsEndpointResponse424
    | PutServicesBINDViewsEndpointResponse500
    | PutServicesBINDViewsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing BIND Views.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-views-put ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDViewsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDViewsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesBINDViewsEndpointResponse400 | PutServicesBINDViewsEndpointResponse401 | PutServicesBINDViewsEndpointResponse403 | PutServicesBINDViewsEndpointResponse404 | PutServicesBINDViewsEndpointResponse405 | PutServicesBINDViewsEndpointResponse406 | PutServicesBINDViewsEndpointResponse409 | PutServicesBINDViewsEndpointResponse415 | PutServicesBINDViewsEndpointResponse422 | PutServicesBINDViewsEndpointResponse424 | PutServicesBINDViewsEndpointResponse500 | PutServicesBINDViewsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesBINDViewsEndpointJsonBodyItem]
    | list[PutServicesBINDViewsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesBINDViewsEndpointResponse400
    | PutServicesBINDViewsEndpointResponse401
    | PutServicesBINDViewsEndpointResponse403
    | PutServicesBINDViewsEndpointResponse404
    | PutServicesBINDViewsEndpointResponse405
    | PutServicesBINDViewsEndpointResponse406
    | PutServicesBINDViewsEndpointResponse409
    | PutServicesBINDViewsEndpointResponse415
    | PutServicesBINDViewsEndpointResponse422
    | PutServicesBINDViewsEndpointResponse424
    | PutServicesBINDViewsEndpointResponse500
    | PutServicesBINDViewsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing BIND Views.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: BINDView<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-views-put ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDViewsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDViewsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesBINDViewsEndpointResponse400 | PutServicesBINDViewsEndpointResponse401 | PutServicesBINDViewsEndpointResponse403 | PutServicesBINDViewsEndpointResponse404 | PutServicesBINDViewsEndpointResponse405 | PutServicesBINDViewsEndpointResponse406 | PutServicesBINDViewsEndpointResponse409 | PutServicesBINDViewsEndpointResponse415 | PutServicesBINDViewsEndpointResponse422 | PutServicesBINDViewsEndpointResponse424 | PutServicesBINDViewsEndpointResponse500 | PutServicesBINDViewsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
