Decision trees have been used in supervised learning approaches to word sense disambiguation , and have fared well in a number of comparative studies ( e.g. , ( Mooney , 1996 ) , ( Pedersen and Bruce , 1997 ) ) . 
We have presented an ensemble approach to word sense disambiguation ( Pedersen , 2000 ) where multiple Naive Bayesian class ers , each based on co { occurrence features from varying sized windows of context , is shown to perform well on the widely studied nouns interest and line . 
In light of this , ( Pedersen , 1996 ) presents Fisher 's exact test as an alternative since it does not rely on the distributional assumptions that underly both Pearson 's test and the likelihood ratio . 
A preliminary version of this paper appears in ( Pedersen , 2001 ) . 
There is no search of the feature space performed to build a representative model as is the case with decision trees . 
Learning continues until all the training examples are accounted for by the decision tree . 
Column 10 shows the accuracy of the decision tree when the Dice CoeÆcient selects the features . 
Column 8 shows the accuracy of the decision tree using the J48 learning algorithm and the features identify ed by a power divergence statistic . 
The most dramatic difference occurred with amaze-v , where the SENSE- VAL average was 92.4 % and the decision tree accuracy was 58.6 % . 
The last line of Table 1 shows the win-tie-loss score of the decision thermopower divergence method relative to every other method . 
Given the sparse and skewed nature of this data , the statistical methods used to select interesting bi grams must be carefully chosen . 
We employ a ? ne grained scoring method , where a word is counted as correctly disambiguated only when the assigned sense tag exactly matches the true sense tag . 
Each sense { tagged occurrence of an ambiguous word is converted into a feature vector , where each feature represents some property of the surrounding text that is considered to be relevant to the disambiguation process . 
One of our long-term objectives is to identify a core set of features that will be useful for disambiguating a wide class of words using both supervised and unsupervised methodologies . 
These typically include the part { of { speech of surrounding words , the presence of certain key words within some window of context , and various syntactic properties of the sentence and the ambiguous word . 
It is not clear how much disambiguation accuracy is improved through the use of features that are identify ed by more complex pre { processing such as part { of { speech tagging , parsing , or anaphora resolution . 
Then the decision tree learning algorithm is described , as are some benchmark learning algorithms that are included for purposes of comparison . 
The following process is repeated for each task . 
The number of test and training instances for each task are shown in columns 2 and 4 . 
The evaluation at SENSEVAL was based on precision and recall , so we converted those scores to accuracy by taking their product . 