Our model is similar in spirit to the random- walk summarization model ( Otterbacher et al. , 2005 ) . 
Using Random Walks for Question-focused Sentence Retrieval
Recent work has motivated the need for systems that support Information Synthesis tasks , in which user seeks a global understanding of a topic story Amigo et al. , 2004 ) . 
Presently , we introduce topic-sensitive LexRank in creating sentence retrieval system . 
While evaluations of question answering systems are often based on a shorter list of ranked sentences we chose to generate longer lists for several reasons . 
In contrast to the classical question answering setting ( e.g . TREC-style Q & A ( Voorhees and Tice , 2000 ) ) , in which the user presents a single question and the system returns corresponding answer ( or a set of likely answers ) , in this case the user has a more complex information . 
Therefore , there is often more than one correct answer to a question.We aim to develop a method for sentence retrieval that goes beyond finding sentences that are similar to a single query . 
In the graph each node represents a sentence . 
However , a small probability for jumping to a node that is lexically similar to the given sentence ( rather than the question itself is needed . 
Below , we describe a topic-sensitive version of LexRank , which is more appropriate for the question-focusedsentence retrieval problem . 
Similarly , when reading about a complex news story such as an emergency situation , users might seek answers to a set of questions in order to understand it better . 
Our goal is to build a question-focused sentence retrieval mechanism using a topic-sensitive version of the method . 
In the training phase the experiment , we evaluated all combination with d in the range of [ 0 , 1 ] ( in increments of 0.10 ) and with a similarity threshold ranging from [ 0 , 0.9 ] ( in increments of 0.05 ) . 
3.4 Experiments with topic-sensitive LexRank . 