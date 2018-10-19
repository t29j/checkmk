# Stubs for kubernetes.client.models.v1beta1_ingress_spec (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1IngressSpec:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    backend: Any = ...
    rules: Any = ...
    tls: Any = ...
    def __init__(self, backend: Optional[Any] = ..., rules: Optional[Any] = ..., tls: Optional[Any] = ...) -> None: ...
    @property
    def backend(self): ...
    @backend.setter
    def backend(self, backend: Any) -> None: ...
    @property
    def rules(self): ...
    @rules.setter
    def rules(self, rules: Any) -> None: ...
    @property
    def tls(self): ...
    @tls.setter
    def tls(self, tls: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
