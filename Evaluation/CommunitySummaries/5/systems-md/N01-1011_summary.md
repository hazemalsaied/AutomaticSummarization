The characteristics of the decision trees and decision stumps learned for each word are shown in Table 2 . 
Learning continues until all the training examples are accounted for by the decision tree . 
One of our original hypotheses was that accurate decision trees of bi grams will include a relatively small number of features . 
A Decision Tree of Bigrams is an Accurate Predictor of Word Sense
Word sense disambiguation is the process of selecting the most appropriate meaning for a word , based on the context in which it occurs . 
Bi grams have been used as features for word sense disambiguation , particularly in the form of collocations where the ambiguous word is one component of the digram e.g. , ( Bruce and Wiebe , 1994 ) , ( Ng and Lee , 1996 ) , ( Yarowsky , 1995 ) ) . 
These typically include the part { of { speech of surrounding words , the presence of certain key words within some window of context , and various syntactic properties of the sentence and the ambiguous word . 
Finally , note that the smallest decision trees are functionally equivalent to our benchmark methods . 
This paper presents a corpus-based approach to word sense disambiguation where a decision tree assigns a sense to an ambiguous word based on the bigrams that occur nearby.
For our purposes it is assumed that the set of possible meaning , i.e . , the Sense inventory , has already been determined . 