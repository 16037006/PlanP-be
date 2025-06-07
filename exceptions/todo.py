from http.client import HTTPException


class TodoException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class TodoNotFoundException(TodoException):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
