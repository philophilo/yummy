from flask import (render_template, request, redirect, url_for,
                   session, flash)
from app import app
from app.model.user_model import User
from app.model.application import Application
from app.model.categories import Categories, Recipes
import datetime


application = Application()


def get_user_recipes(categories):
    category_recipes = dict()
    for key, value in categories.items():
        for recipe in value.recipes.values():
            category_recipes[key] = {
                'items': recipe.ingredients,
                'date': recipe.date,
                'recipe_name':  recipe.name,
                'category_name':value.name,
                'recipe_id': recipe.id}
    return category_recipes

def get_all_user_recipes():
    all_data = dict()
    for user, data in application.users.items():
        all_data[user] = {"data": get_user_recipes(data.categories)}
    return all_data

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if request.form['name'] and request.form['username'] and \
                request.form['password'] and \
                request.form['confirm-password']:
            if request.form['password'] == request.form[
                'confirm-password']:
                user = User(request.form['username'],
                            request.form['password'],
                            request.form['name'])
                if application.register_user(user):
                    flash("you have successfully signed up")
                    return redirect(url_for('login'))
                return render_template('index.html', error="Known \
                                       credentials proceed to login")
            error="password do not match"
            return render_template("index.html", error=error)
    error = "Method not allowed"
    return render_template("index.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_error = None
    if request.method == 'POST':
        if request.form['password'] and request.form['username']:
            if application.does_user_exist(
                request.form['username']):
                if application.login_user(request.form['username'],
                                          request.form['password']):
                    session['username'] = request.form['username']
                    flash('you have successfully logged in',
                          'login_success')
                    return redirect(url_for('yummy'))
            login_error = "No such account found, please signup"
            return render_template('index.html',
                                   login_error = login_error)
        login_error = "Username and password cannot be empty"
        return render_template('index.html', login_error=login_error)
    return render_template('index.html', login_error=login_error)


@app.route('/yummy', methods=['GET', 'POST'])
def yummy():
    yummy_error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    session.pop('flashes', None)
    yummy_recipes = get_user_recipes(user.categories)
    return render_template('profile.html',
                           yummy_recipes = yummy_recipes,
                           yummy_error=yummy_error,
                           user = user)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    add_error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        category_id = application.generate_random_key()
        if user.create_user_category(Categories(category_id, name)):
            category = user.get_category(category_id)
            if category.create_recipe(
                Recipes(application.generate_random_key(),
                        request.form['recipe-name'],
                        request.form['ingredients'],
                        datetime.datetime.now())):
                flash("The recipe has successfully been added")
                return redirect(url_for('recipes_feed'))
            add_error="The category exists already"
    session.pop('flashes', None)
    return render_template('add_recipe.html',
                           add_error=add_error, user=user)


@app.route('/recipes_feed', methods=['GET', 'POST'])
def recipes_feed():
    feed_error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    yummy_recipes = get_all_user_recipes()
    return render_template('index_feed.html', user=user,
                           yummy_recipes=yummy_recipes,
                           feed_error=feed_error)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/delete/recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    # TODO deleting entire category
    category = user.categories
    if not category:
        flash('Recipe does not exist', 'deleted')
        return redirect(url_for('yummy'))

    yummy_recipes = get_user_recipes(user.categories)
    if request.method == 'GET':
        if user.delete_category(recipe_id):
            flash("You have successfully deleted the recipe")
            return redirect(url_for('yummy'))
        error = "could not delete the specified recipe"
    return render_template('profile.html', error=error,
                           yummy_recipes=yummy_recipes,
                           user=user)


# update
@app.route('/update', methods=['GET', 'POST'])
def update_recipe():
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    if request.form['category_id'] and request.form['recipe_id']:
        category_id = request.form['category_id']
        recipe_id = request.form['recipe_id']

        category = user.get_category(category_id)
        if not category:
            return redirect(url_for('yummy'))

        cat_name = request.form['name']
        recipe_name = request.form['recipe-name']
        if cat_name:
            if user.update_category(category_id, cat_name):
                if category.update_recipe(recipe_id, recipe_name,
                                          request.form['ingredients'],
                                          datetime.datetime.now()):
                    flash("You have successfully updated you recipes")
                    return redirect(url_for('yummy'))
        error = "please provide the category name"
    yummy_recipes = get_user_recipes(user.categories)
    return render_template('profile.html',
                           yummy_recipes = yummy_recipes,
                           yummy_error=error,
                           user = user)
