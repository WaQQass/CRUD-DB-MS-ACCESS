import pyodbc


def create(c_str):
    try:
        conn = pyodbc.connect(c_str)
        cursor = conn.cursor()
        cursor.execute('select * from bookings')

        #i_d = int(input("please enter the unique new ID for new entry of movie>>  "))
        name = input("please enter name of movie>>  ")
        price = int(input("please enter price of movie>>  "))
        myuserdata = (name, price)
        stmt = f"INSERT INTO bookings (Movie_name, price) VALUES ('{name}', {price})"

        cursor.execute(stmt)
        conn.commit()
        print("data created")

    except pyodbc.Error as e:
        print(e)


def read(c_str):
    try:
        conn = pyodbc.connect(c_str)
        cursor = conn.cursor()
        cursor.execute('select * from bookings')

        for row in cursor.fetchall():
            print(row)

    except pyodbc.Error as e:
        print(e)


def update(c_str):
    try:
        conn = pyodbc.connect(c_str)
        cursor = conn.cursor()

        user_id = int(
            input("please enter ID of movie name you want to update\n"))
        new = input("please enter new movie name you want to update here\n")
        cursor.execute(
            'UPDATE bookings SET Movie_name= ? WHERE id = ? ', (new, user_id))
        conn.commit()
        print("data updated")

    except pyodbc.Error as e:
        print(e)


def delete(c_str):
    try:
        conn = pyodbc.connect(c_str)
        cursor = conn.cursor()
        user_id = int(input("please enter the user id you want to delete\n"))
        cursor.execute(
            'DELETE FROM bookings  WHERE id = ? ', (user_id))
        conn.commit()
        print("data DELEted")

    except pyodbc.Error as e:
        print(e)
