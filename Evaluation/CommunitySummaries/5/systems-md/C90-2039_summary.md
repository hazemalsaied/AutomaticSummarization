Copying sharable parts is called redundant copying . 
Incremental Copy Graph Unification PROCEDURE Unify ( node 1 node 2 node 1 Dereference ( node . 
Other versions based on more efficient graph unification methods such as Wroblewski 's and Kogure 's method [ 23 , 16 ] have also been developed . 
Strategic Lazy Incremental Copy Graph Unification
The other, called ti~e strategic incremental copy graph unification method, uses an early failure finding strategy which first tries to unify ;ubstructures tending to fail in unification; this method is; based on stochastic data on tim likelihood of failure and ,'educes unnecessary computation.
Various kinds of grammatical formalisms without t , transformation were proposed from the late 1970s I ; rough the 1980s l ( ] aider al 85 , l ( plan and Bresnan 82 , Kay 1~5 , Pollm 'd and Sag 871 . 
These formalisms were developed relatively independentIy but actually had common properties ; theft is , they used data structures called frictional structures or feature structures and they were based on underneath operation on these data structures . 
This method achieves structure sharing by introducing lazy copying to Wroblewski 's incremental copy graph unification method . 
These formalisms were applied in the field of natural language processing and , based on these formalisms , ~ : systems such as machine translation systems were developed [ l < ol ; u , e et a l 8gJ . 
Kowalewski claims that copying is wrong when an algorithm copies too much ( over copying ) or copies too soon ( early copying ) . 
Memory is wasted by such redundant copying and this causes frequent garbage collection and page swapping which decrease the total system efficiency . 
ENDIF ENDIE ENDPROCEDURE Figure 6 : Incremental copy graph unification procedure The problem with Wroblewski 's method is that tile whole result DG is created by using only newly created structures . 
In such unification-based formalisms , feature structure FS ) unification is the most fundamental and significant operation . 
The efficiency of systems based on ..~uch formalisms , such as natural language analysis and generation systems very much depends on their FS personifier efficiencies . 
Output graph G3 Figure 5 : Incremental copy graph unification In this figure , type symbols are omitted . 
Tiffs dependency is especially crucial for lexicon-driven approaches such as tlPSO [ Pollard and Sag 861 and JPSG [ Gunji 871 because rich lexicon information and phrase structure information is described in terms of FSs . 
For example , the node Y ( G3/ < o c g > ) will be modified to be the unification result of G 1/ < a c g > ( or G1/ < b d > ) and G2/ < b d > when the feature path < b d > will be treated . 
The node specified by the feature path < a > ficos input graph G1 ( Gl/ < a > ) has an arc with the label c and the corresponding node of input graph G2 does not . 
The redundantly copied parts are relatively large when input graphs have few common feature paths . 
ENDPROCEDURE Figure 7 : The revised CopyNode procedure has the disadvantage of treating copy dependency information . 
For example , a spoken Present . 