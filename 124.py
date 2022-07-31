from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[{"id":1,"name":"whats your name","contact":"telephone","done":False }, 
{
    "id":2,"name":"friends ","contact":"phone","done":False
}]
@app.route("/add-data",methods=["POST"])

def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"

        },400)

    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["name"],
        "discription":request.json.get("contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({"status":"succes",
    "message":"task added succesfully"
    })

@app.route("/get-data")

def gettask():
    return jsonify({"data":tasks})

if __name__=="__main__":
    app.run()      



