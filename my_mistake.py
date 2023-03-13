class MyCustomError(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = 'This is my mistake'