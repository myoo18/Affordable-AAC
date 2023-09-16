import torch
from transformers import BertTokenizer, BertForMaskedLM

# Load pre-trained model and tokenizer
model_name = "bert-base-uncased"
model = BertForMaskedLM.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)
model.eval()

def generate_text(input_text):
    # For the sake of demonstration, we'll assume that the second word needs correction
    # In practice, a more sophisticated approach would be needed to determine which words to mask
    tokenized_text = tokenizer.tokenize(input_text)
    if len(tokenized_text) > 1:
        tokenized_text[1] = '[MASK]'
    
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    tokens_tensor = torch.tensor([indexed_tokens])

    with torch.no_grad():
        outputs = model(tokens_tensor)
        predictions = outputs[0]

    # Replace the mask token with the predicted token
    if '[MASK]' in tokenized_text:
        predicted_index = torch.argmax(predictions[0, tokenized_text.index('[MASK]')]).item()
        predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
        tokenized_text[tokenized_text.index('[MASK]')] = predicted_token

    return ' '.join(tokenized_text).replace(' ##', '')

# Test
sentence = "me want bike"
print(generate_text(sentence))
