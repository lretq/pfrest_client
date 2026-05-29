from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_vpni_psec_phase_2s_endpoint_data_body_item import PutVPNIPsecPhase2SEndpointDataBodyItem
from ...models.put_vpni_psec_phase_2s_endpoint_json_body_item import PutVPNIPsecPhase2SEndpointJsonBodyItem
from ...models.put_vpni_psec_phase_2s_endpoint_response_400 import PutVPNIPsecPhase2SEndpointResponse400
from ...models.put_vpni_psec_phase_2s_endpoint_response_401 import PutVPNIPsecPhase2SEndpointResponse401
from ...models.put_vpni_psec_phase_2s_endpoint_response_403 import PutVPNIPsecPhase2SEndpointResponse403
from ...models.put_vpni_psec_phase_2s_endpoint_response_404 import PutVPNIPsecPhase2SEndpointResponse404
from ...models.put_vpni_psec_phase_2s_endpoint_response_405 import PutVPNIPsecPhase2SEndpointResponse405
from ...models.put_vpni_psec_phase_2s_endpoint_response_406 import PutVPNIPsecPhase2SEndpointResponse406
from ...models.put_vpni_psec_phase_2s_endpoint_response_409 import PutVPNIPsecPhase2SEndpointResponse409
from ...models.put_vpni_psec_phase_2s_endpoint_response_415 import PutVPNIPsecPhase2SEndpointResponse415
from ...models.put_vpni_psec_phase_2s_endpoint_response_422 import PutVPNIPsecPhase2SEndpointResponse422
from ...models.put_vpni_psec_phase_2s_endpoint_response_424 import PutVPNIPsecPhase2SEndpointResponse424
from ...models.put_vpni_psec_phase_2s_endpoint_response_500 import PutVPNIPsecPhase2SEndpointResponse500
from ...models.put_vpni_psec_phase_2s_endpoint_response_503 import PutVPNIPsecPhase2SEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/vpn/ipsec/phase2s",
    }

    if isinstance(body, list[PutVPNIPsecPhase2SEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutVPNIPsecPhase2SEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutVPNIPsecPhase2SEndpointResponse400
    | PutVPNIPsecPhase2SEndpointResponse401
    | PutVPNIPsecPhase2SEndpointResponse403
    | PutVPNIPsecPhase2SEndpointResponse404
    | PutVPNIPsecPhase2SEndpointResponse405
    | PutVPNIPsecPhase2SEndpointResponse406
    | PutVPNIPsecPhase2SEndpointResponse409
    | PutVPNIPsecPhase2SEndpointResponse415
    | PutVPNIPsecPhase2SEndpointResponse422
    | PutVPNIPsecPhase2SEndpointResponse424
    | PutVPNIPsecPhase2SEndpointResponse500
    | PutVPNIPsecPhase2SEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutVPNIPsecPhase2SEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutVPNIPsecPhase2SEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutVPNIPsecPhase2SEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutVPNIPsecPhase2SEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutVPNIPsecPhase2SEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutVPNIPsecPhase2SEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutVPNIPsecPhase2SEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutVPNIPsecPhase2SEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutVPNIPsecPhase2SEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutVPNIPsecPhase2SEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutVPNIPsecPhase2SEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutVPNIPsecPhase2SEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutVPNIPsecPhase2SEndpointResponse400
    | PutVPNIPsecPhase2SEndpointResponse401
    | PutVPNIPsecPhase2SEndpointResponse403
    | PutVPNIPsecPhase2SEndpointResponse404
    | PutVPNIPsecPhase2SEndpointResponse405
    | PutVPNIPsecPhase2SEndpointResponse406
    | PutVPNIPsecPhase2SEndpointResponse409
    | PutVPNIPsecPhase2SEndpointResponse415
    | PutVPNIPsecPhase2SEndpointResponse422
    | PutVPNIPsecPhase2SEndpointResponse424
    | PutVPNIPsecPhase2SEndpointResponse500
    | PutVPNIPsecPhase2SEndpointResponse503
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
    body: list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutVPNIPsecPhase2SEndpointResponse400
    | PutVPNIPsecPhase2SEndpointResponse401
    | PutVPNIPsecPhase2SEndpointResponse403
    | PutVPNIPsecPhase2SEndpointResponse404
    | PutVPNIPsecPhase2SEndpointResponse405
    | PutVPNIPsecPhase2SEndpointResponse406
    | PutVPNIPsecPhase2SEndpointResponse409
    | PutVPNIPsecPhase2SEndpointResponse415
    | PutVPNIPsecPhase2SEndpointResponse422
    | PutVPNIPsecPhase2SEndpointResponse424
    | PutVPNIPsecPhase2SEndpointResponse500
    | PutVPNIPsecPhase2SEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing IPsec Phase 2s.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2s-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | Unset):
        body (list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNIPsecPhase2SEndpointResponse400 | PutVPNIPsecPhase2SEndpointResponse401 | PutVPNIPsecPhase2SEndpointResponse403 | PutVPNIPsecPhase2SEndpointResponse404 | PutVPNIPsecPhase2SEndpointResponse405 | PutVPNIPsecPhase2SEndpointResponse406 | PutVPNIPsecPhase2SEndpointResponse409 | PutVPNIPsecPhase2SEndpointResponse415 | PutVPNIPsecPhase2SEndpointResponse422 | PutVPNIPsecPhase2SEndpointResponse424 | PutVPNIPsecPhase2SEndpointResponse500 | PutVPNIPsecPhase2SEndpointResponse503]
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
    body: list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutVPNIPsecPhase2SEndpointResponse400
    | PutVPNIPsecPhase2SEndpointResponse401
    | PutVPNIPsecPhase2SEndpointResponse403
    | PutVPNIPsecPhase2SEndpointResponse404
    | PutVPNIPsecPhase2SEndpointResponse405
    | PutVPNIPsecPhase2SEndpointResponse406
    | PutVPNIPsecPhase2SEndpointResponse409
    | PutVPNIPsecPhase2SEndpointResponse415
    | PutVPNIPsecPhase2SEndpointResponse422
    | PutVPNIPsecPhase2SEndpointResponse424
    | PutVPNIPsecPhase2SEndpointResponse500
    | PutVPNIPsecPhase2SEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing IPsec Phase 2s.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2s-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | Unset):
        body (list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNIPsecPhase2SEndpointResponse400 | PutVPNIPsecPhase2SEndpointResponse401 | PutVPNIPsecPhase2SEndpointResponse403 | PutVPNIPsecPhase2SEndpointResponse404 | PutVPNIPsecPhase2SEndpointResponse405 | PutVPNIPsecPhase2SEndpointResponse406 | PutVPNIPsecPhase2SEndpointResponse409 | PutVPNIPsecPhase2SEndpointResponse415 | PutVPNIPsecPhase2SEndpointResponse422 | PutVPNIPsecPhase2SEndpointResponse424 | PutVPNIPsecPhase2SEndpointResponse500 | PutVPNIPsecPhase2SEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutVPNIPsecPhase2SEndpointResponse400
    | PutVPNIPsecPhase2SEndpointResponse401
    | PutVPNIPsecPhase2SEndpointResponse403
    | PutVPNIPsecPhase2SEndpointResponse404
    | PutVPNIPsecPhase2SEndpointResponse405
    | PutVPNIPsecPhase2SEndpointResponse406
    | PutVPNIPsecPhase2SEndpointResponse409
    | PutVPNIPsecPhase2SEndpointResponse415
    | PutVPNIPsecPhase2SEndpointResponse422
    | PutVPNIPsecPhase2SEndpointResponse424
    | PutVPNIPsecPhase2SEndpointResponse500
    | PutVPNIPsecPhase2SEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing IPsec Phase 2s.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2s-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | Unset):
        body (list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNIPsecPhase2SEndpointResponse400 | PutVPNIPsecPhase2SEndpointResponse401 | PutVPNIPsecPhase2SEndpointResponse403 | PutVPNIPsecPhase2SEndpointResponse404 | PutVPNIPsecPhase2SEndpointResponse405 | PutVPNIPsecPhase2SEndpointResponse406 | PutVPNIPsecPhase2SEndpointResponse409 | PutVPNIPsecPhase2SEndpointResponse415 | PutVPNIPsecPhase2SEndpointResponse422 | PutVPNIPsecPhase2SEndpointResponse424 | PutVPNIPsecPhase2SEndpointResponse500 | PutVPNIPsecPhase2SEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutVPNIPsecPhase2SEndpointResponse400
    | PutVPNIPsecPhase2SEndpointResponse401
    | PutVPNIPsecPhase2SEndpointResponse403
    | PutVPNIPsecPhase2SEndpointResponse404
    | PutVPNIPsecPhase2SEndpointResponse405
    | PutVPNIPsecPhase2SEndpointResponse406
    | PutVPNIPsecPhase2SEndpointResponse409
    | PutVPNIPsecPhase2SEndpointResponse415
    | PutVPNIPsecPhase2SEndpointResponse422
    | PutVPNIPsecPhase2SEndpointResponse424
    | PutVPNIPsecPhase2SEndpointResponse500
    | PutVPNIPsecPhase2SEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing IPsec Phase 2s.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: IPsecPhase2<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase2s-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNIPsecPhase2SEndpointJsonBodyItem] | Unset):
        body (list[PutVPNIPsecPhase2SEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNIPsecPhase2SEndpointResponse400 | PutVPNIPsecPhase2SEndpointResponse401 | PutVPNIPsecPhase2SEndpointResponse403 | PutVPNIPsecPhase2SEndpointResponse404 | PutVPNIPsecPhase2SEndpointResponse405 | PutVPNIPsecPhase2SEndpointResponse406 | PutVPNIPsecPhase2SEndpointResponse409 | PutVPNIPsecPhase2SEndpointResponse415 | PutVPNIPsecPhase2SEndpointResponse422 | PutVPNIPsecPhase2SEndpointResponse424 | PutVPNIPsecPhase2SEndpointResponse500 | PutVPNIPsecPhase2SEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
