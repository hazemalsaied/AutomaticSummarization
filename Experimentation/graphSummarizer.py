import os
import sys

import powerlaw
from paper import Paper
from matplotlib import pyplot as plt

from correction import Corrector
from termBank import TermBank
from ducSummarizer import DucSummarizer
from graphVisualisation import GraphBuilder

class GraphSummarizer:
    """

    """

    sourceCorpusPath = '/Users/hazemalsaied/RA/Corpus/'
    corpusPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/SCISUMM/'
    htmlCorpus = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/SCISUMM-NonBinaryHtml/'
    modelPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/SCISUMM/models/'
    peerPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/SCISUMM/systems/'

    # dictionary for storing the edges, the key is a list of lemmas of the edge.
    graph = {}
    importanceRatio = 0

    @staticmethod
    def generateGraphSummary(getBinarySummaries=False):
        """
            This method create the mpdel summaries using the cosine similarity approach.
             for each sentence of the citation we search for the most close sentence of the article
        """

        if not os.path.exists(GraphSummarizer.peerPath):
            os.makedirs(GraphSummarizer.peerPath)
        for subdir, dirs, files in os.walk(GraphSummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(GraphSummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)

                #GraphBuilder.buildGraph()
                GraphSummarizer.buildGraph()
                sortedEdges = sorted(GraphSummarizer.graph.values(), key=lambda Edge: Edge.score, reverse=True)
                GraphSummarizer.importanceRatio = GraphSummarizer.getXMin(sortedEdges)
                summary = []
                for ann in paper.getAnnotations():

                    for citSent in ann.citingSentencesDictionary.values():
                        Corrector.correctSentence(citSent, paperText)
                        for word in citSent.getWords():
                            if word.getLemma() in TermBank.wordsBank.keys():
                                GraphSummarizer.maximizeWeights(word)
                    sents = GraphSummarizer.getSentencesWeights(paper)
                    for sent in sents:
                        distance = sent.getDis(citSent, isTempFMeasure=True)  # sent.getDistance(citSent)
                        ann.addSpanResultItem(distance, sent, citSent)
                    sortedSpanResults = sorted(ann.spanResultList,
                                               key=lambda SpanResultItem: SpanResultItem.distance)
                    for sortedSpanResult in sortedSpanResults:
                        if sortedSpanResult.referenceSent not in summary:
                            summary.append(sortedSpanResult.referenceSent)
                            break
                            # DucSummarizer.adjustWeights(sortedSpanResults[0].referenceSent, paper, WordsNumber=7)
                ff = open(os.path.join(GraphSummarizer.peerPath, documentName + '_Gsummary.md'), 'w+')
                ff.write(DucSummarizer.generateSummaryText(summary))
                ff.close()
            break

    @staticmethod
    def generateGraphSummaryUsingFeatures(getBinarySummaries=False):
        """
            This method create the mpdel summaries using the cosine similarity approach.
             for each sentence of the citation we search for the most close sentence of the article
        """

        if not os.path.exists(GraphSummarizer.peerPath):
            os.makedirs(GraphSummarizer.peerPath)
        for subdir, dirs, files in os.walk(GraphSummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(GraphSummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)
                GraphSummarizer.buildGraph()
                sortedEdges = sorted(GraphSummarizer.graph.values(), key=lambda Edge: Edge.score, reverse=True)
                GraphSummarizer.importanceRatio = GraphSummarizer.getXMin(sortedEdges)
                summary = []
                for ann in paper.getAnnotations():

                    for citId, citSent in ann.citingSentencesDictionary.iteritems():
                        Corrector.correctSentence(citSent, paperText)
                        for word in citSent.getWords():
                            if word.getLemma() in TermBank.wordsBank.keys():
                                GraphSummarizer.maximizeWeights(word)
                    paper.setTempFeatures()
                    sents = GraphSummarizer.getSentencesWeights(paper)
                    for sent in sents:
                        distance = sent.getDis(citSent, isTempFMeasure=True, usingFeatures=True)  # sent.getDistance(citSent)
                        ann.addSpanResultItem(distance, sent, citSent)
                    sortedSpanResults = sorted(ann.spanResultList,
                                               key=lambda SpanResultItem: SpanResultItem.distance)
                    for sortedSpanResult in sortedSpanResults:
                        if sortedSpanResult.referenceSent not in summary:
                            summary.append(sortedSpanResult.referenceSent)
                            break
                            # DucSummarizer.adjustWeights(sortedSpanResults[0].referenceSent, paper, WordsNumber=7)
                ff = open(os.path.join(GraphSummarizer.peerPath, documentName + '_Gsummary.md'), 'w+')
                ff.write(DucSummarizer.generateSummaryText(summary))
                ff.close()
            break

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
                sent.setTempWeight(usingFeatures=True)
                sents.append(sent)
        if paper.getTitle() is not None:
            paper.getTitle().setTempWeight(usingFeature=True)
            sents.append(paper.getTitle())

        sents = sorted(sents, key=lambda Sentence: Sentence.getTempWeight(), reverse=True)
        return sents



    # TODO: change the 1.2 to others values to measure its effect

    @staticmethod
    def maximizeWeights(w):
        w = TermBank.wordsBank[w.getLemma()]
        tempFm = {}
        for k in w.getFMeasure().keys():
            tempFm[k] = w.getFMeasure()[k] * 2
        w.setTempfMeasure(tempFm)
        for edgeKey in GraphSummarizer.graph.keys():
            if w.getLemma() in edgeKey:
                edge = GraphSummarizer.graph[edgeKey]
                newWord = edge.firstWord
                if w is edge.firstWord:
                    newWord = edge.secondWord
                if edge.score > GraphSummarizer.importanceRatio:
                    amplifier = (1.2 + float(edge.score / 10000))
                else:
                    amplifier = (1 + float(edge.score / 10000))
                    tempFm = {}
                for k in w.getFMeasure().keys():
                    tempFm[k] = newWord.getFMeasure()[k] * amplifier
                newWord.setTempfMeasure(tempFm)

    @staticmethod
    def plotEdges():
        sortedEdges = sorted(GraphSummarizer.graph.values(), key=lambda Edge: Edge.score, reverse=True)

        xArr = []
        for edge in sortedEdges:
            xArr.append(edge.score)
        plt.plot(xArr)
        plt.show()

    @staticmethod
    def getXMin(edges):
        """
           For plotting the words of the article according to their weights
        """
        # sortedEdges = sorted(GraphSummarizer.graph.values(), key=lambda Edge: Edge.score, reverse=True)
        xArr = []
        for edge in edges:
            xArr.append(edge.getScore())

        results = powerlaw.Fit(xArr)
        return results.power_law.xmin

    @staticmethod
    def buildGraph():
        idx = 0
        for word in TermBank.wordsBank.values():
            print idx
            idx +=1
            for ph in word.getSentences():
                for phWord in ph.getWords():
                    if word is phWord or phWord not in TermBank.wordsBank.values():
                        continue
                    Edge.addSharedSentence(word, phWord, ph)
        for edge in GraphSummarizer.graph.values():
            edge.getScore()

    @staticmethod
    def inGraph(w1, w2):
        if w1.getLemma() + '#' + w2.getLemma() in GraphSummarizer.graph.keys():
            return True
        if w2.getLemma() + '#' + w1.getLemma() in GraphSummarizer.graph.keys():
            return True
        return False

    @staticmethod
    def getEdge(w1, w2):
        if w1.getLemma() + '#' + w2.getLemma() in GraphSummarizer.graph.keys():
            return GraphSummarizer.graph[w1.getLemma() + '#' + w2.getLemma()]
        if w2.getLemma() + '#' + w1.getLemma() in GraphSummarizer.graph.keys():
            return GraphSummarizer.graph[w2.getLemma() + '#' + w1.getLemma()]
        return None

    @staticmethod
    def match(xmlFilePath):
        """
            This method is used as a primary experience of approaching the task of citation span text matching using the
            techniques of information retrieval

            :param xmlFilePath: the path of referential article

        """
        # paperText = Corrector.getPaperText(xmlFilePath)
        # newPaperPath = Corrector.correct(xmlFilePath, paperText)
        # Loading the corrected file
        referencePaper = Paper(xmlFilePath)
        DucSummarizer.getSentencesWeights(referencePaper)

        for ann in referencePaper.getAnnotations():
            print '#Analyzing the annotation :' + str(ann.citanceNumber) + '\n'
            print '##Reference Sentences: \n'
            sentIdx = '{ '
            sentIdxList = []
            for sent in ann.referenceSentences:
                sentIdx += str(sent.getIndex()) + ', '
                sentIdxList.append(sent.getIndex())
            sentIdx = sentIdx[:-1] + ' }'
            print sentIdx + '\n\n'

            for sent in ann.citingSentences:
                for term in sent.getTerms():
                    if term.getLemma() in TermBank.termsBank.keys():
                        brotherWord = TermBank.termsBank[term.getLemma()]
                        ann.query.append(brotherWord)
                for word in sent.getWords():
                    if word.getLemma() in TermBank.wordsBank.keys():
                        brotherWord = TermBank.wordsBank[word.getLemma()]
                        ann.query.append(brotherWord)

            for word in ann.query:
                if word.isPertinent():
                    print '**' + word.getText() + '** : '
                else:
                    print word.getText()
                sentIdx = '['
                sortedSent = sorted(word.getSentences(), key=lambda Sentence: Sentence.getWeight(), reverse=True)
                for sent in sortedSent[:10]:
                    if sent.getIndex() in sentIdxList:
                        sentIdx += '**' + str(sent.getIndex()) + '**, '
                    else:
                        sentIdx += str(sent.getIndex()) + ', '
                sentIdx = sentIdx[:-1] + ']' + '\n\n'
                print sentIdx


class Edge:
    def __init__(self, w1, w2):
        self.firstWord = w1
        self.secondWord = w2
        self.score = 0
        self.sentences = []
        self.localDistance = []

    @staticmethod
    def addSharedSentence(word, phWord, ph):

        if not GraphSummarizer.inGraph(word, phWord):
            edge = Edge.createEdge(word, phWord)
        else:
            edge = GraphSummarizer.getEdge(word, phWord)

        edge.addSentence(ph)

    def getScore(self):

        buf = 0
        for v in self.localDistance:
            buf += v
        buf = 100 - (buf / len(self.localDistance))
        self.score = len(self.sentences) * 100 + buf
        return self.score

    def addSentence(self, ph):
        if ph not in self.sentences:
            self.sentences.append(ph)
            self.localDistance.append(Edge.getDistanceInSentence(self.firstWord, self.secondWord, ph))

    @staticmethod
    def getDistanceInSentence(w1, w2, ph):
        """
            return the distance between two words in a sentence
            :param w1: the first word
            :param w2: the second word
            :param ph: the sentance
            :return: int the distance
        """
        if w1 not in ph.getWords() or w2 not in ph.getWords():
            return 0
        idx1 = ph.getWords().index(w1)
        idx2 = ph.getWords().index(w2)
        if idx1 - idx2 < 0:
            return idx2 - idx1
        return idx1 - idx2

    @staticmethod
    def createEdge(word, phWord):
        edge = Edge(word, phWord)
        edgeKey = word.getLemma() + '#' + phWord.getLemma()
        GraphSummarizer.graph[edgeKey] = edge
        return edge

    def __str__(self):
        sentt = ''
        for sent in self.sentences:
            sentt += str(sent.getIndex()) + ', '
        diss = ''
        for dis in self.localDistance:
            diss += str(dis) + ', '

        return self.firstWord.getText() + ' ' + self.secondWord.getText() + ' ' + str(
            self.getScore()) + ' distance : ' + \
               diss + ' sents: ' + sentt

reload(sys)
sys.setdefaultencoding('utf8')
GraphSummarizer.generateGraphSummary()
