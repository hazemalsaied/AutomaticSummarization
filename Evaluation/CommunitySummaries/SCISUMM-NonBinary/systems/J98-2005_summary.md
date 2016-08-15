a treebank PCFG whose simple relative frequency estimator corresponds to maximumlikelihood ( Chi and Geman 1998 ) , and which we shall refer to as `` MLPCFG '' . 
Letting ~y denote { w Efk Y ( w ) = Y } , the likelihood of the corpus becomes n H E H P ( A -- '~oL ) f ( A~ ; ~ ) '' i=1 ~OE~y ( ~i ) ( A -- -~o~ ) ER And the maximum-likelihood equation becomes + p ( B fl ) Ei=l EwEfly ( wi , I-I ( A -- . ) cR p ( A -~ a ) f ( A-~ '' ; ~ ) = 0 fT ( B ~ /3 ) = ~iL1 Ep~f ( B ~ fl ; w ) lw E ~y ( ~ , ) ] ( 4 ) , ~s , , , ~Ei=IEpV ( `` a ; w ) lw E ~Y ( o~ , ) ] E ( B_~ , E B ~ where E~ is expectation under fi and where `` ] w E~-~y ( wi ) '' means `` conditioned on 0.2E ~-~Y ( wi ) ' '' There is no hope for a closed form solution , but ( 4 ) does suggest an iteration scheme , which , as it turns out , `` climbs '' the likelihood surface ( though there are no guarantees about approaching a global maximum ) : Let P0 be an arbitrary assignment respecting ( 1 ) . 
Such maximization provides the estimator ( see for instance ( Chi and Geman , 1998 ) ) pG ( A ? a ) =f ( A ? a , T ) f ( A , T ) . 
This result been firstly shown in ( Chaudhuri et al. , 1983 ) and later , with a different proof technique , in ( Chi and Geman , 1998 ) . 
( Wetherell and others use the designation `` consistent '' instead of `` tight , '' but in statistics , consistency refers to the asymptotic correctness of an estimator . ) 
We will show that in both cases the estimated probability is tight . 
Let Sh be the total probability of all trees with depth less than or equal to h. For example , $ 2 = q corresponding to A ~ a , and $ 3 = q + pq2 corresponding to { A ~ a } tO { A ~ AA , A -- ~ a , A -- ~ a } . 
Furthermore , it is not hard to see that any such B has probability zero of arising in any derivation that is based upon the maximum-likelihood probabilities hence the issue of tightness is independent of this assignment . 
Blum 1972 ] first introduced it for hidden Markov models ( regular grammars ) and Baker [ 1979 ] extended it to the problem addressed here ( estimation for context-free grammars ) . 
Proof The proof is almost identical to the one given by Chi and Ceman ( 1998 ) . 
This solves a problem that was left open in the literature ( Chi and Geman,1998 ) 
For each A E V , let F ( A ; w ) be the number of instances of A in w and let F ( A ; w ) be the number of non root instances of A in w. Given oz E ( V U T ) * , let nA ( cZ ) be the number of instances of A in the string o~ , and , finally , let ai be the ith component of the string o~ . 
impose proper probability distributions on D ( Chi and Geman 1998 ) . 
Dumpster Laird , and Rubin [ 1977 ] put the idea into a much more general setting and coined the Chi and Geman Probabilistic Context-Free Grammars term EM for Expectation-Maximization . 
What if the production probabilities are estimated from data ? 
In the usual way , probabilities are introduced through the productions : P : R -- ~ [ 0,1 ] such that VA E V : p ( A -~ c~ ) = 1 . 
This simple estimator , as shown by Chi and Geman ( 1998 ) , assigns proper production probÂ­ abilities for PCFGs . 
Proof Almost identical , except that we use ( 5 ) in place of ( 3 ) and end up with : n E qA EEG_1 [ F ( A ; wi ) -F ( A ; wi ) lw C fly ( w , ) ] ~ 0 . 
This work was supported by Applying probability measures to abstract the Army Research Office languages . 
Denote the maximum-likelihood estimator by fi : n B AB q- ~i=lf -- + /3 ; ca ; ) = 0 V ( S ~ /3 ) E R f , ( B +/3 ) Since ~ fi ( B+/3 ) =l ) fl sA . 
In the simple example here , the estimator converges in one step and is the same ~ as if we had observed the entire parse tree for each wi . 