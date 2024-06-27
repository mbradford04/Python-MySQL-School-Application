import mysql.connector
from mysql.connector import Error

# create function to establish connection from main.py to MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database Connection Successful!!")
    except Error as err:
        print(f"Error: {err}")

    return connection

# call function to establish connection from main.py to MySQL
create_server_connection("localhost", "root","student")