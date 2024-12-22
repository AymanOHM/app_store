from .database import get_db_connection

def add_app(form):
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
        query = f"exec AddApp '{name}', {app_version}, '{category}', {price}, '{app_description}', {dev_id}, '{app_path}', '{icon_path}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully added app '{name}' with id '{app_version}' to the database"
    except Exception as e:
        return f"Error when adding app: {e}"


def add_category(form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cat_name = form['cat_name']
        cat_description = form['cat_description']
        query = f"exec AddCategory '{cat_name}', '{cat_description}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully added category '{cat_name}' to the database"
    except Exception as e:
        return f"Error when adding category: {e}"


def add_dev(form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        email = form['email']
        name = form['name']
        password = form['password']
        contact_info = form['contact_info']
        website = form['website']
        query = f"exec AddDeveloper '{email}', '{name}', '{password}', '{contact_info}', '{website}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully added developer '{name}' to the database"
    except Exception as e:
        return f"Error when adding developer: {e}"


def add_user(form):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        name = form['name']
        email = form['email']
        password = form['password']
        pay_info = form['pay_info']
        balance = form['balance']
        
        query = f"exec AddUser '{name}', '{email}', '{password}', '{pay_info}', '{balance}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully added user '{name}' to the database"
    except Exception as e:
        return f"Error when adding user: {e}"