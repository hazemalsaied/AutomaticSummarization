import os
import sys
import xml.etree.ElementTree
import xml.etree.ElementTree as ET

from Experimentation.paper import Paper
from Experimentation.sentence import Sentence
from Experimentation.termBank import TermBank
from correction import Corrector
from ducSummarizer import DucSummarizer
from ducSummarizer import WordClassifier


class CommunitySummarizer:
    """
         Responsible of generating the model and peer summaries of the scisumm corpus in cosine similarity
    """

    sourceCorpusPath = '/Users/hazemalsaied/RA/Corpus/Sci-Summ/'
    corpusPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/'
    htmlCorpus = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/SCISUMM-NonBinaryHtml/'
    modelPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/SCISUMM/models/'
    peerPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/systems/'

    @staticmethod
    def createAutodeterminedSummary():

        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)

                sents = DucSummarizer.getSentencesWeights(paper)
                threshold = DucSummarizer.getXMinSentence(sents)

                candidateSents = []
                for sent in sents:
                    if sent.getWeight() > threshold and sent.getWordsNum() > 20:
                        candidateSents.append(sent)
                candidateSents = sorted(candidateSents, key=lambda Sentence: Sentence.getWeight(), reverse=True)
                summary = []
                for sent1 in candidateSents:
                    for sent2 in candidateSents:
                        if sent1 is not sent2:
                            distance = sent1.getDis(sent2)
                            if distance > 0.7:
                                candidateSents.remove(sent2)
                    summary.append(sent1)
                    candidateSents.remove(sent1)
                summary = sorted(summary,key=lambda Sentence: Sentence.getIndex())
                summ = DucSummarizer.generateSummaryText(summary)
                print summ

    @staticmethod
    def createDemonstrativeSummary():

        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)

                sents = DucSummarizer.getSentencesWeights(paper)
                threshold = DucSummarizer.getXMinSentence(sents)

                candidateSents = []
                for sent in sents:
                    if sent.getWeight() > threshold and sent.getWordsNum() > 20:
                        candidateSents.append(sent)
                candidateSents = sorted(candidateSents, key=lambda Sentence: Sentence.getWeight(), reverse=True)

                sentenceCluster = {}
                for sent in candidateSents:
                    if sent.getSection() is not None:
                        secIdx = sent.getSection().getIndex()
                        if secIdx in sentenceCluster.keys():
                            sentenceCluster[secIdx].append(sent)
                        else:
                            sentenceCluster[secIdx] = [sent]
                summary = []
                for key in sentenceCluster.keys():
                    sents = sorted(sentenceCluster[key], key=lambda Sentence: Sentence.getWeight(), reverse=True)
                    for sent1 in sents:
                        for sent2 in sents:
                            if sent1 is not sent2:
                                distance = sent1.getDis(sent2)
                                if distance < 0.5:
                                    sents.remove(sent2)
                        summary.append(sent1)
                        sents.remove(sent1)

                summary = sorted(summary, key=lambda Sentence: Sentence.getIndex())
                summ = DucSummarizer.generateSummaryText(summary)
                print summ

    @staticmethod
    def generatePeerCommunitySummary(getBinarySummaries=False, getMaxValue=False, forTerms=False, forWordsAndTerms=False):
        """
            This method create the mpdel summaries using the cosine similarity approach.
             for each sentence of the citation we search for the most close sentence of the article
        """

        if not os.path.exists(CommunitySummarizer.peerPath):
            os.makedirs(CommunitySummarizer.peerPath)
        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)
                if getBinarySummaries:
                    xMin = DucSummarizer.getXMin(TermBank.wordsBank.values())
                summary = []
                for ann in paper.getAnnotations():
                    if not ann.isValid:
                        print ann.citanceNumber + ' : Not valid annotation'
                        continue
                    for citId, citSent in ann.citingSentencesDictionary.iteritems():
                        Corrector.correctSentence(citSent, paperText)
                        for idx, sent in TermBank.sentenceBank.iteritems():
                            if getBinarySummaries:
                                distance = sent.getBinaryDistance(citSent, xMin)
                            else:
                                distance = sent.getDis(citSent, getMaxValue=getMaxValue,
                                                       forTerms=forTerms,forWordsAndTerms=forWordsAndTerms)  # sent.getDistance(citSent)
                            ann.addSpanResultItem(distance, sent, citSent)
                        sortedSpanResults = sorted(ann.spanResultList,
                                                   key=lambda SpanResultItem: SpanResultItem.distance)
                        for sortedSpanResult in sortedSpanResults:
                            if sortedSpanResult.referenceSent not in summary:
                                summary.append(sortedSpanResult.referenceSent)
                                break
                        DucSummarizer.adjustWeights(sortedSpanResults[0].referenceSent, paper, WordsNumber=5)
                ff = open(os.path.join(CommunitySummarizer.peerPath, documentName + '_summary.md'), 'w+')
                ff.write(DucSummarizer.generateSummaryText(summary))
                ff.close()
            break

    @staticmethod
    def testDIstance(getBinarySummaries=False):
        """
            This method create the mpdel summaries using the cosine similarity approach.
             for each sentence of the citation we search for the most close sentence of the article
        """

        if not os.path.exists(CommunitySummarizer.peerPath):
            os.makedirs(CommunitySummarizer.peerPath)
        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)
                if getBinarySummaries:
                    xMin = DucSummarizer.getXMin(TermBank.wordsBank.values())
                summary = []
                for ann in paper.getAnnotations():
                    if not ann.isValid:
                        print ann.citanceNumber + ' : Not valid annotation'
                        continue
                    for citId, citSent in ann.citingSentencesDictionary.iteritems():
                        Corrector.correctSentence(citSent, paperText)
                        for idx, sent in TermBank.sentenceBank.iteritems():
                            distance = sent.getDis(citSent)
                            ann.addSpanResultItem(distance, sent, citSent)
                        sortedSpanResults = sorted(ann.spanResultList,
                                                   key=lambda SpanResultItem: SpanResultItem.distance)
                        for sortedSpanResult in sortedSpanResults:
                            if sortedSpanResult.referenceSent not in summary:
                                summary.append(sortedSpanResult.referenceSent)
                                break
                                # DucSummarizer.adjustWeights(sortedSpanResults[0].referenceSent, paper, WordsNumber=7)
            break

    @staticmethod
    def generateModelCommunitySummary():
        """
            This method generate the model community summary of SCISUMM corpus and save them
            in the evaluation folder with the respect to the convention of ROUGE
        """
        if not os.path.exists(CommunitySummarizer.modelPath):
            os.makedirs(CommunitySummarizer.modelPath)
        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                communitySummaryPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                    'summary/' + documentName + '.community.xml')
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                summFile = open(communitySummaryPath)
                content = summFile.read()
                root = xml.etree.ElementTree.fromstring("<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>" + content)
                # Generating the summary
                summ = ''
                for sent in root:
                    sumSent = Sentence(sent.text)
                    Corrector.correctSentence(sumSent, paperText)
                    summ += sumSent.getText() + '\n'
                ff = open(os.path.join(CommunitySummarizer.modelPath, documentName + '_model.md'), 'w+')
                ff.write(summ)
                ff.close()
            break

    @staticmethod
    def getInteractiveSummary(paper, paperText):
        """
            for each annotation of the paper, this method add a list of @SpanResultItem, sorted using the its distance.

            :param paper: the article after weighting words and sentences
            :param paperText:
        """
        annotationsReport = ''
        for ann in paper.getAnnotations():
            annotationsReport += '\n' + '#Analysing the annotation ' + ann.citanceNumber + '\n'
            if not ann.isValid:
                annotationsReport += '**Not valid annotation**' + '\n'
                continue
            for citId, citSent in ann.citingSentencesDictionary.iteritems():
                Corrector.correctSentence(citSent, paperText)
                annotationsReport += '\n' + '##The Citing Sentences : ' + '\n' + str(citSent) + '\n'
                annotationsReport += '\n' + '###The Corpus Reference Sentences : ' + '\n'
                for idx, sent in TermBank.sentenceBank.iteritems():
                    distance = sent.getDistance(citSent)
                    ann.addSpanResultItem(distance, sent, citSent)
                for sent in ann.referenceSentences:
                    Corrector.correctSentence(sent, paperText)
                    sent.getFakeWeight(paper)
                    citSent.getFakeWeight(paper)
                    dist = citSent.getDistance(sent)
                    annotationsReport += str(dist) + '\n'
                    annotationsReport += '\n' + '\n' + '**' + str(
                        sent.getIndex()) + '** : ' + str(sent) + '\n' + '\n'
                sortedSpanResults = sorted(ann.spanResultList, key=lambda SpanResultItem: SpanResultItem.distance)
                annotationsReport += '\n' + '###Our Reference Sentences : ' + '\n'
                for spanResult in sortedSpanResults[:5]:
                    annotationsReport += str(spanResult).encode("utf-8") + '\n'
            print annotationsReport

    # TODO just for analyzing the result
    @staticmethod
    def getInteractiveSummary1(paper, paperText):
        """
            In this method we will sort the sentences of citing papers
            sorting processes would be done by using the weights of terms of systems papers
            then we should see the result and search of the annotation result and its neighborhood in this sorted list

            :param paper: the article after weighting words and sentences
            :param paperText:
        """
        annotationsReport = ''
        wordBank = TermBank.wordsBank
        for ann in paper.getAnnotations():
            if not ann.isValid:
                annotationsReport += '**Not valid annotation**' + '\n'
                continue
            annotationsReport += '\n' + '#analysing the annotation ' + str(ann.citanceNumber) + '\n'
            # Loading the citing article
            citingArticlePath = "../data/" + ann.referenceArticle[:-4] + "_TRAIN/Citance_XML/" + ann.citingArticle
            paperText = Corrector.getPaperText(citingArticlePath)
            newCitingArticlePath = Corrector.correct(citingArticlePath, paperText)
            citingPaper = Paper(newCitingArticlePath, False)
            citingPaper.wordsBank = wordBank
            sentList = []
            for section in citingPaper.getSections():
                for sent in section.getSentences():
                    sent.setSection(None)
                    sent.setWeight()
                    # sent.setSection(section)
                    sentList.append(sent)
            sentList = sorted(sentList, key=lambda Sentence: Sentence.getWeight(), reverse=True)
            annotationsReport += '###The citing span:'
            for sent in ann.referenceSentences:
                annotationsReport += str(sent.getIndex())
            annotationsReport += '###The most important sentences of the citing article:'
            for sent in sentList[:10]:
                annotationsReport += str(sent.getIndex()) + ': ' + str(sent.getWeight()) + '\n'
                # print annotationsReport

    @staticmethod
    def getInteractiveSummary2(xmlFilePath):
        """
            This method is the contrary of method 1 which :
            In this method we will sort the sentences of citing papers
            sorting processes would be done by using the weights of terms of systems papers

            then we should see the result and search of the annotation result and its neighborhood in this sorted list


            :param xmlFilePath:
        """
        paperText = Corrector.getPaperText(xmlFilePath)

        # Correcting the encoding problem to enhance the text
        newPaperPath = Corrector.correct(xmlFilePath, paperText)
        # Loading the corrected file
        referencePaper = Paper(newPaperPath, False)

        annotationsReport = ''
        for ann in referencePaper.getAnnotations():
            Paper.wordsBank = {}
            if not ann.isValid:
                annotationsReport += '**Not valid annotation**' + '\n'
                continue
            annotationsReport += '\n' + '#analysing the annotation ' + str(ann.citanceNumber) + '\n'
            # Loading the citing article
            citingArticlePath = "../data/" + ann.referenceArticle[:-4] + "_TRAIN/Citance_XML/" + ann.citingArticle
            paperText = Corrector.getPaperText(citingArticlePath)
            newCitingArticlePath = Corrector.correct(citingArticlePath, paperText)
            citingPaper = Paper(newCitingArticlePath)

            sentList = []
            for section in referencePaper.getSections():
                for sent in section.getSentences():
                    sent.setSection(None)
                    sent.setWeight()
                    sentList.append(sent)
            sentList = sorted(sentList, key=lambda Sentence: Sentence.getWeight(), reverse=True)
            annotationsReport += '###The citing span:' + '\n'
            for sent in ann.referenceSentences:
                annotationsReport += str(sent.getIndex()) + ', '
            annotationsReport += '\n###The most important sentences of the Reference ' \
                                 'article according to the citing Article:\n'
            for sent in sentList[:50]:
                annotationsReport += str(sent.getIndex()) + ': ' + str(sent.getWeight()) + '\n'
            print annotationsReport

    @staticmethod
    def generateCitationReport(xmlFilePath):
        """
            This method is the contrary of method 1 which :
            In this method we will sort the sentences of citing papers
            sorting processes would be done by using the weights of terms of systems papers

            then we should see the result and search of the annotation result and its neighborhood in this sorted list

            :param xmlFilePath:
        """
        paperText = Corrector.getPaperText(xmlFilePath)

        # Correcting the encoding problem to enhance the text
        newPaperPath = Corrector.correct(xmlFilePath, paperText)
        # Loading the corrected file
        referencePaper = Paper(newPaperPath)

        report = ''
        for ann in referencePaper.getAnnotations():
            report += '#Citing:' + ann.citingArticle + ' ' + str(ann.citanceNumber) + '\n'
            report += '###Ref: ' + ann.referenceArticle + '\n'
            report += '##Citing Sentences: \n'
            for sent in ann.citingSentences:
                report += '**' + str(sent.getIndex()) + '** :  '
                for word in sent.getWords():
                    if word.getLemma() in TermBank.wordsBank.keys():
                        report += '**' + word.getText() + '** '
                    else:
                        report += word.getText() + ' '
                report += '\n\n'
            report += '##Reference Sentences: \n'
            for sent in ann.referenceSentences:
                report += '**' + str(sent.getIndex()) + '** :  '
                for word in sent.getWords():
                    report += word.getText() + ' '
                report += '\n\n'
            report += '\n\n\n'
        print report

    @staticmethod
    def detectNonValidAnnotations():
        """
            This method is used for detecting the non valid annotation for each document of the SCISUMM
        """
        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for dir in dirs:
                documentName = dir[:8]
                print documentName
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, dir),
                                                'Reference_XML/' + documentName + '.xml')
                paper = Paper(referenceXmlPath, isDucFile=False, setWeights=False)
                for ann in paper.getAnnotations():
                    if not ann.isValid:
                        print ann.citanceNumber, 'is not valid'
            break

    @staticmethod
    def normailzeSummaries():
        CommunitySummarizer.htmlCorpus = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/6/'
        CommunitySummarizer.peerPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/systems/'
        if not os.path.exists(CommunitySummarizer.htmlCorpus):
            os.makedirs(CommunitySummarizer.htmlCorpus)
            # os.makedirs(CommunitySummarizer.htmlCorpus + 'models')
        if not os.path.exists(CommunitySummarizer.htmlCorpus + 'systems'):
            os.makedirs(CommunitySummarizer.htmlCorpus + 'systems')
        # for root, _, files in os.walk(CommunitySummarizer.modelPath):
        #     for f in files:
        #         CommunitySummarizer.normailzeSummary(f, 'models')
        for root, _, files in os.walk(CommunitySummarizer.peerPath):
            for f in files:
                CommunitySummarizer.normailzeSummary(f, 'systems')

    @staticmethod
    def normailzeGraphSummaries():
        CommunitySummarizer.htmlCorpus = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/3/'
        CommunitySummarizer.peerPath = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/systems3/'
        if not os.path.exists(CommunitySummarizer.htmlCorpus):
            os.makedirs(CommunitySummarizer.htmlCorpus)
            # os.makedirs(CommunitySummarizer.htmlCorpus + 'models')
        if not os.path.exists(CommunitySummarizer.htmlCorpus + 'systems'):
            os.makedirs(CommunitySummarizer.htmlCorpus + 'systems')
        # for root, _, files in os.walk(CommunitySummarizer.modelPath):
        #     for f in files:
        #         CommunitySummarizer.normailzeSummary(f, 'models')
        for root, _, files in os.walk(CommunitySummarizer.peerPath):
            for f in files:
                CommunitySummarizer.normailzeSummary(f, 'systems3')

    @staticmethod
    def normailzeSummary(f, folder):
        if f == '.DS_Store':
            return
        CommunitySummarizer.corpusPath = '/Users/hazemalsaied/RA/Evaluation/GraphSummaries/'
        fullPath = os.path.join(CommunitySummarizer.corpusPath + folder, f)

        fo = open(fullPath, "rw+")
        lines = fo.readlines()
        summary = '<html>\n<head><title>'
        summary += f[:-3]
        summary += '</title> </head>\n<body bgcolor="white">\n'
        idx = 0
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            summary += '<a name="' + str(idx) + '">[' + str(idx) + ']</a> <a href="#' + str(idx) + '" id=' \
                       + str(idx) + '>' + line + '</a>\n'
            idx += 1
        summary = summary[:-1] + '</body>\n</html>\n'

        file = open(CommunitySummarizer.htmlCorpus + folder[:-1] + '/' + f[:-2] + 'html', 'w')
        file.write(summary)
        file.close()

    @staticmethod
    def generateEvalXML():

        root = ET.Element('ROUGE-EVAL')
        root.set('version', '1.55')
        taskDic = []
        CommunitySummarizer.htmlCorpus = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/2/'
        for roots, _, files in os.walk(CommunitySummarizer.htmlCorpus + 'models'):
            for f in files:
                if f.split('_')[0] not in taskDic:
                    taskDic.append(f.split('_')[0])
        idx = 1
        for task in taskDic:
            eval = ET.SubElement(root, 'EVAL')
            eval.set('ID', str(idx))
            peerRoot = ET.SubElement(eval, 'PEER-ROOT')
            peerRoot.text = 'c:/rouge/sci-summ/systems'
            modelRoot = ET.SubElement(eval, 'MODEL-ROOT')
            modelRoot.text = 'c:/rouge/sci-summ/models'
            inputFormat = ET.SubElement(eval, 'INPUT-FORMAT')
            inputFormat.set('TYPE', 'SEE')
            models = ET.SubElement(eval, 'MODELS')
            referenceIdx = 1
            for roooot, _, files in os.walk(CommunitySummarizer.htmlCorpus + 'models'):
                for f in files:
                    if f.startswith(task):
                        reference = ET.SubElement(models, 'M')
                        reference.set('ID', f[1:3] + f[4:8] + str(referenceIdx))
                        reference.text = f
                        referenceIdx += 1

            peers = ET.SubElement(eval, 'PEERS')
            peerIdx = 1
            for rooot, _, files in os.walk(CommunitySummarizer.htmlCorpus + 'systems'):
                for f in files:
                    if f.startswith(task):
                        peer = ET.SubElement(peers, 'P')
                        if f.split('_')[1][:-3] == 'sum':
                            peer.set('ID', '59')
                        else:
                            peer.set('ID', f[1:3] + f[4:8])  # )  # str(peerIdx))
                        peer.text = f
                        peerIdx += 1

            idx += 1
        tree = ET.ElementTree(root)
        tree.write("/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/sci-summ.xml")

    @staticmethod
    def getStatistics():
        """
            This method generate all summary of Duc 2007 files and save them into the evaluation folder

            :param path:  '/Users/hazemalsaied/git/scisumm-corpus/DUC2007/update_corpus/'
            :return:
        """

        for subdir, dirs, files in os.walk(CommunitySummarizer.sourceCorpusPath):
            for directory in dirs:
                documentName = directory[:8]
                referenceXmlPath = os.path.join(os.path.join(CommunitySummarizer.sourceCorpusPath, directory),
                                                'Reference_XML/' + documentName + '.xml')
                paperText = Corrector.getPaperText(referenceXmlPath)
                newPath = Corrector.correct(referenceXmlPath, paperText)
                paper = Paper(newPath, isDucFile=False)
                classifierList = []
                for word in TermBank.wordsBank.values():
                    wordCls = WordClassifier(word.getText(), word.getTotalOccurrence(), word.getOccurrence())
                    classifierList.append(wordCls)

                sortedClassifierList = sorted(classifierList,
                                              key=lambda WordClassifier: WordClassifier.frecuency, reverse=True)

                statistics = 'Word,Frecuency,Frecuency in sections\n'
                for cls in sortedClassifierList[:50]:
                    statistics += cls.wordStr + ',' + str(cls.frecuency) + ',' + str(cls.occurrence.values()).replace(
                        ',',
                        '-').replace(
                        '[', '').replace(']', '') + '\n'

                # Writing the summary to the evaluation folder as a peer summary
                fileName = paper.getPaperName() + '_statistics.csv'
                stPath = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries/Statistics/'
                if not os.path.exists(stPath):
                    os.makedirs(stPath)

                ff = open(stPath + fileName, 'w+')
                ff.write(statistics)
                ff.close()


reload(sys)
sys.setdefaultencoding('utf8')
# CommunitySummarizer.detectNonValidAnnotations()
# CommunitySummarizer.generateModelCommunitySummary()
#CommunitySummarizer.generatePeerCommunitySummary(forWordsAndTerms=True)
CommunitySummarizer.normailzeGraphSummaries()
# CommunitySummarizer.generateEvalXML()
# CommunitySummarizer.getStatistics()

#CommunitySummarizer.createAutodeterminedSummary()
#CommunitySummarizer.createDemonstrativeSummary()
