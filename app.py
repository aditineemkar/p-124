from flask import Flask, jsonify, request

app = Flask(__name__, template_folder='template')
tasks = [
    {
        'id': 1,
        'done': false,
        'contact': u'9898989898',
        'name': u"Raju"
    },
    {
         'id': 2,
        'done': false,
        'contact': u'9898989898',
        'name': u"Rajesh"
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
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
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
