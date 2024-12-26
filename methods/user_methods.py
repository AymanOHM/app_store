from .database import get_db_connection

def user_search_app_with_cat(search_term= "", selected_cat= ""):
    search_term = f"'{search_term}'" if search_term else 'NULL'
    selected_cat = f"'{selected_cat}'" if selected_cat else 'NULL'
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = SearchAppsWithCategory {search_term}, {selected_cat};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    
    apps = cursor.fetchall()
    conn.close()
    return apps


def user_balance(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = showBalance {user_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    balance = cursor.fetchone()[0]
    conn.close()
    return balance