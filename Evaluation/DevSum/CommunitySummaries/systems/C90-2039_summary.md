Ile proposed an incremental copy graph unification method to avoid over copying and early copying . 
Previous research identified DG copying as a significant overhead . 
A unification example is shown in Fig . 
In tile directed graph notation , TFS unification corresponds to graph merging . 
Other versions based on more efficient graph unification methods such as Wroblewski 's and Kogure 's method [ 23 , 16 ] have also been developed . 
For example , in Kasper 's disjunctive feature description unification , a definite part [ `` S is larger than a disjunct definite part t '' S . 
For example , the node Y ( G3/ < o c g > ) will be modified to be the unification result of G 1/ < a c g > ( or G1/ < b d > ) and G2/ < b d > when the feature path < b d > will be treated . 
This order is related to the unification failure tendency . 
In such cases , application of the EFF strategy , that is , treating features tending to fall in unification first , reduces unnecessary computation when the unification finally fails . 
Strategic Lazy Incremental Copy Graph Unification
in the learning process , when FS unification is applied , feature treatment orders are randomized for the sake of random extraction . 
That is , the SING unification method applied in an analysis system uses the failure tendency information acquired by a learning analysis process . 
By using learned failure tendency information , feature value unification is applied in an order that first treats features with the greatest tendency to fail . 
Kowalewski claims that copying is wrong when an algorithm copies too much ( over copying ) or copies too soon ( early copying ) . 
Copying sharable parts is called redundant copying . 
This method achieves structure sharing by introducing lazy copying to Wroblewski 's incremental copy graph unification method . 
The other, called ti~e strategic incremental copy graph unification method, uses an early failure finding strategy which first tries to unify ;ubstructures tending to fail in unification; this method is; based on stochastic data on tim likelihood of failure and ,'educes unnecessary computation.
That is , unless some new scheme for reducing excessive copying is introduced such as scucture-sharing of an unchanged shared-forest ( [ Kogure , 1990 ] ) . 
When a NODE node 1 has a NODE node 2 as its FORWARD value , the other contents of tile node 1 are ignored and tim contents of node 2 are used . 
Avoiding this problem in his method requires a special operation of merging a skeleton-environment structure into a skeleton structure , but this prevents structure sharing . 
however the problem with his method is that a unification result graph consists only of newly created structures . 
A better method would minimize the copying of sharable arts . 
Memory is wasted by such redundant copying and this causes frequent garbage collection and page swapping which decrease the total system efficiency . 
Therefore , Pereira 's method needs relatively few new structures when two input FSs are difference in size and which input is larger are known before unification . 
This is unnecessary because there are often input subgraphs that can be used as part of the result graph without any modification , or as sharable parts between one of the input graphs and the result graph . 
Usually , the number of features in two input structures is relatively small and the sizes of the two input structures are often very different . 
Section 2 explains typed feature structures ( TFSs ) and unification on them . 
The strategic lazy incremental copy graph ( SLING ) unification method combines two incremental copy graph unification methods : the lazy incremental copy graph ( LING ) unification method and the strategic incremental copy graph ( SING ) unification method . 
The strategic lazy incremental copy graph unification method is a combination of two methods for unifying mature structures . 
Output graph G3 Figure 5 : Incremental copy graph unification In this figure , type symbols are omitted . 
These formalisms were developed relatively independentIy but actually had common properties ; theft is , they used data structures called frictional structures or feature structures and they were based on underneath operation on these data structures . 
The method is called the lazy i2 ! incremental copy IFaph unification reel , hod ( the LING unification method for short ) . 
With such a method , it is possible to delay copying a node until either its own contents need to change ( e.g. , node G3/Ka c ! 7 > ) or until it is found to have an arc ( sequence ) to a node t , hat needs to be copied ( e.g. , node X G3/ < a c > in Fig . 
FOR ALL arc IN nodes DO IF NotNIL ? ( new arc FindArc ( archangel new arcs ) THEN AddArc ( new node Newark undervalue . 
ENDIF ENDPROCEDURE CopyArcs PROCEDURE AlcsCopied ( node ) new arcs O- FOR ALL arc IN nodes DO new node CopyNode ( overvalue arc , node ) . 
The revised CopyNode procedure takes as its inputs the node to be copied node I and the arc arc I with node I as its value and node 2 as its immediate ancestor node ( i.e. , the arc 's initial node ) , and does the following ( set Fig . 
It substitutes arcs with newly copied nodes for existing arcs . 
ELSE AddArc ( out node shareholder arc node . 
AddArc ( out node complementary new node . 
IF Eq ? ( node node 2 THEN Return ( node 1 . 
ELSE out node GetOutNode ( node node 2 meet ) . 
ENDPROCEDURE Figure 7 : The revised CopyNode procedure has the disadvantage of treating copy dependency information . 
node 2 Dereferencelnode2 ) . 
5 due to a change of node Y G3/ < a c g > ) . 
Several FS Unification methods were proposed in IKarttunen 86 , Ferreira 85 , Wroblewski 871 . 