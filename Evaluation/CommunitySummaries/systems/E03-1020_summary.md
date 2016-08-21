The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
The word sense clustering algorithm as outlined below can be applied to any kind of similarity measure based on any set of features . 
Doro and Widdows construct a graph for a target word w by taking the sub-graph induced by the neighborhood of w ( without w ) and clustering it with MCL . 
Flow within dense regions in the graph is concentrated by both expansion and inflation . 
Discovering Corpus-Specific Word Senses
The benefits of automatic , data-driven word sense discovery for natural language processing and lexicography would be very great . 
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
Finally , section 6 sketches applications of the algorithm and discusses future work . 
The family of such algorithms is described in ( Widdows , 2003 ) . 
The algorithm is based on a graph model representing words and relationships between them.
Instead we link each word to its top n neighbors where n can be determined by the user ( cf . 
We conducted a pilot experiment to examine the performance of our algorithm on a set of words with varying degree of ambiguity . 
However , there are ambiguous words with more closely related senses which are metaphorical or metonymy variations of one another . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
The problem can be addressed by using word sense clustering to attune an existing resource to accurately describe the meanings used in a particular corpus . 
As they rely on the detection of high-density areas in a network of cooccurrences , ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) are the closest methods to ours . 
In our case , we chose a more general approach by working at the level of a simiÂ­larity graph when the similarity of two words is given by their relation of cooccurrence , our situaÂ­tion is comparable to the one of ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) 
In contrast to pure Markov clustering , we do n't try to find a complete clustering of G into senses at once . 
Similar to the approach as presented in ( Dorow and Widdows , 2003 ) we construct a word graph . 
The same corpus evidence which supports a clustering of an ambiguous word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 
This is achieved , in a manner similar to Pantel and Lin 's ( 2002 ) sense clustering approach , by removing c 's features from the set of features used for finding similar words . 
sz44 CD miltrA , literate h , ) Cik Figure 1 : Local graph of the word mouse 
In section 2 , we present the graph model from which we discover word senses . 
Following Lin 's work ( 1998 ) , we are currently investigating a graph with verb-object , verb-subject and modifier-noun-collocations from which it is possible to infer more about the senses of systematically polygamous words . 
Section 3 describes the way we divide graphs surrounding ambiguous words into different areas corresponding to different senses , using Markov clustering ( van Dongen , 2000 ) . 
Sense clusters are iteratively computed by clustering the local graph of similar words around an ambiguous word.
Sense clusters are iteratively computed by clustering the local graph of similar words around an ambiguous word . 