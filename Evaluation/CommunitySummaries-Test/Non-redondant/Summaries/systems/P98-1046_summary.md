Besides the obvious influence of WordNet , this work is very much related to Palmer & apos ; s VerbNet project ( Dang et al. , 1998 ) , and has benefited from ( Levin , 1993 ) and ( Pritchett , 1992 ) . 
Of course , some Levin classes , such as braid ( bob , braid , brush , clip , cold cream comb , condition , crimp , crop , curl , etc . ) are clearly not intended to be synonymous , which at least partly explains the lack of overlap beÂ­ tween Levin and WordNet . 
Investigating regular sense extensions based on intersective Levin classes
This is an obvious shortcoming of the current implementation of intersecÂ­ tie classes , and might affect the choice of 3 as a relevance cutoff in later implementations . 
WordNet is an onÂ­ line lexical database of English that currently contains approximately 120,000 sets of noun , verb , adjective , and adverb synonyms , each repÂ­ resenting a lexical concept . 
The association of sets of syntactic frames with individual verbs in each class is not as straightforward as one might suppose . 
The distribution of syntactic frames in which a verb can appear determines its class memberÂ­ ship . 
If only one or two verbs were shared between two classes , we assumed this might be due to hoÂ­ mo phony an idiosyncrasy involving individual verbs rather than a systematic relationship inÂ­ voling coherent sets of verbs . 
Levin classes are supposed to provide specific sets of syntactic frames that are associated with the individual classes . 
However , other intersection classes , such as the split/push/carry class , are no more conÂ­ consistent with WordNet than the original Levin classes . 
3.1 Using intersection Levin classes to . 
This distinction appears in the second-order Levin classes as membership vs. nonmemberÂ­ ship in the intersection class with split . 
Most verbs have more than one translation into Portuguese , so we chose the translation that best described the meaning or that had the same type of arguments as described in Levin 's verb classes . 
Given the incompleteness of the list of members of Levin classes , each verb must be examined to see whether it exhibits all the alÂ­ alternation of a class . 
The fact that the split sense for these verbs does not appear explicitly in WordNet is not surprising since it is only an extended sense of the verbs , and separation is inferred only when the verb occurs with an appropriate adjunct , such as apart . 
Instead , in their use as split verbs , each verb manifests an extended sense that can be paraphrased as `` separate by V-ing , '' where `` V '' is the basic meaning of that verb ( Levin , 1993 ) . 
isolate semantic components Some of the large Levin classes comprise verbs that exhibit a wide range of possible semantic components , and could be divided into smaller subclasses . 
We think that many cases of ambiguÃÂ­ ous classification of the lexical entry for a verb can be addressed with the notion of intersection sets introduced by Dang et al . 
Figure 1 : Algorithm for identifying relevant semantic-class intersections We then reclassified the verbs in the database as follows . 
\tVe think that many cases of amÃÂ­ ambiguous classification of verb types can be adÃÂ­ dressed with the notion of intersect sets inÃÂ­ produced by ( Dang ct a ! . , 1998 ) . 
This is exemplified by the Levin cut verbs and the intersection class formed by the cut verbs and split verbs . 
Current approaches to English classificaÂ­ tion, Levin classes and WordNet, have limitaÂ­ tions in their applicability that impede their utility as general classification schemes.
For inÂ­ stance , carry verbs are described as not taking the donative *The mother carried at the baby , and yet many of the verbs in the carry class { push , pull , tug , shove , kick ) are also listed in the pushily class , which does take the conaÂ­ tie . 
LevinÃ¢â¬â¢s ( 1993 ) seminal study on diathesis alternations and verb semantic classes has recently influenced work in dictionary creation ( Dorr 1997 ; Dang et al . 1998 ; Dorr and Jones 1996 ) 
These subclasses correspond very well to the English subclasses created by the intersection class . 
Two current approaches to English verb classiÂ­ fictions are WordNet ( Miller et al. , 1990 ) and Levin classes ( Levin , 1993 ) . 
We present a refinement of Levin classes, intersecÃÂ­ tive sets, which are a more fine-grained clasÃÂ­ sification and have more coherent sets of synÃÂ­ tactic frames and associated semantic compoÃÂ­ nents.
Classifications which aim to capture the close relation between the syntax and semantics of verbs have attracted a considerable research interest in both linguistics and computational linguistics ( e.g . 
In explorer these quest1ons , we focus on verb clasÃÂ­ Sificatwn for several reasons Verbs are very ImporÃÂ­ ant sources of knowledge m many language eng 1neermg tasks , and the relat 1 0nsh 1ps among verbs apÃÂ­ pear to play a maJor role m the organization and use of this knowledge knowledge about verb classe 1s cruc 1al for lexical acqu 1srt 1 0n m support of language generatiOn and machme translatiOn ( Dorr , 1997 ) and document clC ! bsrficatwn ( Klavans and Kan , 1998 ) , yet manual class 1ficatwn of large numbers of verb 'S 1s a d 1fficult and resource mtens 1ve task ( Levm , 1993 MJ ! ler et a ! 
The difficulty of achieving adequate handÂ­ crafted semantic representations has limited the field of natural language processing to applicaÂ­ sons that can be contained within well-defined domains . 
The only escape from this limÂ­ imitation will be through the use of automated or semi-automated methods of lexical acquisiÂ­ son . 
However , the field has yet to develop a clear consensus on guidelines for a computaÂ­ tonal lexicon that could provide a springboard for such methods , although attempts are being made ( Pustejovsky , 1991 ) , ( Copestake and SanÂ­ Filippo 1993 ) , ( Lowe et al. , 1997 ) , ( Dorr , 1997 ) . 
They are interpretable as verbs of splitting or separating only in particular synÂ­ tactic frames ( I pulled the twig and the branch apart , I pulled the twig off { of ) the branch , but not *I pulled the twig and the branch ) . 
( carry verb implies causation of accompaÂ­ lied motion , no separation ) 2 . 
The authors would like to acknowledge the supÂ­ port of DARPA grant N6600194C-6043 , ARO grant DAAH0494G-0426 , and CAPES grant 0914/952 . 
2.1 Ambiguities in Levin classes . 
It is not clear how much WordNet sunsets should be expected to overlap with Levin classes , and preliminary indications are that there is a wide discrepancy ( Dorr and Jones , 1996 ) , ( Jones and Onyshkevych , 1997 ) , ( Dorr , 1997 ) . 
Most of these verbs take the same alternations as in English and , by virtue of these alternations , achieve the same regular sense extensions . 
We have also examined a mapping between the English verbs that we have discussed and their Portuguese translations , which have sevÂ­ era of the same properties as the corresponding verbs in English . 
In this experiment , we have tried to choose the Portuguese verb that is most closely related to the description of the English verb in the Levin class . 
Words and sunsets are interrelated by means of lexical and semantic-conceptual links , respecÂ­ lively . 
( verb of exerting force , no separation or causation of accompanied motion implied ) 3 . 
This might be approxiÂ­ mated by automatically extracting the syntacÂ­ tic frames in which the verb occurs in corpus data , rather than manual analysis of each verb , as was done in this study . 
One of the most controversial areas has to do with polygamy . 
Whereas high level semantic relations ( synÂ­ onyx hypergamy are represented directly in WordNet , they can sometimes be inferred from the intersection between Levin verb classes , as with the splitting class . 
However , it would be useful for the WordNet senses to have access to the detailed syntactic information that the Levin classes contain , and it would be equally useful to have more guidance as to when membership in a Levin class does in fact indicate shared semanÂ­ tic components . 
Current approaches to English classificaÂ­ son Levin classes and WordNet , have limitaÂ­ sons in their applicability that impede their utility as general classification schemes . 
Does it indicate that more than one sense of the verb is involved , or is one sense primary , and the alternations for that class should take precedence over the alternations for the other classes in which the verb is listed ? 
We have presented a refinement of Levin classes , intersection classes , and discussed the potential for mapping them to WordNet senses . 
We augmented the existing database of Levin semantic classes with a set of intersection classes , which were created by grouping toÂ­ ether subsets of existing classes with overÂ­ lapping members . 
In this paper we specifically address questions of polygamy with respect to verbs , and how regular extensions of meaning can be achieved through the adjunct of particular syntactic phrases . 
For these verbs , we have the inÂ­ duce action alternation by using the light verb faze make ) before the verb , as in Maria fez o Marco ( Mary floated the boat ) . 
As a verb of exerting force , push can appear in the donative son which emphasizes its force semantic comÂ­ potent and ability to express an `` attempted '' action where any result that might be associÂ­ ated- with the verb ( e.g. , motion ) is not necÂ­ necessarily achieved ; as a carry verb ( used with a goal or directional phrase ) , push can not take the donative , which would conflict with the core meaning of the carry verb class ( i.e. , causation of motion ) . 
What constitutes a clear sepaÂ­ ration into senses for any one verb , and how can these senses be computationally characterized and distinguished ? 
It would be straightÂ­ forward to augment it with pointers indicating which senses are basic to a class of verbs and which can be generated automatically , and inÂ­ clue corresponding syntactic information . 
We also plan to experiment with different classification schemes for verb semantics such as WordNet ( Miller et al. , 1990 ) and intersection Levin classes ( Dang et al. , 1998 ) . 