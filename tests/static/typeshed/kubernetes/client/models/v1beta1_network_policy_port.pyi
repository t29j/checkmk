# Stubs for kubernetes.client.models.v1beta1_network_policy_port (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1NetworkPolicyPort:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    port: Any = ...
    protocol: Any = ...
    def __init__(self, port: Optional[Any] = ..., protocol: Optional[Any] = ...) -> None: ...
    @property
    def port(self): ...
    @port.setter
    def port(self, port: Any) -> None: ...
    @property
    def protocol(self): ...
    @protocol.setter
    def protocol(self, protocol: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
