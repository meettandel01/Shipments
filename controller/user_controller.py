from flask import jsonify, request
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

from config.database import mongo

# API - 1 

def create_user():
    try:
        data = request.json
            
        username =  data.get('username')
        email = data.get('email')
        
        if not username or not email:
            return jsonify({
                "sucess" : "false",
                "Message" : "username and email are required"
            }), 400
        
        if username.matched == 1:
            return jsonify({
                "success": "false",
                "message": "A user with this email already exists"
            }),409
        
        mongo.db.user.insert_one({
            'username' : username,
            'email' :email
        })
        
        return jsonify({
            "success": 'true',
            "message": "User created successfully"
        }),201
    
    except Exception:
        return jsonify({
              "success": "false",
             "message": "Something went wrong, please try again"
        }), 500
    
    
# API - 2

def create_group(user_id):
    try:
    
        data = request.json
        group_name = data.get('group_name' )
        owner_id =  data.get('owner_id','user_id')
        member = data.get('member')
        base_currancy = data.get('base_currancy')
        
        if not group_name  or not owner_id or not member or not base_currancy:
                    return jsonify({
                        "sucess" : "false",
                        "message": "Please add all required field"
                    }), 400
        
        group = mongo.db.user.insert_one({
            'group_name' : group_name,
            'owner_id' : owner_id,
            'member' : member,
            'base_currancy' : base_currancy
        })
        
        return jsonify({
            "success": "true",
            "message": "Group created successfully",

        }),201
    
    
    except Exception:
        return jsonify({
              "success": "false",
             "message": "Something went wrong, please try again"
        }), 500
            


# API -3 

def create_expense(group_id):
    
    try:
    
        data = request.json()
        
        paid_by = data.get('paid_by','<user_id>')
        involved_members = data.get('involved_members','<user_ids>')
        amount = data.get('amount')
        expense_currancy = data.get('expense_currancy')
        description = data.get('description')
        
        
        if amount < 0:
            return jsonify({
                "sucess" : "false",
                "message": "amount must be grather then 0"
        }), 400
        
        if group_id.matched == 0:
            return jsonify({
                "sucess" : "false",
                 "message": "No group found with group id 1. "
            }),404
    except Exception:
        return jsonify({
              "success": "false",
             "message": "Something went wrong, please try again"
        }), 500
    
    
    
    


