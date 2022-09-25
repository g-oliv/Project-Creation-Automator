import sys

from exceptions.invalidArgumentException import InvalidArgumentException
from exceptions.missingArgumentException import MissingArgumentException

PUBLIC = "public"
PRIVATE = "private"


def createProject():

    try:
        if len(sys.argv) < 2:
            raise MissingArgumentException()

        if len(sys.argv) < 3 or sys.argv[2].lower() == PUBLIC:
            visibility = PUBLIC
        elif sys.argv[2].lower() == PRIVATE:
            visibility = PRIVATE
        else:
            raise InvalidArgumentException()

        print(visibility)

    except MissingArgumentException as mae:
        print(mae)
    except InvalidArgumentException as iae:
        print(iae)

    sys.exit(1)


if __name__ == "__main__":
    createProject()
