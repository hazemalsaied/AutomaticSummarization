In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
A next step is to examine them in pairs . 
Improving Data Driven Wordclass Tagging by System Combination
Also of note is the improvement yielded by the best combination . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
After comparison , their outputs are combined using several voting strategies and second stage classifiers . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
5 The most straightforward selection method is an n-way vote . 
Since this model has no facilities for handling unknown words , a Memory-Based system ( see below ) is used to propose distributions of potential tags for words not in the lexicon . 
Data driven methods appear to be the more popular . 
In all Natural Language Processing ( NLP ) systems , we find one or more language models which are used to predict , classify Andros interpret language related observations . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
As it turns out all voting systems outperform the best single tagger , E. 7 Also , the best voting system is the one in which the most specific information is used , Precision-Recall . 
Pairwise Voting So far , we have only used information on the performance of individual taggers . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
The most important observation is that every combination ( significantly ) outperforms the combination of any strict subset of its components . 
Test Increase vs % Reduc- Component son Error Average Rate Best Component T 96.08 - R 96.46 M 96.95 MR 97.03 96.70+0.33 2.6 ( M ) RT 97.11 96.27+0.84 18.4 ( R ) MT 97.26 96.52+0.74 ( M ) E 97.43 MRT 97.52 96.50+1.02 18.7 ( M ) ME 97.56 97.19+0.37 5.1 ( E ) ER 97.58 96.95+0.63 5.8 ( E ) ET 97.60 96.76+0.84 6.6 ( E ) MER 97.75 96.95+0.80 12.5 ( E ) ERT 97.79 96.66+1.13 14.0 ( E ) MET 97.86 96.82+1.04 16.7 ( E ) MERT 97.92 96.73+1.19 19.1 ( E ) Table 3 : Correctness scores on Test for Pairwise Voting with all tagger combinations 7 The value of combination . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
Recent work ( e.g . Brill 1992 ) has demonstrated clearly that this categorization is in fact a mix-up of two distinct Categorization systems : on the one hand there is the representation used for the language model ( rules , Markov model , neural net , case base , etc . ) and on the other hand the manner in which the model is constructed ( hand crafted vs. data driven ) . 
The accuracy measurements for all of them are listed in Table 2 . 
This can be explained by the fact that , in general , hand crafting an explicit model is rather difficult , especially since what is being modeled natural language , is not ( yet ) well- understood . 
When a data driven method is used , a model is automatically learned from the implicit structure of an annotated training corpus . 
The Viterbi algorithm is used to determine the most probable tag sequence . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
Other limiting factors are the power of the hard- and software used to implement the learning method and the availability of training material . 
The patterns between the brackets give the distribution of incorrect tags over the systems . 
During the training phase , cases containing information about the word , the context and the correct tag are stored in memory . 
All combination taggers outperform their best component , with the best combination showing a 19.1 % lower error rate than the best individual tagger . 
Regardless of such closer investigation , we feel that our results are encouraging enough to extend our investigation of combination , starting with additional component taggers and selection strategies , and going on to shifts to other taggers languages . 
Table 2 : Accuracy of individual taggers and combination methods . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
1° Because C5.0 prunes the decision tree , the over fitting of training material ( Tune ) is less than with Memory-Based learning , but the results on Test are also worse . 
The data in Train ( for individual taggers and Tune ( for combination taggers is to be the only information used in tagger construction : all components of all taggers lexicon , context statistics , etc . ) are to be entirely data driven and no manual adjustments are to be done . 
Since the component taggers all used n-gram statistics to model context probabilities and the knowledge representation was hence fundamentally the same in each component , the results were limited . 
Here we use a slight adaptation of the tagger . 
Simple Voting There are many ways in which the results of the component taggers can be combined , selecting a single tag from the set proposed by these taggers . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
Obviously , reasonably good quality ' is not the ultimate goal . 
To examine if the overstraining effects are specific to this particular second level classifier , we also used the C5.0 system , a commercial version of the well-known program C4.5 ( Quinlan 1993 ) for the induction of decision trees , on the same training material . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
Unfortunately , the quality that can be reached for a given task is limited , and not merely by the potential of the learning method used . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 