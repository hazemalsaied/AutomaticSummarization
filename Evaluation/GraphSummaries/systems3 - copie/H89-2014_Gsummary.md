The work described here also makes use of a hidden Markov model . 
The `` augmented network '' uniquely models all second-order dependencies of the type determiner -noun - X , and determiner -adjective -X ( X ranges over { cl ... cn } ) . 
This has the disadvantage that they can not share training data . 
The training corpus was a collection of electronic mail messages concerning the design of the Common-Lisp programming language -a somewhat less than ideal representation of English . 
Only context has been supplied to aid the training procedure , and the latter is responsible for deciding which alternative is more likely , based on the training data . 
The former represents 95.6 % correct word tagging on the text as a whole ( ignoring unknown words ) , and 89 % on the ambiguous words . 
As in the previous section , the corrections are not programmed into the model . 
To model such dependency across the phrase , the networks shown in Figure 2 can be used . 
The basic network can not model the dependency of the number of the verb on its subject , which precedes it by a prepositional phrase . 
Equivalence classes { Eqvl ... Eqvm } replace the words { wl ... Wv } ( m < < v ) and P ( Eqvi I Ci ) replace the parameters P ( Wi I Ci ) . 
This leaves 50 % of the corpus for training all the other equivalence classes . 
In a ranked list of words in the corpus the most frequent 100 words account for approximately 50 % of the total tokens in the corpus , and thus data is available to estimate them reliably . 
A 30,000 word dictionary was used , supplemented by inflectional analysis for words not found directly in the dictionary . 
The basic model tagged these sentences correctly , except for- `` range '' and `` rises '' which were tagged as noun and plural-noun respectively 1 . 
In practice , word context provides significant constraint , so the trade-off appears to be a remarkably favorable one . 
The replacement of the auxiliary category by the following categories greatly improved this : Category Name Words included in Category Be be Been been Being being Have have Have* has , have , had , having be* is , am , are , was , were do* do , does , did modal Modal auxiliaries Unique Equivalence Classes for Common Words Common words occur often enough to be estimated reliably . 
In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
Methods have ranged from locally-operating rules ( Greene and Rubin , 1971 ) , to statistical methods ( Church , 1989 ; DeRose , 1988 ; Garside , Leech and Sampson , 1987 ; Jelinek , 1985 ) and back-propagation ( Benello , Mackie and Anderson , 1989 ; Nakamura and Shikano , 1989 ) . 
It would be appropriate to deal with idioms separately , as done by Gaxside , Leech and Sampson ( 1987 ) . 