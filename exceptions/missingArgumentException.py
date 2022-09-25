class MissingArgumentException(Exception):

    def __init__(self, message="MissingArgumentException: No project name given. Introduce the name of your new project" +
                 "create [<project name>] [<visibility>]"):
        self.message = message
        super().__init__(self.message)
