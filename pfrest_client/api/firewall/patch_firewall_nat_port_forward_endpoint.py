from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_nat_port_forward_endpoint_data_body import PatchFirewallNATPortForwardEndpointDataBody
from ...models.patch_firewall_nat_port_forward_endpoint_json_body import PatchFirewallNATPortForwardEndpointJsonBody
from ...models.patch_firewall_nat_port_forward_endpoint_response_400 import (
    PatchFirewallNATPortForwardEndpointResponse400,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_401 import (
    PatchFirewallNATPortForwardEndpointResponse401,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_403 import (
    PatchFirewallNATPortForwardEndpointResponse403,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_404 import (
    PatchFirewallNATPortForwardEndpointResponse404,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_405 import (
    PatchFirewallNATPortForwardEndpointResponse405,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_406 import (
    PatchFirewallNATPortForwardEndpointResponse406,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_409 import (
    PatchFirewallNATPortForwardEndpointResponse409,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_415 import (
    PatchFirewallNATPortForwardEndpointResponse415,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_422 import (
    PatchFirewallNATPortForwardEndpointResponse422,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_424 import (
    PatchFirewallNATPortForwardEndpointResponse424,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_500 import (
    PatchFirewallNATPortForwardEndpointResponse500,
)
from ...models.patch_firewall_nat_port_forward_endpoint_response_503 import (
    PatchFirewallNATPortForwardEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallNATPortForwardEndpointJsonBody | PatchFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/nat/port_forward",
    }

    if isinstance(body, PatchFirewallNATPortForwardEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallNATPortForwardEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallNATPortForwardEndpointResponse400
    | PatchFirewallNATPortForwardEndpointResponse401
    | PatchFirewallNATPortForwardEndpointResponse403
    | PatchFirewallNATPortForwardEndpointResponse404
    | PatchFirewallNATPortForwardEndpointResponse405
    | PatchFirewallNATPortForwardEndpointResponse406
    | PatchFirewallNATPortForwardEndpointResponse409
    | PatchFirewallNATPortForwardEndpointResponse415
    | PatchFirewallNATPortForwardEndpointResponse422
    | PatchFirewallNATPortForwardEndpointResponse424
    | PatchFirewallNATPortForwardEndpointResponse500
    | PatchFirewallNATPortForwardEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallNATPortForwardEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallNATPortForwardEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallNATPortForwardEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallNATPortForwardEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallNATPortForwardEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallNATPortForwardEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallNATPortForwardEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallNATPortForwardEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallNATPortForwardEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallNATPortForwardEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallNATPortForwardEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallNATPortForwardEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallNATPortForwardEndpointResponse400
    | PatchFirewallNATPortForwardEndpointResponse401
    | PatchFirewallNATPortForwardEndpointResponse403
    | PatchFirewallNATPortForwardEndpointResponse404
    | PatchFirewallNATPortForwardEndpointResponse405
    | PatchFirewallNATPortForwardEndpointResponse406
    | PatchFirewallNATPortForwardEndpointResponse409
    | PatchFirewallNATPortForwardEndpointResponse415
    | PatchFirewallNATPortForwardEndpointResponse422
    | PatchFirewallNATPortForwardEndpointResponse424
    | PatchFirewallNATPortForwardEndpointResponse500
    | PatchFirewallNATPortForwardEndpointResponse503
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
    body: PatchFirewallNATPortForwardEndpointJsonBody | PatchFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallNATPortForwardEndpointResponse400
    | PatchFirewallNATPortForwardEndpointResponse401
    | PatchFirewallNATPortForwardEndpointResponse403
    | PatchFirewallNATPortForwardEndpointResponse404
    | PatchFirewallNATPortForwardEndpointResponse405
    | PatchFirewallNATPortForwardEndpointResponse406
    | PatchFirewallNATPortForwardEndpointResponse409
    | PatchFirewallNATPortForwardEndpointResponse415
    | PatchFirewallNATPortForwardEndpointResponse422
    | PatchFirewallNATPortForwardEndpointResponse424
    | PatchFirewallNATPortForwardEndpointResponse500
    | PatchFirewallNATPortForwardEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PatchFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallNATPortForwardEndpointResponse400 | PatchFirewallNATPortForwardEndpointResponse401 | PatchFirewallNATPortForwardEndpointResponse403 | PatchFirewallNATPortForwardEndpointResponse404 | PatchFirewallNATPortForwardEndpointResponse405 | PatchFirewallNATPortForwardEndpointResponse406 | PatchFirewallNATPortForwardEndpointResponse409 | PatchFirewallNATPortForwardEndpointResponse415 | PatchFirewallNATPortForwardEndpointResponse422 | PatchFirewallNATPortForwardEndpointResponse424 | PatchFirewallNATPortForwardEndpointResponse500 | PatchFirewallNATPortForwardEndpointResponse503]
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
    body: PatchFirewallNATPortForwardEndpointJsonBody | PatchFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallNATPortForwardEndpointResponse400
    | PatchFirewallNATPortForwardEndpointResponse401
    | PatchFirewallNATPortForwardEndpointResponse403
    | PatchFirewallNATPortForwardEndpointResponse404
    | PatchFirewallNATPortForwardEndpointResponse405
    | PatchFirewallNATPortForwardEndpointResponse406
    | PatchFirewallNATPortForwardEndpointResponse409
    | PatchFirewallNATPortForwardEndpointResponse415
    | PatchFirewallNATPortForwardEndpointResponse422
    | PatchFirewallNATPortForwardEndpointResponse424
    | PatchFirewallNATPortForwardEndpointResponse500
    | PatchFirewallNATPortForwardEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PatchFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallNATPortForwardEndpointResponse400 | PatchFirewallNATPortForwardEndpointResponse401 | PatchFirewallNATPortForwardEndpointResponse403 | PatchFirewallNATPortForwardEndpointResponse404 | PatchFirewallNATPortForwardEndpointResponse405 | PatchFirewallNATPortForwardEndpointResponse406 | PatchFirewallNATPortForwardEndpointResponse409 | PatchFirewallNATPortForwardEndpointResponse415 | PatchFirewallNATPortForwardEndpointResponse422 | PatchFirewallNATPortForwardEndpointResponse424 | PatchFirewallNATPortForwardEndpointResponse500 | PatchFirewallNATPortForwardEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallNATPortForwardEndpointJsonBody | PatchFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallNATPortForwardEndpointResponse400
    | PatchFirewallNATPortForwardEndpointResponse401
    | PatchFirewallNATPortForwardEndpointResponse403
    | PatchFirewallNATPortForwardEndpointResponse404
    | PatchFirewallNATPortForwardEndpointResponse405
    | PatchFirewallNATPortForwardEndpointResponse406
    | PatchFirewallNATPortForwardEndpointResponse409
    | PatchFirewallNATPortForwardEndpointResponse415
    | PatchFirewallNATPortForwardEndpointResponse422
    | PatchFirewallNATPortForwardEndpointResponse424
    | PatchFirewallNATPortForwardEndpointResponse500
    | PatchFirewallNATPortForwardEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PatchFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallNATPortForwardEndpointResponse400 | PatchFirewallNATPortForwardEndpointResponse401 | PatchFirewallNATPortForwardEndpointResponse403 | PatchFirewallNATPortForwardEndpointResponse404 | PatchFirewallNATPortForwardEndpointResponse405 | PatchFirewallNATPortForwardEndpointResponse406 | PatchFirewallNATPortForwardEndpointResponse409 | PatchFirewallNATPortForwardEndpointResponse415 | PatchFirewallNATPortForwardEndpointResponse422 | PatchFirewallNATPortForwardEndpointResponse424 | PatchFirewallNATPortForwardEndpointResponse500 | PatchFirewallNATPortForwardEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallNATPortForwardEndpointJsonBody | PatchFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallNATPortForwardEndpointResponse400
    | PatchFirewallNATPortForwardEndpointResponse401
    | PatchFirewallNATPortForwardEndpointResponse403
    | PatchFirewallNATPortForwardEndpointResponse404
    | PatchFirewallNATPortForwardEndpointResponse405
    | PatchFirewallNATPortForwardEndpointResponse406
    | PatchFirewallNATPortForwardEndpointResponse409
    | PatchFirewallNATPortForwardEndpointResponse415
    | PatchFirewallNATPortForwardEndpointResponse422
    | PatchFirewallNATPortForwardEndpointResponse424
    | PatchFirewallNATPortForwardEndpointResponse500
    | PatchFirewallNATPortForwardEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PatchFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallNATPortForwardEndpointResponse400 | PatchFirewallNATPortForwardEndpointResponse401 | PatchFirewallNATPortForwardEndpointResponse403 | PatchFirewallNATPortForwardEndpointResponse404 | PatchFirewallNATPortForwardEndpointResponse405 | PatchFirewallNATPortForwardEndpointResponse406 | PatchFirewallNATPortForwardEndpointResponse409 | PatchFirewallNATPortForwardEndpointResponse415 | PatchFirewallNATPortForwardEndpointResponse422 | PatchFirewallNATPortForwardEndpointResponse424 | PatchFirewallNATPortForwardEndpointResponse500 | PatchFirewallNATPortForwardEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
