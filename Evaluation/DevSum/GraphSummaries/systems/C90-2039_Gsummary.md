This method achieves structure sharing by introducing lazy copying to Wroblewski 's incremental copy graph unification method . 
Ile proposed an incremental copy graph unification method to avoid over copying and early copying . 
Copying sharable parts is called redundant copying . 
Strategic Lazy Incremental Copy Graph Unification
however the problem with his method is that a unification result graph consists only of newly created structures . 
This method is called the strategic ij ! ~crementaI copy graph unification method ( the SING unification method ) . 
These two methods can be combined into a single method called the strategic lazy ijAcremeatal copy graph unification method ( the SLING unification method ) . 
The strategic lazy incremental copy graph ( SLING ) unification method combines two incremental copy graph unification methods : the lazy incremental copy graph ( LING ) unification method and the strategic incremental copy graph ( SING ) unification method . 
The method is called the lazy i2 ! incremental copy IFaph unification reel , hod ( the LING unification method for short ) . 
Various kinds of grammatical formalisms without t , transformation were proposed from the late 1970s I ; rough the 1980s l ( ] aider al 85 , l ( plan and Bresnan 82 , Kay 1~5 , Pollm 'd and Sag 871 . 
These formalisms were applied in the field of natural language processing and , based on these formalisms , ~ : systems such as machine translation systems were developed [ l < ol ; u , e et a l 8gJ . 
That is , the SING unification method applied in an analysis system uses the failure tendency information acquired by a learning analysis process . 
Method In a system where FS unification is applied , there are features whose values fail relatively often in unification with other values and there are features whose values do not fail so often . 
When a new copy of a node is needed later , the LING unification procedure will actually copy structures using the COPY-DEPENDENCY slot value of the node ( in GetOutNode procedure in lJ'ig . 
The LING unification procedure uses a revised CopyNode procedure which does not copy structures immediately . 
The NODE structure has the slots TYPESYMBOL to represent a type symbol , ARCS to represent a set of feature-value pairs , GENERATION to specify the unification process in which the structure has been created , FORWARD , and COPY . 
The section also introduces the key idea of the EFF strategy wolfish comes from observations of his method . 
Thus , the efficiency gain ficos this method is high when the overall FS unification failure rate of the application process is high . 
This paper proposes an FS unification method that allows structure sharing with constant moder node access time . 
The ComplementArcs procedure takes two lists of arcs as NODE TYPESYMBOL : < symbol > [ ARCS : < a list of ARC structures > FORWARD : `` < aNODEstructure orNIL > / COPY : < a NODEstructure or Nil , > GENERATION : < an integer > ARC LABEL : < symbol > VALUE : < : a NODEstructure > Figure 4 : Data Structures for Wroblewski 's method Input graph GI Input graph 62 ¢ ... ... .'77 ... ... .. i : Sobg , hap's not required to be copied L ... ... ... ... ... ... ... ... ... ... ... ... ... ... . 
In tile directed graph notation , TFS unification corresponds to graph merging . 
In this paper , some of the efficiency of the procedure- based system is introduced into an FS unification-based system . 
The revised procedure uses a newly introduced slot COPY-DEPENDENCY . 
Ferreira structure sharing FS unification method can avoid this problem . 
These methods take two DGs as their inputs and give a unification result DG . 
As in TFS unification , failure tendency information is recorded in terms of a triplet consisting of the greatest lower bound type symbol of the input TFSs ' type symbols , a feature and successful flag . 
The unification procedure is applied recursively to feature a values of the input nodes . 
To achieve this , I , he LING unification method , which uses copy dependency information , was developed . 
The LING unification method achieves structure sharing without the O ( log d ) data access overhead of Pereira 's method . 
The efficiency of the LING unification method depends on the proportion of newly created structures in the unification result structures . 
These formalisms were developed relatively independentIy but actually had common properties ; theft is , they used data structures called frictional structures or feature structures and they were based on underneath operation on these data structures . 
That is , an FS unification method is proposed that introduces a strategy called the early failure tending strategy ( the EFF strategy ) to make FS unification efficient , in this method , FS unification orders are not specified explicitly by rule writers but are controlled by learned information on tendencies of FS constraint application failures . 
With such a method , it is possible to delay copying a node until either its own contents need to change ( e.g. , node G3/Ka c ! 7 > ) or until it is found to have an arc ( sequence ) to a node t , hat needs to be copied ( e.g. , node X G3/ < a c > in Fig . 
It substitutes arcs with newly copied nodes for existing arcs . 
The revised CopyNode procedure takes as its inputs the node to be copied node I and the arc arc I with node I as its value and node 2 as its immediate ancestor node ( i.e. , the arc 's initial node ) , and does the following ( set Fig . 
Avoiding this problem in his method requires a special operation of merging a skeleton-environment structure into a skeleton structure , but this prevents structure sharing . 
The combined method Inakes each FS unification efficient and also reduces garbage collection and page swapping occurrences by avoiding memory wastage , thus increasing the total efficiency of li 'S unification-based natural language processing systems such aa analysis and generation systems based on IlI'SG . 
It then adds the arc copies and arcs of node that are not copied to the new node , and returns the new node ; ( 3 ) otherwise , CopyNode adds the pair consisting of the ancestor node node 2 and the are arc into the COPY- DEPENDENCY slot of node 1 '' and returns Nil_ . 
AddArc ( out node complementary new node . 
node 2 Dereferencelnode2 ) . 
endoscopy new node . 
ENDIF Returo ( new node . 
ENDIF IF Eq ? ( out node node 1 THEN complements complement 2 . 
ENDIF FORALL complement IN complements DO new node CopyNode ( complementary . 
A Unification example is shown in Fig . 