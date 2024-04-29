# Ramiro Flores Villarreal
# A01710879
# 29 / 04 / 2024
# Implementation of Computational methods Project: Pokar Grammar


# Imported libraries
import nltk
from nltk import CFG 
nltk.download('punkt')

###Library Functions
# Context-free grammar defined
grammar = CFG.fromstring(""" """)

# Parser with defined grammar
parser = nltk.ChartParser(grammar)

# Test sentence to be parsed
sentence = ""

# Tokenize sentence
tokens = nltk.word_tokenize(sentence)

# Parse sentence
for tree in parser.parse(tokens):
    tree.pretty_print()

