from .database import get_db_connection
from flask import session

def dev_add_app(form):
    name = form['name']
    app_version = form['app_version']
    description = form['description']
    price = form['price']
    category = form['category']
    dev_id = session['id']
    app_path = form['app_path']
    icon_path = form['icon_path']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = DevAddApp '{name}', '{category}', '{app_version}', {price if price else 0}, '{description}', '{dev_id}', '{app_path}', '{icon_path}';\
    SELECT @ReturnValue;"
    
    cursor.execute(query)
    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()

    return output

def dev_update_app(app_id, form):
    name = form['name']
    app_version = form['app_version']
    description = form['description']
    price = form['price']
    category = form['category']
    app_path = form['app_path']
    icon_path = form['icon_path']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = DevUpdateApp {app_id}, '{name}', '{category}', '{app_version}', {price if price else 0}, '{description}', '{app_path}', '{icon_path}';\
    SELECT @ReturnValue;"
    
    cursor.execute(query)
    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()

    return output

def dev_delete_app(app_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = DevDeleteApp {app_id};\
    SELECT @ReturnValue;"
    
    cursor.execute(query)

    cursor.commit()
    conn.close()

def dev_show_apps():
    dev_id = session['id']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"exec showDevApps '{dev_id}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    return results