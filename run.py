from sel import auth
from app import getjson
from parse import parse
from auth import parse_html


def start():
    auth()
    getjson()
    parse()
    parse_html()


# if __name__ == "__main__":
#     start()