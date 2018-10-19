# Stubs for kubernetes.client.api_client (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .configuration import Configuration
from .rest import ApiException, RESTClientObject
from typing import Any, Optional

class ApiClient:
    PRIMITIVE_TYPES: Any = ...
    NATIVE_TYPES_MAPPING: Any = ...
    configuration: Any = ...
    pool: Any = ...
    rest_client: Any = ...
    default_headers: Any = ...
    cookie: Any = ...
    user_agent: str = ...
    def __init__(self, configuration: Optional[Any] = ..., header_name: Optional[Any] = ..., header_value: Optional[Any] = ..., cookie: Optional[Any] = ...) -> None: ...
    def __del__(self) -> None: ...
    @property
    def user_agent(self): ...
    @user_agent.setter
    def user_agent(self, value: Any) -> None: ...
    def set_default_header(self, header_name: Any, header_value: Any) -> None: ...
    def sanitize_for_serialization(self, obj: Any): ...
    def deserialize(self, response: Any, response_type: Any): ...
    def call_api(self, resource_path: Any, method: Any, path_params: Optional[Any] = ..., query_params: Optional[Any] = ..., header_params: Optional[Any] = ..., body: Optional[Any] = ..., post_params: Optional[Any] = ..., files: Optional[Any] = ..., response_type: Optional[Any] = ..., auth_settings: Optional[Any] = ..., async_req: Optional[Any] = ..., _return_http_data_only: Optional[Any] = ..., collection_formats: Optional[Any] = ..., _preload_content: bool = ..., _request_timeout: Optional[Any] = ...): ...
    def request(self, method: Any, url: Any, query_params: Optional[Any] = ..., headers: Optional[Any] = ..., post_params: Optional[Any] = ..., body: Optional[Any] = ..., _preload_content: bool = ..., _request_timeout: Optional[Any] = ...): ...
    def parameters_to_tuples(self, params: Any, collection_formats: Any): ...
    def prepare_post_parameters(self, post_params: Optional[Any] = ..., files: Optional[Any] = ...): ...
    def select_header_accept(self, accepts: Any): ...
    def select_header_content_type(self, content_types: Any): ...
    def update_params_for_auth(self, headers: Any, querys: Any, auth_settings: Any): ...
