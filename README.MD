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

---

## Features

### 1. Image Recognition

Before using language models, the system must recognize the content of an image.

### 2. Pre-trained Model

For this project, we utilize the **Hugging Face transformers library**. Specifically, the `Grammarly/coedit-large` text-to-text (txt) model is used.

### 3. Database

[]

### 4. User Interface

- Fetch related words/sentences from the database.
- Display or verbalize the words/sentences for the user.

### 5. Integration with Language Models

[]

### 6. Continuous Learning

[]

---

## Final Thoughts

[]