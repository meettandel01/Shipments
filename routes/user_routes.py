from flask import Blueprint

from controller.user_controller import(
    create_user,
    create_group, 
    create_expense,
    
)

app.route_Blueprint(
    'user_routes' ==  Blueprint ,
    __name__
)

@user_routes.route('/user', methods = ['POST'])
def add_user():
    return create_user

@user_routes.route('/group', methods = ['POST'])
def add_group():
    return create_group()

@user_routes.route('/group/<group_id/expense>', methods = ['POST'])
def add_group():
    return create_expense()

