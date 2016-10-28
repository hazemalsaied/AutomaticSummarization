The Chinese person-name model is a modified version of that described in Sproat et al . 
A Brief Introduction to the Chinese Writing System Most readers will undoubtedly be at least somewhat familiar with the nature of the Chinese writing system , but there are enough common misunderstandings that it is as well to spend a few paragraphs on properties of the Chinese script that will be relevant to topics discussed in this paper . 
Following Sproat and Shih ( 1990 ) , performance for Chinese segmentation systems is generally reported in terms of the dual measures of precision and recalP It is fairly standard to report precision and recall scores in the mid to high 90 % range . 
A Stochastic Finite-State Word-Segmentation Algorithm for Chinese
Much confusion has been sown about Chinese writing by the use of the term ideograph , suggesting that Hanni somehow directly represent ideas . 
We will evaluate various specific aspects of the segmentation , as well as the overall segmentation perÂ­ performance . 
Lexical-knowledge-based approaches that include statistical information generally presume that one starts with all possible segmentations of a sentence , and picks the best segmentation from the set of possible segmentations using a probabilistic or costÂ­ based scoring mechanism . 
The points enumerated above are particularly related to ITS , but analogous arguments can easily be given for other applications ; see for example Wu and Tseng 's ( 1993 ) discussion of the role of segmentation in information retrieval . 
Thus , if one wants to segment words-for any purpose-from Chinese sentences , one faces a more difficult task than one does in English since one can not use spacing as a guide . 
In Chinese text , individual characters of the script , to which we shall refer by their traditional name of Hanni Z are written one after another with no intervening spaces ; a Chinese sentence is shown in Figure 1.3 Partly as a result of this , the notion `` word '' has never played a role in Chinese philological tradition , and the idea that Chinese lacks anyÂ­ thing analogous to words in European languages has been prevalent among Western monologists see DeFrancis ( 1984 ) . 
Indeed , as we shall show in Section 5 , even human judges differ when presented with the task of segmenting a text into words , so a definition of the criteria used to determine that a given segmentation is correct is crucial before one can interpret such measures . 
Others depend upon various lexical heurisÂ­ tics : for example Chen and Liu ( 1992 ) attempt to balance the length of words in a three-word window , favoring segmentations that give approximately equal length for each word . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
Any NLP application that presumes as input unrestricted text requires an initial phase of text analysis ; such applications involve problems as diverse as machine translation , information retrieval , and text-to-speech synthesis ( TIS ) . 
An initial step of any textÂ­ analysis task is the solemnization of the input into words . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
The three solemnization definitions in this section are essentially descriptive restatements of the corresponding constructive solemnization procedures , which in turn are realizaÃÂ­ sons of the widely followed principle of maximum tokenization ( e.g. , Liu 1986 ; Liang 1986a , 1986b ; Wang 1989 ; Jie 1989 ; Wang , Su , and Mo 1990 ; Jie , Liu , and Liang 1991a , b ; Yeh and Lee 1991 ; Webster and Kit 1992 ; Chen and Liu 1992 ; Guo 1993 ; Wu and Su 1993 ; Nie , Jin , and Hannan 1994 ; Sproat et al . 1996 ; 
For a language like English , this problem is generally regarded as trivial since words are delimited in English text by whitespace or marks of punctuation . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
Furthermore , even the size of the dictionary per se is less important than the appropriateness of the lexicon to a particular test corpus : as Fung and Wu ( 1994 ) have shown , one can obtain substantially better segmentation by tailoring the lexicon to the corpus to be segmented . 
It has been shown for English ( Wang and Hirschberg 1992 ; Hirschberg 1993 ; Sproat 1994 , inter aria that grammatical part of speech provides useful information for these tasks . 
There are thus some very good reasons why segmentation into words is an important task . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
For a given `` word '' in the automatic segmentation , if at least k of the huÂ­ man judges agree that this is a word , then that word is considered to be correct . 
All notions of word , with the exception of the orthographic word , are as relevant in Chinese as they are in English , and just as is the case in other languages , a word in Chinese may correspond to one or more symbols in the orthographic 1 For a related approach to the problem of word-segrnention in Japanese , see Nagata ( 1994 ) , inter aria 
Thus in an English sentence such as I 'm going to show up at the ACL one would reasonably conjecture that there are eight words separated by seven spaces . 
Particular relations are also consistent with particular hypotheses about the segmentation of a given sentence , and the scores for particular relations can be incremented or decremented depending upon whether the segmentations with which they are consistent are `` popular '' or not . 
then define the best segmentation to be the cheapest or best path in Id ( I ) o D* ( i.e. , Id ( I ) composed with the transitive closure of 0 ) .6 Consider the abstract example illustrated in Figure 2 . 
A moment 's reflection will reveal that things are not quite that simple . 
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
Purely statistical approaches have not been very popular , and so far as we are aware earlier work by Sproat and Shih ( 1990 ) is the only published instance of such an approach . 
Methods that allow multiple segmentations must provide criteria for choosing the best segmentation . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
For eight judges , ranging k between 1 and 8 corresponded to a precision score range of 90 % to 30 % , meaning that there were relatively few words ( 30 % of those found by the automatic segmented on which all judges agreed , whereas most of the words found by the segmented such that one human judge agreed . 
The weighted finite-state transducer model developed by Sproat et al . 
In this paper we present a stochastic finite-state model wherein the basic workhorse is the weighted finite-state transducer . 
Since the transducers are built from human-readable descriptions using a lexical toolkit ( Sproat 1995 ) , the system is easily maintained and extended . 
The average agreement among the human judges is .76 , and the average agreement between ST and the humans is .75 , or about 99 % of the inter human One can better visualize the precision-recall similarity matrix by producing from that matrix a distance matrix , computing a classical metric multidimensional scaling ( Torgerson 1958 ; Becker , Chambers , Wilks 1988 ) on that disÂ­ stance matrix , and plotting the first two most significant dimensions . 
As described in Sproat ( 1995 ) , the Chinese segmented presented here fits directly into the context of a broader finite-state model of text analysis for speech synthesis . 
The problem with these styles of evaluation is that , as we shall demonstrate , even human judges do not agree perfectly on how to segment a given text . 
In Section 6 we disÂ­ cuss other issues relating to how higher-order language models could be incorporated into the model . 
It is important to bear in mind , though , that this is not an inherent limitation of the model . 
Chinese word segmentation can be viewed as a stochastic transduction problem . 
If one is interested in translation , one would probably want to consider show up as a single dictionary word since its semantic interpretation is not trivially derivable from the meanings of show and up . 
And if one is interested in TIS , one would probably consider the single orthographic word ACL to consist of three phonological words-lei s'i d/-corresponding to the pronunciation of each of the letters in the acronym . 
The simplest approach involves scoring the various analyses by costs based on word frequency , and picking the lowest cost path ; variants of this approach have been described in Chang , Chen , and Chen ( 1991 ) and Chang and Chen ( 1993 ) . 
Each word is terminated by an arc that represents the transduction between f and the part of speech of that word , weighted with an estimated cost for that word . 
Note that Hanni that are not grouped into dictionary words ( and are not identified as singleÂ­ Hanni words ) , or into one of the other categories of words discussed in this paper , are left unattached and tagged as unknown words . 
Methods for expanding the dictionary include , of course , morphological rules , rules for segmenting personal names , as well as numeral sequences , expressions for dates , and so forth ( Chen and Liu 1992 ; Wang , Li , and Chang 1992 ; Chang and Chen 1993 ; Nie , Jin , and Hannan 1994 ) . 
Another question that remains unanswered is to what extent the linguistic information he considers can be handled-or at least approximated-by finite-state language models , and therefore could be directly interfaced with the segmentation model that we have presented in this paper . 
Note that the back off model assumes that there is a positive correlation between the frequency of a singular noun and its plural . 
The model we use provides a simple framework in which to incorporate a wide variety of lexical information in a uniform way . 
This flexibility , along with the simplicity of implementation and expansion , makes this framework an attractive base for continued research . 
The use of weighted transducers in particular has the attractive property that the model , as it stands , can be straightforwardly interfaced to other modules of a larger speech or natural language system : presumably one does not want to segment Chinese text for its own sake but instead with a larger purpose in mind . 
More complex approaches such as the relaxation technique have been applied to this problem Fan and Tsai ( 1988 } . 
Some approaches depend upon some form of conÂ­ strain satisfaction based on syntactic or semantic features ( e.g. , Yeh and Lee [ 1991 ] , which uses a unification-based approach ) . 
2 Chinese ? l* han 4zi 4 character ' ; this is the same word as Japanese Kania 
Furthermore , by inverting the transducer so that it maps from phonemic transcriptions to Hanni sequences , one can apply the segmented to other problems , such as speech recognition ( Pereira , Riley , and Sproat 1994 ) . 
It is formally straightforward to extend the grammar to include these names , though it does increase the likelihood of over generation and we are unaware of any working systems that incorporate this type of name . 
We of course also fail to identify , by the methods just described , given names used without their associated family name . 
4.4 Chinese Personal Names . 
Since foreign names can be of any length , and since their original pronunciation is effectively unlimited , the identiÂ­ fiction of such names is tricky . 
Obviously , the presence of a title after a potential name N increases the probability that N is in fact a name . 
Again , famous place names will most likely be found in the dictionary , but less well-known names , such as 1PMÂ± R ; bu4lang3-shi4wei2-ke4 'Brunswick ' ( as in the New Jersey town name 'New Brunswick ' ) will not generally be found . 
Whether a language even has orthographic words is largely dependent on the writing system used to represent the language ( rather than the language itself ) ; the notion `` orthographic word '' is not universal . 
where the husband 's family name is optionally pretended to the woman 's full name ; thus ; f : *lf # i xu3lin2-yan2hai3 would represent the name that Ms. Lin Yanhai would take if she married someone named Xu . 
This is in general very difficult , given the extremely free manner in which Chinese given names are formed , and given that in these cases we lack even a family name to give the model confidence that it is identifying a name . 
Our system fails in ( a ) because of $ shell a rare family name ; the system identifies it as a family name , whereas it should be analyzed as part of the given name . 
The major problem for all segmentation systems remains the coverage afforded by the dictionary and the lexical rules used to augment the dictionary to deal with unseen words . 
each word in the lexicon whether or not each string is actually an instance of the word in question . 
For example , it is well-known that one can build a finite-state digram word ) model by simply assigning a state Si to each word Wi in the vocabulary , and having ( word ) arcs leaving that state weighted such that for each Wj and corresponding arc aj leaving Si , the cost on aj is the digram of WiWj- ( Costs for unseen bi grams in such a scheme would typically be modeled with a special back off state . ) 
In this paper we have argued that Chinese word segmentation can be modeled efÂ­ effectively using weighted finite-state transducers . 
The first concerns how to deal with ambiguities in segmentation . 
There are clearly eight orthographic words in the example given , but if one were doing syntactic analysis one would probably want to consider I 'm to consist of two syntactic words , namely I and am . 
Space- or punctuation-delimited * 700 Mountain Avenue , 2d451 Murray Hill , NJ 07974 , USA . 
While size of the resulting transducers may seem daunting-the segmented described here , as it is used in the Bell Labs Mandarin TTS system has about 32,000 states and 209,000 arcs-recent work on minimization of weighted machines and transducers ( cf . 
Email : alls bell-labs . 
com t 700 Mountain Avenue , 2d451 Murray Hill , NJ 07974 , USA . 
Email : cls @ bell-labs . 
com t 600 Mountain Avenue , 2c278 Murray Hill , NJ 07974 , USA . 
TIS systems in general need to do more than simply compute the . 
The method reported in this paper makes use solely of epigram probabilities , and is therefore a zeroeth-order model : the cost of a particular segmentation is estimated as the sum of the costs of the individual words in the segmentation . 
In this way , the method reported on here will necessarily be similar to a greedy method , though of course not identical . 
The method just described segments dictionary words , but as noted in Section 1 , there are several classes of words that should be handled that are not found in a standard dictionary . 
This larger corpus was kindly provided to us by United Informatics Inc. , R.O.C . a set of initial estimates of the word frequencies. 9 In this re-estimation procedure only the entries in the base dictionary were used : in other words , derived words not in the base dictionary and personal and foreign names were not used . 
In this example there are four `` input characters , '' A , B , C and D , and these map respectively to four `` pronunciations '' a , b , c and d. Furthermore , there are four `` words '' represented in the dictionary . 
G1 and G2 are Hanni we can estimate the probability of the sequence being a name as the product of : â¢ the probability that a word chosen randomly from a text will be a name-p ( rule 1 ) , and â¢ the probability that the name is of the form 1hanzi-family 2hanzi-given-p ( rule 2 ) , and â¢ the probability that the family name is the particular Hanni ( rule 6 ) , and â¢ the probability that the given name consists of the particular Hanni and G2-p ( rule 9 ) This model is essentially the one proposed in Chang et al . 
Finally , we model the probability of a new transliterated name as the product of PTN and PTN ( Hanni ) for each Hanni in the putative name. 1 3 The foreign name model is implemented as an WFST , which is then summed with the WFST implementing the dictionary , morph 13 The current model is too simplistic in several respects . 
On a set of 11 sentence fragments-the A set-where they reported 100 % recall and precision for name identification , we had 73 % recall and 80 % precision . 
However , it is almost universally the case that no clear definition of what constitutes a `` correct '' segmentation is given , so these performance measures are hard to evaluate . 
However , some caveats are in order in comparing this method ( or any method ) with other approaches to segÂ­ segmentation reported in the literature . 
For novel texts , no lexicon that consists simply of a list of word entries will ever be entirely satisfactory , since the list will inevitably omit many constructions that should be considered words . 
This WFST represents the segmentation of the text into the words AB and CD , word boundaries being marked by arcs mapping between f and part-of-speech labels . 
Word frequencies are estimated by a re-estimation procedure that involves applyÂ­ ing the segmentation algorithm presented here to a corpus of 20 million words, 8 using 8 Our training corpus was drawn from a larger corpus of mixed-genre text consisting mostly of . 
constitute names , since we have only their segmentation , not the actual classification of the segmented words . 
pronunciation depends upon word affiliation : tfJ is pronounced deO when it is a pronominal modification marker , but di4 in the word Â§tfJ mu4di4 ' ; fl ; is normally gal , ' but qian 2 in a person 's given name . 
While the semantic aspect of radicals is by no means completely predictive , the semantic homogeneity of many classes is quite striking : for example 254 out of the 263 examples ( 97 % ) of the INSECT class listed by Wieger ( 1965 , 77376 ) denote crawling or invertebrate animals ; similarly 21 out of the 22 examples ( 95 % ) of the GHOST class ( page 808 ) denote ghosts or spirits . 
19 We note that it is not always clear in Wang , Li , and Chang 's examples which segmented words . 
Roughly speaking , previous work can be divided into three categories , namely purely statistical approaches , purely lexiÂ­ cal rule-based approaches , and approaches that combine lexical information with staÂ­ statistical information . 
In a more recent study than Chang et al. , Wang , Li , and Chang ( 1992 ) propose a surname-driven , non-stochastic , rule-based system for identifying personal names. 1 7 Wang , Li , and Chang also compare their performance with Chang et al . 's system . 
Note that Chang , Chen , and Chen ( 1991 ) , in addition to word-frequency information , include a constraint-satisfication model , so their method is really a hybrid approach . 
Fortunately , we were able to obtain a copy of the full set of sentences from Chang et al . on which Wang , Li , and Chang tested their system , along with the output of their system. 1 8 In what follows we will discuss all cases from this set where our performance on names differs from that of Wang , Li , and Chang . 
Email : gale @ research . 
Various segmentation approaches were then compared with human performance : 1 . 
Nonetheless , the results of the comparison with human judges demonstrates that there is mileage being gained by incorporating models of these types of words . 
att . 
com Â§Cambridge , UK Email : nc201 eng.cam.ac.uk 1996 Association for Computational Linguistics ( a ) B ) ( , : & ; ? ' H o w d o y o u s a y o c t o p u s i n J a p a n e s e ? ' ( b ) P l a u s i b l e S e g m e n t a t i o n I B X I I 1 : & I 0 0 r i 4 w e n 2 z h a n g l y u 2 z e n 3 m e 0 s h u o l ' J a p a n e s e ' ' o c t o p u s ' ' h o w ' ' s a y ' ( c ) Figure 1 I m p l a u s i b l e S e g m e n t a t i o n [ Â§ ] lxI 1 : & I ri4 wen 2 yu2zen3 shuttle ' essay fish how say A Chinese sentence in ( a ) illustrating the lack of word boundaries . 
In ( b ) is a plausible segmentation for this sentence ; in ( c ) is an implausible segmentation . 
For that application , at a minimum , one would want to know the phonological word boundaries . 
This is because our corpus is not annotated , and hence does not distinguish between the various words represented by homographs , such as , which could be adv 'be about to ' orInc jiang 4 ( military ) general'-as in 1j\xiao3jiang4 general . ' 
As noted , this sentence consists of four words , namely B X ri4wen2 , ' : Â¥ , zhanglyu 2 : & P : l zen 3me 0 , ' and IDt shuttle . ' 
Most languages that use Roman , Greek , Cyrillic , Armenian , or Semitic scripts , and many that use Indian-derived scripts , mark orthographic word boundaries ; however , languages written in a Chinese-derived writÂ­ ing system , including Chinese and Japanese , as well as Indian-derived writing systems of languages like Thai , do not delimit orthographic words. 1 Put another way , written Chinese simply lacks orthographic words . 
Making the reasonable assumption that similar information is relevant for solving these problems in Chinese , it follows that a prerequisite for intonation-boundary assignment and prominence assignment is word segmentation . 
The model segments Chinese text into dictionary entries and words derived by various productive lexical processes , and -- since the primary intended application of this model is to text-to-speech synthesis -- provides pronunciations for these words . 
Affix Pron Base category N found N missed ( recall ) N correct ( precision ) t , -,7 The second issue is that rare family names can be responsible for over generation especially if these names are otherwise common as single-hanzi words . 
Some of these approaches ( e.g. , Lin , Chiang , and Su [ 1993 ] ) attempt to identify unknown words , but do not acÂ­ tally tag the words as belonging to one or another class of expression . 
4.5 Transliterations of Foreign Words . 
As we shall argue , the semantic class affiliation of a Hanni constitutes useful information in predicting its properties . 
A related point is that mutual information is helpful in augmenting existing electronic dictionaries , ( cf . 
Church and Hanks [ 1989 ] ) , and we have used lists of character pairs ranked by mutual information to expand our own dictionary . 
The breakdown of the different types of words found by ST in the test corpus is given in Table 3 . 
4.2 A Sample Segmentation Using Only Dictionary Words Figure 4 shows two possible paths from the lattice of possible analyses of the input sentence B X : Â¥ . : .S : P : l 'How do you say octopus in Japanese ? ' previously shown in Figure 1 . 
Clearly the percentage of productively formed words is quite small ( for this particular corpus ) , meaning that dictionary entries are covering most of the 15 GR is .73 or 96 % .. 
Table 3 Classes of words found by ST for the test corpus . 
Papers that use this method or minor variants thereof include Liang ( 1986 ) , Li et al . 
This is to allow for fair comparison between the statistical method and GR , which is also purely dictionary-based . 
As can be seen , GR and this `` pared-down '' statistical method perform quite similarly , though the statistical method is still slightly better. 1 6 AG clearly performs much less like humans than these methods , whereas the full statistical algorithm , including morphological derivatives and names , performs most closely to humans among the automatic methods . 
We have argued that the proposed method performs well . 
Unfortunately , there is no standard corpus of Chinese texts , tagged with either single or multiple human judgments , with which one can compare performance of various methods . 
This implies , therefore , that a major factor in the performance of a Chinese segmented is the quality of the base dictionary , and this is probably a more important factor-from the point of view of performance alone-than the particular computational methods used . 
Let us notate the set of previously unseen , or novel , members of a category X as unseen ( X ) ; thus , novel members of the set of words derived in f , menO will be deÂ­ noted unseen ( f , ) . 
To evaluate proper-name identification , we randomly seÂ­ elected 186 sentences containing 12,000 Hanni from our test corpus and segmented the text automatically , tagging personal names ; note that for names , there is always a sinÂ­ gle unambiguous answer , unlike the more general question of which segmentation is correct . 
In Table 5 we present results from small test corÂ­ port for the productive affixes handled by the current version of the system ; as with names , the segmentation of morphologically derived words is generally either right or wrong . 
orthographic words are thus only a starting point for further analysis and can only be regarded as a useful hint at the desired division of the sentence into words . 
Twentieth-century linguistic work on Chinese ( Chao 1968 ; Li and Thompson 1981 ; Tang 1988,1989 , inter aria has revealed the incorrectness of this traditional view . 
Clearly this is not the only way to estimate word-frequencies , however , and one could consider applying other methods : in particÂ­ ulnar since the problem is similar to the problem of assigning part-of-speech tags to an untagged corpus given a lexicon and some initial estimate of the a priori probabilities for the tags , one might consider a more sophisticated approach such as that described in Kupiec ( 1992 ) ; one could also use methods that depend on a small hand-tagged seed corpus , as suggested by one reviewer . 
However , for our purposes it is not sufficient to repreÂ­ sent the morphological decomposition of , say , plural nouns : we also need an estimate of the cost of the resulting word . 
A minimal requirement for building a Chinese word segmented is obviously a dictionary ; furthermore , as has been argued persuasively by Fung and Wu ( 1994 ) , one will perform much better at segmenting text by using a dictionary constructed with text of the same genre as the text to be segmented . 
On the other hand , in a translation system one probably wants to treat this string as a single dictionary word since it has a conventional and somewhat unpredictable translation into English . 
On the first of these-the B set-our system had 64 % recall and 86 % precision ; on the second-the C set-it had 33 % recall and 19 % precision . 
The last affix in the list is the nominal plural f , men0.20 In the table are the ( typical ) classes of words to which the affix attaches , the number found in the test corpus by the method , the number correct ( with a precision measure ) , and the number missed ( with a recall measure ) . 
In many cases these failures in recall would be fixed by having better estimates of the actual probÂ­ abilities of single-hanzi words , since our estimates are often inflated . 
The simplest version of the maximum matching algorithm effectively deals with ambiguity by ignoring it , since the method is guaranteed to produce only one segmentation . 
In addition to the automatic methods , AG , GR , and ST , just discussed , we also added to the Plot the values for the current Algorithm using only dictionary entries ( i.e . , no productively derived words or names ) . 