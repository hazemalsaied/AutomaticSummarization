The latest in a series of natural language processing system evaluations was concluded in October 1995 and was the topic of the Sixth Message Understanding Conference ( MUC6 ) in November . 
It also facilitates information extraction , since some of the information in the extraction templates is in the form of literal text strings , which some systems have in the past had difficulty reproducing in their output . 
Many of the sites have emphasized their pattern-matching techniques in discussing the strengths of their MUC6 systems . 
Even the simplest of the tasks , Named Entity , occasionally requires in-depth processing , e.g. , to determine whether `` 60 pounds '' is an expression of weight or of monetary value . 
The Named Entity and Coreference tasks entailed Standard Generalized Markup Language ( SGML ) annotation of texts and were being conducted for the first time . 
Recognition of alternative ways of identifying an entity constitutes a large portion of the Coreference task and another critical portion of the Template Element task and has been shown to represent only a modest challenge when the referents are names or pronouns . 
From the 100 test articles , a subset of 30 articles ( some relevant to the Scenario Template task , others not ) was selected for use as the test set for the Named Entity and Coreference tasks . 
This period comprised the `` evaluation epoch . '' 
The precision figure is supported by evidence from the NE evaluation . 
For MUC6 , text filtering scores were as high as 98 % recall ( with precision in the 80th percentile ) or 96 % precision ( with recall in the 80th percentile ) . 
MUC6 56.40 MUC5 EJV 52.75 MUC5 JJV 60.07 MUC5 EME 49.18 MUC5 JME 56.31 Table 4 . 
One of the innovations of MUC6 was to formalize the general structure of event templates , and all three scenarios defined in the course of MUC6 conformed to that general structure . 
There is a task-neutral DATE slot that is defined as a template element ; it was used in the MUC6 dry run as part of the labor negotiation scenario , but as currently defined , it fails to capture meaningfully some of the recurring kinds of date information . 
Three scenarios were defined in the course of MUC6 : ( 1 ) a scenario concerning the event of organizations placing orders to buy aircraft with aircraft manufacturers ( the `` aircraft order '' scenario ) ; ( 2 ) a scenario concerning the event of contract negotiations between labor unions and companies ( the `` labor negotiations '' scenario ) ; ( 3 ) a scenario concerning changes in corporate managers occupying executive posts ( the `` management succession '' scenario ) . 
test set used for the MUC6 dry run , which was based on a scenario concerning labor union contract negotiations , there were only about half as many organizations and persons mentioned as there were in the test set used for the formal run . 
Finally , a change in administration of the MUC evaluations is occurring that will bring fresh ideas . 
COREFERENCE The task as defined for MUC6 was restricted to noun phrases ( NPs ) and was intended to be limited to phenomena that were relatively noncontroversial and easy to describe . 
Note that nearly 80 % of the tags were ENAMEX and that almost half of those were categorization as organization names . 
ST Results on Some Aspects of Task and on `` Walkthrough Article '' Three succession events are reported in the walk through article . 
Note also that even the best system on the third event was unable to determine that the succession event was occurring at McCannEfickson ; in addition , it only partially captured the full title of the post . 
The SUCCESSION_EVENT object points down to the Ib~AND_OUT object , which in turn points down to PERSON Template Element objects that represent the persons involved in the succession event . 
Human performance was measured in terms of annotator variability on only 30 texts in the test set and showed agreement to be approximately 83 % , when one annotator 's templates were treated as the `` key '' and the other annotator 's templates were treated as the `` response '' . 
This capability has other useful applications as well , e.g. , it enables text highlighting in a browser . 
CORPUS Testing was conducted using Wall Street Journal texts provided by the Linguistic Data Consortium . 
Text strings that are to be annotated are termed markable . 
( The test sets used for MUC5 had a much higher proportion of relevant texts . ) 
There was a large number of factors that contributed to the 20 % disagreement , including overlooking referential , using different interpretations of vague portions of the guidelines , and making different subjective decisions when the text of an article was ambiguous , sloppy , etc.. 
Of the 100 texts in the test set , 54 were relevant to the management succession scenario , including six that were only marginally relevant . 
The POST slot requires a text string as fill , and there is no finite list of possible fills for the slot . 
In this article , the management succession scenario will be used as the basis for discussion . 
The management succession template consists of four object types , which are linked together via one-way pointers to form a hierarchical structure . 
( BBN system ) Table 5 . 
Statistically , large differences of up to 15 points may not be reflected as a difference in the ranking of the systems . 
It was also unexpected that one of the systems would match human performance on the task . 
It should be noted that human performance on this task was also relatively low , but it is unclear whether the degree of disagreement can be accounted for primarily by the reasons given above or whether the disagreement is attributable to the fact that the guidelines for that slot had not been finalized at the time when the annotators created their version of the keys . 
As indicated in table 2 , all systems performed better on identifying person names than on identifying organization or location names , and all but a few systems performed better on location names than on organization names . 