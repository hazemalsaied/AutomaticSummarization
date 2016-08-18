We believe that the approach in this paper is the ? rst time that decision trees based strictly on digram features have been employed . 
The most accurate method is the decision tree based on a feature set determined by the power divergence statistic . 
A Decision Tree of Bigrams is an Accurate Predictor of Word Sense
Learning continues until all the training examples are accounted for by the decision tree . 
Each feature selected during the search process is represented by a node in the learned decision tree . 
Decision trees are among the most widely used machine learning algorithms . 
Test instances are disambiguated by ? ding a path through the learned decision tree from the root to a leaf node that corresponds with the observed features . 
Then the decision tree learning algorithm is described , as are some benchmark learning algorithms that are included for purposes of comparison . 
This paper describes an approach where a decision tree is learned from some number of sentences where each instance of an ambiguous word has been manually annotated with a sense { tag that denotes the most appropriate sense for that context . 
In light of this , ( Pedersen , 1996 ) presents Fisher 's exact test as an alternative since it does not rely on the distributional assumptions that underly both Pearson 's test and the likelihood ratio . 
Decision trees have been used in supervised learning approaches to word sense disambiguation , and have fared well in a number of comparative studies ( e.g. , ( Mooney , 1996 ) , ( Pedersen and Bruce , 1997 ) ) . 
We have presented an ensemble approach to word sense disambiguation ( Pedersen , 2000 ) where multiple Naive Bayesian class ers , each based on co { occurrence features from varying sized windows of context , is shown to perform well on the widely studied nouns interest and line . 
Word sense disambiguation is the process of selecting the most appropriate meaning for a word , based on the context in which it occurs . 
We have developed an approach to word sense disambiguation that represents text entirely in terms of the occurrence of bi grams which we de ? ne to be two cat : cat totals big n 11 = 10 n 12 = 20 n 1+ = 30 : big n 21 = 40 n 22 = 930 n 2+ = 970 totals n +1 =50 n +2 =950 n ++ =1000 Figure 1 : Representation of Bigram Counts consecutive words that occur in a text . 
These typically include the part { of { speech of surrounding words , the presence of certain key words within some window of context , and various syntactic properties of the sentence and the ambiguous word . 
In general the total context available for each ambiguous word is less than 100 surrounding words . 
The characteristics of the decision trees and decision stumps learned for each word are shown in Table 2 . 
The following process is repeated for each task . 
For example , there were two tasks associated with bet , one for its use as a noun and the other as a verb . 
A preliminary version of this paper appears in ( Pedersen , 2001 ) . 
The evaluation at SENSEVAL was based on precision and recall , so we converted those scores to accuracy by taking their product . 
The last line of Table 1 shows the win-tie-loss scores of the Decision thermopower divergence methods relative to every other methods . 