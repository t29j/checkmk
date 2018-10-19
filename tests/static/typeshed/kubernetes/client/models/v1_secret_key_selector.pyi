# Stubs for kubernetes.client.models.v1_secret_key_selector (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1SecretKeySelector:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    key: Any = ...
    name: Any = ...
    optional: Any = ...
    def __init__(self, key: Optional[Any] = ..., name: Optional[Any] = ..., optional: Optional[Any] = ...) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def optional(self): ...
    @optional.setter
    def optional(self, optional: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
