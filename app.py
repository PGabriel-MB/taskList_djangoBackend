from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful  import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail

from database.db import initialize_db
from routes import initialize_routes


app = Flask(__name__)
CORS(app)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)

# imports requiring app and mail
from resources.errors import errors

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://adminPGabriel:adminPGabriel@cluster0.pgpdg.mongodb.net/taskListDB?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)
