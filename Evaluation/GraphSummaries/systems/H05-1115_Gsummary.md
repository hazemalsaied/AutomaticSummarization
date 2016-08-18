However , a small probability for jumping to a node that is lexically similar to the given sentence ( rather than the question itself is needed . 
Recently , graph-based methods have proved useful for number of NLP and IR tasks such as documentre-ranking in ad hoc IR ( Kurland and Lee , 2005 ) and analyzing sentiments in text ( Pang and Lee,2004 ) . 
Since we are interested in a passage retrieval mechanism that sentences relevant to a given question , providing input to the question answering component of our system , the improvement in average TRDR score is very promising . 
Table 4 shows the configurations of that performed better than the baseline system on the training data , based on mean TRDRscores over the 184 training questions . 
The value of d , which we will also refer to as the question bias ,  is a trade-off between two terms in the Vertices : Sentence IndexSentence Index SalienceSalience SentenceSentence 
With probability ( 1-d ) , a transition is made to the nodes that are lexically similar to the current node . 
In ( Erkan and Radev , 2004 ) , we introduce method and successfully applied it generic multi-document summarization . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
Once the similarity graph constructed the sentences are then ranked according to their eigenvector centrality . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
Our goal is to build a question-focused sentence retrieval mechanism using a topic-sensitive version of the method . 
The stationary distribution of a Markov chain can be computed by a simple iterative algorithm , called power method. 1 A simpler version of Equation 5 , where A is uniform matrix andB is a normalized binary matrix , is known as PageRank ( Brin and Page , 1998 ; Pageet al. , 1998 ) and used to rank the web pages by theGoogle search engine . 
As previously mentioned , the original LexRank method performed welling the context of generic summarization . 
Presently , we introduce topic-sensitive LexRank in creating sentence retrieval system . 
3.4 Experiments with topic-sensitive LexRank . 
3.1 The LexRank method . 
In topic-sensitive LexRank , we first stem all of the sentences in a set of articles and compute word IDFsby the following formula : ides log ( N + 1 0.5 + sfw ) ( 1 ) whereN is the total number of sentences in the cluster , and sfw is the number of sentences that the word appears in . 
In the training phase the experiment , we evaluated all combination with d in the range of [ 0 , 1 ] ( in increments of 0.10 ) and with a similarity threshold ranging from [ 0 , 0.9 ] ( in increments of 0.05 ) . 
We presented topic-sensitive LexRank and applied it to the problem of Sentence Retrieval . 