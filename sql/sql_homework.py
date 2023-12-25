import sqlite3
import random
import string

DB_NAME = "my_harry_poter.db"
TABLE_NAME = "Gryffindor"

def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    return connection, cursor

def create_table(connection, cursor):
    cursor.execute(
        f"create table {TABLE_NAME} ("
        "first_name text, "
        "last_name text, "
        "blood_status text, "
        "born int"
        ");"
    )
    connection.commit()

def connect_to_db():
    return create_database()

def write_to_db(connection, cursor, sql_request):
    cursor.execute(sql_request)
    connection.commit()

def main():
    try:
        connection, cursor = create_database()
        create_table(connection, cursor)
    except:
        pass

    connection, cursor = connect_to_db()

def person_creator(first_name, last_name, blood_status, born):
    connection, cursor = connect_to_db()
    notrepeat = cursor.execute(f"select * from {TABLE_NAME} where first_name=='{first_name}' and last_name =='{last_name}'").fetchall()
    if len(notrepeat) == 0:
        write_to_db(connection, cursor,f"insert into {TABLE_NAME} values ('{first_name}', '{last_name}', '{blood_status}', '{born}');")
    else:
        print('not adding that wizard. he/she is there already.')

if __name__ == "__main__":
    main()

person_creator('Harry', 'Poter', 'Half-breed', 1980)
person_creator('Ronald', 'Weasley', 'Pure-blood', 1979)
person_creator('Hermione', 'Granger', 'Muggle-born', 1979)
person_creator('Neville', 'Longbottom', 'Pure-blood', 1980)
person_creator('Rubeus', 'Hagrid', 'Half-breed', 1928)

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


def random_wizard():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=7))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    blood_statuses = ['Pure-blood', 'Half-breed', 'Muggle-born']
    blood_status = random.choice(blood_statuses)
    born_year = random.randint(1920, 2023)
    return first_name, last_name, blood_status, born_year

wizard_name , wizard_last_name, wizard_blood_status, wizard_born = random_wizard()

person_creator(wizard_name, wizard_last_name,  wizard_blood_status, wizard_born)

#print(wizard_name , wizard_last_name, wizard_blood_status, wizard_born)

rows = cursor.execute(f"select * from {TABLE_NAME};").fetchall()
print(rows)

born80 = cursor.execute(f"select * from {TABLE_NAME} where born == 1980;").fetchall()
print(born80)

bornfirst = cursor.execute(f"select * from {TABLE_NAME} order by born;").fetchone()
print(bornfirst)

def delete_wizard(cursor, first_name):
    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE first_name=?", (first_name,))
    cursor.connection.commit()
    print(f"{first_name} has been deleted from the database.")

delete_wizard(cursor, wizard_name)

notborn80 = cursor.execute(f"select * from {TABLE_NAME} where born != 1980;").fetchall()
print(notborn80)

halfbread = cursor.execute(f"select * from {TABLE_NAME} where blood_status =='Half-breed';").fetchall()
print(halfbread)