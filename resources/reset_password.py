import database
from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from flask_restful  import Resource

from models.User import User
