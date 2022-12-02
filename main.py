## python -m textblob.download_corpora
from textblob.classifiers import NaiveBayesClassifier

with open('datos.json','r') as fl:
    cl = NaiveBayesClassifier(fl, format="json")
    
print(cl.classify("el bocata esta malisimo"))

