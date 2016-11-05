Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
A next step is to examine them in pairs . 
van Halteren ( ed . ) 
van Halteren 1996 ) . 
Compare this to the `` tune '' set in van Halteren , Zavrel , and Daelemans ( 1998 ) . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
After that , the decisive factor appears to be the difference in language model : T is generally a better combiner than M and R , 12 even though it has the lowest accuracy when operating alone . 
Data driven methods appear to be the more popular . 
Also of note is the improvement yielded by the best combination . 
After comparison , their outputs are combined using several voting strategies and second stage classifiers . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
Improving Data Driven Wordclass Tagging by System Combination
The most important observation is that every combination ( significantly ) outperforms the combination of any strict subset of its components . 
the Maximum Entropy tagger ( 97.43 % ) . 
For our experiment , we divide the corpus into three parts . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 
5 The most straightforward selection method is an n-way vote . 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
The Viterbi algorithm is used to determine the most probable tag sequence . 
Other limiting factors are the power of the hard- and software used to implement the learning method and the availability of training material . 
Surprisingly , none of the Memory-Based based methods reaches the quality of TagPair . 
The patterns between the brackets give the distribution of incorrect tags over the systems . 
We should rather aim for optimal selection in those cases where the correct tag is not outvoted , which would ideally lead to correct tagging of 98.21 % of the words ( in Tune ) . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
Here we use a slight adaptation of the tagger . 
However , it is unlikely that we will be able to identify this 4This implies that it is impossible to note if errors counted against a tagger are in fact errors in the benchmark tagging . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
This was suspected to be the main reason for the relative lack of performance by the more sophisticated combiners . 
The third and final part , Test , consists of the remaining 10 % ( .115101 tokens ) and is used for the final performance measurements of all taggers . 
6 The question is how large a vote we allow each tagger . 
In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
Table 2 : Accuracy of individual taggers and combination methods . 
the probability of each tag Tx given that the tagger suggested tag Ti . 
Simple Voting There are many ways in which the results of the component taggers can be combined , selecting a single tag from the set proposed by these taggers . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
Where TagPair used to be significantly better than MBL , the roles are now well reversed . 
For this experiment we have selected four systems , primarily on the basis of availability . 
Catnapping 1996 on such effects in the Penn Treebank corpus ) . 
A potential loophole is that each type of learning method brings its own inductive bias ' to the task and therefore different methods will tend to produce different errors . 
For unknown word , the single positions before and after , three suffix letters , and information about capitalization and presence of a hyphen or a digit are used . 