3.4 Experiments with topic-sensitive LexRank . 
In ( Erkan and Radev , 2004 ) , we introduce method and successfully applied it generic multi-document summarization . 
Finally , our best sentence retrieval system was applied to our test data set evaluate against the baseline . 
3.1 The LexRank method . 
In the new approach , the 916 score of a sentence is determined by a mixture model of the relevance of the sentence to the query and the similarity of the sentence to other high-scoring sentences . 
With probability ( 1-d ) , a transition is made to the nodes that are lexically similar to the current node . 
This is similar to snippet ( Wu eta 2004 ) . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
Our goal is to build a question-focused sentence retrieval mechanism using a topic-sensitive version of the method . 
As previously mentioned , the original LexRank method performed welling the context of generic summarization . 
The stationary distribution of a Markov chain can be computed by a simple iterative algorithm , called power method. 1 A simpler version of Equation 5 , where A is uniform matrix andB is a normalized binary matrix , is known as PageRank ( Brin and Page , 1998 ; Pageet al. , 1998 ) and used to rank the web pages by theGoogle search engine . 
In the training phase the experiment , we evaluated all combination with d in the range of [ 0 , 1 ] ( in increments of 0.10 ) and with a similarity threshold ranging from [ 0 , 0.9 ] ( in increments of 0.05 ) . 