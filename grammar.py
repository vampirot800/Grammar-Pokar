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
sentence -> play 'of' combo hand

play -> 'bets' | 'folds' | 'calls' | 'raises' | 'checks' | 'allIn'

combo -> 'pair' 'of' card 'and' card | 'twoPairs' 'of' rank 'and' rank | 'threeOfKind'
 'of' rank | 'straight' 'of' rank rank rank rank card | 'flush' 'of' rank rank rank rank rank
| 'fullHouse' 'of' rank rank 'and' rank rank rank | 'pokar' 'of' rank | 
'straightFlush' 'of' rank rank rank rank card | 'RoyalFlush'

hand -> card card

card -> rank 'of' suit

rank -> '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | 'J' | 'Q' | 'K' | 'A'

suit -> 'hearts' | 'diamonds' | 'clubs' | 'spades'
""")

# Parser with defined grammar
parser = nltk.ChartParser(grammar)

# Test sentence to be parsed
sentence = "bets on fullHouse pair 5 of Spades threeOfKind Q of hearts"

# Tokenize sentence
tokens = nltk.word_tokenize(sentence)

# Parse sentence
for tree in parser.parse(tokens):
    tree.pretty_print()

