Robust pronoun resolution with limited knowledge
Most traditional approaches to anaphora resolution rely heavily on linguistic and domain knowledge.
One of the disadvantages of developing a knowledgeÃÂ­ based system, however, is that it is a very labourÃÂ­ intensive and time-consuming task.
This paper presÃÂ­ ents a robust, knowledge-poor approach to resolving pronouns in technical manuals, which operates on texts pre-processed by a part-of-speech tagger.
Co reference resolution is a field in which major progress has been made in the last decade . 
Candidates are assigned scores by each indicator and the candidate with the highest score is returned as the antecedent.
Some of the limitations of the traditional rule based approaches ( Mitkov , 1998 ) could be overcome by machine learning techniques , which allow automating the acquisition of knowledge from annotated corpora . 
( Mitkov , 1998 ; Poesio et al. , 2002 ; Markert and Nissim , 2005 ) ) , machine learning methods were embraced ( cf . 
`` Non-prepositional '' noun phrases A `` pure '' , `` non-prepositional '' noun phrase is given a higher preference than a noun phrase which is part of a prepositional phrase ( 0 , -1 ) . 
For the most part , anaphora resolution has focused on traditional linguistic methods ( Carbonell & Brown 1988 ; Carter 1987 ; Hobbs 1978 ; Ingria & Stallard 1989 ; Lappin & McCord 1990 ; Lappin & Leass 1994 ; Mitkov 1994 ; Rich & LuperFoy 1988 ; Sidner 1979 ; Webber 1979 ) . 
However , to represent and manipulate the various types of linguistic and domain knowledge involved requires considerable human input and computational expense . 
While various alternatives have been proposed , making use of e.g . neural networks , a situation seÂ­ antics framework , or the principles of reasoning with uncertainty ( e.g . Connoly et al . 1994 ; Mitkov 1995 ; Tin & Akman 1995 ) , there is still a strong need for the development of robust and effective strategies to meet the demands of practical NLP systems , and to enhance further the automatic proÂ­ cussing of growing language resources . 
Several proposals have already addressed the anaphora resolution problem by deliberately limiting the extent to which they rely on domain Andros linguistic knowledge ( Baldwin 1997 ; Dagan & ital 1990 ; Kennedy & Boguraev 1996 ; Mitkov 1998 ; Nasukawa 1994 ; Williams et al . 1996 ) . 
Our work is a continuation of these latest trends in the search for inexpensive , fast and reliable procedures for anaphÂ­ ora resolution . 
It is also an example of how anaphora in a specific genre can be resolved quite successfully without any sophisticated linguistic knowledge or even without parsing . 
Finally , our evaluation shows that the basic set of antecedent tracking indicators can work well not only for English , but also for other languages ( in our case Polish and Arabic ) . 
With a view to avoiding complex syntactic , semanÂ­ tic and discourse analysis ( which is vital for realÂ­ world applications ) , we developed a robust , knowlÂ­ edge-poor approach to pronoun resolution which does not parse and analysis the input in order to identify antecedents of anaphora . 
It makes use of only a part-of-speech tagger , plus simple noun phrase rules ( sentence constituents are identified at the level of noun phrase at most ) and operates on the basis of antecedent-tracking preferences ( referred to hereafter as `` antecedent indicators '' ) . 
For anaphora in simple sentences , noun phrases in the previous senÂ­ sentence are the best candidate for antecedent , followed by noun phrases situated 2 sentences further back and finally nouns 3 sentences further back { 1 , 0 , -1 ) . 
The approach works as follows : it takes as an input the output of a text processed by a part-of-speech tagger , identifies the noun phrases which precede the anaphora within a distance of 2 sentences , checks them for gender and number agreement with the anaphora and then applies the genre-specific antecedent indicators to the reÂ­ raining candidates ( see next section ) . 
The noun phrase with the highest aggregate score is proposed as antecedent ; in the rare event of a tie , priority is given to the candidate with the higher score for imÂ­ mediate reference . 
If immediate reference has not been identified , then priority is given to the Candi date with the best collocation pattern score . 
If this does not help , the candidate with the higher score for indicating verbs is preferred . 
If still no choice is possible , the most recent from the remaining candiÂ­ dates is selected as the antecedent . 
2.1 Antecedent indicators . 
Antecedent indicators ( preferences ) play a decisive role in tracking down the antecedent from a set of possible candidates . 
Candidates are assigned a score ( -1 , 0 , 1 or 2 ) for each indicator ; the candidate with the highest aggregate score is proposed as the anteÂ­ cement . 
The antecedent indicators have been identiÂ­ fie empirically and are related to salience ( definiteness , givenness , indicating verbs , lexical reiteration , section heading preference , `` nonÂ­ prepositional '' noun phrases ) , to structural matches ( collocation , immediate reference ) , to referential distance or to preference of terms . 
Whilst some of the indicators are more genre-specific ( term preferÂ­ enc and others are less genre-specific ( `` immediate reference '' ) , the majority appear to be genreÂ­ independent . 
In the following we shall outline some the indicators used and shall illustrate them by exÂ­ ample . 
Definiteness Definite noun phrases in previous sentences are more likely antecedents of pronominal anaphora than indefinite ones ( definite noun phrases score 0 and indefinite ones are penalty by -1 ) . 
We regard a noun phrase as definite if the head noun is modified by a definite article , or by demonstrative or possesÂ­ give pronouns . 
This rule is ignored if there are no definite articles , possessive or demonstrative proÂ­ nouns in the paragraph ( this exception is taken into account because some English user 's guides tend to omit articles ) . 
Givenness Noun phrases in previous sentences representing the `` given information '' ( theme ) 1 are deemed good candidates for antecedents and score I ( candidates not representing the theme score 0 ) . 
In a coherent text ( Firbas 1992 ) , the given or known information , or theme , usually appears first , and thus forms a coÂ­ referential link with the preceding text . 
The new information , or heme provides some information about the theme . 
1We use the simple heuristics that the given information is the first noun phrase in a non-imperative sentence . 
Indicating verbs If a verb is a member of the Verb_set = { discuss , present , illustrate , identify , summarize examine , describe , define , show , check , develop , review , reÂ­ port , outline , consider , investigate , explore , assess , analysis synthesis study , survey , deal , cover } , we consider the first NP following it as the preferred anÂ­ antecedent scores 1 and 0 ) . 
Evaluation shows a success rate of 89.7 % for the genre of techÂ­ finical manuals and at least in this genre , the approach appears to be more successful than other similar methods . 
Empirical evidence sugÂ­ tests that because of the salience of the noun phrases which follow them , the verbs listed above are particularly good indicators . 
Mitkov ( 1998 ) obtains a success rate of 89.7 % for pronominal references , working with English technical manuals . 
Lexical reiteration Lexically reiterated items are likely candidates for antecedent ( a NP scores 2 if is repeated within the same paragraph twice or more , 1 if repeated once and 0 if not ) . 
languages An attractive feature of any NLP approach would be its language `` universality '' . 
Lexically reiterated items include reÂ­ pated synonymous noun phrases which may often be preceded by definite articles or demonstratives . 
Also , a sequence of noun phrases with the same head counts as lexical reiteration ( e.g . `` toner bottle '' , `` bottle of toner '' , `` the bottle '' ) . 
While we acknowledge that most of the monolingual NLP approaches are not automatically transferable ( with the same degree of efficiency ) to other languages , it would be highly desirable if this could be done with minimal adaptaÂ­ son . 
Section heading preference If a noun phrase occurs in the heading of the section , part of which is the current sentence , then we conÂ­ sider it as the preferred candidate ( 1 , 0 ) . 
Example : Insert the cassette into the VCR making sure iti is suitable for the length of recording . 
Here `` the VCR '' is penalty -1 ) for being part of the prepositional phrase `` into the VCR '' . 
The robust approach adapted for Polish demonstrated a high success rate of 93.3 % in resolvÂ­ ing anaphora with critical success rate of 86.2 % ) . 
This preference can be explained in terms of saliÂ­ enc from the point of view of the centering theory . 
The latter proposes the ranking `` subject , direct obÂ­ sect indirect object '' ( Brennan et al . 1987 ) and noun phrases which are parts of prepositional phrases are usually indirect objects . 
Similarly to the evaluation for English , we comÂ­ pared the approach for Polish with ( i ) a Baseline Model which discounts candidates on the basis of agreement in number and gender and , if there were still competing candidates , selects as the antecedent the most recent subject matching the anaphora in gender and number ( ii ) a Baseline Model which checks agreement in number and gender and , if there were still more than one candidate left , picks up as the antecedent the most recent noun phrase that agrees with the anaphora . 
Collocation pattern preference This preference is given to candidates which have an identical collocation pattern with a pronoun ( 2,0 ) . 
Our preference-based approach showed clear suÂ­ priority over both baseline models . 
The collocation preference here is restricted to the patterns `` noun phrase ( pronoun ) , verb '' and `` verb , noun phrase ( pronoun ) '' . 
Owing to lack of syntactic information , this preference is somewhat weaker than the collocation preference described in ( Dagan & ital 1990 ) . 
Example : Press the key down and turn the volume up ... 
Press iti again . 
Immediate reference In technical manuals the `` immediate reference '' clue can often be useful in identifying the antecedent . 
We have also adapted and evaluated the approach for Polish ( 93.3 % success rate ) and for Arabic ( 95.2 % success rate ) . 
We have recently adapted the approach for AraÂ­ bic as well ( Mitkov & Belguith 1998 ) . 
The heuristics used is that in constructions of the form `` ... ( You ) V 1 NP ... con ( you ) V 2 it ( con ( you ) V3 it ) '' , where con e { and/or/before/after ... } , the noun phrase immediately after V 1 is a very likely candidate for antecedent of the pronoun `` it '' immeÂ­ mediately following V2 and is therefore given preference ( scores 2 and 0 ) . 
Input is checked against agreement and for a number of antecedent indicators . 
It is also quite freÂ­ Quent with imperative constructions . 
Example : To print the paper , you can stand the printer up or lay iti flat . 
To turn on the printer , press the Power button and hold iti down for a moment . 
Unwrap the paperiness form iti and align  then load iti into the drawer . 
Referential distance In complex sentences , noun phrases in the previous clause 2 are the best candidate for the antecedent of an anaphora in the subsequent clause , followed by noun phrases in the previous sentence , then by nouns situated 2 sentences further back and finally nouns 3 sentences further back ( 2 , 1 , 0 , -1 ) . 
Term preference NPs representing terms in the field are more likely to be the antecedent than NPs which are not terms ( score 1 if the NP is a term and 0 if not ) . 
Most traditional approaches to anaphora resolution rely heavily on linguistic and domain knowledge . 
We used the robust approach as a basis for develÂ­ oping a genre-specific reference resolution approach in Polish . 
 2 1dentification of clauses in complex sentences is do e heuristically . 
As already mentioned , each of the antecedent inÂ­ indicators assigns a score with a value { -1 , 0 , 1 , 2 } . 
Top symptoms like `` lexical reiteration '' asÂ­ sign score `` 2 '' whereas `` non-prepositional '' noun phrases are given a negative score of `` -1 '' . 
Evaluation reports a success rate of 89.7 % which is better than the sucÂ­ less rates of the approaches selected for comparison and tested on the same data . 