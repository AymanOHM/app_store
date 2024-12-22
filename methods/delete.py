from .database import get_db_connection

def delete_app(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec DeleteApp '{id}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully deleted app with id '{id}'"
    except Exception as e:
        return f"Error when deleting app: {e}"


def delete_category(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec DeleteCategory '{id}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully deleted category with id '{id}'"
    except Exception as e:
        return f"Error when deleting category: {e}"


def delete_dev(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec DeleteDeveloper '{id}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully deleted developer with id '{id}'"
    except Exception as e:
        return f"Error when deleting developer: {e}"


def delete_user(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec DeleteUser '{id}'"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        return f"Successfully deleted user with id '{id}'"
    except Exception as e:
        return f"Error when deleting user: {e}"