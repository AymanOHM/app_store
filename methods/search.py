from .database import get_db_connection

def search_app(key= ""):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec SearchApp '{key}'"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"Error when searching for app: \n{e}"


def search_cat(key= ""):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec SearchCat '{key}'"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"Error when searching for category: \n{e}"


def search_user(key= ""):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec SearchUser '{key}'"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"Error when searching for user: \n{e}"


def search_dev(key= ""):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"exec SearchDev '{key}'"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"Error when searching for developer: \n{e}"