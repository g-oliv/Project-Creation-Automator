class InvalidArgumentException(Exception):

    def __init__(self, message="InvalidArgumentException: Visibility options are: \n> public \n> private"):
        self.message = message
        super().__init__(self.message)
