from flask import Flask, request, jsonify
import mysql.connector as conn
app = Flask(__name__)

@app.route('/testfun')

def test():
    get_name = request.args.get('get_name')
    return "this is my first function on postman get{}".format(get_name)

@app.route('/get_data') # very imp function for data serches in browser
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con =conn.connect(host ="localhost", user = "root", password = "Betul3146", database = db)
        cur =  con.cursor(dictionary = True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__=='__main__':
    app.run(port=5002)
#http://127.0.0.1:5002/testfun?get_name = amit kaumar




"""@app.route('/testfun')

def test():
    get_name = request.args.get('get_name')
    mbl_num = request.args.get('mobile')
    mail_id = request.args.get('mail')
    return "this is my first function on postman get{} {} {}".format(get_name, mbl_num, mail_id)

if __name__=='__main__':
    app.run(port=5002)
#http://127.0.0.1:5002/testfun?get_name = amit kaumar & mobile = 82946598263 & mail = maitbd@jagfdg.com
"""


# first execute in postman than search in url as like given example