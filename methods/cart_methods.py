from .database import get_db_connection
from flask import session

def cart_add_app(user_id, app_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = AddToCart {user_id}, {app_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()
    return output

def cart_remove_app(user_id, app_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = removeCartApp {app_id}, {user_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    
    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()
    return output

def cart_total_price(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue DECIMAL(10, 2);\
    EXEC GetTransactionTotalPrice {user_id}, @ReturnValue OUTPUT ;\
    SELECT @ReturnValue;"
    cursor.execute(query)
    total = cursor.fetchone()[0]

    conn.close()
    return total

def cart_show(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = showCart {user_id};\
    SELECT @ReturnValue;"
    cursor.execute(query)
    output = cursor.fetchall()

    conn.close()
    return output

def cart_checkout(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DECLARE @ReturnValue INT;\
    EXEC @ReturnValue = CheckOut {user_id};\
    SELECT @ReturnValue;"
    print(query)
    cursor.execute(query)
    output = cursor.fetchone()[0]

    cursor.commit()
    conn.close()
    return output