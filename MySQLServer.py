import mysql.connector
from mysql.connector import Error

def create_database():
   
    connection = None
    cursor = None
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="My#SQL00"  
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


if __name__ == "__main__":
    create_database()