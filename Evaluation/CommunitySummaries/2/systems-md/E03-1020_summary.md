The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
The idea underlying the MCL-algorithm is that random walks within the graph will tend to stay in the same cluster rather than jump between clusters . 
We then determined the WordNet sunsets which most adequately characterized the sense clusters . 
there are other related efforts on word sense discrimination ( Dorow and Widdows , 2003 ; Fukumoto and Suzuki , 1999 ; Pedersen and Bruce , 1997 ) . 
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
Their algorithm required a threshold as input , which controlled the number of senses . 
The algorithm in ( Dorow and Widdows , 2003 ) represented target noun word , its neighbors and their relationships using a graph in which each node denoted a noun and two nodes had an edge between them if they co-occurred with more than a given number of times . 
As they rely on the detection of high-density areas in a network of cooccurrences , ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) are the closest methods to ours . 
Instead we link each word to its top n neighbors where n can be determined by the user ( cf . 
The word sense clustering algorithm as outlined below can be applied to any kind of similarity measure based on any set of features . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
The same corpus evidence which supports a clustering of an ambiguous word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 
Therefore , even after removal of the wing-node , the two areas of meaning are still linked via tail . 
In our case , we chose a more general approach by working at the level of a simiÂ­larity graph when the similarity of two words is given by their relation of cooccurrence , our situaÂ­tion is comparable to the one of ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) 
From a global viewpoint , these two differences lead ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) to build finer senses than ours . 
Similar to the approach as presented in ( Dorow and Widdows , 2003 ) we construct a word graph . 
Discrimination against previously extracted sense clusters enables us to discover new senses . 
This is achieved , in a manner similar to Pantel and Lin 's ( 2002 ) sense clustering approach , by removing c 's features from the set of features used for finding similar words . 
Doro and Widdows construct a graph for a target word w by taking the sub-graph induced by the neighborhood of w ( without w ) and clustering it with MCL . 
The algorithm is based on a graph model representing words and relationships between them . 