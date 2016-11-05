They attempted to improve named entity translation by combining phonetic and semantic information . 
In our translation problem , C ( c ) is viewed as the query and C ( e ) is viewed as a document . 
In this paper , we propose a new approach for the task of mining new word translations from comparable corpora , by combining both context and transliteration information . 
If a word e in English is indeed the translation of a word c in Chinese , then we would expect e to be ranked very high in both lists in general . 
The work of ( Fung and Yee , 1998 ; Rapp , 1995 ; Rapp , 1999 ) noted that if an English word e is the translation of a Chinese word c , then the contexts of the two words are similar . 
Their contextual semantic similarity model is different from our language modeling approach to measuring context similarity . 
In this approach , a language model is derived from each document D . Then the probability of generating the query the machine transliteration method proposed by Q according to that language model , P ( Q | D ) , ( Knight and Graehl , 1998 ) . 
elected as follows : For each occurrence of c , we set a window of size 50 characters centered at c. We discarded all the Chinese words in the context that were not in the dictionary we used . 
On the other hand , using our method of combining both sources of information and setting M = â , 19 Chinese words ( i.e. , the first 22 Chinese words in Table 3 except å·´ä½äº å©å æ®å©æ³ have their correct English translations at rank one position . 
Being more readily available , comparable corpora are thus more suitable than parallel corpora for the task of acquiring new word translations , although relatively less research has been done in the past on comparable corpora . 
While we have only tested our method on Chinese-English comparable corpora , our method is general and applicable to other language pairs . 
For a Chinese source word occurring within a half- month period p , we looked for its English translation candidate words occurring in news documents in the same period p. 5.3 Translation candidates . 
We translated Chinese words into English . 
our task is to compute P ( C ( c ) | C ( e ) ) for each In a typical information retrieval ( IR ) problem , a query is given and a ranked list of documents English word e and find the e that gives the highest P ( C ( c ) | C ( e ) ) , estimated as : most relevant to the query is returned from a document collection . 
In this paper , we proposed a new method to mine new word translations from comparable corpora , by combining context and transliteration information , which are complementary sources of information . 
The results when we set M = 10 are shown in Table 1 . 
Previous research efforts on acquiring translations from comparable corpora include ( Fung and Yee , 1998 ; Rapp , 1995 ; Rapp , 1999 ) . 
Comparable corpora refer to texts that are not direct translation but are about the same topic . 
That is , Chinese is the source language and English is the target language . 
We use a variant of Within IR , there is a new approach to documents retrieval called the languages modeling approach ( Ponte & Croft , 98 ) . 