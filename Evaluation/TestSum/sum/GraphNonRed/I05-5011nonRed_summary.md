In this paper , we will propose an unsupervised method to discover paraphrases from a large untagged corpus . 
We proposed an unsupervised method to discover paraphrases from a large untagged corpus . 
There has also been work using a bootstrap- ping approach [ Brin 98 ; Agichtein and Gravano 00 ; Ravichandran and Hovy 02 ] . 
Automatic Paraphrase Discovery based on Context and Keywords between NE Pairs
After tagging a large corpus with an automatic NE tagger , the method tries to find sets of paraphrases automatically without being given a seed phrase or any kind of cue . 
After tagging a large corpus with an automatic NE tagger , the method tries to find sets of paraphrases automatically without being given a seed phrase or any kinds of cue . 
We are focusing on phrases which have two Named Entities ( NEs ) , as those types of phrases are very important for IE applications . 
Next , for each pair of NE categories , we collect all the contexts and find the keywords which are topical for that NE category pair . 
The NE tagger is a rule-based system with 140 NE categories [ Sekine et al . 2004 ] . 
Extract NE instance pairs with contexts First , we extract NE pair instances with their context from the corpus . 
One of such approaches uses comparable documents , which are sets of documents whose content are foundation to be almost the same , such as different newspaper stories about the same event [ Shinyama and Sekine 03 ] or different translations of the same story [ Barzilay 01 ] . 
Also , expanding on the techniques for the automatic generation of extraction patterns ( Riloff 96 ; Sudo 03 ) using our method , the extraction patterns which have the same meaning can be automatically linked , enabling us to produce the final table fully automatically . 
Overview of the method 2.2 Step by Step Algorithm . 
Recently , this topic has been getting more attention , as is evident from the Paraphrase Workshops in 2003 and 2004 , driven by the needs of various NLP applications . 
It is not easy to make a clear definition of paraphrase . 
buy - acquire ( 5 ) buy - agree ( 2 ) buy - purchase ( 5 ) buy - acquisition ( 7 ) buy - pay ( 2 ) * buy - buyout ( 3 ) buy - bid ( 2 ) acquire - purchase ( 2 ) acquire - acquisition ( 2 ) acquire - pay ( 2 ) * purchase - acquisition ( 4 ) purchase - stake ( 2 ) * acquisition - stake ( 2 ) * unit - subsidiary ( 2 ) unit - parent ( 5 ) It is clear that these links form two clusters which are mostly correct . 
Another approach to finding paraphrases is to find phrases which take similar subjects and objects in large corpora by using mutual information of word distribution [ Lin and Pantel 01 ] . 
In order to create an IE system for a new domain , one has to spend a long time to create the knowledge . 
Rather we believe several methods have to be developed using different heuristics to discover wider variety of paraphrases . 
There have been other kinds of efforts to discover paraphrase automatically from corpora . 
We realize the importance of paraphrase ; however , the major obstacle is the construction of paraphrase knowledge . 
We would like to thank Prof. Ralph Grish- man , Mr. Takaaki Hasegawa and Mr. Yusuke Shinyama for useful comments , discussion and evaluation . 
They contain about 200M words ( 25M , 110M , 40M and 19M words , respectively ) . 
In this section , we will explain the algorithm step by step with examples . 
As we shall see , most of the linked sets are paraphrases . 
We are focusing on phrase which have two Named Entities ( NEs ) , as those types of phrase are very important for IE applications . 