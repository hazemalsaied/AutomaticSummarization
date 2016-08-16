In these experiments , there were no decision trees that used all of the digram features identify ed by the ? altering step , and for many words the decision tree learner went on to eliminate most of the candidate features . 
There is no search of the feature space performed to build a representative model as is the case with decision trees . 
A decision stump is a one node decision tree ( Holte , 1993 ) that is created by stopping the decision tree learner after the single most informative feature is added to the tree . 
Rather than attempting to provide computer programs with real { world knowledge comparable to that of humans , natural language processing has turned to corpus { based methods . 
Each sense { tagged occurrence of an ambiguous word is converted into a feature vector , where each feature represents some property of the surrounding text that is considered to be relevant to the disambiguation process . 
Word sense disambiguation is the process of selecting the most appropriate meaning for a word , based on the context in which it occurs . 
These typically include the part { of { speech of surrounding words , the presence of certain key words within some window of context , and various syntactic properties of the sentence and the ambiguous word . 
Then the decision tree learning algorithm is described , as are some benchmark learning algorithms that are included for purposes of comparison . 
The following process is repeated for each task . 
A preliminary version of this paper appears in ( Pedersen , 2001 ) . 