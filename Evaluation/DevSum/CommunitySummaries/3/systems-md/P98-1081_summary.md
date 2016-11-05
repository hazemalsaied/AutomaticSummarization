Also of note is the improvement yielded by the best combination . 
A next step is to examine them in pairs . 
van Halteren ( ed . ) 
van Halteren 1996 ) . 
Compare this to the `` tune '' set in van Halteren , Zavrel , and Daelemans ( 1998 ) . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
This can be explained by the fact that , in general , hand crafting an explicit model is rather difficult , especially since what is being modeled natural language , is not ( yet ) well- understood . 
Data driven methods appear to be the more popular . 
Our experiment shows that , at least for the task at hand , combination of several different systems allows us to raise the performance ceiling for data driven systems . 
After comparison , their outputs are combined using several voting strategies and second stage classifiers . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
Improving Data Driven Wordclass Tagging by System Combination
The most important observation is that every combination ( significantly ) outperforms the combination of any strict subset of its components . 
the Maximum Entropy tagger ( 97.43 % ) . 
But the investigation need not be limited to word class tagging , for we expect that there are many other NLP tasks where combination could lead to worthwhile improvements . 
For our experiment , we divide the corpus into three parts . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
5 The most straightforward selection method is an n-way vote . 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 
6In our experiment , a random selection from among the winning tags is made whenever there is a tie . 
Other limiting factors are the power of the hard- and software used to implement the learning method and the availability of training material . 
A potential loophole is that each type of learning method brings its own inductive bias ' to the task and therefore different methods will tend to produce different errors . 
Of all the four systems , this one has access to the most information : contextual information ( the words and tags in a window spanning three positions before and after the focus word ) as well as lexical information ( the existence of words formed by suffix ) . 
The Viterbi algorithm is used to determine the most probable tag sequence . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
Here we use a slight adaptation of the tagger . 
As far as we know this is also one of the first rigorous measurements of the relative quality of different tagger generators , using a single tagger and dataset and identical circumstances . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
This was suspected to be the main reason for the relative lack of performance by the more sophisticated combiners . 
6 The question is how large a vote we allow each tagger . 
However , it is unlikely that we will be able to identify this 4This implies that it is impossible to note if errors counted against a tagger are in fact errors in the benchmark tagging . 
In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
Table 2 : Accuracy of individual taggers and combination methods . 
Simple Voting There are many ways in which the results of the component taggers can be combined , selecting a single tag from the set proposed by these taggers . 
the probability of each tag Tx given that the tagger suggested tag Ti . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
Where TagPair used to be significantly better than MBL , the roles are now well reversed . 
For this experiment we have selected four systems , primarily on the basis of availability . 
The corpus comprises about one million words , divided over 500 samples of 2000 words from 15 text types . 
The accuracy measurements for all of them are listed in Table 2 . 
For unknown word , the single positions before and after , three suffix letters , and information about capitalization and presence of a hyphen or a digit are used . 