The algorithm is based on a graph model representing words and relationships between them.
Discovering Corpus-Specific Word Senses
In contrast to pure Markov clustering , we do n't try to find a complete clustering of G into senses at once . 
Sense clusters are iteratively computed by clustering the local graph of similar words around an ambiguous word.
there are other related efforts on word sense discrimination ( Dorow and Widdows , 2003 ; Fukumoto and Suzuki , 1999 ; Pedersen and Bruce , 1997 ) . 
On the other hand , if the local graph is too big , we will get a lot of noise . 
We then recompute the local graph Gw by discriminating against c 's features . 
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
This paper describes an algorithm which automatically discovers word senses from free text and maps them to the appropriate entries of existing dictionaries or taxonomies . 
Automatic word sense discovery has applications of many kinds . 
It can greatly facilitate a lexicographer 's work and can be used to automatically construct corpus-based taxonomies or to tune existing ones . 
The same corpus evidence which supports a clustering of an ambiguous word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 
This paper is organized as follows . 
In section 2 , we present the graph model from which we discover word senses . 
Section 3 describes the way we divide graphs surrounding ambiguous words into different areas corresponding to different senses , using Markov clustering ( van Dongen , 2000 ) . 
The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
In section 4 , we outline a word sense discovery algorithm which bypasses the problem of parameter tuning . 
We conducted a pilot experiment to examine the performance of our algorithm on a set of words with varying degree of ambiguity . 
Section 5 describes the experiment and presents a sample of the results . 
Finally , section 6 sketches applications of the algorithm and discusses future work . 
The model from which we discover distinct Word senses is built automatically from the British National corpus , which is tagged for parts of speech . 