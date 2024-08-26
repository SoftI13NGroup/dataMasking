from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline
from faker import Faker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialization for model and Faker
tokenizer = BertTokenizer.from_pretrained('dslim/bert-base-NER')
model = BertForTokenClassification.from_pretrained('dslim/bert-base-NER')
ner = pipeline('ner', model=model, tokenizer=tokenizer)
faker = Faker()

# Function for masking data
def mask_sensitive_data(text):
    entities = ner(text)
    for entity in entities:
        is_begin, entity_type = entity["entity"].split("-")
        print("_______")
        print(entity["word"])
        print(entity["entity"])
        if entity_type in ['PER', 'ORG', 'LOC']:  # Например, замена имен, организаций, локаций
            fake_data = faker.first_name() if entity_type == 'PER' and is_begin == "B" else faker.last_name() if entity_type == "PER" else faker.company() if entity_type == 'ORG'and is_begin == "B" else entity["word"] if entity_type == "ORG" else faker.city()
            highlighted_word = f"<span style='color:red;'>{fake_data}</span>"
            text = text.replace(entity['word'], highlighted_word)
    return text

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    masked_message = mask_sensitive_data(user_message)
    return jsonify({'response': masked_message})

if __name__ == '__main__':
    app.run(debug=True)

