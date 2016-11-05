3.2 Relevance to the question . 
Using Random Walks for Question-focused Sentence Retrieval
In ( Erkan and Radev , 2004 ) , we introduce method and successfully applied it generic multi-document summarization . 
The value of d , which we will also refer to as the question bias ,  is a trade-off between two terms in the Vertices : Sentence IndexSentence Index SalienceSalience SentenceSentence 
3.1 The LexRank method . 
In the new approach , the 916 score of a sentence is determined by a mixture model of the relevance of the sentence to the query and the similarity of the sentence to other high-scoring sentences . 
Our model is similar in spirit to the random- walk summarization model ( Otterbacher et al. , 2005 ) . 
Once the similarity graph constructed the sentences are then ranked according to their eigenvector centrality . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
3.4 Experiments with topic-sensitive LexRank . 
As previously mentioned , the original LexRank method performed welling the context of generic summarization . 
In the training phase the experiment , we evaluated all combination with d in the range of [ 0 , 1 ] ( in increments of 0.10 ) and with a similarity threshold ranging from [ 0 , 0.9 ] ( in increments of 0.05 ) . 
We presented topic-sensitive LexRank and applied it to the problem of Sentence Retrieval . 