from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        "ID": 1,
        "Title": U"The Best Name Ever",
        "Description": U"Best",
        "Done": False
    },
    {
        "ID": 2,
        "Title": U"The Worst Name Ever",
        "Description": U"Worst",
        "Done": False
    }
]

@app.route("/")

def hello_world():
    return "Hello World"

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": tasks
    })

@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "ERROR",
            "message": "Data Not Provided"
        }, 400)
    task = {
        "ID": tasks[-1]["ID"] + 1,
        "Title": request.json["Title"],
        "Description": request.json["Description"],
        "Done": False
    }

    tasks.append(task)

    return jsonify({
            "status": "Success",
            "message": "Task added Successfully"
        })


if (__name__ == "__main__"):
    app.run(debug = True)