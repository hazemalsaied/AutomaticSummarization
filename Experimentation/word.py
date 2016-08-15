import re
import string

from nltk.corpus import stopwords
from nltk.corpus import wordnet
from termBank import TermBank

class Word:
    titleWordWeight = 1.2
    abstractWordWeight = 1.2

    # The main initiator
    def __init__(self, text, sentence, index=None, paper=None, isTerm=False):
        self.__idx = None
        self.__isCandidate = True
        self.__isPertinent = False
        self.__indices = []
        self.__sentences = []
        self.__weight = {}
        self.__occurrence = {}
        self.__recall = {}
        self.__precision = {}
        self.__tempfMeasure = {}
        self.__fMeasure = {}
        self.__pertinencyMap = {}
        self.__hatedFF = -1
        self.__wordOccurrenceInSections = -1
        self.__lemma = ''
        self.__totalOccurrence = -1
        self.__maxWeight = -1
        self.__fakeWeight = -1
        self.__isFeature = {}
        self.__isTempFeature = {}
        self.__isContrastFeature = False
        self.__isAbstractWord = False
        self.__isTitleWord = False
        self.__paper = None
        self.__isTerm = isTerm
        if index is not None:
            self.addIndex(index)
        self.addSentence(sentence)
        numberPattern = re.compile("[-+]?\d*\.\d+|\d+")
        mixedPattern = re.compile("\w+")
        self.__isNumber = False
        self.__isStop = False
        self.__isMixed = False
        self.__isPunctuation = False
        if paper is not None:
            self.__paper = paper
        if text in string.punctuation:
            self.setAsPunctuation()
        if numberPattern.match(text):
            self.setAsNumber()
        if not mixedPattern.match(text):
            self.setAsMixed()
        if text.lower() in stopwords.words('english') or text.lower() in TermBank.stopWordsList:
            self.setAsStop()
        if self.__isPunctuation or self.__isMixed or self.__isStop or self.__isNumber or len(text) < 3:
            self.__isCandidate = False
        self.setText(text)
        if sentence.getSection() is not None:
            if isTerm:
                TermBank.termsBank[self.__lemma] = self
            elif self.isCandidateFeature():
                TermBank.addWordBankItem(self)
                sentence.getSection().addWordBankItem(self)

    def getTempfMeasure(self):
        return self.__tempfMeasure

    def setTempfMeasure(self, fmeasure):
        self.__tempfMeasure = fmeasure

    def setAsPertinent(self):
        self.__isPertinent = True

    def isPertinent(self):
        return self.__isPertinent

    def isTerm(self):
        return self.__isTerm

    def getIndices(self):
        return self.__indices

    def setIndices(self, index):
        self.__indices = index

    def addIndex(self, index):
        self.__indices.append(index)

    def setAsNumber(self):
        self.__isNumber = True

    def isNumber(self):
        if self.__isNumber:
            return True
        return False

    def setAsMixed(self):
        self.__isMixed = True

    def setAsPunctuation(self):
        self.__isPunctuation = True

    def isMixed(self):
        if self.__isMixed:
            return True
        return False

    def setAsStop(self):
        self.__isStop = True

    def isStop(self):
        if self.__isStop:
            return True
        return False

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text
        if self.isCandidateFeature():
            self.__lemma = TermBank.wordNetLemmatizer.lemmatize(self.__text).lower()
        else:
            self.__lemma = text.lower()

    def getLemma(self):
        if self.__lemma != '':
            return self.__lemma
        return self.__text

    def setLemma(self, text):
        self.__lemma = text.lower()

    def getWeight(self, sectionIndex):
        if sectionIndex in self.__weight:
            return self.__weight[sectionIndex]
        return 0

    def setWeight(self, weigh, sectionIndex):
        if sectionIndex not in self.__weight:
            if self.exist(TermBank.getAbstractTerms()):
                weigh *= Word.abstractWordWeight
                self.__isAbstractWord = True
            if self.exist(TermBank.getTitleTerms()):
                weigh *= Word.titleWordWeight
                self.__isTitleWord = True
            self.__weight[sectionIndex] = weigh

    def setMaxWeight(self):
        if self.isCandidateFeature() and self.__weight.values():
            self.__maxWeight = max(self.__weight.values())
        else:
            self.__maxWeight = 0

    def getFakeWeight(self, paper):
        if self.__fakeWeight == -1:
            self.setFakeWeight(paper)
        return self.__fakeWeight

    def getSynset(self):
        wordnet.synsets(self.getLemma())

    def setFakeWeight(self, paper):
        self.__fakeWeight = paper.getMaxWeight(self.getLemma())
        self.__maxWeight = paper.getMaxWeight(self.getLemma())

    def updateMaxWeight(self, w):
        self.__maxWeight = w

    def getMaxWeight(self):
        return self.__maxWeight

    def getPaper(self):
        return self.__paper

    def setPaper(self, paper):
        self.__paper = paper

    def getSentences(self):
        return self.__sentences

    def addSentence(self, sentence, isTitle=False):
        if isTitle:
            self.__sentences.append(sentence)
        elif sentence.getSection() is not None:
            self.__sentences.append(sentence)

    def setIdx(self, idx):
        self.__idx = idx

    def getIdx(self):
        return self.__idx

    def isCandidateFeature(self):
        return self.__isCandidate

    def setAsFeature(self, secIdx, isFeature):
        self.__isFeature[secIdx] = isFeature

    def isFeature(self,secIdx):
        return self.__isFeature[secIdx]

    def setAsTempFeature(self, secIdx, isFeature):
        self.__isTempFeature[secIdx] = isFeature

    def isTempFeature(self, secIdx):
        return self.__isTempFeature[secIdx]

    def setAsContrastFeature(self):
        self.__isContrastFeature = True

    def isContrastFeature(self):
        return self.__isContrastFeature

    def exist(self, list):
        for word in list:
            if word.getLemma() == self.__lemma:
                return True
        return False

    def getTotalOccurrence(self):

        if self.__totalOccurrence != -1:
            return self.__totalOccurrence

        self.__totalOccurrence = 0
        if self.__occurrence:
            for v in self.__occurrence.values():
                self.__totalOccurrence += v
        return self.__totalOccurrence

    def calculateOccurrence(self, sections):
        if self.isTerm() or self.isCandidateFeature():
            if not self.__occurrence:
                for section in sections:
                    self.__occurrence[section.getIndex()] = section.getWordOccurence(self.getLemma())

        return self.__occurrence

    def getOccurrence(self):
        return self.__occurrence

    def getSectionOccurrence(self, section):
        secIdx = section.getIndex()
        if secIdx in section.sectionOccurrences.keys():
            return section.sectionOccurrences[secIdx]
        buff = 0
        wordMemory = {}
        for sent in section.getSentences():
            for word in sent.getWords():
                if word.isCandidateFeature() and word.getLemma() not in wordMemory.keys():
                    wordMemory[word.getLemma()] = word
                    if secIdx in word.getOccurrence().keys():
                        buff += word.getOccurrence()[secIdx]
        section.sectionOccurrences[secIdx] = buff
        return buff

    def getSectionOccurrenceForTerms(self, section):
        secIdx = section.getIndex()
        if secIdx in section.sectionOccurrencesForTerms.keys():
            return section.sectionOccurrencesForTerms[secIdx]
        buff = 0
        termsMemory = {}
        for sent in section.getSentences():
            for word in sent.getTerms():
                if word.getLemma() not in termsMemory.keys():
                    termsMemory[word.getLemma()] = word
                    if secIdx in word.getOccurrence().keys():
                        buff += word.getOccurrence()[secIdx]
        section.sectionOccurrencesForTerms[secIdx] = buff
        return buff

    def getRecall(self, sections):
        if not self.isCandidateFeature():
            return {}
        if self.getTotalOccurrence() == 0:
            return {}
        for section in sections:
            self.__recall[section.getIndex()] = 0
            secIdx = section.getIndex()
            if self.getTotalOccurrence() != 0 and secIdx in self.__occurrence:
                self.__recall[secIdx] = float(self.__occurrence[secIdx]) / self.getTotalOccurrence()
            else:
                self.__recall[secIdx] = 0
        return  self.__recall

    def getPrecision(self, sections, forTerms=False):
        if not self.isCandidateFeature():
            return {}
        for section in sections:
            secIdx = section.getIndex()
            if forTerms:
                sectionOccurence = self.getSectionOccurrenceForTerms(section)
            else:
                sectionOccurence = self.getSectionOccurrence(section)
            self.__precision[secIdx] = 0
            if secIdx in self.__occurrence and sectionOccurence != 0:
                self.__precision[section.getIndex()] = float(self.__occurrence[secIdx]) / sectionOccurence
        return self.__precision

    def modifyFMeasure(self, id, value):
        self.__fMeasure[id] = value

    def setFMeasure(self, fmeasureDictionay):
        self.__fMeasure = fmeasureDictionay
    def getFMeasure(self):
        if self.__fMeasure:
            return self.__fMeasure
        return {}

    def getHatedFF(self):
        if self.__hatedFF != -1:
            return self.__hatedFF
        counter = 0
        buffer = 0
        for sectionIndex in xrange(0, TermBank.sectionsNumber):
            if self.getFMeasure() and self.getFMeasure()[sectionIndex] != 0:
                counter += 1
                buffer += self.getFMeasure()[sectionIndex]
        if counter != 0:
            self.__hatedFF = float(buffer) / counter
        else:
            self.__hatedFF = 0
        return self.__hatedFF

    def calculateFMeasure(self, sections, forTerms=False):
        if not self.isCandidateFeature():
            return {}

        self.getRecall(sections)
        self.getPrecision(sections, forTerms)
        for secIdx in xrange(0, TermBank.sectionsNumber):
            #secIdx = section.getIndex()
            self.__fMeasure[secIdx] = 0
            if secIdx in self.__precision and secIdx in self.__recall \
                    and (self.__precision[secIdx] + self.__recall[secIdx]) != 0:
                self.__fMeasure[secIdx] = 2 * self.__precision[secIdx] * self.__recall[secIdx] / \
                                          (self.__precision[secIdx] + self.__recall[secIdx])

        self.getHatedFF()
        self.__tempfMeasure = self.__fMeasure
        return self.__fMeasure

    def initializePertinencyMap(self):
        if TermBank.sectionsNumber == 0:
            print '#ERROR: initializePertinencyMap: sectionsNumber is 0'
            return
        for secIdx in xrange(0, TermBank.sectionsNumber):
            self.__pertinencyMap[secIdx] = False

    def updataPertinencyMap(self, secIdx):
        if not self.__pertinencyMap:
            self.initializePertinencyMap()
        if secIdx in self.__pertinencyMap.keys():
            self.__pertinencyMap[secIdx] = True

    def getPertinencyMap(self):
        if not self.__pertinencyMap:
            self.initializePertinencyMap()
        return self.__pertinencyMap

    def getPertinencyReport(self, secIdx, ):
        if secIdx not in self.__pertinencyMap.keys() or not self.__pertinencyMap[secIdx]:
            return ''
        result = self.getText() + ' **' + self.getLemma() + '** occurence: ' + str(
            self.__occurrence[secIdx]) + ', Total occurence: ' \
                 + str(self.__totalOccurrence) + ', F-measure: ' + str(self.__fMeasure[secIdx]) + '\n'
        result += '\t where: FF threshold : ' + str(self.__hatedFF) + ', FFd threshold '
        if self.isTerm():
            result += str(TermBank.hattedFFDForTerms) + '\n'
        else:
            result += str(TermBank.hattedFFD) + '\n'
        return result

    def __str__(self):
        result = self.getText()

        if self.__isContrastFeature:
            result += ': ,Contrast '
        if self.__isAbstractWord:
            result += ' ,Abstract '
        if self.__isTitleWord:
            result += ' ,Title '
        if self.isMixed():
            result += ' ,Mixed '
        if self.isStop():
            result += ' ,Stop'
        if self.isNumber():
            result += ' ,Number'
        # if self.__weight is not None:
        #    result += '\n' + ' ,weight: ' + str(self.__weight)
        if self.__fMeasure:
            result += '\n' + ' ,fmeasure: ' + str(self.__fMeasure)
        return result