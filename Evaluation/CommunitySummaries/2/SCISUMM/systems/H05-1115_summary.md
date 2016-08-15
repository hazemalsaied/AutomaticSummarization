The final number of questions annotated for answer the entire corpus was 341 , and the distribution questions per cluster can be found in Table 1 . 
Using Random Walks for Question-focused Sentence Retrieval
Recent work has motivated the need for systems that support Information Synthesis tasks , in which user seeks a global understanding of a topic story Amigo et al. , 2004 ) . 
We evaluate its performance against a competitive baseline , which considers the similarity between each sentence and the question using IDF-weighed word overlap ) . 
We presented topic-sensitive LexRank and applied it to the problem of sentence retrieval . 
In the new approach , the 916 score of a sentence is determined by a mixture model of the relevance of the sentence to the query and the similarity of the sentence to other high-scoring sentences . 
The baseline system explained above does not make use of any inter-sentence information in a cluster.We hypothesize that a sentence that is similar to the high scoring sentences in the cluster should also a high score . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
The idea behind using LexRank for sentence retrieval is that a system that considers only the similarity between candidate sentences and the input and not the similarity between the candidate sentences themselves , is likely to miss some important sentences . 
Out of the 72 questions in the set , the baseline system outperformed LexRank on 22 of the questions . 
It should be noted that both for the LexRank and baseline systems , chronological ordering of the documents sentence is preserved , such that in cases where two sentences have the same score , the one published is ranked higher . 
In contrast to the classical question answering setting ( e.g . TREC-style Q & A ( Voorhees and Tice , 2000 ) ) , in which the user presents a single question and the system returns corresponding answer ( or a set of likely answers ) , in this case the user has a more complex information . 
Similarly , when reading about a complex news story such as an emergency situation , users might seek answers to a set of questions in order to understand it better . 
For example , Figure 1 shows the interface to our Web-based news summarization systems which a user has queried for information about Hurricane Isabel . 