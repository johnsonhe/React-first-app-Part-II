from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = str(uuid.uuid4())
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToAdd = request.get_json()
      users['users_list'].remove(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   
   elif request.method == 'DELETE':
      for user in users['users_list']:
        if user['id'] == id:
           users['users_list'].remove(user)
           resp = jsonify(success=True)
           resp.status_code = 204
           return resp
      resp = jsonify({"error 404": "resource not found"})
      resp.status_code = 404
      return resp
   return users

@app.route('/users')
def get_usersnamejob(name,job):
   search_name = request.args.get('name') #accessing the value of parameter 'name'
   search_job = request.args.get('job') #accessing the value of parameter 'job'
   if search_name :
      subdict = {'users_list' : []}
      for user in users['users_list']:
         if user['name'] == search_name and user['job'] == search_job:
            subdict['users_list'].append(user)
      return subdict
   return users