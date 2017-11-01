from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import views

app.config.from_object('config.BaseConfig')
app.secret_key = "kj][p]l/=7<F9>j 9877<F10>q2e"
app.config['SESSION_TYPE'] = "filesystem"
app.debug=True

