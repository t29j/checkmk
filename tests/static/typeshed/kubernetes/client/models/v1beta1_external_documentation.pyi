# Stubs for kubernetes.client.models.v1beta1_external_documentation (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1ExternalDocumentation:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    description: Any = ...
    url: Any = ...
    def __init__(self, description: Optional[Any] = ..., url: Optional[Any] = ...) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description: Any) -> None: ...
    @property
    def url(self): ...
    @url.setter
    def url(self, url: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
