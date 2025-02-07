from .database import get_db_connection

def update_app(id, form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        name = form['name']
        app_version = form['app_version']
        category = form['category']
        price = form['price']
        app_description = form['app_description']
        dev_id = form['dev_id']
        app_path = form['app_path']
        icon_path = form['icon_path']
        
        query = f"exec UpdateApp {id}, '{name}', '{category}', {app_version}, {price}, '{app_description}', {dev_id}, '{app_path}', '{icon_path}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully updated app '{name}' with id {id}"
    except Exception as e:
        return f"Error when updating app: \n{e}"


def update_category(id, form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cat_name = form['cat_name']
        cat_description = form['cat_description']
        query = f"exec UpdateCategory {id}, '{cat_name}', '{cat_description}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully updated category '{cat_name}'"
    except Exception as e:
        return f"Error when updating category: \n{e}"


def update_dev(id, form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        email = form['email']
        name = form['name']
        password = form['password']
        contact_info = form['contact_info']
        website = form['website']
        query = f"exec UpdateDeveloper {id}, '{email}', '{name}', '{password}', '{contact_info}', '{website}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully updated developer '{name}'"
    except Exception as e:
        return f"Error when updating developer: \n{e}"


def update_user(id, form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        name = form['name']
        email = form['email']
        password = form['password']
        pay_info = form['pay_info']
        balance = form['balance']
        
        query = f"exec UpdateUser {id}, '{name}', '{email}', '{password}', '{pay_info}', '{balance}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully updated user '{name}'"
    except Exception as e:
        return f"Error when updating user: \n{e}"