The latest in a series of natural language processing system evaluations was concluded in October 1995 and was the topic of the Sixth Message Understanding Conference ( MUC6 ) in November . 
The measures used for information extraction include two overall ones , the F-measure and error per response fill , and several other , more diagnostic ones ( recall , precision , under generation over generation and substitution ) . 
OVERVIEW OF RESULTS OF THE MUC-6 EVALUATION
Even the simplest of the tasks , Named Entity , occasionally requires in-depth processing , e.g. , to determine whether `` 60 pounds '' is an expression of weight or of monetary value . 
The Named Entity and Coreference tasks entailed Standard Generalized Markup Language ( SGML ) annotation of texts and were being conducted for the first time . 
In the middle of the spectrum are definite descriptions and pronouns whose choice of referent is constrained by such factors as structural relations and discourse focus . 
Most human errors pertained to definite descriptions and bare nominals , not to names and pronouns . 
Participants were invited to enter their systems in as many as four different task-oriented evaluations . 
The other two tasks , Template Element and Scenario Template , were information extraction tasks that followed on from the MUC evaluations conducted in previous years . 
The evolution and design of the MUC6 evaluation are discussed in the paper by Grishman and Sundheim in this volume . 
COREFERENCE The task as defined for MUC6 was restricted to noun phrases ( NPs ) and was intended to be limited to phenomena that were relatively noncontroversial and easy to describe . 
Note that nearly 80 % of the tags were ENAMEX and that almost half of those were categorization as organization names . 
ST Results on Some Aspects of Task and on `` Walkthrough Article '' Three succession events are reported in the walk through article . 
Note also that even the best system on the third event was unable to determine that the succession event was occurring at McCannEfickson ; in addition , it only partially captured the full title of the post . 
The SUCCESSION_EVENT object points down to the Ib~AND_OUT object , which in turn points down to PERSON Template Element objects that represent the persons involved in the succession event . 
The management succession template consists of four object types , which are linked together via one-way pointers to form a hierarchical structure . 
All except the Scenario Template task are defined independently of any particular domain . 
It was also unexpected that one of the systems would match human performance on the task . 
Common organization names , first names of people , and location names can be handled by recourse to list lookup , although there are drawbacks : some names may be on more than one list , the lists will not be complete and may not match the name as it is realized in the text ( e.g. , may not cover the needed abbreviated form of an organization name , may not cover the complete person name ) , etc.. 
This paper surveys the results of the EVALUATION on each tasks and , to a more limited extent , across tasks . 