import json
import os.path

import pymongo as pymongo
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify, request, redirect
from form import SignUpForm, LoginForm

app = Flask(__name__)
app.secret_key = "kjjjgjgkjlhuaiy7u"
conn_string = "mongodb+srv://ksp1510:kishan@cluster0.syoit.mongodb.net/db_rental?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"
my_client = pymongo.MongoClient(conn_string)
db = my_client["db_rental"]
user = db['users']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up.html', form=form)


@app.route('/cars', methods=['GET', 'POST'])
def cars():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        add = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        contact = request.form['contact']
        email = request.form['email']
        userid = request.form['userid']
        password = request.form['password']
        lic_num = request.form['lic_num']
        lic_val = request.form['lic_val']
        rto = request.form['rto']

        mydict = {"First_Name": fname, "Last_Name": lname, "Address": add, "City": city, "Pincode": pin,
                  "Contact": contact,
                  "E-mail": email, "User_Id": userid, "Password": password, "License-Numebr": lic_num,
                  "Validity": lic_val,
                  "RTO": rto}

        x = user.insert_one(mydict)
        print(x)

    return render_template("cars.html")


@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('aboutus.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
