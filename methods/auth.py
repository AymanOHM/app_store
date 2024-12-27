from .database import get_db_connection


def get_user_id(form):
    username = form['name']
    password = form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = UserLogin '{username}', '{password}';\
    SELECT @ReturnValue;"
    cursor.execute(query)
    user_id = cursor.fetchone()[0]
    conn.close()

    return user_id

def get_dev_id(form):
    username = form['name']
    password = form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = DevLogin '{username}', '{password}';\
    SELECT @ReturnValue;"
    cursor.execute(query)
    dev_id = cursor.fetchone()[0]
    conn.close()

    return dev_id

def user_signup(form):
    name = form['name']
    email = form['email']
    password = form['password']
    pay_info = form['pay_info']
    balance = form['balance']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = UserSignUp '{name}', '{email}', '{password}', '{pay_info}', {balance if balance else 0};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()

    return output

def dev_signup(form):
    name = form['name']
    email = form['email']
    password = form['password']
    contact_info = form['contact_info']
    website = form['website']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = DevSignUp '{name}', '{email}', '{password}', '{contact_info}', '{website}';\
    SELECT @ReturnValue;"
    cursor.execute(query)

    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()

    return output