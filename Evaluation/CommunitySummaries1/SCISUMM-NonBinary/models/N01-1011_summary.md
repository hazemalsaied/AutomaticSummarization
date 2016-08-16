This paper presents a corpus-based approach to word sense disambiguation where a decision tree assigns a sense to an ambiguous word based on the bi grams that occur nearby . 
The approach in this paper relies upon a feature set made up of bi grams , two word sequences that occur in a text . 
The context in which an ambiguous word occurs is represented by some number of binary features that indicate whether or not a particular digram has occurred within approximately 50 words to the left or right of the word being disambiguated . 
Given the sparse and skewed nature of this data , the statistical methods used to select interesting bi grams must be carefully chosen . 
A number of well known statistics belong to this family , including the likelihood ratio statisticG 2 and Pearson'sX 2 statistic . 
However , ( Cressie and Read , 1984 ) suggest that there are cases where Pearson 's statistic is more reliable than the likelihood ratio and that one test should not always be preferred over the other . 
Unfortunately it is usually not clear which test is most appropriate for a particular sample of data . 
We have developed the Bigram Statistics Package to produce ranked lists of bi grams using a range of tests . 
Our empirical study utilizes the training and test data from the 1998 SENSEVAL evaluation of word sense disambiguation systems . 
Two feature sets are selected from the training data based on the top 100 ranked bi grams according to the power divergence statistic and the Dice CoeÃcient . 
While the accuracy of this approach was as good as any previously published results , the learned models were complex and diÃcult to interpret , in e ? ect acting as very accurate black boxes . 
This paper shows that the combination of a simple feature set made up of bi grams and a standard decision tree learning algorithm results in accurate word sense disambiguation . 
