import sys
import xml.etree.ElementTree
import xml.etree.ElementTree

from sentence import Sentence
from spanResult import SpanResultItem


class Annotation:
    """
        This class is used to encapsulate all needed features of article annotations
         Every object of this class represent a line of the annotation file
    """

    def __init__(self, annotationText, paper):
        self.query = []
        self.spanResultList = []
        self.isValid = True
        annotations = annotationText.split('|')
        self.citingSentences = []
        self.citingSentencesDictionary = {}
        self.referenceSentences = []
        self.referenceSentencesDictionary = {}

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
            title = annList[0].strip()
            if title == 'Citance Number':
                self.citanceNumber = content
            elif title == 'Reference Article':
                self.referenceArticle = content
            elif title == 'Citing Article':
                self.citingArticle = content
            elif title == 'Citation Marker':
                self.citationMarker = content
            elif title == 'Citation Text':
                self.citationText = content
            elif title == 'Reference Text':
                self.referenceText = content
            elif title == 'Discourse Facet':
                self.discourseFacet = content
        self.getCitingSentences()
        #self.maximizeContext(paper)
        self.getReferenceSentences()

        # def getNeighborSentences(self, paper):
        # TODO: add the implemmentation
        # sents = self.getCitingSentences()
        # citingPaperPath = self.getCitingPaperPath()

    def getCitingPaperPath(self, paper):
        if paper is not None and paper.getPaperName() is not None and self.citingArticle is not None:
            return '../data/' + paper.getPaperName() + '/citance_XML/' + self.citingArticle
        return None

    def addSpanResultItem(self, distance, sent, citingSent):
        self.spanResultList.append(SpanResultItem(distance, sent, citingSent))

    def maximizeContext(self, paper):
        path = self.getCitingPaperPath(paper)
        if path is None:
            return
        try:
            citingArticle = open(path)
            content = citingArticle.read()
            self.root = xml.etree.ElementTree.fromstring("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>" + content)
            self.context = []
            contextRangeStart = 0
            if self.citingSentences is None or len(self.citingSentences) == 0 or self.citingSentences[
                0].getIndex() is None:
                print "```" + "Context Maximisation Error:  couldn't capture sentence index." + "```" + '\n\n' + "```" + path + "```" + '\n'
                return
            if self.citingSentences[0].getIndex() > 2:
                contextRangeStart = self.citingSentences[0].getIndex() - 3

            contextRangeEnd = self.citingSentences[len(self.citingSentences) - 1].getIndex() + 3
            contextRange = xrange(contextRangeStart, contextRangeEnd)

            for child in self.root:
                for item in child:
                    if item.tag == 'S' and int(item.attrib['sid']) in contextRange:
                        sentence = Sentence(item.text)
                        sentence.setIndex(int(item.attrib['sid']))
                        if sentence is not None:
                            self.context.append(sentence)
                            self.citingSentencesDictionary[sentence.getIndex()] = sentence
                            # self.citingSentences = self.context

        except:
            print "```" + "Context Maximisation Error:  " + str(
                sys.exc_info()[0]) + "```" + '\n\n' + "```" + path + "```"
            raise

    def getCitingSentences(self):
        if len(self.citingSentences) > 0:
            return self.citingSentences
        try:
            self.root = xml.etree.ElementTree.fromstring(
                "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><citance>" + self.citationText + '</citance>')
        except:
            self.isValid = False
            return
        for child in self.root:
            sentence = Sentence(child.text)
            sentence.setIndex(int(child.attrib['sid']))
            self.citingSentences.append(sentence)
            self.citingSentencesDictionary[int(child.attrib['sid'])] = sentence
        return self.citingSentences

    def getReferenceSentences(self):
        if len(self.referenceSentences) > 0:
            return self.referenceSentences
        try:
            self.root = xml.etree.ElementTree.fromstring(
                "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><citance>" + self.referenceText + '</citance>')
        except:
            self.isValid = False
            return
        for child in self.root:
            sentence = Sentence(child.text)
            sentence.setIndex(int(child.attrib['sid']))
            self.referenceSentences.append(sentence)
            self.referenceSentencesDictionary[int(child.attrib['sid'])] = sentence
        return self.referenceSentences
