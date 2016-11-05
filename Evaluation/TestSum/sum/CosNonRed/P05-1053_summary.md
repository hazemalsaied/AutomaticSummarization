Exploring Various Knowledge in Relation Extraction
This suggests that most of useful information in full parse trees for relation extraction is shallow and can be captured by chunking.
Normally , the above overlap features are too general to be effective alone . 
Moreover , we only apply the simple linear kernel , although other kernels can perform better . 
It shows that our system achieves best performance of 63.1 % /49.5 / 55.5 in precision/recall/F-measure when combining diverse lexical , syntactic and semantic features . 
For example , we want to determine whether a person is at a location , based on the evidence in the context . 
â¢ The usefulness of mention level features is quite limited . 
The relation extraction task was formulated at the 7th Message Understanding Conference ( MUC7 1998 ) and is starting to be addressed more and more within the natural language processing and machine learning communities . 
This category of features concerns about the information inherent only in the full parse tree . 
This suggests that most of useful information in full parse trees for relation extraction is shallow and can be captured by chunking . 
Helenka et al ( 2003 ) proposed extracting relations by computing kernel functions between parse trees . 
â¢ WM2 : bag-of-words in M2 â¢ HM2 : head word of M2 â¢ HM12 : combination of HM1 and HM2 â¢ WBNULL : when no word in between â¢ WBFL : the only word in between when only one word in between â¢ WBF : first word in between when at least two words in between â¢ WBL : last word in between when at least two words in between â¢ WBO : other words in between except first and last words when at least three words in between â¢ BM1F : first word before M1 â¢ BM1L : second word before M1 â¢ AM2F : first word after M2 â¢ AM2L : second word after M2 4.2 Entity Type . 
This category of features includes : â¢ # MB : number of other mentions in between â¢ # WB : number of words in between â¢ M1 > M2 or M1 < M2 : flag indicating whether M2/M1is included in M1/M2 . 
Culotte et al ( 2004 ) extended this work to estimate kernel functions between augmented dependency trees and achieved 63.2 F-measure in relation detection and 45.8 F-measure in relation detection and classification on the 5 ACE relation types . 
Many methods have been proposed to deal with this task , including supervised learning algorithms ( Miller et al. , 2000 ; Zelenko et al. , 2002 ; Culotta and Soresen , 2004 ; Kambhatla , 2004 ; Zhou et al. , 2005 ) , semi-supervised learning algorithms ( Brin , 1998 ; Agichtein and Gravano , 2000 ; Zhang , 2004 ) , and unsupervised learning algorithm ( Hasegawa et al. , 2004 ) . 
Many machine learning methods have been proposed to address this problem , e.g. , supervised learning algorithms ( Miller et al. , 2000 ; Zelenko et al. , 2002 ; Culotta and Soresen , 2004 ; Kambhatla , 2004 ; Zhou et al. , 2005 ) , semi-supervised learning algorithms ( Brin , 1998 ; Agichtein and Gravano , 2000 ; Zhang , 2004 ) , and unsupervised learning algorithms ( Hasegawa et al. , 2004 ) . 
Chang 2004 ) approached relation classification by combining various lexical and syntactic features with bootstrapping on top of Support Vector Machines . 
This may be due to the fact that most of relations in the ACE corpus are quite local . 
Miller et al ( 2000 ) augmented syntactic full parse trees with semantic information corresponding to entities and relations , and built generative models for the augmented trees . 
Finally , we present experimental setting and results in Section 5 and conclude with some general observations in relation extraction in Section 6 . 
â¢ Incorporating the overlap features gives some balance between precision and recall . 
â¢ Chunking features are very useful . 
Complicated relation extraction tasks may also impose a big challenge to the modeling approach used by Miller et al ( 2000 ) which integrates various tasks such as part-of-speech tagging , named entity recognition , template element extraction and relation extraction , in a single model . 
We use SVM as our learning algorithm with the full feature set from Zhou et al . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
In this paper , we have presented a feature-based approach for relation extraction where diverse lexical , syntactic and semantic knowledge are employed . 
It shows that : Features P R F Words 69.2 23.7 35.3 +Entity Type 67.1 32.1 43.4 +Mention Level 67.1 33.0 44.2 +Overlap 57.4 40.9 47.8 +Chunking 61.5 46.5 53.0 +Dependency Tree 62.1 47.2 53.6 +Parse Tree 62.3 47.6 54.0 +Semantic Resources 63.1 49.5 55.5 Table 2 : Contribution of different features over 43 relation subtypes in the test data â¢ Using word features only achieves the performance of 69.2 % /23.7 /35.3 in precision/recall/F- measure . 
This suggests that feature-based methods can effectively combine different features from a variety of sources ( e.g . WordNet and gazetteers ) that can be brought to bear on relation extraction . 
While short-distance relations dominate and can be resolved by simple features such as word and chunking features , the further dependency tree and parse tree features can only take effect in the remaining much less and more difficult long-distance relations . 
Tree kernel-based approaches proposed by Zelenko et al ( 2003 ) and Culotta et al ( 2004 ) are able to explore the implicit feature space without much feature engineering . 
For each pair of mentions 3 we compute various lexical , syntactic and semantic features . 
With the dramatic increase in the amount of textual information available in digital archives and the WWW , there has been growing interest in techniques for automatically extracting information from text . 
â¢ To our surprise , incorporating the dependency tree and parse tree features only improve the F- measure by 0.6 and 0.4 respectively . 
In this paper , we separate the features of base phrase chunking from those of full parsing . 
â¢ Entity type features are very useful and improve the F-measure by 8.1 largely due to the recall increase . 
explicit relations occur in text with explicit evidence suggesting the relationships . 
5 55 .5 Ka mb hat la ( 20 04 ) : fe feature bas ed 6 3 . 
Information Extraction ( IE ) systems are expected to identify relevant information ( usually of predefined types ) from text documents in a certain domain and put them in a structured format . 
This suggests that relation detection is critical for relation extraction . 
This feature concerns about the entity type of both the mentions , which can be PERSON , ORGANIZATION , FACILITY , LOCATION and GeoPolitical Entity or GPE : â¢ ET12 : combination of mention entity types 4.3 Mention Level . 
The effective incorporation of diverse features enables our system outperform previously best- reported systems on the ACE corpus . 
While short-distance relations dominate and can be resolved by above simple features , the dependency tree and parse tree features can only take effect in the remaining much less long-distance relations . 
This feature considers the entity level of both the mentions , which can be NAME , NOMIAL and PRONOUN : â¢ ML12 : combination of mention levels 4.4 Overlap . 
Most of the chunking features concern about the head words of the phrases between the two mentions . 
Two features are defined to include this information : â¢ ET1SC2 : combination of the entity type of M1 and the semantic class of M2 when M2 triggers a personal social subtype . 
Two features are defined to include this information : â¢ ET1Country : the entity type of M1 when M2 is a country name â¢ CountryET2 : the entity type of M2 when M1 is a country name 5  //ilk.kub.nl/~sabine/chunklink/ Personal Relative Trigger Word List This is used to differentiate the six personal social relation subtypes in ACE : Parent , Grandparent , Spouse , Sibling , Other-Relative and Other- Personal . 
This paper investigates the incorporation of diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using SVM . 
According to the scope of the NIST Automatic Content Extraction ( ACE ) program , current research in IE has three main objectives : Entity Detection and Tracking ( EDT ) , Relation Detection and Characterization ( RDC ) , and Event Detection and Characterization ( EDC ) . 
Although tree kernel-based approaches facilitate the exploration of the implicit feature space with the parse tree structure , yet the current technologies are expected to be further advanced to be effective for relatively complicated relation extraction tasks such as the one defined in ACE where 5 types and 24 subtypes need to be extracted . 
The EDT task entails the detection of entity mentions and chaining them together by identifying their co reference . 
2 Joachims has just released a new version of SVMLight . 
Basically , SVMs are binary classifiers . 
For efficiency , we apply the one vs. others strategy , which builds K classifiers so as to separate one class from all others , instead of the pairwise strategy , which builds K* ( K-1 ) /2 classifiers considering all pairs of classes . 
In the future work , we will focus on exploring more semantic knowledge in relation extraction , which has not been covered by current research . 
In this way , we model relation extraction as a multi-class classification problem with 43 classes , two for each relation subtype ( except the above 6 symmetric subtypes ) and a âNONEâ class for the case where the two mentions are not related . 
The RDC task detects and classifies implicit and explicit relations 1 between entities identified by the EDT task . 
Support Vector Machines ( SVMs ) are a supervised machine learning technique motivated by the statistical learning theory ( Vapnik 1998 ) . 
This paper focuses on the ACE RDC task and employs diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using Support Vector Machines ( SVMs ) . 
It shows that 73 % ( 627/864 of errors results from relation detection and 27 % ( 237/864 of errors results from relation characterization , among which 17.8 % ( 154/864 of errors are from misclassification across relation types and 9.6 % ( 83/864 # of relations of errors are from misclassification of relation sub- types inside the same relation types . 
In this paper , we only model explicit relations because of poor inter-annotator agreement in the annotation of implicit relations and their limited number . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
Yet further research work is still expected to make it effective with complicated relation extraction tasks such as the one defined in ACE . 
Evaluation on the ACE corpus shows that Detection Error False Negative 462 base phrase chunking contributes to most of the False Positive 165 Table 6 : Distribution of errors 6 Discussion and Conclusion . 
Kamchatka 2004 ) employed Maximum Entropy models for relation extraction with features derived from word , entity type , mention level , overlap , dependency tree and parse tree . 
This is done by replacing the pronominal mention with the most recent non-pronominal antecedent when determining the word features , which include : â¢ WM1 : bag-of-words in M1 â¢ HM1 : head word of M1 3 In ACE , each mention has a head annotation and an . 
Note that only 6 of these 24 relation subtypes are symmetric : âRelative- Locationâ , âAssociateâ , âOther-Relativeâ , âOther- Professionalâ , âSiblingâ , and âSpouseâ . 
This paper will further explore the feature-based approach with a systematic study on the extensive incorporation of diverse lexical , syntactic and semantic information . 
Based on the structural risk minimization of the statistical learning theory , SVMs seek an optimal separating hyper-plane to divide the training examples into two classes and make decisions based on support vectors which are selected as the only effective instances in the training set . 
In ACE vocabulary , entities are objects , mentions are references to them , and relations are semantic relationships between entities . 
â¢ CPHBNULL when no phrase in between â¢ CPHBFL : the only phrase head when only one phrase in between â¢ CPHBF : first phrase head in between when at least two phrases in between â¢ CPHBL : last phrase head in between when at least two phrase heads in between â¢ CPHBO : other phrase heads in between except first and last phrase heads when at least three phrases in between â¢ CPHBM1F : first phrase head before M1 â¢ CPHBM1L : second phrase head before M1 â¢ CPHAM2F : first phrase head after M2 â¢ CPHAM2F : second phrase head after M2 â¢ CPP : path of phrase labels connecting the two mentions in the chunking â¢ CPPH : path of phrase labels connecting the two mentions in the chunking augmented with head words , if at most two phrases in between 4.6 Dependency Tree . 
It also shows that our system achieves overall performance of 77.2 % /60.7 /68.0 and 63.1 % /49.5 /55.5 in precision/recall/F-measure on the 5 ACE relation types and the best-reported systems on the ACE corpus . 
Compared with Kambhatla ( 2004 ) , we separately incorporate the base phrase chunking information , which contributes to most of the performance improvement from syntactic aspect . 
It also shows that our fea 1 In ACE (  //www.ldc.upenn.edu/Projects/ACE ) , . 
The ACE corpus is gathered from various newspapers , newswire and broadcasts . 
The tree kernels developed in Culotta et al ( 2004 ) are yet to be effective on the ACE RDC task . 
Entities can be of five types : persons , organizations , locations , facilities and geopolitical entities ( GPE : geographically defined regions that indicate a political boundary , e.g . countries , states , cities , etc . ) . 
â¢ ET1DW1 : combination of the entity type and the dependent word for M1 â¢ H1DW1 : combination of the head word and the dependent word for M1 â¢ ET2DW2 : combination of the entity type and the dependent word for M2 â¢ H2DW2 : combination of the head word and the dependent word for M2 â¢ ET12SameNP : combination of ET12 and whether M1 and M2 included in the same NP â¢ ET12SamePP : combination of ET12 and whether M1 and M2 exist in the same PP â¢ ET12SameVP : combination of ET12 and whether M1 and M2 included in the same VP 4.7 Parse Tree . 
Table 3 shows that about 70 % of relations exist where two mentions are embedded in each other or separated by at most one word . 
Qc 2005 Association for Computational Linguistics ture-based approach outperforms tree kernel-based approaches by 11 F-measure in relation detection and more than 20 F-measure in relation detection and classification on the 5 ACE relation types . 
This category of features includes information about the words , part-of-speeches and phrase labels of the words on which the mentions are dependent in the dependency tree derived from the syntactic full parse tree . 
Evaluation on the ACE corpus shows that effective incorporation of diverse features enables our system outperform previously best-reported systems on the 24 ACE relation subtypes and significantly outperforms tree kernel-based systems by over 20 in F-measure on the 5 ACE relation types . 
The effect of personal relative trigger words is very limited due to the limited number of testing instances over personal social relation subtypes . 
Similar to word features , three categories of phrase heads are considered : 1 ) the phrase heads in between are also classified into three bins : the first phrase head in between , the last phrase head in between and other phrase heads in between ; 2 ) the phrase heads before M1 are classified into two bins : the first phrase head before and the second phrase head before ; 3 ) the phrase heads after M2 are classified into two bins : the first phrase head after and the second phrase head after . 
Besides , we also demonstrate how semantic information such as WordNet and Name List , can be used in feature-based relation extraction to further improve the performance . 
Mentions have three levels : names , nominal expressions or pronouns . 
2 51 .8 63 .2 67 .1 35 .0 45 .8 Table 5 : Comparison of our system with other best-reported systems on the ACE corpus Error Type # Errors first . 
Extraction of semantic relationships between entities can be very useful for applications such as question answering , e.g . to answer the query âWho is the president of the United States ? â . 
In addition , we distinguish the argument order of the two mentions ( M1 for the first mention and M2 for the second mention ) , e.g . M1-Parent- Of-M2 vs. M2-Parent-Of-M1 . 
Our study illustrates that the base phrase chunking information contributes to most of the performance improvement from syntactic aspect while additional full parsing information does not contribute much , largely due to the fact that most of relations defined in ACE corpus are within a very short distance . 
We also demonstrate how semantic information such as WordNet ( Miller 1990 ) and Name List can be used in the feature-based framework . 
This has an effect of choosing the base phrase contained in the extent annotation . 
Evaluation shows that the incorporation of diverse features enables our system achieve best reported performance . 
Implicit relations need not have explicit supporting evidence in text , though they should be evident from a reading of the document . 
We also demonstrate how semantic information such as WordNet and Name List , can be used in feature-based relation extraction to further improve the performance . 
According to their positions , four categories of words are considered : 1 ) the words of both the mentions , 2 ) the words between the two mentions , 3 ) the words before M1 , and 4 ) the words after M2 . 
427 Proceedings of the 43rd Annual Meeting of the ACL , pages 427â434 Ann Arbor , June 2005 . 
The rest of this paper is organized as follows . 
Section 2 presents related work . 
Table 2 measures the performance of our relation extraction system over the 43 ACE relation subtypes on the testing set . 
Section 3 and Section 4 describe our approaches and various features employed respectively . 