Doro and Widdows construct a graph for a target word w by taking the sub-graph induced by the neighborhood of w ( without w ) and clustering it with MCL . 
Following the method in ( Widdows and Dorow , 2002 ) , we build a graph in which each node represents a noun and two nodes have an edge between them if they co-occur in lists more than a given number of times 1 . 
The idea underlying the MCL-algorithm is that random walks within the graph will tend to stay in the same cluster rather than jump between clusters . 
Discovering Corpus-Specific Word Senses
there are other related efforts on word sense discrimination ( Dorow and Widdows , 2003 ; Fukumoto and Suzuki , 1999 ; Pedersen and Bruce , 1997 ) . 
Then senses of target word were iteratively learned by clustering the local graph of similar words around target word . 
Their algorithm required a threshold as input , which controlled the number of senses . 
The algorithm in ( Dorow and Widdows , 2003 ) represented target noun word , its neighbors and their relationships using a graph in which each node denoted a noun and two nodes had an edge between them if they co-occurred with more than a given number of times . 
As they rely on the detection of high-density areas in a network of cooccurrences , ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) are the closest methods to ours . 
From a global viewpoint , these two differences lead ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) to build finer senses than ours . 
Instead we link each word to its top n neighbors where n can be determined by the user ( cf . 
Output the list of class-labels which best represent the different senses of w in the corpus . 
Discrimination against previously extracted sense clusters enables us to discover new senses . 
Similar to the approach as presented in ( Dorow and Widdows , 2003 ) we construct a word graph . 
In our case , we chose a more general approach by working at the level of a simiÂ­larity graph when the similarity of two words is given by their relation of cooccurrence , our situaÂ­tion is comparable to the one of ( VÃ©ronis , 2003 ) and ( Dorow and Widdows , 2003 ) 
The family of such algorithms is described in ( Widdows , 2003 ) . 
However , whereas there are many edges within an area of meaning , there is only a small number of ( weak ) links between different areas of meaning . 
Section 5 describes the experiment and presents a sample of the results . 
This is achieved , in a manner similar to Pantel and Lin 's ( 2002 ) sense clustering approach , by removing c 's features from the set of features used for finding similar words . 
Sense clusters are iteratively computed by clustering the local graph of similar words around an ambiguous word . 
The same corpus evidence which supports a clustering of an ambiguous Word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 