from flask import *
from flask import request

app = Flask(__name__, template_folder="templates")
 
@app.route("/")
def index():
    return "hi there, this is the best web site in the world"

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

