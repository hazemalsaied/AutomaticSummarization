The implementation of the hidden Markov model is based on that of Rabiner , Levinson and Sondhi ( 1983 ) . 
The basic network can not model the dependency of the number of the verb on its subject , which precedes it by a prepositional phrase . 
The `` augmented network '' uniquely models all second-order dependencies of the type determiner -noun - X , and determiner -adjective -X ( X ranges over { cl ... cn } ) . 
This has the disadvantage that they can not share training data . 
Only context has been supplied to aid the training procedure , and the latter is responsible for deciding which alternative is more likely , based on the training data . 
The training corpus was a collection of electronic mail messages concerning the design of the Common-Lisp programming language -a somewhat less than ideal representation of English . 
This work was sponsored in part by the Defense Advanced Research Projects Agency ( DOD ) , under the Information Science and Technology Office , contract # N0014086-C-8996 . 
95 To complete the description of the augmented model it is necessary to mention tying of the model states ( Jelinek and Mercer , 1980 ) . 
To model such dependency across the phrase , the networks shown in Figure 2 can be used . 
It can be trained reliably on moderate amounts of training text , and through the use of selectively augmented networks it can model high-order dependencies without requiring an excessive number of parameters . 
In the 21 category model reported in Kupiec ( 1989 ) only 129 equivalence classes were required to cover a 30,000 word dictionary . 
Many Lisp-specific words were not in the vocabulary , and thus tagged as unknown , however the lisp category was nevertheless created for frequently occurring Lisp symbols in an attempt to reduce bias in the estimation . 
In a ranked list of words in the corpus the most frequent 100 words account for approximately 50 % of the total tokens in the corpus , and thus data is available to estimate them reliably . 
The most frequent 100 words of the corpus were assigned individually in the model , thereby enabling them to have different distributions over their categories . 
The basic model tagged these sentences correctly , except for- `` range '' and `` rises '' which were tagged as noun and plural-noun respectively 1 . 
SINGULAR ALL STATES IN BASIC NETWORK NOT SHOWN Figure 2 : Augmented Networks for Example of Subject/Verb Agreement For example , consider the word `` up '' in the following sentences : `` He ran up a big bill '' . 
In fact , the number of equivalence classes is essentially independent of the size of the dictionary , enabling new words to be added without any modification to the model . 
A 30,000 word dictionary was used , supplemented by inflectional analysis for words not found directly in the dictionary . 
The performance of a tagging program depends on the choice and number of categories used , and the correct tag assignment for words is not always obvious . 
A stochastic methods for assigning part-of-speech categories to unrestricted English text has been described . 