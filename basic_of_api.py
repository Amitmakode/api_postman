from flask import Flask,request, jsonify
import mysql.connector as conn

apps = Flask(__name__)

mydb = conn.connect(host = "localhost", user = "root", passwd = "Betul3146")
cursor = mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.mysqltable(name varchar(30), number int(12))")


@apps.route('/insert', methods = ["POST"])
def insert():
    if request.method == "POST":
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable values(%s, %s)",(name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

if __name__ == "__main__":
    apps.run() # run(port = 5001) we can use also it


