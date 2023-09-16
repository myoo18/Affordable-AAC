import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#load pre-trained model and tokenizer
model_name = "grammarly/coedit-large"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_text(input_text):
    indexed_tokens = tokenizer.encode(input_text, return_tensors='pt')
    
    with torch.no_grad():
        #adjust max_length as needed
        outputs = model.generate(indexed_tokens, max_length=100)

    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_output

