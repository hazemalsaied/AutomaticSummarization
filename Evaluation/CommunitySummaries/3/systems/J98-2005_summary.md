a treebank PCFG whose simple relative frequency estimator corresponds to maximumlikelihood ( Chi and Geman 1998 ) , and which we shall refer to as `` MLPCFG '' . 
This result been firstly shown in ( Chaudhuri et al. , 1983 ) and later , with a different proof technique , in ( Chi and Geman , 1998 ) . 
Such maximization provides the estimator ( see for instance ( Chi and Geman , 1998 ) ) pG ( A ? a ) =f ( A ? a , T ) f ( A , T ) . 
Proof The proof is almost identical to the one given by Chi and Ceman ( 1998 ) . 
( 8~fl ea ~ ( B -- ~/3 ) = ~=lf B -- ~/3 ; cai ) ( 3 ) c~ s.t . H < B-~ ) e~ ~i=lf B -- -+o4cai ) The maximum-likelihood estimator is the natural , `` relative frequency , '' estimator . 
impose proper probability distributions on D ( Chi and Geman 1998 ) . 
Given a set of finite parse trees wl , w2 ... .. w , , the maximum-likelihood estimator for p ( see Section 2 ) is , sensibly enough , the `` relative frequency '' estimator y'~nlf A ~ AA ; wi ) ~i=1 f ( A ~ AA ; wi ) + f ( A ~ a ; wi ) ] where f ( . ; w ) is the number of occurrences of the production `` . '' in the tree w. The sentence a m , although ambiguous ( there are multiple parses when m > 2 ) , always involves m - 1 of the A ~ AA productions and m of the A ~ a productions . 
We will show that in both cases the estimated probability is tight . 
Dumpster Laird , and Rubin [ 1977 ] put the idea into a much more general setting and coined the Chi and Geman Probabilistic Context-Free Grammars term EM for Expectation-Maximization . 
Blum 1972 ] first introduced it for hidden Markov models ( regular grammars ) and Baker [ 1979 ] extended it to the problem addressed here ( estimation for context-free grammars ) . 
This solves a problem that was left open in the literature ( Chi and Geman,1998 ) 
This simple estimator , as shown by Chi and Geman ( 1998 ) , assigns proper production probÂ­ abilities for PCFGs . 
( A~c~ ) ER Chi and Geman Probabilistic Context-Free Grammars Given a set of finite parse trees cab ca2 , ... , can , drawn independently according to the distribution imposed by p , we wish to estimate p. In terms of the frequency function f , introduced in Section 1 , the likelihood of the data is L = L ( p ; cal , ca2 ... .. con ) n = II II p ( AY i=1 ( A~ ) ER Recall the derivation of the maximum-likelihood estimator of p : The log of the likelihood is : n ~ ~f ( A -- + a ; cai ) log A ~ a ) . 
Estimation of Probabilistic Context-Free Grammars
We show here that estimated production probabilities always yield proper distributions.
the sample , then the last production has ~ probability zero and hence the sequence has probability zero . 
wlEU~ Y ( w¢ ) =Y ( oa ) In the case where only yields are observed , the treatment is complicated considerably by the possibility of null productions ( A -- , 0 ) and unit productions ( A ~ B E V ) . 
Proof Almost identical , except that we use ( 5 ) in place of ( 3 ) and end up with : n E qA EEG_1 [ F ( A ; wi ) -F ( A ; wi ) lw C fly ( w , ) ] ~ 0 . 
We show here that estimated production probabilities always yield proper distributions . 
( Wetherell and others use the designation `` consistent '' instead of `` tight , '' but in statistics , consistency refers to the asymptotic correctness of an estimator . ) 
Suppose B E V is unobserved among the parse tree cabc 0 2 -.. , can . 