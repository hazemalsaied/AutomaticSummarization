Superdense tagging is also interesting for many applications that use shallow semantics , e.g . information extraction and question answering . 
Our evaluation will use exactly the same test sets as Ciaramita and Johnson ( 2003 ) . 
Carmita and Johnson ( 2003 ) found that common nouns missing from WORDNET 1.6 occurred every 8 sentences in the BLLIP corpus . 
An additional potential is to integrate automatically acquired relationships with the information found in WordNet , which seems to suffer from several serious limitations ( Curran 2005 ) , and typically overlaps to a rather limited extent with the output of automatic acquisition methods . 
Technical domains , such as medicine , require separate treatment since common words often take on special meanings , and a significant proportion of their vocabulary does not overlap with everyday vocabulary . 
This technique is similar to Hearst and SchuÂ¨ tze ( 1993 ) and Widdows ( 2003 ) . 
However , sometimes the unknown noun does not appear in our 2 billion word corpus , or at least does not appear frequently enough to provide sufficient contextual information to extract reliable synonyms . 
Superdense tagging assigns unknown nouns one of 26 broad semantic categories used by lexicographers to organize their manual insertion into WORDNET . 
Our results significantly outperform Ciaramita and Johnson ( 2003 ) on both test sets even though our system is unsupervised . 
We have used the WORDNET 1.6 test set to experiment with different parameter settings and have kept the WORDNET 1.7.1 test set as a final comparison of best results with Ciaramita and Johnson ( 2003 ) . 
consistency when classifying similar words into categories . 
Also , in the data from Ciaramita and Johnson all of the words are in lower case , so no sensible guessing rules could help . 
How are words with multiple super senses handled ? 
One solution would be to take the intersection between vector across words for each superdense i.e . to find the common contexts that these words appear in ) . 