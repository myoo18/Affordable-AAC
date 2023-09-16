import spacy

nlp = spacy.load("en_core_web_sm")

def rearrange_sentence(sentence):
    doc = nlp(sentence)
    
    #Get POS and tokenize
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    others = [token.text for token in doc if token.pos_ not in ["PRON", "VERB"]]

    #Simple rearrangement
    rearranged_tokens = pronouns + verbs + others
    
    #Make back to string
    rearranged_sentence = ' '.join(rearranged_tokens)
   
    
    return rearranged_sentence

