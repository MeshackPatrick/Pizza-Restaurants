from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)