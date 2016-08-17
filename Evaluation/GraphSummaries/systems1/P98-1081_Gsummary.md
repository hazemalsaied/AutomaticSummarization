Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
A next step is to examine them in pairs . 
Table 2 : Accuracy of individual taggers and combination methods . 
van Halteren ( ed . ) 
5 The most straightforward selection method is an n-way vote . 
The relation between the accuracy of combinations ( using TagPair ) and that of the individual taggers is shown in Table 3 . 
In the machine learning literature this approach is known as ensemble , stacked , or combined classifiers . 
van Halteren 1996 ) . 
Improving Data Driven Wordclass Tagging by System Combination
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
The accuracy measurements for all of them are listed in Table 2 . 
Our experiment shows that , at least for the task at hand , combination of several different systems allows us to raise the performance ceiling for data driven systems . 
To see whether this is in fact a good way to spend the extra data , we also trained the two best individual systems ( E and M , with exactly the same settings as in the first experiments ) on a concatenation of Train and Tune , so that they had access to every piece of data that the combination had seen . 
The practice of feeding the outputs of a number of classifiers as features for a next learner sit is significantly better than the runner-up ( Precision-Recall ) with p=0 . 
The Viterbi algorithm is used to determine the most probable tag sequence . 
During the training phase , cases containing information about the word , the context and the correct tag are stored in memory . 
In the more advanced versions we also add information about the word in question ( Tags+Word ) and the tags suggested by all taggers for the previous and the next position ( Tags+Context ) . 
Both Tune and Test contain around 2.5 % new tokens ( wrt Train ) and a further 0.2 % known tokens with new tags . 
Unfortunately , the quality that can be reached for a given task is limited , and not merely by the potential of the learning method used . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
Z. system starts with a basic corpus annotation ( each word is tagged with its most likely tag ) and then searches through a space of transformation rules in order to reduce the discrepancy between its current annotation and the correct one ( in our case 528 rules were learned ) . 
The data we use for our experiment consists of the tagged LOB corpus ( Johansson 1986 ) . 
2Ratnaparkhi 's Java implementation of this system is available at ftp : //ftp.cis.upenn.edu/ 
It ought therefore to be advantageous to step away from the underlying mechanism of Voting and to models the situations observed in Tune more closely . 