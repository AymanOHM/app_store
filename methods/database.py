import pyodbc

def get_db_connection():
    # Database Connection
    DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
    SERVER_NAME = r'(LocalDB)\MSSQLLocalDB'
    DATABASE_NAME = 'appstore'
    conn = pyodbc.connect(F'DRIVER={{{DRIVER_NAME}}};SERVER={
                          SERVER_NAME};DATABASE={DATABASE_NAME};')
    return conn