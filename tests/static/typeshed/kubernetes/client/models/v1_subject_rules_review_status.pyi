# Stubs for kubernetes.client.models.v1_subject_rules_review_status (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1SubjectRulesReviewStatus:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    evaluation_error: Any = ...
    incomplete: Any = ...
    non_resource_rules: Any = ...
    resource_rules: Any = ...
    def __init__(self, evaluation_error: Optional[Any] = ..., incomplete: Optional[Any] = ..., non_resource_rules: Optional[Any] = ..., resource_rules: Optional[Any] = ...) -> None: ...
    @property
    def evaluation_error(self): ...
    @evaluation_error.setter
    def evaluation_error(self, evaluation_error: Any) -> None: ...
    @property
    def incomplete(self): ...
    @incomplete.setter
    def incomplete(self, incomplete: Any) -> None: ...
    @property
    def non_resource_rules(self): ...
    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules: Any) -> None: ...
    @property
    def resource_rules(self): ...
    @resource_rules.setter
    def resource_rules(self, resource_rules: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
