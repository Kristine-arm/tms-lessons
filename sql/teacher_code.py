import sqlite3
from dataclasses import dataclass

DB_NAME = "my_database.db"
TABLE_NAME = "People"


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    return connection, cursor


def create_table(connection, cursor):
    cursor.execute(
        f"create table {TABLE_NAME} ("
        "name text, "
        "last_name text, "
        "age int, "
        "country text"
        ");"
    )
    connection.commit()


def connect_to_db():
    return create_database()


def write_to_db(connection, cursor, sql_request):
    cursor.execute(sql_request)
    connection.commit()


@dataclass
class Person:
    name: str
    family_name: str
    age: int
    country: str


def main():
    # connection, cursor = create_database()
    # create_table(connection, cursor)
    connection, cursor = connect_to_db()
    # write_to_db(
    #     connection,
    #     cursor,
    #     f"insert into {TABLE_NAME} values ('Jimmy', 'Glock', 16, 'Scotland');",
    # )
    rows = cursor.execute(f"select * from {TABLE_NAME};").fetchall()
    people = [Person(*row) for row in rows]

    # for person in people:
    #     print(f"{person.name.title()} {person.family_name.title()}")
    ...


if __name__ == "__main__":
    main()