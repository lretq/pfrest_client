from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_ha_proxy_frontends_endpoint_data_body_item import (
    PutServicesHAProxyFrontendsEndpointDataBodyItem,
)
from ...models.put_services_ha_proxy_frontends_endpoint_json_body_item import (
    PutServicesHAProxyFrontendsEndpointJsonBodyItem,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_400 import (
    PutServicesHAProxyFrontendsEndpointResponse400,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_401 import (
    PutServicesHAProxyFrontendsEndpointResponse401,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_403 import (
    PutServicesHAProxyFrontendsEndpointResponse403,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_404 import (
    PutServicesHAProxyFrontendsEndpointResponse404,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_405 import (
    PutServicesHAProxyFrontendsEndpointResponse405,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_406 import (
    PutServicesHAProxyFrontendsEndpointResponse406,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_409 import (
    PutServicesHAProxyFrontendsEndpointResponse409,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_415 import (
    PutServicesHAProxyFrontendsEndpointResponse415,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_422 import (
    PutServicesHAProxyFrontendsEndpointResponse422,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_424 import (
    PutServicesHAProxyFrontendsEndpointResponse424,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_500 import (
    PutServicesHAProxyFrontendsEndpointResponse500,
)
from ...models.put_services_ha_proxy_frontends_endpoint_response_503 import (
    PutServicesHAProxyFrontendsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesHAProxyFrontendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyFrontendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/haproxy/frontends",
    }

    if isinstance(body, list[PutServicesHAProxyFrontendsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesHAProxyFrontendsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesHAProxyFrontendsEndpointResponse400
    | PutServicesHAProxyFrontendsEndpointResponse401
    | PutServicesHAProxyFrontendsEndpointResponse403
    | PutServicesHAProxyFrontendsEndpointResponse404
    | PutServicesHAProxyFrontendsEndpointResponse405
    | PutServicesHAProxyFrontendsEndpointResponse406
    | PutServicesHAProxyFrontendsEndpointResponse409
    | PutServicesHAProxyFrontendsEndpointResponse415
    | PutServicesHAProxyFrontendsEndpointResponse422
    | PutServicesHAProxyFrontendsEndpointResponse424
    | PutServicesHAProxyFrontendsEndpointResponse500
    | PutServicesHAProxyFrontendsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesHAProxyFrontendsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesHAProxyFrontendsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesHAProxyFrontendsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesHAProxyFrontendsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesHAProxyFrontendsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesHAProxyFrontendsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesHAProxyFrontendsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesHAProxyFrontendsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesHAProxyFrontendsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesHAProxyFrontendsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesHAProxyFrontendsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesHAProxyFrontendsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesHAProxyFrontendsEndpointResponse400
    | PutServicesHAProxyFrontendsEndpointResponse401
    | PutServicesHAProxyFrontendsEndpointResponse403
    | PutServicesHAProxyFrontendsEndpointResponse404
    | PutServicesHAProxyFrontendsEndpointResponse405
    | PutServicesHAProxyFrontendsEndpointResponse406
    | PutServicesHAProxyFrontendsEndpointResponse409
    | PutServicesHAProxyFrontendsEndpointResponse415
    | PutServicesHAProxyFrontendsEndpointResponse422
    | PutServicesHAProxyFrontendsEndpointResponse424
    | PutServicesHAProxyFrontendsEndpointResponse500
    | PutServicesHAProxyFrontendsEndpointResponse503
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
    body: list[PutServicesHAProxyFrontendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyFrontendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesHAProxyFrontendsEndpointResponse400
    | PutServicesHAProxyFrontendsEndpointResponse401
    | PutServicesHAProxyFrontendsEndpointResponse403
    | PutServicesHAProxyFrontendsEndpointResponse404
    | PutServicesHAProxyFrontendsEndpointResponse405
    | PutServicesHAProxyFrontendsEndpointResponse406
    | PutServicesHAProxyFrontendsEndpointResponse409
    | PutServicesHAProxyFrontendsEndpointResponse415
    | PutServicesHAProxyFrontendsEndpointResponse422
    | PutServicesHAProxyFrontendsEndpointResponse424
    | PutServicesHAProxyFrontendsEndpointResponse500
    | PutServicesHAProxyFrontendsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing HAProxy Frontends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFrontendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFrontendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesHAProxyFrontendsEndpointResponse400 | PutServicesHAProxyFrontendsEndpointResponse401 | PutServicesHAProxyFrontendsEndpointResponse403 | PutServicesHAProxyFrontendsEndpointResponse404 | PutServicesHAProxyFrontendsEndpointResponse405 | PutServicesHAProxyFrontendsEndpointResponse406 | PutServicesHAProxyFrontendsEndpointResponse409 | PutServicesHAProxyFrontendsEndpointResponse415 | PutServicesHAProxyFrontendsEndpointResponse422 | PutServicesHAProxyFrontendsEndpointResponse424 | PutServicesHAProxyFrontendsEndpointResponse500 | PutServicesHAProxyFrontendsEndpointResponse503]
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
    body: list[PutServicesHAProxyFrontendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyFrontendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesHAProxyFrontendsEndpointResponse400
    | PutServicesHAProxyFrontendsEndpointResponse401
    | PutServicesHAProxyFrontendsEndpointResponse403
    | PutServicesHAProxyFrontendsEndpointResponse404
    | PutServicesHAProxyFrontendsEndpointResponse405
    | PutServicesHAProxyFrontendsEndpointResponse406
    | PutServicesHAProxyFrontendsEndpointResponse409
    | PutServicesHAProxyFrontendsEndpointResponse415
    | PutServicesHAProxyFrontendsEndpointResponse422
    | PutServicesHAProxyFrontendsEndpointResponse424
    | PutServicesHAProxyFrontendsEndpointResponse500
    | PutServicesHAProxyFrontendsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing HAProxy Frontends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFrontendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFrontendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesHAProxyFrontendsEndpointResponse400 | PutServicesHAProxyFrontendsEndpointResponse401 | PutServicesHAProxyFrontendsEndpointResponse403 | PutServicesHAProxyFrontendsEndpointResponse404 | PutServicesHAProxyFrontendsEndpointResponse405 | PutServicesHAProxyFrontendsEndpointResponse406 | PutServicesHAProxyFrontendsEndpointResponse409 | PutServicesHAProxyFrontendsEndpointResponse415 | PutServicesHAProxyFrontendsEndpointResponse422 | PutServicesHAProxyFrontendsEndpointResponse424 | PutServicesHAProxyFrontendsEndpointResponse500 | PutServicesHAProxyFrontendsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesHAProxyFrontendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyFrontendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesHAProxyFrontendsEndpointResponse400
    | PutServicesHAProxyFrontendsEndpointResponse401
    | PutServicesHAProxyFrontendsEndpointResponse403
    | PutServicesHAProxyFrontendsEndpointResponse404
    | PutServicesHAProxyFrontendsEndpointResponse405
    | PutServicesHAProxyFrontendsEndpointResponse406
    | PutServicesHAProxyFrontendsEndpointResponse409
    | PutServicesHAProxyFrontendsEndpointResponse415
    | PutServicesHAProxyFrontendsEndpointResponse422
    | PutServicesHAProxyFrontendsEndpointResponse424
    | PutServicesHAProxyFrontendsEndpointResponse500
    | PutServicesHAProxyFrontendsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing HAProxy Frontends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFrontendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFrontendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesHAProxyFrontendsEndpointResponse400 | PutServicesHAProxyFrontendsEndpointResponse401 | PutServicesHAProxyFrontendsEndpointResponse403 | PutServicesHAProxyFrontendsEndpointResponse404 | PutServicesHAProxyFrontendsEndpointResponse405 | PutServicesHAProxyFrontendsEndpointResponse406 | PutServicesHAProxyFrontendsEndpointResponse409 | PutServicesHAProxyFrontendsEndpointResponse415 | PutServicesHAProxyFrontendsEndpointResponse422 | PutServicesHAProxyFrontendsEndpointResponse424 | PutServicesHAProxyFrontendsEndpointResponse500 | PutServicesHAProxyFrontendsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesHAProxyFrontendsEndpointJsonBodyItem]
    | list[PutServicesHAProxyFrontendsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesHAProxyFrontendsEndpointResponse400
    | PutServicesHAProxyFrontendsEndpointResponse401
    | PutServicesHAProxyFrontendsEndpointResponse403
    | PutServicesHAProxyFrontendsEndpointResponse404
    | PutServicesHAProxyFrontendsEndpointResponse405
    | PutServicesHAProxyFrontendsEndpointResponse406
    | PutServicesHAProxyFrontendsEndpointResponse409
    | PutServicesHAProxyFrontendsEndpointResponse415
    | PutServicesHAProxyFrontendsEndpointResponse422
    | PutServicesHAProxyFrontendsEndpointResponse424
    | PutServicesHAProxyFrontendsEndpointResponse500
    | PutServicesHAProxyFrontendsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing HAProxy Frontends.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontends-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFrontendsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFrontendsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesHAProxyFrontendsEndpointResponse400 | PutServicesHAProxyFrontendsEndpointResponse401 | PutServicesHAProxyFrontendsEndpointResponse403 | PutServicesHAProxyFrontendsEndpointResponse404 | PutServicesHAProxyFrontendsEndpointResponse405 | PutServicesHAProxyFrontendsEndpointResponse406 | PutServicesHAProxyFrontendsEndpointResponse409 | PutServicesHAProxyFrontendsEndpointResponse415 | PutServicesHAProxyFrontendsEndpointResponse422 | PutServicesHAProxyFrontendsEndpointResponse424 | PutServicesHAProxyFrontendsEndpointResponse500 | PutServicesHAProxyFrontendsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
