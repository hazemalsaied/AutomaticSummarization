a treebank PCFG whose simple relative frequency estimator corresponds to maximumlikelihood ( Chi and Geman 1998 ) , and which we shall refer to as `` MLPCFG '' . 
Evidently the likelihood is unaffected by the particular assignment of fi ( B -- ~ fl ) . 
Such maximization provides the estimator ( see for instance ( Chi and Geman , 1998 ) ) pG ( A ? a ) =f ( A ? a , T ) f ( A , T ) . 
This result been firstly shown in ( Chaudhuri et al. , 1983 ) and later , with a different proof technique , in ( Chi and Geman , 1998 ) . 
Is it tight ? 
a What if p is estimated from data ? 
This simple estimator , as shown by Chi and Geman ( 1998 ) , assigns proper production probÂ­ abilities for PCFGs . 
impose proper probability distributions on D ( Chi and Geman 1998 ) . 
Dumpster Laird , and Rubin [ 1977 ] put the idea into a much more general setting and coined the Chi and Geman Probabilistic Context-Free Grammars term EM for Expectation-Maximization . 
Blum 1972 ] first introduced it for hidden Markov models ( regular grammars ) and Baker [ 1979 ] extended it to the problem addressed here ( estimation for context-free grammars ) . 
For each A E V , let F ( A ; w ) be the number of instances of A in w and let F ( A ; w ) be the number of non root instances of A in w. Given oz E ( V U T ) * , let nA ( cZ ) be the number of instances of A in the string o~ , and , finally , let ai be the ith component of the string o~ . 
It is reasonable to hope that if the trees in the sample are finite , then an estimate of production probabilities based upon the sample will produce a system that assigns probability zero to the set of infinite trees . 
This solves a problem that was left open in the literature ( Chi and Geman,1998 ) 
Proof The proof is almost identical to the one given by Chi and Ceman ( 1998 ) . 
What if the production probabilities are estimated from data ? 
We show here that estimated production probabilities always yield proper distributions.
( A~c~ ) ER Chi and Geman Probabilistic Context-Free Grammars Given a set of finite parse trees cab ca2 , ... , can , drawn independently according to the distribution imposed by p , we wish to estimate p. In terms of the frequency function f , introduced in Section 1 , the likelihood of the data is L = L ( p ; cal , ca2 ... .. con ) n = II II p ( AY i=1 ( A~ ) ER Recall the derivation of the maximum-likelihood estimator of p : The log of the likelihood is : n ~ ~f ( A -- + a ; cai ) log A ~ a ) . 
Proof Almost identical , except that we use ( 5 ) in place of ( 3 ) and end up with : n E qA EEG_1 [ F ( A ; wi ) -F ( A ; wi ) lw C fly ( w , ) ] ~ 0 . 
Furthermore , CFG 's are readily fit with a probability distribution ( to make probabilistic CFG 's -- or PCFG 's ) , rendering them suitable for ambiguous languages through the maximum a posteriori rule of choosing the most probable parse . 
Estimation of Probabilistic Context-Free Grammars
Suppose B E V is unobserved among the parse tree cabc 0 2 -.. , can . 