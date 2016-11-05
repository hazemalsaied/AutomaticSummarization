2 Table 5 Segmentation performance presented in previous work and of our combination model . 
Table 1 shows the performance of the dictionary-based segmentation . 
CRF + Rule system represents a combination of CRF model and rule based model presented in Zhang et al . 
Best 0 5 represents the best system of the Second International Chinese Word Segmentation Bakeoff on the corresponding data ; CRF + rule-system represents confidence- based combination of CRF and rule-based models , presented in Zhang et al . 
In addition , we found a clear weakness with the IOB tagging approach : It yields a very low in-vocabulary ( IV ) rate ( R-iv ) in return for a higher out-of-vocabulary ( OOV ) rate ( R-oov ) . 
The effect of the confidence measure is shown in Table 3 , where we used Î± = 0.7 and confidence threshold t = 0.8 . 
We found the former achieved better performance than the existing character-based tagging, and the latter improved segmentation further by combining the former with a dictionary-based segmentation.
using the FMM , and then labeled with âIOBâ tags by the CRFs . 
0 means the current word ; â1 â2 the first or second word to the left ; 1 , 2 , the first or second word to the right . 
Since it was a closed test , some information such as Arabic and Chinese number and alphabetical letters can not be used . 
It is composed of three parts : a dictionary-based N-gram word segmentation for segmenting IV words , a subword- based tagging by the CRF for recognizing OOVs , and a confidence-dependent word segmentation used for merging the results of both the dictionary-based and the IOB tagging . 
Detailed descriptions about sub word tagging by CRF can be found in our paper ( Zhang et al. , 2006 ) . 
A confidence measure threshold , t , was defined for making a decision based on the value . 
The confidence measure comes from two sources : IOB tagging and dictionary- based word segmentation . 
We found a speed up both in training and test . 
Note a lexicon and a LM are the only needed resources for building a dictionary-based CWS , like the Ã¢â¬Ådict-hybrid.Ã¢â¬Â ( Zhang et al. , 2006 ) We used the Ã¢â¬Ådict-hybridÃ¢â¬Â to segment the SMT training corpus and test data . 
Section 4 describes current state- of-the-art methods for Chinese word segmentation , with which our results were compared . 
After the dictionary- based word segmentation , the words are re-segmented into sub words by FMM before being fed to IOB tagging . 
For the subword-based tagging , we added another 2000 most frequent multiple- character words to the lexicons for tagging . 
In this work , we proposed a subword-based IOB tagging method for Chinese word segmentation . 
Our word segmentation process is illustrated in Fig . 
It was first used in Chinese word segmentation by ( Xue and Shen , 2003 ) , where maximum entropy methods were used . 
We chose the three models that achieved at least one best score in the closed tests from Emerson ( 2005 ) , as well as the sub-word-based model of Zhang et al . 
For the character-based tagging , we used all the Chinese characters . 
In the followings , we illustrate our word segmentation process in Section 2 , where the subword-based tagging is implemented by the CRFs method . 
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
The character-based âIOBâ tagging approach has been widely used in Chinese word segmentation recently ( Xue and Shen , 2003 ; Peng and McCallum , 2004 ; Tseng et al. , 2005 ) . 
We proposed two approaches to improve Chinese word segmentation a subword-based tagging and a confidence measure approach.
In addition, the latter can be used to balance out-of-vocabulary rates and in-vocabulary rates.
We proposed two approaches to improve Chinese word segmentation : a subword-based tagging and a confidence measure approach . 