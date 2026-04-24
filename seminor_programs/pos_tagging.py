import spacy

nlp = spacy.load('en_core_web_sm')

text = 'I love coding'

doc = nlp(text)

for token in doc:
    
    print(token.text, token.pos_, token.tag_)