However , a small probability for jumping to a node that is lexically similar to the given sentence ( rather than the question itself is needed . 
Using Random Walks for Question-focused Sentence Retrieval
In ( Erkan and Radev , 2004 ) , we introduce method and successfully applied it generic multi-document summarization . 
To evaluate our sentence retrieval mechanism , reproduced extract files , which contain a list of sentences deemed to be relevant to the question , for the system and from human judgment . 
3.1 The LexRank method . 
In the new approach , the 916 score of a sentence is determined by a mixture model of the relevance of the sentence to the query and the similarity of the sentence to other high-scoring sentences . 
Our model is similar in spirit to the random- walk summarization model ( Otterbacher et al. , 2005 ) . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
As previously mentioned , the original LexRank method performed welling the context of generic summarization . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
In the training phase the experiment , we evaluated all combination with d in the range of [ 0 , 1 ] ( in increments of 0.10 ) and with a similarity threshold ranging from [ 0 , 0.9 ] ( in increments of 0.05 ) . 
3.4 Experiments with topic-sensitive LexRank . 