from flask import Flask, Response
from flask_bcrypt import Bcrypt
from flask_restful  import Api
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from routes import initialize_routes
from resources.errors import errors


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://adminPGabriel:adminPGabriel@cluster0.pgpdg.mongodb.net/taskListIonic?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

app.run()
