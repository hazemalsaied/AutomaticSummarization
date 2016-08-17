In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
To model the context necessary to correct the error , two extra states are used , as shown in Figure 1 . 
In the 21 category model reported in Kupiec ( 1989 ) only 129 equivalence classes were required to cover a 30,000 word dictionary . 
Methods have ranged from locally-operating rules ( Greene and Rubin , 1971 ) , to statistical methods ( Church , 1989 ; DeRose , 1988 ; Garside , Leech and Sampson , 1987 ; Jelinek , 1985 ) and back-propagation ( Benello , Mackie and Anderson , 1989 ; Nakamura and Shikano , 1989 ) . 
To model such dependency across the phrase , the networks shown in Figure 2 can be used . 
This leaves 50 % of the corpus for training all the other equivalence classes . 
The lexical context available for modeling a word 's category is solely the category of the preceding word ( expressed via the transition probabilities P ( Ci [ Ci1 ) . 
In this situation , the Baum-Welch algorithm ( Baum , 1972 ) can be used to estimate the model parameters . 
It minimizes the resources required for high performance automatic tagging . 
A 30,000 word dictionary was used , supplemented by inflectional analysis for words not found directly in the dictionary . 
It would be appropriate to deal with idioms separately , as done by Gaxside , Leech and Sampson ( 1987 ) . 