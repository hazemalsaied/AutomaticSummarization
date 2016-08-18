This approach to disambiguation combines the benefits of both Yarowsky 's ( 1995 ) and Schtitze 's ( 1998 ) approaches . 
Based on the intuition that nouns which co-occur in a list are often semantically related , we extract contexts of the form Noun , Noun , ... Andros Noun , e.g . `` gnomic DNA from rat , mouse and dog '' . 
Following the method in ( Widdows and Dorow , 2002 ) , we build a graph in which each node represents a noun and two nodes have an edge between them if they co-occur in lists more than a given number of times 1 . 
The quality of the Markov clustering depends strongly on several parameters such as a granularity factor and the size of the local graph . 
Section 3 describes the way we divide graphs surrounding ambiguous words into different areas corresponding to different senses , using Markov clustering ( van Dongen , 2000 ) . 
We then determined the WordNet sunsets which most adequately characterized the sense clusters . 
In section 4 , we outline a word sense discovery algorithm which bypasses the problem of parameter tuning . 
In section 2 , we present the graph model from which we discover word senses . 
This paper describes an algorithm which automatically discovers word senses from free text and maps them to the appropriate entries of existing dictionaries or taxonomies . 
The ability to map senses into a taxonomy using the class-labelling algorithm can be used to ensure that the sense-distinctions discovered correspond to recognized differences in meaning . 
The family of such algorithms is described in ( Widdows , 2003 ) . 
Our algorithm was applied to each word in the list ( with parameters Iii = 20 , n2 = 10 , r = 2.0 , k = 2.0 ) in order to extract the top two sense clusters only . 
Instead we link each word to its top n neighbors where n can be determined by the user ( cf . 
The same corpus evidence which supports a clustering of an ambiguous word into distinct senses can be used to decide which sense is referred to in a given context ( Schiitze , 1998 ) . 
However , there are ambiguous words with more closely related senses which are metaphorical or metonymy variations of one another . 
Following Lin 's work ( 1998 ) , we are currently investigating a graph with verb-object , verb-subject and modifier-noun-collocations from which it is possible to infer more about the senses of systematically polygamous words . 
However , whereas there are many edges within an area of meaning , there is only a small number of ( weak ) links between different areas of meaning . 
Flow within dense regions in the graph is concentrated by both expansion and inflation . 
In contrast to pure Markov clustering , we do n't try to find a complete clustering of G into senses at once . 
Take the `` best '' cluster ( the one that is most strongly connected to w in Gw before removal of w ) , add it to the final list of clusters L and removal its features from F. 5 . 
Usually , one sense of an ambiguous word w is much more frequent than its other senses present in the corpus . 
The word sense clustering algorithm as outlined below can be applied to any kind of similarity measure based on any set of features . 
sz44 CD miltrA , literate h , ) Cik Figure 1 : Local graph of the word mouse 
1 Si ample cutoff functions proved unsatisfactory because of the bias they give to more frequent words . 
The problem can be addressed by using word sense clustering to attune an existing resource to accurately describe the meanings used in a particular corpus . 
To detect the different areas of meaning in our local graphs , we use a cluster algorithm for graphs ( Markov clustering , MCL ) developed by van Dongen ( 2000 ) . 
The output of the MCL-algorithm strongly depends on the inflation and expansion parameters r and k as well as the size of the local graph which serves as input to MCL . 
If the local graph handed over to the MCL process is small , we might miss some of w 's meaning in the corpus . 