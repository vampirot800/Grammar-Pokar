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
test -> play combo
play -> 'bets' 'on' | 'folds' 'with' | 'raises' 'with'| 'checks' 'with' | 'goes' 'all' 'in'
combo -> royalFlush | straightFlush | fullHouse | pokar | straight | flush | threeOfKind | twoPairs | pair | highCard
royalFlush -> 'royal' 'flush' 'AKQJ10' 'of' suit
straightFlush -> 'straight' 'flush' 'of' rank rank rank rank card
fullHouse -> 'full' 'house' 'of' pair threeOfKind
pokar -> 'four' 'of' 'a' 'kind' 'of' rank
straight -> 'straight' 'of' rank rank rank rank rank
flush -> 'flush' 'of' suit
threeOfKind -> 'three' 'of' rank
twoPairs -> 'two' 'pairs' 'of' rank 'and' rank
pair -> 'pair' 'of' rank
highCard -> 'high' 'card' 'of' rank
hand -> card card
card -> rank 'of' suit
rank -> '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | 'J' | 'Q' | 'K' | 'A'
suit -> 'hearts' | 'diamonds' | 'clubs' | 'spades'
""")

# Parser with defined grammar
parser = nltk.ChartParser(grammar)

# List of test sentences to be parsed
sentences = [
    "bets on full house of pair of 5 three of 6",
    "raises with royal flush AKQJ10 of spades",
    "folds with high card of K"
]

# Function to parse and display the parse trees
def parse_sentences(sentences):
    for sentence in sentences:
        print(f"Sentence: {sentence}")
        tokens = nltk.word_tokenize(sentence)
        for tree in parser.parse(tokens):
            tree.pretty_print()
        print("\n")

# Parse the list of sentences
parse_sentences(sentences)

