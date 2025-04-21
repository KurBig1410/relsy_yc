from sel import auth
from app import getjson
from parse import parse


def start():
    auth()
    getjson()
    parse()


if __name__ == "__main__":
    start()