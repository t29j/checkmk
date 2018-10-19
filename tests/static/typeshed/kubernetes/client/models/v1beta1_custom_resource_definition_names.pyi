# Stubs for kubernetes.client.models.v1beta1_custom_resource_definition_names (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1CustomResourceDefinitionNames:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    categories: Any = ...
    kind: str = ...
    list_kind: str = ...
    plural: Any = ...
    short_names: Any = ...
    singular: Any = ...
    def __init__(self, categories: Optional[Any] = ..., kind: Optional[Any] = ..., list_kind: Optional[Any] = ..., plural: Optional[Any] = ..., short_names: Optional[Any] = ..., singular: Optional[Any] = ...) -> None: ...
    @property
    def categories(self): ...
    @categories.setter
    def categories(self, categories: Any) -> None: ...
    @property
    def kind(self) -> str: ...
    @kind.setter
    def kind(self, kind: str) -> None: ...
    @property
    def list_kind(self): ...
    @list_kind.setter
    def list_kind(self, list_kind: Any) -> None: ...
    @property
    def plural(self): ...
    @plural.setter
    def plural(self, plural: Any) -> None: ...
    @property
    def short_names(self): ...
    @short_names.setter
    def short_names(self, short_names: Any) -> None: ...
    @property
    def singular(self): ...
    @singular.setter
    def singular(self, singular: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
