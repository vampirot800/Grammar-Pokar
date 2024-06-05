# Grammar-Pokar
Implementation of Computational Methods Project

Pokar Syntaxis Grammar

## Description
This grammar directly mirrors the syntax used in playing poker, providing a structured representation of the game's elements. It defines the values of individual cards, the various combinations that players can achieve, and the composition of hands. By capturing the specific language used in poker gameplay, the grammar facilitates the understanding and parsing of poker-related sentences.  

The **modeling technique** I decided to use was parsing tree diagrams for test cases 

## Model of the Solution

The grammar recognizes the language syntaxis for playing poker.

In earlier versions of my grammar, I faced an issue with left recursion. During parsing, certain instances occurred where a non-terminal inadvertently produced itself as the leftmost symbol. To address this, I introduced a new non-terminal preposition, which includes the options 'of', 'with', and 'on'. This addition effectively resolved the left recursion problem and improved the efficiency of the grammar parsing process.

I also used a function to check for ambiguity in my grammar, the function generates all parse trees for the sentence, and in case of more than one parse tree, thw output would be: "Ambiguity detected! Multiple parse trees found." 

(The ambiguity check function is commented below the code)

## Implementation
I implemented a tester for this grammar using the python library nltk, using functions for parsing and displaying the trees of the succesful test cases (tree pretty print) 

## Tests    
I provided 5 test sentences in the code that should be parsed correctly and shown:
    "bets on full house of pair of 5 with three of 6",
    "raises with royal flush AKQJ10 of spades",
    "folds with high card of K of clubs",
    "calls on straight of 3 4 5 6 7",
    "checks with four of a kind of K",
    "goes all in with straight flush of 7 8 9 J Q of diamonds"

I also provided 3 sentences that should NOT be approved or parsed and provide an error output:
    "Bets on straight flush of 2 of spades and high card of Q"
    "Raises with two pairs of 8 and 9 and goes all in"
    "Folds with royal flush of diamonds"

## Analysis

The grammar presented can be classified as a Context-Free Grammar (CFG) within the Chomsky Hierarchy Extended Level. Context-Free Grammars are characterized by rules that define how symbols (both terminals and non-terminals) can be combined to form strings. In this grammar, the rules define the syntactic structure of poker-related sentences, including plays, combinations, hands, and individual cards.


