import os, xml
import shutil
import xml.etree.ElementTree as ET
from correction import Corrector
from sentence import Sentence

class RougeNormalisation:
    @staticmethod
    def normailzeGraphSummaries(readingFolder, writingFolder):

        if not os.path.exists(writingFolder):
            os.makedirs(writingFolder)

        for root, _, files in os.walk(readingFolder):
            for fileName in files:
                RougeNormalisation.normailzeSummary(fileName, readingFolder, writingFolder)

    @staticmethod
    def normailzeSummary(fileName, readingFolderPath, writingFolderPath):

        if fileName == '.DS_Store':
            return

        fo = open(os.path.join(readingFolderPath, fileName), "rw+")
        lines = fo.readlines()
        summary = '<html>\n<head><title>'
        summary += fileName[:-3]
        summary += '</title> </head>\n<body bgcolor="white">\n'
        idx = 0
        for line in lines:
            if line == '\n':
                continue
            if line.endswith('\n'):
                line = line[:-1]
            summary += '<a name="' + str(idx) + '">[' + str(idx) + ']</a> <a href="#' + str(idx) + '" id=' \
                       + str(idx) + '>' + line + '</a>\n'
            idx += 1
        summary = summary[:-1] + '</body>\n</html>\n'

        file = open(os.path.join(writingFolderPath, fileName[:-2] + 'html'), 'w')
        file.write(summary)
        file.close()


    @staticmethod
    def renamePeerSummaries(readingFolder,writingFolder):

        if not os.path.exists(writingFolder):
            os.makedirs(writingFolder)

        for root, dirs, files in os.walk(readingFolder):
            for dir in dirs:
                if dir == 'all' or dir == 'models':
                    continue
                for sysRoot, sysDirs, sysfiles in os.walk(os.path.join(readingFolder,dir)):
                    for summary in sysfiles:
                        readingFile = os.path.join(os.path.join(readingFolder, dir), summary)
                        writingFile = os.path.join(writingFolder, dir + '#'+ summary )
                        shutil.copyfile(readingFile,writingFile)

    @staticmethod
    def generateEvalXML(readingFolder,writingFolder ):

        if not os.path.exists(writingFolder):
            os.makedirs(writingFolder)

        taskDic = []

        for root, dirs, files in os.walk(os.path.join(readingFolder, 'models')):
            for f in files:
                if f.split('_')[0] not in taskDic:
                    taskDic.append(f.split('_')[0])

        for root, dirs, files in os.walk(readingFolder):
            for dir in dirs:
                if dir == 'models':
                    continue
                root = ET.Element('ROUGE-EVAL')
                root.set('version', '1.55')

                idx = 1
                for task in taskDic:
                    eval = ET.SubElement(root, 'EVAL')
                    eval.set('ID', str(idx))
                    peerRoot = ET.SubElement(eval, 'PEER-ROOT')
                    peerRoot.text = 'c:/rouge/OtherSysSummariesHtml/' + dir
                    modelRoot = ET.SubElement(eval, 'MODEL-ROOT')
                    modelRoot.text = 'c:/rouge/OtherSysSummariesHtml/models'
                    inputFormat = ET.SubElement(eval, 'INPUT-FORMAT')
                    inputFormat.set('TYPE', 'SEE')
                    models = ET.SubElement(eval, 'MODELS')
                    referenceIdx = 1
                    for roooot, _, files in os.walk(os.path.join(readingFolder, 'models')):
                        for f in files:
                            if f.startswith(task):
                                reference = ET.SubElement(models, 'M')
                                reference.set('ID', f[1:3] + f[4:8] + str(referenceIdx))
                                reference.text = f
                                referenceIdx += 1

                    peers = ET.SubElement(eval, 'PEERS')
                    peerIdx = 1
                    for rooot, _, files in os.walk(os.path.join(readingFolder, dir)):
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
                tree.write(os.path.join(writingFolder, dir+ '.xml'))



    @staticmethod
    def generateModelSummary(readingFolder, writingFolder):
        """
            This method generate the model community summary of SCISUMM corpus and save them
            in the evaluation folder with the respect to the convention of ROUGE
        """
        if not os.path.exists(writingFolder):
            os.makedirs(writingFolder)
        for subdir, dirs, files in os.walk(readingFolder):
            for directory in dirs:
                documentName = directory[:8]
                communitySummaryPath = os.path.join(os.path.join(readingFolder, directory),'summary/' + documentName + '.community.txt')
                summFile = open(communitySummaryPath)
                content = summFile.readlines()
                summ = ''
                for line in content:
                    line = line.replace('</S>', '')
                    line = line.replace('<S sid ="', '')
                    line = line.replace('" ssid = "', '')
                    if '">' in line:
                        line = line.replace('">', '##')
                        line = line.split('##')[1]
                    summ += line + '\n'
                ff = open(os.path.join(writingFolder, documentName + '_model.md'), 'w+')
                ff.write(summ)
                ff.close()
            break

#readingFolder = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummariesHtml'
#writingFolder = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummariesHtml/all'
#RougeNormalisation.renamePeerSummaries(readingFolder, writingFolder)

#readingFolder = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummaries/models'
#writingFolder = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummariesHtml/models'
#RougeNormalisation.normailzeGraphSummaries(readingFolder,writingFolder)

#writingFolder = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummaries/models'
#readingFolder = '/Users/hazemalsaied/RA/Corpus/Sci-Summ-Test/'
#RougeNormalisation.generateModelSummary(readingFolder,writingFolder)

readingFolder = '/Users/hazemalsaied/RA/Evaluation/OtherSysSummariesHtml'
writingFolder = '/Users/hazemalsaied/RA/Evaluation/RougeXmls'
RougeNormalisation.generateEvalXML(readingFolder,writingFolder )