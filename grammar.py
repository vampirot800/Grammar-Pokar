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
test -> play preposition combo
play -> 'bets' | 'folds' | 'raises' | 'calls' |'checks'| 'goes' 'all' 'in'
combo -> royalFlush | straightFlush | fullHouse | pokar | straight | flush | threeOfKind | twoPairs | pair | highCard
royalFlush -> 'royal' 'flush' 'AKQJ10' preposition suit
straightFlush -> 'straight' 'flush' preposition rank rank rank rank card
fullHouse -> 'full' 'house' preposition pair preposition threeOfKind
pokar -> 'poker' preposition rank
straight -> 'straight' preposition rank rank rank rank rank
flush -> 'flush' preposition suit
threeOfKind -> 'three' preposition rank
twoPairs -> 'two' 'pairs' preposition rank 'and' rank
pair -> 'pair' preposition rank
highCard -> 'high' 'card' preposition card
hand -> card card
card -> rank preposition suit
preposition -> 'of' | 'with' | 'on' 
rank -> '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | 'J' | 'Q' | 'K' | 'A'
suit -> 'hearts' | 'diamonds' | 'clubs' | 'spades'
""")

# Parser with defined grammar
parser = nltk.ChartParser(grammar)

# List of test sentences to be parsed
sentences = [
    #Correctly parsed Sentences
    "bets on full house of pair of 5 with three of 6",
    "raises with royal flush AKQJ10 of spades",
    "folds with high card of K of clubs",
    "calls on straight of 3 4 5 6 7",
    "checks with poker of K",
    "goes all in with straight flush of 7 8 9 J Q of diamonds"

    #Unsuccesful cases, not following grammar rules (Uncomment lines for testing)
    #"Bets on straight flush of 2 of spades and high card of Q"
    #"Raises with two pairs of 8 and 9 and goes all in"
    #"Folds with royal flush of diamonds"
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


# Ambiguity check
# tokens = nltk.word_tokenize("bets on full house of pair of 5 and three of 6")

# Generate all parse trees for the sentence
# parse_trees = list(parser.parse(tokens))

# Check if there is more than one parse tree
# if len(parse_trees) > 1:
#     print("Ambiguity detected! Multiple parse trees found.")
# else:
#     print("No ambiguity detected. Single parse tree found.")
