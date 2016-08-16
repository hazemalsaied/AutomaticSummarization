However , a small probability for jumping to a node that is lexically similar to the given sentence ( rather than the question itself is needed . 
Using Random Walks for Question-focused Sentence Retrieval
In ( Erkan and Radev , 2004 ) , we introduce method and successfully applied it generic multi-document summarization . 
The value of d , which we will also refer to as the question bias ,  is a trade-off between two terms in the Vertices : Sentence IndexSentence Index SalienceSalience SentenceSentence 
3.1 The LexRank method . 
When using any metric to compare sentences and a query , there is always likely to bea tie between multiple sentences ( or , similarly , there may be cases where fewer than the number of desired sentences have similarity scores above zero ) .LexRank effectively provides a means to break such ties . 
Our model is similar in spirit to the random- walk summarization model ( Otterbacher et al. , 2005 ) . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
We also considered several threshold for inter-sentence cosine similarities , where we ignored the similarities between the sentences that are below the threshold . 
The idea behind using LexRank for sentence retrieval is that a system that considers only the similarity between candidate sentences and the input and not the similarity between the candidate sentences themselves , is likely to miss some important sentences . 
It should be noted that both for the LexRank and baseline systems , chronological ordering of the documents sentence is preserved , such that in cases where two sentences have the same score , the one published is ranked higher . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
In the training phase the experiment , we evaluated all combination with d in the range of [ 0 , 1 ] ( in increments of 0.10 ) and with a similarity threshold ranging from [ 0 , 0.9 ] ( in increments of 0.05 ) . 
We presented topic-sensitive LexRank and applied it to the problem of Sentence Retrieval . 