from .database import get_db_connection

def search_app(key= ""):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"exec SearchApp '{key}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def search_cat(key= ""):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"exec SearchCat '{key}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def search_user(key= ""):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"exec SearchUser '{key}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def search_dev(key= ""):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"exec SearchDev '{key}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results