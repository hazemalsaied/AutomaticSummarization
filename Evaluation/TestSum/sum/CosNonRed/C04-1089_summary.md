# o is the total number of output English translations . 
The correctness of the English translations was manually checked . 
Being more readily available , comparable corpora are thus more suitable than parallel corpora for the task of acquiring new word translations , although relatively less research has been done in the past on comparable corpora . 
Much research has been done on using parallel corpora to learn bilingual lexicons ( Melamed , 1997 ; Moore , 2003 ) . 
For example , various news agencies report major world events in different languages , and such news documents form a readily available source of comparable corpora . 
On the other hand , the work of ( Cao and Li , 2002 ; Fung and Yee , 1998 ; Rapp , 1995 ; Rapp , 1999 ) used only the context of w to locate its translation in a second language . 
Similarly , AlOnaizan and Knight ( 2002a 2002b only made use of transliteration information alone and so was not directly comparable . 
Since we are using comparable corpora , it is possible that the translation of a new word does not exist in the target corpus . 
To investigate the effect of the two individual sources of information ( context and transliteration ) , we checked how many translations could be found using only one source of information ( i.e. , context alone or transliteration alone ) , on those Chinese words that have translations in the English part of the comparable corpus . 
Some recent research used comparable corpora to re-score name transliterations ( Sproat et al. , 2006 ; Klementiev and Roth , 2006 ) or mine new word translations ( Udupa et al. , 2009 ; Ji , 2009 ; Fung and Yee , 1998 ; Rapp , 1999 ; Shao and Ng , 2004 ; Hassan et al. , 2007 ) . 
Some recent research used comparable corpora to mine name translation pairs ( Feng et al. , 2004 ; Kutsumi et al. , 2004 ; Udupa et al. , 2009 ; Ji , 2009 ; Fung and Yee , 1998 ; Rapp , 1999 ; Shao and Ng , 2004 ; Lu and Zhao , 2006 ; Hassan et al. , 2007 ) . 
The English Gigaword corpus consists of news from four newswire services : Agence France Press English Service , Associated Press Worldstream English Service , New York Times Newswire Service , and Xinhua News Agency English Service . 
Chinese Giga- word corpus consists of news from two agencies : = ââ P ( l a a i | pi ) Xinhua News Agency and Central News Agency . 
Other similar research lines are the TACKBP Entity Linking ( EL ) ( Ji et al. , 2010 ; Ji et al. , 2011 ) , which links a named entity in news and web documents to an appropriate knowledge base ( KB ) entry , the task of mining name translation pairs from comparable corpora ( Udupa et al. , 2009 ; Ji , 2009 ; Fung and Yee , 1998 ; Rapp , 1999 ; Shao and Ng , 2004 ; Hassan et al. , 2007 ) and the link prediction problem ( Adamic and Adar , 2001 ; LibenNowell and Kleinberg , 2003 ; Sun et al. , 2011b ; Hasan et al. , 2006 ; Wang et al. , 2007 ; Sun et al. , 2011a ) . 
Their contextual semantic similarity model is different from our language modeling approach to measuring context similarity . 
â t c t ! t The candidate ei that is ranked the highest according to the average rank is taken to be the cor where t is a term in the corpus , ct is the number rec translation and is output . 
Previous research efforts on acquiring translations from comparable corpora include ( Fung and Yee , 1998 ; Rapp , 1995 ; Rapp , 1999 ) . 
The work of ( Fung and Yee , 1998 ; Rapp , 1995 ; Rapp , 1999 ) noted that if an English word e is the translation of a Chinese word c , then the contexts of the two words are similar . 
That is , Chinese is the source language and English is the target language . 
But it is not difficult to extend our methods to handle this problem . 