import math
import os, sys

from paper import Paper


class SciSummSigleDocSummarizer:
    @staticmethod
    def summarizeSciSumm(path, summPath):
        """
            This method generate all summary of Duc 2007 files and save them into the evaluation folder

            :return:
        """
        if not os.path.exists(summPath):
            os.makedirs(summPath)

        for subdir, dirs, files in os.walk(path):
            for directory in dirs:
                tempPath = os.path.join(path, directory)
                referenceXmlPath = os.path.join(tempPath, 'Reference_XML/' + directory + '-correction.xml')

                summary = SciSummSigleDocSummarizer.summarizeSD(referenceXmlPath)
                redSummary = SciSummSigleDocSummarizer.summarizeSD(referenceXmlPath, getRedondantSum=True)
                # Deleting empty lines for applying the convention of ROUGE 2.0
                SciSummSigleDocSummarizer.writeSummary(summary, directory)
                SciSummSigleDocSummarizer.writeSummary(redSummary, directory, isRed=True)

    @staticmethod
    def writeSummary(summary, directory,isRed=False):
        lines = summary.split('\n')
        newSummm = ''
        for line in lines:
            if line.rsplit():
                newSummm += line + '\n'
        newSummm = newSummm[:-1]
        # Writing the summary to the evaluation folder as a peer summary
        if not isRed:
            ff = open(os.path.join(summPath, directory + '_sum.md'), 'w+')
        else:
            ff = open(os.path.join(summPath, directory + '_redsum.md'), 'w+')
        ff.write(newSummm)
        ff.close()

    @staticmethod
    def summarizeSD(xmlFilePath,getRedondantSum=False):
        """
            Static method responsible of processing the paper from A to Z.
            it provoke all needed methods form summarizing the paper.

            :param xmlFilePath: the relative path of the xml representing the CL Paper we have to summarize
            :param isDucFile
        """
        paper = Paper(xmlFilePath)
        summarySents = SciSummSigleDocSummarizer.getSDSummary(paper,getRedondantSum)
        return SciSummSigleDocSummarizer.generateSummaryText(summarySents)

    @staticmethod
    def getSDSummary(paper, getRedondantSum=False):
        """
            this method is responsible of selecting the most important sentences of the article.
            the important sentence is the sentence whose weight is the bigger.

            :param paper:  the article after weighting words and sentences.
            :return: a list of selected @sentence objects.
        """
        summary = []
        orderedSents = SciSummSigleDocSummarizer.getSentencesWeights(paper)
        idx = 0
        firstSent = orderedSents[idx]
        while firstSent.getUsefulWordsNum() < 7:
            idx +=1
            firstSent = orderedSents[idx]
        summary.append(firstSent)
        summaryLength = firstSent.getWordsNum()
        while summaryLength < 250:
            if not getRedondantSum:
                SciSummSigleDocSummarizer.adjustWeights(summary[-1], paper)
                orderedSents = SciSummSigleDocSummarizer.getSentencesWeights(paper)

            # Adding non-repeated sentence
            for sent in orderedSents:
                if sent not in summary and sent.getUsefulWordsNum() > 7:
                    summary.append(sent)
                    summaryLength += sent.getWordsNum()
                    break
        return summary

    @staticmethod
    def generateSummaryText(summarySents):
        """
            Generate a 100 word summary given a list of sentence objects selected according to the summarization method

            :param summarySents: a list of sentence objects selected according to the summarization method
            :return: the summary as a block of text
        """
        summaryText = ''
        summaryLenght = 0
        for sent in summarySents[:-1]:
            if sent.getText().rstrip():
                summaryText += sent.getText() + '\n'
                summaryLenght += sent.getWordsNum()
        sent = summarySents[-1]
        # for controlling the size of the summary
        if summaryLenght + sent.getWordsNum() > 250:
            r = summaryLenght + sent.getWordsNum() - 250
            idx = 0
            for word in sent.getWords():
                if idx <= r:
                    summaryText += word.getText() + ' '
                    idx += 1
                else:
                    break

        return summaryText

    @staticmethod
    def getSentencesWeights(paper):
        """
            After assigning weights for all the words of the article, we assign weights for sentences in calculating the
            average of informative words for each sentence.

            :param paper:  the article after weighting words.
        """
        sents = []
        for section in paper.getSections():
            for sent in section.getSentences():
                sent.setWeight()
                sents.append(sent)
        if paper.getTitle() is not None:
            paper.getTitle().setWeight()
            sents.append(paper.getTitle())

        sents = sorted(sents, key=lambda Sentence: Sentence.getWeight(), reverse=True)
        return sents

    @staticmethod
    def adjustWeights(targetSentence, paper, WordsNumber=3):
        """
            This method reduce the weight of top-weighted words who taken place in the target sentence.
            It's a method used for reducing the redonduncy of the summary.

            :param targetSentence: the added sentence to the summary
            :param paper:  the paper to be summarized
        """
        idx = 0
        secIdx = 0
        if targetSentence.getSection() is not None:
            secIdx = targetSentence.getSection().getIndex()
        words = sorted(targetSentence.getCandWords(), key=lambda Word: Word.getFMeasure().get(secIdx, 0), reverse=True)
        # Sometimes the same keyword take place twice in the same phrase. so we add this list to prevent
        # processing the same word more than one time.
        modifiedWords = []
        for word in words:
            if word not in modifiedWords and idx < WordsNumber:
                idx += 1
                word.modifyFMeasure(secIdx, math.pow(word.getFMeasure()[secIdx], 2))
                modifiedWords.append(word)

reload(sys)
sys.setdefaultencoding('utf8')
corpusPath = '/Users/hazemalsaied/RA/Corpus/Sci-Summ-Test/'
summPath = '/Users/hazemalsaied/RA/Evaluation/SciSumm/summaries'
SciSummSigleDocSummarizer.summarizeSciSumm(corpusPath, summPath)