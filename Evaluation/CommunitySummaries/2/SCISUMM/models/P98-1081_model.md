In order to see whether combination of the component taggers is likely to lead to improvements of tagging quality , we first examine the results of the individual taggers when applied to Tune . 
We accept that we are measuring quality in relation to a specific tagging 
5 The most straightforward selection method is an n-way vote . 
The most democratic option is to give each tagger one vote ( Majority ) . 
However , it appears more useful to give more weight to taggers which have proved their quality . 
This can be general quality , e.g . each tagger votes its overall precision ( TotPrecision ) , or quality in relation to the current situation , e.g . each tagger votes its precision on the suggested tag ( Tag- Precision ) . 
The information about each tagger 's quality is derived from an inspection of its results on Tune . 
Table 2 : Accuracy of individual taggers and combination methods . 
Each classier votes for its classification and every pair of classifiers votes for the sense that is most likely given the joint classification . 
A next step is to examine them in pairs . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
