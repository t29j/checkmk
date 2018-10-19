# Stubs for kubernetes.client.models.v1_attached_volume (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1AttachedVolume:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    device_path: Any = ...
    name: Any = ...
    def __init__(self, device_path: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    @property
    def device_path(self): ...
    @device_path.setter
    def device_path(self, device_path: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
