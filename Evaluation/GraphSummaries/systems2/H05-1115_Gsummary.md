3.4 Experiments with topic-sensitive LexRank . 
Finally , our best sentence retrieval system was applied to our test data set evaluate against the baseline . 
An intuitive interpretation of the stationary distribution can be under- 917 stood by the concept of a random walk on the graph representation of the Markov chain.With probability d , a transition is made from the current node ( sentence ) to the nodes that are similar to the query . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
Our goal is to build a question-focused sentence retrieval mechanism using a topic-sensitive version of the method . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
In topic-sensitive LexRank , we first stem all of the Sentence in a set of articles and compute word IDFsby the following formula : ides log ( N + 1 0.5 + sfw ) ( 1 ) whereN is the total number of Sentence in the clusters , and sfw is the number of Sentence that the word appears in . 