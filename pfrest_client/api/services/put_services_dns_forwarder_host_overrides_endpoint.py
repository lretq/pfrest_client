from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_dns_forwarder_host_overrides_endpoint_data_body_item import (
    PutServicesDNSForwarderHostOverridesEndpointDataBodyItem,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_json_body_item import (
    PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_400 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse400,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_401 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse401,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_403 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse403,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_404 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse404,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_405 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse405,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_406 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse406,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_409 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse409,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_415 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse415,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_422 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse422,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_424 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse424,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_500 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse500,
)
from ...models.put_services_dns_forwarder_host_overrides_endpoint_response_503 import (
    PutServicesDNSForwarderHostOverridesEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/dns_forwarder/host_overrides",
    }

    if isinstance(body, list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesDNSForwarderHostOverridesEndpointResponse400
    | PutServicesDNSForwarderHostOverridesEndpointResponse401
    | PutServicesDNSForwarderHostOverridesEndpointResponse403
    | PutServicesDNSForwarderHostOverridesEndpointResponse404
    | PutServicesDNSForwarderHostOverridesEndpointResponse405
    | PutServicesDNSForwarderHostOverridesEndpointResponse406
    | PutServicesDNSForwarderHostOverridesEndpointResponse409
    | PutServicesDNSForwarderHostOverridesEndpointResponse415
    | PutServicesDNSForwarderHostOverridesEndpointResponse422
    | PutServicesDNSForwarderHostOverridesEndpointResponse424
    | PutServicesDNSForwarderHostOverridesEndpointResponse500
    | PutServicesDNSForwarderHostOverridesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesDNSForwarderHostOverridesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesDNSForwarderHostOverridesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesDNSForwarderHostOverridesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesDNSForwarderHostOverridesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesDNSForwarderHostOverridesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesDNSForwarderHostOverridesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesDNSForwarderHostOverridesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesDNSForwarderHostOverridesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesDNSForwarderHostOverridesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesDNSForwarderHostOverridesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesDNSForwarderHostOverridesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesDNSForwarderHostOverridesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesDNSForwarderHostOverridesEndpointResponse400
    | PutServicesDNSForwarderHostOverridesEndpointResponse401
    | PutServicesDNSForwarderHostOverridesEndpointResponse403
    | PutServicesDNSForwarderHostOverridesEndpointResponse404
    | PutServicesDNSForwarderHostOverridesEndpointResponse405
    | PutServicesDNSForwarderHostOverridesEndpointResponse406
    | PutServicesDNSForwarderHostOverridesEndpointResponse409
    | PutServicesDNSForwarderHostOverridesEndpointResponse415
    | PutServicesDNSForwarderHostOverridesEndpointResponse422
    | PutServicesDNSForwarderHostOverridesEndpointResponse424
    | PutServicesDNSForwarderHostOverridesEndpointResponse500
    | PutServicesDNSForwarderHostOverridesEndpointResponse503
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
    body: list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesDNSForwarderHostOverridesEndpointResponse400
    | PutServicesDNSForwarderHostOverridesEndpointResponse401
    | PutServicesDNSForwarderHostOverridesEndpointResponse403
    | PutServicesDNSForwarderHostOverridesEndpointResponse404
    | PutServicesDNSForwarderHostOverridesEndpointResponse405
    | PutServicesDNSForwarderHostOverridesEndpointResponse406
    | PutServicesDNSForwarderHostOverridesEndpointResponse409
    | PutServicesDNSForwarderHostOverridesEndpointResponse415
    | PutServicesDNSForwarderHostOverridesEndpointResponse422
    | PutServicesDNSForwarderHostOverridesEndpointResponse424
    | PutServicesDNSForwarderHostOverridesEndpointResponse500
    | PutServicesDNSForwarderHostOverridesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing DNS Forwarder Host
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-forwarder-host-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesDNSForwarderHostOverridesEndpointResponse400 | PutServicesDNSForwarderHostOverridesEndpointResponse401 | PutServicesDNSForwarderHostOverridesEndpointResponse403 | PutServicesDNSForwarderHostOverridesEndpointResponse404 | PutServicesDNSForwarderHostOverridesEndpointResponse405 | PutServicesDNSForwarderHostOverridesEndpointResponse406 | PutServicesDNSForwarderHostOverridesEndpointResponse409 | PutServicesDNSForwarderHostOverridesEndpointResponse415 | PutServicesDNSForwarderHostOverridesEndpointResponse422 | PutServicesDNSForwarderHostOverridesEndpointResponse424 | PutServicesDNSForwarderHostOverridesEndpointResponse500 | PutServicesDNSForwarderHostOverridesEndpointResponse503]
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
    body: list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesDNSForwarderHostOverridesEndpointResponse400
    | PutServicesDNSForwarderHostOverridesEndpointResponse401
    | PutServicesDNSForwarderHostOverridesEndpointResponse403
    | PutServicesDNSForwarderHostOverridesEndpointResponse404
    | PutServicesDNSForwarderHostOverridesEndpointResponse405
    | PutServicesDNSForwarderHostOverridesEndpointResponse406
    | PutServicesDNSForwarderHostOverridesEndpointResponse409
    | PutServicesDNSForwarderHostOverridesEndpointResponse415
    | PutServicesDNSForwarderHostOverridesEndpointResponse422
    | PutServicesDNSForwarderHostOverridesEndpointResponse424
    | PutServicesDNSForwarderHostOverridesEndpointResponse500
    | PutServicesDNSForwarderHostOverridesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing DNS Forwarder Host
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-forwarder-host-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesDNSForwarderHostOverridesEndpointResponse400 | PutServicesDNSForwarderHostOverridesEndpointResponse401 | PutServicesDNSForwarderHostOverridesEndpointResponse403 | PutServicesDNSForwarderHostOverridesEndpointResponse404 | PutServicesDNSForwarderHostOverridesEndpointResponse405 | PutServicesDNSForwarderHostOverridesEndpointResponse406 | PutServicesDNSForwarderHostOverridesEndpointResponse409 | PutServicesDNSForwarderHostOverridesEndpointResponse415 | PutServicesDNSForwarderHostOverridesEndpointResponse422 | PutServicesDNSForwarderHostOverridesEndpointResponse424 | PutServicesDNSForwarderHostOverridesEndpointResponse500 | PutServicesDNSForwarderHostOverridesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesDNSForwarderHostOverridesEndpointResponse400
    | PutServicesDNSForwarderHostOverridesEndpointResponse401
    | PutServicesDNSForwarderHostOverridesEndpointResponse403
    | PutServicesDNSForwarderHostOverridesEndpointResponse404
    | PutServicesDNSForwarderHostOverridesEndpointResponse405
    | PutServicesDNSForwarderHostOverridesEndpointResponse406
    | PutServicesDNSForwarderHostOverridesEndpointResponse409
    | PutServicesDNSForwarderHostOverridesEndpointResponse415
    | PutServicesDNSForwarderHostOverridesEndpointResponse422
    | PutServicesDNSForwarderHostOverridesEndpointResponse424
    | PutServicesDNSForwarderHostOverridesEndpointResponse500
    | PutServicesDNSForwarderHostOverridesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing DNS Forwarder Host
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-forwarder-host-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesDNSForwarderHostOverridesEndpointResponse400 | PutServicesDNSForwarderHostOverridesEndpointResponse401 | PutServicesDNSForwarderHostOverridesEndpointResponse403 | PutServicesDNSForwarderHostOverridesEndpointResponse404 | PutServicesDNSForwarderHostOverridesEndpointResponse405 | PutServicesDNSForwarderHostOverridesEndpointResponse406 | PutServicesDNSForwarderHostOverridesEndpointResponse409 | PutServicesDNSForwarderHostOverridesEndpointResponse415 | PutServicesDNSForwarderHostOverridesEndpointResponse422 | PutServicesDNSForwarderHostOverridesEndpointResponse424 | PutServicesDNSForwarderHostOverridesEndpointResponse500 | PutServicesDNSForwarderHostOverridesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem]
    | list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesDNSForwarderHostOverridesEndpointResponse400
    | PutServicesDNSForwarderHostOverridesEndpointResponse401
    | PutServicesDNSForwarderHostOverridesEndpointResponse403
    | PutServicesDNSForwarderHostOverridesEndpointResponse404
    | PutServicesDNSForwarderHostOverridesEndpointResponse405
    | PutServicesDNSForwarderHostOverridesEndpointResponse406
    | PutServicesDNSForwarderHostOverridesEndpointResponse409
    | PutServicesDNSForwarderHostOverridesEndpointResponse415
    | PutServicesDNSForwarderHostOverridesEndpointResponse422
    | PutServicesDNSForwarderHostOverridesEndpointResponse424
    | PutServicesDNSForwarderHostOverridesEndpointResponse500
    | PutServicesDNSForwarderHostOverridesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing DNS Forwarder Host
    Overrides.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**:
    DNSForwarderHostOverride<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-dns-forwarder-host-overrides-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesDNSForwarderHostOverridesEndpointJsonBodyItem] | Unset):
        body (list[PutServicesDNSForwarderHostOverridesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesDNSForwarderHostOverridesEndpointResponse400 | PutServicesDNSForwarderHostOverridesEndpointResponse401 | PutServicesDNSForwarderHostOverridesEndpointResponse403 | PutServicesDNSForwarderHostOverridesEndpointResponse404 | PutServicesDNSForwarderHostOverridesEndpointResponse405 | PutServicesDNSForwarderHostOverridesEndpointResponse406 | PutServicesDNSForwarderHostOverridesEndpointResponse409 | PutServicesDNSForwarderHostOverridesEndpointResponse415 | PutServicesDNSForwarderHostOverridesEndpointResponse422 | PutServicesDNSForwarderHostOverridesEndpointResponse424 | PutServicesDNSForwarderHostOverridesEndpointResponse500 | PutServicesDNSForwarderHostOverridesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
