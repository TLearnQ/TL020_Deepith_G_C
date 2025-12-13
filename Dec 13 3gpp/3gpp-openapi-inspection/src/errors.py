class APIResponseError(Exception):
    def __init__(self, message, status_code=None, endpoint=None):
        super().__init__(message)
        self.status_code = status_code
        self.endpoint = endpoint
