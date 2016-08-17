If the corpus is unparsed then there is an iterative approach to maximum-likelihood estimation ( the EM or Baum-Welsh algorithm -- again , see Section 2 ) and the same question arises : do we get actual probabilities or do the estimated PCFG 's assign some mass to infinite trees ? 
Maximum likelihood from incomplete data via the EM algorithm . 
For each A E V , let F ( A ; w ) be the number of instances of A in w and let F ( A ; w ) be the number of non root instances of A in w. Given oz E ( V U T ) * , let nA ( cZ ) be the number of instances of A in the string o~ , and , finally , let ai be the ith component of the string o~ . 
2 * Division of Applied Mathematics , Brown University , Providence , RI 02912 USA 1 Note added in proof : An alternative proof of one of our main results ( see Corollary , Section 3 ) recently appeared in the IEEE Transactions on Pattern Analysis and Machine Intelligence ( S , Sanchez and Bened ( [ 1997 ] ) . 
( 8~fl ea ~ ( B -- ~/3 ) = ~=lf B -- ~/3 ; cai ) ( 3 ) c~ s.t . H < B-~ ) e~ ~i=lf B -- -+o4cai ) The maximum-likelihood estimator is the natural , `` relative frequency , '' estimator . 
What if the production probabilities are estimated from data ? 
Given a set of finite parse trees wl , w2 ... .. w , , the maximum-likelihood estimator for p ( see Section 2 ) is , sensibly enough , the `` relative frequency '' estimator y'~nlf A ~ AA ; wi ) ~i=1 f ( A ~ AA ; wi ) + f ( A ~ a ; wi ) ] where f ( . ; w ) is the number of occurrences of the production `` . '' in the tree w. The sentence a m , although ambiguous ( there are multiple parses when m > 2 ) , always involves m - 1 of the A ~ AA productions and m of the A ~ a productions . 
Thus , ~ is again less than ½ and the distribution is again tight . 
Dumpster Laird , and Rubin [ 1977 ] put the idea into a much more general setting and coined the Chi and Geman Probabilistic Context-Free Grammars term EM for Expectation-Maximization . 
Context-free grammars ( CFG 's ) are useful because of their relatively broad coverage and because of the availability of efficient parsing algorithms . 
( 6 ) AEV i=1 In the absence of unit productions and null productions , F ( A ; w ) < 21w [ ( twice the length of the string w ) . 
This iteration procedure is an instance of the EM Algorithm . 
Letting ~y denote { w Efk Y ( w ) = Y } , the likelihood of the corpus becomes n H E H P ( A -- '~oL ) f ( A~ ; ~ ) '' i=1 ~OE~y ( ~i ) ( A -- -~o~ ) ER And the maximum-likelihood equation becomes + p ( B fl ) Ei=l EwEfly ( wi , I-I ( A -- . ) cR p ( A -~ a ) f ( A-~ '' ; ~ ) = 0 fT ( B ~ /3 ) = ~iL1 Ep~f ( B ~ fl ; w ) lw E ~y ( ~ , ) ] ( 4 ) , ~s , , , ~Ei=IEpV ( `` a ; w ) lw E ~Y ( o~ , ) ] E ( B_~ , E B ~ where E~ is expectation under fi and where `` ] w E~-~y ( wi ) '' means `` conditioned on 0.2E ~-~Y ( wi ) ' '' There is no hope for a closed form solution , but ( 4 ) does suggest an iteration scheme , which , as it turns out , `` climbs '' the likelihood surface ( though there are no guarantees about approaching a global maximum ) : Let P0 be an arbitrary assignment respecting ( 1 ) . 
Assign probability p to the first production ( A ~ AA ) and q = 1 -p to the second ( A ~ a ) . 
Given a context-free grammar G = ( V , T , R , S ) , let f2 be the set of finite parse trees , let p : R ~ [ 0,1 ] be a system of production probabilities satisfying ( 1 ) , and let wl , w2 , . 
Each production in R has the form A ~ oL , where A E V and o~ E ( VUT ) * . 
Proof Almost identical , except that we use ( 5 ) in place of ( 3 ) and end up with : n E qA EEG_1 [ F ( A ; wi ) -F ( A ; wi ) lw C fly ( w , ) ] ~ 0 . 
( We use R in place of the more typical P to avoid confusion with probabilities . ) 
Journal of the Royal Statistical Society , Series B , 39:138 . 
Is it tight ? 