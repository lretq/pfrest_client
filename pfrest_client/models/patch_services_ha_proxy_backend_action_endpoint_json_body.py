from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_backend_action_action import HAProxyBackendActionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesHAProxyBackendActionEndpointJsonBody")


@_attrs_define
class PatchServicesHAProxyBackendActionEndpointJsonBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        action (HAProxyBackendActionAction | Unset): The action to take when an ACL match is found.<br>
        acl (str | Unset): The name of the backend ACL this action is associated with.<br>
        server (str | Unset): The backend server to use when an ACL match is found.<br><br>This field is only available
            when the following conditions are met:<br>- `action` must be equal to `'use_server'`<br>
        customaction (str | Unset): The custom action to take when an ACL match is found.<br><br>This field is only
            available when the following conditions are met:<br>- `action` must be equal to `'custom'`<br>
        deny_status (str | Unset): The deny status to use when an ACL match is found.<br><br>This field is only
            available when the following conditions are met:<br>- `action` must be one of [ http-request_deny, http-
            request_tarpit ]<br>
        realm (str | Unset): The authentication realm to use when an ACL match is found.<br><br>This field is only
            available when the following conditions are met:<br>- `action` must be equal to `'http-request_auth'`<br>
        rule (str | Unset): The redirect rule to use when an ACL match is found.<br><br>This field is only available
            when the following conditions are met:<br>- `action` must be equal to `'http-request_redirect'`<br>
        lua_function (str | Unset): The Lua function to use when an ACL match is found.<br><br>This field is only
            available when the following conditions are met:<br>- `action` must be one of [ http-request_lua, http-
            request_use-service, http-response_lua, tcp-request_content_lua, tcp-request_content_use-service, tcp-
            response_content_lua ]<br>
        name (str | Unset): The name to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-request_add-header, http-request_set-header,
            http-request_del-header, http-request_replace-header, http-request_replace-value, http-response_add-header,
            http-response_set-header, http-response_del-header, http-response_replace-header, http-response_replace-value,
            http-after-response_add-header, http-after-response_set-header, http-after-response_del-header, http-after-
            response_replace-header, http-after-response_replace-value ]<br>
        fmt (str | Unset): The fmt value to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-request_add-header, http-request_set-header,
            http-request_set-method, http-request_set-path, http-request_set-query, http-request_set-uri, http-response_add-
            header, http-response_set-header, http-after-response_add-header, http-after-response_set-header ]<br>
        find (str | Unset): The value to find when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-request_replace-header, http-request_replace-
            value, http-response_replace-header, http-request_replace-path, http-response_replace-value, http-after-
            response_replace-header, http-after-response_replace-value ]<br>
        replace (str | Unset): The value to replace with when an ACL match is found.<br><br>This field is only available
            when the following conditions are met:<br>- `action` must be one of [ http-request_replace-header, http-
            request_replace-value, http-request_replace-path, http-response_replace-header, http-response_replace-value,
            http-after-response_replace-header, http-after-response_replace-value ]<br>
        path (str | Unset): The path to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be equal to `'http-request_replace-path'`<br>
        status (str | Unset): The status to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-response_set-status, http-after-response_set-
            status ]<br>
        reason (str | Unset): The status reason to use when an ACL match is found.<br><br>This field is only available
            when the following conditions are met:<br>- `action` must be one of [ http-response_set-status, http-after-
            response_set-status ]<br>
    """

    parent_id: int
    id: int
    action: HAProxyBackendActionAction | Unset = UNSET
    acl: str | Unset = UNSET
    server: str | Unset = UNSET
    customaction: str | Unset = UNSET
    deny_status: str | Unset = UNSET
    realm: str | Unset = UNSET
    rule: str | Unset = UNSET
    lua_function: str | Unset = UNSET
    name: str | Unset = UNSET
    fmt: str | Unset = UNSET
    find: str | Unset = UNSET
    replace: str | Unset = UNSET
    path: str | Unset = UNSET
    status: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        acl = self.acl

        server = self.server

        customaction = self.customaction

        deny_status = self.deny_status

        realm = self.realm

        rule = self.rule

        lua_function = self.lua_function

        name = self.name

        fmt = self.fmt

        find = self.find

        replace = self.replace

        path = self.path

        status = self.status

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if acl is not UNSET:
            field_dict["acl"] = acl
        if server is not UNSET:
            field_dict["server"] = server
        if customaction is not UNSET:
            field_dict["customaction"] = customaction
        if deny_status is not UNSET:
            field_dict["deny_status"] = deny_status
        if realm is not UNSET:
            field_dict["realm"] = realm
        if rule is not UNSET:
            field_dict["rule"] = rule
        if lua_function is not UNSET:
            field_dict["lua_function"] = lua_function
        if name is not UNSET:
            field_dict["name"] = name
        if fmt is not UNSET:
            field_dict["fmt"] = fmt
        if find is not UNSET:
            field_dict["find"] = find
        if replace is not UNSET:
            field_dict["replace"] = replace
        if path is not UNSET:
            field_dict["path"] = path
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        _action = d.pop("action", UNSET)
        action: HAProxyBackendActionAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = HAProxyBackendActionAction(_action)

        acl = d.pop("acl", UNSET)

        server = d.pop("server", UNSET)

        customaction = d.pop("customaction", UNSET)

        deny_status = d.pop("deny_status", UNSET)

        realm = d.pop("realm", UNSET)

        rule = d.pop("rule", UNSET)

        lua_function = d.pop("lua_function", UNSET)

        name = d.pop("name", UNSET)

        fmt = d.pop("fmt", UNSET)

        find = d.pop("find", UNSET)

        replace = d.pop("replace", UNSET)

        path = d.pop("path", UNSET)

        status = d.pop("status", UNSET)

        reason = d.pop("reason", UNSET)

        patch_services_ha_proxy_backend_action_endpoint_json_body = cls(
            parent_id=parent_id,
            id=id,
            action=action,
            acl=acl,
            server=server,
            customaction=customaction,
            deny_status=deny_status,
            realm=realm,
            rule=rule,
            lua_function=lua_function,
            name=name,
            fmt=fmt,
            find=find,
            replace=replace,
            path=path,
            status=status,
            reason=reason,
        )

        patch_services_ha_proxy_backend_action_endpoint_json_body.additional_properties = d
        return patch_services_ha_proxy_backend_action_endpoint_json_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
