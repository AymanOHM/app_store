from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

def get_db_connection():
    # Database Connection
    DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
    SERVER_NAME = r'(LocalDB)\MSSQLLocalDB'
    DATABASE_NAME = 'appstore'
    conn = pyodbc.connect(F'DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};')
    return conn

@app.route('/')
def home():
    return "<h1> Welcome to the App Store </h1>"

@app.route('/crud', methods=['GET', 'POST'])
def crud():
    if request.method == 'POST':
        operation = request.form['operation']
        entity = request.form['entity']
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if operation == 'search':
            search_term = request.form['search']
            query = f"SELECT * FROM {entity}s WHERE name LIKE ?"
            cursor.execute(query, ('%' + search_term + '%',))
            results = cursor.fetchall()
            conn.close()
            return render_template('crud.html', results=results, entity=entity)
        
        elif operation == 'add':
            if entity == 'user':
                name = request.form['name']
                email = request.form['email']
                password = request.form['password']
                pay_info = request.form['pay_info']
                balance = request.form['balance']
                query = "INSERT INTO users (name, email, password, pay_info, balance) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(query, (name, email, password, pay_info, balance))
            elif entity == 'developer':
                name = request.form['name']
                email = request.form['email']
                password = request.form['password']
                contact_info = request.form['contact_info']
                website = request.form['website']
                query = "INSERT INTO developers (name, email, password, contact_info, website) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(query, (name, email, password, contact_info, website))
            elif entity == 'app':
                name = request.form['name']
                app_version = request.form['app_version']
                price = request.form['price']
                app_description = request.form['app_description']
                dev_id = request.form['dev_id']
                app_path = request.form['app_path']
                icon_path = request.form['icon_path']
                query = "INSERT INTO apps (name, app_version, price, app_description, dev_id, app_path, icon_path) VALUES (?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (name, app_version, price, app_description, dev_id, app_path, icon_path))
            elif entity == 'category':
                cat_name = request.form['cat_name']
                cat_description = request.form['cat_description']
                query = "INSERT INTO categories (cat_name, cat_description) VALUES (?, ?)"
                cursor.execute(query, (cat_name, cat_description))
            conn.commit()
            conn.close()
            return redirect(url_for('crud'))
    
    return render_template('crud.html')

@app.route('/delete/<entity>/<id>', methods=['GET'])
def delete(entity, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"DELETE FROM {entity}s WHERE app_id = ?"
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('crud'))

@app.route('/update/<entity>/<id>/', methods=['POST'])
def update(entity, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if entity == 'user':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        pay_info = request.form['pay_info']
        balance = request.form['balance']
        query = "UPDATE users SET name = ?, email = ?, password = ?, pay_info = ?, balance = ? WHERE user_id = ?"
        cursor.execute(query, (name, email, password, pay_info, balance, id))
    elif entity == 'developer':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        contact_info = request.form['contact_info']
        website = request.form['website']
        query = "UPDATE developers SET name = ?, email = ?, password = ?, contact_info = ?, website = ? WHERE dev_id = ?"
        cursor.execute(query, (name, email, password, contact_info, website, id))
    elif entity == 'app':
        name = request.form['name']
        app_version = request.form['app_version']
        price = request.form['price']
        app_description = request.form['app_description']
        dev_id = request.form['dev_id']
        app_path = request.form['app_path']
        icon_path = request.form['icon_path']
        query = "UPDATE apps SET name = ?, app_version = ?, price = ?, app_description = ?, dev_id = ?, app_path = ?, icon_path = ? WHERE app_id = ?"
        cursor.execute(query, (name, app_version, price, app_description, dev_id, app_path, icon_path, id))
    elif entity == 'category':
        cat_name = request.form['cat_name']
        cat_description = request.form['cat_description']
        query = "UPDATE categories SET cat_name = ?, cat_description = ? WHERE cat_name = ?"
        cursor.execute(query, (cat_name, cat_description, id))
    conn.commit()
    conn.close()
    return redirect(url_for('crud'))

if __name__ == '__main__':
    # Establish a connection to the SQL Server
    app.run(host= '0.0.0.0', debug=True)