from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
from waitress import serve

conn = mysql.connector.connect(host = "hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user = "admin", password = "abcd1234", database = "hospital")
cur = conn.cursor()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/doctor', methods=["GET", "POST"])
def doctor():
    conn = mysql.connector.connect(host="hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user="admin",
                                   password="abcd1234", database="hospital")
    cur = conn.cursor()
    q = "select * from doctor;"
    cur.execute(q)
    records = cur.fetchall()
    return render_template("doctor.html", data = records)


@app.route('/patient', methods=["GET", "POST"])
def patient():
    conn = mysql.connector.connect(host="hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user="admin",
                                   password="abcd1234", database="hospital")
    cur = conn.cursor()
    q = "select * from patient;"
    cur.execute(q)
    records = cur.fetchall()
    return render_template("patient.html", data = records)


@app.route('/adddoctor', methods=["GET", "POST"])
def adddoctor():
    if request.method == "POST":
        conn = mysql.connector.connect(host="hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user="admin",
                                       password="abcd1234", database="hospital")
        cur = conn.cursor()
        name = request.form.get('name')
        q = f'insert into doctor(fname) values("{name}");'
        cur.execute(q)
        conn.commit()
    return render_template("adddoctor.html")


@app.route('/addpatient', methods=["GET", "POST"])
def addpatient():
    if request.method == "POST":
        conn = mysql.connector.connect(host="hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user="admin",
                                       password="abcd1234", database="hospital")
        cur = conn.cursor()
        name = request.form.get('name')
        q = f'insert into patient(fname) values("{name}");'
        print(q)
        cur.execute(q)
        conn.commit()
    return render_template("addpatient.html")


@app.route('/deldoctor', methods=["GET", "POST"])
def deldoctor():
    if request.method == "POST":
        conn = mysql.connector.connect(host="hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user="admin",
                                       password="abcd1234", database="hospital")
        cur = conn.cursor()
        id = request.form.get('id')
        q = f'delete from doctor where id = {id};'
        cur.execute(q)
        conn.commit()
    return render_template("deldoctor.html")


@app.route('/delpatient', methods=["GET", "POST"])
def delpatient():
    if request.method == "POST":
        conn = mysql.connector.connect(host="hospital.crnfmujofayx.us-east-1.rds.amazonaws.com", user="admin",
                                       password="abcd1234", database="hospital")
        cur = conn.cursor()
        id = request.form.get('id')
        q = f'delete from patient where id = {id};'
        cur.execute(q)
        conn.commit()
    return render_template("delpatient.html")

if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, host='0.0.0.0', port=80)