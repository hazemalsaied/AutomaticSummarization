import re

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.text import Text

from termBank import TermBank


class Section:
    def __init__(self, sectionIndex, sentences, paper):
        self.setSectionIndex(sectionIndex)
        self.__wordBank = {}
        self.__sentences = []
        self.__text = ''
        self.setSentences(sentences)
        self.setPaper(paper)
        self.sectionOccurrences = {}
        self.sectionOccurrencesForTerms = {}

    def addWordBankItem(self, word):
        if not word.isTerm():
            self.__wordBank[word.getLemma().lower()] = word

    def isInWordBank(self, wordForm):
        lemma = TermBank.wordNetLemmatizer.lemmatize(wordForm).lower()
        if lemma in self.__wordBank.keys():
            return True
        return False

    def getWordBankItem(self, wordForm):
        lemma = TermBank.wordNetLemmatizer.lemmatize(wordForm)
        if lemma in self.__wordBank.keys():
            return self.__wordBank[lemma]
        return None

    def getWordBank(self):
        return self.__wordBank

    def getIndex(self):
        return self.__sectionIndex

    def setSectionIndex(self, sectionIndex):
        self.__sectionIndex = sectionIndex

    def getTitle(self):
        return self.__title

    def setTitle(self, name):
        self.__title = name

    def getPaper(self):
        return self.__paper

    def setPaper(self, paper):
        self.__paper = paper

    def setSentences(self, sens):
        self.__sentences = sens

    def getSentences(self):
        return self.__sentences

    def addSentence(self, sentence):
        self.__sentences.append(sentence)

    def getSentencesNum(self):
        return len(self.__sentences)

    def addText(self, text):
        self.__text += text

    def getText(self):
        return self.__text

    def setLemmatizedText(self):
        self.__lemmatizedText = ''
        for sent in self.getSentences():
            for word in sent.getWords():
                # if word.isCandidateFeature():
                self.__lemmatizedText += word.getLemma() + ' '

    def getLemmatizedText(self):
        if self.__lemmatizedText is '':
            self.setLemmatizedText()
        return self.__lemmatizedText

    def getWordOccurence(self, text):
        lemmetedText = ''
        words = word_tokenize(text)
        wordnetLemmatizer = WordNetLemmatizer()
        for word in words:
            lemmetedText += wordnetLemmatizer.lemmatize(word) + ' '
        lemmetedText = lemmetedText[:-1].lower()
        lemmatizedSection = self.getLemmatizedText()

        moby = Text(lemmatizedSection)
        if lemmetedText[-1] == '\\' :
            lemmetedText = lemmetedText[:-1]
        return len(re.findall(lemmetedText, lemmatizedSection))
        # re.findall(r'lemmetedText', sectionlemmatizedText)

    def __str__(self):
        return self.getIndex()  # + self.getTitle()
