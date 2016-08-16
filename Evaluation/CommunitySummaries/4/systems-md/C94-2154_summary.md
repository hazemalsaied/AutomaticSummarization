Thus , though RES is computationally expensive , Troll uses RES only during compilation , never during run time . 
there are a number of different constraint languages within feature structure frameworks ( e.g. , Alshawi et al . 1991 ; Carpenter 1992 ; Dorre and Eisle 1991 ; Emele and Zajac 1990 ; Gerdemann and King 1994 ; Krieger and Schafer 1994 ; de Paiva 1993 ; Smolka 1989 ) . 
Legerdemain and G6tz 's Troll system ( see [ G6Tz 1993 ] , [ GFRDEIVIANN AND KING 1994 ] and [ GERDEMANN ( FC ) ] ) employs an efficient refinement of RES to test the satisfiability of feature structures . 
In fact , Troll represents each feature structure as a disjunction of the resolved of the feature structure . 
Loosely speaking , the resolved of a feature structure have the same underlying finite state automaton as the feature structure , and differ only in their output function . 
Troll exploits this property to represent each feature structure as a finite state automaton and a set of output frictions . 
The '1Â¥oll unifier is closed on these representations . 
Consider again the encoding of p and the feature structure 9~ . 
113 , | ) -721174Tfilfi , ,ge , , ( ler- many { rig , King } g'~sfs.n birefringence . 
It would , of course , not be very efficient to work with such large disjunctions of feature structures . 
C , legerdemain % King [ 8 ] have also shown that a feature structure l ] lets all encoded FCRs ifl '' the feature structure is satisfiable . 
well-typable iff the feature structure subsumes a well-typed feature structure , in ALl . : , type inferencing is employed to ensure that all feature structures are well-typable -- in fact , all feature structures are well typed . 
Let types resolution be the total function R : - > DRFS such that R ( F ) is the set of all resolved of F. Guided by the partition and all-or-nothing conditions , King [ 13 ] has formulated a semantics of FEATURE structure and developed a notion of a satisfiable FEATURE structure such that F E FS is satisfiable iff R ( F ) 0 . 