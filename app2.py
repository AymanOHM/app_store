from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Establish a connection to the SQL Server
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'(LocalDB)\MSSQLLocalDB'
DATABASE_NAME = 'appstore'

command = f'Driver={{{DRIVER_NAME}}}; Server={SERVER_NAME}; Database={DATABASE_NAME}; Trusted_Connection=yes;'
conn = pyodbc.connect(command)
print("Connected to the database successfully")

# Create a cursor object to execute SQL queries
# cursor = conn.cursor()
# cursor.execute("exec EditApp @app_id = 23, @name= 'Facebook', @app_version= 0.123, @price= 0, @app_description= 'Social Media', @dev_id= 1, @app_path= 'D:/facebook/app', @icon_path= 'D:/facebook/icon';")
# cursor.commit() # Save to database

# cursor.execute('select * from apps')
# results = cursor.fetchall() # Get results
# print(results)

@app.route('/')
def index():
    return render_template('/.test/index.html')

@app.route('/search/', methods= ['GET', 'POST'])
def search():
    if request.method == 'POST':
        item = request.form['item']
        print("Searching for", item)
        return "<h1>Found</h1>" + item

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    