hen a NODE node 1 has a NODE node 2 as its FORWARD value , the other contents of tile node 1 are ignored and tim contents of node 2 are used . 

The procedure incrementally copies nodes and ares on the subgraphs of each input 1 ) G until a node with an empty ARCS value is found .
 
The output node has been created only when neither input node is current ; or otherwise the output node is an existing current node .
 
Each arc value is copied and an arc with the same label and the copied value is added to the output node .
 
With such a method , it is possible to delay copying a node until either its own contents need to change ( e.g. , node G3/Ka c ! 7 > ) or until it is found to have an arc ( sequence ) to a node t , hat needs to be copied ( e.g. , node X G3/ < a c > in Fig .
 
The revised CopyNode procedure takes as its inputs the node to be copied node I and the arc arc I with node I as its value and node 2 as its immediate ancestor node ( i.e. , the arc 's initial node ) , and does the following ( set Fig .
 
7 ) : ( 1 ) if node , the dereference result of node is current , then CopyNode returns node l '' to indicate that the ancestor node node 2 must be coiffed immediately ; ( 2 ) otherwise , CopyArcs is applied to node 1 and if it returns , ~ ; several arc copies , CopyNode creates a new copy node .
 
( 2 ) In the worst eases , in which there ares unique labels arc but all results structures ares newly created , the methods CopyNode procedure CopyNode ( node , arc , ancestor ) node = dereference ( node ) .