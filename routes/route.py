from flask import render_template, request, jsonify
from server import app
from database.db import connectionSQL, insert_records, consult_records


@app.route('/')
def home_page():
    connectionSQL()
    return render_template("home.html")
    
@app.route('/register')
def register_page():
    return render_template('register.html')
    
@app.route('/consult')
def consult_page():
    return render_template('consult.html')
    
@app.route("/register_user", methods=["post"])
def register_user():
    data_patient = request.form
    patnr, titel, vname, nname , gbdat = data_patient["patnr"], data_patient["titel"], data_patient["vname"], data_patient["nname"],  data_patient["gbdat"]
    insert_records(patnr, titel,  vname, nname,  gbdat)
    return render_template("register.html")


@app.route("/consult_user", methods=["post"])
def consult_user():
    data_id = request.get_json()
    result = consult_records(data_id["patnr"])
    if result != None:
        name = result[0][2]
        lastname = result[0][3]
        resp_data = {"status":"ok",
            "name": name,
            "lasrname": lastname
        }
    else:
        resp_data = {"status":"error"}
    print(result)
    return jsonify(resp_data)
