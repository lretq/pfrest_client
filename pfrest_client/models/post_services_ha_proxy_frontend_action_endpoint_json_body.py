from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_frontend_action_action import HAProxyFrontendActionAction

T = TypeVar("T", bound="PostServicesHAProxyFrontendActionEndpointJsonBody")


@_attrs_define
class PostServicesHAProxyFrontendActionEndpointJsonBody:
    """
    Attributes:
        action (HAProxyFrontendActionAction): The action to take when an ACL match is found.<br>
        acl (str): The name of the frontend ACL this action is associated with.<br>
        backend (str): The backend to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be equal to `'use_backend'`<br>
        customaction (str): The custom action to take when an ACL match is found.<br><br>This field is only available
            when the following conditions are met:<br>- `action` must be equal to `'custom'`<br>
        deny_status (str): The deny status to use when an ACL match is found.<br><br>This field is only available when
            the following conditions are met:<br>- `action` must be one of [ http-request_deny, http-request_tarpit ]<br>
        realm (str): The authentication realm to use when an ACL match is found.<br><br>This field is only available
            when the following conditions are met:<br>- `action` must be equal to `'http-request_auth'`<br>
        rule (str): The redirect rule to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be equal to `'http-request_redirect'`<br>
        lua_function (str): The Lua function to use when an ACL match is found.<br><br>This field is only available when
            the following conditions are met:<br>- `action` must be one of [ http-request_lua, http-request_use-service,
            http-response_lua, tcp-request_content_lua, tcp-request_content_use-service, tcp-response_content_lua ]<br>
        name (str): The name to use when an ACL match is found.<br><br>This field is only available when the following
            conditions are met:<br>- `action` must be one of [ http-request_add-header, http-request_set-header, http-
            request_del-header, http-request_replace-header, http-request_replace-value, http-response_add-header, http-
            response_set-header, http-response_del-header, http-response_replace-header, http-response_replace-value, http-
            after-response_add-header, http-after-response_set-header, http-after-response_del-header, http-after-
            response_replace-header, http-after-response_replace-value ]<br>
        fmt (str): The fmt value to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-request_add-header, http-request_set-header,
            http-request_set-method, http-request_set-path, http-request_set-query, http-request_set-uri, http-response_add-
            header, http-response_set-header, http-after-response_add-header, http-after-response_set-header ]<br>
        find (str): The value to find when an ACL match is found.<br><br>This field is only available when the following
            conditions are met:<br>- `action` must be one of [ http-request_replace-header, http-request_replace-value,
            http-response_replace-header, http-request_replace-path, http-response_replace-value, http-after-
            response_replace-header, http-after-response_replace-value ]<br>
        replace (str): The value to replace with when an ACL match is found.<br><br>This field is only available when
            the following conditions are met:<br>- `action` must be one of [ http-request_replace-header, http-
            request_replace-value, http-request_replace-path, http-response_replace-header, http-response_replace-value,
            http-after-response_replace-header, http-after-response_replace-value ]<br>
        path (str): The path to use when an ACL match is found.<br><br>This field is only available when the following
            conditions are met:<br>- `action` must be equal to `'http-request_replace-path'`<br>
        status (str): The status to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-response_set-status, http-after-response_set-
            status ]<br>
        reason (str): The status reason to use when an ACL match is found.<br><br>This field is only available when the
            following conditions are met:<br>- `action` must be one of [ http-response_set-status, http-after-response_set-
            status ]<br>
        parent_id (int): The ID of the parent this object is nested under.
    """

    action: HAProxyFrontendActionAction
    acl: str
    backend: str
    customaction: str
    deny_status: str
    realm: str
    rule: str
    lua_function: str
    name: str
    fmt: str
    find: str
    replace: str
    path: str
    status: str
    reason: str
    parent_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        acl = self.acl

        backend = self.backend

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

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "acl": acl,
                "backend": backend,
                "customaction": customaction,
                "deny_status": deny_status,
                "realm": realm,
                "rule": rule,
                "lua_function": lua_function,
                "name": name,
                "fmt": fmt,
                "find": find,
                "replace": replace,
                "path": path,
                "status": status,
                "reason": reason,
                "parent_id": parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = HAProxyFrontendActionAction(d.pop("action"))

        acl = d.pop("acl")

        backend = d.pop("backend")

        customaction = d.pop("customaction")

        deny_status = d.pop("deny_status")

        realm = d.pop("realm")

        rule = d.pop("rule")

        lua_function = d.pop("lua_function")

        name = d.pop("name")

        fmt = d.pop("fmt")

        find = d.pop("find")

        replace = d.pop("replace")

        path = d.pop("path")

        status = d.pop("status")

        reason = d.pop("reason")

        parent_id = d.pop("parent_id")

        post_services_ha_proxy_frontend_action_endpoint_json_body = cls(
            action=action,
            acl=acl,
            backend=backend,
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
            parent_id=parent_id,
        )

        post_services_ha_proxy_frontend_action_endpoint_json_body.additional_properties = d
        return post_services_ha_proxy_frontend_action_endpoint_json_body

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
