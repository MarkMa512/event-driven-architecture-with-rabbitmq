from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    pass

@app.route('/')
def index():
    return "Hello! Apple"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')