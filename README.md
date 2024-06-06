# Grammar-Pokar
Implementation of Computational Methods Project

Pokar Syntaxis Grammar

## Description
This grammar directly mirrors the syntax used in playing poker, providing a structured representation of the game's elements. It defines the values of individual cards, the various combinations that players can achieve, and the composition of hands. By capturing the specific language used in poker gameplay, the grammar facilitates the understanding and parsing of poker-related sentences.  

The **modeling technique** I decided to use was parsing tree diagrams for test cases 

## Model of the Solution

The grammar recognizes the language syntaxis for playing poker.

In earlier versions of my grammar, I faced an issue with left recursion. During parsing, certain instances occurred where a non-terminal inadvertently produced itself as the leftmost symbol. To address this, I introduced a new non-terminal preposition, which includes the options 'of', 'with', and 'on'. This addition effectively resolved the left recursion problem and improved the efficiency of the grammar parsing process.

I also used a function to check for ambiguity in my grammar, the function generates all parse trees for the sentence, and in case of more than one parse tree, the output would be: "Ambiguity detected! Multiple parse trees found." 

(The ambiguity check function is commented below the code)

Grammar:
```
sentence -> play preposition combo
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
```

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
```
Sentence: bets on full house of pair of 5 with three of 6
                                        sentence                                                    
  _________________________________________|__________                                               
 |        |                                         combo                                           
 |        |                                           |                                              
 |        |                                       fullHouse                                         
 |        |        ___________________________________|__________________________________            
 |        |       |     |        |                   pair              |            threeOfKind     
 |        |       |     |        |          __________|_______         |         ________|_______    
play preposition  |     |   preposition    |     preposition rank preposition   |   preposition rank
 |        |       |     |        |         |          |       |        |        |        |       |   
bets      on     full house      of       pair        of      5       with    three      of      6  



Sentence: raises with royal flush AKQJ10 of spades
                         sentence                              
   _________________________|_________                          
  |         |                       combo                      
  |         |                         |                         
  |         |                     royalFlush                   
  |         |         ________________|____________________     
 play  preposition   |      |         |      preposition  suit 
  |         |        |      |         |           |        |    
raises     with    royal  flush     AKQJ10        of     spades



Sentence: folds with high card of K of clubs
                       sentence                                   
   _______________________|__________                              
  |        |                       combo                          
  |        |                         |                             
  |        |                      highCard                        
  |        |        _________________|________________             
  |        |       |      |          |               card         
  |        |       |      |          |        ________|________    
 play preposition  |      |     preposition rank preposition  suit
  |        |       |      |          |       |        |        |   
folds     with    high   card        of      K        of     clubs



Sentence: calls on straight of 3 4 5 6 7
                                       sentence                        
   _______________________________________|________                     
  |        |                                     combo                 
  |        |                                       |                    
  |        |                                    straight               
  |        |          _____________________________|________________    
 play preposition    |     preposition   rank     rank   rank rank rank
  |        |         |          |         |        |      |    |    |   
calls      on     straight      of        3        4      5    6    7  



Sentence: checks with poker of K
                   sentence                 
   ___________________|__________            
  |         |                  combo        
  |         |                    |           
  |         |                  pokar        
  |         |          __________|_______    
 play  preposition    |     preposition rank
  |         |         |          |       |   
checks     with     poker        of      K  



Sentence: goes all in with straight flush of 7 8 9 J Q of diamonds
                                           sentence                                                        
       _______________________________________|_________________                                            
      |            |                                          combo                                        
      |            |                                            |                                           
      |            |                                      straightFlush                                    
      |            |          __________________________________|___________________________                
      |            |         |       |        |       |         |        |    |            card            
      |            |         |       |        |       |         |        |    |     ________|_________      
     play     preposition    |       |   preposition rank      rank     rank rank rank preposition   suit  
  ____|____        |         |       |        |       |         |        |    |    |        |         |     
goes all   in     with    straight flush      of      7         8        9    J    Q        of     diamonds
```
## Analysis

While researching, I found time complexity for a chart parser in general can have a worst time complexity of: O(n^3*m), where n is the length of the input sentence and m is the number of grammar rules. 

The grammar is not ambigous as checked with the function below the code (only single parse trees are found when testing sentences), and i analyzed the time it took to parse which was : 0.0019066333770751953 seconds which indicates the parsing is efficient in my sentences.

The grammar presented can be classified as a Context-Free Grammar (CFG) within the Chomsky Hierarchy Extended Level. Context-Free Grammars are characterized by rules that define how symbols (both terminals and non-terminals) can be combined to form strings. These grammars generate languages that can be parsed using algorithms like the CYK algorithm and can be recognized by pushdown automata. In this grammar, the rules define the syntactic structure of poker-related sentences, including plays, combinations, hands, and individual cards.

Context-Free Grammars allow for the creation of recursive and nested structures, enabling the representation of complex constructs such as poker hands and sequences of plays. The grammar rules specify the possible sequences of actions (like betting, folding, or raising) and the various possible poker hand combinations (such as royal flush, straight flush, or full house).


## References:
Brian & Kristy Roark & Hollingshead. (n.d.). Linear complexity context-free parsing pipelines via chart ... https://aclanthology.org/N09-1073.pdf 