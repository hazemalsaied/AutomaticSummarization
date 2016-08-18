import math
import os
import sys

import powerlaw
from matplotlib import pyplot as plt

from correction import Corrector
from ducSummarizer import DucSummarizer
from paper import Paper
from termBank import TermBank


class GraphSummarizer:
    """

    """

    sourceCorpusPath = '/Users/hazemalsaied/RA/Corpus/Sci-Summ'
    corpusPath = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/'
    htmlCorpus = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/html'
    modelPath = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/models/'
    peerPath = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/systems/'

    # dictionary for storing the edges, the key is a list of lemmas of the edge.
    graph = {}
    importanceRatio = 0

    @staticmethod
    def generateGraphSummaryFast(getBinarySummaries=False, forTerms=False):
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
                                                'Reference_XML/' + documentName + '-correction.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                # newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(referenceXmlPath, isDucFile=False)

                # GraphSummarizer.buildGraph()
                # sortedEdges = sorted(GraphSummarizer.graph.values(), key=lambda Edge: Edge.score, reverse=True)
                # GraphSummarizer.importanceRatio = GraphSummarizer.getXMin(sortedEdges)
                summary = []
                traitedLemmas = []
                for ann in paper.getAnnotations():

                    for citSent in ann.citingSentencesDictionary.values():
                        Corrector.correctSentence(citSent, paperText)

                        if forTerms:
                            termsList = []
                            lemmaList = []

                            for term in citSent.getTerms():
                                if term.getLemma() in TermBank.termsBank.keys():
                                    term = TermBank.termsBank[term.getLemma()]
                                    termsList.append(term)
                                    lemmaList.append(term.getLemma())
                            if len(termsList) > 0:
                                weightByWords = False
                                for term in termsList:
                                    if term.getLemma() not in traitedLemmas:
                                        traitedLemmas.append(term.getLemma())
                                        wordEdges = GraphSummarizer.getTermRelations(term)
                                        GraphSummarizer.minimizeWeights(term, wordEdges, lemmaList, forTerms=True)
                            else:
                                weightByWords = True
                                wordsList = []
                                lemmaList = []
                                for word in citSent.getWords():
                                    if word.getLemma() in TermBank.wordsBank.keys():
                                        word = TermBank.wordsBank[word.getLemma()]
                                        wordsList.append(word)
                                        lemmaList.append(word.getLemma())

                                for word in wordsList:
                                    if word.getLemma() not in traitedLemmas:
                                        traitedLemmas.append(word.getLemma())
                                        wordEdges = GraphSummarizer.getTermRelations(word)
                                        GraphSummarizer.minimizeWeights(word, wordEdges, lemmaList, forTerms=False)
                        else:# For Words
                            weightByWords = True
                            lemmaList = []
                            wordList = []
                            for word in citSent.getWords():
                                if word.getLemma() in TermBank.wordsBank.keys():
                                    word = TermBank.wordsBank[word.getLemma()]
                                    wordList.append(word)
                                    lemmaList.append(word.getLemma())

                            for word in wordList:
                                if word.getLemma() not in traitedLemmas:
                                    traitedLemmas.append(word.getLemma())
                                    wordEdges = GraphSummarizer.getWordRelations(word)
                                    GraphSummarizer.minimizeWeights(word, wordEdges, lemmaList, forTerms=False)
                        if forTerms and weightByWords:
                            sents = GraphSummarizer.getSentencesWeights(paper)
                            for sent in sents:
                                distance = sent.getDis(citSent,isTempFMeasure=True)
                                if distance < 1:  # sent.getDistance(citSent)
                                    ann.addSpanResultItem(distance, sent, citSent)
                        else:
                            sents = GraphSummarizer.getSentencesWeights(paper, forTerms=forTerms)
                            for sent in sents:
                                distance = sent.getDis(citSent, forTerms=forTerms, isTempFMeasure=True)
                                if distance < 1:  # sent.getDistance(citSent)
                                    ann.addSpanResultItem(distance, sent, citSent)

                        sortedSpanResults = sorted(ann.spanResultList,
                                                   key=lambda SpanResultItem: SpanResultItem.distance)
                        sentNumm = len(ann.referenceSentencesDictionary.values())
                        idx = 1
                        for sortedSpanResult in sortedSpanResults:
                            if sortedSpanResult.referenceSent not in summary:
                                summary.append(sortedSpanResult.referenceSent)
                                idx += 1
                                if idx > sentNumm:
                                    break
                                    # DucSummarizer.adjustWeights(sortedSpanResults[0].referenceSent, paper, WordsNumber=7)
                ff = open(os.path.join(GraphSummarizer.peerPath, documentName + '_Gsummary.md'), 'w+')
                ff.write(DucSummarizer.generateSummaryText(summary))
                ff.close()
            break

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

                # GraphBuilder.buildGraph()
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
                        distance = sent.getDis(citSent, isTempFMeasure=True,
                                               usingFeatures=True)  # sent.getDistance(citSent)
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
    def getSentencesWeights(paper, forTerms=False):
        """
            After assigning weights for all the words of the article, we assign weights for sentences in calculating the
            average of informative words for each sentence.

            :param paper:  the article after weighting words.
        """
        sents = []
        for section in paper.getSections():
            for sent in section.getSentences():
                sent.setTempWeight(usingFeatures=True, forTerms=forTerms)
                sents.append(sent)
        if paper.getTitle() is not None:
            paper.getTitle().setTempWeight(usingFeatures=True, forTerms=forTerms)
            sents.append(paper.getTitle())

        sents = sorted(sents, key=lambda Sentence: Sentence.getTempWeight(), reverse=True)
        return sents

    @staticmethod
    def minimizeWeights(w, wordEdges, lemmaList, forTerms=False):

        dictionary = TermBank.wordsBank
        if forTerms:
            dictionary = TermBank.termsBank

        w = dictionary[w.getLemma()]
        tempFm = {}
        for k in w.getFMeasure().keys():
            tempFm[k] = max(w.getFMeasure().values()) * 5
        w.setTempfMeasure(tempFm)
        for edge in wordEdges:
            score = edge.getScore()

            newWord = edge.firstWord
            if w is edge.firstWord:
                newWord = edge.secondWord
            if newWord.getLemma() not in lemmaList:
                tempFm = {}
                for k in newWord.getFMeasure().keys():
                    tempFm[k] = math.pow(newWord.getFMeasure()[k], 2 + int(score / 100))
                newWord.setTempfMeasure(tempFm)
            else:
                newWord.setTempfMeasure(newWord.getFMeasure())
    # TODO: change the 1.2 to others values to measure its effect

    @staticmethod
    def maximizeWeights(w, wordEdges):
        w = TermBank.wordsBank[w.getLemma()]
        tempFm = {}
        for k in w.getFMeasure().keys():
            tempFm[k] = w.getFMeasure()[k] * 5
        w.setTempfMeasure(tempFm)
        for edge in wordEdges:
            # GraphSummarizer.graph.keys():
            # if w.getLemma() in edgeKey:
            # edge = GraphSummarizer.graph[edgeKey]
            edge.getScore()
            newWord = edge.firstWord
            if w is edge.firstWord:
                newWord = edge.secondWord
            # if edge.score > GraphSummarizer.importanceRatio:
            amplifier = (4.2 + float(edge.score / 10000))
            # else:
            #    amplifier = (1 + float(edge.score / 10000))
            #    tempFm = {}
            for k in newWord.getFMeasure().keys():
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
    def getTermRelations(term):
        wordEdges = []
        for ph in term.getSentences():

            for phTerm in ph.getTerms():
                if term is phTerm or phTerm not in TermBank.termsBank.values():
                    continue
                edge = Edge.addSharedSentence(term, phTerm, ph)
                if edge not in wordEdges:
                    wordEdges.append(edge)
        # for edge in GraphSummarizer.graph.values():
        #    edge.getScore()
        return wordEdges

    @staticmethod
    def getWordRelations(term):
        wordEdges = []
        for ph in term.getSentences():

            for phTerm in ph.getWords():
                if term is phTerm:
                    continue
                edge = Edge.addSharedSentence(term, phTerm, ph)
                if edge not in wordEdges:
                    wordEdges.append(edge)
        # for edge in GraphSummarizer.graph.values():
        #    edge.getScore()
        return wordEdges

    # @staticmethod
    # def getWordRelations(word):
    #     wordEdges = []
    #     for ph in word.getSentences():
    #         idx = ph.getWords().index(word)
    #         words = []
    #
    #         wordNum = 0
    #         if idx < len(ph.getWords()) - 1:
    #             for wordIdx in xrange(idx + 1, len(ph.getWords()) - 1):
    #                 if ph.getWords()[wordIdx].getLemma() in TermBank.wordsBank.keys():
    #                     words.append(ph.getWords()[wordIdx])
    #                     wordNum += 1
    #                 if wordNum == 3:
    #                     break
    #
    #         wordNum = 0
    #         if idx > 0:
    #             for wordIdx in xrange(0, idx - 1):
    #                 if ph.getWords()[idx - wordIdx - 1].getLemma() in TermBank.wordsBank.keys():
    #                     words.append(ph.getWords()[idx - wordIdx - 1])
    #                     wordNum += 1
    #                 if wordNum == 3:
    #                     break
    #
    #         for phWord in words:
    #             if word is phWord or phWord not in TermBank.wordsBank.values():
    #                 continue
    #             edge = Edge.addSharedSentence(word, phWord, ph)
    #             if edge not in wordEdges:
    #                 wordEdges.append(edge)
    #     # for edge in GraphSummarizer.graph.values():
    #     #    edge.getScore()
    #     return wordEdges

    @staticmethod
    def getWordRelationsOld(word):

        for ph in word.getSentences():
            idx = ph.getWords().index(word)
            if idx - 3 < 0:
                startIdx = 0
            else:
                startIdx = idx - 3
            if idx + 3 >= len(ph.getWords()):
                endIdx = len(ph.getWords()) - 1
            else:
                endIdx = idx + 3
            words = []
            for wordIdx in xrange(startIdx, endIdx):
                words.append(ph.getWords()[wordIdx])

            for phWord in ph.getWords():
                if word is phWord or phWord not in TermBank.wordsBank.values():
                    continue
                Edge.addSharedSentence(word, phWord, ph)
        for edge in GraphSummarizer.graph.values():
            edge.getScore()

    @staticmethod
    def buildGraph():
        idx = 0
        for word in TermBank.wordsBank.values():
            idx += 1
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
        return edge

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
GraphSummarizer.generateGraphSummaryFast()

# system 1: word-based graph with
