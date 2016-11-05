( Stolcke et al. , 2000 ) use HMMs for dialogue modelling , where sequences of observations correspond to sequences of dialog act types . 
It maximizes the probability of getting the entire DA sequence correct , but it does not necessarily find the DA sequence that has the most DA labels correct ( Dermatas and Kokkinakis 1995 ) . 
To date , the majority of work on dialog act modeling has addressed spoken dialogue ( Samuel et al. , 1998 ; Stolcke et al. , 2000 ; Surendran and Levow , 2006 ; Bangalore et al. , 2008 ; Sridhar et al. , 2009 ; Di Eugenio et al. , 2010 ) . 
A more efficient , though mathematically less accurate , solution can be obtained by combining guesses about the correct DA types directly at the level of the LM . 
We have developed an integrated probabilistic approach to dialog act modeling for conversational speech , and tested it on a large speech corpus . 
The relation between utterances and speaker turns is not one-to-one : a single turn can contain multiple utterances , and utterances can span more than one turn ( e.g. , in the case of channeling by the other speaker in utterance . 
A back channel is a short utterance that plays discourse-structuring roles , e.g. , indicating that the speaker should go on talking . 
Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech
Dialog act ( DA ) annotations and tagging , inspired by the speech act theory of Austin ( 1975 ) and Searle ( 1976 ) , have been used in the NLP community to understand and model dialog . 
We trained standard back off models ( Katz 1987 ) , using the frequency smoothing approach of Witten and Bell ( 1991 ) . 
Conversational feedback is mostly performance short utterances such as yeah , mh , okay produced by the main speaker but by one of the other participants of a conversation . 
The relatively small improvements from higher-order models could be a result of lack of training data , or of an inherent independence of DAs from DAs further removed . 
Such utterances are among the most frequent in conversational data ( Stolcke et al. , 2000 ) . 
By representing a higher level intention of utterance human conversation , dialog act labels are being used to enrich the information provided spoken words ( Stolcke et al. , 2000 ) . 
The problem with applying Equation 11 , of course , is that the DA type Ui is generally not known ( except maybe in applications where the user interface can be engineered to allow only one kind of DA for a given utterance ) . 
This leads to the following formulation : W~ = argmaxP ( WilAi , E ) wi -- -- argument P ( WilAi , Ui , E ) P ( UilE ) Wi Ui argument [ ] P ( WiiAi , Ui ) P ( Ui [ E ) ( 12 ) W~ U~ The last step in Equation 12 is justified because , as shown in Figure 1 and 4 , the evidence E ( acoustic , prosody , words ) pertaining to utterance other than i can affect the current utterance only through its DA types Ui . 