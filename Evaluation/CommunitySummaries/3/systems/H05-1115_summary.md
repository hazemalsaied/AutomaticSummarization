The final number of questions annotated for answer the entire corpus was 341 , and the distribution questions per cluster can be found in Table 1 . 
Using Random Walks for Question-focused Sentence Retrieval
Recent work has motivated the need for systems that support Information Synthesis tasks , in which user seeks a global understanding of a topic story Amigo et al. , 2004 ) . 
To evaluate our sentence retrieval mechanism , reproduced extract files , which contain a list of sentences deemed to be relevant to the question , for the system and from human judgment . 
We presented topic-sensitive LexRank and applied it to the problem of sentence retrieval . 
In the new approach , the 916 score of a sentence is determined by a mixture model of the relevance of the sentence to the query and the similarity of the sentence to other high-scoring sentences . 
Our model is similar in spirit to the random- walk summarization model ( Otterbacher et al. , 2005 ) . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
Out of the 72 questions in the set , the baseline system outperformed LexRank on 22 of the questions . 
To contrast , LexRank might perform better when the question provides fewer content words , since it considers both similarity to the query andinter-sentence similarity . 
In contrast to the classical question answering setting ( e.g . TREC-style Q & A ( Voorhees and Tice , 2000 ) ) , in which the user presents a single question and the system returns corresponding answer ( or a set of likely answers ) , in this case the user has a more complex information . 
Given this observation , we experimented with two mixed strategies , in which the numbers of content word in a question determined whether LexRank or the baseline systems was used for Sentence Retrieval . 