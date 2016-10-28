Robust pronoun resolution with limited knowledge
Most traditional approaches to anaphora resolution rely heavily on linguistic and domain knowledge.
One of the disadvantages of developing a knowledgeÃÂ­ based system, however, is that it is a very labourÃÂ­ intensive and time-consuming task.
This paper presÃÂ­ ents a robust, knowledge-poor approach to resolving pronouns in technical manuals, which operates on texts pre-processed by a part-of-speech tagger.
Co reference resolution is a field in which major progress has been made in the last decade . 
Candidates are assigned scores by each indicator and the candidate with the highest score is returned as the antecedent.
Some of the limitations of the traditional rule based approaches ( Mitkov , 1998 ) could be overcome by machine learning techniques , which allow automating the acquisition of knowledge from annotated corpora . 
( Mitkov , 1998 ; Poesio et al. , 2002 ; Markert and Nissim , 2005 ) ) , machine learning methods were embraced ( cf . 
For the most part , anaphora resolution has focused on traditional linguistic methods ( Carbonell & Brown 1988 ; Carter 1987 ; Hobbs 1978 ; Ingria & Stallard 1989 ; Lappin & McCord 1990 ; Lappin & Leass 1994 ; Mitkov 1994 ; Rich & LuperFoy 1988 ; Sidner 1979 ; Webber 1979 ) . 
However , to represent and manipulate the various types of linguistic and domain knowledge involved requires considerable human input and computational expense . 
While various alternatives have been proposed , making use of e.g . neural networks , a situation seÂ­ antics framework , or the principles of reasoning with uncertainty ( e.g . Connoly et al . 1994 ; Mitkov 1995 ; Tin & Akman 1995 ) , there is still a strong need for the development of robust and effective strategies to meet the demands of practical NLP systems , and to enhance further the automatic proÂ­ cussing of growing language resources . 
Several proposals have already addressed the anaphora resolution problem by deliberately limiting the extent to which they rely on domain Andros linguistic knowledge ( Baldwin 1997 ; Dagan & ital 1990 ; Kennedy & Boguraev 1996 ; Mitkov 1998 ; Nasukawa 1994 ; Williams et al . 1996 ) . 
Our work is a continuation of these latest trends in the search for inexpensive , fast and reliable procedures for anaphÂ­ ora resolution . 
It is also an example of how anaphora in a specific genre can be resolved quite successfully without any sophisticated linguistic knowledge or even without parsing . 
Finally , our evaluation shows that the basic set of antecedent tracking indicators can work well not only for English , but also for other languages ( in our case Polish and Arabic ) . 
With a view to avoiding complex syntactic , semanÂ­ tic and discourse analysis ( which is vital for realÂ­ world applications ) , we developed a robust , knowlÂ­ edge-poor approach to pronoun resolution which does not parse and analysis the input in order to identify antecedents of anaphora . 
`` Non-prepositional '' noun phrases A `` pure '' , `` non-prepositional '' noun phrase is given a higher preference than a noun phrase which is part of a prepositional phrase ( 0 , -1 ) . 
It makes use of only a part-of-speech tagger , plus simple noun phrase rules ( sentence constituents are identified at the level of noun phrase at most ) and operates on the basis of antecedent-tracking preferences ( referred to hereafter as `` antecedent indicators '' ) . 
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
For anaphora in simple sentences , noun phrases in the previous senÂ­ sentence are the best candidate for antecedent , followed by noun phrases situated 2 sentences further back and finally nouns 3 sentences further back { 1 , 0 , -1 ) . 
1We use the simple heuristics that the given information is the first noun phrase in a non-imperative sentence . 
Empirical evidence sugÂ­ tests that because of the salience of the noun phrases which follow them , the verbs listed above are particularly good indicators . 
Lexically reiterated items include reÂ­ pated synonymous noun phrases which may often be preceded by definite articles or demonstratives . 
Also , a sequence of noun phrases with the same head counts as lexical reiteration ( e.g . `` toner bottle '' , `` bottle of toner '' , `` the bottle '' ) . 
The new information , or heme provides some information about the theme . 
Indicating verbs If a verb is a member of the Verb_set = { discuss , present , illustrate , identify , summarize examine , describe , define , show , check , develop , review , reÂ­ port , outline , consider , investigate , explore , assess , analysis synthesis study , survey , deal , cover } , we consider the first NP following it as the preferred anÂ­ antecedent scores 1 and 0 ) . 
Lexical reiteration Lexically reiterated items are likely candidates for antecedent ( a NP scores 2 if is repeated within the same paragraph twice or more , 1 if repeated once and 0 if not ) . 
Section heading preference If a noun phrase occurs in the heading of the section , part of which is the current sentence , then we conÂ­ sider it as the preferred candidate ( 1 , 0 ) . 
Example : Insert the cassette into the VCR making sure iti is suitable for the length of recording . 
Here `` the VCR '' is penalty -1 ) for being part of the prepositional phrase `` into the VCR '' . 
This preference can be explained in terms of saliÂ­ enc from the point of view of the centering theory . 
The latter proposes the ranking `` subject , direct obÂ­ sect indirect object '' ( Brennan et al . 1987 ) and noun phrases which are parts of prepositional phrases are usually indirect objects . 
Collocation pattern preference This preference is given to candidates which have an identical collocation pattern with a pronoun ( 2,0 ) . 
The collocation preference here is restricted to the patterns `` noun phrase ( pronoun ) , verb '' and `` verb , noun phrase ( pronoun ) '' . 
Owing to lack of syntactic information , this preference is somewhat weaker than the collocation preference described in ( Dagan & ital 1990 ) . 
Example : Press the key down and turn the volume up ... 
Press iti again . 
Immediate reference In technical manuals the `` immediate reference '' clue can often be useful in identifying the antecedent . 
The heuristics used is that in constructions of the form `` ... ( You ) V 1 NP ... con ( you ) V 2 it ( con ( you ) V3 it ) '' , where con e { and/or/before/after ... } , the noun phrase immediately after V 1 is a very likely candidate for antecedent of the pronoun `` it '' immeÂ­ mediately following V2 and is therefore given preference ( scores 2 and 0 ) . 
Input is checked against agreement and for a number of antecedent indicators . 
It is also quite freÂ­ Quent with imperative constructions . 
Example : To print the paper , you can stand the printer up or lay iti flat . 
To turn on the printer , press the Power button and hold iti down for a moment . 
Unwrap the paperiness form iti and align  then load iti into the drawer . 
Referential distance In complex sentences , noun phrases in the previous clause 2 are the best candidate for the antecedent of an anaphora in the subsequent clause , followed by noun phrases in the previous sentence , then by nouns situated 2 sentences further back and finally nouns 3 sentences further back ( 2 , 1 , 0 , -1 ) . 
Term preference NPs representing terms in the field are more likely to be the antecedent than NPs which are not terms ( score 1 if the NP is a term and 0 if not ) . 
 2 1dentification of clauses in complex sentences is do e heuristically . 
