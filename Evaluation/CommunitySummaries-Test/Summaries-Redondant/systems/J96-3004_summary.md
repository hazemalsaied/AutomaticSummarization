The Chinese person-name model is a modified version of that described in Sproat et al . 
A Brief Introduction to the Chinese Writing System Most readers will undoubtedly be at least somewhat familiar with the nature of the Chinese writing system , but there are enough common misunderstandings that it is as well to spend a few paragraphs on properties of the Chinese script that will be relevant to topics discussed in this paper . 
Following Sproat and Shih ( 1990 ) , performance for Chinese segmentation systems is generally reported in terms of the dual measures of precision and recalP It is fairly standard to report precision and recall scores in the mid to high 90 % range . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
A Brief Introduction to the Chinese Writing System Most readers will undoubtedly be at least somewhat familiar with the nature of the Chinese writing system , but there are enough common misunderstandings that it is as well to spend a few paragraphs on properties of the Chinese script that will be relevant to topics discussed in this paper . 
Following Sproat and Shih ( 1990 ) , performance for Chinese segmentation systems is generally reported in terms of the dual measures of precision and recalP It is fairly standard to report precision and recall scores in the mid to high 90 % range . 
Lexical-knowledge-based approaches that include statistical information generally presume that one starts with all possible segmentations of a sentence , and picks the best segmentation from the set of possible segmentations using a probabilistic or costÂ­ based scoring mechanism . 
The points enumerated above are particularly related to ITS , but analogous arguments can easily be given for other applications ; see for example Wu and Tseng 's ( 1993 ) discussion of the role of segmentation in information retrieval . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
A Brief Introduction to the Chinese Writing System Most readers will undoubtedly be at least somewhat familiar with the nature of the Chinese writing system , but there are enough common misunderstandings that it is as well to spend a few paragraphs on properties of the Chinese script that will be relevant to topics discussed in this paper . 
Indeed , as we shall show in Section 5 , even human judges differ when presented with the task of segmenting a text into words , so a definition of the criteria used to determine that a given segmentation is correct is crucial before one can interpret such measures . 
Others depend upon various lexical heurisÂ­ tics : for example Chen and Liu ( 1992 ) attempt to balance the length of words in a three-word window , favoring segmentations that give approximately equal length for each word . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
A Stochastic Finite-State Word-Segmentation Algorithm for Chinese
Any NLP application that presumes as input unrestricted text requires an initial phase of text analysis ; such applications involve problems as diverse as machine translation , information retrieval , and text-to-speech synthesis ( TIS ) . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
A Brief Introduction to the Chinese Writing System Most readers will undoubtedly be at least somewhat familiar with the nature of the Chinese writing system , but there are enough common misunderstandings that it is as well to spend a few paragraphs on properties of the Chinese script that will be relevant to topics discussed in this paper . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
Furthermore , even the size of the dictionary per se is less important than the appropriateness of the lexicon to a particular test corpus : as Fung and Wu ( 1994 ) have shown , one can obtain substantially better segmentation by tailoring the lexicon to the corpus to be segmented . 
It has been shown for English ( Wang and Hirschberg 1992 ; Hirschberg 1993 ; Sproat 1994 , inter aria that grammatical part of speech provides useful information for these tasks . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
There are thus some very good reasons why segmentation into words is an important task . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
There are thus some very good reasons why segmentation into words is an important task . 
We will evaluate various specific aspects of the segmentation , as well as the overall segmentation perÂ­ performance . 
Particular relations are also consistent with particular hypotheses about the segmentation of a given sentence , and the scores for particular relations can be incremented or decremented depending upon whether the segmentations with which they are consistent are `` popular '' or not . 
A Stochastic Finite-State Word-Segmentation Algorithm for Chinese
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
Lexical-knowledge-based approaches that include statistical information generally presume that one starts with all possible segmentations of a sentence , and picks the best segmentation from the set of possible segmentations using a probabilistic or costÂ­ based scoring mechanism . 
Methods that allow multiple segmentations must provide criteria for choosing the best segmentation . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
For eight judges , ranging k between 1 and 8 corresponded to a precision score range of 90 % to 30 % , meaning that there were relatively few words ( 30 % of those found by the automatic segmented on which all judges agreed , whereas most of the words found by the segmented such that one human judge agreed . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
In this paper we present a stochastic finite-state model wherein the basic workhorse is the weighted finite-state transducer . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
The average agreement among the human judges is .76 , and the average agreement between ST and the humans is .75 , or about 99 % of the inter human One can better visualize the precision-recall similarity matrix by producing from that matrix a distance matrix , computing a classical metric multidimensional scaling ( Torgerson 1958 ; Becker , Chambers , Wilks 1988 ) on that disÂ­ stance matrix , and plotting the first two most significant dimensions . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
The average agreement among the human judges is .76 , and the average agreement between ST and the humans is .75 , or about 99 % of the inter human One can better visualize the precision-recall similarity matrix by producing from that matrix a distance matrix , computing a classical metric multidimensional scaling ( Torgerson 1958 ; Becker , Chambers , Wilks 1988 ) on that disÂ­ stance matrix , and plotting the first two most significant dimensions . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
The simplest approach involves scoring the various analyses by costs based on word frequency , and picking the lowest cost path ; variants of this approach have been described in Chang , Chen , and Chen ( 1991 ) and Chang and Chen ( 1993 ) . 
In Chinese text , individual characters of the script , to which we shall refer by their traditional name of Hanni Z are written one after another with no intervening spaces ; a Chinese sentence is shown in Figure 1.3 Partly as a result of this , the notion `` word '' has never played a role in Chinese philological tradition , and the idea that Chinese lacks anyÂ­ thing analogous to words in European languages has been prevalent among Western monologists see DeFrancis ( 1984 ) . 
Thus in an English sentence such as I 'm going to show up at the ACL one would reasonably conjecture that there are eight words separated by seven spaces . 
The three solemnization definitions in this section are essentially descriptive restatements of the corresponding constructive solemnization procedures , which in turn are realizaÃÂ­ sons of the widely followed principle of maximum tokenization ( e.g. , Liu 1986 ; Liang 1986a , 1986b ; Wang 1989 ; Jie 1989 ; Wang , Su , and Mo 1990 ; Jie , Liu , and Liang 1991a , b ; Yeh and Lee 1991 ; Webster and Kit 1992 ; Chen and Liu 1992 ; Guo 1993 ; Wu and Su 1993 ; Nie , Jin , and Hannan 1994 ; Sproat et al . 1996 ; 
The weighted finite-state transducer model developed by Sproat et al . 
The weighted finite-state transducer model developed by Sproat et al . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
The weighted finite-state transducer model developed by Sproat et al . 
Purely statistical approaches have not been very popular , and so far as we are aware earlier work by Sproat and Shih ( 1990 ) is the only published instance of such an approach . 
Purely statistical approaches have not been very popular , and so far as we are aware earlier work by Sproat and Shih ( 1990 ) is the only published instance of such an approach . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
4.4 Chinese Personal Names . 
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
4.4 Chinese Personal Names . 
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
The family name set is restricted : there are a few hundred single-hanzi family names , and about ten double-hanzi ones . 
It is formally straightforward to extend the grammar to include these names , though it does increase the likelihood of over generation and we are unaware of any working systems that incorporate this type of name . 
This is in general very difficult , given the extremely free manner in which Chinese given names are formed , and given that in these cases we lack even a family name to give the model confidence that it is identifying a name . 
The major problem for all segmentation systems remains the coverage afforded by the dictionary and the lexical rules used to augment the dictionary to deal with unseen words . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
In Section 6 we disÂ­ cuss other issues relating to how higher-order language models could be incorporated into the model . 
We will evaluate various specific aspects of the segmentation , as well as the overall segmentation perÂ­ performance . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
A Stochastic Finite-State Word-Segmentation Algorithm for Chinese
The Chinese person-name model is a modified version of that described in Sproat et al . 
The weighted finite-state transducer model developed by Sproat et al . 
In this paper we present a stochastic finite-state model wherein the basic workhorse is the weighted finite-state transducer . 
The weighted finite-state transducer model developed by Sproat et al . 
In this paper we present a stochastic finite-state model wherein the basic workhorse is the weighted finite-state transducer . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
TIS systems in general need to do more than simply compute the . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
The method just described segments dictionary words , but as noted in Section 1 , there are several classes of words that should be handled that are not found in a standard dictionary . 
Note that Hanni that are not grouped into dictionary words ( and are not identified as singleÂ­ Hanni words ) , or into one of the other categories of words discussed in this paper , are left unattached and tagged as unknown words . 
This larger corpus was kindly provided to us by United Informatics Inc. , R.O.C . a set of initial estimates of the word frequencies. 9 In this re-estimation procedure only the entries in the base dictionary were used : in other words , derived words not in the base dictionary and personal and foreign names were not used . 
This is in general very difficult , given the extremely free manner in which Chinese given names are formed , and given that in these cases we lack even a family name to give the model confidence that it is identifying a name . 
For example , it is well-known that one can build a finite-state digram word ) model by simply assigning a state Si to each word Wi in the vocabulary , and having ( word ) arcs leaving that state weighted such that for each Wj and corresponding arc aj leaving Si , the cost on aj is the digram of WiWj- ( Costs for unseen bi grams in such a scheme would typically be modeled with a special back off state . ) 
On a set of 11 sentence fragments-the A set-where they reported 100 % recall and precision for name identification , we had 73 % recall and 80 % precision . 
We will evaluate various specific aspects of the segmentation , as well as the overall segmentation perÂ­ performance . 
Indeed , as we shall show in Section 5 , even human judges differ when presented with the task of segmenting a text into words , so a definition of the criteria used to determine that a given segmentation is correct is crucial before one can interpret such measures . 
Methods that allow multiple segmentations must provide criteria for choosing the best segmentation . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
For a given `` word '' in the automatic segmentation , if at least k of the huÂ­ man judges agree that this is a word , then that word is considered to be correct . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
For a given `` word '' in the automatic segmentation , if at least k of the huÂ­ man judges agree that this is a word , then that word is considered to be correct . 
While the semantic aspect of radicals is by no means completely predictive , the semantic homogeneity of many classes is quite striking : for example 254 out of the 263 examples ( 97 % ) of the INSECT class listed by Wieger ( 1965 , 77376 ) denote crawling or invertebrate animals ; similarly 21 out of the 22 examples ( 95 % ) of the GHOST class ( page 808 ) denote ghosts or spirits . 
19 We note that it is not always clear in Wang , Li , and Chang 's examples which segmented words . 
Purely statistical approaches have not been very popular , and so far as we are aware earlier work by Sproat and Shih ( 1990 ) is the only published instance of such an approach . 
The simplest approach involves scoring the various analyses by costs based on word frequency , and picking the lowest cost path ; variants of this approach have been described in Chang , Chen , and Chen ( 1991 ) and Chang and Chen ( 1993 ) . 
Some approaches depend upon some form of conÂ­ strain satisfaction based on syntactic or semantic features ( e.g. , Yeh and Lee [ 1991 ] , which uses a unification-based approach ) . 
Roughly speaking , previous work can be divided into three categories , namely purely statistical approaches , purely lexiÂ­ cal rule-based approaches , and approaches that combine lexical information with staÂ­ statistical information . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
A Stochastic Finite-State Word-Segmentation Algorithm for Chinese
Any NLP application that presumes as input unrestricted text requires an initial phase of text analysis ; such applications involve problems as diverse as machine translation , information retrieval , and text-to-speech synthesis ( TIS ) . 
An initial step of any textÂ­ analysis task is the solemnization of the input into words . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
each word in the lexicon whether or not each string is actually an instance of the word in question . 
Each word is terminated by an arc that represents the transduction between f and the part of speech of that word , weighted with an estimated cost for that word . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
Purely statistical approaches have not been very popular , and so far as we are aware earlier work by Sproat and Shih ( 1990 ) is the only published instance of such an approach . 
16 As one reviewer points out , one problem with the epigram model chosen here is that there is still a. tendency to pick a segmentation containing fewer words . 
As we shall argue , the semantic class affiliation of a Hanni constitutes useful information in predicting its properties . 
A related point is that mutual information is helpful in augmenting existing electronic dictionaries , ( cf . 
Church and Hanks [ 1989 ] ) , and we have used lists of character pairs ranked by mutual information to expand our own dictionary . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
In this way , the method reported on here will necessarily be similar to a greedy method , though of course not identical . 
Papers that use this method or minor variants thereof include Liang ( 1986 ) , Li et al . 
In this way , the method reported on here will necessarily be similar to a greedy method , though of course not identical . 
Papers that use this method or minor variants thereof include Liang ( 1986 ) , Li et al . 
In this way , the method reported on here will necessarily be similar to a greedy method , though of course not identical . 
A Stochastic Finite-State Word-Segmentation Algorithm for Chinese
Let us notate the set of previously unseen , or novel , members of a category X as unseen ( X ) ; thus , novel members of the set of words derived in f , menO will be deÂ­ noted unseen ( f , ) . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
constitute names , since we have only their segmentation , not the actual classification of the segmented words . 
The Chinese person-name model is a modified version of that described in Sproat et al . 
While it may not be totally impossible to fully incorporate such knowledge and heuristics into the general framework of path evaluation and searching , they are apÃÂ­ apparently employed neither in Sproat et al . 
This larger corpus was kindly provided to us by United Informatics Inc. , R.O.C . a set of initial estimates of the word frequencies. 9 In this re-estimation procedure only the entries in the base dictionary were used : in other words , derived words not in the base dictionary and personal and foreign names were not used . 
Raphael A ren 2 ' is a fairly uncontroversial case of a monograph word , and replica ( middle country ) 'China ' a fairly uncontroversial case of a diÂ­ grapheme word . 
In this paper we present a stochastic finite-state model for segmenting Chinese text into words , both words found in a ( static ) lexicon as well as words derived via the above-mentioned productive processes . 
There is a sizable literature on Chinese word segmentation : recent reviews include Wang , Su , and Mo ( 1990 ) and Wu and Tseng ( 1993 ) . 
On a set of 11 sentence fragments-the A set-where they reported 100 % recall and precision for name identification , we had 73 % recall and 80 % precision . 
On the first of these-the B set-our system had 64 % recall and 86 % precision ; on the second-the C set-it had 33 % recall and 19 % precision . 
The last affix in the list is the nominal plural f , men0.20 In the table are the ( typical ) classes of words to which the affix attaches , the number found in the test corpus by the method , the number correct ( with a precision measure ) , and the number missed ( with a recall measure ) . 
orthographic words are thus only a starting point for further analysis and can only be regarded as a useful hint at the desired division of the sentence into words . 
orthographic words are thus only a starting point for further analysis and can only be regarded as a useful hint at the desired division of the sentence into words . 