# Stubs for kubernetes.client.models.v1beta1_rule_with_operations (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1RuleWithOperations:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    api_groups: Any = ...
    api_versions: Any = ...
    operations: Any = ...
    resources: Any = ...
    def __init__(self, api_groups: Optional[Any] = ..., api_versions: Optional[Any] = ..., operations: Optional[Any] = ..., resources: Optional[Any] = ...) -> None: ...
    @property
    def api_groups(self): ...
    @api_groups.setter
    def api_groups(self, api_groups: Any) -> None: ...
    @property
    def api_versions(self): ...
    @api_versions.setter
    def api_versions(self, api_versions: Any) -> None: ...
    @property
    def operations(self): ...
    @operations.setter
    def operations(self, operations: Any) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
