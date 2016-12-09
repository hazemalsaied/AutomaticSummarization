The words between the two mentions are classified into three bins : the first word in between , the last word in between and other words in between . 
Similar to word features , three categories of phrase heads are considered : 1 ) the phrase heads in between are also classified into three bins : the first phrase head in between , the last phrase head in between and other phrase heads in between ; 2 ) the phrase heads before M1 are classified into two bins : the first phrase head before and the second phrase head before ; 3 ) the phrase heads after M2 are classified into two bins : the first phrase head after and the second phrase head after . 
It consists of 97 documents ( ~50k words ) and 1386 instances of relations . 
The final decision of an instance in the multiple binary classification is determined by the class which has the maximal SVM output . 
This paper uses the ACE corpus provided by LDC to train and evaluate our feature-based relation extraction system . 
Support Vector Machines ( SVMs ) are a supervised machine learning technique motivated by the statistical learning theory ( Vapnik 1998 ) . 
It also shows that our system outperforms tree kernel-based systems ( Culotta et al 2004 ) by over 20 F-measure on extracting 5 ACE relation types . 
4 5 