van Halteren ( ed . ) 
van Halteren 1996 ) . 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
Also of note is the improvement yielded by the best combination . 
Our experiment shows that , at least for the task at hand , combination of several different systems allows us to raise the performance ceiling for data driven systems . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
It ought therefore to be advantageous to step away from the underlying mechanism of voting and to model the situations observed in Tune more closely . 
As it turns out all voting systems outperform the best single tagger , E. 7 Also , the best voting system is the one in which the most specific information is used , Precision-Recall . 
Since this model has no facilities for handling unknown words , a Memory-Based system ( see below ) is used to propose distributions of potential tags for words not in the lexicon . 
It uses a number of word and context features rather similar to system M , and trains a Maximum Entropy model that assigns a weighting parameter to each feature-value and combination of features that is relevant to the estimation of the probability P ( tag [ features ) . 
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
After that , the decisive factor appears to be the difference in language model : T is generally a better combiner than M and R , 12 even though it has the lowest accuracy when operating alone . 
In this paper , we are concerned with the question whether these differences between models can indeed be exploited to yield a data driven model with superior performance . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
This can be explained by the fact that , in general , hand crafting an explicit model is rather difficult , especially since what is being modeled natural language , is not ( yet ) well- understood . 
When a data driven method is used , a model is automatically learned from the implicit structure of an annotated training corpus . 
Since the component taggers all used n-gram statistics to model context probabilities and the knowledge representation was hence fundamentally the same in each component , the results were limited . 
In all Natural Language Processing ( NLP ) systems , we find one or more language models which are used to predict , classify Andros interpret language related observations . 
A next step is to examine them in pairs . 
Recent work ( e.g . Brill 1992 ) has demonstrated clearly that this categorization is in fact a mix-up of two distinct Categorization systems : on the one hand there is the representation used for the language model ( rules , Markov model , neural net , case base , etc . ) and on the other hand the manner in which the model is constructed ( hand crafted vs. data driven ) . 
Data driven methods appear to be the more popular . 
Other limiting factors are the power of the hard- and software used to implement the learning method and the availability of training material . 
A potential loophole is that each type of learning method brings its own inductive bias ' to the task and therefore different methods will tend to produce different errors . 
Stacked classifiers From the measurements so far it appears that the use of more detailed information leads to a better accuracy improvement . 
The accuracy measurements for all of them are listed in Table 2 . 
First , the combined votes will make the system more robust to the quirks of each learner 's particular bias . 
6 The question is how large a vote we allow each tagger . 
Test Increase vs % Reduc- Component son Error Average Rate Best Component T 96.08 - R 96.46 M 96.95 MR 97.03 96.70+0.33 2.6 ( M ) RT 97.11 96.27+0.84 18.4 ( R ) MT 97.26 96.52+0.74 ( M ) E 97.43 MRT 97.52 96.50+1.02 18.7 ( M ) ME 97.56 97.19+0.37 5.1 ( E ) ER 97.58 96.95+0.63 5.8 ( E ) ET 97.60 96.76+0.84 6.6 ( E ) MER 97.75 96.95+0.80 12.5 ( E ) ERT 97.79 96.66+1.13 14.0 ( E ) MET 97.86 96.82+1.04 16.7 ( E ) MERT 97.92 96.73+1.19 19.1 ( E ) Table 3 : Correctness scores on Test for Pairwise Voting with all tagger combinations 7 The value of combination . 
Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
The first part , called Train , consists of 80 % of the data ( 931062 tokens ) , constructed 3Ditto tags are used for the components of multi- token units , e.g . if `` as well as '' is taken to be a coordination conjunction , it is tagged `` as_CC1 well_CC2 as_CC3 '' , using three related but different ditto tags . 
In the basic version ( Tags ) , each case consists of the tags suggested by the component taggers and the correct tag . 
Its tagging , which was manually checked and corrected , is generally accepted to be quite accurate . 
First of all , tagging is a widely researched and well-understood task ( cf . 
The pairwise voting system , using all four individual taggers , scores 97.92 % correct on Test , a 19.1 % reduction in error rate over the best individual system , viz . 
Pairwise Voting So far , we have only used information on the performance of individual taggers . 
Simple Voting There are many ways in which the results of the component taggers can be combined , selecting a single tag from the set proposed by these taggers . 
The most democratic option is to give each tagger one vote ( Majority ) . 
5 The most straightforward selection method is an n-way vote . 
9 The explanation for this can be found when we examine the differences within the Memory- Based general strategy : the more feature information is stored , the higher the accuracy on Tune , but the lower the accuracy on Test . 
Unfortunately , the quality that can be reached for a given task is limited , and not merely by the potential of the learning method used . 
Also , the use of information about each individual method 's behavior in principle even admits the possibility to fix collective errors . 
To see whether this is in fact a good way to spend the extra data , we also trained the two best individual systems ( E and M , with exactly the same settings as in the first experiments ) on a concatenation of Train and Tune , so that they had access to every piece of data that the combination had seen . 
It has been shown that , when the errors are uncorrelated to a sufficient degree , the resulting combined classifier will often perform better than all the individual systems ( Ali and Pazzani 1996 ; Chan and Stolfo 1995 ; Tumer and Gosh 1996 ) . 
The quality of the individual taggers cf . 
The relation between the accuracy of combinations ( using TagPair ) and that of the individual taggers is shown in Table 3 . 
It turns out that the increase in the individual taggers is quite limited when compared to combination . 
If a tag pair T1T2 has never been observed in Tune , we fall back on information on the individual taggers , viz . 
Table 2 : Accuracy of individual taggers and combination methods . 
The data in Train ( for individual taggers and Tune ( for combination taggers is to be the only information used in tagger construction : all components of all taggers lexicon , context statistics , etc . ) are to be entirely data driven and no manual adjustments are to be done . 
In order to see whether combination of the component taggers is likely to lead to improvements of tagging quality , we first examine the results of the individual taggers when applied to Tune . 
As far as we know this is also one of the first rigorous measurements of the relative quality of different tagger generators , using a single tagger and dataset and identical circumstances . 
the Maximum Entropy tagger ( 97.43 % ) . 
Here we use a slight adaptation of the tagger . 
But we have even more information on how well the taggers perform . 
However , it appears more useful to give more weight to taggers which have proved their quality . 
All Taggers Correct 92.49 Majority Correct ( 31,211 ) 4.34 Correct Present , No Majority 1.37 ( 22,1111 ) Minority Correct ( 13,121 ) 1.01 All Taggers Wrong 0.78 Table 1 : Tagger agreement on Tune . 
The information about each tagger 's quality is derived from an inspection of its results on Tune . 
The fourth and final system is the MXPOST system as described by Ratnaparkhi ( 19962 ; henceforth tagger E , for Entropy ) . 
1° Because C5.0 prunes the decision tree , the over fitting of training material ( Tune ) is less than with Memory-Based learning , but the results on Test are also worse . 
To examine if the overstraining effects are specific to this particular second level classifier , we also used the C5.0 system , a commercial version of the well-known program C4.5 ( Quinlan 1993 ) for the induction of decision trees , on the same training material . 
The reasons for this choice are several . 
This might be explained by the fact that recall information is missing ( for overall performance this does not matter , since recall is equal to precision ) . 
The third and final part , Test , consists of the remaining 10 % ( .115101 tokens ) and is used for the final performance measurements of all taggers . 
Second , current performance levels on this task still leave room for improvement : state of the art ' performance for data driven automatic word class taggers ( tagging English text with single tags from a low detail tagger is 9697 % correctly tagged words . 
The first and oldest system uses a traditional trig-ram model ( Steetskamp 1995 ; henceforth tagger T , for Trigrams ) , based on context statistics P ( ti [ ti-l , ti-2 ) and lexical statistics P ( Tildi directly estimated from relative corpus frequencies . 
The second part , Tune , consists of 10 % of the data ( every ninth utterance , 114479 tokens ) and is used to select the best tagger parameters where applicable and to develop the combination methods . 
As explained above , for combination to lead to improvement , the component taggers must differ in the errors that they make . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
Regardless of such closer investigation , we feel that our results are encouraging enough to extend our investigation of combination , starting with additional component taggers and selection strategies , and going on to shifts to other taggers languages . 
Note that with this method ( and those in the next section ) a tag suggested by a minority ( or even none ) of the taggers still has a chance to win . 
This information can be used by forcing each tagger also to add to the vote for tags suggested by the opposition , by an amount equal to 1 minus the recall on the opposing tag ( Precision-Recall ) . 
In the more advanced versions we also add information about the word in question ( Tags+Word ) and the tags suggested by all taggers for the previous and the next position ( Tags+Context ) . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
9Tags ( Memory-Based ) scores significantly worse than TagPair ( p=0.0274 and not significantly better than Precision-Recall ( p=0.2766 . 
7Even the worst combinator , Majority , is significantly better than E : using McNemar 's chi-square , p -- 0 . 
12Although not significantly better , e.g . the differences within the group ME/ER/ET are not significant . 
The practice of feeding the outputs of a number of classifiers as features for a next learner sit is significantly better than the runner-up ( Precision-Recall ) with p=0 . 
We accept that we are measuring quality in relation to a specific Tagging rather than the linguistic truth ( if such exists ) and can only hope the tagged LOB corpus lives up to its reputation . 