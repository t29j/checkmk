# Stubs for kubernetes.client.models.v1_node_selector_term (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1NodeSelectorTerm:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    match_expressions: Any = ...
    match_fields: Any = ...
    def __init__(self, match_expressions: Optional[Any] = ..., match_fields: Optional[Any] = ...) -> None: ...
    @property
    def match_expressions(self): ...
    @match_expressions.setter
    def match_expressions(self, match_expressions: Any) -> None: ...
    @property
    def match_fields(self): ...
    @match_fields.setter
    def match_fields(self, match_fields: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
