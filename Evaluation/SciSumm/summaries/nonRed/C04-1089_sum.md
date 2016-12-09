This research is partially supported by a research grant R252000-125112 from National University of Singapore Academic Research Fund . 
We thank Jia Li for implementing the EM algorithm to train transliteration probabilities . 
If M = 10 , 15 Chinese words ( i.e. , the first 19 Chinese words in Table 3 except å¶çæ¯ å·´ä½äº å©å æ®å©æ³ have their correct English translations at rank one position . 
Knight and Graehl ( 1998 ) proposed a probabilistic model for machine transliteration . 
In our translation problem , C ( c ) is viewed as the query and C ( e ) is viewed as a document . 
In this paper , we proposed a new method to mine new word translations from comparable corpora , by combining context and transliteration information , which are complementary sources of information . 
This pronunciation is converted to source language pronunciation and then to source language word that our method estimates stead of P ( c | e ) and P ( e ) . 
We evaluated our approach on six months of Chinese and English Gigaword corpora , with encouraging results . 
Being more readily available , comparable corpora are thus more suitable than parallel corpora for the task of acquiring new word translations , although relatively less research has been done in the past on comparable corpora . 
q ( tc ) is the number ( i.e . , the surrounding Word ) of a Chinese Word c . Each C ( e ) , the context of an English Word of occurrence es of tc in C ( c ) . Tc ( C ( e ) ) is the bag of Chinese Word obtained by translating the First , each Chinese character in 