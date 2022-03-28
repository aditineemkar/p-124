from flask import Flask, jsonify, request

app = Flask(__name__, template_folder='template')
tasks = [
    {
        'id': 1,
        'title': u'Study',
        'description': u'Science',
        'done': False
    },
    {
        'id': 2,
        'title': u'Code',
        'description': u'Need to code!',
        'done': False
    }
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully!"
    })


@app.route('/get-data')
def get_data():
    return jsonify({
        "data": tasks
    })


if __name__ == "__main__":
    app.run(debug=True)
