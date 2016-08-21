The final number of questions annotated for answer the entire corpus was 341 , and the distribution questions per cluster can be found in Table 1 . 
Using Random Walks for Question-focused Sentence Retrieval
Recent work has motivated the need for systems that support Information Synthesis tasks , in which user seeks a global understanding of a topic story Amigo et al. , 2004 ) . 
To evaluate our sentence retrieval mechanism , reproduced extract files , which contain a list of sentences deemed to be relevant to the question , for the system and from human judgment . 
We presented topic-sensitive LexRank and applied it to the problem of sentence retrieval . 
In the new approach , the 916 score of a sentence is determined by a mixture model of the relevance of the sentence to the query and the similarity of the sentence to other high-scoring sentences . 
Our model is similar in spirit to the random- walk summarization model ( Otterbacher et al. , 2005 ) . 
The baseline system explained above does not make use of any inter-sentence information in a cluster.We hypothesize that a sentence that is similar to the high scoring sentences in the cluster should also a high score . 
Graph Figure 2 : LexRank example : sentence similarity graph with a cosine threshold of 0.15 . 
To apply LexRank , a similarity graph is produce the sentences in an input document set . 
As discussed in Section 2 , our goal wast develop a topic-sensitive version of LexRank and to use it to improve a baseline system , which previously been used successfully for query-basedsentence retrieval ( Allan et al. , 2003 ) . 
Out of the 72 questions in the set , the baseline system outperformed LexRank on 22 of the questions . 
To contrast , LexRank might perform better when the question provides fewer content words , since it considers both similarity to the query andinter-sentence similarity . 
Given this observation , we experimented with two mixed strategies , in which the number of content words in a question determined whether LexRank or the baseline system was used for sentence retrieval . 
This time , all four LexRank systems outperformed the baseline , both in terms of average MRRand TRDR scores . 
While LexRank outperforms the baseline system on the first two clusters both in terms of and TRDR , their performances are not substantially different on the third cluster . 
It should be noted that both for the LexRank and baseline systems , chronological ordering of the documents sentence is preserved , such that in cases where two sentences have the same score , the one published is ranked higher . 
The idea behind using LexRank for sentence retrieval is that a system that considers only the similarity between candidate sentences and the input and not the similarity between the candidate sentences themselves , is likely to miss some important sentences . 
An example of such a scenario is illustrated inTables 8 and 9 , which show the top ranked sentence the baseline and LexRank , respectively for the question caused the Kursk to sink ?  from theKursk submarine cluster . 
In contrast to the classical question answering setting ( e.g . TREC-style Q & A ( Voorhees and Tice , 2000 ) ) , in which the user presents a single question and the system returns corresponding answer ( or a set of likely answers ) , in this case the user has a more complex information . 
The score for the four LexRank systems and the baseline on the development data are shown in systems Ave. MRR Ave. TRDR baseline 0.5518 0.8297 LR [ 0.14,0.95 ] 0.5267 0.8305LR [ 0.18,0.90 ] 0.5376 0.8382LR [ 0.18,0.95 ] 0.5421 0.8382LR [ 0.20,0.95 ] 0.5404 0.8311 Table 4 : training phase : systems outperforming the baseline in terms of TRDR score . 