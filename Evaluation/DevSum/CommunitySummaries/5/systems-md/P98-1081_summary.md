van Halteren ( ed . ) 
van Halteren 1996 ) . 
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
Compare this to the `` tune '' set in van Halteren , Zavrel , and Daelemans ( 1998 ) . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
Improving Data Driven Wordclass Tagging by System Combination
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
In all Natural Language Processing ( NLP ) systems , we find one or more language models which are used to predict , classify Andros interpret language related observations . 
Test Increase vs % Reduc- Component son Error Average Rate Best Component T 96.08 - R 96.46 M 96.95 MR 97.03 96.70+0.33 2.6 ( M ) RT 97.11 96.27+0.84 18.4 ( R ) MT 97.26 96.52+0.74 ( M ) E 97.43 MRT 97.52 96.50+1.02 18.7 ( M ) ME 97.56 97.19+0.37 5.1 ( E ) ER 97.58 96.95+0.63 5.8 ( E ) ET 97.60 96.76+0.84 6.6 ( E ) MER 97.75 96.95+0.80 12.5 ( E ) ERT 97.79 96.66+1.13 14.0 ( E ) MET 97.86 96.82+1.04 16.7 ( E ) MERT 97.92 96.73+1.19 19.1 ( E ) Table 3 : Correctness scores on Test for Pairwise Voting with all tagger combinations 7 The value of combination . 
In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
Recent work ( e.g . Brill 1992 ) has demonstrated clearly that this categorization is in fact a mix-up of two distinct Categorization systems : on the one hand there is the representation used for the language model ( rules , Markov model , neural net , case base , etc . ) and on the other hand the manner in which the model is constructed ( hand crafted vs. data driven ) . 
Data driven methods appear to be the more popular . 
This can be explained by the fact that , in general , hand crafting an explicit model is rather difficult , especially since what is being modeled natural language , is not ( yet ) well- understood . 
When a data driven method is used , a model is automatically learned from the implicit structure of an annotated training corpus . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
Obviously , reasonably good quality ' is not the ultimate goal . 
Stacked classifiers From the measurements so far it appears that the use of more detailed information leads to a better accuracy improvement . 
Unfortunately , the quality that can be reached for a given task is limited , and not merely by the potential of the learning method used . 
Other limiting factors are the power of the hard- and software used to implement the learning method and the availability of training material . 
Because of these limitations , we find that for most tasks we are ( at any point in time ) faced with a ceiling to the quality that can be reached with any ( then ) available machine learning system . 
However , the fact that any given system can not go beyond this ceiling does not mean that machine learning as a whole is similarly limited . 
To see whether this is in fact a good way to spend the extra data , we also trained the two best individual systems ( E and M , with exactly the same settings as in the first experiments ) on a concatenation of Train and Tune , so that they had access to every piece of data that the combination had seen . 
A potential loophole is that each type of learning method brings its own inductive bias ' to the task and therefore different methods will tend to produce different errors . 
The quality of the individual taggers cf . 
The relation between the accuracy of combinations ( using TagPair ) and that of the individual taggers is shown in Table 3 . 
It turns out that the increase in the individual taggers is quite limited when compared to combination . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
1° Because C5.0 prunes the decision tree , the over fitting of training material ( Tune ) is less than with Memory-Based learning , but the results on Test are also worse . 
To examine if the overstraining effects are specific to this particular second level classifier , we also used the C5.0 system , a commercial version of the well-known program C4.5 ( Quinlan 1993 ) for the induction of decision trees , on the same training material . 
In the machine learning literature this approach is known as ensemble , stacked , or combined classifiers . 
Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
The second part , Tune , consists of 10 % of the data ( every ninth utterance , 114479 tokens ) and is used to select the best tagger parameters where applicable and to develop the combination methods . 
As explained above , for combination to lead to improvement , the component taggers must differ in the errors that they make . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
It has been shown that , when the errors are uncorrelated to a sufficient degree , the resulting combined classifier will often perform better than all the individual systems ( Ali and Pazzani 1996 ; Chan and Stolfo 1995 ; Tumer and Gosh 1996 ) . 
The underlying assumption is twofold . 
The data we use for our experiment consists of the tagged LOB corpus ( Johansson 1986 ) . 
First , the combined votes will make the system more robust to the quirks of each learner 's particular bias . 
Also , the use of information about each individual methods 's behavior in principle even admits the possibility to fix collective errors . 