The efficiency of the SING unification method depends on the following factors : ( 1 ) The overall FS unification failure rate of the process : in extreme cases , if Go unification failure occurs , the method has no advantages except the overhead of feature unification order sorting . 
The SING unification method introduces the concept of feature unification strategy . 
Other versions based on more efficient graph unification methods such as Wroblewski 's and Kogure 's method [ 23 , 16 ] have also been developed . 
To achieve this , I , he LING unification method , which uses copy dependency information , was developed . 
In Kasper 's disjunctive feature description unification [ Kasper 861 , such cases occur very frequently in unifying definite and disjunct 's definite parts . 
Various kinds of grammatical formalisms without t , transformation were proposed from the late 1970s I ; rough the 1980s l ( ] aider al 85 , l ( plan and Bresnan 82 , Kay 1~5 , Pollm 'd and Sag 871 . 
in the learning process , when FS unification is applied , feature treatment orders are randomized for the sake of random extraction . 
These formalisms were developed relatively independentIy but actually had common properties ; theft is , they used data structures called frictional structures or feature structures and they were based on underneath operation on these data structures . 
In Section 5 , a method which uses this generalized strategy is proposed . 
The strategic lazy incremental copy graph ( SLING ) unification method combines two incremental copy graph unification methods : the lazy incremental copy graph ( LING ) unification method and the strategic incremental copy graph ( SING ) unification method . 
When a NODE node 1 has a NODE node 2 as its FORWARD value , the other contents of tile node 1 are ignored and tim contents of node 2 are used . 
Japanese analysis system based on llPSG [ Kogure 891 uses 90 % - 98 % of the elapsed time in FS unification . 
That is , unless some new scheme for reducing excessive copying is introduced such as scucture-sharing of an unchanged shared-forest ( [ Kogure , 1990 ] ) . 
One , called the lazy incremental copy graph unification method , achieves structure sharing with constant order data access time which reduces the required memory . 
Strategic Lazy Incremental Copy Graph Unification
Kowalewski claims that copying is wrong when an algorithm copies too much ( over copying ) or copies too soon ( early copying ) . 
With such a method , it is possible to delay copying a node until either its own contents need to change ( e.g. , node G3/Ka c ! 7 > ) or until it is found to have an arc ( sequence ) to a node t , hat needs to be copied ( e.g. , node X G3/ < a c > in Fig . 
The revised CopyNode procedure takes as its inputs the node to be copied node I and the arc arc I with node I as its value and node 2 as its immediate ancestor node ( i.e. , the arc 's initial node ) , and does the following ( set Fig . 
node 2 Dereferencelnode2 ) . 
7 ) : ( 1 ) if node , the dereference result of node is current , then CopyNode returns node l '' to indicate that the ancestor node node 2 must be coiffed immediately ; ( 2 ) otherwise , CopyArcs is applied to node 1 and if it returns , ~ ; several arc copies , CopyNode creates a new copy node . 
A Unification example is shown in Fig . 