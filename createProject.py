import sys

from exceptions.invalidArgumentException import InvalidArgumentException
from exceptions.missingArgumentException import MissingArgumentException

PUBLIC = "public"
PRIVATE = "private"


def createProject():

    try:
        if len(sys.argv) < 2:
            raise MissingArgumentException()

        projectName = sys.argv[1]
        if len(sys.argv) < 3:
            visibility = "public"
        elif sys.argv[2].lower() == "public":
            visibility = PUBLIC
        elif sys.argv[2].lower() == "private":
            visibility = PRIVATE
        else:
            raise InvalidArgumentException()

        print(projectName, visibility)

    except MissingArgumentException as mae:
        print(mae)
    except InvalidArgumentException as iae:
        print(iae)


if __name__ == "__main__":
    createProject()
