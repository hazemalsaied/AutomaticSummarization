import os


class Statistics:
    reportPath = '/Users/hazemalsaied/RA/Evaluation/statistics.md'

    @staticmethod
    def getAvgReport(sysPath, ourSysPath):
        totalAVG = 0
        totalLineNum = 0
        report = open(Statistics.reportPath, 'a')
        for root, dirs, files in os.walk(sysPath):
            for dir in dirs:
                dirpath = os.path.join(sysPath, dir)
                sysAvg = Statistics.calculateSummariesWordAvg(dirpath)
                lineNum = Statistics.calculateSummariesLinesAvg(dirpath)
                totalLineNum += lineNum
                totalAVG += sysAvg
                report.write('**' + dir + '** : ' + str(sysAvg) + ' Words, ' + str(lineNum) + ' Lines'+ '\n')
            report.write('####Total AVG : ' + str(totalAVG / len(dirs)) +' words, '+ str(totalLineNum / len(dirs))+  ' lines \n')
            break
        #report.write('##Our system AVG: ' + str(Statistics.calculateSummariesWordAvg(ourSysPath)))

        report.close()

    @staticmethod
    def getLinesNum(summaryFile):
        file = open(summaryFile)
        return len(file.readlines())

    @staticmethod
    def calculateSummariesLinesAvg(summariesFolder):
        lineNum = 0
        for root, dirs, files in os.walk(summariesFolder):
            for file in files:
                fileDir = os.path.join(summariesFolder, file)
                lineNum += Statistics.getLinesNum(fileDir)
            break
        print lineNum / 10
        return lineNum / 10

    @staticmethod
    def calculateSummariesWordAvg(summariesFolder):
        summ = 0
        for root, dirs, files in os.walk(summariesFolder):
            for file in files:
                fileDir = os.path.join(summariesFolder, file)
                summ += Statistics.calculateSummaryWordCount(fileDir)
            break
        return summ / 10

    @staticmethod
    def calculateSummaryWordCount(summaryFile):
        with open(summaryFile) as f:
            # create a list of all words fetched from the file using a list comprehension
            words = [word for line in f for word in line.split()]
            return len(words)


summaryFile = '/Users/hazemalsaied/RA/Evaluation/TestSum/sum'
ourSys = '/Users/hazemalsaied/RA/Evaluation/CommunitySummaries-Test/Summaries-Redondant/systems'


#Statistics.calculateSummariesWordAvg(ourSys)
Statistics.getAvgReport(summaryFile, ourSys)
