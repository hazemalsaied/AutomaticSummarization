The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
Following the method in ( Widdows and Dorow , 2002 ) , we build a graph in which each node represents a noun and two nodes have an edge between them if they co-occur in lists more than a given number of times 1 . 
We then determined the WordNet sunsets which most adequately characterized the sense clusters . 
there are other related efforts on word sense discrimination ( Dorow and Widdows , 2003 ; Fukumoto and Suzuki , 1999 ; Pedersen and Bruce , 1997 ) . 
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
Their algorithm required a threshold as input , which controlled the number of senses . 
The algorithm in ( Dorow and Widdows , 2003 ) represented target noun word , its neighbors and their relationships using a graph in which each node denoted a noun and two nodes had an edge between them if they co-occurred with more than a given number of times . 
As they rely on the detection of high-density areas in a network of cooccurrences , ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) are the closest methods to ours . 
Instead we link each word to its top n neighbors where n can be determined by the user ( cf . 
1 Si ample cutoff functions proved unsatisfactory because of the bias they give to more frequent words . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
The same corpus evidence which supports a clustering of an ambiguous word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 
Therefore , even after removal of the wing-node , the two areas of meaning are still linked via tail . 
In our case , we chose a more general approach by working at the level of a simiÂ­larity graph when the similarity of two words is given by their relation of cooccurrence , our situaÂ­tion is comparable to the one of ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) 
From a global viewpoint , these two differences lead ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) to build finer senses than ours . 
Similar to the approach as presented in ( Dorow and Widdows , 2003 ) we construct a word graph . 
In contrast to pure Markov clustering , we do n't try to find a complete clustering of G into senses at once . 
This is achieved , in a manner similar to Pantel and Lin 's ( 2002 ) sense clustering approach , by removing c 's features from the set of features used for finding similar words . 
Doro and Widdows construct a graph for a target word w by taking the sub-graph induced by the neighborhood of w ( without w ) and clustering it with MCL . 
sz44 CD miltrA , literate h , ) Cik Figure 1 : local graph of the Word mouse 