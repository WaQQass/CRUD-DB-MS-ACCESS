import crud_db_functions
import os

# Set the base directory
base_dir = os.getcwd()

# Set the relative path to the MS Access file
file_path = 'db/cinema.accdb'

# Join the base directory and the file path
abs_path = os.path.join(base_dir, file_path)
#con_str = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
connection_string = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + \
    abs_path
print('''type 
        c for create enter new values
        r for read
        u for update
        d for delete\n''')
while True:
    user_input = input("please type what you want to do\n")
    if user_input == "c":
        print("your table is here \n")
        crud_db_functions.read(connection_string)
        crud_db_functions.create(connection_string)
        print("data has been entered, updated table is here \n")
        crud_db_functions.read(connection_string)
    elif user_input == "r":
        print("your DB complete list is \n")
        crud_db_functions.read(connection_string)
    elif user_input == "u":
        crud_db_functions.update(connection_string)
        print("your table has been updated \n your updated table is given below")
        crud_db_functions.read(connection_string)
    elif user_input == "d":
        print("your table is here\n")
        crud_db_functions.read(connection_string)
        crud_db_functions.delete(connection_string)
        print("Now updated table is here after delete a row \n")
        crud_db_functions.read(connection_string)

    else:
        break
print("sorry sir galat command")
