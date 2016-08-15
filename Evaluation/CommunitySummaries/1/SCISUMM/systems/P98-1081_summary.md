Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
A next step is to examine them in pairs . 
van Halteren ( ed . ) 
van Halteren 1996 ) . 
This was suspected to be the main reason for the relative lack of performance by the more sophisticated combiners . 
Compare this to the `` tune '' set in van Halteren , Zavrel , and Daelemans ( 1998 ) . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
5 The most straightforward selection method is an n-way vote . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
Improving Data Driven Wordclass Tagging by System Combination
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
Pairwise Voting So far , we have only used information on the performance of individual taggers . 
For our experiment , we divide the corpus into three parts . 
The most important observation is that every combination ( significantly ) outperforms the combination of any strict subset of its components . 
Regardless of such closer investigation , we feel that our results are encouraging enough to extend our investigation of combination , starting with additional component taggers and selection strategies , and going on to shifts to other taggers languages . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
That this is indeed the case can be seen in Table 1 . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
To realize the benefits of stacking , either more data is needed or a second stage classifier that is better suited to this type of problem . 
The accuracy measurements for all of them are listed in Table 2 . 
1° Because C5.0 prunes the decision tree , the over fitting of training material ( Tune ) is less than with Memory-Based learning , but the results on Test are also worse . 
Our experiment shows that , at least for the task at hand , combination of several different systems allows us to raise the performance ceiling for data driven systems . 
Each tagger is allowed to vote for the tag of its choice and the tag with the highest number of votes is selected . 
Data driven methods appear to be the more popular . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
The difficulty of the tagging task can be judged by the two baseline measurements in Table 2 below , representing a completely random choice from the potential tags for each token ( Random ) and selection of the lexically most likely tag ( LexProb ) . 
The changes are mainly cosmetic , e.g . non-alphabetic characters such as `` $ '' in tag names have been replaced . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
All combination taggers outperform their best component , with the best combination showing a 19.1 % lower error rate than the best individual tagger . 
The data in Train ( for individual taggers and Tune ( for combination taggers is to be the only information used in tagger construction : all components of all taggers lexicon , context statistics , etc . ) are to be entirely data driven and no manual adjustments are to be done . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
The second part , Tune , consists of 10 % of the data ( every ninth utterance , 114479 tokens ) and is used to select the best tagger parameters where applicable and to develop the combination methods . 
The third and final part , Test , consists of the remaining 10 % ( .115101 tokens ) and is used for the final performance measurements of all taggers . 
Here we use a slight adaptation of the tagger . 
In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
the probability of each tag Tx given that the tagger suggested tag Ti . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
Where TagPair used to be significantly better than MBL , the roles are now well reversed . 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
Catnapping 1996 on such effects in the Penn Treebank corpus ) . 
7Even the worst combinator , Majority , is significantly better than E : using McNemar 's chi-square , p -- 0 . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 