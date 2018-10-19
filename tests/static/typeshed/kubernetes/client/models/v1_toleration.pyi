# Stubs for kubernetes.client.models.v1_toleration (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1Toleration:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    effect: Any = ...
    key: Any = ...
    operator: Any = ...
    toleration_seconds: Any = ...
    value: Any = ...
    def __init__(self, effect: Optional[Any] = ..., key: Optional[Any] = ..., operator: Optional[Any] = ..., toleration_seconds: Optional[Any] = ..., value: Optional[Any] = ...) -> None: ...
    @property
    def effect(self): ...
    @effect.setter
    def effect(self, effect: Any) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key: Any) -> None: ...
    @property
    def operator(self): ...
    @operator.setter
    def operator(self, operator: Any) -> None: ...
    @property
    def toleration_seconds(self): ...
    @toleration_seconds.setter
    def toleration_seconds(self, toleration_seconds: Any) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
