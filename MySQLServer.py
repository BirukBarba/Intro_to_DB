import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user, password, host if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ayelusql@24785'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure resources are properly closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional message for clarity
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()