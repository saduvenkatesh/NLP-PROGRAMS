import spacy
# load spacy model
NLP = spacy.load('en_core_web_sm')
# load data
sentence = "I love coding"
doc = NLP(sentence)
# print entities
for ent in doc.ents:
 print(ent.text, ent.start_char, ent.end_char, ent.label_)

