Using Random Walks for Question-focused Sentence Retrieval 
Our goal is to build a question-focused sentence retrieval mechanism using a topic-sensitive version of the LexRank method . 
The output of our system , a ranked list of sentences relevant to the user question , can be subsequently used as input to an answer selection system in order to find specific answers from the extracted sentences . 
Alternatively , the sentences cane returned to the user as a question-focused summary . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
In the graph , each node represents a sentence . 
There are edges between nodes for which the cosine similarity between the respective pair of sentences exceeds given threshold . 
The degree of a given node Isa indication of how much information the respective sentence has in common with other sentences . 
In topic-sensitive LexRank , we first stem all of the sentences in a set of articles and compute word IDFsby the following formula : 
In a Web-based news summarization setting , users of our system could choose to see the retrieved sentences ( sin Table 9 ) as a question-focused summary . 
