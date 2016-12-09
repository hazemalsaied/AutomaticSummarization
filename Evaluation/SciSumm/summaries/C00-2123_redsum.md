Pr ( eI 1 ) is the language model of the target language , whereas Pr ( fJ 1 jeI1 ) is the translation model . 
An inverted alignment is defined as follows : inverted alignment : i ! j = bi : Target positions i are mapped to source positions bi . 
The goal of machine translation is the translation of a text given in some source language into a target language . 
The model is often further restricted so that each source word is assigned to exactly one target word ( Brown et al. , 1993 ; Ney et al. , 2000 ) . 
The translation of one position in the source sentence may be postponed for up to L = 3 source positions , and the translation of up to two source positions may be anticipated for at most R = 10 source positions . 
For the translation model Pr ( fJ 1 jeI 1 ) , we go on the assumption that each source word is aligned to exactly one target word . 
The alignment model uses two kinds of parameters : alignment probabilities p ( aj jajô1 I ; J ) , where the probability of alignment aj for position j depends on the previous alignment position ajô1 Ney et al. , 2000 ) and lexicon probabilities p ( fj jean . 
e0 ; e are the last two target Word , 