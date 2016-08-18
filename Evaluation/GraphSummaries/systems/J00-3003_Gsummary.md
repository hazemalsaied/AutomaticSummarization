2.3 Major Dialogue Act Types . 
However , the approach gives only a small reduction in word error on our corpus , which can be attributed to a preponderance of a single dialog act type ( statements ) . 
The system detects sequences of distinctive pitch patterns by training one continuous- density HMM for each DA type . 
We compute P ( A [ U ) by decomposing it into an acoustic likelihood P ( A ] W ) and a word-based likelihood P ( W [ U ) , and summing over all word sequences : P ( AlU ) = ~-~P ( AIW , U ) P ( WIU ) w = ~P ( AIW ) P ( W [ U ) ( 6 ) w The second line is justified under the assumption that the recognizer acoustics ( typically , ancestral coefficients ) are invariant to DA type once the words are fixed . 
Unfortunately , the event classification accuracy on the Switchboard corpus was considerably poorer than in the Map Task domain , and DA recognition results when coupled with a discourse grammar were substantially worse than with decision trees . 
The simplest approach is to assume that the two types of acoustic observations ( recognizer acoustics and prosodic features ) are approximately conditionally independent once Ui is given : P ( ai , w , ,Fdui ) = P ( A~ , Wdui ) e ( Fifai , W~ , Ui ) ~ , P ( ai , Wi [ Ui ) P ( FilUi ) ( 8 ) Since the recognizer acoustics are modeled by way of their dependence on words , it is particularly important to avoid using prosodic features that are directly correlated with word identities , or features that are also modeled by the discourse grammars , such as utterance position relative to turn changes . 
The more frequent DA types are briefly characterized below . 
Similarly , we find distinctive correlations between certain phrases and DA types . 
An extensive comparison of the prosodic DA modeling literature with our work can be found in Shriberg et al . ( 1998 ) . 
As indicated in the introduction , our work builds on a number of previous efforts in computational discourse modeling and automatic discourse processing , most of which occurred over the last half-decade . 
W7 -- argmaxP ( WilAi , Ui ) wi P ( WilUi ) P ( AilWi , Ui ) = argument P ( AiIUi ) argmaxP ( WilUi ) P ( AirWi ) ( 11 ) wi As before in the DA classification model , we tacitly assume that the words Wi depend only on the DA of the current utterance , and also that the acoustics are independent of the DA type if the words are fixed . 
Table 7 DA classification using prosodic decision trees ( chance = 35 % ) . 
We have developed an integrated probabilistic approach to dialog act modeling for conversational speech , and tested it on a large speech corpus . 
Prior and related work is summarized in Section 7 . 
The following table shows examples of channels in the context of a Switchboard conversation : Speaker Dialogue Act Utterance B STATEMENT but , uh , we 're to the point now where our financial income is enough that we can consider putting some away - A BACKCHANNEL Uh-huh . 
The data was partitioned into a training set of 1,115 conversations ( 1.4M words , 198K utterances ) , used for estimating the various components of our model , and a test set of 19 conversations ( 29K words , 4K utterances ) . 
Dialog grammars for conversational speech need to be made more aware of the temporal properties of utterances . 
Also , the focus on conversational speech recognition led to a certain bias toward categories that were lexically or syntactically distinct ( recognition accuracy is traditionally measured including all lexical elements in an utterance ) . 
To expedite the DA labeling task and remain consistent with other Switchboard-based research efforts , we made use of a version of the corpus that had been hand-segmented into sentence-level units prior to our own work and independently of our DA labeling system ( Meteer et al . 1995 ) . 
Section 6 shows how DA models can be used to benefit speech recognition . 
Finally , we developed a principled way of incorporating DA modeling into the probability model of a continuous speech recognizer , by constraining word hypotheses using the discourse context . 
Interaction dominance ( Linell 1990 ) might be measured more accurately using DA distributions than with simpler techniques , and could serve as an indicator of the type or genre of discourse at hand . 
Here we investigate the interaction of prosodic models with the dialog grammar and the word-based DA models discussed above . 
We also investigated non-n-gram discourse models , based on various language modeling techniques known from speech recognition . 
Discourse Grammar P ( U ) P ( U , T ) P ( UIT ) None 42 84 42 Unigram 11.0 18.5 9.0 Bigram 7.9 10.4 5.1 Trigram 7.5 9.8 4.8 4.1 N-gram Discourse Models A computationally convenient type of discourse grammar is an n-gram model based on DA tags , as it allows efficient decoding in the HMM framework . 
Eventually , it is desirable to integrate dialog grammar , lexical , and prosodic cues into a single model , e.g. , one that predicts the next DA based on DA history and all the local evidence . 
Apart from corpus and tag set differences , our approach differs primarily in that it generalizes the simple HMM approach to cope with new kinds of problems , based on the Bayes network representations depicted in Figures 2 and 4 . 
As discussed in Section 8 , this problem is best addressed by joint lexical-prosodic models . 
Based on these considerations , we decided not to confound the DA classification task with the additional problems introduced by automatic segmentation and assumed the utterance-level segmentations as given . 
Further issues and open problems are addressed in Section 8 , followed by concluding remarks in Section 9 . 
Automatic segmentation of spontaneous speech is an open research problem in its own right ( Mast et al . 1996 ; Stolcke and Shriberg 1996 ) . 
Their tag sets are also generally smaller , but some of the same problems of balance occur . 
Table 2 The 42 dialog act labels . 
3.1 Dialogue Act Likelihoods . 
Dialog Act Example Utterance YEs-No-QUESTION Do you have to have any special training ? 
A total of 1,155 Switchboard conversations were labeled , comprising 205,000 utterances and 1.4 million words . 
For examples , Wi is the words transcription of the ith utterance within a conversation ( not the ith words ) . 