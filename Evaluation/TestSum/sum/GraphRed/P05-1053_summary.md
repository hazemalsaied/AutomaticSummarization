It also shows that feature-based methods dramatically outperform kernel methods . 
For details about SVMLight , please see  //svmlight.joachims.org/ 
Although tree kernel-based approaches facilitate the exploration of the implicit feature space with the parse tree structure , yet the current technologies are expected to be further advanced to be effective for relatively complicated relation extraction tasks such as the one defined in ACE where 5 types and 24 subtypes need to be extracted . 
For example , we want to determine whether a person is at a location , based on the evidence in the context . 
Evaluation on the ACE corpus shows that our system outperforms Kambhatla ( 2004 ) by about 3 F-measure on extracting 24 ACE relation subtypes . 
For example , we want to determine whether a person is at a location , based on the evidence in the context . 
The rest of this paper is organized as follows . 
The relation extraction task was formulated at the 7th Message Understanding Conference ( MUC7 1998 ) and is starting to be addressed more and more within the natural language processing and machine learning communities . 
Miller et al ( 2000 ) augmented syntactic full parse trees with semantic information corresponding to entities and relations , and built generative models for the augmented trees . 
Miller et al ( 2000 ) augmented syntactic full parse trees with semantic information corresponding to entities and relations , and built generative models for the augmented trees . 
The rest of this paper is organized as follows . 
This category of features includes : â¢ # MB : number of other mentions in between â¢ # WB : number of words in between â¢ M1 > M2 or M1 < M2 : flag indicating whether M2/M1is included in M1/M2 . 
This category of features includes : â¢ # MB : number of other mentions in between â¢ # WB : number of words in between â¢ M1 > M2 or M1 < M2 : flag indicating whether M2/M1is included in M1/M2 . 
Dependency tree th parse trees . 
Dependency tree th parse trees . 
This paper focuses on the ACE RDC task and employs diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using Support Vector Machines ( SVMs ) . 
Kamchatka 2004 ) employed Maximum Entropy models for relation extraction with features derived from word , entity type , mention level , overlap , dependency tree and parse tree . 
Our study illustrates that the base phrase chunking information contributes to most of the performance improvement from syntactic aspect while additional full parsing information does not contribute much , largely due to the fact that most of relations defined in ACE corpus are within a very short distance . 
Kamchatka 2004 ) employed Maximum Entropy models for relation extraction with features derived from word , entity type , mention level , overlap , dependency tree and parse tree . 
The final decision of an instance in the multiple binary classification is determined by the class which has the maximal SVM output . 
In this paper , we separate the features of base phrase chunking from those of full parsing . 
In this paper , we separate the features of base phrase chunking from those of full parsing . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
Exploring Various Knowledge in Relation Extraction
Compared with Kambhatla ( 2004 ) , we separately incorporate the base phrase chunking information , which contributes to most of the performance improvement from syntactic aspect . 
Tree kernel-based approaches proposed by Zelenko et al ( 2003 ) and Culotta et al ( 2004 ) are able to explore the implicit feature space without much feature engineering . 
Tree kernel-based approaches proposed by Zelenko et al ( 2003 ) and Culotta et al ( 2004 ) are able to explore the implicit feature space without much feature engineering . 
â¢ Chunking features are very useful . 
â¢ Chunking features are very useful . 
While short-distance relations dominate and can be resolved by simple features such as word and chunking features , the further dependency tree and parse tree features can only take effect in the remaining much less and more difficult long-distance relations . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
In this paper , we only model explicit relations because of poor inter-annotator agreement in the annotation of implicit relations and their limited number . 
With the dramatic increase in the amount of textual information available in digital archives and the WWW , there has been growing interest in techniques for automatically extracting information from text . 
Last , effective ways need to be explored to incorporate information embedded in the full Collins M . 
Instead of exploring the full parse tree information directly as previous related work , we incorporate the base phrase chunking information performance improvement from syntactic aspect while further incorporation of the parse tree and dependence tree information only slightly improves the performance . 
This is done by replacing the pronominal mention with the most recent non-pronominal antecedent when determining the word features , which include : â¢ WM1 : bag-of-words in M1 â¢ HM1 : head word of M1 3 In ACE , each mention has a head annotation and an . 
This is done by replacing the pronominal mention with the most recent non-pronominal antecedent when determining the word features , which include : â¢ WM1 : bag-of-words in M1 â¢ HM1 : head word of M1 3 In ACE , each mention has a head annotation and an . 
This is done by replacing the pronominal mention with the most recent non-pronominal antecedent when determining the word features , which include : â¢ WM1 : bag-of-words in M1 â¢ HM1 : head word of M1 3 In ACE , each mention has a head annotation and an . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
This feature considers the entity level of both the mentions , which can be NAME , NOMIAL and PRONOUN : â¢ ML12 : combination of mention levels 4.4 Overlap . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
However , this paper only uses the binary-class version . 
Basically , SVMs are binary classifiers . 
Basically , SVMs are binary classifiers . 
Exploring Various Knowledge in Relation Extraction
Complicated relation extraction tasks may also impose a big challenge to the modeling approach used by Miller et al ( 2000 ) which integrates various tasks such as part-of-speech tagging , named entity recognition , template element extraction and relation extraction , in a single model . 
This paper focuses on the ACE RDC task and employs diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using Support Vector Machines ( SVMs ) . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
Two features are defined to include this information : â¢ ET1SC2 : combination of the entity type of M1 and the semantic class of M2 when M2 triggers a personal social subtype . 
This paper focuses on the ACE RDC task and employs diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using Support Vector Machines ( SVMs ) . 
In ACE vocabulary , entities are objects , mentions are references to them , and relations are semantic relationships between entities . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
Support Vector Machines ( SVMs ) are a supervised machine learning technique motivated by the statistical learning theory ( Vapnik 1998 ) . 
Support Vector Machines ( SVMs ) are a supervised machine learning technique motivated by the statistical learning theory ( Vapnik 1998 ) . 
In the future work , we will focus on exploring more semantic knowledge in relation extraction , which has not been covered by current research . 
In the future work , we will focus on exploring more semantic knowledge in relation extraction , which has not been covered by current research . 
The experiment result also shows that our feature-based approach outperforms the tree kernel-based approaches by more than 20 F-measure on the extraction of 5 ACE relation types . 
This paper focuses on the ACE RDC task and employs diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using Support Vector Machines ( SVMs ) . 
The tree kernels developed in Culotta et al ( 2004 ) are yet to be effective on the ACE RDC task . 
For example , we want to determine whether a person is at a location , based on the evidence in the context . 
Two features are defined to include this information : â¢ ET1Country : the entity type of M1 when M2 is a country name â¢ CountryET2 : the entity type of M2 when M1 is a country name 5  //ilk.kub.nl/~sabine/chunklink/ Personal Relative Trigger Word List This is used to differentiate the six personal social relation subtypes in ACE : Parent , Grandparent , Spouse , Sibling , Other-Relative and Other- Personal . 
Compared with Kambhatla ( 2004 ) , we separately incorporate the base phrase chunking information , which contributes to most of the performance improvement from syntactic aspect . 
This category of features includes information about the words , part-of-speeches and phrase labels of the words on which the mentions are dependent in the dependency tree derived from the syntactic full parse tree . 
It also shows that our fea 1 In ACE (  //www.ldc.upenn.edu/Projects/ACE ) , . 
It also shows that our fea 1 In ACE (  //www.ldc.upenn.edu/Projects/ACE ) , . 
It also shows that our fea 1 In ACE (  //www.ldc.upenn.edu/Projects/ACE ) , . 
Exploring Various Knowledge in Relation Extraction
The experiment result also shows that our feature-based approach outperforms the tree kernel-based approaches by more than 20 F-measure on the extraction of 5 ACE relation types . 
Tree kernel-based approaches proposed by Zelenko et al ( 2003 ) and Culotta et al ( 2004 ) are able to explore the implicit feature space without much feature engineering . 
Support Vector Machines ( SVMs ) are a supervised machine learning technique motivated by the statistical learning theory ( Vapnik 1998 ) . 
â¢ The usefulness of mention level features is quite limited . 
â¢ The usefulness of mention level features is quite limited . 
This category of features includes : â¢ # MB : number of other mentions in between â¢ # WB : number of words in between â¢ M1 > M2 or M1 < M2 : flag indicating whether M2/M1is included in M1/M2 . 
Exploring Various Knowledge in Relation Extraction
It also shows that our fea 1 In ACE (  //www.ldc.upenn.edu/Projects/ACE ) , . 
In addition , we distinguish the argument order of the two mentions ( M1 for the first mention and M2 for the second mention ) , e.g . M1-Parent- Of-M2 vs. M2-Parent-Of-M1 . 
Evaluation on the ACE corpus shows that our system outperforms Kambhatla ( 2004 ) by about 3 F-measure on extracting 24 ACE relation subtypes . 
It shows that our system achieves best performance of 63.1 % /49.5 / 55.5 in precision/recall/F-measure when combining diverse lexical , syntactic and semantic features . 
The dependency tree is built by using the phrase head information returned by the Collinsâ parser and linking all the other fragments in a phrase to its head . 
In this paper , we separate the features of base phrase chunking from those of full parsing . 
Yet further research work is still expected to make it effective with complicated relation extraction tasks such as the one defined in ACE . 
Section 3 and Section 4 describe our approach and various features employed respectively . 
According to the scope of the NIST Automatic Content Extraction ( ACE ) program , current research in IE has three main objectives : Entity Detection and Tracking ( EDT ) , Relation Detection and Characterization ( RDC ) , and Event Detection and Characterization ( EDC ) . 
This category of features includes information about the words , part-of-speeches and phrase labels of the words on which the mentions are dependent in the dependency tree derived from the syntactic full parse tree . 
8 6 9 . 4 7 2 . 6 General Staff 2 0 1 1 0 8 4 6 71 . 
The tree kernels developed in Culotta et al ( 2004 ) are yet to be effective on the ACE RDC task . 
â¢ The usefulness of mention level features is quite limited . 
Information Extraction ( IE ) systems are expected to identify relevant information ( usually of predefined types ) from text documents in a certain domain and put them in a structured format . 
countries names lists This is to differentiate the Relation subtype âROLE.Citizen-Ofâ , which defines the relationships between a persons and the countries of the personnels citizenship , from other subtypes , especially âROLE.Residenceâ , where defines the relationships between a persons and the locations in which the persons lives . 