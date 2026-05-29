from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_system_tunables_endpoint_data_body_item import PutSystemTunablesEndpointDataBodyItem
from ...models.put_system_tunables_endpoint_json_body_item import PutSystemTunablesEndpointJsonBodyItem
from ...models.put_system_tunables_endpoint_response_400 import PutSystemTunablesEndpointResponse400
from ...models.put_system_tunables_endpoint_response_401 import PutSystemTunablesEndpointResponse401
from ...models.put_system_tunables_endpoint_response_403 import PutSystemTunablesEndpointResponse403
from ...models.put_system_tunables_endpoint_response_404 import PutSystemTunablesEndpointResponse404
from ...models.put_system_tunables_endpoint_response_405 import PutSystemTunablesEndpointResponse405
from ...models.put_system_tunables_endpoint_response_406 import PutSystemTunablesEndpointResponse406
from ...models.put_system_tunables_endpoint_response_409 import PutSystemTunablesEndpointResponse409
from ...models.put_system_tunables_endpoint_response_415 import PutSystemTunablesEndpointResponse415
from ...models.put_system_tunables_endpoint_response_422 import PutSystemTunablesEndpointResponse422
from ...models.put_system_tunables_endpoint_response_424 import PutSystemTunablesEndpointResponse424
from ...models.put_system_tunables_endpoint_response_500 import PutSystemTunablesEndpointResponse500
from ...models.put_system_tunables_endpoint_response_503 import PutSystemTunablesEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutSystemTunablesEndpointJsonBodyItem] | list[PutSystemTunablesEndpointDataBodyItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/system/tunables",
    }

    if isinstance(body, list[PutSystemTunablesEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutSystemTunablesEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutSystemTunablesEndpointResponse400
    | PutSystemTunablesEndpointResponse401
    | PutSystemTunablesEndpointResponse403
    | PutSystemTunablesEndpointResponse404
    | PutSystemTunablesEndpointResponse405
    | PutSystemTunablesEndpointResponse406
    | PutSystemTunablesEndpointResponse409
    | PutSystemTunablesEndpointResponse415
    | PutSystemTunablesEndpointResponse422
    | PutSystemTunablesEndpointResponse424
    | PutSystemTunablesEndpointResponse500
    | PutSystemTunablesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutSystemTunablesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutSystemTunablesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutSystemTunablesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutSystemTunablesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutSystemTunablesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutSystemTunablesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutSystemTunablesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutSystemTunablesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutSystemTunablesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutSystemTunablesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutSystemTunablesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutSystemTunablesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutSystemTunablesEndpointResponse400
    | PutSystemTunablesEndpointResponse401
    | PutSystemTunablesEndpointResponse403
    | PutSystemTunablesEndpointResponse404
    | PutSystemTunablesEndpointResponse405
    | PutSystemTunablesEndpointResponse406
    | PutSystemTunablesEndpointResponse409
    | PutSystemTunablesEndpointResponse415
    | PutSystemTunablesEndpointResponse422
    | PutSystemTunablesEndpointResponse424
    | PutSystemTunablesEndpointResponse500
    | PutSystemTunablesEndpointResponse503
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
    body: list[PutSystemTunablesEndpointJsonBodyItem] | list[PutSystemTunablesEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutSystemTunablesEndpointResponse400
    | PutSystemTunablesEndpointResponse401
    | PutSystemTunablesEndpointResponse403
    | PutSystemTunablesEndpointResponse404
    | PutSystemTunablesEndpointResponse405
    | PutSystemTunablesEndpointResponse406
    | PutSystemTunablesEndpointResponse409
    | PutSystemTunablesEndpointResponse415
    | PutSystemTunablesEndpointResponse422
    | PutSystemTunablesEndpointResponse424
    | PutSystemTunablesEndpointResponse500
    | PutSystemTunablesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing System Tunables.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunables-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutSystemTunablesEndpointJsonBodyItem] | Unset):
        body (list[PutSystemTunablesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSystemTunablesEndpointResponse400 | PutSystemTunablesEndpointResponse401 | PutSystemTunablesEndpointResponse403 | PutSystemTunablesEndpointResponse404 | PutSystemTunablesEndpointResponse405 | PutSystemTunablesEndpointResponse406 | PutSystemTunablesEndpointResponse409 | PutSystemTunablesEndpointResponse415 | PutSystemTunablesEndpointResponse422 | PutSystemTunablesEndpointResponse424 | PutSystemTunablesEndpointResponse500 | PutSystemTunablesEndpointResponse503]
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
    body: list[PutSystemTunablesEndpointJsonBodyItem] | list[PutSystemTunablesEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutSystemTunablesEndpointResponse400
    | PutSystemTunablesEndpointResponse401
    | PutSystemTunablesEndpointResponse403
    | PutSystemTunablesEndpointResponse404
    | PutSystemTunablesEndpointResponse405
    | PutSystemTunablesEndpointResponse406
    | PutSystemTunablesEndpointResponse409
    | PutSystemTunablesEndpointResponse415
    | PutSystemTunablesEndpointResponse422
    | PutSystemTunablesEndpointResponse424
    | PutSystemTunablesEndpointResponse500
    | PutSystemTunablesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing System Tunables.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunables-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutSystemTunablesEndpointJsonBodyItem] | Unset):
        body (list[PutSystemTunablesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSystemTunablesEndpointResponse400 | PutSystemTunablesEndpointResponse401 | PutSystemTunablesEndpointResponse403 | PutSystemTunablesEndpointResponse404 | PutSystemTunablesEndpointResponse405 | PutSystemTunablesEndpointResponse406 | PutSystemTunablesEndpointResponse409 | PutSystemTunablesEndpointResponse415 | PutSystemTunablesEndpointResponse422 | PutSystemTunablesEndpointResponse424 | PutSystemTunablesEndpointResponse500 | PutSystemTunablesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutSystemTunablesEndpointJsonBodyItem] | list[PutSystemTunablesEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutSystemTunablesEndpointResponse400
    | PutSystemTunablesEndpointResponse401
    | PutSystemTunablesEndpointResponse403
    | PutSystemTunablesEndpointResponse404
    | PutSystemTunablesEndpointResponse405
    | PutSystemTunablesEndpointResponse406
    | PutSystemTunablesEndpointResponse409
    | PutSystemTunablesEndpointResponse415
    | PutSystemTunablesEndpointResponse422
    | PutSystemTunablesEndpointResponse424
    | PutSystemTunablesEndpointResponse500
    | PutSystemTunablesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing System Tunables.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunables-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutSystemTunablesEndpointJsonBodyItem] | Unset):
        body (list[PutSystemTunablesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSystemTunablesEndpointResponse400 | PutSystemTunablesEndpointResponse401 | PutSystemTunablesEndpointResponse403 | PutSystemTunablesEndpointResponse404 | PutSystemTunablesEndpointResponse405 | PutSystemTunablesEndpointResponse406 | PutSystemTunablesEndpointResponse409 | PutSystemTunablesEndpointResponse415 | PutSystemTunablesEndpointResponse422 | PutSystemTunablesEndpointResponse424 | PutSystemTunablesEndpointResponse500 | PutSystemTunablesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutSystemTunablesEndpointJsonBodyItem] | list[PutSystemTunablesEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutSystemTunablesEndpointResponse400
    | PutSystemTunablesEndpointResponse401
    | PutSystemTunablesEndpointResponse403
    | PutSystemTunablesEndpointResponse404
    | PutSystemTunablesEndpointResponse405
    | PutSystemTunablesEndpointResponse406
    | PutSystemTunablesEndpointResponse409
    | PutSystemTunablesEndpointResponse415
    | PutSystemTunablesEndpointResponse422
    | PutSystemTunablesEndpointResponse424
    | PutSystemTunablesEndpointResponse500
    | PutSystemTunablesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing System Tunables.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunables-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutSystemTunablesEndpointJsonBodyItem] | Unset):
        body (list[PutSystemTunablesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSystemTunablesEndpointResponse400 | PutSystemTunablesEndpointResponse401 | PutSystemTunablesEndpointResponse403 | PutSystemTunablesEndpointResponse404 | PutSystemTunablesEndpointResponse405 | PutSystemTunablesEndpointResponse406 | PutSystemTunablesEndpointResponse409 | PutSystemTunablesEndpointResponse415 | PutSystemTunablesEndpointResponse422 | PutSystemTunablesEndpointResponse424 | PutSystemTunablesEndpointResponse500 | PutSystemTunablesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
