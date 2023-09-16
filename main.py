import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def fill_in_the_blanks(text, model, tokenizer):
    # Encode the input text and convert it to tensor
    indexed_tokens = tokenizer.encode(text, return_tensors='pt')
    
    # Generate a prediction
    with torch.no_grad():
        outputs = model.generate(indexed_tokens, max_length=50, num_return_sequences=1, temperature=1.0)
    
    # Decode the generated text back to a readable string
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_output

# Load pre-trained model and tokenizer
model_name = "gpt2-medium"  # You can also use "gpt2", "gpt2-large", or "gpt2-xl" depending on your needs and available resources
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Your example
input_text = "me want bike"
indexed_tokens = tokenizer.encode(input_text, return_tensors='pt')
attention_mask = torch.ones_like(indexed_tokens)
with torch.no_grad():
    outputs = model.generate(indexed_tokens, attention_mask=attention_mask, max_length=50, num_return_sequences=1, temperature=1.0)
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded_output)
