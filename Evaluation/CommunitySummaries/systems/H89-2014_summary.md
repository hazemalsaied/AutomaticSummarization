This approach is similar in spirit to the iterative computational approaches of the Hidden Markov Models ( Kupiec , 1989 
To model such dependency across the phrase , the networks shown in Figure 2 can be used . 
In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
The paper describes refinements that are currently being investigated in a model for part-of-speech assignment to words in unrestricted text.
The determination of part-of-speech categories for words is an important problem in language modeling , because both the syntactic and semantic roles of words depend on their part-of-speech category ( henceforth simply termed `` category '' ) . 
In the 21 category model reported in Kupiec ( 1989 ) only 129 equivalence classes were required to cover a 30,000 word dictionary . 
In fact , the number of equivalence classes is essentially independent of the size of the dictionary , enabling new words to be added without any modification to the model . 
The most frequent 100 words of the corpus were assigned individually in the model , thereby enabling them to have different distributions over their categories . 
The paper describes refinements that are currently being investigated in a model for part-of-speech assignment to words in unrestricted text . 
Examples show how word dependency across phrases can be modeled . 
Equivalence classes { Eqvl ... Eqvm } replace the words { wl ... Wv } ( m < < v ) and P ( Eqvi I Ci ) replace the parameters P ( Wi I Ci ) . 
Methods have ranged from locally-operating rules ( Greene and Rubin , 1971 ) , to statistical methods ( Church , 1989 ; DeRose , 1988 ; Garside , Leech and Sampson , 1987 ; Jelinek , 1985 ) and back-propagation ( Benello , Mackie and Anderson , 1989 ; Nakamura and Shikano , 1989 ) . 