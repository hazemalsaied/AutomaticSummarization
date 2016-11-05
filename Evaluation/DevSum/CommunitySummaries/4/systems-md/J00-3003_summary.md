( Stolcke et al. , 2000 ) use HMMs for dialogue modelling , where sequences of observations correspond to sequences of dialog act types . 
They also explore the performance with decision trees and neural networks and report their highest accuracy at 65 % on the Switchboard corpus . 
To date , the majority of work on dialog act modeling has addressed spoken dialogue ( Samuel et al. , 1998 ; Stolcke et al. , 2000 ; Surendran and Levow , 2006 ; Bangalore et al. , 2008 ; Sridhar et al. , 2009 ; Di Eugenio et al. , 2010 ) . 
2.3 Major Dialogue Act Types . 
We have developed an integrated probabilistic approach to dialog act modeling for conversational speech , and tested it on a large speech corpus . 
Conversational feedback is mostly performance short utterances such as yeah , mh , okay produced by the main speaker but by one of the other participants of a conversation . 
Such utterances are among the most frequent in conversational data ( Stolcke et al. , 2000 ) . 
Finally , DA types themselves are assumed to be independent beyond a short span ( corresponding to the order of the dialog ) . 
Dialog act ( DA ) annotations and tagging , inspired by the speech act theory of Austin ( 1975 ) and Searle ( 1976 ) , have been used in the NLP community to understand and model dialog . 
Initial work was done unspoken interactions ( see for example ( Stolcke et al.,2000 ) ) . 
Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech
As discussed in Section 8 , this problem is best addressed by joint lexical-prosodic models . 
The HMM terminology was chosen here mainly for historical reasons.. 
Figure 1 shows the variables in the resulting HMM with directed edges representing conditional dependence . 
Dialog Act Example Utterance YEs-No-QUESTION Do you have to have any special training ? 
By representing a higher level intention of utterance human conversation , dialog act labels are being used to enrich the information provided spoken words ( Stolcke et al. , 2000 ) . 