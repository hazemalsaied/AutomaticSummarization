We believe that decision trees meet these criteria . 
Given the sparse and skewed nature of this data , the statistical methods used to select interesting bi grams must be carefully chosen . 
Our empirical study utilizes the training and test data from the 1998 SENSEVAL evaluation of word sense disambiguation systems . 
Decision trees have been used in supervised learning approaches to word sense disambiguation , and have fared well in a number of comparative studies ( e.g. , ( Mooney , 1996 ) , ( Pedersen and Bruce , 1997 ) ) . 
Bi grams have been used as features for word sense disambiguation , particularly in the form of collocations where the ambiguous word is one component of the digram e.g. , ( Bruce and Wiebe , 1994 ) , ( Ng and Lee , 1996 ) , ( Yarowsky , 1995 ) ) . 
Then the decision tree learning algorithm is described , as are some benchmark learning algorithms that are included for purposes of comparison . 
The Bigram Statistics Package has been implemented by Satanjeev Banerjee , who is supported by a Grant { in { Aid of Research , Artistry and Scholarship from the OÆce of the Vice President for Research and the Dean of the Graduate School of the University of Minnesota . 
The evaluation at SENSEVAL was based on precision and recall , so we converted those scores to accuracy by taking their product . 