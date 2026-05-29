from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_ha_proxy_files_data_body_item import PutServicesHAProxyFilesDataBodyItem
from ...models.put_services_ha_proxy_files_json_body_item import PutServicesHAProxyFilesJsonBodyItem
from ...models.put_services_ha_proxy_files_response_400 import PutServicesHAProxyFilesResponse400
from ...models.put_services_ha_proxy_files_response_401 import PutServicesHAProxyFilesResponse401
from ...models.put_services_ha_proxy_files_response_403 import PutServicesHAProxyFilesResponse403
from ...models.put_services_ha_proxy_files_response_404 import PutServicesHAProxyFilesResponse404
from ...models.put_services_ha_proxy_files_response_405 import PutServicesHAProxyFilesResponse405
from ...models.put_services_ha_proxy_files_response_406 import PutServicesHAProxyFilesResponse406
from ...models.put_services_ha_proxy_files_response_409 import PutServicesHAProxyFilesResponse409
from ...models.put_services_ha_proxy_files_response_415 import PutServicesHAProxyFilesResponse415
from ...models.put_services_ha_proxy_files_response_422 import PutServicesHAProxyFilesResponse422
from ...models.put_services_ha_proxy_files_response_424 import PutServicesHAProxyFilesResponse424
from ...models.put_services_ha_proxy_files_response_500 import PutServicesHAProxyFilesResponse500
from ...models.put_services_ha_proxy_files_response_503 import PutServicesHAProxyFilesResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesHAProxyFilesJsonBodyItem] | list[PutServicesHAProxyFilesDataBodyItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/haproxy/files",
    }

    if isinstance(body, list[PutServicesHAProxyFilesJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesHAProxyFilesDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesHAProxyFilesResponse400
    | PutServicesHAProxyFilesResponse401
    | PutServicesHAProxyFilesResponse403
    | PutServicesHAProxyFilesResponse404
    | PutServicesHAProxyFilesResponse405
    | PutServicesHAProxyFilesResponse406
    | PutServicesHAProxyFilesResponse409
    | PutServicesHAProxyFilesResponse415
    | PutServicesHAProxyFilesResponse422
    | PutServicesHAProxyFilesResponse424
    | PutServicesHAProxyFilesResponse500
    | PutServicesHAProxyFilesResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesHAProxyFilesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesHAProxyFilesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesHAProxyFilesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesHAProxyFilesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesHAProxyFilesResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesHAProxyFilesResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesHAProxyFilesResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesHAProxyFilesResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesHAProxyFilesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesHAProxyFilesResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesHAProxyFilesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesHAProxyFilesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesHAProxyFilesResponse400
    | PutServicesHAProxyFilesResponse401
    | PutServicesHAProxyFilesResponse403
    | PutServicesHAProxyFilesResponse404
    | PutServicesHAProxyFilesResponse405
    | PutServicesHAProxyFilesResponse406
    | PutServicesHAProxyFilesResponse409
    | PutServicesHAProxyFilesResponse415
    | PutServicesHAProxyFilesResponse422
    | PutServicesHAProxyFilesResponse424
    | PutServicesHAProxyFilesResponse500
    | PutServicesHAProxyFilesResponse503
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
    body: list[PutServicesHAProxyFilesJsonBodyItem] | list[PutServicesHAProxyFilesDataBodyItem] | Unset = UNSET,
) -> Response[
    PutServicesHAProxyFilesResponse400
    | PutServicesHAProxyFilesResponse401
    | PutServicesHAProxyFilesResponse403
    | PutServicesHAProxyFilesResponse404
    | PutServicesHAProxyFilesResponse405
    | PutServicesHAProxyFilesResponse406
    | PutServicesHAProxyFilesResponse409
    | PutServicesHAProxyFilesResponse415
    | PutServicesHAProxyFilesResponse422
    | PutServicesHAProxyFilesResponse424
    | PutServicesHAProxyFilesResponse500
    | PutServicesHAProxyFilesResponse503
]:
    """<h3>Description:</h3>Replaces all existing HAProxy Files.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-files-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFilesJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFilesDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesHAProxyFilesResponse400 | PutServicesHAProxyFilesResponse401 | PutServicesHAProxyFilesResponse403 | PutServicesHAProxyFilesResponse404 | PutServicesHAProxyFilesResponse405 | PutServicesHAProxyFilesResponse406 | PutServicesHAProxyFilesResponse409 | PutServicesHAProxyFilesResponse415 | PutServicesHAProxyFilesResponse422 | PutServicesHAProxyFilesResponse424 | PutServicesHAProxyFilesResponse500 | PutServicesHAProxyFilesResponse503]
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
    body: list[PutServicesHAProxyFilesJsonBodyItem] | list[PutServicesHAProxyFilesDataBodyItem] | Unset = UNSET,
) -> (
    PutServicesHAProxyFilesResponse400
    | PutServicesHAProxyFilesResponse401
    | PutServicesHAProxyFilesResponse403
    | PutServicesHAProxyFilesResponse404
    | PutServicesHAProxyFilesResponse405
    | PutServicesHAProxyFilesResponse406
    | PutServicesHAProxyFilesResponse409
    | PutServicesHAProxyFilesResponse415
    | PutServicesHAProxyFilesResponse422
    | PutServicesHAProxyFilesResponse424
    | PutServicesHAProxyFilesResponse500
    | PutServicesHAProxyFilesResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing HAProxy Files.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-files-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFilesJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFilesDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesHAProxyFilesResponse400 | PutServicesHAProxyFilesResponse401 | PutServicesHAProxyFilesResponse403 | PutServicesHAProxyFilesResponse404 | PutServicesHAProxyFilesResponse405 | PutServicesHAProxyFilesResponse406 | PutServicesHAProxyFilesResponse409 | PutServicesHAProxyFilesResponse415 | PutServicesHAProxyFilesResponse422 | PutServicesHAProxyFilesResponse424 | PutServicesHAProxyFilesResponse500 | PutServicesHAProxyFilesResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesHAProxyFilesJsonBodyItem] | list[PutServicesHAProxyFilesDataBodyItem] | Unset = UNSET,
) -> Response[
    PutServicesHAProxyFilesResponse400
    | PutServicesHAProxyFilesResponse401
    | PutServicesHAProxyFilesResponse403
    | PutServicesHAProxyFilesResponse404
    | PutServicesHAProxyFilesResponse405
    | PutServicesHAProxyFilesResponse406
    | PutServicesHAProxyFilesResponse409
    | PutServicesHAProxyFilesResponse415
    | PutServicesHAProxyFilesResponse422
    | PutServicesHAProxyFilesResponse424
    | PutServicesHAProxyFilesResponse500
    | PutServicesHAProxyFilesResponse503
]:
    """<h3>Description:</h3>Replaces all existing HAProxy Files.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-files-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFilesJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFilesDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesHAProxyFilesResponse400 | PutServicesHAProxyFilesResponse401 | PutServicesHAProxyFilesResponse403 | PutServicesHAProxyFilesResponse404 | PutServicesHAProxyFilesResponse405 | PutServicesHAProxyFilesResponse406 | PutServicesHAProxyFilesResponse409 | PutServicesHAProxyFilesResponse415 | PutServicesHAProxyFilesResponse422 | PutServicesHAProxyFilesResponse424 | PutServicesHAProxyFilesResponse500 | PutServicesHAProxyFilesResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesHAProxyFilesJsonBodyItem] | list[PutServicesHAProxyFilesDataBodyItem] | Unset = UNSET,
) -> (
    PutServicesHAProxyFilesResponse400
    | PutServicesHAProxyFilesResponse401
    | PutServicesHAProxyFilesResponse403
    | PutServicesHAProxyFilesResponse404
    | PutServicesHAProxyFilesResponse405
    | PutServicesHAProxyFilesResponse406
    | PutServicesHAProxyFilesResponse409
    | PutServicesHAProxyFilesResponse415
    | PutServicesHAProxyFilesResponse422
    | PutServicesHAProxyFilesResponse424
    | PutServicesHAProxyFilesResponse500
    | PutServicesHAProxyFilesResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing HAProxy Files.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-files-put ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesHAProxyFilesJsonBodyItem] | Unset):
        body (list[PutServicesHAProxyFilesDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesHAProxyFilesResponse400 | PutServicesHAProxyFilesResponse401 | PutServicesHAProxyFilesResponse403 | PutServicesHAProxyFilesResponse404 | PutServicesHAProxyFilesResponse405 | PutServicesHAProxyFilesResponse406 | PutServicesHAProxyFilesResponse409 | PutServicesHAProxyFilesResponse415 | PutServicesHAProxyFilesResponse422 | PutServicesHAProxyFilesResponse424 | PutServicesHAProxyFilesResponse500 | PutServicesHAProxyFilesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
