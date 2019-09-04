class BaseException(Exception):
    pass


class InvalidArgs(BaseException):
    def __init__(self, message, status):
        self.message = message
        self.status = status

    def __call__(self):
        return dict(message=self.message, status=self.status)
