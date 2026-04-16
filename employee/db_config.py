import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sattireddy@123!",
        database="employee_db"
    )
