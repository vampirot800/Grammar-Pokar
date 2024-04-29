# Ramiro Flores Villarreal
# A01710879
# 29 / 04 / 2024
# Implementation of Computational methods Project: Pokar Grammar


# Imported libraries
import nltk
from nltk import CFG
nltk.download('punkt')

# Context-free grammar defined
grammar = CFG.fromstring
("""
combo -> 'pair' | 'twoPair' | 'threeOfKind' | 'straight' | 'flush' | 'fullHouse' | 'pokar' | 'straightFlush' | 'RoyalFlush'
hand -> card card
card -> rank suit
rank -> '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | 'J' | 'Q' | 'K' | 'A'
suit -> 'hearts' | 'diamonds' | 'clubs' | 'spades' 
""")

# Parser with defined grammar
parser = nltk.ChartParser(grammar)

# Test sentence to be parsed
sentence = ""

# Tokenize sentence
tokens = nltk.word_tokenize(sentence)

# Parse sentence
for tree in parser.parse(tokens):
    tree.pretty_print()

