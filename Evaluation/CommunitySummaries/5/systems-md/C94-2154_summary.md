THE CORRECT AND EFFICIENT IMPLEMENTATION OF APPROPRIATENESS SPECIFICATIONS FOR TYPED FEATURE STRUCTURES
Consider again the encoding of p and the feature structure 9~ . 
Unification of sets of feature structures is defined here ill the standard way : S t2 , S '' = { 1 '' [ I '' ' 6 S and l '' '' G S '' and 1 '' = 1 '' ' H 1 '' '' } . 
Legerdemain and G6tz 's Troll system ( see [ G6Tz 1993 ] , [ GFRDEIVIANN AND KING 1994 ] and [ GERDEMANN ( FC ) ] ) employs an efficient refinement of RES to test the satisfiability of feature structures . 
Loosely speaking , the resolved of a feature structure have the same underlying finite state automaton as the feature structure , and differ only in their output function . 
In fact , Troll represents each feature structure as a disjunction of the resolved of the feature structure . 
Troll exploits this property to represent each feature structure as a finite state automaton and a set of output frictions . 
there are a number of different constraint languages within feature structure frameworks ( e.g. , Alshawi et al . 1991 ; Carpenter 1992 ; Dorre and Eisle 1991 ; Emele and Zajac 1990 ; Gerdemann and King 1994 ; Krieger and Schafer 1994 ; de Paiva 1993 ; Smolka 1989 ) . 
Unification lbrmMisms may be either un-typed ( DCC~s , PATRII , 1 , F ( ; ) or typed ( npsG ) . 
C , legerdemain % King [ 8 ] have also shown that a feature structure l ] lets all encoded FCRs ifl '' the feature structure is satisfiable . 
Consider , For exam- pie , our encoding of the disjunctive FCR p and suppose that 99 is the fe , feature structure t [ f : +,9 : - ] . 
well-typable iff the feature structure subsumes a well-typed feature structure , in ALl . : , type inferencing is employed to ensure that all feature structures are well-typable -- in fact , all feature structures are well typed . 
Let types resolution be the total function R : - > DRFS such that R ( F ) is the set of all resolved of F. Guided by the partition and all-or-nothing conditions , King [ 13 ] has formulated a semantics of FEATURE structure and developed a notion of a satisfiable FEATURE structure such that F E FS is satisfiable iff R ( F ) 0 . 