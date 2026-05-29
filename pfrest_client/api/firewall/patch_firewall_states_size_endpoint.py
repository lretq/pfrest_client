from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_states_size_endpoint_data_body import PatchFirewallStatesSizeEndpointDataBody
from ...models.patch_firewall_states_size_endpoint_json_body import PatchFirewallStatesSizeEndpointJsonBody
from ...models.patch_firewall_states_size_endpoint_response_400 import PatchFirewallStatesSizeEndpointResponse400
from ...models.patch_firewall_states_size_endpoint_response_401 import PatchFirewallStatesSizeEndpointResponse401
from ...models.patch_firewall_states_size_endpoint_response_403 import PatchFirewallStatesSizeEndpointResponse403
from ...models.patch_firewall_states_size_endpoint_response_404 import PatchFirewallStatesSizeEndpointResponse404
from ...models.patch_firewall_states_size_endpoint_response_405 import PatchFirewallStatesSizeEndpointResponse405
from ...models.patch_firewall_states_size_endpoint_response_406 import PatchFirewallStatesSizeEndpointResponse406
from ...models.patch_firewall_states_size_endpoint_response_409 import PatchFirewallStatesSizeEndpointResponse409
from ...models.patch_firewall_states_size_endpoint_response_415 import PatchFirewallStatesSizeEndpointResponse415
from ...models.patch_firewall_states_size_endpoint_response_422 import PatchFirewallStatesSizeEndpointResponse422
from ...models.patch_firewall_states_size_endpoint_response_424 import PatchFirewallStatesSizeEndpointResponse424
from ...models.patch_firewall_states_size_endpoint_response_500 import PatchFirewallStatesSizeEndpointResponse500
from ...models.patch_firewall_states_size_endpoint_response_503 import PatchFirewallStatesSizeEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallStatesSizeEndpointJsonBody | PatchFirewallStatesSizeEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/states/size",
    }

    if isinstance(body, PatchFirewallStatesSizeEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallStatesSizeEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallStatesSizeEndpointResponse400
    | PatchFirewallStatesSizeEndpointResponse401
    | PatchFirewallStatesSizeEndpointResponse403
    | PatchFirewallStatesSizeEndpointResponse404
    | PatchFirewallStatesSizeEndpointResponse405
    | PatchFirewallStatesSizeEndpointResponse406
    | PatchFirewallStatesSizeEndpointResponse409
    | PatchFirewallStatesSizeEndpointResponse415
    | PatchFirewallStatesSizeEndpointResponse422
    | PatchFirewallStatesSizeEndpointResponse424
    | PatchFirewallStatesSizeEndpointResponse500
    | PatchFirewallStatesSizeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallStatesSizeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallStatesSizeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallStatesSizeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallStatesSizeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallStatesSizeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallStatesSizeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallStatesSizeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallStatesSizeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallStatesSizeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallStatesSizeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallStatesSizeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallStatesSizeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallStatesSizeEndpointResponse400
    | PatchFirewallStatesSizeEndpointResponse401
    | PatchFirewallStatesSizeEndpointResponse403
    | PatchFirewallStatesSizeEndpointResponse404
    | PatchFirewallStatesSizeEndpointResponse405
    | PatchFirewallStatesSizeEndpointResponse406
    | PatchFirewallStatesSizeEndpointResponse409
    | PatchFirewallStatesSizeEndpointResponse415
    | PatchFirewallStatesSizeEndpointResponse422
    | PatchFirewallStatesSizeEndpointResponse424
    | PatchFirewallStatesSizeEndpointResponse500
    | PatchFirewallStatesSizeEndpointResponse503
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
    body: PatchFirewallStatesSizeEndpointJsonBody | PatchFirewallStatesSizeEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallStatesSizeEndpointResponse400
    | PatchFirewallStatesSizeEndpointResponse401
    | PatchFirewallStatesSizeEndpointResponse403
    | PatchFirewallStatesSizeEndpointResponse404
    | PatchFirewallStatesSizeEndpointResponse405
    | PatchFirewallStatesSizeEndpointResponse406
    | PatchFirewallStatesSizeEndpointResponse409
    | PatchFirewallStatesSizeEndpointResponse415
    | PatchFirewallStatesSizeEndpointResponse422
    | PatchFirewallStatesSizeEndpointResponse424
    | PatchFirewallStatesSizeEndpointResponse500
    | PatchFirewallStatesSizeEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallStatesSizeEndpointJsonBody | Unset):
        body (PatchFirewallStatesSizeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallStatesSizeEndpointResponse400 | PatchFirewallStatesSizeEndpointResponse401 | PatchFirewallStatesSizeEndpointResponse403 | PatchFirewallStatesSizeEndpointResponse404 | PatchFirewallStatesSizeEndpointResponse405 | PatchFirewallStatesSizeEndpointResponse406 | PatchFirewallStatesSizeEndpointResponse409 | PatchFirewallStatesSizeEndpointResponse415 | PatchFirewallStatesSizeEndpointResponse422 | PatchFirewallStatesSizeEndpointResponse424 | PatchFirewallStatesSizeEndpointResponse500 | PatchFirewallStatesSizeEndpointResponse503]
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
    body: PatchFirewallStatesSizeEndpointJsonBody | PatchFirewallStatesSizeEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallStatesSizeEndpointResponse400
    | PatchFirewallStatesSizeEndpointResponse401
    | PatchFirewallStatesSizeEndpointResponse403
    | PatchFirewallStatesSizeEndpointResponse404
    | PatchFirewallStatesSizeEndpointResponse405
    | PatchFirewallStatesSizeEndpointResponse406
    | PatchFirewallStatesSizeEndpointResponse409
    | PatchFirewallStatesSizeEndpointResponse415
    | PatchFirewallStatesSizeEndpointResponse422
    | PatchFirewallStatesSizeEndpointResponse424
    | PatchFirewallStatesSizeEndpointResponse500
    | PatchFirewallStatesSizeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallStatesSizeEndpointJsonBody | Unset):
        body (PatchFirewallStatesSizeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallStatesSizeEndpointResponse400 | PatchFirewallStatesSizeEndpointResponse401 | PatchFirewallStatesSizeEndpointResponse403 | PatchFirewallStatesSizeEndpointResponse404 | PatchFirewallStatesSizeEndpointResponse405 | PatchFirewallStatesSizeEndpointResponse406 | PatchFirewallStatesSizeEndpointResponse409 | PatchFirewallStatesSizeEndpointResponse415 | PatchFirewallStatesSizeEndpointResponse422 | PatchFirewallStatesSizeEndpointResponse424 | PatchFirewallStatesSizeEndpointResponse500 | PatchFirewallStatesSizeEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallStatesSizeEndpointJsonBody | PatchFirewallStatesSizeEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallStatesSizeEndpointResponse400
    | PatchFirewallStatesSizeEndpointResponse401
    | PatchFirewallStatesSizeEndpointResponse403
    | PatchFirewallStatesSizeEndpointResponse404
    | PatchFirewallStatesSizeEndpointResponse405
    | PatchFirewallStatesSizeEndpointResponse406
    | PatchFirewallStatesSizeEndpointResponse409
    | PatchFirewallStatesSizeEndpointResponse415
    | PatchFirewallStatesSizeEndpointResponse422
    | PatchFirewallStatesSizeEndpointResponse424
    | PatchFirewallStatesSizeEndpointResponse500
    | PatchFirewallStatesSizeEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallStatesSizeEndpointJsonBody | Unset):
        body (PatchFirewallStatesSizeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallStatesSizeEndpointResponse400 | PatchFirewallStatesSizeEndpointResponse401 | PatchFirewallStatesSizeEndpointResponse403 | PatchFirewallStatesSizeEndpointResponse404 | PatchFirewallStatesSizeEndpointResponse405 | PatchFirewallStatesSizeEndpointResponse406 | PatchFirewallStatesSizeEndpointResponse409 | PatchFirewallStatesSizeEndpointResponse415 | PatchFirewallStatesSizeEndpointResponse422 | PatchFirewallStatesSizeEndpointResponse424 | PatchFirewallStatesSizeEndpointResponse500 | PatchFirewallStatesSizeEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallStatesSizeEndpointJsonBody | PatchFirewallStatesSizeEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallStatesSizeEndpointResponse400
    | PatchFirewallStatesSizeEndpointResponse401
    | PatchFirewallStatesSizeEndpointResponse403
    | PatchFirewallStatesSizeEndpointResponse404
    | PatchFirewallStatesSizeEndpointResponse405
    | PatchFirewallStatesSizeEndpointResponse406
    | PatchFirewallStatesSizeEndpointResponse409
    | PatchFirewallStatesSizeEndpointResponse415
    | PatchFirewallStatesSizeEndpointResponse422
    | PatchFirewallStatesSizeEndpointResponse424
    | PatchFirewallStatesSizeEndpointResponse500
    | PatchFirewallStatesSizeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallStatesSizeEndpointJsonBody | Unset):
        body (PatchFirewallStatesSizeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallStatesSizeEndpointResponse400 | PatchFirewallStatesSizeEndpointResponse401 | PatchFirewallStatesSizeEndpointResponse403 | PatchFirewallStatesSizeEndpointResponse404 | PatchFirewallStatesSizeEndpointResponse405 | PatchFirewallStatesSizeEndpointResponse406 | PatchFirewallStatesSizeEndpointResponse409 | PatchFirewallStatesSizeEndpointResponse415 | PatchFirewallStatesSizeEndpointResponse422 | PatchFirewallStatesSizeEndpointResponse424 | PatchFirewallStatesSizeEndpointResponse500 | PatchFirewallStatesSizeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
