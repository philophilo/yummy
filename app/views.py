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

