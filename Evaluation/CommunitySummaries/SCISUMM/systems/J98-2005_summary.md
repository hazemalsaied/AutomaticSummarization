a treebank PCFG whose simple relative frequency estimator corresponds to maximumlikelihood ( Chi and Geman 1998 ) , and which we shall refer to as `` MLPCFG '' . 
This result been firstly shown in ( Chaudhuri et al. , 1983 ) and later , with a different proof technique , in ( Chi and Geman , 1998 ) . 
Such maximization provides the estimator ( see for instance ( Chi and Geman , 1998 ) ) pG ( A ? a ) =f ( A ? a , T ) f ( A , T ) . 
Proof The proof is almost identical to the one given by Chi and Ceman ( 1998 ) . 
( 8~fl ea ~ ( B -- ~/3 ) = ~=lf B -- ~/3 ; cai ) ( 3 ) c~ s.t . H < B-~ ) e~ ~i=lf B -- -+o4cai ) The maximum-likelihood estimator is the natural , `` relative frequency , '' estimator . 
impose proper probability distributions on D ( Chi and Geman 1998 ) . 
Given a set of finite parse trees wl , w2 ... .. w , , the maximum-likelihood estimator for p ( see Section 2 ) is , sensibly enough , the `` relative frequency '' estimator y'~nlf A ~ AA ; wi ) ~i=1 f ( A ~ AA ; wi ) + f ( A ~ a ; wi ) ] where f ( . ; w ) is the number of occurrences of the production `` . '' in the tree w. The sentence a m , although ambiguous ( there are multiple parses when m > 2 ) , always involves m - 1 of the A ~ AA productions and m of the A ~ a productions . 
We will show that in both cases the estimated probability is tight . 
Dumpster Laird , and Rubin [ 1977 ] put the idea into a much more general setting and coined the Chi and Geman Probabilistic Context-Free Grammars term EM for Expectation-Maximization . 
Based upon the results of Stolcke [ 1995 ] it is likely that this restriction can be relaxed , but we have not pursued this . 
This solves a problem that was left open in the literature ( Chi and Geman,1998 ) 
For each A E V , let F ( A ; w ) be the number of instances of A in w and let F ( A ; w ) be the number of non root instances of A in w. Given oz E ( V U T ) * , let nA ( cZ ) be the number of instances of A in the string o~ , and , finally , let ai be the ith component of the string o~ . 
This simple estimator , as shown by Chi and Geman ( 1998 ) , assigns proper production probÂ­ abilities for PCFGs . 
Estimation of Probabilistic Context-Free Grammars
We show here that estimated production probabilities always yield proper distributions.
What if the production probabilities are estimated from data ? 
We show here that estimated production probabilities always yield proper distributions . 
Proof Almost identical , except that we use ( 5 ) in place of ( 3 ) and end up with : n E qA EEG_1 [ F ( A ; wi ) -F ( A ; wi ) lw C fly ( w , ) ] ~ 0 . 
Thus , ~ is again less than ½ and the distribution is again tight . 
( Wetherell and others use the designation `` consistent '' instead of `` tight , '' but in statistics , consistency refers to the asymptotic correctness of an estimator . ) 
Suppose B E V is unobserved among the parse tree cabc 0 2 -.. , can . 