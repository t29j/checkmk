# Stubs for kubernetes.client.models.extensions_v1beta1_supplemental_groups_strategy_options (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ExtensionsV1beta1SupplementalGroupsStrategyOptions:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    ranges: Any = ...
    rule: Any = ...
    def __init__(self, ranges: Optional[Any] = ..., rule: Optional[Any] = ...) -> None: ...
    @property
    def ranges(self): ...
    @ranges.setter
    def ranges(self, ranges: Any) -> None: ...
    @property
    def rule(self): ...
    @rule.setter
    def rule(self, rule: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
