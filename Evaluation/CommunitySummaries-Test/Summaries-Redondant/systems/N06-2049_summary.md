2 Table 5 Segmentation performance presented in previous work and of our combination model . 
2 Table 5 Segmentation performance presented in previous work and of our combination model . 
CRF + Rule system represents a combination of CRF model and rule based model presented in Zhang et al . 
Best 0 5 represents the best system of the Second International Chinese Word Segmentation Bakeoff on the corresponding data ; CRF + rule-system represents confidence- based combination of CRF and rule-based models , presented in Zhang et al . 
CRF + Rule system represents a combination of CRF model and rule based model presented in Zhang et al . 
Best 0 5 represents the best system of the Second International Chinese Word Segmentation Bakeoff on the corresponding data ; CRF + rule-system represents confidence- based combination of CRF and rule-based models , presented in Zhang et al . 
In addition , we found a clear weakness with the IOB tagging approach : It yields a very low in-vocabulary ( IV ) rate ( R-iv ) in return for a higher out-of-vocabulary ( OOV ) rate ( R-oov ) . 
The effect of the confidence measure is shown in Table 3 , where we used Î± = 0.7 and confidence threshold t = 0.8 . 
Our results are listed together with the best results from Bakeoff 2005 in Table 4 in terms of F-scores . 
We found the former achieved better performance than the existing character-based tagging, and the latter improved segmentation further by combining the former with a dictionary-based segmentation.
The effect of the confidence measure is shown in Table 3 , where we used Î± = 0.7 and confidence threshold t = 0.8 . 
using the FMM , and then labeled with âIOBâ tags by the CRFs . 
0 means the current word ; â1 â2 the first or second word to the left ; 1 , 2 , the first or second word to the right . 
It is composed of three parts : a dictionary-based N-gram word segmentation for segmenting IV words , a subword- based tagging by the CRF for recognizing OOVs , and a confidence-dependent word segmentation used for merging the results of both the dictionary-based and the IOB tagging . 
Our results are listed together with the best results from Bakeoff 2005 in Table 4 in terms of F-scores . 
After the dictionary- based word segmentation , the words are re-segmented into sub words by FMM before being fed to IOB tagging . 
Since it was a closed test , some information such as Arabic and Chinese number and alphabetical letters can not be used . 
It is composed of three parts : a dictionary-based N-gram word segmentation for segmenting IV words , a subword- based tagging by the CRF for recognizing OOVs , and a confidence-dependent word segmentation used for merging the results of both the dictionary-based and the IOB tagging . 
Detailed descriptions about sub word tagging by CRF can be found in our paper ( Zhang et al. , 2006 ) . 
A confidence measure threshold , t , was defined for making a decision based on the value . 
A confidence measure threshold , t , was defined for making a decision based on the value . 
Since it was a closed test , some information such as Arabic and Chinese number and alphabetical letters can not be used . 
Since it was a closed test , some information such as Arabic and Chinese number and alphabetical letters can not be used . 
Best 0 5 represents the best system of the Second International Chinese Word Segmentation Bakeoff on the corresponding data ; CRF + rule-system represents confidence- based combination of CRF and rule-based models , presented in Zhang et al . 
Best 0 5 represents the best system of the Second International Chinese Word Segmentation Bakeoff on the corresponding data ; CRF + rule-system represents confidence- based combination of CRF and rule-based models , presented in Zhang et al . 
For the subword-based tagging , we added another 2000 most frequent multiple- character words to the lexicons for tagging . 
In this work , we proposed a subword-based IOB tagging method for Chinese word segmentation . 
Qc 2006 Association for Computational Linguistics input åã£ +XDQJ < LQJ & KXQ OLYHV LQ % HLMLQJFLW\ Dictionary-based word segmentation å ã£ á¯¹ Ô£ à³¼ à£«Òá +XDQJ < LQJ & KXQ OLYHV LQ % HLMLQJFLW\ Subword-based IOB tagging å/ ã£ / , á¯¹/ Ô£/2 à³¼/2 % á/ +XDQJ/ % < LQJ/ , & KXQ/ , OLYHV/2 LQ/2 % HLMLQJ/ % FLW\/ , Confidence-based segmentation å/ ã£ / , á¯¹/ Ô£/2 à³¼/2 % á/ +XDQJ/ % < LQJ/ , & KXQ/ , OLYHV/2 LQ/2 % HLMLQJ/ % FLW\/ , output åã£ Ô£ à³¼ à£«Òá +XDQJ < LQJ & KXQ OLYHV LQ % HLMLQJFLW\ Figure 1 : Outline of word segmentation process data . 
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
0 means the current word ; â1 â2 the first or second word to the left ; 1 , 2 , the first or second word to the right . 
Our word segmentation process is illustrated in Fig . 
0 means the current word ; â1 â2 the first or second word to the left ; 1 , 2 , the first or second word to the right . 
Our word segmentation process is illustrated in Fig . 
Since it was a closed test , some information such as Arabic and Chinese number and alphabetical letters can not be used . 
We found a speed up both in training and test . 
For the subword-based tagging , we added another 2000 most frequent multiple- character words to the lexicons for tagging . 
It is composed of three parts : a dictionary-based N-gram word segmentation for segmenting IV words , a subword- based tagging by the CRF for recognizing OOVs , and a confidence-dependent word segmentation used for merging the results of both the dictionary-based and the IOB tagging . 
After the dictionary- based word segmentation , the words are re-segmented into sub words by FMM before being fed to IOB tagging . 
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
We proposed two approaches to improve Chinese word segmentation a subword-based tagging and a confidence measure approach.
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
We proposed two approaches to improve Chinese word segmentation a subword-based tagging and a confidence measure approach.
In this work , we proposed a subword-based IOB tagging method for Chinese word segmentation . 
We proposed two approaches to improve Chinese word segmentation a subword-based tagging and a confidence measure approach . 