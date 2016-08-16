Also of note is the improvement yielded by the best combination . 
A next step is to examine them in pairs . 
van Halteren ( ed . ) 
van Halteren 1996 ) . 
This was suspected to be the main reason for the relative lack of performance by the more sophisticated combiners . 
Compare this to the `` tune '' set in van Halteren , Zavrel , and Daelemans ( 1998 ) . 
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
5 The most straightforward selection method is an n-way vote . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
Improving Data Driven Wordclass Tagging by System Combination
After comparison , their outputs are combined using several voting strategies and second stage classifiers . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
For our experiment , we divide the corpus into three parts . 
The most important observation is that every combination ( significantly ) outperforms the combination of any strict subset of its components . 
the Maximum Entropy tagger ( 97.43 % ) . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
First of all , tagging is a widely researched and well-understood task ( cf . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
To realize the benefits of stacking , either more data is needed or a second stage classifier that is better suited to this type of problem . 
The accuracy measurements for all of them are listed in Table 2 . 
Our experiment shows that , at least for the task at hand , combination of several different systems allows us to raise the performance ceiling for data driven systems . 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
6In our experiment , a random selection from among the winning tags is made whenever there is a tie . 
Data driven methods appear to be the more popular . 
Other limiting factors are the power of the hard- and software used to implement the learning method and the availability of training material . 
The patterns between the brackets give the distribution of incorrect tags over the systems . 
During the training phase , cases containing information about the word , the context and the correct tag are stored in memory . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
Here we use a slight adaptation of the tagger . 
All combination taggers outperform their best component , with the best combination showing a 19.1 % lower error rate than the best individual tagger . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
The third and final part , Test , consists of the remaining 10 % ( .115101 tokens ) and is used for the final performance measurements of all taggers . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
The data in Train ( for individual taggers and Tune ( for combination taggers is to be the only information used in tagger construction : all components of all taggers lexicon , context statistics , etc . ) are to be entirely data driven and no manual adjustments are to be done . 
The Viterbi algorithm is used to determine the most probable tag sequence . 
A beam search is then used to find the highest probability tag sequence . 
The changes are mainly cosmetic , e.g . non-alphabetic characters such as `` $ '' in tag names have been replaced . 
Where TagPair used to be significantly better than MBL , the roles are now well reversed . 
For this experiment we have selected four systems , primarily on the basis of availability . 
Catnapping 1996 on such effects in the Penn Treebank corpus ) . 
Table 2 : Accuracy of individual taggers and combination methods . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 