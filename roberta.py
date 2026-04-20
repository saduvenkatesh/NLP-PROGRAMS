from transformers import RobertaTokenizer, RobertaForSequenceClassification

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('roberta-base')

text = "AI is the future"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

outputs = model(**inputs)
print(outputs.logits)