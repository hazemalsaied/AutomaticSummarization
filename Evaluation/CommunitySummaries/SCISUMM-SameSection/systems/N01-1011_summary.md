They perform a general to spec c search of a feature space , adding the most informative features to a tree structure as the search proceeds . 
The objective is to select a minimal set of features that eÆciently partitions the feature space into classes of observations and assemble them into a tree . 
A decision stump is a one node decision tree ( Holte , 1993 ) that is created by stopping the decision tree learner after the single most informative feature is added to the tree . 
A Decision Tree of Bigrams is an Accurate Predictor of Word Sense
There is a further assumption that each feature is conditionally independent of all other features , given the sense of the ambiguous word . 
It is most often used with a bag of words feature set , where every word in the training sample is represented by a binary feature that indicates whether or not it occurs in the window of context surrounding the ambiguous word . 
In general the total context available for each ambiguous word is less than 100 surrounding words . 
Decision trees are among the most widely used machine learning algorithms . 
We included all 36 tasks from SENSEVAL for which training and test data were provided . 
This paper presents a corpus-based approach to word sense disambiguation where a decision tree assigns a sense to an ambiguous word based on the bigrams that occur nearby . 