It also shows that feature-based methods dramatically outperform kernel methods . 
For details about SVMLight , please see  //svmlight.joachims.org/ 
Although tree kernel-based approaches facilitate the exploration of the implicit feature space with the parse tree structure , yet the current technologies are expected to be further advanced to be effective for relatively complicated relation extraction tasks such as the one defined in ACE where 5 types and 24 subtypes need to be extracted . 
For example , we want to determine whether a person is at a location , based on the evidence in the context . 
Evaluation on the ACE corpus shows that our system outperforms Kambhatla ( 2004 ) by about 3 F-measure on extracting 24 ACE relation subtypes . 
Based on the structural risk minimization of the statistical learning theory , SVMs seek an optimal separating hyper-plane to divide the training examples into two classes and make decisions based on support vectors which are selected as the only effective instances in the training set . 
The rest of this paper is organized as follows . 
The relation extraction task was formulated at the 7th Message Understanding Conference ( MUC7 1998 ) and is starting to be addressed more and more within the natural language processing and machine learning communities . 
Miller et al ( 2000 ) augmented syntactic full parse trees with semantic information corresponding to entities and relations , and built generative models for the augmented trees . 
The experiment result also shows that our feature-based approach outperforms the tree kernel-based approaches by more than 20 F-measure on the extraction of 5 ACE relation types . 
However , this paper only uses the binary-class version . 
This category of features includes : â¢ # MB : number of other mentions in between â¢ # WB : number of words in between â¢ M1 > M2 or M1 < M2 : flag indicating whether M2/M1is included in M1/M2 . 
4.1 Words . 
Dependency tree th parse trees . 
â¢ To our surprise , incorporating the dependency tree and parse tree features only improve the F- measure by 0.6 and 0.4 respectively . 
This paper focuses on the ACE RDC task and employs diverse lexical , syntactic and semantic knowledge in feature-based relation extraction using Support Vector Machines ( SVMs ) . 
Kamchatka 2004 ) employed Maximum Entropy models for relation extraction with features derived from word , entity type , mention level , overlap , dependency tree and parse tree . 
Our study illustrates that the base phrase chunking information contributes to most of the performance improvement from syntactic aspect while additional full parsing information does not contribute much , largely due to the fact that most of relations defined in ACE corpus are within a very short distance . 
Head-driven statistical models for natural language parsing . 
The final decision of an instance in the multiple binary classification is determined by the class which has the maximal SVM output . 
In this paper , we separate the features of base phrase chunking from those of full parsing . 
This category of features concerns about the information inherent only in the full parse tree . 
The reason why we choose SVMs for this purpose is that SVMs represent the state-ofâthe-art in the machine learning research community , and there are good implementations of the algorithm available . 
The related work mentioned in Section 2 extended to explore the information embedded in the full parse trees . 
Therefore , the state-of-art full parsing still needs to be further enhanced to provide accurate enough information , especially PP ( Preposition Phrase ) attachment . 
Exploring Various Knowledge in Relation Extraction
Compared with Kambhatla ( 2004 ) , we separately incorporate the base phrase chunking information , which contributes to most of the performance improvement from syntactic aspect . 
Tree kernel-based approaches proposed by Zelenko et al ( 2003 ) and Culotta et al ( 2004 ) are able to explore the implicit feature space without much feature engineering . 
This paper will further explore the feature-based approach with a systematic study on the extensive incorporation of diverse lexical , syntactic and semantic information . 
â¢ Chunking features are very useful . 
Table 2 also measures the contributions of different features by gradually increasing the feature set . 
While short-distance relations dominate and can be resolved by simple features such as word and chunking features , the further dependency tree and parse tree features can only take effect in the remaining much less and more difficult long-distance relations . 
â¢ The usefulness of mention level features is quite limited . 
Normally , the above overlap features are too general to be effective alone . 
In this paper , we only model explicit relations because of poor inter-annotator agreement in the annotation of implicit relations and their limited number . 
With the dramatic increase in the amount of textual information available in digital archives and the WWW , there has been growing interest in techniques for automatically extracting information from text . 
Last , effective ways need to be explored to incorporate information embedded in the full Collins M . 
Instead of exploring the full parse tree information directly as previous related work , we incorporate the base phrase chunking information performance improvement from syntactic aspect while further incorporation of the parse tree and dependence tree information only slightly improves the performance . 
This is done by replacing the pronominal mention with the most recent non-pronominal antecedent when determining the word features , which include : â¢ WM1 : bag-of-words in M1 â¢ HM1 : head word of M1 3 In ACE , each mention has a head annotation and an . 
Section 3 and Section 4 describe our approach and various features employed respectively . 
â¢ Incorporating the overlap features gives some balance between precision and recall . 
It shows that our system achieves best performance of 63.1 % /49.5 / 55.5 in precision/recall/F-measure when combining diverse lexical , syntactic and semantic features . 
5 55 .5 Ka mb hat la ( 20 04 ) : fe feature bas ed 6 3 . 
While short-distance relations dominate and can be resolved by above simple features , the dependency tree and parse tree features can only take effect in the remaining much less long-distance relations . 
This feature considers the entity level of both the mentions , which can be NAME , NOMIAL and PRONOUN : â¢ ML12 : combination of mention levels 4.4 Overlap . 
â¢ Entity type features are very useful and improve the F-measure by 8.1 largely due to the recall increase . 
2 Joachims has just released a new version of SVMLight . 
Basically , SVMs are binary classifiers . 
For efficiency , we apply the one vs. others strategy , which builds K classifiers so as to separate one class from all others , instead of the pairwise strategy , which builds K* ( K-1 ) /2 classifiers considering all pairs of classes . 
Finally , we present experimental setting and results in Section 5 and conclude with some general observations in relation extraction in Section 6 . 
Complicated relation extraction tasks may also impose a big challenge to the modeling approach used by Miller et al ( 2000 ) which integrates various tasks such as part-of-speech tagging , named entity recognition , template element extraction and relation extraction , in a single model . 
Chang 2004 ) approached relation classification by combining various lexical and syntactic features with bootstrapping on top of Support Vector Machines . 
It also shows that the ACE RDC task defines some difficult sub- types such as the subtypes âBased-Inâ , âLocatedâ and âResidenceâ under the type âATâ , which are difficult even for human experts to differentiate . 
Two features are defined to include this information : â¢ ET1SC2 : combination of the entity type of M1 and the semantic class of M2 when M2 triggers a personal social subtype . 
Table 1 lists the types and subtypes of relations for the ACE Relation Detection and Characterization ( RDC ) task , along with their frequency of occurrence in the ACE training set . 
In ACE vocabulary , entities are objects , mentions are references to them , and relations are semantic relationships between entities . 
Support Vector Machines ( SVMs ) are a supervised machine learning technique motivated by the statistical learning theory ( Vapnik 1998 ) . 
The tree kernels developed in Culotta et al ( 2004 ) are yet to be effective on the ACE RDC task . 
The RDC task detects and classifies implicit and explicit relations 1 between entities identified by the EDT task . 
In the future work , we will focus on exploring more semantic knowledge in relation extraction , which has not been covered by current research . 
Two features are defined to include this information : â¢ ET1Country : the entity type of M1 when M2 is a country name â¢ CountryET2 : the entity type of M2 when M1 is a country name 5  //ilk.kub.nl/~sabine/chunklink/ Personal Relative Trigger Word List This is used to differentiate the six personal social relation subtypes in ACE : Parent , Grandparent , Spouse , Sibling , Other-Relative and Other- Personal . 
It also shows that our system outperforms tree kernel-based systems ( Culotta et al 2004 ) by over 20 F-measure on extracting 5 ACE relation types . 
In this paper , we have presented a feature-based approach for relation extraction where diverse lexical , syntactic and semantic knowledge are employed . 
It is well known that chunking plays a critical role in the Template Relation task of the 7th Message Understanding Conference ( MUC7 1998 ) . 
Section 2 presents related work . 
This is largely due to incorporation of two semantic resources , i.e . the country name list and the personal relative trigger word list . 
For each pair of mentions 3 we compute various lexical , syntactic and semantic features . 
This category of features includes information about the words , part-of-speeches and phrase labels of the words on which the mentions are dependent in the dependency tree derived from the syntactic full parse tree . 
It also shows that our fea 1 In ACE (  //www.ldc.upenn.edu/Projects/ACE ) , . 
The dependency tree is built by using the phrase head information returned by the Collinsâ parser and linking all the other fragments in a phrase to its head . 
Here , the base phrase chunks are derived from full parse trees using the Perl script 5 written by Sabine Buchholz from Tilburg University and the Collinsâ parser ( Collins 1999 ) is employed for full parsing . 
Therefore , it would be interesting to see how imperfect EDT affects the performance in relation extraction . 
Qc 2005 Association for Computational Linguistics ture-based approach outperforms tree kernel-based approaches by 11 F-measure in relation detection and more than 20 F-measure in relation detection and classification on the 5 ACE relation types . 
This feature concerns about the entity type of both the mentions , which can be PERSON , ORGANIZATION , FACILITY , LOCATION and GeoPolitical Entity or GPE : â¢ ET12 : combination of mention entity types 4.3 Mention Level . 
Most of the chunking features concern about the head words of the phrases between the two mentions . 
Similar to word features , three categories of phrase heads are considered : 1 ) the phrase heads in between are also classified into three bins : the first phrase head in between , the last phrase head in between and other phrase heads in between ; 2 ) the phrase heads before M1 are classified into two bins : the first phrase head before and the second phrase head before ; 3 ) the phrase heads after M2 are classified into two bins : the first phrase head after and the second phrase head after . 
It shows that : Features P R F Words 69.2 23.7 35.3 +Entity Type 67.1 32.1 43.4 +Mention Level 67.1 33.0 44.2 +Overlap 57.4 40.9 47.8 +Chunking 61.5 46.5 53.0 +Dependency Tree 62.1 47.2 53.6 +Parse Tree 62.3 47.6 54.0 +Semantic Resources 63.1 49.5 55.5 Table 2 : Contribution of different features over 43 relation subtypes in the test data â¢ Using word features only achieves the performance of 69.2 % /23.7 /35.3 in precision/recall/F- measure . 
â¢ ET1DW1 : combination of the entity type and the dependent word for M1 â¢ H1DW1 : combination of the head word and the dependent word for M1 â¢ ET2DW2 : combination of the entity type and the dependent word for M2 â¢ H2DW2 : combination of the head word and the dependent word for M2 â¢ ET12SameNP : combination of ET12 and whether M1 and M2 included in the same NP â¢ ET12SamePP : combination of ET12 and whether M1 and M2 exist in the same PP â¢ ET12SameVP : combination of ET12 and whether M1 and M2 included in the same VP 4.7 Parse Tree . 
This suggests that relation detection is critical for relation extraction . 
Yet further research work is still expected to make it effective with complicated relation extraction tasks such as the one defined in ACE . 
In addition , we distinguish the argument order of the two mentions ( M1 for the first mention and M2 for the second mention ) , e.g . M1-Parent- Of-M2 vs. M2-Parent-Of-M1 . 
Evaluation on the ACE corpus shows that Detection Error False Negative 462 base phrase chunking contributes to most of the False Positive 165 Table 6 : Distribution of errors 6 Discussion and Conclusion . 
The effective incorporation of diverse features enables our system outperform previously best- reported systems on the ACE corpus . 
Information Extraction ( IE ) systems are expected to identify relevant information ( usually of predefined types ) from text documents in a certain domain and put them in a structured format . 
4.5 Base Phrase Chunking . 
However , The remaining words that do not have above four classes are manually classified . 
Evaluation on the ACE RDC task shows that our approach of combining various kinds of evidence can scale better to problems , where we have a lot of relation types with a relatively small amount of annotated data . 
According to the scope of the NIST Automatic Content Extraction ( ACE ) program , current research in IE has three main objectives : Entity Detection and Tracking ( EDT ) , Relation Detection and Characterization ( RDC ) , and Event Detection and Characterization ( EDC ) . 
â¢ PTP : path of phrase labels ( removing duplicates ) connecting M1 and M2 in the parse tree â¢ PTPH : path of phrase labels ( removing duplicates ) connecting M1 and M2 in the parse tree augmented with the head word of the top phrase in the path . 
8 6 9 . 4 7 2 . 6 General Staff 2 0 1 1 0 8 4 6 71 . 
In this paper , we use the binary-class SVMLight2 developed by Joachims ( 1998 ) . 
This suggests that feature-based methods can effectively combine different features from a variety of sources ( e.g . WordNet and gazetteers ) that can be brought to bear on relation extraction . 
Culotte A. and Sorensen J . 
countries names lists This is to differentiate the Relation subtype âROLE.Citizen-Ofâ , which defines the relationships between a persons and the countries of the personnels citizenship , from other subtypes , especially âROLE.Residenceâ , where defines the relationships between a persons and the locations in which the persons lives . 