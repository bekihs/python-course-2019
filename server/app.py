from flask import *
from flask import request , render_template
import json
f = open("users.json" , "w")
f.close()
app = Flask(__name__, template_folder="static")
 
@app.route("/")
def index():
    return render_template("1.html" , name="world")
@app.route("/<name>")
def my_name(name):
    return render_template("1.html" , name=name)

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

if __name__ == '__main__':
    app.run(debug=False)

