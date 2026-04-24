import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

text="I love coding"

doc = nlp(text)

for token in doc:
    
    print(token.text, token.dep_, token.head.text)
    

displacy.serve(doc,style="dep")