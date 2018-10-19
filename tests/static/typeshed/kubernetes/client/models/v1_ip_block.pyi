# Stubs for kubernetes.client.models.v1_ip_block (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1IPBlock:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    cidr: Any = ...
    def __init__(self, cidr: Optional[Any] = ..., _except: Optional[Any] = ...) -> None: ...
    @property
    def cidr(self): ...
    @cidr.setter
    def cidr(self, cidr: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
