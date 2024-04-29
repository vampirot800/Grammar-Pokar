# Ramiro Flores Villarreal
# A01710879
# 29 / 04 / 2024
# Implementation of Computational methods Project: Pokar Grammar


# Imported libraries
import nltk
from nltk import CFG
nltk.download('punkt')

# Context-free grammar defined
grammar = CFG.fromstring("""
sentence -> play 'of' combo hand
play -> 'bets' | 'folds' | 'calls' | 'raises' | 'checks' | 'all in'
combo -> highCard | pair | twoPairs | threeOfKind | straight | flush | fullHouse | pokar | straightFlush | royalFlush
highCard -> 'High Card of:' rank
pair -> 'Pair of:' card 'and' card
twoPairs -> 'Two Pairs of:' rank 'and' rank
threeOfKind -> 'Three of a kind of:' rank
straight -> 'Straight of:' rank rank rank rank rank
flush -> 'Flush of:' suit
fullHouse -> 'Full House of:' pair 'and' threeOfKind
pokar -> 'Four of a kind of:' rank
straightFlush -> 'Straight Flush of:' rank rank rank rank card
royalFlush -> 'Royal Flush of A K Q J 10' suit
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

