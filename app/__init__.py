from flask import Flask
from flask_restx import Api


app = Flask(__name__)
api = Api(
    app, 
    title='BoilerPlate1',
    description='EndPoinst BoilerPlate',
    doc='/swagger-ui'
)