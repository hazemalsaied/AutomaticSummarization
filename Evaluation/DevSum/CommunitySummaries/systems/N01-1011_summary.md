They perform a general to spec c search of a feature space , adding the most informative features to a tree structure as the search proceeds . 
The objective is to select a minimal set of features that eÆciently partitions the feature space into classes of observations and assemble them into a tree . 
A decision stump is a one node decision tree ( Holte , 1993 ) that is created by stopping the decision tree learner after the single most informative feature is added to the tree . 
Learning continues until all the training examples are accounted for by the decision tree . 
In general , such a tree will be overly spec c to the training data and not generalize well to new examples . 
Each feature selected during the search process is represented by a node in the learned decision tree . 
Column 8 shows the accuracy of the decision tree using the J48 learning algorithm and the features identify ed by a power divergence statistic . 
Column 10 shows the accuracy of the decision tree when the Dice CoeÆcient selects the features . 
The most dramatic difference occurred with amaze-v , where the SENSE- VAL average was 92.4 % and the decision tree accuracy was 58.6 % . 
A Decision Tree of Bigrams is an Accurate Predictor of Word Sense
This paper presents a corpus-based approach to word sense disambiguation where a decision tree assigns a sense to an ambiguous word based on the bigrams that occur nearby.
Word sense disambiguation is the process of selecting the most appropriate meaning for a word , based on the context in which it occurs . 
There is a further assumption that each feature is conditionally independent of all other features , given the sense of the ambiguous word . 
It is most often used with a bag of words feature set , where every word in the training sample is represented by a binary feature that indicates whether or not it occurs in the window of context surrounding the ambiguous word . 
In general the total context available for each ambiguous word is less than 100 surrounding words . 
Decision tree and decision stump learning is performed twice , once using the feature set determined by the power divergence statistic and again using the feature set identify ed by the Dice CoeÆcient . 
Decision trees are among the most widely used machine learning algorithms . 
We included all 36 tasks from SENSEVAL for which training and test data were provided . 
For example , there were two tasks associated with bet , one for its use as a noun and the other as a verb . 
For our purposes it is assumed that the set of possible meanings , i.e. , the sense inventory , has already been determined . 
For example , suppose bill has the following set of possible meanings : a piece of currency , pending legislation , or a bird jaw . 
When used in the context of The Senate bill is under consideration , a human reader immediately understands that bill is being used in the legislative Sense . 