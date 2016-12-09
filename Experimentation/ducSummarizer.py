import math
import os
import os.path
import xml.etree.ElementTree as ET
from shutil import copyfile

import powerlaw
from paper import Paper
from matplotlib import pyplot as plt
from termBank import TermBank
from sentence import Sentence

class DucSummarizer:
    """
        A class used for generating a single document summary, the DUC 2007 data is used.
    """
    ducDocumentsPath = "/Users/hazemalsaied/RA/Corpus/DUC2007/corpus/"
    ducPeerPath = '/Users/hazemalsaied/RA/Corpus/DUC2007/ROUGE/peers/'
    ducModelPath = '/Users/hazemalsaied/RA/Corpus/DUC2007/ROUGE/models/'
    evPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/'
    evReferencePath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/models/'
    evSystemPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/systems/'
    evHtmlPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/'

    @staticmethod
    def getStatistics(path, doubleSection=False):
        """
            This method generate all summary of Duc 2007 files and save them into the evaluation folder

            :param path:  '/Users/hazemalsaied/git/scisumm-corpus/DUC2007/update_corpus/'
            :return:
        """
        for ducFile in os.listdir(path):
            if ducFile == '.DS_Store':
                continue

            paper = Paper(os.path.join(path, ducFile), isDucFile=True, doubleSection=doubleSection)
            classifierList = []
            for word in TermBank.wordsBank.values():
                wordCls = WordClassifier(word.getText(), word.getTotalOccurrence(), word.getOccurrence())
                classifierList.append(wordCls)

            sortedClassifierList = sorted(classifierList,
                                           key=lambda WordClassifier: WordClassifier.frecuency,reverse=True)

            statistics = 'Word,Frecuency,Frecuency in sections\n'
            for cls in sortedClassifierList[:50]:
                statistics += cls.wordStr + ','+ str(cls.frecuency) + ','+ str(cls.occurrence.values()).replace(',','-').replace('[','').replace(']','') + '\n'


            # Writing the summary to the evaluation folder as a peer summary
            fileName = ducFile[0:5] + '_statistics.csv'
            stPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/Statistics/'
            if not os.path.exists(stPath):
                os.makedirs(stPath)

            ff = open(stPath + fileName, 'w+')
            ff.write(statistics)
            ff.close()

    @staticmethod
    def summarizeDUC2007(path,doubleSection=False):
        """
            This method generate all summary of Duc 2007 files and save them into the evaluation folder

            :param path:  '/Users/hazemalsaied/git/scisumm-corpus/DUC2007/update_corpus/'
            :return:
        """
        if not os.path.exists(DucSummarizer.evSystemPath):
            os.makedirs(DucSummarizer.evSystemPath)
        for ducFile in os.listdir(path):
            if ducFile == '.DS_Store':
                continue
            summary = DucSummarizer.summarizeSD(os.path.join(path, ducFile), isDucFile=True,doubleSection=doubleSection)
            # Deleting empty lines for applying the convention of ROUGE 2.0
            lines = summary.split('\n')
            newSummm = ''
            for line in lines:
                if line.rsplit():
                    newSummm += line + '\n'
            newSummm = newSummm[:-1]
            # Writing the summary to the evaluation folder as a peer summary
            fileName = ducFile[0:5] + '_sumNonRed.md'
            ff = open(os.path.join(DucSummarizer.evSystemPath, fileName), 'w+')
            ff.write(newSummm)
            ff.close()

    @staticmethod
    def summarizeSD(xmlFilePath, isDucFile=False, doubleSection=False):
        """
            Static method responsible of processing the paper from A to Z.
            it provoke all needed methods form summarizing the paper.

            :param xmlFilePath: the relative path of the xml representing the CL Paper we have to summarize
            :param isDucFile
        """
        paper = Paper(xmlFilePath, isDucFile=isDucFile,doubleSection=doubleSection)
        summarySents = DucSummarizer.getSDSummary(paper)
        return DucSummarizer.generateSummaryText(summarySents)

    @staticmethod
    def getSDSummary(paper):
        """
            this method is responsible of selecting the most important sentences of the article.
            the important sentence is the sentence whose weight is the bigger.

            :param paper:  the article after weighting words and sentences.
            :return: a list of selected @sentence objects.
        """
        summary = []
        orderedSents = DucSummarizer.getSentencesWeights(paper)
        idx=0
        while orderedSents[idx].getWordsNum() < 15:
            idx +=1
        firstSent = orderedSents[idx]
        summary.append(firstSent)
        summaryLength = firstSent.getWordsNum()
        while summaryLength < 100:
            DucSummarizer.adjustWeights(summary[-1], paper)
            orderedSents = DucSummarizer.getSentencesWeights(paper)
            # Adding non-repeated sentence
            for sent in orderedSents:
                if sent not in summary and sent.getWordsNum() > 15:
                    summary.append(sent)
                    summaryLength += sent.getWordsNum()
                    break
        return summary

        adjustWeights

    @staticmethod
    def plottingSentences(orderedSents):
        """
            For plotting the orderedSents of the article according to their weights

            :param orderedSents:  a list of paper sentences ordered according to their weights
        """
        xArr = []
        for sent in orderedSents:
            xArr.append(sent.getWeight())
        plt.plot(xArr)
        plt.show()

    @staticmethod
    def plottingWords(words):
        """
           For plotting the words of the article according to their weights
        """
        sortedWords = sorted(words, key=lambda Word: max(Word.getFMeasure().values()),
                             reverse=True)
        xArr = []
        for word in sortedWords:
            xArr.append(max(word.getFMeasure().values()))
        plt.plot(xArr)
        plt.show()

    @staticmethod
    def getXMin(words):
        """
           For plotting the words of the article according to their weights
        """
        sortedWords = sorted(words, key=lambda Word: max(Word.getFMeasure().values()),
                             reverse=True)
        xArr = []
        for word in sortedWords:
            xArr.append(max(word.getFMeasure().values()))

        results = powerlaw.Fit(xArr)
        return results.power_law.xmin

    @staticmethod
    def getXMinSentence(sentences):
        """
           For plotting the words of the article according to their weights
        """
        sortedSents = sorted(sentences, key=lambda Sentence: Sentence.getWeight(), reverse=True)
        xArr = []
        for sent in sortedSents:
            xArr.append(sent.getWeight())

        results = powerlaw.Fit(xArr)
        return results.power_law.xmin

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
        if summaryLenght + sent.getWordsNum() > 100:
            r = summaryLenght + sent.getWordsNum() - 100
            idx = 0
            for word in sent.getWords():
                if idx <= r:
                    summaryText += word.getText() + ' '
                    idx += 1
                else:
                    break

        return summaryText

    @staticmethod
    def prepareDUCPeer(path):
        """
            This method remove all DUC2007 peer files attached to the update summary task.
        :param path: the path to the peer files of DUC 2007 for ROUGE : /Users/hazemalsaied/git/scisumm-corpus/DUC2007/updateEval/ROUGE/systems/
        """
        if not os.path.exists(DucSummarizer.evSystemPath):
            os.makedirs(DucSummarizer.evSystemPath)
        for root, _, files in os.walk(path):
            for f in files:
                fullpath = os.path.join(root, f)
                if f[6] != 'A':
                    os.remove(fullpath)
                else:
                    newFileName = f[:5] + '_' + f[-2:] + '.md'
                    copyfile(fullpath, os.path.join(DucSummarizer.evSystemPath, newFileName))

    @staticmethod
    def prepareDUCCorpus(path):
        """
            This method remove all DUC2007 peer files attached to the update summary task.
        :param path: the path to the peer files of DUC 2007 for ROUGE : /Users/hazemalsaied/git/scisumm-corpus/DUC2007/updateEval/ROUGE/systems/
        """
        for root, _, files in os.walk(path):
            for f in files:
                if f[-5] != 'A':
                    fullPath = os.path.join(root, f)
                    os.remove(fullPath)

    @staticmethod
    def prepareModelNameConvention(path):
        """
        Copy the model files of DUC 2007 into the evaluation folder

        :param path:
        :return:
        """
        if not os.path.exists(DucSummarizer.evReferencePath):
            os.makedirs(DucSummarizer.evReferencePath)
        for modelFile in os.listdir(path):
            srcname = os.path.join(path, modelFile)
            taskName = modelFile[0:5]
            newName = taskName + '_' + modelFile[-3] + '-' + modelFile[-1] + '.md'
            copyfile(srcname, os.path.join(DucSummarizer.evReferencePath, newName))

    @staticmethod
    def normailzeSummaries():
        DucSummarizer.evReferencePath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/4/models/'
        DucSummarizer.evSystemPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/4/systems/'
        DucSummarizer.evHtmlPath = DucSummarizer.evHtmlPath + '/html/4/'
        if not os.path.exists(DucSummarizer.evHtmlPath):
            os.makedirs(DucSummarizer.evHtmlPath)
        if not os.path.exists(DucSummarizer.evHtmlPath + 'models'):
            os.makedirs(DucSummarizer.evHtmlPath + 'models')
        if not os.path.exists(DucSummarizer.evHtmlPath + 'systems'):
            os.makedirs(DucSummarizer.evHtmlPath + 'systems')
        for root, _, files in os.walk(DucSummarizer.evReferencePath):
            for f in files:
                DucSummarizer.normailzeSummary(f, 'models')
        for root, _, files in os.walk(DucSummarizer.evSystemPath):
            for f in files:
                DucSummarizer.normailzeSummary(f, 'systems')

    @staticmethod
    def normailzeSummary(f, folder):
        DucSummarizer.evPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/4/'
        fullPath = os.path.join(DucSummarizer.evPath + folder, f)

        fo = open(fullPath, "rw+")
        lines = fo.readlines()
        summary = '<html>\n<head><title>'
        summary += f[:-3]
        summary += '</title> </head>\n<body bgcolor="white">\n'
        idx = 0
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            summary += '<a name="' + str(idx) + f[2:5] + '">[' + f[2:5] + ']</a> <a href="#' + f[2:5] + '" id=' \
                       + f[2:5] + str(idx) + '>' + line + '</a>\n'
            idx += 1
        summary = summary[:-1] + '</body>\n</html>\n'

        file = open(DucSummarizer.evHtmlPath + folder + '/' + f[:-2] + 'html', 'w')
        file.write(summary)
        file.close()

    @staticmethod
    def generateEvalXML():

        root = ET.Element('ROUGE-EVAL')
        root.set('version', '1.55')
        taskDic = []
        idList = []
        DucSummarizer.evReferencePath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/1/models/'
        DucSummarizer.evSystemPath = '/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/DUC2007/1/systems/'
        for roots, _, files in os.walk(DucSummarizer.evReferencePath):
            for f in files:
                if f.split('_')[0] not in taskDic:
                    taskDic.append(f.split('_')[0])
        idx = 1
        for task in taskDic:
            eval = ET.SubElement(root, 'EVAL')
            eval.set('ID', str(idx))
            peerRoot = ET.SubElement(eval, 'PEER-ROOT')
            peerRoot.text = 'c:/rouge/DUC2007Html/systems'
            modelRoot = ET.SubElement(eval, 'MODEL-ROOT')
            modelRoot.text = 'c:/rouge/DUC2007Html/models'

            models = ET.SubElement(eval, 'MODELS')

            inputFormat = ET.SubElement(eval, 'INPUT-FORMAT')
            inputFormat.set('TYPE', 'SEE')
            referenceIdx = 1
            for roooot, _, files in os.walk(DucSummarizer.evReferencePath):
                for f in files:
                    if f.startswith(task):
                        reference = ET.SubElement(models, 'M')
                        reference.set('ID', str(referenceIdx))  # f.split('_')[1][:-5])  #
                        reference.text = f[:-2] + 'html'
                        referenceIdx += 1

            peers = ET.SubElement(eval, 'PEERS')
            peerIdx = 1
            for rooot, _, files in os.walk(DucSummarizer.evSystemPath):
                for f in files:
                    if f.startswith(task):
                        peer = ET.SubElement(peers, 'P')
                        if f.split('_')[1][:-3] == 'sum':
                            peer.set('ID', '59')
                        else:
                            peer.set('ID', f.split('_')[1][:-3])  # str(peerIdx))
                        peer.text = f[:-2] + 'html'
                        peerIdx += 1

            idx += 1
        tree = ET.ElementTree(root)
        tree.write("/Users/hazemalsaied/RA/Evaluation/SingleDocSumm/duc2007.xml")

class WordClassifier:

    def __init__(self, wordStr, frecuency, occurrence):
        self.wordStr = wordStr
        self.frecuency = frecuency
        self.occurrence = occurrence


#DucSummarizer.prepareDUCPeer(DucSummarizer.ducPeerPath)
#DucSummarizer.prepareModelNameConvention(DucSummarizer.ducModelPath)
#DucSummarizer.prepareDUCCorpus(DucSummarizer.ducDocumentsPath)
#DucSummarizer.summarizeDUC2007(DucSummarizer.ducDocumentsPath, True)
#DucSummarizer.getStatistics(DucSummarizer.ducDocumentsPath)
#DucSummarizer.normailzeSummaries()
#DucSummarizer.generateEvalXML()
