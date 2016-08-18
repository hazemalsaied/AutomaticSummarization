Copying sharable parts is called redundant copying . 
Memory is wasted by such redundant copying and this causes frequent garbage collection and page swapping which decrease the total system efficiency . 
Incremental Copy Graph Unification PROCEDURE Unify ( node 1 node 2 node 1 Dereference ( node . 
Several FS unification methods were proposed in IKarttunen 86 , Ferreira 85 , Wroblewski 871 . 
To achieve this , I , he LING unification method , which uses copy dependency information , was developed . 
The LING unification procedure uses a revised CopyNode procedure which does not copy structures immediately . 
A unification example is shown in Fig . 
This order is related to the unification failure tendency . 
Various kinds of grammatical formalisms without t , transformation were proposed from the late 1970s I ; rough the 1980s l ( ] aider al 85 , l ( plan and Bresnan 82 , Kay 1~5 , Pollm 'd and Sag 871 . 
These formalisms were applied in the field of natural language processing and , based on these formalisms , ~ : systems such as machine translation systems were developed [ l < ol ; u , e et a l 8gJ . 
This order strategy can be generalized to the EFF and applied to the ordering of arcs with common labels . 
7 ) : ( 1 ) if node , the dereference result of node is current , then CopyNode returns node l '' to indicate that the ancestor node node 2 must be coiffed immediately ; ( 2 ) otherwise , CopyArcs is applied to node 1 and if it returns , ~ ; several arc copies , CopyNode creates a new copy node . 
This method achieves structure sharing by introducing lazy copying to Wroblewski 's incremental copy graph unification method . 
In Section 5 , a method which uses this generalized strategy is proposed . 
Kowalewski claims that copying is wrong when an algorithm copies too much ( over copying ) or copies too soon ( early copying ) . 
Japanese analysis system based on llPSG [ Kogure 891 uses 90 % - 98 % of the elapsed time in FS unification . 
Previous research identified DG copying as a significant overhead . 
A better method would minimize the copying of sharable arts . 
Strategic Lazy Incremental Copy Graph Unification
Output graph G3 Figure 5 : Incremental copy graph unification In this figure , type symbols are omitted . 
ENDIF ENDIE ENDPROCEDURE Figure 6 : Incremental copy graph unification procedure The problem with Wroblewski 's method is that tile whole result DG is created by using only newly created structures . 
For example , the node Y ( G3/ < o c g > ) will be modified to be the unification result of G 1/ < a c g > ( or G1/ < b d > ) and G2/ < b d > when the feature path < b d > will be treated . 
The node specified by the feature path < a > ficos input graph G1 ( Gl/ < a > ) has an arc with the label c and the corresponding node of input graph G2 does not . 
The redundantly copied parts are relatively large when input graphs have few common feature paths . 
The section also introduces the key idea of the EFF strategy wolfish comes from observations of his method . 
node 2 Dereferencelnode2 ) . 
endoscopy new node . 
AddArc ( out node complementary new node . 
ENDPROCEDURE Figure 7 : The revised CopyNode procedure has the disadvantage of treating copy dependency information . 
5 due to a change of node Y G3/ < a c g > ) . 
ENDIF Returo ( new node . 
In tile directed Graph notation , TFS Unification corresponds to Graph merging . 