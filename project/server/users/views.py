# project/server/users/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

get_blueprint = Blueprint('users', __name__)

class ViewUsers(MethodView):
    """
    View all users
    """

    def get(self):
        
        json_list = User.query.all()
        lst = []
        for i  in json_list:
            lst.append(i.email)
        responseObject = {
            'status': 'success',
            'message': lst,
        }

        return make_response(jsonify(responseObject)), 201


users_view = ViewUsers.as_view('view_users')

get_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)