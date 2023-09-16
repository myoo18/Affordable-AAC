from flask import Flask, jsonify, render_template, request, url_for, redirect, flash
from model import generate_text

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'  # replace 'your_super_secret_key' with a random string

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form.get("input_text")

    if not input_text:
        flash("No input text provided")
        return redirect(url_for('index'))

    decoded_output = generate_text(input_text)
    
    flash(f"Prediction: {decoded_output}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
