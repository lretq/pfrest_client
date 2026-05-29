from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_open_vpn_client_export_endpoint_data_body import PostVPNOpenVPNClientExportEndpointDataBody
from ...models.post_vpn_open_vpn_client_export_endpoint_json_body import PostVPNOpenVPNClientExportEndpointJsonBody
from ...models.post_vpn_open_vpn_client_export_endpoint_response_400 import (
    PostVPNOpenVPNClientExportEndpointResponse400,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_401 import (
    PostVPNOpenVPNClientExportEndpointResponse401,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_403 import (
    PostVPNOpenVPNClientExportEndpointResponse403,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_404 import (
    PostVPNOpenVPNClientExportEndpointResponse404,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_405 import (
    PostVPNOpenVPNClientExportEndpointResponse405,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_406 import (
    PostVPNOpenVPNClientExportEndpointResponse406,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_409 import (
    PostVPNOpenVPNClientExportEndpointResponse409,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_415 import (
    PostVPNOpenVPNClientExportEndpointResponse415,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_422 import (
    PostVPNOpenVPNClientExportEndpointResponse422,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_424 import (
    PostVPNOpenVPNClientExportEndpointResponse424,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_500 import (
    PostVPNOpenVPNClientExportEndpointResponse500,
)
from ...models.post_vpn_open_vpn_client_export_endpoint_response_503 import (
    PostVPNOpenVPNClientExportEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNOpenVPNClientExportEndpointJsonBody | PostVPNOpenVPNClientExportEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/openvpn/client_export",
    }

    if isinstance(body, PostVPNOpenVPNClientExportEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNOpenVPNClientExportEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNOpenVPNClientExportEndpointResponse400
    | PostVPNOpenVPNClientExportEndpointResponse401
    | PostVPNOpenVPNClientExportEndpointResponse403
    | PostVPNOpenVPNClientExportEndpointResponse404
    | PostVPNOpenVPNClientExportEndpointResponse405
    | PostVPNOpenVPNClientExportEndpointResponse406
    | PostVPNOpenVPNClientExportEndpointResponse409
    | PostVPNOpenVPNClientExportEndpointResponse415
    | PostVPNOpenVPNClientExportEndpointResponse422
    | PostVPNOpenVPNClientExportEndpointResponse424
    | PostVPNOpenVPNClientExportEndpointResponse500
    | PostVPNOpenVPNClientExportEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNOpenVPNClientExportEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNOpenVPNClientExportEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNOpenVPNClientExportEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNOpenVPNClientExportEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNOpenVPNClientExportEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNOpenVPNClientExportEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNOpenVPNClientExportEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNOpenVPNClientExportEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNOpenVPNClientExportEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNOpenVPNClientExportEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNOpenVPNClientExportEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNOpenVPNClientExportEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNOpenVPNClientExportEndpointResponse400
    | PostVPNOpenVPNClientExportEndpointResponse401
    | PostVPNOpenVPNClientExportEndpointResponse403
    | PostVPNOpenVPNClientExportEndpointResponse404
    | PostVPNOpenVPNClientExportEndpointResponse405
    | PostVPNOpenVPNClientExportEndpointResponse406
    | PostVPNOpenVPNClientExportEndpointResponse409
    | PostVPNOpenVPNClientExportEndpointResponse415
    | PostVPNOpenVPNClientExportEndpointResponse422
    | PostVPNOpenVPNClientExportEndpointResponse424
    | PostVPNOpenVPNClientExportEndpointResponse500
    | PostVPNOpenVPNClientExportEndpointResponse503
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
    body: PostVPNOpenVPNClientExportEndpointJsonBody | PostVPNOpenVPNClientExportEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNClientExportEndpointResponse400
    | PostVPNOpenVPNClientExportEndpointResponse401
    | PostVPNOpenVPNClientExportEndpointResponse403
    | PostVPNOpenVPNClientExportEndpointResponse404
    | PostVPNOpenVPNClientExportEndpointResponse405
    | PostVPNOpenVPNClientExportEndpointResponse406
    | PostVPNOpenVPNClientExportEndpointResponse409
    | PostVPNOpenVPNClientExportEndpointResponse415
    | PostVPNOpenVPNClientExportEndpointResponse422
    | PostVPNOpenVPNClientExportEndpointResponse424
    | PostVPNOpenVPNClientExportEndpointResponse500
    | PostVPNOpenVPNClientExportEndpointResponse503
]:
    """<h3>Description:</h3>Export an OpenVPN Client configuration.

    Before using this endpoint, you must define a default export configuration for your OpenVPN
    server(s) using the the endpoint at /api/v2/openvpn/vpn/client_export/config as you will need its ID
    to use this endpoint. Any specific configurations made to this endpoint will override the default
    configurations, but will not store them in the pfSense configuration.

    Exports of exe, zip and other binary file types MUST use the 'application/octet-stream' accept type
    as their data is not serializable.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated
    model**: OpenVPNClientExport<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-post ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNClientExportEndpointResponse400 | PostVPNOpenVPNClientExportEndpointResponse401 | PostVPNOpenVPNClientExportEndpointResponse403 | PostVPNOpenVPNClientExportEndpointResponse404 | PostVPNOpenVPNClientExportEndpointResponse405 | PostVPNOpenVPNClientExportEndpointResponse406 | PostVPNOpenVPNClientExportEndpointResponse409 | PostVPNOpenVPNClientExportEndpointResponse415 | PostVPNOpenVPNClientExportEndpointResponse422 | PostVPNOpenVPNClientExportEndpointResponse424 | PostVPNOpenVPNClientExportEndpointResponse500 | PostVPNOpenVPNClientExportEndpointResponse503]
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
    body: PostVPNOpenVPNClientExportEndpointJsonBody | PostVPNOpenVPNClientExportEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNClientExportEndpointResponse400
    | PostVPNOpenVPNClientExportEndpointResponse401
    | PostVPNOpenVPNClientExportEndpointResponse403
    | PostVPNOpenVPNClientExportEndpointResponse404
    | PostVPNOpenVPNClientExportEndpointResponse405
    | PostVPNOpenVPNClientExportEndpointResponse406
    | PostVPNOpenVPNClientExportEndpointResponse409
    | PostVPNOpenVPNClientExportEndpointResponse415
    | PostVPNOpenVPNClientExportEndpointResponse422
    | PostVPNOpenVPNClientExportEndpointResponse424
    | PostVPNOpenVPNClientExportEndpointResponse500
    | PostVPNOpenVPNClientExportEndpointResponse503
    | None
):
    """<h3>Description:</h3>Export an OpenVPN Client configuration.

    Before using this endpoint, you must define a default export configuration for your OpenVPN
    server(s) using the the endpoint at /api/v2/openvpn/vpn/client_export/config as you will need its ID
    to use this endpoint. Any specific configurations made to this endpoint will override the default
    configurations, but will not store them in the pfSense configuration.

    Exports of exe, zip and other binary file types MUST use the 'application/octet-stream' accept type
    as their data is not serializable.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated
    model**: OpenVPNClientExport<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-post ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNClientExportEndpointResponse400 | PostVPNOpenVPNClientExportEndpointResponse401 | PostVPNOpenVPNClientExportEndpointResponse403 | PostVPNOpenVPNClientExportEndpointResponse404 | PostVPNOpenVPNClientExportEndpointResponse405 | PostVPNOpenVPNClientExportEndpointResponse406 | PostVPNOpenVPNClientExportEndpointResponse409 | PostVPNOpenVPNClientExportEndpointResponse415 | PostVPNOpenVPNClientExportEndpointResponse422 | PostVPNOpenVPNClientExportEndpointResponse424 | PostVPNOpenVPNClientExportEndpointResponse500 | PostVPNOpenVPNClientExportEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNClientExportEndpointJsonBody | PostVPNOpenVPNClientExportEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNClientExportEndpointResponse400
    | PostVPNOpenVPNClientExportEndpointResponse401
    | PostVPNOpenVPNClientExportEndpointResponse403
    | PostVPNOpenVPNClientExportEndpointResponse404
    | PostVPNOpenVPNClientExportEndpointResponse405
    | PostVPNOpenVPNClientExportEndpointResponse406
    | PostVPNOpenVPNClientExportEndpointResponse409
    | PostVPNOpenVPNClientExportEndpointResponse415
    | PostVPNOpenVPNClientExportEndpointResponse422
    | PostVPNOpenVPNClientExportEndpointResponse424
    | PostVPNOpenVPNClientExportEndpointResponse500
    | PostVPNOpenVPNClientExportEndpointResponse503
]:
    """<h3>Description:</h3>Export an OpenVPN Client configuration.

    Before using this endpoint, you must define a default export configuration for your OpenVPN
    server(s) using the the endpoint at /api/v2/openvpn/vpn/client_export/config as you will need its ID
    to use this endpoint. Any specific configurations made to this endpoint will override the default
    configurations, but will not store them in the pfSense configuration.

    Exports of exe, zip and other binary file types MUST use the 'application/octet-stream' accept type
    as their data is not serializable.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated
    model**: OpenVPNClientExport<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-post ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNClientExportEndpointResponse400 | PostVPNOpenVPNClientExportEndpointResponse401 | PostVPNOpenVPNClientExportEndpointResponse403 | PostVPNOpenVPNClientExportEndpointResponse404 | PostVPNOpenVPNClientExportEndpointResponse405 | PostVPNOpenVPNClientExportEndpointResponse406 | PostVPNOpenVPNClientExportEndpointResponse409 | PostVPNOpenVPNClientExportEndpointResponse415 | PostVPNOpenVPNClientExportEndpointResponse422 | PostVPNOpenVPNClientExportEndpointResponse424 | PostVPNOpenVPNClientExportEndpointResponse500 | PostVPNOpenVPNClientExportEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNClientExportEndpointJsonBody | PostVPNOpenVPNClientExportEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNClientExportEndpointResponse400
    | PostVPNOpenVPNClientExportEndpointResponse401
    | PostVPNOpenVPNClientExportEndpointResponse403
    | PostVPNOpenVPNClientExportEndpointResponse404
    | PostVPNOpenVPNClientExportEndpointResponse405
    | PostVPNOpenVPNClientExportEndpointResponse406
    | PostVPNOpenVPNClientExportEndpointResponse409
    | PostVPNOpenVPNClientExportEndpointResponse415
    | PostVPNOpenVPNClientExportEndpointResponse422
    | PostVPNOpenVPNClientExportEndpointResponse424
    | PostVPNOpenVPNClientExportEndpointResponse500
    | PostVPNOpenVPNClientExportEndpointResponse503
    | None
):
    """<h3>Description:</h3>Export an OpenVPN Client configuration.

    Before using this endpoint, you must define a default export configuration for your OpenVPN
    server(s) using the the endpoint at /api/v2/openvpn/vpn/client_export/config as you will need its ID
    to use this endpoint. Any specific configurations made to this endpoint will override the default
    configurations, but will not store them in the pfSense configuration.

    Exports of exe, zip and other binary file types MUST use the 'application/octet-stream' accept type
    as their data is not serializable.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated
    model**: OpenVPNClientExport<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-vpn-openvpn-client-export-post ]<br>**Required packages**: [
    pfSense-pkg-openvpn-client-export ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientExportEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientExportEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNClientExportEndpointResponse400 | PostVPNOpenVPNClientExportEndpointResponse401 | PostVPNOpenVPNClientExportEndpointResponse403 | PostVPNOpenVPNClientExportEndpointResponse404 | PostVPNOpenVPNClientExportEndpointResponse405 | PostVPNOpenVPNClientExportEndpointResponse406 | PostVPNOpenVPNClientExportEndpointResponse409 | PostVPNOpenVPNClientExportEndpointResponse415 | PostVPNOpenVPNClientExportEndpointResponse422 | PostVPNOpenVPNClientExportEndpointResponse424 | PostVPNOpenVPNClientExportEndpointResponse500 | PostVPNOpenVPNClientExportEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
