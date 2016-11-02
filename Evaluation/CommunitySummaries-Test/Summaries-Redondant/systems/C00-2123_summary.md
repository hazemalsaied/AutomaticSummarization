Word Re-ordering and DP-based Search in Statistical Machine Translation
Word Re-ordering and DP-based Search in Statistical Machine Translation
Word Re-ordering and DP-based Search in Statistical Machine Translation
We are given a source string fJ 1 = f1 : : : fj : : : fJ of length J , which is to be translated into a target string eI 1 = e1 : : : ei : : : eI of length I . Among all possible target strings , we will choose the string with the highest probability : ^eI 1 = arg max eI 1 fPr ( eI 1jfJ 1 ) g = arg max eI 1 fPr ( eI 1 ) Pr ( fJ 1 jeI 1 ) g : ( 1 ) The argyle operation denotes the search problem , i.e . the generation of the output sentence in the target language . 
The goal of machine translation is the translation of a text given in some source language into a target language . 
On average , 6 reference translations per automatic translation are available . 
The Levenshtein distance between the automatic translation and each of the reference translations is computed , and the minimum Levenshtein distance is taken . 
The computing time is given in terms of CPU time per sentence ( on a 450MHz PentiumIIIPC ) . 
The German finite verbs bin ( second example ) and Frontenac ( third example ) are too far away from the personal pronouns rich and 'Sie ' ( 6 respectively 5 source sentence positions ) . 
For each source word f , the list of its possible translations e is sorted according to p ( fje ) pun e ) , where pun e ) is the trigram probability of the English word e. It is suÃcient to consider only the best 50 words . 
The sentence length probability p ( JjI ) is omitted without any loss in performance . 
The sentence length probability p ( JjI ) is omitted without any loss in performance . 
On average , 6 reference translations per automatic translation are available . 
We show translation results for three approaches : the monotone search ( MonS ) , where no word reordering is allowed ( Tillmann , 1997 ) , the monotone search ( QmS ) as presented in this paper and the IBM style ( IbmS ) search as described in Section 3.2 . 
We show translation results for three approaches : the monotone search ( MonS ) , where no word reordering is allowed ( Tillmann , 1997 ) , the monotone search ( QmS ) as presented in this paper and the IBM style ( IbmS ) search as described in Section 3.2 . 
input : source string f1 : : : fj : : : fJ initialization for each cardinality c = 1 ; 2 ; ; J do for each pair ( C ; j ) , where j 2 C and jCj = c do for each target word e 2 E Qe0 ( e ; C ; j ) = p ( fj je ) max Ã ; e00 j02Cnfjg fp ( jjj 0 J ) p ( Ã ) pÃ ( eje 0 e00 ) Qe00 ( e0 ; C n fjg ; j0 ) g words fj in the input string of length J . For the final translation each source position is considered exactly once . 
Word Re-ordering and DP-based Search in Statistical Machine Translation
The word joining is done on the basis of a likelihood criterion . 
A procedural definition to restrict1In the approach described in ( Berger et al. , 1996 ) , a mor pathological analysis is carried out and word morphemes rather than full-form words are used during the search . 
Additionally , for a given coverage set , at most 250 different hypotheses are kept during the search process , and the number of different words to be hypothesized by a source word is limited . 
For a trigram language model , the partial hypotheses are of the form ( e0 ; e ; C ; j ) . 
We show translation results for three approaches : the monotone search ( MonS ) , where no word reordering is allowed ( Tillmann , 1997 ) , the monotone search ( QmS ) as presented in this paper and the IBM style ( IbmS ) search as described in Section 3.2 . 
An extended lexicon model is defined , and its likelihood is compared to a baseline lexicon model , which takes only single-word dependencies into account . 
Word Re-ordering and DP-based Search in Statistical Machine Translation
An extended lexicon model is defined , and its likelihood is compared to a baseline lexicon model , which takes only single-word dependencies into account . 
For each source word f , the list of its possible translations e is sorted according to p ( fje ) pun e ) , where pun e ) is the trigram probability of the English word e. It is suÃcient to consider only the best 50 words . 
The complexity of the monotone search is O ( E3 J ( R2+LR ) ) . 
We show translation results for three approaches : the monotone search ( MonS ) , where no word reordering is allowed ( Tillmann , 1997 ) , the monotone search ( QmS ) as presented in this paper and the IBM style ( IbmS ) search as described in Section 3.2 . 
We show Translation results for three approaches : the monotone Search ( MonS ) , where no Word reordering is allowed ( Tillmann , 1997 ) , the monotone Search ( QmS ) as presented in this paper and the IBM Style ( IbmS ) Search as described in Section 3.2 . 