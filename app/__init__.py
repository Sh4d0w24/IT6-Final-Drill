from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'jake'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'northwind'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from app import routes