The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
Flow within dense regions in the graph is concentrated by both expansion and inflation . 
Discovering Corpus-Specific Word Senses
The word sense clustering algorithm as outlined below can be applied to any kind of similarity measure based on any set of features . 
sz44 CD miltrA , literate h , ) Cik Figure 1 : Local graph of the word mouse 
We conducted a pilot experiment to examine the performance of our algorithm on a set of words with varying degree of ambiguity . 
Finally , section 6 sketches applications of the algorithm and discusses future work . 
The algorithm is based on a graph model representing words and relationships between them.
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
Doro and Widdows construct a graph for a target word w by taking the sub-graph induced by the neighborhood of w ( without w ) and clustering it with MCL . 
The model from which we discover distinct word senses is built automatically from the British National corpus , which is tagged for parts of speech . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
As they rely on the detection of high-density areas in a network of cooccurrences , ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) are the closest methods to ours . 
In our case , we chose a more general approach by working at the level of a simiÂ­larity graph when the similarity of two words is given by their relation of cooccurrence , our situaÂ­tion is comparable to the one of ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) 
Preliminary observations show that the different neighbors in Table 1 can be used to indicate with great accuracy which of the senses is being used . 
Similar to the approach as presented in ( Dorow and Widdows , 2003 ) we construct a word graph . 
The same corpus evidence which supports a clustering of an ambiguous word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 
This is achieved , in a manner similar to Pantel and Lin 's ( 2002 ) sense clustering approach , by removing c 's features from the set of features used for finding similar words . 
The algorithm is based on a graph model representing words and relationships between them . 
Sense clusters are iteratively computed by clustering the local graph of similar words around an ambiguous word . 