print("--- SCRIPT IS RUNNING ---")
import mysql.connector
from mysql.connector import Error

def create_database():
    """ Connects to MySQL and creates the alx_book_store database """
    connection = None
    cursor = None
    try:
        # Connect to MySQL Server (update with your password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MySQL00"  # <-- Good, you updated this
        )
        
        sql_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# THIS BLOCK MUST HAVE NO INDENTATION (no spaces at the front)
create_database()
# The stray " at the end has also been removed.