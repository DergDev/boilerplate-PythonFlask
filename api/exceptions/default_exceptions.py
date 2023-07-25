class DefaultAPIException(Exception):
    """Exception raised for errors raised by APIs used by the Boilerplate.

    Attributes:
        return_code -- return code from the API
        message -- explanation of the error
    """

    def __init__(self, message="{0} unexpectedly returned the code: {1}", return_code: int = 500):
        self.api = "DefaultAPI"
        self.message = message.format(self.api, return_code)
        super().__init__(self.message)
