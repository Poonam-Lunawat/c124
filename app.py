from flask import Flask,jsonify,request
#jsonify is helper method provided by flask to properly return JSON data

app = Flask(__name__)
tasks =[
    {
        'id':1,
        'title': u'Buy groceries',
        'description': u'Milk,cheese, Pizza, fruit',
        'done': False
    },
    {
        'id':2,
        'title': u'Learn Python',
        'description': u'Find out a good tutorial',
        'done': False
    },
]
@app.route('/')
def hello_world():
    return "hello world"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"},400)

    task ={
        'id':tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })


if(__name__=="__main__"):
    app.run(debug=True) # default port number is 5000
    #app.run(debug=True, port=8080) it will change port number
    