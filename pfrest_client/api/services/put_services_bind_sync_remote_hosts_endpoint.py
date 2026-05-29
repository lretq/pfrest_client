from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_bind_sync_remote_hosts_endpoint_data_body_item import (
    PutServicesBINDSyncRemoteHostsEndpointDataBodyItem,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_json_body_item import (
    PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_400 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse400,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_401 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse401,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_403 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse403,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_404 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse404,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_405 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse405,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_406 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse406,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_409 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse409,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_415 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse415,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_422 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse422,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_424 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse424,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_500 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse500,
)
from ...models.put_services_bind_sync_remote_hosts_endpoint_response_503 import (
    PutServicesBINDSyncRemoteHostsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem]
    | list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/bind/sync/remote_hosts",
    }

    if isinstance(body, list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesBINDSyncRemoteHostsEndpointResponse400
    | PutServicesBINDSyncRemoteHostsEndpointResponse401
    | PutServicesBINDSyncRemoteHostsEndpointResponse403
    | PutServicesBINDSyncRemoteHostsEndpointResponse404
    | PutServicesBINDSyncRemoteHostsEndpointResponse405
    | PutServicesBINDSyncRemoteHostsEndpointResponse406
    | PutServicesBINDSyncRemoteHostsEndpointResponse409
    | PutServicesBINDSyncRemoteHostsEndpointResponse415
    | PutServicesBINDSyncRemoteHostsEndpointResponse422
    | PutServicesBINDSyncRemoteHostsEndpointResponse424
    | PutServicesBINDSyncRemoteHostsEndpointResponse500
    | PutServicesBINDSyncRemoteHostsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesBINDSyncRemoteHostsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesBINDSyncRemoteHostsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesBINDSyncRemoteHostsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesBINDSyncRemoteHostsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesBINDSyncRemoteHostsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesBINDSyncRemoteHostsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesBINDSyncRemoteHostsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesBINDSyncRemoteHostsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesBINDSyncRemoteHostsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesBINDSyncRemoteHostsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesBINDSyncRemoteHostsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesBINDSyncRemoteHostsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesBINDSyncRemoteHostsEndpointResponse400
    | PutServicesBINDSyncRemoteHostsEndpointResponse401
    | PutServicesBINDSyncRemoteHostsEndpointResponse403
    | PutServicesBINDSyncRemoteHostsEndpointResponse404
    | PutServicesBINDSyncRemoteHostsEndpointResponse405
    | PutServicesBINDSyncRemoteHostsEndpointResponse406
    | PutServicesBINDSyncRemoteHostsEndpointResponse409
    | PutServicesBINDSyncRemoteHostsEndpointResponse415
    | PutServicesBINDSyncRemoteHostsEndpointResponse422
    | PutServicesBINDSyncRemoteHostsEndpointResponse424
    | PutServicesBINDSyncRemoteHostsEndpointResponse500
    | PutServicesBINDSyncRemoteHostsEndpointResponse503
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
    body: list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem]
    | list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesBINDSyncRemoteHostsEndpointResponse400
    | PutServicesBINDSyncRemoteHostsEndpointResponse401
    | PutServicesBINDSyncRemoteHostsEndpointResponse403
    | PutServicesBINDSyncRemoteHostsEndpointResponse404
    | PutServicesBINDSyncRemoteHostsEndpointResponse405
    | PutServicesBINDSyncRemoteHostsEndpointResponse406
    | PutServicesBINDSyncRemoteHostsEndpointResponse409
    | PutServicesBINDSyncRemoteHostsEndpointResponse415
    | PutServicesBINDSyncRemoteHostsEndpointResponse422
    | PutServicesBINDSyncRemoteHostsEndpointResponse424
    | PutServicesBINDSyncRemoteHostsEndpointResponse500
    | PutServicesBINDSyncRemoteHostsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesBINDSyncRemoteHostsEndpointResponse400 | PutServicesBINDSyncRemoteHostsEndpointResponse401 | PutServicesBINDSyncRemoteHostsEndpointResponse403 | PutServicesBINDSyncRemoteHostsEndpointResponse404 | PutServicesBINDSyncRemoteHostsEndpointResponse405 | PutServicesBINDSyncRemoteHostsEndpointResponse406 | PutServicesBINDSyncRemoteHostsEndpointResponse409 | PutServicesBINDSyncRemoteHostsEndpointResponse415 | PutServicesBINDSyncRemoteHostsEndpointResponse422 | PutServicesBINDSyncRemoteHostsEndpointResponse424 | PutServicesBINDSyncRemoteHostsEndpointResponse500 | PutServicesBINDSyncRemoteHostsEndpointResponse503]
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
    body: list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem]
    | list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesBINDSyncRemoteHostsEndpointResponse400
    | PutServicesBINDSyncRemoteHostsEndpointResponse401
    | PutServicesBINDSyncRemoteHostsEndpointResponse403
    | PutServicesBINDSyncRemoteHostsEndpointResponse404
    | PutServicesBINDSyncRemoteHostsEndpointResponse405
    | PutServicesBINDSyncRemoteHostsEndpointResponse406
    | PutServicesBINDSyncRemoteHostsEndpointResponse409
    | PutServicesBINDSyncRemoteHostsEndpointResponse415
    | PutServicesBINDSyncRemoteHostsEndpointResponse422
    | PutServicesBINDSyncRemoteHostsEndpointResponse424
    | PutServicesBINDSyncRemoteHostsEndpointResponse500
    | PutServicesBINDSyncRemoteHostsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesBINDSyncRemoteHostsEndpointResponse400 | PutServicesBINDSyncRemoteHostsEndpointResponse401 | PutServicesBINDSyncRemoteHostsEndpointResponse403 | PutServicesBINDSyncRemoteHostsEndpointResponse404 | PutServicesBINDSyncRemoteHostsEndpointResponse405 | PutServicesBINDSyncRemoteHostsEndpointResponse406 | PutServicesBINDSyncRemoteHostsEndpointResponse409 | PutServicesBINDSyncRemoteHostsEndpointResponse415 | PutServicesBINDSyncRemoteHostsEndpointResponse422 | PutServicesBINDSyncRemoteHostsEndpointResponse424 | PutServicesBINDSyncRemoteHostsEndpointResponse500 | PutServicesBINDSyncRemoteHostsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem]
    | list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesBINDSyncRemoteHostsEndpointResponse400
    | PutServicesBINDSyncRemoteHostsEndpointResponse401
    | PutServicesBINDSyncRemoteHostsEndpointResponse403
    | PutServicesBINDSyncRemoteHostsEndpointResponse404
    | PutServicesBINDSyncRemoteHostsEndpointResponse405
    | PutServicesBINDSyncRemoteHostsEndpointResponse406
    | PutServicesBINDSyncRemoteHostsEndpointResponse409
    | PutServicesBINDSyncRemoteHostsEndpointResponse415
    | PutServicesBINDSyncRemoteHostsEndpointResponse422
    | PutServicesBINDSyncRemoteHostsEndpointResponse424
    | PutServicesBINDSyncRemoteHostsEndpointResponse500
    | PutServicesBINDSyncRemoteHostsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesBINDSyncRemoteHostsEndpointResponse400 | PutServicesBINDSyncRemoteHostsEndpointResponse401 | PutServicesBINDSyncRemoteHostsEndpointResponse403 | PutServicesBINDSyncRemoteHostsEndpointResponse404 | PutServicesBINDSyncRemoteHostsEndpointResponse405 | PutServicesBINDSyncRemoteHostsEndpointResponse406 | PutServicesBINDSyncRemoteHostsEndpointResponse409 | PutServicesBINDSyncRemoteHostsEndpointResponse415 | PutServicesBINDSyncRemoteHostsEndpointResponse422 | PutServicesBINDSyncRemoteHostsEndpointResponse424 | PutServicesBINDSyncRemoteHostsEndpointResponse500 | PutServicesBINDSyncRemoteHostsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem]
    | list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesBINDSyncRemoteHostsEndpointResponse400
    | PutServicesBINDSyncRemoteHostsEndpointResponse401
    | PutServicesBINDSyncRemoteHostsEndpointResponse403
    | PutServicesBINDSyncRemoteHostsEndpointResponse404
    | PutServicesBINDSyncRemoteHostsEndpointResponse405
    | PutServicesBINDSyncRemoteHostsEndpointResponse406
    | PutServicesBINDSyncRemoteHostsEndpointResponse409
    | PutServicesBINDSyncRemoteHostsEndpointResponse415
    | PutServicesBINDSyncRemoteHostsEndpointResponse422
    | PutServicesBINDSyncRemoteHostsEndpointResponse424
    | PutServicesBINDSyncRemoteHostsEndpointResponse500
    | PutServicesBINDSyncRemoteHostsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-put ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesBINDSyncRemoteHostsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesBINDSyncRemoteHostsEndpointResponse400 | PutServicesBINDSyncRemoteHostsEndpointResponse401 | PutServicesBINDSyncRemoteHostsEndpointResponse403 | PutServicesBINDSyncRemoteHostsEndpointResponse404 | PutServicesBINDSyncRemoteHostsEndpointResponse405 | PutServicesBINDSyncRemoteHostsEndpointResponse406 | PutServicesBINDSyncRemoteHostsEndpointResponse409 | PutServicesBINDSyncRemoteHostsEndpointResponse415 | PutServicesBINDSyncRemoteHostsEndpointResponse422 | PutServicesBINDSyncRemoteHostsEndpointResponse424 | PutServicesBINDSyncRemoteHostsEndpointResponse500 | PutServicesBINDSyncRemoteHostsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
