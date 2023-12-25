import sqlite3
from dataclasses import dataclass

Table_Name = "People"
DB_Name = "my_database.db"
def create_database():
    connection = sqlite3.connect(DB_Name)
    cursor = connection.cursor()
    return connection, cursor

def create_table(connection, cursor):
    cursor.execute(f"create table {Table_Name}(name text, last_name text, age int, country text);")
    connection.commit()

def connect_to_db():
    return create_database()


def write_to_db(connection, cursor, sql_request):
    cursor.execute(sql_request)
    connection.commit()

@dataclass
class Person:
    name:str
    family_name:str
    age: int
    country: str

def main():
    #connection, cursor  = create_database()
    #create_table (connection, cursor)
    connection, cursor = connect_to_db()
    write_to_db(connection, cursor, f"insert into {Table_Name} values('Jane', 'Mathews', 28, 'Italy' );")
    rows = cursor.execute(f"select * from {Table_Name};").fetchall()
    people= [Person(*row) for row in rows]
    # for row in rows:
    #     person = Person(row)
    #     people.append(person)
    for person in people:
        print (f"{person.name.title()}{person.family_name.title()}")
    ...
if __name__== '__main__':
    main()

# connection = sqlite3.connect("my_database312312.db")
# cursor = connection.cursor()
# #cursor.execute("create table Ludki (name text, last_name text, age int, country text);")
# #connection.commit()
# cursor.execute("INSERT INTO Ludki Values ('Lech', 'Kaczynski', 69, 'Rosja');")
# connection.commit()
# cursor.execute("SELECT * FROM Ludki")
# rows = cursor.fetchall()  # Pobranie wszystkich wierszy wynikowych
#
# for row in rows:
#     print(row)