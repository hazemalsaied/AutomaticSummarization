import re
import xml.etree.ElementTree
import xml.etree.ElementTree
import xml.etree.cElementTree as ET

import editdistance
import enchant
from nltk import word_tokenize


class Corrector:
    """
        :Note for resolving the import issue, you have to install the Lib, for more information:
         http://pythonhosted.org/pyenchant/tutorial.html#installing-the-package
         you could need install dictionaries, if your systems doesn't contain any generic dictionary used by enchant
    """
    stopWordsList = []

    @staticmethod
    def getPaperText(paperPath):
        paperFile = open(paperPath)
        content = paperFile.read()
        root = xml.etree.ElementTree.fromstring("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>" + content)
        # Storing the text of the article for using it as a corpus, for getting the occurence of each
        # suggestion of the distorted words
        paperText = ''
        for element in root.iter():
            if element.text is not None:
                paperText += element.text + ' '

        return paperText

    @staticmethod
    def loadStopWords():
        """
            Method for loading the manula stop word list content
        """
        stopsFile = open("/Users/hazemalsaied/RA/Experimentation/stopWordsExpanded.txt")
        for line in stopsFile.xreadlines():
            Corrector.stopWordsList.append(line.strip().lower())

    @staticmethod
    def correctSentence(sentence, paperText):
        """
            This method is used for correcting the Sentence Object.
            it's kind of adapted version of the general method correct.
            it is used for correcting the sentences of annotations.

            :param sentence: The sentence we should correct
            :param paperText: the paper as a block of text for using it as a corpus in maxarg procesure
            while generating the suggestions and theirprobabilities.
        """
        enDictionary = enchant.Dict("en_US")
        newSenteceText = ''
        words = word_tokenize(sentence.getText())
        for word in sentence.getWords():

            if Corrector.shouldCorrect(word.getText(), words):
                # Divided word situation, ex. struct -ure
                nextWord = sentence.getNextWord(word)
                if nextWord is not None and not enDictionary.check(
                        nextWord.getText()):
                    composedWord = word.getText() + nextWord.getText()
                    if enDictionary.check(composedWord):
                        sentence.getWords().remove(nextWord)
                        word.setText(composedWord)
                elif len(enDictionary.suggest(word.getText())) > 0:
                    newWord = Corrector.getBestSuggestion(word.getText(), enDictionary.suggest(word.getText()),
                                                          paperText)
                    word.setText(newWord)
            newSenteceText += word.getText() + ' '
        sentence.setText(newSenteceText)

    @staticmethod
    def shouldCorrect(word, words):
        """
            Checking according to a couple of conditions if we shoulf use the correction or not
            :param word:
            :return:
        """
        wordIndex = words.index(word)
        enDictionary = enchant.Dict("en_US")
        if not enDictionary.check(word) and (word.lower() not in Corrector.stopWordsList) \
                and len(word) > 3 and ((wordIndex == 0 and word.lower()[1:] == word[1:]) or (
                wordIndex != 0 and word.lower() == word)) and '-' not in word:
            return True
        return False

    @staticmethod
    def getBestSuggestion(originalWord, words, paperText):
        # Situations like node1, feature4
        if Corrector.contanDijit(originalWord):
            return Corrector.correctDigitedWords(originalWord)
        # situations where the first suggestion is very close but not very common, ubstructure : substructure and
        # structure exist in suggestions but strucuture is very common, so we increase the probablility of substructure
        if editdistance.eval(originalWord, words[0]) < 3 and len(re.findall(words[0], paperText)) > 0:
            return words[0]
        # Other cases
        return Corrector.maximizeProbabilities(originalWord, words, paperText)

    @staticmethod
    def maximizeProbabilities(originalWord, words, paperText):
        bestOccurrence = 0
        result = ''
        for word in words:
            occurences = len(re.findall(word, paperText))
            if occurences > bestOccurrence:
                result = word
                bestOccurrence = occurences
            elif occurences == bestOccurrence:
                if editdistance.eval(originalWord, result) > editdistance.eval(originalWord, word):
                    result = word
        return result

    @staticmethod
    def contanDijit(word):
        if any(ch.isdigit() for ch in word):
            return True
        return False

    @staticmethod
    def correctDigitedWords(word):
        result = ''
        for ch in word:
            if ch.isdigit():
                result += ' ' + ch
            else:
                result += ch
        return result

    @staticmethod
    def correct(paperPath, paperText):
        """
            this method try to increase the quality of the article before processing it.
            we try to group the devised words such as feat ure.
            and for the words who doesn't exist in the dictionary, we take the suggestions of the suitable words and
            claculate the distance between the word and its alternatives. if the distance is less than 3 then
            we accept the suggestion.

            :param paperPath: the path of the paper.
            :return: the path of the new file.

        """
        Corrector.loadStopWords()
        paperFile = open(paperPath)
        content = paperFile.read()
        root = xml.etree.ElementTree.fromstring("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>" + content)
        enDictionary = enchant.Dict("en_US")
        mdText = ''
        sectionIndex = 0
        notIndictionary = 0
        for section in root:
            mdSection = '## section ' + str(sectionIndex) + '\n'
            sectionIndex += 1
            for sentence in section:
                sentenceWords = word_tokenize(sentence.text)
                newSenteceText = ''
                mdSentence = ''
                isComposedWord = False
                for word in sentenceWords:
                    mdWord = word
                    if not isComposedWord:
                        if Corrector.shouldCorrect(word, sentenceWords):
                            wordIndex = sentenceWords.index(word)

                            if not enDictionary.check(word):
                                notIndictionary += 1

                            # Divided word situation, ex. struct -ure
                            if (wordIndex < (len(sentenceWords) - 1)) and not enDictionary.check(
                                    sentenceWords[wordIndex + 1]):
                                composedWord = word + sentenceWords[wordIndex + 1]
                                if enDictionary.check(composedWord):
                                    mdWord = '***' + composedWord + '***( ' + word + ' ' + sentenceWords[
                                        wordIndex + 1] + ')'
                                    word = composedWord
                                isComposedWord = True
                            if len(enDictionary.suggest(word)) > 0:
                                newWord = Corrector.getBestSuggestion(word, enDictionary.suggest(word), paperText)
                                mdWord = '**' + newWord + '**( ' + word + ' )'
                                word = newWord
                        newSenteceText += word + ' '
                        mdSentence += mdWord + ' '

                    else:
                        isComposedWord = False
                sentence.text = newSenteceText
                mdSection += mdSentence + '\n\n'
            mdText += mdSection + '\n\n\n\n\n\n'
        mdText = '#Correction of ' + str(notIndictionary) + ' unrecognized words\n' + mdText
        tree = ET.ElementTree(root)
        newPath = paperPath[:-4] + "-correction.xml"
        tree.write(newPath)
        # print mdText
        return newPath