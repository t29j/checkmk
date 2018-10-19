# Stubs for kubernetes.client.models.v1_token_review_status (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1TokenReviewStatus:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    authenticated: Any = ...
    error: Any = ...
    user: Any = ...
    def __init__(self, authenticated: Optional[Any] = ..., error: Optional[Any] = ..., user: Optional[Any] = ...) -> None: ...
    @property
    def authenticated(self): ...
    @authenticated.setter
    def authenticated(self, authenticated: Any) -> None: ...
    @property
    def error(self): ...
    @error.setter
    def error(self, error: Any) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
