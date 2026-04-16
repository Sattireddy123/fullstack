import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Sattireddy@123!",
        database="user_db",
        auth_plugin='mysql_native_password'
    )