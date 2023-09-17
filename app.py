from flask import Flask, render_template, request, url_for, redirect, flash
from model import generate_text
from input import rearrange_sentence
from flask_pymongo import PyMongo
import en_core_web_sm
from pymongo import MongoClient
import certifi




connection = 'mongodb+srv://jyee25:jyee@vthacks.lza3x1j.mongodb.net/'
client = MongoClient(connection, tlsCAFile=certifi.where())
# Select the correct database and collection

db = client['gridwords']  # replace 'your_database_name' with the name of your database
collection = db['noun']

app = Flask(__name__, static_folder='static', template_folder='templates')

app.secret_key = 'your_super_secret_key'  


@app.route('/', methods=['GET', 'POST'])
def index():
    data = {}
    selected_words = []
    if request.method == 'POST':
        selected_words_json = request.form.get("selected_words")
        if selected_words_json:
            selected_words = json.loads(selected_words_json)
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        data[collection_name] = [doc.get('word', doc.get(collection_name)) for doc in collection.find({}, {"word": 1, collection_name: 1, "_id": 0}) if 'word' in doc or collection_name in doc]
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

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
    app.run(debug=True)
