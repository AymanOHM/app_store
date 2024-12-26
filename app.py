from flask import Flask, render_template, request, redirect, url_for, session
from methods import search_app, search_cat, search_dev, search_user
from methods import add_app, add_category, add_dev, add_user
from methods import delete_app, delete_category, delete_dev, delete_user
from methods import update_app, update_category, update_dev, update_user
from methods import get_user_id, get_dev_id, user_signup, dev_signup
from methods import dev_add_app, dev_update_app, dev_delete_app, dev_show_apps
from methods.user_methods import user_search_app_with_cat, user_balance
from methods.viewapp_methods import app_get, app_get_developer
from methods.cart_methods import cart_add_app, cart_show, cart_total_price
from random import choices

app = Flask(__name__)
app.secret_key = "hello"

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

@app.route('/user_home', methods=['GET', 'POST'])
def user_home():
    if ('user_type' not in session) or session['user_type'] != 'user':
        return redirect(url_for('login'))
    
    categories = search_cat('')
    if request.method == 'POST':
        if 'search' in request.form:
            search_term = request.form['search']
            selected_cat = request.form['category']
            apps = user_search_app_with_cat(search_term, selected_cat)
            return render_template('user_home.html', search_term= search_term, selected_category= selected_cat, categories= categories, apps= apps)
        
    apps = user_search_app_with_cat()
    apps = choices(apps, k=9) if len(apps) > 9 else apps
    print(apps)
    return render_template('user_home.html', categories= categories, apps= apps)

@app.route('/dev_home', methods=['GET'])
def dev_home():
    if ('user_type' not in session) or session['user_type'] != 'developer':
        return redirect(url_for('login'))
    
    error = request.args.get('error')
    success = request.args.get('success')
    
    return render_template('dev_home.html', apps= dev_show_apps(), categories=search_cat(''), error=error, success=success)

@app.route('/view_app/<app_id>/', methods=['GET'])
def view_app(app_id):
    app = app_get(app_id)
    developer = app_get_developer(app_id)
    return render_template('view_app.html', app=app, developer= developer)


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


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if ('user_type' not in session) or session['user_type'] != 'user':
        return redirect(url_for('login'))
    
    user_id = session['id']
    
    # Get cart apps
    apps = cart_show(user_id)
    
    # Get total price
    #todo: get total price
    total = cart_total_price(user_id)
    if total == -1:
        return "Error happened while calculating total price"
    
    # Get user balance
    balance = user_balance(user_id)
    
    return render_template('cart.html', cart_items=apps, total= total, user_balance=balance)








# Login and Signup
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_type' in session:
        if session['user_type'] == 'user':
            return redirect(url_for('user_home'))
        else:
            return redirect(url_for('dev_home'))
    
    if request.method == 'POST':
            
        user_type = request.form['user_type']
        
        get_id_funcs = {
            'user': get_user_id,
            'developer': get_dev_id,
        }
        
        
        id = get_id_funcs[user_type](request.form)
        if id == -1:
            return render_template('login.html', error = "Invalid username or password")
        else:
            
            if user_type == 'user':
                session['user_type'] = "user"
                session['id'] = id
                return redirect(url_for('user_home'))
            else:
                session['user_type'] = "developer"
                session['id'] = id
                return redirect(url_for('dev_home'))
            
    error = request.args.get('error')
    success = request.args.get('success')
    return render_template('login.html', error=error, success=success)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_type = request.form['user_type']
        signup_functions = {
            'user': user_signup,
            'developer': dev_signup,
        }
        rsp = signup_functions[user_type](request.form)
        if rsp == -1:
            return render_template('signup.html', error = "There was an error creating your account")
        else:
            return redirect(url_for('login', success = "Account created successfully"))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user_type', None)
    session.pop('id', None)
    return redirect(url_for('login'))








# API Endpoints
@app.route('/dv_add_app', methods=['POST', 'GET'])
def dv_add_app():
    output = dev_add_app(request.form)
    
    if   output == -1:
        message = "There was an error adding the app"
        return redirect(url_for('dev_home', error=message))
    elif output == 1:
        message = "App name already exists"
        return redirect(url_for('dev_home', error=message))
    elif output == 2:
        message = "Icon path already exists"
        return redirect(url_for('dev_home', error=message))
    elif output == 3:
        message = "App path already exists"
        return redirect(url_for('dev_home', error=message))
    else:
        message = "App added successfully"
        return redirect(url_for('dev_home', success=message))

@app.route('/dv_update_app/<app_id>', methods=['POST'])
def dv_update_app(app_id):
    output = dev_update_app(app_id, request.form)
    
    if output == 1:
        message = "App name already exists"
        return redirect(url_for('dev_home', error=message))
    elif output == 2:
        message = "Icon path already exists"
        return redirect(url_for('dev_home', error=message))
    elif output == 3:
        message = "App path already exists"
        return redirect(url_for('dev_home', error=message))
    elif output == -1:
        message = "There was an error updating the app"
        return redirect(url_for('dev_home', error=message))
    else:
        message = "App updated successfully"
        return redirect(url_for('dev_home', success=message))

@app.route('/dv_delete_app/<app_id>', methods=['GET'])
def dv_delete_app(app_id):
    try:
        dev_delete_app(app_id)
        message = "App deleted successfully"
        return redirect(url_for('dev_home', success=message))
    except Exception as e:
        message = "There was an error deleting the app:\n{e}"
        return redirect(url_for('dev_home', error=message))

@app.route('/api/categories', methods=['GET'])
def api_categories():
    categories = [item[0] for item in search_cat('')]
    return categories

@app.route('/api/get_app_cat', methods=['GET'])
def api_get_app_cat():
    categories = [item[0] for item in search_cat('')]
    return categories

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        app_id = int( request.json.get('app_id') )
        user_id = session['id']
        output = cart_add_app(user_id, app_id)
        if output == 1:
            return {'success': False, 'error': 'App already exists in the cart'}
        elif output == 0:
            return {'success': True}
        else:
            return {'success': False, 'error': 'Unknown error occurred'}
        
    except Exception as e:
        print(e)
        return {'success': False, 'error': 'Unknown error occurred'}


if __name__ == '__main__':
    # Establish a connection to the SQL Server
    app.run(host='0.0.0.0', debug=True)
