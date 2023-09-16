from flask import Flask, render_template, request, url_for, redirect, flash, session
from model import generate_text
from input import rearrange_sentence
from pymongo import MongoClient
import certifi

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

# MongoDB setup
connection = 'mongodb+srv://jyee25:jyee@vthacks.lza3x1j.mongodb.net/'
client = MongoClient(connection, tlsCAFile=certifi.where())
#connection to users mongodb
dbusers = client['users']
collection = dbusers['login']

@app.route('/')
def index():
    
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uName = request.form["field_user"]
        uPass = request.form["field_pass"]
        if(collection != None):
            print("yes")

        user = collection.find_one({"user": uName})
        if user and user['pass'] == uPass:
            print("User authenticated!")
            session['username'] = uName
            session['logged in'] = True
            return redirect(url_for('index'))
        #user not found
        return render_template('login.html', error=True)

    return render_template('login.html')



@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")


@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form.get("input_text")

    if not input_text:
        flash("No input text provided")
        return redirect(url_for('index'))

    input_text = rearrange_sentence(input_text)#Fix sentence
    decoded_output = generate_text(input_text)
    
    flash(f"Prediction: {decoded_output}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
