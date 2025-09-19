from flask import Flask , jsonify , request
app = Flask(__name__)

todos = [
    {"label" : "My First Task" , "done":False}
]

@app.route('/todos',methods=['GET'])
def todo_list():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)