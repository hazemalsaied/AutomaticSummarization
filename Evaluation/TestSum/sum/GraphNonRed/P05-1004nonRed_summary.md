Carmita and Johnson ( 2003 ) call this superdense tagging and describe a multi-class perception tagger , which uses WORDNETâs hierarchical structure to create many annotated training instances from the sunset glosses . 
Our evaluation will use exactly the same test sets as Ciaramita and Johnson ( 2003 ) . 
Carmita and Johnson ( 2003 ) propose a very natural evaluation for superdense tagging : inserting the extra common nouns that have been added to a new version of WORDNET . 
Bur- gun and Bodenreider ( 2001 ) compared an alignment of WORDNET with the UMLS medical resource and found only a very small degree of overlap . 
A disadvantage of this similarity approach is that it requires full synonym extraction , which compares the unknown word against a large number of words when , in S Y S T E M W N 1.6 W N 1.7 .1 Cia ra mit a an d Joh nso n bas eli ne 2 1 % 2 8 % Cia ra mit a an d Joh nso n per cep tro n 5 3 % 5 3 % Si mil art y bas ed res ult s 6 8 % 6 3 % Table 6 : Summary of superdense tagging accuracies fact , we want to calculate the similarity to a small number of super senses . 
This technique is similar to Hearst and SchuÂ¨ tze ( 1993 ) and Widdows ( 2003 ) . 
Broad semantic classification is currently used by lexicographers to or- anise the manual insertion of words into WORDNET , and is an experimental precursor to automatically inserting words directly into the WORDNET hierarchy . 
Our application of semantic similarity to superdense tagging follows earlier work by Hearst and SchuÂ¨ tze ( 1993 ) and Widdows ( 2003 ) . 
Carmita and Johnson ( 2003 ) believe that the key sense distinctions are still maintained by super senses . 
Our results significantly outperform Ciaramita and Johnson ( 2003 ) on both test sets even though our system is unsupervised . 
Does every superdense of each extracted synonym get the whole weight of that synonym or is it distributed evenly between the super senses like Resnik ( 1995 ) ? 
Superdense tagging is also interesting for many applications that use shallow semantics , e.g . information extraction and question answering . 
A considerable amount of research addresses structurally and statistically manipulating the hierarchy of WORD- NET and the construction of new word nets using the concept structure from English . 
For lexical FreeNet , Beefer- man ( 1998 ) adds over 350 000 collocation pairs ( trigger pairs ) extracted from a 160 million words corpus of broadcast news using mutual information . 