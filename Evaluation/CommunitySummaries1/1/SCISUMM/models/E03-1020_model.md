The algorithm is based on a graph model representing words and relationships between them . 
Sense clusters are iteratively computed by clustering the local graph of similar words around an ambiguous word . 
This paper describes an algorithm which automatically discovers word senses from free text and maps them to the appropriate entries of existing dictionaries or taxonomies . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
Following the method in ( Widdows and Dorow , 2002 ) , we build a graph in which each node represents a noun and two nodes have an edge between them if they co-occur in lists more than a given number of times 1 . 
To detect the different areas of meaning in our local graphs , we use a cluster algorithm for graphs ( Markov clustering , MCL ) developed by van Dongen ( 2000 ) . 
The local graph in step 1 consists of w , the ni neighbors of w and the n9 neighbors of the neighbors of w. Since in each iteration we only attempt to find the `` best '' cluster , it suffices to build a relatively small graph in 1 . 
We then determined the WordNet sunsets which most adequately characterized the sense clusters . 
This gives rise to an automatic , unsupervised word sense disambiguation algorithm which is trained on the data to be disambiguated . 
Preliminary observations show that the different neighbors in Table 1 can be used to indicate with great accuracy which of the senses is being used . 
