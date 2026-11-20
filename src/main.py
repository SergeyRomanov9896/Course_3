from db.database import get_connection


def main(connect):
    print(connect)


if __name__ == "__main__":
    main(get_connection())
