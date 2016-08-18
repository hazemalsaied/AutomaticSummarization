2.3 Major Dialogue Act Types . 
However , the approach gives only a small reduction in word error on our corpus , which can be attributed to a preponderance of a single dialog act type ( statements ) . 
The HMM states correspond to DAs , observations correspond to utterances , transition probabilities are given by the discourse grammar ( see Section 4 ) , and observation probabilities are given by the local likelihoods P ( Eil Ui ) . 
Speaker Dialogue Act Utterance A STATEMENT we 're from , uh , I 'm from Ohio / A STATEMENT and my wife 's from Florida / A TURN-ExIT SO , -/ B BACKCHANNEL Uh-huh./ A HEDGE so , I do n't know , / A ABANDONED it 's Klipsmack > , -/ A STATEMENT I 'm glad it 's not the kind of problem I have to come up with an answer to because it 's not - Answers and Agreements . 
5.2.4 Neural Network Classifiers . 
Finally , Ries ( 1999a shows that neural networks using only trigram features can be superior to higher-order n-gram DA models . 
We have the apparent difficulty that decision trees ( as well as other classifiers , such as neural networks ) give estimates for the posterior probabilities , P ( Ui [ Fi ) . 
Neural networks are worth investigating since they offer potential advantages over decision trees . 
Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech
4 5.1 Dialogue Act Classification Using Words . 
In an automatic labeling of word boundaries as either utterance or boundaries using a combination of lexical and prosodic cues , we obtained 96 % accuracy based on correct word transcripts , and 78 % accuracy with automatically recognized words . 
Eventually , it is desirable to integrate dialog grammar , lexical , and prosodic cues into a single model , e.g. , one that predicts the next DA based on DA history and all the local evidence . 
Our primary purpose in adapting the tag set was to enable computational DA modeling for conversational speech , with possible improvements to conversational speech recognition . 
Also , the focus on conversational speech recognition led to a certain bias toward categories that were lexically or syntactically distinct ( recognition accuracy is traditionally measured including all lexical elements in an utterance ) . 
A back channel is a short utterance that plays discourse-structuring roles , e.g. , indicating that the speaker should go on talking . 
Dialog grammars for conversational speech need to be made more aware of the temporal properties of utterances . 
A DA represents the meaning of an utterance at the level of elocutionary force ( Austin 1962 ) . 
5.2 Dialogue Act Classification Using Prosody . 
We chose to follow a recent standard for shallow discourse structure annotation , the Dialog Act Markup in Several Layers ( DAMSL ) tag set , which was designed by the natural language processing community under the auspices of the Discourse Resource Initiative ( Core and Allen 1997 ) . 
Table 2 The 42 dialog act labels . 
1 % What did you wear to work today ? 
However , we believe that this study represents a fairly comprehensive application of technology in this area and can serve as a point of departure and reference for other work . 
The idea caught on very quickly : Suhm and Waibel ( 1994 ) , Mast et aL ( 1996 ) , Warnke et al . ( 1997 ) , Reithinger and Klesen ( 1997 ) , and Taylor et al . ( 1998 ) all use variants of back off interpolated , or class n-gram language models to estimate DA likelihoods . 
Warned et al . ( 1999 ) and Ohler , Harbeck , and Niemann ( 1999 ) use related discriminative training algorithms for language models . 
Assuming that the true ( hand-transcribed ) words of utterances are given as evidence , we can compute word-based likelihoods P ( WIU ) in a straightforward way , by building a statistical language model for each of the 42 DAs . 
The HMM terminology was chosen here mainly for historical reasons.. 
Apart from corpus and tag set differences , our approach differs primarily in that it generalizes the simple HMM approach to cope with new kinds of problems , based on the Bayes network representations depicted in Figures 2 and 4 . 
The system detects sequences of distinctive pitch patterns by training one continuous- density HMM for each DA type . 
Figure 1 shows the variables in the resulting HMM with directed edges representing conditional dependence . 
Some researchers explicitly used HMM induction techniques to infer dialog grammars . 
To keep things simple , a first-order HMM ( trigram discourse grammar ) is assumed . 
~ Ui ) ... -- -* Un < end > Figure 1 The discourse HMM as Bayes network . 
( Indeed , with the exception of Samuel , Carberry , and VijayShanker ( 1998 ) , all models listed in Table 14 rely on some version of this HMM metaphor . ) 
We then used the decision tree posteriors as scaled DA likelihoods in the dialog model HMM , combining it with various n-gram dialog grammars for testing on our full standard test set . 
The distinction was designed to capture the different kinds of responses we saw to opinions ( which are often countered or disagreed with via further opinions ) and to statements ( which more often elicit continuer or channels : Dialogue Act Example Utterance STATEMENT Well , we have a cat , um , STATEMENT He 's probably , oh , a good two years old , big , old , fat and sassy tabby . 
3.1 Dialogue Act likelihood . 