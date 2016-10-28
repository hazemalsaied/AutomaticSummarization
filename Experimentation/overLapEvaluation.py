from annotation import Annotation
import os
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

class OverLapEvaluation:

    @staticmethod
    def getAnnotationNumbers(offset):

        offset = offset.replace('[', '')
        offset = offset.replace(']', '')
        offset = offset.strip()
        firstList = offset.split(',')
        finalList = []
        for element in firstList:
            element = element.replace('\'', '')
            finalList.append(element)
        return finalList[0:5]

    @staticmethod
    def compareTwoAnnotationLists(goldReferenceOffset, automaticReferenceOffset):


        goldReferenceOffsetList = OverLapEvaluation.getAnnotationNumbers(goldReferenceOffset.referenceOffset)
        automaticReferenceOffsetList = OverLapEvaluation.getAnnotationNumbers(automaticReferenceOffset.referenceOffset)
        return OverLapEvaluation.getEvaluationScore(goldReferenceOffsetList,automaticReferenceOffsetList)

    @staticmethod
    def getEvaluationScore(goldReferenceOffsetList,automaticReferenceOffsetList):
        evaluationResult = 0
        idx = 0
        for num in automaticReferenceOffsetList:
            if num in goldReferenceOffsetList:
                evaluationResult += 500 - idx
            idx += 10
        return evaluationResult

    @staticmethod
    def getAnnotations(annotationPath):
        try:
            annotationFile = open(annotationPath)
            annotations = []
            lines = annotationFile.readlines()
            for line in lines:
                if len(line.split('|')) > 1:
                    annotations.append(Annotation(line, None))
            annotationFile.close()
            return annotations
        except:
            print "getAnnotations Problem" + '\n'
        raise

    autoAnnotationDictionary = None
    goldAnnotationDictionary = None

    @staticmethod
    def getGoldAnnotationByCitanceNum(annos, num):
        if OverLapEvaluation.goldAnnotationDictionary is None:
            OverLapEvaluation.goldAnnotationDictionary = {}
            for ann in annos:
                OverLapEvaluation.goldAnnotationDictionary[ann.citanceNumber] = ann
        if str(num) in OverLapEvaluation.goldAnnotationDictionary.keys():
            return OverLapEvaluation.goldAnnotationDictionary[num]
        return None

    @staticmethod
    def getAutoAnnotationByCitanceNum(annos, num):
        if OverLapEvaluation.autoAnnotationDictionary is None:
            OverLapEvaluation.autoAnnotationDictionary = {}
            for ann in annos:
                OverLapEvaluation.autoAnnotationDictionary[ann.citanceNumber] = ann
        if str(num) in OverLapEvaluation.autoAnnotationDictionary.keys():
            return OverLapEvaluation.autoAnnotationDictionary[num]
        return None



    @staticmethod
    def getDocNameFromAnnFile(annPath):
        annPathCom = annPath.split('/')
        annFileName = annPathCom[len(annPathCom)-1]
        return annFileName.split('.')[0]

    corpusPath = '/Users/hazemalsaied/RA/Corpus/Sci-Summ-Test/'
    goldAnnsFilesDic = {}

    @staticmethod
    def getGoldAnnotatioFilsDic():
        for subdir, dirs, files in os.walk(OverLapEvaluation.corpusPath):
            for directory in dirs:
                annPath = os.path.join(OverLapEvaluation.corpusPath + directory, 'annotation/' + directory + '.annv3.txt')
                anns = OverLapEvaluation.getAnnotations(annPath)
                OverLapEvaluation.goldAnnsFilesDic[directory] = anns
            break

    systems = '/Users/hazemalsaied/RA/Evaluation/OtherSys/'

    @staticmethod
    def compareAnnotations(goldAnnotationPath, autoAnnotationPath):

        #OverLapEvaluation.getGoldAnnotatioFilsDic()

        for subdir, dirs, files in os.walk(OverLapEvaluation.systems):
            for directory in dirs:
                if directory != 'Gold':
                    for runSubdir, runDirs, runFiles in os.walk(os.path.join(OverLapEvaluation.systems, directory)):
                        for runDir in runDirs:
                            for taskSubdir, taskDirs, taskFiles  in os.walk(os.path.join(OverLapEvaluation.systems + directory, runDir)):
                                for taskDir in taskDirs:
                                    if taskDir == 'Task1':
                                        for annSubdir, annDirs, annFiles in os.walk(
                                                os.path.join(OverLapEvaluation.systems + directory, runDir + '/Task1')):


                                            sysPath = os.path.join(OverLapEvaluation.systems + directory, runDir + '/Task1')
                                            print directory
                                            OverLapEvaluation.createSystemXml(sysPath , directory,runDir)



                                            # result = ''
                                            # finalResult = 0
                                            # for articleFile in annFiles:
                                            #     filePath = os.path.join(OverLapEvaluation.systems + directory, runDir + '/Task1/'+ articleFile)
                                            #     fileName = articleFile[:8]
                                            #     if fileName != '.DS_Stor':
                                            #         goldRefOffset = OverLapEvaluation.goldAnnsFilesDic[fileName]
                                            #         autoRefOffset = OverLapEvaluation.getAnnotations(filePath)
                                            #         finalResult += OverLapEvaluation.evaluateAnnotations(goldRefOffset,autoRefOffset)
                                            #
                                            # result += str(finalResult) + ' = ' + directory + ' #' +runDir + '\n'
                                            #
                                            # ff = open(OverLapEvaluation.resultPath, 'a')
                                            # ff.write(result)
                                            # ff.close()
                                            # print result
            break

    resultPath = '/Users/hazemalsaied/RA/Evaluation/TextSpanResult.md'
    @staticmethod
    def evaluateAnnotations(goldRefOffset, autoRefOffset):
        result = ''
        finalResult = 0
        for annIdx in xrange(1, len(goldRefOffset) + 1):
            goldReferenceOffset = OverLapEvaluation.getGoldAnnotationByCitanceNum(goldRefOffset, str(annIdx))

            autoReferenceOffset = OverLapEvaluation.getAutoAnnotationByCitanceNum(autoRefOffset, str(annIdx))
            if goldReferenceOffset is not None and autoReferenceOffset is not None:
                finalResult += OverLapEvaluation.compareTwoAnnotationLists(goldReferenceOffset, autoReferenceOffset)
        return finalResult

    @staticmethod
    def getAnnByCitanceNum(anns, num):
        print num
        for ann in anns:
            if str(ann.citanceNumber) == str(num):
                return ann
        return None



    @staticmethod
    def createSystemXml(articlesPath, sysId, runId):
        top = Element('System', susId = sysId, runId = runId)
        for annSubdir, annDirs, annFiles in os.walk(articlesPath):
            print articlesPath
            for annFile in annFiles:
                print annFile
                if str(annFile).startswith('.DS_Store') :
                    continue
                articleName = annFile[:8]

                articleEle = SubElement(top, 'Article')
                articleEle.set('name', articleName)
                filePath = os.path.join(articlesPath + '/'+annFile)
                goldAnns = OverLapEvaluation.goldAnnsFilesDic[articleName]
                autoAnns = OverLapEvaluation.getAnnotations(filePath)
                for annIdx in xrange(1, len(goldAnns)+1):
                    print annIdx
                    goldReferenceOffset = OverLapEvaluation.getAnnByCitanceNum(goldAnns, str(annIdx))
                    if goldReferenceOffset is not None:
                        annEle = SubElement(articleEle, 'Annotation')
                        annEle.set('citanceNum',goldReferenceOffset.citanceNumber)
                        annEle.set('citation', goldReferenceOffset.citationOffset)
                        annEle.set('goldRef',goldReferenceOffset.referenceOffset)
                        autoReferenceOffset = OverLapEvaluation.getAnnByCitanceNum(autoAnns, str(annIdx))
                        if autoReferenceOffset is not None:
                            autoRef = str(OverLapEvaluation.getAnnotationNumbers(str(autoReferenceOffset.referenceOffset)))
                            annEle.set('autoRef', autoRef)
                            evScore = OverLapEvaluation.getEvaluationScore(OverLapEvaluation.getAnnotationNumbers(goldReferenceOffset.referenceOffset),OverLapEvaluation.getAnnotationNumbers(autoRef))
                            annEle.set('EvalScore', str(evScore))

                        else:
                            annEle.set('autoRef', '')
            break

        path = '/Users/hazemalsaied/RA/Evaluation/XmlBank/' + sysId + '_' + runId + '.xml'
        ff = open(path, 'w')

        ff.write(tostring(top))
        ff.close()



goldPath = '/Users/hazemalsaied/RA/Corpus/Sci-Summ-Test/C00-2123/annotation/C00-2123.annv3.txt'
testPath = '/Users/hazemalsaied/RA/Evaluation/OtherSys/System10/run1_one_line/Task1/C00-2123.annv3.txt'


#OverLapEvaluation.getGoldAnnotatioFilsDic()
#OverLapEvaluation.compareAnnotations(goldPath, testPath)