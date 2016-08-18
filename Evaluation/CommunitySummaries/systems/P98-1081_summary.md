van Halteren ( ed . ) 
The most important result that has undergone a change between van Halteren , Zavrel , and Daelemans ( 1998 ) and our current experiments is the relative accuracy of TagPair and stacked systems such as MBL . 
van Halteren 1996 ) . 
In van Halteren , Zavrel , and Daelemans ( 1998 ) we used a straightforward imÂ­ implementation of HMM 's , which turned out to have the worst accuracy of the four competing methods . 
As we now apply the methods of van Halteren , Zavrel , and Daelemans ( 1998 ) to WSJ as well , it is easier to make a comparison . 
Compare this to the `` tune '' set in van Halteren , Zavrel , and Daelemans ( 1998 ) . 
The first is the LOB corpus ( Johansson 1986 ) , which we used in the earlier experiments as well ( van Halteren , Zavrel , and Daelemans 1998 ) and which has proved to be a good testing ground . 
Traditionally , these models were categorized as either rule-based/symbolic or corpus-based/probabilistic . 
This is much easier and can quickly lead to a model which produces results with a reasonably good quality . 
A next step is to examine them in pairs . 
When a data driven method is used , a model is automatically learned from the implicit structure of an annotated training corpus . 
Since this model has no facilities for handling unknown words , a Memory-Based system ( see below ) is used to propose distributions of potential tags for words not in the lexicon . 
Improving Data Driven Wordclass Tagging by System Combination
With LOB and a single 114K tune set ( van Halteren , Zavrel , and Daelemans 1998 ) , both MBL and Decision Trees degraded significantly when adding context , and MBL degraded when adding the word 
Component taggers In 1992 , van Halteren combined a number of taggers by way of a straightforward majority vote ( cf . 
When used on Test , the pairwise voting strategy ( TagPair ) clearly outperforms the other voting strategies , 8 but does not yet approach the level where all tying majority votes are handled correctly ( 98.31 % ) . 
For our experiment , we divide the corpus into three parts . 
Four well-known tagger generators (Hidden Markov Model, Memory-Based, Transformation Rules and Maximum Entropy) are trained on the same corpus data.
For part-of-speech tagging , a significant increase in accuracy through combining the output of different taggers was first demonstrated in van Halteren , Zavrel , and Daelemans ( 1998 ) and Brill and Wu ( 1998 ) . 
The second system is the Transformation Based Learning system as described by Brill ( 19941 ; henceforth tagger R , for Rules ) . 
That this is indeed the case can be seen in Table 1 . 
After comparison, their outputs are combined using several voting strategies and second stage classifiers.
After comparison , their outputs are combined using several voting strategies and second stage classifiers . 
When combining the taggers , every tagger pair is taken in turn and allowed to vote ( with the probability described above ) for each possible tag , i.e . not just the ones suggested by the component taggers . 
Stacked classifiers From the measurements so far it appears that the use of more detailed information leads to a better accuracy improvement . 
We will execute our investigation by means of an experiment . 
The practice of feeding the outputs of a number of classifiers as features for a next learner sit is significantly better than the runner-up ( Precision-Recall ) with p=0 . 
Finally , a number of rather different methods are available that generate a fully functional tagging system from annotated text . 
Note that with this method ( and those in the next section ) a tag suggested by a minority ( or even none ) of the taggers still has a chance to win . 
It has been shown that , when the errors are uncorrelated to a sufficient degree , the resulting combined classifier will often perform better than all the individual systems ( Ali and Pazzani 1996 ; Chan and Stolfo 1995 ; Tumer and Gosh 1996 ) . 
In all Natural Language Processing ( NLP ) systems , we find one or more language models which are used to predict , classify Andros interpret language related observations . 
The quality of the individual taggers cf . 
Here we use a slight adaptation of the tagger . 
Table 2 : Accuracy of individual taggers and combination methods . 
Recent work ( e.g . Brill 1992 ) has demonstrated clearly that this categorization is in fact a mix-up of two distinct Categorization systems : on the one hand there is the representation used for the language model ( rules , Markov model , neural net , case base , etc . ) and on the other hand the manner in which the model is constructed ( hand crafted vs. data driven ) . 
tokens , but , because of a 92.5 % agreement over all four taggers , it yielded less than 9K tokens of useful training material to resolve disagreements . 
This was suspected to be the main reason for the relative lack of performance by the more sophisticated combiners . 
Both Tune and Test contain around 2.5 % new tokens ( wrt Train ) and a further 0.2 % known tokens with new tags . 
However , it appears more useful to give more weight to taggers which have proved their quality . 
In both approaches , different tagger genÂ­ aerators were applied to the same training data and their predictions combined using different combination methods , including stacking . 
Obviously there is still room for a closer examination of the differences between the combination methods , e.g . the question whether Memory-Based combination would have performed better if we had provided more training data than just Tune , and of the remaining errors , e.g . the effects of inconsistency in the data ( cf . 
Simple Voting There are many ways in which the results of the component taggers can be combined , selecting a single tag from the set proposed by these taggers . 
Since the component taggers all used n-gram statistics to model context probabilities and the knowledge representation was hence fundamentally the same in each component , the results were limited . 
We can investigate all situations where one tagger suggests T1 and the other T2 and estimate the probability that in this situation the tag should actually be Tx . 
Where TagPair used to be significantly better than MBL , the roles are now well reversed . 
12Although not significantly better , e.g . the differences within the group ME/ER/ET are not significant . 
The data we use for our experiment consists of the tagged LOB corpus ( Johansson 1986 ) . 
For the first two the similarity metric used during tagging is a straightforward overlap count ; for the third we need to use an Information Gain weighting ( Daelemans ct al . 1997 ) . 
We do this by means of an experiment involving the task of morpho-syntactic word class tagging . 