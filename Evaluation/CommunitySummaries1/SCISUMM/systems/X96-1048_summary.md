The introduction of two new tasks into the MUC evaluations and the restructuring of information extraction into two separate tasks have infused new life into the evaluations . 
The other two tasks , Template Element and Scenario Template , were information extraction tasks that followed on from the MUC evaluations conducted in previous years . 
Many of the sites have emphasized their pattern-matching techniques in discussing the strengths of their MUC6 systems . 
NAMED ENTITY The Named Entity ( NE ) task requires insertion of SGML tags into the text stream . 
Identification of certain common types of names , which constitutes a large portion of the Named Entity task and a critical portion of the Template Element task , has proven to be largely a solved problem . 
The system-generated outputs are from three different systems , since no one system did better than all other systems on all three events . 
OVERVIEW OF RESULTS OF THE MUC-6 EVALUATION
The evolution and design of the MUC6 evaluation are discussed in the paper by Grishman and Sundheim in this volume . 
The amount of agreement between the two annotators was found to be 80 % recall and 82 % precision . 
An algorithm developed by the MITRE Corporation for MUC6 was implemented by SAIC and used for scoring the task . 
For MUC6 , text filtering scores were as high as 98 % recall ( with precision in the 80th percentile ) or 96 % precision ( with recall in the 80th percentile ) . 
The identification of a name as that of an organization ( hence , instantiation of an ORGANIZATION object ) or as a person ( PERSON object ) is a named entity identification task . 
 Scenario Template ( ST ) -- Drawing evidence from anywhere in the text , extract respecified event information , and relate the event information to the particular organization and person entities involved in the event . 
Human performance was measured in terms of annotator variability on only 30 texts in the test set and showed agreement to be approximately 83 % , when one annotator 's templates were treated as the `` key '' and the other annotator 's templates were treated as the `` response '' . 
Systems are measured for their performance on distinguishing relevant from relevant texts via the text filtering metric , which uses the classic information retrieval definitions of recall and precision . 
CORPUS Testing was conducted using Wall Street Journal texts provided by the Linguistic Data Consortium . 
The two SGML-based tasks required innovations to tie system-internal data structures to the original text so that the annotations could be inserted by the system without altering the original text in any other way . 
It was also unexpected that one of the systems would match human performance on the task . 
Common organization names , first names of people , and location names can be handled by recourse to list lookup , although there are drawbacks : some names may be on more than one list , the lists will not be complete and may not match the name as it is realized in the text ( e.g. , may not cover the needed abbreviated form of an organization name , may not cover the complete person name ) , etc.. 
The latest in a series of natural language processing system EVALUATION was concluded in October 1995 and was the topic of the Sixth Message Understanding Conference ( MUC6 ) in November . 