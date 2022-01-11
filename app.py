from flask import Flask, Response
from flask_bcrypt import Bcrypt
from flask_restful  import Api

from database.db import initialize_db
from resources.routes import initialize_routes
from models.User import User


app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://adminPGabriel:adminPGabriel@cluster0.pgpdg.mongodb.net/taskListIonic?retryWrites=true&w=majority"'
}

initialize_db(app)

@app.route('/')
def home():
    usuarios = User.objects.all()
    return Response(usuarios, mimetype="application/json", status=200)


initialize_routes(api)

app.run()