As already mentioned , each of the antecedent inÂ­ indicators assigns a score with a value { -1 , 0 , 1 , 2 } . 
These scores have been determined experimentally on an empirical basis and are constantly being upÂ­ dated . 
Top symptoms like `` lexical reiteration '' asÂ­ sign score `` 2 '' whereas `` non-prepositional '' noun phrases are given a negative score of `` -1 '' . 
We should point out that the antecedent indicators are preferences and not absolute factors . 
There might be cases where one or more of the antecedent indicators do not `` point '' to the correct antecedent . 
For inÂ­ stance , in the sentence `` Insert the cassette into the VCRi making sure iti is turned on '' , the indicator `` non-prepositional noun phrases '' would penalty the correct antecedent . 
When all preferences ( antecedent indicators ) are taken into account , however , the right antecedent is still very likely to be tracked down - in the above example , the `` non-prepositional noun phrases '' heuristics ( penalty ) would be overturned by the `` collocation preference '' heuristics . 
2.2 Informal description of the algorithm . 
Evaluation shows a success rate of 89.7 % for the genre of techÂ­ finical manuals and at least in this genre , the approach appears to be more successful than other similar methods . 
The algorithm for pronoun resolution can be deÂ­ scribed informally as follows : 1 . 
Examine the current sentence and the two preÂ­ . 
ceding sentences ( if available ) . 
Mitkov ( 1998 ) obtains a success rate of 89.7 % for pronominal references , working with English technical manuals . 
We have also adapted and evaluated the approach for Polish ( 93.3 % success rate ) and for Arabic ( 95.2 % success rate ) . 
Look for noun phrases 3 only to the left of the anaphor 4 2 . 
languages An attractive feature of any NLP approach would be its language `` universality '' . 
Select from the noun phrases identified only . 
those which agree in gender and numberS with the pronominal anaphora and group them as a set of potential candidates 
ital candidate and assign scores ; the candidate with the highest aggregate score is proposed as 3A sentence splitter would already have segmented the text into sentences , a POS tagger would already have determined the parts of speech and a simple phrasal grammar would already have detected the noun phrases 4In this project we do not treat anaphora non-anaphoric `` it '' occurring in constructions such as `` It is important '' , `` It is necessary '' is eliminated by a `` referential filter '' 5Note that this restriction may not always apply in lanÂ­ gages other than English ( e.g . German ) ; on the other hand , there are certain collective nouns in English which do not agree in number with their antecedents ( e.g . `` government '' , `` team '' , `` parliament '' etc . can be referred to by `` they '' ; equally some plural nouns ( e.g . `` data '' ) can be referred to by `` it '' ) and are exempted from the agreeÂ­ met test . 
While we acknowledge that most of the monolingual NLP approaches are not automatically transferable ( with the same degree of efficiency ) to other languages , it would be highly desirable if this could be done with minimal adaptaÂ­ son . 
For this purpose we have drawn up a compreÂ­ tensive list of all such cases ; to our knowledge , no other computational treatment of pronominal anaphora resoluÂ­ son has addressed the problem of `` agreement excepÂ­ sons . 
antecedent . 
If two candidates have an equal score , the candidate with the higher score for immediate reference is proposed as antecedent . 
If immediate reference does not hold , propose the candidate with higher score for collocation pattern . 
The robust approach adapted for Polish demonstrated a high success rate of 93.3 % in resolvÂ­ ing anaphora with critical success rate of 86.2 % ) . 
If collocation pattern suggests a tie or does not hold , select the candidate with higher score for indicating verbs . 
If this indicator does not hold again , go for the most recent candidate . 
Similarly to the evaluation for English , we comÂ­ pared the approach for Polish with ( i ) a Baseline Model which discounts candidates on the basis of agreement in number and gender and , if there were still competing candidates , selects as the antecedent the most recent subject matching the anaphora in gender and number ( ii ) a Baseline Model which checks agreement in number and gender and , if there were still more than one candidate left , picks up as the antecedent the most recent noun phrase that agrees with the anaphora . 
Our preference-based approach showed clear suÂ­ priority over both baseline models . 
3 . 
We have recently adapted the approach for AraÂ­ bic as well ( Mitkov & Belguith 1998 ) . 
Most traditional approaches to anaphora resolution rely heavily on linguistic and domain knowledge . 
We used the robust approach as a basis for develÂ­ oping a genre-specific reference resolution approach in Polish . 
Evaluation . 
For practical reasons , the approach presented does not incorporate syntactic and semantic information ( other than a list of domain terms ) and it is not realÂ­ is tic to expect its performance to be as good as an approach which makes use of syntactic and semantic knowledge in terms of constraints and preferences . 
The lack of syntactic information , for instance , means giving up c-cornmand constraints and subject preference ( or on other occasions object preference , see Mitkov I995 ) which could be used in center tracking . 
Syntactic parallelism , useful in discrimiÂ­ eating between identical pronouns on the basis of their syntactic function , also has to be forgone . 
Lack of semantic knowledge rules out the use of verb seÂ­ antics and semantic parallelism . 
Our evaluation , however , suggests that much less is lost than might be feared . 
In fact , our evaluation shows that the reÂ­ cults are comparable to syntax-based methods ( Lappin & Leass I994 ) . 
We believe that the good success rate is due to the fact that a number of anteÂ­ cement indicators are taken into account and no facÂ­ tor is given absolute preference . 
In particular , this strategy can often override incorrect decisions linked with strong centering preference ( Mitkov & Belguith I998 ) or syntactic and semantic parallelism preferÂ­ hences see below ) . 
3.1 Evaluation A . Our first evaluation exercise ( Mitkov & Stys 1997 ) was based on a random sample text from a technical manual in English ( Minolta 1994 ) . 
Evaluation reports a success rate of 89.7 % which is better than the sucÂ­ less rates of the approaches selected for comparison and tested on the same data . 
There were 71 pronouns in the 140 page technical manual ; 7 of the pronouns were non-anaphoric and 16 anaphoric . 
The resolution of anaphora was carried out with a sucÂ­ less rate of 95.8 % . 
The approach being robust ( an attempt is made to resolve each anaphora and a proÂ­ posed antecedent is returned ) , this figure represents both `` precision '' and `` recall '' if we use the MUC terminology . 
To avoid any terminological confusion , we shall therefore use the more neutral term `` success rate '' while discussing the evaluation . 
In order to evaluate the effectiveness of the apÂ­ roach and to explore if I how far it is superior over the baseline models for anaphora resolution , we also tested the sample text on ( i ) a Baseline Model which checks agreement in number and gender and , where more than one candidate remains , picks as anteceÂ­ dent the most recent subject matching the gender and number of the anaphora ii ) a Baseline Model which picks as antecedent the most recent noun phrase that matches the gender and number of the anaphora 
The success rate of the `` Baseline Subject '' was 29.2 % , whereas the success rate of `` Baseline Most Recent NP '' was 62.5 % . 
Given that our knowledgeÂ­ poor approach is basically an enhancement of a baseline model through a set of antecedent indicaÂ­ tors , we see a dramatic improvement in performance ( 95.8 % ) when these preferences are called upon . 
Typically , our preference-based model proved superior to both baseline models when the anteceÂ­ dent was neither the most recent subject nor the most recent noun phrase matching the anaphora in gender and number . 
Example : Identify the drawer by the lit paper port LED and add paper to itj . 
The aggregate score for `` the drawer '' is 7 ( definiteness 1 + givenness 0 + term preference 1 + indicating verbs I + lexical reiteration 0 + section heading 0 + collocation 0 + referential distance 2 + non-prepositional noun phrase 0 + immediate referÂ­ enc 2 = 7 ) , whereas aggregate score for the most recent matching noun phrase ( `` the lit paper port LED '' ) is 4 ( definiteness 1 + givenness 0 + term preference I + indicating verbs 0 + lexical reiteraÂ­ son 0 + section heading 0 + collocation 0 + referenÂ­ ital distance 2 + non-prepositional noun phrase 0 + immediate reference 0 = 4 ) . 
From this example we can also see that our knowledge-poor approach successfully tackles cases in which the anaphora and theÂ· antecedent have not only different syntactic functions but also different semantic roles . 
Usually knowledge-based apÂ­ roaches have difficulties in such a situation because they use preferences such as `` syntactic parallelism '' or `` semantic parallelism '' . 
Our robust approach does not use these because it has no information about the syntactic structure of the sentence or about the synÂ­ tactic functionalism role of each individual word . 
As far as the typical failure cases are concerned , we anticipate the knowledge-poor approach to have difficulties with sentences which have a more comÂ­ lex syntactic structure . 
This should not be surprising , given that the approach does not rely on any syntactic knowledge and in particular , it does not produce any parse tree . 
Indeed , the approach fails on the sentence : The paper through key can be used to feed [ a blank sheet of paper ] j through the copier out into the copy tray without making a copy on itj . 
where `` blank sheet of paper '' scores only 2 as opÂ­ posed to the `` the paper through key '' which scores 6 . 
3.2 Evaluation B . We carried out a second evaluation of the approach on a different set of sample texts from the genre of technical manuals ( 47-page Portable Style-Writer User 's Guide ( Stylewriter 1994 ) . 
Out of 223 proÂ­ nouns in the text , 167 were non-anaphoric ( deictic and non-anaphoric `` it '' ) . 
The evaluation carried out was manual to ensure that no added error was genÂ­ rated e.g . due to possible wrong sentence detection or POS tagging ) . 
Another reason for doing it by hand is to ensure a fair comparison with Breck Baldwin 's method , which not being available to us , had to be hand-simulated ( see 3.3 ) . 
The evaluation indicated 83.6 % success rate . 
The `` Baseline subject '' model tested on the same data scored 33.9 % recall and 67.9 % precision , whereas `` Baseline most recent '' scored 66.7 % . 
Note that `` Baseline subject '' can be assessed both in terms of recall and precision because this `` version '' is not robust : in the event of no subject being available , it is not able to propose an antecedent ( the manual guide used as evaluation text contained many imÂ­ imperative sentences ) . 
In the second experiment we evaluated the apÂ­ roach from the point of view also of its `` critical success rate '' . 