import numpy as np
from nltk import word_tokenize
from numpy.linalg import norm
from scipy import spatial

from termBank import TermBank
from word import Word


class Sentence:
    def __init__(self, text, index=None, section=None, isAbstract=None):

        self.__text = text
        self.__words = []
        self.__isFake = False
        self.__section = None
        self.__usefulWordsNum = 0
        self.__termsNum = 0
        self.__isValid = True
        self.__weight = -1
        self.__index = index
        if index is not None:
            TermBank.addSentenceBankItem(self)
        wordList = word_tokenize(text)
        self.__wordsNum = len(wordList)
        if wordList[len(wordList) - 1].strip() == '\n':
            wordList = wordList[:len(wordList) - 1]
        if section is None and index is None and isAbstract is None:
            for item in wordList:
                self.__words.append(Word(item, self))

        else:
            self.setIndex(index)
            self.__section = section
            if section is not None:
                section.addText(text)
            if isAbstract:
                for item in wordList:
                    self.addWord(Word(item, self, wordList.index(item), None))
                return

            for item in wordList:
                word = None
                if TermBank.isInWordBank(item.lower()):
                    word = TermBank.getWordBankItem(item.lower())
                    word.addIndex(wordList.index(item))
                    word.addSentence(self)
                    self.addWord(word)
                else:
                    word = self.addWord(Word(item, self, wordList.index(item), self.getSection().getPaper()))
                if word.isCandidateFeature():
                    self.__usefulWordsNum += 1
            # adding this feature for preventing the distorted sentences from entering in the competition or summarization.
            if float(len(self.getMixedWords())) / len(self.getWords()) > 0.6:
                self.__isValid = False
        # TODO
        # Extracting the terms
        for word in self.getWords():
            if not word.isCandidateFeature():
                continue
            secondWord = self.getNextWord(word)
            if secondWord is None or not secondWord.isCandidateFeature():
                continue

            self.__termsNum += 1
            lemmatizedTermText = word.getLemma() + ' ' + secondWord.getLemma()
            if lemmatizedTermText.lower() in TermBank.termsBank.keys():
                term = TermBank.termsBank[lemmatizedTermText.lower()]
                term.addIndex(self.getWords().index(word))
                term.addSentence(self)
                self.addWord(term)
            else:
                paper = None
                if self.getSection() is not None:
                    paper = self.getSection().getPaper()

                self.addWord(
                    Word(lemmatizedTermText, self, self.getWords().index(word), paper,
                         True))
            # thirdWord = self.getNextWord(secondWord)
            # if thirdWord is not None and thirdWord.isCandidateFeature():
            #     self.__termsNum += 1
            #     lemmatizedTermText += ' ' + thirdWord.getLemma()
            #     if lemmatizedTermText.lower() in TermBank.termsBank.keys():
            #         term = TermBank.termsBank[lemmatizedTermText.lower()]
            #         term.addIndex(self.getWords().index(word))
            #         term.addSentence(self)
            #         self.addWord(term)
            #     else:
            #         paper = None
            #         if self.getSection() is not None:
            #             paper = self.getSection().getPaper()
            #         self.addWord(
            #             Word(lemmatizedTermText, self, self.getWords().index(word),
            #                  paper, True))
                    # Paper.addSentenceBankItem(self)

    def getIndex(self):
        return self.__index

    def setIndex(self, index):
        if self.__index is None:
            self.__index = int(index)
            TermBank.addSentenceBankItem(self)
        else:
            self.__index = int(index)

    def getWeight(self):
        if self.__weight != -1 and self.getSection() is not None:
            self.setWeight()
        return self.__weight

    def setWeight(self, weight=-1, paper=None):
        """
            After assigning weights for all the words of the article, we assign weights for sentences in calculating the
            average of informative words for each sentence.

            :param paper: if the sentence is fake or not associated with a section we use words' weights stored in paper object
            :return: a float representing the weight of the sentence
        """
        if weight != -1:
            self.__weight = weight
            return
        self.__weight = 0
        counter = 0
        for word in self.getWords():
            word = TermBank.getWordBankItem(word.getLemma())
            if word is not None:
                wordWeight = 0
                counter += 1
                if self.getSection() is None:
                    if word.getFMeasure():
                        wordWeight = max(word.getFMeasure().values())
                else:
                    wordWeight = word.getFMeasure()[self.getSection().getIndex()]
                self.__weight += wordWeight
        if counter is not 0:
            self.__weight = self.__weight / counter
        return self.__weight

    def getTempWeight(self):
        return self.__TempWeight

    def setTempWeight(self, weight=-1, paper=None, usingFeatures=False,forTerms=False):
        """
            After assigning weights for all the words of the article, we assign weights for sentences in calculating the
            average of informative words for each sentence.

            :param paper: if the sentence is fake or not associated with a section we use words' weights stored in paper object
            :return: a float representing the weight of the sentence
        """
        if weight != -1:
            self.__TempWeight = weight
            return
        self.__TempWeight = 0
        counter = 0
        dictionary = TermBank.wordsBank
        if forTerms:
            dictionary = TermBank.termsBank
        composantList = self.getWords()
        if forTerms:
            composantList = self.getTerms()
        for composant in composantList:
            #if usingFeatures and self.getSection() is not None and not word.isTempFeature(self.getSection().getIndex()):
            #        continue
            if not composant.isTerm() and not composant.isCandidateFeature():
                continue
            composant = dictionary[composant.getLemma()]
            if composant is not None and composant.getTempfMeasure():
                composantWeight = 0
                counter += 1
                if self.getSection() is None:
                        composantWeight = max(composant.getTempfMeasure().values())
                else:
                    composantWeight = composant.getTempfMeasure()[self.getSection().getIndex()]
                self.__TempWeight += composantWeight
        if counter is not 0:
            self.__TempWeight = self.__TempWeight / counter
        return self.__TempWeight

    def getSection(self):
        return self.__section

    def setSection(self, section):
        self.__section = section

    def isFake(self):
        return self.__isFake

    def setAsFake(self):
        self.__isFake = True

    def getFakeWeight(self, paper):
        counter = 0
        weightBuffer = 0
        for word in self.__words:
            if word.isCandidateFeature():
                counter += 1
            weightBuffer += word.getFakeWeight(paper)
        if counter is not 0:
            return weightBuffer / counter
        return 0

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text

    def getCandWords(self):
        result = []
        for word in self.__words:
            if not word.isTerm() and word.isCandidateFeature() and word.getFMeasure():
                result.append(word)
        return result

    def getWords(self):
        result = []
        for word in self.__words:
            if not word.isTerm():
                result.append(word)
        return result

    def getTerms(self):
        result = []
        for word in self.__words:
            if word.isTerm():
                result.append(word)
        return result

    def setWords(self, words):
        self.__words = words

    def addWord(self, word):
        self.__words.append(word)
        return word

    def getWordsNum(self):
        return self.__wordsNum

    def getTermsNum(self):
        return self.__termsNum

    def getUsefulWordsNum(self):
        return self.__usefulWordsNum

    def getImportantLength(self):
        length = 0
        for word in self.getWords():
            if word.isCandidateFeature():
                length += 1
        return length

    def getLemmaList(self):
        lemma = []
        for word in self.getWords():
            if word.isCandidateFeature():
                lemma.append(word.getLemma())
        return lemma

    def getLemmaListOfTerms(self):
        lemma = []
        for word in self.getTerms():
            lemma.append(word.getLemma())
        return lemma

    def getMixedWords(self):
        result = []
        for word in self.getWords():
            if word.isMixed():
                result.append(word)
        return result

    def isValid(self):
        return self.__isValid

    def getWordBag(self, ph1, ph2, usingFeatures, forTerms=False,forWordsAndTerms=False):
        wordBag = {}

        if forWordsAndTerms:

            terms = ph1.getTerms() + ph2.getTerms()
            tempWords = ph1.getWords() + ph2.getWords()
            for word in tempWords:
                addWord = True
                for term in terms:
                    if word.getLemma() in term.getLemma():
                        addWord = False
                if addWord:
                    terms.append(word)

            for word in terms:
                if word.isTerm():
                    if word.getLemma() in TermBank.termsBank.keys():
                        if usingFeatures and self.getSection() is not None and not word.isTempFeature()[
                            self.getSection().getIndex()]:
                            continue
                        copyWord = TermBank.termsBank[word.getLemma()]
                        if word.isCandidateFeature() and copyWord.getFMeasure():
                            wordBag[copyWord.getLemma()] = copyWord
                else:
                    if word.getLemma() in TermBank.wordsBank.keys():
                        if usingFeatures and self.getSection() is not None and not word.isTempFeature()[
                            self.getSection().getIndex()]:
                            continue
                        copyWord = TermBank.wordsBank[word.getLemma()]
                        if word.isCandidateFeature() and copyWord.getFMeasure():
                            wordBag[copyWord.getLemma()] = copyWord
            return wordBag


        if forTerms:
            words = ph1.getTerms() + ph2.getTerms()
            for word in words:
                if word.getLemma() in TermBank.termsBank.keys():
                    if usingFeatures and self.getSection() is not None and not word.isTempFeature()[
                        self.getSection().getIndex()]:
                        continue
                    copyWord = TermBank.termsBank[word.getLemma()]
                    if word.isCandidateFeature() and copyWord.getFMeasure():
                        wordBag[copyWord.getLemma()] = copyWord
            return wordBag

        words = ph1.getWords() + ph2.getWords()
        for word in words:
            if word.getLemma() in TermBank.wordsBank.keys():
                if usingFeatures and self.getSection() is not None and not word.isTempFeature()[self.getSection().getIndex()]:
                    continue
                copyWord = TermBank.wordsBank[word.getLemma()]
                if copyWord.isCandidateFeature() and copyWord.getFMeasure():
                    wordBag[copyWord.getLemma()] = copyWord
        return wordBag

    def getValue(self,isTempFMeasure, word):
        value = word.getFMeasure()
        if isTempFMeasure:
            value = word.getTempfMeasure()
        return value

    def vectorize(self, bag, secIdx, isTempFMeasure, forTerms=False,forWordsAndTerms=False):

        vector = []

        lemmas = self.getLemmaList()
        if forWordsAndTerms:
            lemmas = []
            for word in self.getTerms() + self.getWords():
                if word.getLemma() in bag.keys() and  word.getLemma()  not in lemmas:
                    lemmas.append(word.getLemma())

        if forTerms:
            lemmas = []
            for term in self.getTerms():
                lemmas.append(term.getLemma())
        for word in bag.values():
            if word.isTerm():
                word = TermBank.termsBank[word.getLemma()]
            else:
                word = TermBank.wordsBank[word.getLemma()]
            if not secIdx:
                fmeasure = max(self.getValue(isTempFMeasure, word).values())
            else:
                fmeasure = self.getValue(isTempFMeasure, word)[secIdx]
            if word.getLemma() in lemmas:
                vector.append(fmeasure)
            else:
                vector.append(0)
        return vector

    def getDis(self, ph1, isTempFMeasure=False, usingFeatures=False, getMaxValue=False, forTerms=False,forWordsAndTerms=False):
        bag = self.getWordBag(ph1, self, usingFeatures,forTerms=forTerms, forWordsAndTerms=forWordsAndTerms)
        v = []
        for ph in [ph1, self]:
            secIdx = False
            if not getMaxValue and ph.getSection() is not None:
                secIdx = ph.getSection().getIndex()
            # else:
            #     for phh in [ph1, self]:
            #         if phh is not ph and phh.getSection() is not None:
            #             secIdx = phh.getSection().getIndex()

            v.append(ph.vectorize(bag, secIdx,isTempFMeasure,forTerms=forTerms,forWordsAndTerms=forWordsAndTerms))
        return spatial.distance.cosine(v[0], v[1])

    def getTermalDistance(self, citingSent):
        """
            This method is sed to calculate the distance between two sentences using the cosine similarity measure
             and the weights of the two sentences' words according to the feature maximiwation on the article.

            :param citingSent: the sentence mentioned in the citance
            :return: the distance between two sentences
        """
        firstVector = []
        secondVector = []
        firstLemmaList = self.getLemmaList()
        secondLemmaList = citingSent.getLemmaList()
        terms = self.getTerms()
        termsLemmas = []
        for term in terms:
            lemma = term.getLemma()
            parts = lemma.split(' ')
            for part in parts:
                termsLemmas.append(part)
        wordTerms = self.getTerms()
        for word in self.getWords():
            if word.getLemma() not in termsLemmas and word.isCandidateFeature():
                wordTerms.append(word)

        for word in wordTerms:
            firstVectorItem = None
            if word.getFMeasure() and self.getSection():
                sectionIndex = self.getSection().getIndex()
                firstVectorItem = word.getFMeasure()[sectionIndex]

            else:
                if not word.isTerm():
                    if TermBank.isInWordBank(word.getLemma()):
                        brotherWord = TermBank.getWordBankItem(word.getLemma())
                        if brotherWord is not None and brotherWord.getFMeasure():
                            firstVectorItem = max(brotherWord.getFMeasure().values())
                elif word.isTerm():
                    if TermBank.isInTermBank(word.getLemma()):
                        brotherWord = TermBank.getTermBankItem(word.getLemma())
                        if brotherWord is not None and brotherWord.getFMeasure():
                            firstVectorItem = max(brotherWord.getFMeasure().values())

            if firstVectorItem is not None:
                firstVector.append(firstVectorItem)

                if word.getLemma() in secondLemmaList:
                    secondVector.append(firstVectorItem)
                else:
                    secondVector.append(0)

        for word in citingSent.getWords():
            if word.isCandidateFeature() and word.getLemma() not in firstLemmaList:
                secondVectorItem = None
                if word.getFMeasure() and self.getSection() is not None:
                    sectionIndex = self.getSection().getIndex()
                    secondVectorItem = word.getFMeasure()[sectionIndex]

                elif TermBank.isInWordBank(word.getLemma()):
                    brotherWord = TermBank.getWordBankItem(word.getLemma())
                    if brotherWord is not None and brotherWord.getFMeasure():
                        secondVectorItem = max(brotherWord.getFMeasure().values())
                if secondVectorItem is not None:
                    secondVector.append(secondVectorItem)
                    firstVector.append(0)

        return spatial.distance.cosine(firstVector, secondVector)

    def getDistance(self, citingSent):
        """
            This method is sed to calculate the distance between two sentences using the cosine similarity measure
             and the weights of the two sentences' words according to the feature maximiwation on the article.

            :param citingSent: the sentence mentioned in the citance
            :return: the distance between two sentences
        """
        firstVector = []
        secondVector = []
        firstLemmaList = self.getLemmaList()
        secondLemmaList = citingSent.getLemmaList()

        for word in self.getWords():

            if not word.isCandidateFeature():
                continue
            firstVectorItem = None
            if word.getFMeasure() and self.getSection():
                sectionIndex = self.getSection().getIndex()
                firstVectorItem = word.getFMeasure()[sectionIndex]

            elif TermBank.isInWordBank(word.getLemma()):
                brotherWord = TermBank.getWordBankItem(word.getLemma())
                if brotherWord is not None and brotherWord.getFMeasure():
                    firstVectorItem = max(brotherWord.getFMeasure().values())

            if firstVectorItem is not None:
                firstVector.append(firstVectorItem)

                if word.getLemma() in secondLemmaList:
                    secondVector.append(firstVectorItem)
                else:
                    secondVector.append(0)

        for word in citingSent.getWords():
            if word.isCandidateFeature() and word.getLemma() not in firstLemmaList:
                secondVectorItem = None
                if word.getFMeasure() and self.getSection() is not None:
                    sectionIndex = self.getSection().getIndex()
                    secondVectorItem = word.getFMeasure()[sectionIndex]

                elif TermBank.isInWordBank(word.getLemma()):
                    brotherWord = TermBank.getWordBankItem(word.getLemma())
                    if brotherWord is not None and brotherWord.getFMeasure():
                        secondVectorItem = max(brotherWord.getFMeasure().values())
                if secondVectorItem is not None:
                    secondVector.append(secondVectorItem)
                    firstVector.append(0)

        return spatial.distance.cosine(firstVector, secondVector)

    def getBinaryDistance(self, citingSent, threshold):
        """
            This method is sed to calculate the distance between two sentences using the cosine similarity measure
             and the weights of the two sentences' words according to the feature maximiwation on the article.

            :param citingSent: the sentence mentioned in the citance
            :param threshold:
        """

        firstVector = []
        secondVector = []
        firstLemmaList = self.getLemmaList()
        secondLemmaList = citingSent.getLemmaList()

        for word in self.getWords():

            if not word.isCandidateFeature():
                continue
            firstVectorItem = None
            if word.getFMeasure() and self.getSection():
                sectionIndex = self.getSection().getIndex()
                if word.getFMeasure()[sectionIndex] > threshold:
                    firstVectorItem = 1

            elif TermBank.isInWordBank(word.getLemma()):
                brotherWord = TermBank.getWordBankItem(word.getLemma())
                if brotherWord is not None and brotherWord.getFMeasure():
                    if max(brotherWord.getFMeasure().values()) > threshold:
                        firstVectorItem = 1

            if firstVectorItem is not None:
                firstVector.append(firstVectorItem)

                if word.getLemma() in secondLemmaList:
                    secondVector.append(firstVectorItem)
                else:
                    secondVector.append(0)

        for word in citingSent.getWords():
            if word.isCandidateFeature() and word.getLemma() not in firstLemmaList:
                secondVectorItem = None
                if word.getFMeasure() and self.getSection() is not None:
                    sectionIndex = self.getSection().getIndex()
                    if word.getFMeasure()[sectionIndex] > threshold:
                        secondVectorItem = 1

                elif TermBank.isInWordBank(word.getLemma()):
                    brotherWord = TermBank.getWordBankItem(word.getLemma())
                    if brotherWord is not None and brotherWord.getFMeasure():
                        if max(brotherWord.getFMeasure().values()) > threshold:
                            secondVectorItem = 1
                if secondVectorItem is not None:
                    secondVector.append(secondVectorItem)
                    firstVector.append(0)
        # print firstVector
        # print secondVector
        # print spatial.distance.cosine(firstVector, secondVector)
        return spatial.distance.cosine(firstVector, secondVector)

    def getNextWord(self, word):
        if not word.isTerm():
            index = self.getWords().index(word)
            if index < self.getWordsNum() - 1:
                return self.getWords()[index + 1]
        return None

    def __str__(self):

        result = '\n'
        sectionIndex = -1
        if self.getSection() is not None:
            sectionIndex = self.getSection().getIndex()
        for word in self.getWords():
            wordFmeasure = 0
            if sectionIndex != -1 and sectionIndex in word.getFMeasure().keys():
                wordFmeasure = word.getFMeasure()[sectionIndex]
            else:
                brotherWord = TermBank.getWordBankItem(word.getLemma())
                if brotherWord is not None and brotherWord.getFMeasure():
                    wordFmeasure = max(brotherWord.getFMeasure().values())

            if word.isFeature():
                result += ' ***' + word.getText() + '*** '
            elif word.isCandidateFeature():
                result += ' **' + word.getText() + '** '
            else:
                result += word.getText() + ' '
            if wordFmeasure != 0:
                result += ' ( ' + str(wordFmeasure) + ' ) '
        return result.encode("utf-8")


# firstVector = [0.1, 0.4, 0.0, 0.0]
# secondVector = [0.1, 0.4, 0.1, 0.0]
# print np.dot(firstVector, secondVector)
# print norm(firstVector)
# print norm(secondVector)
# print spatial.distance.cosine(firstVector, secondVector)
