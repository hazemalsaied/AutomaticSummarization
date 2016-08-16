The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
Doro and Widdows construct a graph for a target word w by taking the sub-graph induced by the neighborhood of w ( without w ) and clustering it with MCL . 
Discovering Corpus-Specific Word Senses
The benefits of automatic , data-driven word sense discovery for natural language processing and lexicography would be very great . 
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
The family of such algorithms is described in ( Widdows , 2003 ) . 
We prepare an evaluation of our algorithm as applied to the collocation relationships ( cf . 
The algorithm is based on a graph model representing words and relationships between them.
Instead we link each word to its top n neighbors where n can be determined by the user ( cf . 
We conducted a pilot experiment to examine the performance of our algorithm on a set of words with varying degree of ambiguity . 
However , there are ambiguous words with more closely related senses which are metaphorical or metonymy variations of one another . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
As they rely on the detection of high-density areas in a network of cooccurrences , ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) are the closest methods to ours . 
In our case , we chose a more general approach by working at the level of a simiÂ­larity graph when the similarity of two words is given by their relation of cooccurrence , our situaÂ­tion is comparable to the one of ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) 
In contrast to pure Markov clustering , we do n't try to find a complete clustering of G into senses at once . 
Similar to the approach as presented in ( Dorow and Widdows , 2003 ) we construct a word graph . 
In section 4 , we outline a word sense discovery algorithm which bypasses the problem of parameter tuning . 
This is achieved , in a manner similar to Pantel and Lin 's ( 2002 ) sense clustering approach , by removing c 's features from the set of features used for finding similar words . 
sz44 CD miltrA , literate h , ) Cik Figure 1 : Local graph of the word mouse 
Section 3 describes the way we divide graph surrounding ambiguous Word into different areas corresponding to different senses , using Markov clustering ( van Dongen , 2000 ) . 