This approach is similar in spirit to the iterative computational approaches of the Hidden Markov Models ( Kupiec , 1989 
The basic network can not model the dependency of the number of the verb on its subject , which precedes it by a prepositional phrase . 
This has the disadvantage that they can not share training data . 
The former represents 95.6 % correct word tagging on the text as a whole ( ignoring unknown words ) , and 89 % on the ambiguous words . 
As in the previous section , the corrections are not programmed into the model . 
To model such dependency across the phrase , the networks shown in Figure 2 can be used . 
A total of 1,526 words had ambiguous categories ( i.e . 40 % of the document ) . 
A 30,000 word dictionary was used , supplemented by inflectional analysis for words not found directly in the dictionary . 
State chains are used to model selective higher-order conditioning in the model , which obviates the proliferation of parameters attendant in uniformly higher-order models . 
Examples show how word dependency across phrases can be modeled . 
In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
Methods have ranged from locally-operating rules ( Greene and Rubin , 1971 ) , to statistical methods ( Church , 1989 ; DeRose , 1988 ; Garside , Leech and Sampson , 1987 ; Jelinek , 1985 ) and back-propagation ( Benello , Mackie and Anderson , 1989 ; Nakamura and Shikano , 1989 ) . 