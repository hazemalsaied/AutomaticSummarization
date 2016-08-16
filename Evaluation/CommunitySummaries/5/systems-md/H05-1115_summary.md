3.4 Experiments with topic-sensitive LexRank . 
Using Random Walks for Question-focused Sentence Retrieval
Recent work has motivated the need for systems that support Information Synthesis tasks , in which user seeks a global understanding of a topic story Amigo et al. , 2004 ) . 
Finally , our best sentence retrieval system was applied to our test data set evaluate against the baseline . 
In contrast to the classical question answering setting ( e.g . TREC-style Q & A ( Voorhees and Tice , 2000 ) ) , in which the user presents a single question and the system returns corresponding answer ( or a set of likely answers ) , in this case the user has a more complex information . 
Similarly , when reading about a complex news story such as an emergency situation , users might seek answers to a set of questions in order to understand it better . 
For example , Figure 1 shows the interface to our Web-based news summarization system which a user has queried for information about Hurricane Isabel . 
Understanding such stories is challenging for a number of reasons . 
An intuitive interpretation of the stationary distribution can be under- 917 stood by the concept of a random walk on the graph representation of the Markov chain.With probability d , a transition is made from the current node ( sentence ) to the nodes that are similar to the query . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
In particular , complex stories contain many sub-events ( e.g . devastation of the hurricane , the relief effort , etc . ) Inaddition , while some facts surrounding the situation not change ( such as Which area did the hurricane first hit ?  ) , others may change with time ( Howmany people have been left homeless ?  ) . 
Our goal is to build a question-focused sentence retrieval mechanism using a topic-sensitive version of the method . 
Therefore , we are working towards developing a system for question answering from clusters of complex stories published over time . 
In topic-sensitive LexRank , we first stem all of the Sentence in a set of articles and compute word IDFsby the following formula : ides log ( N + 1 0.5 + sfw ) ( 1 ) whereN is the total number of Sentence in the clusters , and sfw is the number of Sentence that the word appears in . 