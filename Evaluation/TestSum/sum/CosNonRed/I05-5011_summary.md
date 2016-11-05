Recently , this topic has been getting more attention , as is evident from the Paraphrase Workshops in 2003 and 2004 , driven by the needs of various NLP applications . 
For example , we can easily imagine that the number of paraphrases for âA buys Bâ is enormous and it is not possible to create a comprehensive inventory by hand . 
Automatic Paraphrase Discovery based on Context and Keywords between NE Pairs
Up to now , most IE researchers have been creating paraphrase knowledge ( or IE patterns ) by hand and for specific tasks . 
After tagging a large corpus with an automatic NE tagger , the method tries to find sets of paraphrases automatically without being given a seed phrase or any kinds of cue . 
In this paper , we will propose an unsupervised method to discover paraphrases from a large untagged corpus . 
One of the difficulties in Natural Language Processing is the fact that there are many ways to express the same thing or event . 
As a later reï¬nement , Sekine ( 2005 ) makes a similar attempt at using distributional similarity over named entity pairs in order to produce a list of fully lexical phrasal paraphrases for specific concepts represented by keywords . 
If the expression is a word or a short phrase ( like corporation and accompany , it is called a synonym . 
We proposed an unsupervised method to discover paraphrases from a large untagged corpus . 
There has been a lot of research on such lexical relations , along with the creation of resources such as WordNet . 
However , those methods need initial seeds , so the relation between entities has to be known in advance . 
If the expression is longer or complicated ( like âA buys Bâ and âAâs purchase of Bâ ) , it is called paraphrase i.e . a set of phrases which express the same thing or event . 
We realize the importance of paraphrase ; however , the major obstacle is the construction of paraphrase knowledge . 
Also , we donate know how many such paraphrase sets are necessary to cover even some everyday things or events . 
For example , in Information Retrieval ( IR ) , we have to match a user query to the expressions in the desired documents , while in Question Answering ( QA ) , we have to find the answer to the user question even if the formulation of the answer in the document is different from the question . 
Also , in Information Extraction ( IE ) , in which the system tries to extract elements of some events ( e.g . date and company names of a corporate merger event ) , several event instances from different news articles have to be aligned even if these are expressed differently . 
So , there is a limitation that IE can only be performed for a predefined task , like discorporate or management . 
We agree with Sekine ( 2005 ) who claims that several different methods are required to discover a wider variety of paraphrases . 
In order to create an IE system for a new domain , one has to spend a long time to create the knowledge . 
So , it is too costly to make IE technology âopen- domain or âon-demandâ like IR or QA . 
We are focusing on phrases which have two Named Entities ( NEs ) , as those types of phrases are very important for IE applications . 
Here , the term frequency ( TF ) is the frequency of a word in the bag and the inverse term frequency ( ITF ) is the inverse of the log of the frequency in the entire corpus . 
Automatic paraphrase discovery is an important but challenging task . 
We propose an unsupervised method to discover paraphrases from a large untagged corpus , without requiring any seed phrase or other cue . 
For examples , in Figure 3 , we can see that the phrase in the âbuyâ acquire and purchase sets are mostly Paraphrase . 