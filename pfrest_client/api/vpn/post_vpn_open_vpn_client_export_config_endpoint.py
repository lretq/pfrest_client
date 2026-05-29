from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_open_vpn_client_export_config_endpoint_data_body import (
    PostVPNOpenVPNClientExportConfigEndpointDataBody,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_json_body import (
    PostVPNOpenVPNClientExportConfigEndpointJsonBody,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_400 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse400,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_401 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse401,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_403 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse403,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_404 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse404,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_405 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse405,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_406 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse406,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_409 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse409,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_415 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse415,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_422 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse422,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_424 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse424,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_500 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse500,
)
from ...models.post_vpn_open_vpn_client_export_config_endpoint_response_503 import (
    PostVPNOpenVPNClientExportConfigEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNOpenVPNClientExportConfigEndpointJsonBody
    | PostVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/openvpn/client_export/config",
    }

    if isinstance(body, PostVPNOpenVPNClientExportConfigEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNOpenVPNClientExportConfigEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNOpenVPNClientExportConfigEndpointResponse400
    | PostVPNOpenVPNClientExportConfigEndpointResponse401
    | PostVPNOpenVPNClientExportConfigEndpointResponse403
    | PostVPNOpenVPNClientExportConfigEndpointResponse404
    | PostVPNOpenVPNClientExportConfigEndpointResponse405
    | PostVPNOpenVPNClientExportConfigEndpointResponse406
    | PostVPNOpenVPNClientExportConfigEndpointResponse409
    | PostVPNOpenVPNClientExportConfigEndpointResponse415
    | PostVPNOpenVPNClientExportConfigEndpointResponse422
    | PostVPNOpenVPNClientExportConfigEndpointResponse424
    | PostVPNOpenVPNClientExportConfigEndpointResponse500
    | PostVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNOpenVPNClientExportConfigEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNOpenVPNClientExportConfigEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNOpenVPNClientExportConfigEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNOpenVPNClientExportConfigEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNOpenVPNClientExportConfigEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNOpenVPNClientExportConfigEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNOpenVPNClientExportConfigEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNOpenVPNClientExportConfigEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNOpenVPNClientExportConfigEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNOpenVPNClientExportConfigEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNOpenVPNClientExportConfigEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNOpenVPNClientExportConfigEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNOpenVPNClientExportConfigEndpointResponse400
    | PostVPNOpenVPNClientExportConfigEndpointResponse401
    | PostVPNOpenVPNClientExportConfigEndpointResponse403
    | PostVPNOpenVPNClientExportConfigEndpointResponse404
    | PostVPNOpenVPNClientExportConfigEndpointResponse405
    | PostVPNOpenVPNClientExportConfigEndpointResponse406
    | PostVPNOpenVPNClientExportConfigEndpointResponse409
    | PostVPNOpenVPNClientExportConfigEndpointResponse415
    | PostVPNOpenVPNClientExportConfigEndpointResponse422
    | PostVPNOpenVPNClientExportConfigEndpointResponse424
    | PostVPNOpenVPNClientExportConfigEndpointResponse500
    | PostVPNOpenVPNClientExportConfigEndpointResponse503
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
    body: PostVPNOpenVPNClientExportConfigEndpointJsonBody
    | PostVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNClientExportConfigEndpointResponse400
    | PostVPNOpenVPNClientExportConfigEndpointResponse401
    | PostVPNOpenVPNClientExportConfigEndpointResponse403
    | PostVPNOpenVPNClientExportConfigEndpointResponse404
    | PostVPNOpenVPNClientExportConfigEndpointResponse405
    | PostVPNOpenVPNClientExportConfigEndpointResponse406
    | PostVPNOpenVPNClientExportConfigEndpointResponse409
    | PostVPNOpenVPNClientExportConfigEndpointResponse415
    | PostVPNOpenVPNClientExportConfigEndpointResponse422
    | PostVPNOpenVPNClientExportConfigEndpointResponse424
    | PostVPNOpenVPNClientExportConfigEndpointResponse500
    | PostVPNOpenVPNClientExportConfigEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    post ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNClientExportConfigEndpointResponse400 | PostVPNOpenVPNClientExportConfigEndpointResponse401 | PostVPNOpenVPNClientExportConfigEndpointResponse403 | PostVPNOpenVPNClientExportConfigEndpointResponse404 | PostVPNOpenVPNClientExportConfigEndpointResponse405 | PostVPNOpenVPNClientExportConfigEndpointResponse406 | PostVPNOpenVPNClientExportConfigEndpointResponse409 | PostVPNOpenVPNClientExportConfigEndpointResponse415 | PostVPNOpenVPNClientExportConfigEndpointResponse422 | PostVPNOpenVPNClientExportConfigEndpointResponse424 | PostVPNOpenVPNClientExportConfigEndpointResponse500 | PostVPNOpenVPNClientExportConfigEndpointResponse503]
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
    body: PostVPNOpenVPNClientExportConfigEndpointJsonBody
    | PostVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> (
    PostVPNOpenVPNClientExportConfigEndpointResponse400
    | PostVPNOpenVPNClientExportConfigEndpointResponse401
    | PostVPNOpenVPNClientExportConfigEndpointResponse403
    | PostVPNOpenVPNClientExportConfigEndpointResponse404
    | PostVPNOpenVPNClientExportConfigEndpointResponse405
    | PostVPNOpenVPNClientExportConfigEndpointResponse406
    | PostVPNOpenVPNClientExportConfigEndpointResponse409
    | PostVPNOpenVPNClientExportConfigEndpointResponse415
    | PostVPNOpenVPNClientExportConfigEndpointResponse422
    | PostVPNOpenVPNClientExportConfigEndpointResponse424
    | PostVPNOpenVPNClientExportConfigEndpointResponse500
    | PostVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    post ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNClientExportConfigEndpointResponse400 | PostVPNOpenVPNClientExportConfigEndpointResponse401 | PostVPNOpenVPNClientExportConfigEndpointResponse403 | PostVPNOpenVPNClientExportConfigEndpointResponse404 | PostVPNOpenVPNClientExportConfigEndpointResponse405 | PostVPNOpenVPNClientExportConfigEndpointResponse406 | PostVPNOpenVPNClientExportConfigEndpointResponse409 | PostVPNOpenVPNClientExportConfigEndpointResponse415 | PostVPNOpenVPNClientExportConfigEndpointResponse422 | PostVPNOpenVPNClientExportConfigEndpointResponse424 | PostVPNOpenVPNClientExportConfigEndpointResponse500 | PostVPNOpenVPNClientExportConfigEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNClientExportConfigEndpointJsonBody
    | PostVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNClientExportConfigEndpointResponse400
    | PostVPNOpenVPNClientExportConfigEndpointResponse401
    | PostVPNOpenVPNClientExportConfigEndpointResponse403
    | PostVPNOpenVPNClientExportConfigEndpointResponse404
    | PostVPNOpenVPNClientExportConfigEndpointResponse405
    | PostVPNOpenVPNClientExportConfigEndpointResponse406
    | PostVPNOpenVPNClientExportConfigEndpointResponse409
    | PostVPNOpenVPNClientExportConfigEndpointResponse415
    | PostVPNOpenVPNClientExportConfigEndpointResponse422
    | PostVPNOpenVPNClientExportConfigEndpointResponse424
    | PostVPNOpenVPNClientExportConfigEndpointResponse500
    | PostVPNOpenVPNClientExportConfigEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    post ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNClientExportConfigEndpointResponse400 | PostVPNOpenVPNClientExportConfigEndpointResponse401 | PostVPNOpenVPNClientExportConfigEndpointResponse403 | PostVPNOpenVPNClientExportConfigEndpointResponse404 | PostVPNOpenVPNClientExportConfigEndpointResponse405 | PostVPNOpenVPNClientExportConfigEndpointResponse406 | PostVPNOpenVPNClientExportConfigEndpointResponse409 | PostVPNOpenVPNClientExportConfigEndpointResponse415 | PostVPNOpenVPNClientExportConfigEndpointResponse422 | PostVPNOpenVPNClientExportConfigEndpointResponse424 | PostVPNOpenVPNClientExportConfigEndpointResponse500 | PostVPNOpenVPNClientExportConfigEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNClientExportConfigEndpointJsonBody
    | PostVPNOpenVPNClientExportConfigEndpointDataBody
    | Unset = UNSET,
) -> (
    PostVPNOpenVPNClientExportConfigEndpointResponse400
    | PostVPNOpenVPNClientExportConfigEndpointResponse401
    | PostVPNOpenVPNClientExportConfigEndpointResponse403
    | PostVPNOpenVPNClientExportConfigEndpointResponse404
    | PostVPNOpenVPNClientExportConfigEndpointResponse405
    | PostVPNOpenVPNClientExportConfigEndpointResponse406
    | PostVPNOpenVPNClientExportConfigEndpointResponse409
    | PostVPNOpenVPNClientExportConfigEndpointResponse415
    | PostVPNOpenVPNClientExportConfigEndpointResponse422
    | PostVPNOpenVPNClientExportConfigEndpointResponse424
    | PostVPNOpenVPNClientExportConfigEndpointResponse500
    | PostVPNOpenVPNClientExportConfigEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Client Export Config.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientExportConfig<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-export-config-
    post ]<br>**Required packages**: [ pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportConfigEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportConfigEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNClientExportConfigEndpointResponse400 | PostVPNOpenVPNClientExportConfigEndpointResponse401 | PostVPNOpenVPNClientExportConfigEndpointResponse403 | PostVPNOpenVPNClientExportConfigEndpointResponse404 | PostVPNOpenVPNClientExportConfigEndpointResponse405 | PostVPNOpenVPNClientExportConfigEndpointResponse406 | PostVPNOpenVPNClientExportConfigEndpointResponse409 | PostVPNOpenVPNClientExportConfigEndpointResponse415 | PostVPNOpenVPNClientExportConfigEndpointResponse422 | PostVPNOpenVPNClientExportConfigEndpointResponse424 | PostVPNOpenVPNClientExportConfigEndpointResponse500 | PostVPNOpenVPNClientExportConfigEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
