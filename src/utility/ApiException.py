class ApiException(Exception):
    status_code: int
    error_code: str

    def __init__(self, msg: str, status_code: int, err_code: str):
        super().__init__(msg)
        self.status_code = status_code
        self.error_code = err_code


class ApiInvalidInputException(ApiException):
    def __init__(self, msg: str, status_code: int = 400, err_code: str = "INVALID_INPUT"):
        super().__init__(msg, status_code, err_code)


class ApiDuplicateResourceException(ApiException):
    def __init__(self, msg: str, status_code: int = 409, err_code: str = "DUPLICATE_RESOURCE"):
        super().__init__(msg, status_code, err_code)


class ApiResourceNotFoundException(ApiException):
    def __init__(self, msg: str, status_code: int = 404, err_code: str = "NOT_FOUND"):
        super().__init__(msg, status_code, err_code)


class ApiPermissionException(ApiException):
    def __init__(self, msg: str, status_code: int = 403, err_code: str = "PERMISSION_DENIED"):
        super().__init__(msg, status_code, err_code)


class ApiTokenException(ApiException):
    def __init__(self, msg: str, status_code: int = 401, err_code: str = "NOT_AUTHORIZED"):
        super().__init__(msg, status_code, err_code)


class ApiResourceLockedException(ApiException):
    def __init__(self, msg: str, status_code: int = 423, err_code: str = "RESOURCE_LOCKED"):
        super().__init__(msg, status_code, err_code)


class ApiResourceOperationException(ApiException):
    def __init__(self, msg: str, status_code: int = 500, err_code: str = "INTERNAL_ERROR"):
        super().__init__(msg, status_code, err_code)


class ApiUnimplementedException(ApiException):
    def __init__(self, msg: str, status_code: int = 501, err_code: str = "UNIMPLEMENTED"):
        super().__init__(msg, status_code, err_code)
