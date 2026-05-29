from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_ha_proxy_backends_endpoint_data_body_item import (
    PutServicesHAProxyBackendsEndpointDataBodyItem,
)
from ...models.put_services_ha_proxy_backends_endpoint_json_body_item import (
    PutServicesHAProxyBackendsEndpointJsonBodyItem,
)
from ...models.put_services_ha_proxy_backends_endpoint_response_400 import PutServicesHAProxyBackendsEndpointResponse400
from ...models.put_services_ha_proxy_backends_endpoint_response_401 import PutServicesHAProxyBackendsEndpointResponse401
from ...models.put_services_ha_proxy_backends_endpoint_response_403 import PutServicesHAProxyBackendsEndpointResponse403
from ...models.put_services_ha_proxy_backends_endpoint_response_404 import PutServicesHAProxyBackendsEndpointResponse404
from ...models.put_services_ha_proxy_backends_endpoint_response_405 import PutServicesHAProxyBackendsEndpointResponse405
from ...models.put_services_ha_proxy_backends_endpoint_response_406 import PutServicesHAProxyBackendsEndpointResponse406
from ...models.put_services_ha_proxy_backends_endpoint_response_409 import PutServicesHAProxyBackendsEndpointResponse409
from ...models.put_services_ha_proxy_backends_endpoint_response_415 import PutServicesHAProxyBackendsEndpointResponse415
from ...models.put_services_ha_proxy_backends_endpoint_response_422 import PutServicesHAProxyBackendsEndpointResponse422
from ...models.put_services_ha_proxy_backends_endpoint_response_424 import PutServicesHAProxyBackendsEndpointResponse424
from ...models.put_services_ha_proxy_backends_endpoint_response_500 import PutServicesHAProxyBackendsEndpointResponse500
from ...models.put_services_ha_proxy_backends_endpoint_response_503 import PutServicesHAProxyBackendsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesHAProxyBackendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyBackendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/haproxy/backends",
    }

    if isinstance(body, list[PutServicesHAProxyBackendsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesHAProxyBackendsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesHAProxyBackendsEndpointResponse400
    | PutServicesHAProxyBackendsEndpointResponse401
    | PutServicesHAProxyBackendsEndpointResponse403
    | PutServicesHAProxyBackendsEndpointResponse404
    | PutServicesHAProxyBackendsEndpointResponse405
    | PutServicesHAProxyBackendsEndpointResponse406
    | PutServicesHAProxyBackendsEndpointResponse409
    | PutServicesHAProxyBackendsEndpointResponse415
    | PutServicesHAProxyBackendsEndpointResponse422
    | PutServicesHAProxyBackendsEndpointResponse424
    | PutServicesHAProxyBackendsEndpointResponse500
    | PutServicesHAProxyBackendsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesHAProxyBackendsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesHAProxyBackendsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesHAProxyBackendsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesHAProxyBackendsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesHAProxyBackendsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesHAProxyBackendsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesHAProxyBackendsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesHAProxyBackendsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesHAProxyBackendsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesHAProxyBackendsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesHAProxyBackendsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesHAProxyBackendsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesHAProxyBackendsEndpointResponse400
    | PutServicesHAProxyBackendsEndpointResponse401
    | PutServicesHAProxyBackendsEndpointResponse403
    | PutServicesHAProxyBackendsEndpointResponse404
    | PutServicesHAProxyBackendsEndpointResponse405
    | PutServicesHAProxyBackendsEndpointResponse406
    | PutServicesHAProxyBackendsEndpointResponse409
    | PutServicesHAProxyBackendsEndpointResponse415
    | PutServicesHAProxyBackendsEndpointResponse422
    | PutServicesHAProxyBackendsEndpointResponse424
    | PutServicesHAProxyBackendsEndpointResponse500
    | PutServicesHAProxyBackendsEndpointResponse503
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
    body: list[PutServicesHAProxyBackendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyBackendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesHAProxyBackendsEndpointResponse400
    | PutServicesHAProxyBackendsEndpointResponse401
    | PutServicesHAProxyBackendsEndpointResponse403
    | PutServicesHAProxyBackendsEndpointResponse404
    | PutServicesHAProxyBackendsEndpointResponse405
    | PutServicesHAProxyBackendsEndpointResponse406
    | PutServicesHAProxyBackendsEndpointResponse409
    | PutServicesHAProxyBackendsEndpointResponse415
    | PutServicesHAProxyBackendsEndpointResponse422
    | PutServicesHAProxyBackendsEndpointResponse424
    | PutServicesHAProxyBackendsEndpointResponse500
    | PutServicesHAProxyBackendsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing HAProxy Backends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyBackendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyBackendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesHAProxyBackendsEndpointResponse400 | PutServicesHAProxyBackendsEndpointResponse401 | PutServicesHAProxyBackendsEndpointResponse403 | PutServicesHAProxyBackendsEndpointResponse404 | PutServicesHAProxyBackendsEndpointResponse405 | PutServicesHAProxyBackendsEndpointResponse406 | PutServicesHAProxyBackendsEndpointResponse409 | PutServicesHAProxyBackendsEndpointResponse415 | PutServicesHAProxyBackendsEndpointResponse422 | PutServicesHAProxyBackendsEndpointResponse424 | PutServicesHAProxyBackendsEndpointResponse500 | PutServicesHAProxyBackendsEndpointResponse503]
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
    body: list[PutServicesHAProxyBackendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyBackendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesHAProxyBackendsEndpointResponse400
    | PutServicesHAProxyBackendsEndpointResponse401
    | PutServicesHAProxyBackendsEndpointResponse403
    | PutServicesHAProxyBackendsEndpointResponse404
    | PutServicesHAProxyBackendsEndpointResponse405
    | PutServicesHAProxyBackendsEndpointResponse406
    | PutServicesHAProxyBackendsEndpointResponse409
    | PutServicesHAProxyBackendsEndpointResponse415
    | PutServicesHAProxyBackendsEndpointResponse422
    | PutServicesHAProxyBackendsEndpointResponse424
    | PutServicesHAProxyBackendsEndpointResponse500
    | PutServicesHAProxyBackendsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing HAProxy Backends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyBackendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyBackendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesHAProxyBackendsEndpointResponse400 | PutServicesHAProxyBackendsEndpointResponse401 | PutServicesHAProxyBackendsEndpointResponse403 | PutServicesHAProxyBackendsEndpointResponse404 | PutServicesHAProxyBackendsEndpointResponse405 | PutServicesHAProxyBackendsEndpointResponse406 | PutServicesHAProxyBackendsEndpointResponse409 | PutServicesHAProxyBackendsEndpointResponse415 | PutServicesHAProxyBackendsEndpointResponse422 | PutServicesHAProxyBackendsEndpointResponse424 | PutServicesHAProxyBackendsEndpointResponse500 | PutServicesHAProxyBackendsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesHAProxyBackendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyBackendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesHAProxyBackendsEndpointResponse400
    | PutServicesHAProxyBackendsEndpointResponse401
    | PutServicesHAProxyBackendsEndpointResponse403
    | PutServicesHAProxyBackendsEndpointResponse404
    | PutServicesHAProxyBackendsEndpointResponse405
    | PutServicesHAProxyBackendsEndpointResponse406
    | PutServicesHAProxyBackendsEndpointResponse409
    | PutServicesHAProxyBackendsEndpointResponse415
    | PutServicesHAProxyBackendsEndpointResponse422
    | PutServicesHAProxyBackendsEndpointResponse424
    | PutServicesHAProxyBackendsEndpointResponse500
    | PutServicesHAProxyBackendsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing HAProxy Backends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyBackendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyBackendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesHAProxyBackendsEndpointResponse400 | PutServicesHAProxyBackendsEndpointResponse401 | PutServicesHAProxyBackendsEndpointResponse403 | PutServicesHAProxyBackendsEndpointResponse404 | PutServicesHAProxyBackendsEndpointResponse405 | PutServicesHAProxyBackendsEndpointResponse406 | PutServicesHAProxyBackendsEndpointResponse409 | PutServicesHAProxyBackendsEndpointResponse415 | PutServicesHAProxyBackendsEndpointResponse422 | PutServicesHAProxyBackendsEndpointResponse424 | PutServicesHAProxyBackendsEndpointResponse500 | PutServicesHAProxyBackendsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesHAProxyBackendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyBackendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesHAProxyBackendsEndpointResponse400
    | PutServicesHAProxyBackendsEndpointResponse401
    | PutServicesHAProxyBackendsEndpointResponse403
    | PutServicesHAProxyBackendsEndpointResponse404
    | PutServicesHAProxyBackendsEndpointResponse405
    | PutServicesHAProxyBackendsEndpointResponse406
    | PutServicesHAProxyBackendsEndpointResponse409
    | PutServicesHAProxyBackendsEndpointResponse415
    | PutServicesHAProxyBackendsEndpointResponse422
    | PutServicesHAProxyBackendsEndpointResponse424
    | PutServicesHAProxyBackendsEndpointResponse500
    | PutServicesHAProxyBackendsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing HAProxy Backends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyBackendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyBackendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesHAProxyBackendsEndpointResponse400 | PutServicesHAProxyBackendsEndpointResponse401 | PutServicesHAProxyBackendsEndpointResponse403 | PutServicesHAProxyBackendsEndpointResponse404 | PutServicesHAProxyBackendsEndpointResponse405 | PutServicesHAProxyBackendsEndpointResponse406 | PutServicesHAProxyBackendsEndpointResponse409 | PutServicesHAProxyBackendsEndpointResponse415 | PutServicesHAProxyBackendsEndpointResponse422 | PutServicesHAProxyBackendsEndpointResponse424 | PutServicesHAProxyBackendsEndpointResponse500 | PutServicesHAProxyBackendsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
