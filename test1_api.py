from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/abc', methods = ['GET','POST']) # GET is url calling and POST is body, /abc is a rout which is calling for run the programm
def test1():
    if request.method=='POST':
        a = request.json["num1"]
        b = request.json["num2"]
        result = a + b
        return jsonify((str(result)))

@app.route('/abc/amit', methods = ['GET','POST']) # GET is url calling and POST is body, /abc/amit is a rout which is calling for run the programm
def test2():
    if request.method=='POST':
        a = request.json["num1"]
        b = request.json["num2"]
        result = a * b
        return jsonify((str(result)))


@app.route('/abc/amit/kumar', methods = ['GET','POST']) # GET is url calling and POST is body, /abc/amit/kumar is a rout which is calling for run the programm
def test3 ():
    if request.method=='POST':
        a = request.json["num1"]
        b = request.json["num2"]
        result = a - b
        return jsonify((str(result)))



if __name__ == '__main__':
    app.run(port= 5001)


