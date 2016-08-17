section 2 ) , and we plan to evaluate the uses of our clustering algorithm for unsupervised disambiguation more thoroughly . 
The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
We then determined the WordNet sunsets which most adequately characterized the sense clusters . 
Discovering Corpus-Specific Word Senses
The algorithm consists of the following steps : 1 . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
In section 2 , we present the graph model from which we discover word senses . 
However , whereas there are many edges within an area of meaning , there is only a small number of ( weak ) links between different areas of meaning . 
Automatic word sense discovery has applications of many kinds . 
Preliminary observations show that the different neighbors in Table 1 can be used to indicate with great accuracy which of the senses is being used . 
Our algorithm was applied to each word in the list ( with parameters Iii = 20 , n2 = 10 , r = 2.0 , k = 2.0 ) in order to extract the top two sense clusters only . 
The family of such algorithms is described in ( Widdows , 2003 ) . 
Following the method in ( Widdows and Dorow , 2002 ) , we build a graph in which each node represents a noun and two nodes have an edge between them if they co-occur in lists more than a given number of times 1 . 
The expansion steps corresponds with taking the k-th power of TG as outlined above and allows node to see new neighbors . 