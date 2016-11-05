THE CORRECT AND EFFICIENT IMPLEMENTATION OF APPROPRIATENESS SPECIFICATIONS FOR TYPED FEATURE STRUCTURES
there are a number of different constraint languages within feature structure frameworks ( e.g. , Alshawi et al . 1991 ; Carpenter 1992 ; Dorre and Eisle 1991 ; Emele and Zajac 1990 ; Gerdemann and King 1994 ; Krieger and Schafer 1994 ; de Paiva 1993 ; Smolka 1989 ) . 
Legerdemain and G6tz 's Troll system ( see [ G6Tz 1993 ] , [ GFRDEIVIANN AND KING 1994 ] and [ GERDEMANN ( FC ) ] ) employs an efficient refinement of RES to test the satisfiability of feature structures . 
Thus , though RES is computationally expensive , Troll uses RES only during compilation , never during run time . 
Unification lbrmMisms may be either un-typed ( DCC~s , PATRII , 1 , F ( ; ) or typed ( npsG ) . 
A m~L , ior reason for adding types to ~ form ism is to express restrictions on feature a.s in ( ; l 's ( : : [ 5 ] in order to rule out nonexistent ) es of objects . 
For example , there are no verbs which have the [ mixture . The simplest way to express such restrictions is by means of a.n appropriateness function : Type × Feat ~ Type . 
With such a.n ample rol ) brittleness son Sllch restriction s may be expressed , though no restrictions involving entrances be expressed . 
In this pal ) er , we will first in §2 survey the range of type constraints may be expressed with just a. type hierarchy and * ' ] 'he research ( ! lllL ( 'd ill | , his ; paper was pay tidally sponsored hy ' [ subproject `` ( ; onsl.rahH.s on Grammar flora Efficient Ck : generation of the Soi , der forschungsbereich 340 of the Deutsche [ `` orschungsgemeinscha ft. `` VVe would also like to thank Shiloh for help l comments ou thc ideas presented here . 
All mistakes arc of collard our OWll . 
IKI . 
Wilhelmine . 
113 , | ) -721174Tfilfi , ,ge , , ( ler- many { rig , King } g'~sfs.n birefringence . 
a.n N ) appropriateness specification . 
Then in ~3 , we discuss how such type constraints linty be maintained under unification as exemplified in the na.tura. 1 language D~rs- generation system '.l'ro l [ 7 ] . 
1 Unlike previous systems such as ALl , : , Troll does not employ any type inferencing inste~M , a , limited amount of named disjunction ( [ 1 1 ] , [ 12 ] , [ 6 ] ) is introduced to record type resolved u son possibilities . 
The amount of dis- junction is also kept small by the technique of unwilling g described in [ 9 ] . 
This strategy actually apl ) appropriateness conditions in some cases in which a. type in-ferencing strategy would fail l ) 'inMly , in §4 , we discuss the possibilities for genera Lizzie this ample roach to handle a bro~Mer ringer of constraints including constraints inw ) ling ties . 
As discussed iu Gerdemann , ~ King [ 8 ] , one can view ample rol ) privateness CO [ editions as ( lining style fea, 1 tl re nonoccurence restrict : ions ( FCRs ) . 
In [ 8 ] , we divided FCRs into co , j , active and ditz fictive . 
A conjunctive FCI/ . 
is a constraint of the following formal i [ ' a.n object is of ; ~ cert ; fin kind then ill deserves certain with dues of certitude kinds An FCI~ stat : ing tha, 2 a. verb must Howe v and N features with values A- and -respectively is all example of a. conjunctive FCI { . 
A disjunctive I '' CI { . 
is of the form : l Rachel ] roll qysl.em was implemented in Quintus Prolog by Dale ( legerdemain and ' [ Shiloh ] Stz . 
if an object is of a. celibate then it deserves cert akin ca, 1 tll'C~s with vMues of certain kinds , or it deserves certain pei'ha.liS other ) fea. 1 u res evil h viii of terrain pergolas other ) kinds , or ... 
( 31 : it i : lesser . ; s i : erl ; akin lethal S other ) fea, 1 ll res Vi , l. [ ll ( ~S o [ certain ( perhaps other ) khi , < ls lo : :I exam nipple the following F ( ' , |/ . 
sl.a.t.iug , t inverCed verbs lilt|S1 , lie auxiliary tries is disjunctive : a verb Ilitisl ; hare the [ ' ( ~il.l.tll ( ~s INV and AUX with valises d a.Iid I , -a.iitl i L- , or - ; Mid -respectivel.y . Both o| these |el'illS or l , ' ( ' , lls iiHly I ) ( ! 
expressed in a. foi'llla.iiSlli shipload ~ fiiiil.e , Myrtia . [ order ( Type , E ) o| types killdeer sub-  8illnptioli a , finite sel . 
Feat of ro ; ./.t tll . ( ~s , and an approx privateness , ial rliilcl.ion : Type X Feat -~ Type . 
[ intuitively the l , types I ; lie notion ol '' kinds + , j '' object t g : t , ' ill ' capon , of tyl > e t ' i~ < i Mso of l ; Ylle L , il , ll ( ] Approp ( l , f ) = lI ill ' ( ! ; i ( ' [ I object oF type t deserves [ eaA.urt~ f wil . ] i : i . Vi./ . ] lle or type ft. ~ @ 'e call S/IC ] I it . 
[ Ol'tll ; liiSlll i-i , ii ; I , ] ) l ) l '' Opl ' ] al , polio ~/ fOl'lllil ] i~ ; lll . 
( ' , iLl'- peliLel '' , s AI , F , and ( , Ardelia . 
i ; ill ( | ( i ( ~t , z 's Troll are ex : -t.niples o| illilllenienl.a.Lions o| a , pF , ro ] ) ria , Loliess |or ill iSlil , s . l low an a.i ) appropriateness orniaJisnl enc les a conjunctive I : ( ' , R is ob\ . 'i < > us~ bll ( . 
llOW it encodes a disjunctive I '' ( ',1 { is less so . 
Ali example ] usl ; ral ; es best how it . 
is done . 
~Ul ) pOS0 that F ( ',1 { [ i sl.al.es , ob- toeclips if type t deserve 
[ ( ! a . [ ./ll ( ! S f and , I ) oth with boolea.I/ dues ( I [ Hell's [ lel'lllOF ( ~ that the valises of f ail g iil/lSl Aler ! e , [ > is the disjunct ] w ! I '' ( 111 . 
if a , u object is o [ type l then it deserve s f with value and q with due , or it deserts f with value 9 with value - To  0ncode 3 > first iul , rodLiCe sultanates t ~ ; +l.ll [ l '' of I ( 1 E I/ , 1. # # ) , O11 ( ! 
SUl ) tyl ) e [ ' ( ) l ' ea , ch disjunct the consequent of . 
Then encode the ] 'ea.tli 'e/wthl~.~ 'on ( ! il.illliS in l , he [ first disjunct ILy putting ( t ' , ./ ) : : ~-a , nd Approp ( //~ q ) -+ , and encode the I'eature/value conditions in the second dis-juu ( : t by putting Approp ( t ' , f ) = - . 
and Approp ( t ' , g ) = . . '2 This a uproar ch Ina , kes two ill ort ; a , lll , closed-world type assumptions a , bouL ( .he types titling Slll ) SlllIle 11o other types ( hellCe- forth species ) , l : first the p ; partition states that for each type t , if a.n object is ( 31 ' type t the the object is of ex-ax-I.ly o11 ( 2 species subsumed by t. Second , the all-or-nothing condition , tes that 1 ' ( 31 ' each species , q audited f , either every el '' IIO ol > , incl or species s deserves feature . # c.3 All a.l ) ltroltriM , elites orli+ia.lisill ] l a.s ALl : , ( [ 2 ] , [ 3 ] ) ti , ; t.l . does not quiet both conditions llOt ; ] roper y el|cOde a , disjunct '- five l '' ( : l/ . 
For example consider disjunctive I '' CI { . 
p. An a.I ) prl ; ) primal elleSS [ hernial iSlli I/lily l/O ( properly encode 1 , hit t / a.lld t '' I'll rt , sell MI valid the disjunct s ill the COll.qeqll ( Hlt or [ i wiLhout the i ) Arly inion ] son . 
< till a.llln'ol brittleness orlila.liSlll ilia y IIOl . 
for the type l , I.he path ( fg ) lakes a varied I ) y . % one lust hll , ro duce the chain ( / , f ) = . , , Approp ( 'a , g ) = .~ . 
well-typable iff the feature structure subsumes a well-typed feature structure , in ALl . : , type inferencing is employed to ensure that all feature structures are well-typable -- in fact , all feature structures are well typed . 
Let type resolution be the total function R : - > DRFS such that R ( F ) is the set of all resolved of F. Guided by the partition and all-or-nothing conditions , King [ 13 ] has formulated a semantics of feature structures and developed a notion of a satisfiable feature structure such that F E FS is satisfiable iff R ( F ) 0 . 
The Troll system , which is based on this idea , effectively implements type resolution . 
Why does type resorption succeed where . 
types inferencing fails ? 