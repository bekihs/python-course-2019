from flask import *
from flask import request , render_template
import json
import requests  
from User import User 
app = Flask(__name__, template_folder="static")
 
lstUsers = []

@app.route("/")
def index():
    name = request.args.get('name')
    if (name is None):
        name = "world"
    return render_template("1.html" , name=name)

@app.route("/users")
def users():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    print(res)
    data = res.json()
    print(data)
    return jsonify(data)
    
# @app.route("/<name>")
# def my_name(name):
#     return render_template("1.html" , name=name)

@app.route("/user" , methods=["post"])
def createUser():
    if (request.form["firstName"] == None):
        abort({"message" , "missing firstName"})
    user = User(request.form["firstName"] , request.form["lastName"])
    lstUsers.append(user)
    return jsonify(user.serialize())
@app.route("/getusers")
def getUsers():
    return jsonify([user.serialize() for user in lstUsers])
@app.route("/message")
def get_messages():
    f = open("users.json" , "r")
    lines = f.readlines()
    return jsonify(lines)
@app.route("/message" , methods=['post'])
def new_message():
    print(json.dumps(request.form))
    f = open("users.json" , "a")
    f.writelines([ json.dumps(request.form) , ","])
    f.close()
    #save data in database 
    return "yessss" + request.form["text"]


@app.route("/user" , methods=['put'])
def update_user():
    return "this is an updae"
@app.route("/user/<user_id>" , methods=['get'])
def get_user(user_id):
    return "this is a get"
@app.route("/user/<user_id>" , methods=['delete'])
def delete_user(user_id):
    return "this is a delete"

@app.route("/<username>/<int:age>")
def user(username,age):
    return jsonify({'name':username ,'age':age , 'lastname':request.args.get('lastname')})

@app.route("/<username>/<string:lastname>")
def user_with_name(username,lastname):
    return jsonify({'name':username ,'lastname':lastname })


@app.route("/books")
def books():
    return jsonify(["first book" , "second Book"])

@app.errorhandler(500)
def error_page(e):
    return "oh noooo :("
    
@app.errorhandler(404)
def error_page404():
    return "sorry we dont have the oage you're looking for"

if __name__ == '__main__':
    app.run(debug=False)

