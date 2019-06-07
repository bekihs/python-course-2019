from flask import Flask, jsonify
app = Flask(__name__, template_folder="templates")

tasks = [
    {
        'title': u'Buy groceries',
        'done': False
    },
    {
        'title': u'Learn Python',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

    # render_template, request

@app.route('/user' ,  methods=['get'])
def index():
    return "Hello, World!"
    
@app.route('/user', methods=['POST'])
def get_user():
  #dont forget to import the request object from flask. 
  #inside the form dictionary we can find all the parameters that the client sent us
  username = request.form['username']
  password = request.form['password']
  #login(arg,arg) is a function that tries to log in and returns true or false
  status = username +" " + password
  return status

@app.route('/user/<name>')
def hello(name=None):
  #name=None ensures the code runs even when no name is provided
  return render_template('user-profile.html', name=name)
@app.route('/books')
def books():
    return "books" 
 
@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=False)

    