import spacy
from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb+srv://jyee25:jyee@vthacks.lza3x1j.mongodb.net/')

# Access the 'gridwords' database
db = client['gridwords']

# Load SpaCy's model
nlp = spacy.load("en_core_web_sm")

def rearrange_sentence(sentence):
    doc = nlp(sentence)
    
    # Get POS and tokenize
    adjectives = [token.text for token in doc if token.pos_ in ["ADJ", "ADP", "DET"]]
    verbs = [token.text for token in doc if token.pos_ in ["VERB", "INTJ", "AUX", "ADV"]]
    nouns = [token.text for token in doc if token.pos_ in ["PROPN", "NOUN"]]
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    others = [token.text for token in doc if token.pos_ not in ["ADJ", "ADP", "DET", "VERB", "INTJ", "AUX", "ADV", "PROPN", "NOUN", "PRON"]]

    # Simple rearrangement
    rearranged_tokens = pronouns + verbs + adjectives + nouns + others
    
    # Convert back to string
    rearranged_sentence = ' '.join(rearranged_tokens)
    print(rearranged_sentence)
   
    return rearranged_sentence
