The work described here also makes use of a hidden Markov model . 
In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
For an n category model this requires n 3 transition probabilities . 
In the 21 category model reported in Kupiec ( 1989 ) only 129 equivalence classes were required to cover a 30,000 word dictionary . 
To model such dependency across the phrase , the networks shown in Figure 2 can be used . 
The implementation of the hidden Markov model is based on that of Rabiner , Levinson and Sondhi ( 1983 ) . 
The most frequent 100 words of the corpus were assigned individually in the model , thereby enabling them to have different distributions over their categories . 
In this situation , the Baum-Welch algorithm ( Baum , 1972 ) can be used to estimate the model parameters . 
Several workers have addressed the problem of tagging text . 
However they are both members of the equivalence class noun-or-verb , and so are considered to behave identically . 
Methods have ranged from locally-operating rules ( Greene and Rubin , 1971 ) , to statistical methods ( Church , 1989 ; DeRose , 1988 ; Garside , Leech and Sampson , 1987 ; Jelinek , 1985 ) and back-propagation ( Benello , Mackie and Anderson , 1989 ; Nakamura and Shikano , 1989 ) . 