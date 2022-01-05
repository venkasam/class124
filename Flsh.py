from flask import Flask,jsonify,request

app=Flask(__name__)
tasks = [ { 'id': 1, 'title': u'Buy groceries', 'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': False }, 
         { 'id': 2, 'title': u'Learn Python', 'description': u'Need to find a good Python tutorial on the web', 'done': False } ]
@app.route("/")
def hello():
    return "helloworld"
@app.route("/aboutme")
def about():
    return "this is samiksha "
@app.route("/adddata",methods=["POST"])
def attask():
    if not request.json:
        return jsonify({
            'staus':"error",
            "message":"pleaseproveidethedata"
        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    
        }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"sent"
    })
    @app.route("/get-data") 
    def get_task():
        return jsonify({ "data" : tasks })
    

if __name__=="__main__":
    app.run()
 