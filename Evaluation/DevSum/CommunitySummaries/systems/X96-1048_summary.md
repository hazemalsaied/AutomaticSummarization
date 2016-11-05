The introduction of two new tasks into the MUC evaluations and the restructuring of information extraction into two separate tasks have infused new life into the evaluations . 
The other two tasks , Template Element and Scenario Template , were information extraction tasks that followed on from the MUC evaluations conducted in previous years . 
Many of the sites have emphasized their pattern-matching techniques in discussing the strengths of their MUC6 systems . 
NAMED ENTITY The Named Entity ( NE ) task requires insertion of SGML tags into the text stream . 
Even the simplest of the tasks , Named Entity , occasionally requires in-depth processing , e.g. , to determine whether `` 60 pounds '' is an expression of weight or of monetary value . 
About half the systems focused only on individual co reference which has direct relevance to the other MUC6 evaluation tasks . 
Documentation of each of the tasks and summary scores for all systems evaluated can be found in the MUC6 proceedings [ 1 ] . 
The latest in a series of natural language processing system evaluations was concluded in October 1995 and was the topic of the Sixth Message Understanding Conference ( MUC6 ) in November . 
Commercial systems are available already that include identification of those defined for this MUC6 task , and since a number of systems performed very well for MUC6 , it is evident that high performance is probably within reach of any development site that devotes enough effort to the task . 
No analysis has been done of the relative difficulty of the MUC6 ST task compared to previous extraction evaluation tasks . 
One of the innovations of MUC6 was to formalize the general structure of event templates , and all three scenarios defined in the course of MUC6 conformed to that general structure . 
CO Results on Some Aspects of Task and on `` Walkthrough Article '' To keep the annotation of the evaluation data fairly simple , the MUC6 planning committee decided not to design the notation to subcategory linkages and markable in any way . 
The amount of agreement between the two annotators was found to be 80 % recall and 82 % precision . 
The one-month limitation on development in preparation for MUC6 would be difficult to factor into the computation , and even without that additional factor , the problem of coming up with a reasonable , objective way of measuring relative task difficulty has not been adequately addressed . 
The evolution and design of the MUC6 evaluation are discussed in the paper by Grishman and Sundheim in this volume . 
The author is turning over government leadership of the MUC work to Elaine Marsh at the Naval Research Laboratory in Washington , D.C. Ms. Marsh has many years of experience in computational linguistics to offer , along with extensive familiarity with the MUC evaluations , and will undoubtedly lead the work exceptionally well . 
Overall recall and precision on the TE task 6 10090 80 ° `` 7 '' o qb l  70 60 50 40 30 20 10 0 0 10 20 30 40 50 60 70 80 90 100 Recall Figure 5 . 
The identification of a name as that of an organization ( hence , instantiation of an ORGANIZATION object ) or as a person ( PERSON object ) is a named entity identification task . 
 Scenario Template ( ST ) -- Drawing evidence from anywhere in the text , extract respecified event information , and relate the event information to the particular organization and person entities involved in the event . 
Note also that even the best system on the third event was unable to determine that the succession event was occurring at McCannEfickson ; in addition , it only partially captured the full title of the post . 
The SUCCESSION_EVENT object points down to the Ib~AND_OUT object , which in turn points down to PERSON Template Element objects that represent the persons involved in the succession event . 
The evaluation metrics used for NE are essentially the same as those used for the two template-filling tasks , Template Element and Scenario Template . 
Human performance was measured in terms of annotator variability on only 30 texts in the test set and showed agreement to be approximately 83 % , when one annotator 's templates were treated as the `` key '' and the other annotator 's templates were treated as the `` response '' . 
This capability has other useful applications as well , e.g. , it enables text highlighting in a browser . 
Inter annotator scoring showed that one annotator missed tagging one instance of `` Coke '' as an ( optional ) organization , and the other annotator missed one date expression ( `` September '' ) . 
Systems are measured for their performance on distinguishing relevant from relevant texts via the text filtering metric , which uses the classic information retrieval definitions of recall and precision . 
Human performance was measured by comparing the 30 draft answer keys produced by the annotator at NRaD with those produced by the annotator at SAIC . 
The two SGML-based tasks required innovations to tie system-internal data structures to the original text so that the annotations could be inserted by the system without altering the original text in any other way . 
Text strings that are to be annotated are termed markable . 
The variety of tasks designed for MUC6 reflects the interests of both participants and sponsors in assessing and furthering research that can satisfy some urgent text processing needs in the very near term and can lead to solutions to more challenging text understanding problems in the longer term . 
CORPUS Testing was conducted using Wall Street Journal texts provided by the Linguistic Data Consortium . 
Management Succession Template Structure intentional and is comparable to the richness of the MUC3 `` TST2 '' test set and the MUC4 `` TST4 '' test set . 
The system-generated outputs are from three different systems , since no one system did better than all other systems on all three events . 
( BBN system ) Table 5 . 
It was also unexpected that one of the systems would match human performance on the task . 
Top performance on PERSON objects came close to human performance , while performance on ORGANIZATION objects fell significantly short of human performance , with the caveat that human performance was measured on only a portion of the test set . 
Common organization names , first names of people , and location names can be handled by recourse to list lookup , although there are drawbacks : some names may be on more than one list , the lists will not be complete and may not match the name as it is realized in the text ( e.g. , may not cover the needed abbreviated form of an organization name , may not cover the complete person name ) , etc.. 
OVERVIEW OF RESULTS OF THE MUC-6 EVALUATION
Participants were invited to enter their systems in as many as four different task-oriented EVALUATION . 