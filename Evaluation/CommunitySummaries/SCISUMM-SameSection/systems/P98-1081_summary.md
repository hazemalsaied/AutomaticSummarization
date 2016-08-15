In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
A next step is to examine them in pairs . 
Improving Data Driven Wordclass Tagging by System Combination
Also of note is the improvement yielded by the best combination . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
After comparison , their outputs are combined using several voting strategies and second stage classifiers . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
Since this model has no facilities for handling unknown words , a Memory-Based system ( see below ) is used to propose distributions of potential tags for words not in the lexicon . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
Data driven methods appear to be the more popular . 
But the investigation need not be limited to word class tagging , for we expect that there are many other NLP tasks where combination could lead to worthwhile improvements . 
As it turns out all voting systems outperform the best single tagger , E. 7 Also , the best voting system is the one in which the most specific information is used , Precision-Recall . 
Pairwise Voting So far , we have only used information on the performance of individual taggers . 
Simple Voting There are many ways in which the results of the component taggers can be combined , selecting a single tag from the set proposed by these taggers . 
Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
As explained above , for combination to lead to improvement , the component taggers must differ in the errors that they make . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
First of all , tagging is a widely researched and well-understood task ( cf . 
In all Natural Language Processing ( NLP ) systems , we find one or more language models which are used to predict , classify Andros interpret language related observations . 
Test Increase vs % Reduc- Component son Error Average Rate Best Component T 96.08 - R 96.46 M 96.95 MR 97.03 96.70+0.33 2.6 ( M ) RT 97.11 96.27+0.84 18.4 ( R ) MT 97.26 96.52+0.74 ( M ) E 97.43 MRT 97.52 96.50+1.02 18.7 ( M ) ME 97.56 97.19+0.37 5.1 ( E ) ER 97.58 96.95+0.63 5.8 ( E ) ET 97.60 96.76+0.84 6.6 ( E ) MER 97.75 96.95+0.80 12.5 ( E ) ERT 97.79 96.66+1.13 14.0 ( E ) MET 97.86 96.82+1.04 16.7 ( E ) MERT 97.92 96.73+1.19 19.1 ( E ) Table 3 : Correctness scores on Test for Pairwise Voting with all tagger combinations 7 The value of combination . 
The accuracy measurements for all of them are listed in Table 2 . 
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
The pairwise voting system , using all four individual taggers , scores 97.92 % correct on Test , a 19.1 % reduction in error rate over the best individual system , viz . 
the probability of each tag Tx given that the tagger suggested tag Ti . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
When a data driven method is used , a model is automatically learned from the implicit structure of an annotated training corpus . 
The patterns between the brackets give the distribution of incorrect tags over the systems . 
During the training phase , cases containing information about the word , the context and the correct tag are stored in memory . 
The data in Train ( for individual taggers and Tune ( for combination taggers is to be the only information used in tagger construction : all components of all taggers lexicon , context statistics , etc . ) are to be entirely data driven and no manual adjustments are to be done . 
However , it is unlikely that we will be able to identify this 4This implies that it is impossible to note if errors counted against a tagger are in fact errors in the benchmark tagging . 
Here we use a slight adaptation of the tagger . 
Recent work ( e.g . Brill 1992 ) has demonstrated clearly that this categorization is in fact a mix-up of two distinct Categorization systems : on the one hand there is the representation used for the language model ( rules , Markov model , neural net , case base , etc . ) and on the other hand the manner in which the model is constructed ( hand crafted vs. data driven ) . 
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
The second part , Tune , consists of 10 % of the data ( every ninth utterance , 114479 tokens ) and is used to select the best tagger parameters where applicable and to develop the combination methods . 
1° Because C5.0 prunes the decision tree , the over fitting of training material ( Tune ) is less than with Memory-Based learning , but the results on Test are also worse . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
Regardless of such closer investigation , we feel that our results are encouraging enough to extend our investigation of combination , starting with additional component taggers and selection strategies , and going on to shifts to other taggers languages . 
All combination taggers outperform their best component , with the best combination showing a 19.1 % lower error rate than the best individual tagger . 
In the basic version ( Tags ) , each case consists of the tags suggested by the component taggers and the correct tag . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
This can be explained by the fact that , in general , hand crafting an explicit model is rather difficult , especially since what is being modeled natural language , is not ( yet ) well- understood . 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 