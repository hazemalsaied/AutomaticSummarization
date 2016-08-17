van Halteren ( ed . ) 
A next step is to examine them in pairs . 
Each of these uses different features of the text to be tagged , and each has a completely different representation of the language model . 
Pairwise Voting So far , we have only used information on the performance of individual taggers . 
5 The most straightforward selection method is an n-way vote . 
van Halteren 1996 ) . 
The accuracy measurements for all of them are listed in Table 2 . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
An example sentence tagged with the resulting tagger is : The ATI singular or plural article Lord NPT singular titular noun Major NPT singular titular noun extended VBD past tense of verb an AT singular article invitation NN singular common noun to IN preposition all ABN pre-quantifier the ATI singular or plural article parliamentary JJ adjective candidates NNS plural common noun SPER period The tagger consists of 170 different tags ( including ditto tags 3 ) and has an average ambiguity of 2.69 tags per word form . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
In the more advanced versions we also add information about the word in question ( Tags+Word ) and the tags suggested by all taggers for the previous and the next position ( Tags+Context ) . 
Stacked classifiers From the measurements so far it appears that the use of more detailed information leads to a better accuracy improvement . 
To see whether this is in fact a good way to spend the extra data , we also trained the two best individual systems ( E and M , with exactly the same settings as in the first experiments ) on a concatenation of Train and Tune , so that they had access to every piece of data that the combination had seen . 
However , specific information is not always superior , for TotPrecision scores higher than TagPrecision . 
As it turns out all voting systems outperform the best single tagger , E. 7 Also , the best voting system is the one in which the most specific information is used , Precision-Recall . 
However , the actual use of this information is severely limited in that the individual information items can only be combined according to the patterns laid down in the rule templates . 
The Viterbi algorithm is used to determine the most probable tag sequence . 
But we have even more information on how well the taggers perform . 
For the first two the similarity metric used during tagging is a straightforward overlap count ; for the third we need to use an Information Gain weighting ( Daelemans ct al . 1997 ) . 
As explained above , for combination to lead to improvement , the component taggers must differ in the errors that they make . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
After that , the decisive factor appears to be the difference in language model : T is generally a better combiner than M and R , 12 even though it has the lowest accuracy when operating alone . 
The data we use for our experiment consists of the tagged LOB corpus ( Johansson 1986 ) . 
9 The explanation for this can be found when we examine the differences within the Memory- Based general strategy : the more feature information is stored , the higher the accuracy on Tune , but the lower the accuracy on Test . 
The third systems uses Memory-Based learning as described by Daelemans et al . ( 1996 ; henceforth taggers M , for Memory ) . 