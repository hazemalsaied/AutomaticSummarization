In this work we used it more delicately . 
In this work we used it more delicately . 
Using the CRFs approaches , we prove that it outperformed the character- based method using the CRF approaches . 
Using the CRFs approaches , we prove that it outperformed the character- based method using the CRF approaches . 
A new OOV was thus created . 
In section 2.2 , we proposed a confidence measure approach to reevaluate the results of IOB tagging by combinations of the results of the dictionary-based segmentation . 
It proves the proposed word-based IOB tagging was very effective . 
It was first used in Chinese word segmentation by ( Xue and Shen , 2003 ) , where maximum entropy methods were used . 
It was first used in Chinese word segmentation by ( Xue and Shen , 2003 ) , where maximum entropy methods were used . 
In the results of the closed test in Bakeoff 2005 ( Emerson , 2005 ) , the work of ( Tseng et al. , 2005 ) , using conditional random fields ( CRF ) for the IOB tagging , yielded very high R-oovs in all of the four corpora used , but the R-iv rates were lower . 
71 6 0.9 64 0.9 72 Table 2 : Segmentation results by a pure subword-based IOB tagging . 
The authors appreciate the reviewer effort and good advice for improving the paper . 
We could yield a better results than those shown in Table 4 using such information . 
In this section we introduce a confidence measure approach to combine the two results . 
In the results of the closed test in Bakeoff 2005 ( Emerson , 2005 ) , the work of ( Tseng et al. , 2005 ) , using conditional random fields ( CRF ) for the IOB tagging , yielded very high R-oovs in all of the four corpora used , but the R-iv rates were lower . 
95 1 Table 4 : Comparison our results with the best ones from Sighan Bakeoff 2005 in terms of F-score ivs than Table 2 . 
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
The segmentation results using CRF tagging are shown in Table 2 , where the upper numbers of each slot were produced by the character-based approach while the lower numbers were of the subword-based . 
In the results of the closed test in Bakeoff 2005 ( Emerson , 2005 ) , the work of ( Tseng et al. , 2005 ) , using conditional random fields ( CRF ) for the IOB tagging , yielded very high R-oovs in all of the four corpora used , but the R-iv rates were lower . 
By way of the confidence measure we combined results from the dictionary-based and the IOB-tagging-based and as a result , we could achieve the optimal performance . 
By way of the confidence measure we combined results from the dictionary-based and the IOB-tagging-based and as a result , we could achieve the optimal performance . 
For AS corpus , âAdam Smithâ are two words in the training but become a one- word in the test , âAdamSmithâ . 
In addition , we found a clear weakness with the IOB tagging approach : It yields a very low in-vocabulary ( IV ) rate ( R-iv ) in return for a higher out-of-vocabulary ( OOV ) rate ( R-oov ) . 
It is composed of three parts : a dictionary-based N-gram word segmentation for segmenting IV words , a subword- based tagging by the CRF for recognizing OOVs , and a confidence-dependent word segmentation used for merging the results of both the dictionary-based and the IOB tagging . 
We defined a cutoff value for each feature type and selected the features with occurrence counts over the cutoff . 
2.2 Confidence-dependent word segmentation . 
We downloaded and used the package âCRF++â from the site âhttp //www.chasen.org/Ëtaku/software.â According to the CRFs , the probability of an IOB tag sequence , T = t0 t1 Â· Â· Â· tM , given the word sequence , W = w0 w1 Â· Â· Â· wM , is defined by p ( T |W ) = and current observation ti simultaneously ; gk ( ti , W ) , the epigram feature functions because they trigger only current observation ti . Î»k and Âµk are the model parameters corresponding to feature functions fk and gk respectively . 
Tri- gram LMs were generated using the SRI LM toolkit for disambiguation . 
Tri- gram LMs were generated using the SRI LM toolkit for disambiguation . 