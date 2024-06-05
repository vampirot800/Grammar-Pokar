# Grammar-Pokar
Implementation of Computational Methods Project

Pokar Syntaxis Grammar

## Description
This grammar directly mirrors the syntax used in playing poker, providing a structured representation of the game's elements. It defines the values of individual cards, the various combinations that players can achieve, and the composition of hands. By capturing the specific language used in poker gameplay, the grammar facilitates the understanding and parsing of poker-related sentences.  

The grammar presented can be classified as a Context-Free Grammar (CFG) within the Chomsky Hierarchy Extended Level. Context-Free Grammars are characterized by rules that define how symbols (both terminals and non-terminals) can be combined to form strings. In this grammar, the rules define the syntactic structure of poker-related sentences, including plays, combinations, hands, and individual cards.

The **modeling technique** I decided to use was parsing tree diagrams for test cases 

## Model of the Solution


## Implementation


## Tests


## Analysis

The **complexity** of my model is in 

I used the regex library from Python which internally according to the API documentation uses the algorithms from Unix to better parse... etc ... this means that my time complexity in general remains as O(n) 

My first approach to the **solution** was to use an automaton in prolog which is also a natural solution however following the recommendations I found in  (sun et al, 2054)  I preferred the Regular Expression because it is faster in the context of ... etc ... havinf an overall time of  O(log n)


