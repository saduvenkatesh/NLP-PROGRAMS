from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

text = "I love AI"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

outputs = model(**inputs)
logits = outputs.logits

print(logits)