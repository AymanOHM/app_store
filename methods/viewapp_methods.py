from .database import get_db_connection


def app_get(app_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = showAppDetails {app_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    app = cursor.fetchone()
    conn.close()
    return app

def app_get_developer(app_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = getAppDeveloper {app_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    dev_id = cursor.fetchone()
    conn.close()
    return dev_id

def app_get_reviews(app_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = showAppReviews {app_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    reviews = cursor.fetchall()
    conn.close()
    return reviews