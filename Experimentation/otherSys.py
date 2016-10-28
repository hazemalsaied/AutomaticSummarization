import os

from RougeNormalisation import RougeNormalisation
from overLapEvaluation import OverLapEvaluation


class OtherSys:
    @staticmethod
    def generateSummaries():

        for subdir, dirs, files in os.walk(OverLapEvaluation.systems):
            for directory in dirs:
                if directory != 'Gold':
                    for runSubdir, runDirs, runFiles in os.walk(os.path.join(OverLapEvaluation.systems, directory)):
                        for runDir in runDirs:
                            for taskSubdir, taskDirs, taskFiles in os.walk(
                                    os.path.join(OverLapEvaluation.systems + directory, runDir)):
                                for taskDir in taskDirs:
                                    if taskDir == 'Task1':
                                        for annSubdir, annDirs, annFiles in os.walk(
                                                os.path.join(OverLapEvaluation.systems + directory, runDir + '/Task1')):
                                            sysPath = os.path.join(OverLapEvaluation.systems + directory,
                                                                   runDir + '/Task1')
                                            OtherSys.generateSummary(sysPath, directory, runDir)
            break

    resultPath = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummaries/'

    @staticmethod
    def generateSummary(articlesPath, sysId, runId):

        if not os.path.exists(OtherSys.resultPath):
            os.makedirs(OtherSys.resultPath)

        for annSubdir, annDirs, annFiles in os.walk(articlesPath):
            for annFile in annFiles:
                if str(annFile).startswith('.DS_Store'):
                    continue
                articleName = annFile[:8]
                print articleName
                filePath = os.path.join(articlesPath + '/' + annFile)

                goldAnns = OverLapEvaluation.goldAnnsFilesDic[articleName]
                autoAnns = OverLapEvaluation.getAnnotations(filePath)
                summarySents = []
                for autoAnn in autoAnns:
                    annIdx = autoAnn.citanceNumber
                    print '@', annIdx
                    goldAnn = OverLapEvaluation.getAnnByCitanceNum(goldAnns, str(annIdx))
                    if goldAnn is None:
                        continue
                    sentNum = len(OverLapEvaluation.getAnnotationNumbers(goldAnn.referenceOffset))
                    if autoAnn is not None and autoAnn.getReferenceSentences() is not None:
                        summarySents.extend(autoAnn.getReferenceSentences()[:sentNum])
                summary = OtherSys.generateSummaryText(summarySents)
                folderPath = OtherSys.resultPath + sysId + '_' + runId + '/'
                if not os.path.exists(folderPath):
                    os.makedirs(folderPath)
                path = folderPath + articleName + '_sum.md'
                ff = open(path, 'w')

                ff.write(summary.encode('utf-8').strip())
                ff.close()
            break

    @staticmethod
    def generateSummaryText(summarySents):
        """
            Generate a 100 word summary given a list of sentence objects selected according to the summarization method

            :param summarySents: a list of sentence objects selected according to the summarization method
            :return: the summary as a block of text
        """
        summarySents = sorted(summarySents,
                              key=lambda Sentence: Sentence.getIndex())
        summaryText = ''
        for sent in summarySents:
            if sent.getText().rstrip():
                summaryText += sent.getText() + '\n'
        return summaryText

    readingSumariesPath = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummaries/'
    writinSumariesPath = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummariesHtml/'

    @staticmethod
    def generateHtmlSummaries():

        for subdir, dirs, files in os.walk(OtherSys.readingSumariesPath):
            for sysDir in dirs:
                RougeNormalisation.normailzeGraphSummaries(os.path.join(
                    OtherSys.readingSumariesPath,
                    sysDir), os.path.join(OtherSys.writinSumariesPath,sysDir))
            break
OtherSys.generateHtmlSummaries()
#GenerateOtherSystemsSummaries.generateSummaries()
