# Project Setup and Instructions

## Setup

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install transformers
   pip install torch torchvision
   pip install Flask
   pip install flask_pymongo
   pip install pymongo
   pip install werkzeug
   pip install certifi
   pip install ssl
   pip install spacy
   pip install scikit-learn
   python -m spacy download en_core_web_sm
   ```

4. **Upgrade pip (if needed)**

   ```bash
   python.exe -m pip install --upgrade pip
   ```

if spacy didnt work
   ```bash
   python -m spacy download en
   ```

## Running the Application

To run the project:

```bash
python main.py
```
