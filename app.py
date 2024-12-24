from flask import Flask, render_template, request, redirect, url_for
from methods import search_app, search_cat, search_dev, search_user
from methods import add_app, add_category, add_dev, add_user
from methods import delete_app, delete_category, delete_dev, delete_user
from methods import update_app, update_category, update_dev, update_user

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/crud', methods=['GET', 'POST'])
def crud():
    if request.method == 'POST':
        operation = request.form['operation']
        entity = request.form['entity']

        if operation == 'search':
            search = {
                'app': search_app,
                'category': search_cat,
                'developer': search_dev,
                'user': search_user,
            }
            search_term = request.form['search']
            results = search[entity](search_term)
            message = f"Results for {entity.capitalize()} with '{search_term}':" if results else f"No results for {
                entity.capitalize()} with '{search_term}'"
            return render_template('crud.html', message=message, results=results, entity=entity)

        elif operation == 'add':
            adder = {
                'app': add_app,
                'category': add_category,
                'developer': add_dev,
                'user': add_user,
            }
            message = adder[entity](request.form)

            return render_template('crud.html', message=message)

    return render_template('crud.html')


@app.route('/delete/<entity>/<id>', methods=['GET'])
def delete(entity, id):
    delete_functions = {
        'app': delete_app,
        'category': delete_category,
        'developer': delete_dev,
        'user': delete_user,
    }
    message = delete_functions[entity](id)
    return render_template('crud.html', message=message)


@app.route('/update/<entity>/<id>/', methods=['POST'])
def update(entity, id):
    update_functions = {
        'app': update_app,
        'category': update_category,
        'developer': update_dev,
        'user': update_user,
    }
    message = update_functions[entity](id, request.form)
    return render_template('crud.html', message=message)


# API Endpoints
@app.route('/api/categories', methods=['GET'])
def api_categories():
    categories = [item[0] for item in search_cat('')]
    return categories

@app.route('/api/get_app_cat', methods=['GET'])
def api_get_app_cat():
    categories = [item[0] for item in search_cat('')]
    return categories


if __name__ == '__main__':
    # Establish a connection to the SQL Server
    app.run(host='0.0.0.0', debug=True)
