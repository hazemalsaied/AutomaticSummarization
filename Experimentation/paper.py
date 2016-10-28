"""
    Created on Mar 31, 2016
    @author: dugue, Al Saied
"""
import sys
import xml.etree.ElementTree
import xml.etree.cElementTree as ET

from nltk import pos_tag
from nltk import word_tokenize

from annotation import Annotation
from section import Section
from sentence import Sentence
from termBank import TermBank
from word import Word


class Paper:
    """
        This class is instanciated for creating an object which contains references to wordsn sentences ans sections.

    """
    def __init__(self, paperPath, setWeights=True, isDucFile=False,doubleSection=False):
        """
            this constructor create objects to encapsulate all the elements of the xml file.
            :param paperPath: the path of the xml format of the article
        """
        termBank = TermBank()
        try:
            paperFile = open(paperPath)
            self.setPaperPath(paperPath)

            content = paperFile.read()
            # Trying to parse the xml into hierarchy of objects.
            self.__title = None
            self.__sections = []
            self.__abstractSentences = []
            sectionIndex = 0
        except:
            raise
        if isDucFile:
            self.root = xml.etree.ElementTree.fromstring(content)
            self.__paperName = self.root.get("name")
            sentenceIdx = 0
            fakeSectionIdx = 0
            for doc in self.root:
                if doubleSection:
                    if sectionIndex % 2 == 0:
                        section = Section(fakeSectionIdx, [], self)
                        fakeSectionIdx += 1
                        self.addSection(section)
                elif not doubleSection:
                    section = Section(sectionIndex, [], self)
                    self.addSection(section)
                for line in doc:
                    sentence = Sentence(line.text, sentenceIdx, section, False)
                    sentenceIdx += 1
                    section.addSentence(sentence)
                section.setTitle(doc.get("name"))

                section.setLemmatizedText()
                sectionIndex += 1
            if doubleSection:
                TermBank.sectionsNumber = fakeSectionIdx
            else:
                TermBank.sectionsNumber = sectionIndex
        else:
            self.setPaperName(paperPath)
            self.setAnnotations(paperPath)
            self.root = xml.etree.ElementTree.fromstring("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>" + content)
            # Openning the xml file

            # Initialising he lemmatizer which will be used for getting wordform lemmas
            # wordBank and sentence bank are dictionary used to store a unique object of each word and sentence of the paper

            # Iteration over the first level elements of the xml
            for child in self.root:
                if child.tag.lower() == 'abstract':
                    # Iteration over the second level elements of the xml
                    for item in child:
                        self.addAbstractSentence(Sentence(item.text, item.attrib['sid'], None, True))
                    # Storing the important words of the abstract
                    self.addAbstractTerms()
                # Iteration over the first level elements of the xml, of the type section
                elif child.tag.lower() == 'section' and len(child) > 0:
                    section = Section(sectionIndex, [], self)
                    # Iteration over the second level elements of the xml, of the type sentence
                    for item in child:
                        sentence = Sentence(item.text, int(item.attrib['sid']), section, False)
                        section.addSentence(sentence)
                    section.setTitle(child.get("title"))
                    self.addSection(section)
                    # Storing the section content, words, as a list of lemma in lower case.
                    section.setLemmatizedText()
                    # Storing the important words of sections' titles
                    self.addTitleTerms(section.getTitle())
                    sectionIndex += 1
                # Adding the title of the paper.
                elif child.tag.lower() == 's':
                    self.setTitle(Sentence(child.text))
                    self.getTitle().setIndex(int(child.attrib['sid']))
                    for word in self.getTitle().getWords():
                        if word.isCandidateFeature():
                            word.addSentence(self.getTitle(), True)
                            TermBank.wordsBank[word.getLemma().lower()] = word
                            TermBank.titleTerms.append(word)
                    for term in self.getTitle().getTerms():
                        term.addSentence(self.getTitle(), True)
                        TermBank.termsBank[term.getLemma().lower()] = term
                    if setWeights:
                        TermBank.addSentenceBankItem(self.getTitle())
                    self.addTitleTerms(self.getTitle())
                    for word in self.getTitle().getWords():
                        if word.isCandidateFeature():
                            TermBank.addWordBankItem(word)
            TermBank.sectionsNumber = sectionIndex
            # this method calculate the f-measure and other weights.
        if setWeights:
            self.setPaperWeights()
            self.setFeatures()

    def setFeatures(self):
        for word in TermBank.wordsBank.values():
            for secIdx in xrange(0,TermBank.sectionsNumber):
                fMeasuree = word.getFMeasure()[secIdx]
                word.setAsFeature(secIdx, False)
                if fMeasuree >= word.getHatedFF() and fMeasuree >= TermBank.hattedFFD:
                    word.setAsFeature(secIdx,True)

    def setTempFeatures(self):
        for word in TermBank.wordsBank.values():
            for secIdx in xrange(0, TermBank.sectionsNumber):
                tempfMeasuree = word.getTempfMeasure()[secIdx]
                word.setAsTempFeature(secIdx, False)
                if tempfMeasuree >= word.getHatedFF() and tempfMeasuree >= TermBank.hattedFFD:
                    word.setAsTempFeature(secIdx, True)

    def setPaperWeights(self):

        # Creating F-measure values for article words
        self.claculateFmeasure()
        # Calculating the threshold of FFD for determining whether a word is a feature or not
        TermBank.calculateHattedFFD()
        # Determining whether a word is a feature or not
        PertinentWordsCounter = self.calucuatePertinency()
        # Printing the result
        #TODO self.printPertinencyReport(PertinentWordsCounter)

        # for term in TermBank.termsBank.values():
        #     print term.getText()
        # print 'f'

    def claculateFmeasure(self):

        for term in TermBank.termsBank.values():
            term.calculateOccurrence(self.getSections())

        for word in TermBank.wordsBank.values():
            word.calculateOccurrence(self.getSections())

        for word in TermBank.wordsBank.values():
            if word.isCandidateFeature():
                word.calculateFMeasure(self.getSections())

        for term in TermBank.termsBank.values():
            term.calculateFMeasure(self.getSections(), True)

    def calucuatePertinency(self):
        PertinentWordsCounter = 0
        for word in TermBank.wordsBank.values():
            for secIdx in xrange(0, TermBank.sectionsNumber):
                fMeasuree = word.getFMeasure()[secIdx]
                if fMeasuree >= word.getHatedFF() and fMeasuree >= TermBank.hattedFFD:
                    PertinentWordsCounter += 1
                    word.updataPertinencyMap(secIdx)

        PertinentTermsCounter = 0
        for term in TermBank.termsBank.values():
            for secIdx in xrange(0, TermBank.sectionsNumber):
                fMeasuree = term.getFMeasure()[secIdx]
                if fMeasuree >= term.getHatedFF() and fMeasuree >= TermBank.hattedFFDForTerms:
                    PertinentTermsCounter += 1
                    term.updataPertinencyMap(secIdx)

        return str(PertinentWordsCounter) + '/' + str(PertinentTermsCounter)

    def printPertinencyReport(self, PertinentWordsCounter):

        print '#' + PertinentWordsCounter + ' Pertinent Words/Terms: '
        for secIdx in xrange(0, TermBank.sectionsNumber):
            print "\n" + '##Section  ' + str(secIdx) + ":\n"
            counter = 0
            for word in TermBank.wordsBank.values():
                if word.getPertinencyReport(secIdx) != '':
                    print str(counter) + '- ' + word.getPertinencyReport(secIdx)
                    counter += 1
        counter = 0
        for secIdx in xrange(0, TermBank.sectionsNumber):
            print "\n" + '##Section  ' + str(secIdx) + ":\n"
            for term in TermBank.termsBank.values():
                if term.getPertinencyReport(secIdx) != '':
                    print str(counter) + '- ' + term.getPertinencyReport(secIdx)
                    counter += 1

    def addAbstractTerms(self):
        """
            method for Storing the important words of the abstract.
        """
        for sentence in self.getAbstract():
            wordList = word_tokenize(sentence.getText())
            # We use post tagging for over-weighting the abstract terms who are nous
            wordListTagged = pos_tag(wordList)
            for word in sentence.getWords():
                for postTag in wordListTagged:
                    if postTag[0].lower() == word.getText().lower() and postTag[1].startswith('NN'):
                        if word.isCandidateFeature() and not word.exist(TermBank.getAbstractTerms()):
                            TermBank.addAbstractTerm(word)

    def addTitleTerms(self, wordsStr):
        """
            method for Storing the important words of titles.
        """
        if wordsStr is not str:
            return
        wordList = word_tokenize(wordsStr)
        # For avoiding the ordinary words, introduction conclusions ..
        for wordForm in wordList:
            word = Word(wordForm, None, wordList.index(wordForm), None)
            if word.isCandidateFeature() and not word.exist(TermBank.getTitleTerms()):
                TermBank.titleTerms.append(word)

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setAnnotations(self, paperPath):
        """
            THis method try to read the annotation files of each document of the corpus.
            for each citing paper it store the required data inside @Annotation object

            :param paperPath: the path of the paper
        """
        annPathList = self.getPaperName().split('_')
        annotationPath = '/Users/hazemalsaied/RA/Corpus/Sci-Summ-Test/' + self.getPaperName() + '/annotation/' + annPathList[0] + '.annv3.txt'
        try:
            annotationFile = open(annotationPath)
            self.__annotationPath = annotationPath
            self.__annotations = []
            lines = annotationFile.readlines()
            # self.createAnnotationXML(lines)
            for line in lines:
                if len(line.split('|')) > 1:
                    self.__annotations.append(Annotation(line, self))
            annotationFile.close()
        except IOError as e:
            print "```" + "I/O error({0}): {1}".format(e.errno,
                                                       e.strerror) + "```" + '\n' + "```" + annotationPath + "```" + '\n'
        except:
            print "```" + "Annotation Reading Error:  " + str(
                sys.exc_info()[0]) + "```" + '\n' + "```" + annotationPath + "```" + '\n'
            raise

    def createAnnotationXML(self, lines):

        root = ET.Element("root")
        for line in lines:
            if len(line.split('|')) > 1:
                citance = ET.SubElement(root, "Citance")
                annotations = line.split('|')
                self.citingSentences = []
                self.citingSentencesDictionary = {}
                for ann in annotations:
                    annList = ann.split(':')
                    if len(annList) <= 1:
                        continue
                    content = ''
                    if len(annList) > 2:
                        for i in xrange(1, len(annList)):
                            content += annList[i]
                    else:
                        content = annList[1].strip()
                    content = str(content)
                    title = annList[0].strip().replace(' ', '_')
                    if 'citation text' in annList[0].lower() or 'systems text' in annList[0].lower():
                        try:
                            citationTextSents = xml.etree.ElementTree.fromstring('<Sents>' + content + '</Sents>')
                            citationText = ET.SubElement(citance, title)
                            for item in citationTextSents.getchildren():
                                sent = ET.SubElement(citationText, item.tag)
                                sent.text = item.text
                                sent.attrib = item.attrib
                        except:
                            print "Unexpected error:", sys.exc_info()[0]
                    else:
                        ET.SubElement(citance, title).text = content
        tree = ET.ElementTree(root)
        tree.write('../Corpus/Sci-Summ/' + self.getPaperName() + '/annotation/xml' + self.getPaperName() + '.xml')

    def getAnnotations(self):
        """
            Return a list of annotation objects which contain information about the systems paper and the citing papers
        """
        return self.__annotations

    def setAbstract(self, sentences):
        self.__abstractSentences = sentences

    def getAbstract(self):
        return self.__abstractSentences

    def setPaperName(self, path):
        """
            Storing the name of the document , ex 'C90_2093_TRAIN'

            :param path: the path of the paper
        """
        self.__paperName = ''
        getName = False
        pathlist = path.split('/')
        for item in pathlist:
            if getName:
                self.__paperName = item
                break
            if item == 'Sci-Summ-Test':
                getName = True

    def getPaperName(self):
        """
            :return: The name of the paper, ex 'C90_2093_TRAIN'
        """
        return self.__paperName

    def addAbstractSentence(self, sent):
        self.__abstractSentences.append(sent)

    def setPaperPath(self, path):
        self.__paperPath = path

    def getPaperPath(self):
        return self.__paperPath

    def setSections(self, secs):
        self.__sections = secs

    def getSections(self):
        return self.__sections

    def getSectionsNum(self):
        return len(self.__sections)

    def addSection(self, section):
        self.__sections.append(section)

        return None

    def getMaxWeight(self, lemma):
        if lemma in TermBank.wordsBank:
            word = TermBank.wordsBank[lemma]
            return word.getMaxWeight()
        return 0
