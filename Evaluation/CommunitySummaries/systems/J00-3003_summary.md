( Stolcke et al. , 2000 ) use HMMs for dialogue modelling , where sequences of observations correspond to sequences of dialog act types . 
It maximizes the probability of getting the entire DA sequence correct , but it does not necessarily find the DA sequence that has the most DA labels correct ( Dermatas and Kokkinakis 1995 ) . 
Applying Bayes ' rule we get U* = argmaxP ( UIE ) U P ( U ) P ( ElU ) = argument u P ( E ) = argmaxP ( U ) P ( ElU ) ( 1 ) U Here P ( U ) represents the prior probability of a DA sequence , and P ( EIU ) is the like- Table 4 Summary of random variables used in dialog modeling . 
As described later , this involves considering multiple alternative recognized word sequences . 
To make both the modeling and the search for the best DA sequence feasible , we further require that our likelihood models are decomposable by utterance . 
Returning to the prior distribution of DA sequences P ( U ) , it is convenient to make certain independence assumptions here , too . 
When applied to a discourse model with locally decomposable likelihoods and Markovian discourse grammar , it will therefore find precisely the DA sequence with the highest posterior probability : U* = argmaxP ( UIE ) ( 4 ) u The combination of likelihood and prior modeling , HMMs , and Viterbi decoding is fundamentally the same as the standard probabilistic approaches to speech recognition ( Bahl , Jelinek , and Mercer 1983 ) and tagging ( Church 1988 ) . 
Constraints on the likely sequence of dialog acts are modeled via a dialog act n-gram . 
To date , the majority of work on dialog act modeling has addressed spoken dialogue ( Samuel et al. , 1998 ; Stolcke et al. , 2000 ; Surendran and Levow , 2006 ; Bangalore et al. , 2008 ; Sridhar et al. , 2009 ; Di Eugenio et al. , 2010 ) . 
Initial work was done unspoken interactions ( see for example ( Stolcke et al.,2000 ) ) . 
A more efficient , though mathematically less accurate , solution can be obtained by combining guesses about the correct DA types directly at the level of the LM . 
The problem with applying Equation 11 , of course , is that the DA type Ui is generally not known ( except maybe in applications where the user interface can be engineered to allow only one kind of DA for a given utterance ) . 
We have developed an integrated probabilistic approach to dialog act modeling for conversational speech , and tested it on a large speech corpus . 
We develop a probabilistic integration of speech recognition with dialog modeling , to improve both speech recognition and dialog act classification accuracy . 
The relation between utterances and speaker turns is not one-to-one : a single turn can contain multiple utterances , and utterances can span more than one turn ( e.g. , in the case of channeling by the other speaker in utterance . 
A back channel is a short utterance that plays discourse-structuring roles , e.g. , indicating that the speaker should go on talking . 
We expect recognition of channels to be useful because of their discourse-structuring role ( knowing that the hearer expects the speaker to go on talking tells us something about the course of the narrative ) and because they seem to occur at certain kinds of syntactic boundaries ; detecting a back channel may thus help in predicting utterance boundaries and surrounding lexical material . 
The following table shows examples of channels in the context of a Switchboard conversation : Speaker Dialogue Act Utterance B STATEMENT but , uh , we 're to the point now where our financial income is enough that we can consider putting some away - A BACKCHANNEL Uh-huh . 
Therefore , we need to infer the likely DA types for each utterance , using available evidence E from the entire conversation . 
Woszczyna and Waibel ( 1994 ) , for example , trained an ergodic HMM using expectation-maximization to model speech act sequencing . 
DA modeling has mostly been geared toward automatic DA classification , and much less work has been done on applying DA models to automatic speech recognition . 
In related work DAs are used as a first processing step to infer dialog games ( Carlson 1983 ; Levin and Moore 1977 ; Levin et al . 1999 ) , a slightly higher level unit that comprises a small number of DAs . 
1 % What did you wear to work today ? 
Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech
Conversational feedback is mostly performance short utterances such as yeah , mh , okay produced by the main speaker but by one of the other participants of a conversation . 
Such utterances are among the most frequent in conversational data ( Stolcke et al. , 2000 ) . 
We trained standard back off models ( Katz 1987 ) , using the frequency smoothing approach of Witten and Bell ( 1991 ) . 
The relatively small improvements from higher-order models could be a result of lack of training data , or of an inherent independence of DAs from DAs further removed . 
However , this does not seem to be true for DA sequences in our corpus , as the cache model showed no improvement over the standard N-gram . 
By representing a higher level intention of utterance human conversation , dialog act labels are being used to enrich the information provided spoken words ( Stolcke et al. , 2000 ) . 
They also explore the performance with decision trees and neural networks and report their highest accuracy at 65 % on the Switchboard corpus . 
Dialog act ( DA ) annotations and tagging , inspired by the speech act theory of Austin ( 1975 ) and Searle ( 1976 ) , have been used in the NLP community to understand and model dialog . 
The ability to model and automatically detect discourse structure is an important step toward understanding spontaneous dialog . 
While there is hardly consensus on exactly how discourse structure should be described , some agreement exists that a useful first level of analysis involves the identification of dialog acts ( DAs ) . 
A DA represents the meaning of an utterance at the level of elocutionary force ( Austin 1962 ) . 
To train our statistical models on this corpus , we combined an extensive effort in human hand-coding of DAs for each utterance , with a variety of automatic and semiautomatic tools . 
2.1 Utterance Segmentation . 
We refer to the units of this segmentation as utterances . 
In an automatic labeling of word boundaries as either utterance or boundaries using a combination of lexical and prosodic cues , we obtained 96 % accuracy based on correct word transcripts , and 78 % accuracy with automatically recognized words . 
A total of 1,155 Switchboard conversation were labeled , comprising 205,000 utterance and 1.4 million words . 