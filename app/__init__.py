from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from config import environment
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(environment[getenv('ENVIRONMENT')])

api = Api(
    app, 
    title='BoilerPlate1',
    description='EndPoinst BoilerPlate',
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)