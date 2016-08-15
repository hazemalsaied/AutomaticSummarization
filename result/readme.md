#The result files guide
In the files titled result + Number we have multiple versions of results.

the result file contains the console output of our code when exeuted.
These files are divided into three sections.

##The first section :

in this section we have the significant words according to the contrast measure.

##The second section :

in this section we have the significant words according to the F-measure.

##The third section :

The summary of the document without using the citance.
It contains the 5 percesnt sentences of each section.

The sentences are selected using their weights on the long enough sentences, i.e the sentences which contain more than
informative words.

##The fourth section :

This section contains an analysis of matching process between the reference document and the citing ones.

for every annotation, we mention the citing sentence, the reference sentences associated to this sentence acoording
to the corpus annotation, and the same result but using our code.

Before every sentence in this section you have the **distance** of this sentence of the citing sentence using our
technique of matching.

please notice that we are talking about the dostance, not the **similarity**.

#Index of results according to numbers:

- **OCR correction**: this file contains a corrected copy of the article after applying multiple technique for enhancing the quality of the file.
the bold word is corrected word, beside it, between () you can see the original one.
This file is the corrected version of C90-2039_TRAIN

- **Elegant Report Of Citation**: This file contains a list of citing sentences and their contexts with the suitable reference ones according to the corpus annotation


- **Result**: this file is the first version of our code result.

- **Result1**: We change the threeshold of the contrast to 1.2 instead of 1, i.e reducing the number of significant words.

    - **the number of the words has been reduced is moving from 237 to 170.**

- **Result2**: We Add the enhanced list of stop words.

    - **the number of the words has been reduced is moving from 237 to 198, for words extracted using contrast, and from 163 to 140.**

- **Result3**: After adding the corretion, the xml is in higher quality and the candidate features are in bold and features in italic bold.

- **Result4**: the result after using more accurate calculation of feature maximisation, no matrices anymore.

- **MatchingResults** this file contains a first progress report of the new approche used for finding the span text of a citation inside the reference paper.
    for each annotation, we list inside those brackets {} the indices of corpus result. then we list on each line a term or a word of the citing sentence who could be part of the principal query and the first ten sentences who contain it. these sentences are sorted according to their feature maximization weight. 