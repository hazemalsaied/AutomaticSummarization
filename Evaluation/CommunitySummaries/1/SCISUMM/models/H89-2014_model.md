The model has the advantage that a pre-tagged training corpus is not required . 
The work described here also makes use of a hidden Markov model . 
In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
There it is assumed that the distribution of the use of a word depends on the set of categories it can assume , and words are partitioned accordingly . 
An alternative to uniformly increasing the order of the conditioning is to extend it selectively . 
Mixed higher- order context can be modeled by introducing explicit state sequences . 
In this regard , word equivalence classes were used ( Kupiec , 1989 ) . 
There it is assumed that the distribution of the use of a word depends on the set of categories it can assume , and words are partitioned accordingly . 
In a ranked list of words in the corpus the most frequent 100 words account for approximately 50 % of the total tokens in the corpus , and thus data is available to estimate them reliably . 
The most frequent 100 words of the corpus were assigned individually in the model , thereby enabling them to have different distributions over their categories . 
Mixed higher- order context can be modeled by introducing explicit state sequences . 
In the arrangement the basic first-order network remains , permitting all possible category sequences , and modeling first-order dependency . 
The basic network is then augmented with the extra state sequences which model certain category sequences in more detail . 
A model containing all of the refinements described , was tested using a magazine article containing 146 sentences ( 3,822 words ) . 
A 30,000 word dictionary was used , supplemented by inflectional analysis for words not found directly in the dictionary . 
A stochastic method for assigning part-of-speech categories to unrestricted English text has been described . 
