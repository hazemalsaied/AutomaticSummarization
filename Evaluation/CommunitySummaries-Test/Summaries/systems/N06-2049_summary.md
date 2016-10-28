2 Table 5 Segmentation performance presented in previous work and of our combination model . 
Table 1 shows the performance of the dictionary-based segmentation . 
CRF + Rule system represents a combination of CRF model and rule based model presented in Zhang et al . 
Best 0 5 represents the best system of the Second International Chinese Word Segmentation Bakeoff on the corresponding data ; CRF + rule-system represents confidence- based combination of CRF and rule-based models , presented in Zhang et al . 
A confidence measure threshold , t , was defined for making a decision based on the value . 
Using the CRFs approaches , we prove that it outperformed the character- based method using the CRF approaches . 
In addition , we found a clear weakness with the IOB tagging approach : It yields a very low in-vocabulary ( IV ) rate ( R-iv ) in return for a higher out-of-vocabulary ( OOV ) rate ( R-oov ) . 
The effect of the confidence measure is shown in Table 3 , where we used Î± = 0.7 and confidence threshold t = 0.8 . 
Our results are listed together with the best results from Bakeoff 2005 in Table 4 in terms of F-scores . 
We found the former achieved better performance than the existing character-based tagging, and the latter improved segmentation further by combining the former with a dictionary-based segmentation.
using the FMM , and then labeled with âIOBâ tags by the CRFs . 
For example , inconsistent errors of foreign names can be fixed if alphabetical characters are known . 
0 means the current word ; â1 â2 the first or second word to the left ; 1 , 2 , the first or second word to the right . 
It is composed of three parts : a dictionary-based N-gram word segmentation for segmenting IV words , a subword- based tagging by the CRF for recognizing OOVs , and a confidence-dependent word segmentation used for merging the results of both the dictionary-based and the IOB tagging . 
After the dictionary- based word segmentation , the words are re-segmented into sub words by FMM before being fed to IOB tagging . 
It was first used in Chinese word segmentation by ( Xue and Shen , 2003 ) , where maximum entropy methods were used . 
Since it was a closed test , some information such as Arabic and Chinese number and alphabetical letters can not be used . 
Our word segmentation process is illustrated in Fig . 
Detailed descriptions about sub word tagging by CRF can be found in our paper ( Zhang et al. , 2006 ) . 
The confidence measure comes from two sources : IOB tagging and dictionary- based word segmentation . 
The upper numbers are of the character- based and the lower ones , the subword-based . 
We found a speed up both in training and test . 
Note a lexicon and a LM are the only needed resources for building a dictionary-based CWS , like the Ã¢â¬Ådict-hybrid.Ã¢â¬Â ( Zhang et al. , 2006 ) We used the Ã¢â¬Ådict-hybridÃ¢â¬Â to segment the SMT training corpus and test data . 
Section 4 describes current state- of-the-art methods for Chinese word segmentation , with which our results were compared . 
The character-based âIOBâ tagging approach has been widely used in Chinese word segmentation recently ( Xue and Shen , 2003 ; Peng and McCallum , 2004 ; Tseng et al. , 2005 ) . 
For the subword-based tagging , we added another 2000 most frequent multiple- character words to the lexicons for tagging . 
In this work , we proposed a subword-based IOB tagging method for Chinese word segmentation . 
Qc 2006 Association for Computational Linguistics input åã£ +XDQJ < LQJ & KXQ OLYHV LQ % HLMLQJFLW\ Dictionary-based word segmentation å ã£ á¯¹ Ô£ à³¼ à£«Òá +XDQJ < LQJ & KXQ OLYHV LQ % HLMLQJFLW\ Subword-based IOB tagging å/ ã£ / , á¯¹/ Ô£/2 à³¼/2 % á/ +XDQJ/ % < LQJ/ , & KXQ/ , OLYHV/2 LQ/2 % HLMLQJ/ % FLW\/ , Confidence-based segmentation å/ ã£ / , á¯¹/ Ô£/2 à³¼/2 % á/ +XDQJ/ % < LQJ/ , & KXQ/ , OLYHV/2 LQ/2 % HLMLQJ/ % FLW\/ , output åã£ Ô£ à³¼ à£«Òá +XDQJ < LQJ & KXQ OLYHV LQ % HLMLQJFLW\ Figure 1 : Outline of word segmentation process data . 
Subword-based Tagging by Conditional Random Fields for Chinese Word Segmentation
2.2 Confidence-dependent word segmentation . 
While OOV recognition is very important in word segmentation , a higher IV rate is also desired . 
In the followings , we illustrate our word segmentation process in Section 2 , where the subword-based tagging is implemented by the CRFs method . 
First , we extracted a word list from the training data sorted in decreasing order by their counts in the training 193 Proceedings of the Human Language Technology Conference of the North American Chapter of the ACL , pages 193â196 New York , June 2006 . 
We chose the three models that achieved at least one best score in the closed tests from Emerson ( 2005 ) , as well as the sub-word-based model of Zhang et al . 
We chose the three models that achieved at least one best score in the closed tests from Emerson ( 2005 ) , as well as the sub-word-based model of Zhang , Kikui , and Sumita ( 2006 ) for comparison . 
For the character-based tagging , we used all the Chinese characters . 
We regard the words in the subset as the sub words for the IOB tagging . 
Since this work was to evaluate the proposed subword-based IOB tagging , we carried out the closed test only . 
We proposed two approaches to improve Chinese word segmentation a subword-based tagging and a confidence measure approach.
We proposed two approaches to improve Chinese word segmentation : a subword-based tagging and a confidence measure approach . 
In addition, the latter can be used to balance out-of-vocabulary rates and in-vocabulary rates.
Under the scheme , each character of a word is labeled as âBâ if it is the first character of a multiple-character word , or âOâ if the character functions as an independent word , or âIâ otherwise For example , â ( whole ) ( Beijing city ) â is labeled as â ( whole ) /O ( north ) /B ( capital ) /I ( city ) /Iâ . 
We found that so far all the existing implementations were using character-based IOB tagging . 
In this work we propose a subword-based IOB tagging , which assigns tags to a predefined lexicon subset consisting of the most frequent multiple-character words in addition to single Chinese characters . 
If only Chinese characters are used , the subword-based IOB tagging is downgraded into a character-based one . 
Taking the same example mentioned above , â ( whole ) ( Beijing city ) â is labeled as â ( whole ) /O ( Beijing ) /B ( city ) /Iâ in the Subword-based Tagging , where â ( Beijing ) /Bâ is labeled as one unit . 