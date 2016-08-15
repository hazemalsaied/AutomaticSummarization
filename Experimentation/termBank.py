from nltk.stem import WordNetLemmatizer

class TermBank:

    stopWordsList = []
    abstractTerms = []
    wordsBank = {}
    termsBank = {}
    sentenceBank = {}
    titleTerms = []
    wordNetLemmatizer = WordNetLemmatizer()
    sectionsNumber = 0
    hattedFFDForTerms = 0
    hattedFFD = 0

    def __init__(self):

        TermBank.stopWordsList = []
        self.loadStopWords()
        TermBank.abstractTerms = []
        TermBank.wordsBank = {}
        TermBank.termsBank = {}
        TermBank.sentenceBank = {}
        TermBank.titleTerms = []
        TermBank.wordNetLemmatizer = WordNetLemmatizer()
        TermBank.sectionsNumber = 0
        TermBank.hattedFFDForTerms = 0
        TermBank.hattedFFD = 0

    def loadStopWords(self):
        """
            Method for loading the manula stop word list content
        """
        stopsFile = open("/Users/hazemalsaied/git/scisumm-corpus/Experimentation/stopWordsExpanded.txt")
        for line in stopsFile.xreadlines():
            TermBank.stopWordsList.append(line.strip().lower())

    @staticmethod
    def setAbstractTerms(terms):
        TermBank.abstractTerms = terms

    @staticmethod
    def getAbstractTerms():
        return TermBank.abstractTerms

    @staticmethod
    def addAbstractTerm(term):
        TermBank.abstractTerms.append(term)

    @staticmethod
    def addWordBankItem(word):
        if not word.isTerm():
            TermBank.wordsBank[word.getLemma().lower()] = word

    @staticmethod
    def getWordBankItem(wordForm):
        lemma = TermBank.wordNetLemmatizer.lemmatize(wordForm)
        if lemma in TermBank.wordsBank.keys():
            return TermBank.wordsBank[lemma]

    @staticmethod
    def isInWordBank(wordForm):
        lemma = TermBank.wordNetLemmatizer.lemmatize(wordForm).lower()
        if lemma in TermBank.wordsBank.keys():
            return True
        return False

    @staticmethod
    def isInTermBank(wordForm):
        if wordForm in TermBank.termsBank.keys():
            return True
        return False

    @staticmethod
    def getTermBankItem(wordForm):
        if wordForm in TermBank.termsBank.keys():
            return TermBank.wordsBank[wordForm]

    def setTitleTerms(self, terms):
        TermBank.titleTerms = terms

    @staticmethod
    def getTitleTerms():
        return TermBank.titleTerms

    @staticmethod
    def addTitleTerm(term):
        TermBank.titleTerms.append(term)

    @staticmethod
    def getSentenceBank():
        return TermBank.sentenceBank

    @staticmethod
    def getSentenceBankItem(index):
        if index in TermBank.sentenceBank.keys():
            return TermBank.sentenceBank[index]
        return None

    @staticmethod
    def addSentenceBankItem(sent):
        if sent.getIndex() is not None:
            #if TermBank.getSentenceBankItem(sent.getIndex()) is not None:
            #    print '## Warning: sentences with the same index ', sent.getIndex(), ' : ', sent
            TermBank.sentenceBank[sent.getIndex()] = sent

    @staticmethod
    def calculateHattedFFD():
        tempSum = 0.
        for word in TermBank.wordsBank.values():
            tempSum += word.getHatedFF()
        TermBank.hattedFFD = tempSum / len(TermBank.wordsBank)

        for term in TermBank.termsBank.values():
            tempSum += term.getHatedFF()
        TermBank.hattedFFDForTerms = tempSum / len(TermBank.termsBank)
