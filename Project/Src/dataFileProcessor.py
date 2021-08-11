# @file dataFileProcessor.py
#
# @brief
#
# @version
#   09/Aug/2021:  Author. Akshay Shrivas

import os

from .Config.configData import SuccessString, delimiter, dataFileName, debug, newLine
from .Config.configData import NoDataSetPresent
from .LoggerUtil import log_write, openLogFile, closeLogFile


def giveMeLines():

    dir_path = os.path.dirname(os.path.realpath(__file__))

    fileName = dir_path + "\Data\\" + dataFileName

    count = 0

    try :
        count = sum(1 for ln in open(fileName))
    except Exception as ee:
        print("Error in couting linses", ee)

    return count

def parseMe(line):

    data  = {}

    taskName, taskDate, userDetais, taskId = line.split(delimiter)

    data["TaskName"] = taskName
    data["TaskDate"] = taskDate
    data["TaskUser"] = userDetais
    data["TaskId"] = taskId

    return data

def retrieveDataFromDataFile():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    fileName = dir_path + "\Data\\" + dataFileName

    flag = 0

    #print(fileName)
    try:
        r = open(fileName)
        rd = r.readline()
        fi = 0
        response = {}

        while rd:
            temp = {}
            rd = rd.rstrip()
            if rd == '':
                rd = r.readline()
                continue
            
            fi =  fi + 1
            temp = parseMe(rd)
            response[fi] = temp

            rd = r.readline()

        r.close()
    except Exception as e:
        flag = 1
        print("Error in retrieving", e)
    
    if flag == 0 :
        return response
    else :
        return NoDataSetPresent

def processToDB(line, opType, ipAddr):

    dir_path = os.path.dirname(os.path.realpath(__file__))

    fileName = dir_path + "\Data\\" + dataFileName

    if opType == 1:
        logger = openLogFile()
        log_write(logger, ipAddr, "InsertOperation", line)
        closeLogFile(logger)

        try:
            line_count = giveMeLines()

            fp = open(fileName, 'a')

            line_count = line_count + 1
            line = line + delimiter + str(line_count)

            fp.write(line)
            print(file=fp)

            fp.close()
        except IOError:
            print("Unable To perform Write")
        except Exception as e:
            print("some other error \t  ", e)

    elif opType == 2: # Delete operation
        #print("To be implemented")

        logger = openLogFile()
        log_write(logger, ipAddr, "DeleteOperation", line)
        closeLogFile(logger)

        with open(fileName,"r+") as f:
            allLines = f.readlines()
            f.seek(0)
            for ln in allLines:
                if line not in ln:
                    f.write(ln)
            f.truncate()

    else :
        logger = openLogFile()
        log_write(logger, ipAddr, "UpdateOperation", line)
        closeLogFile(logger)

        try:
            lineNo = 0
            r = open(fileName)
            rd = r.readline()

            while rd:
                
                lineNo = lineNo + 1
                if rd == "":
                    rd = r.readline()
                    continue

                if opType in rd:
                    myData = rd
                    break

                rd = r.readline()

            r.close()
        except Exception as e:
            print("Exception in find ", e)

        try :
            fileObj = open(fileName, "r")
            allLine = fileObj.readlines()
            newData = line + delimiter + str(lineNo) + newLine
            #print(newData)
            allLine[lineNo-1] = newData
            fileObj.close()
        except Exception as e:
            print("Exception in reading all lines ", e)

        try:
            fileObj = open(fileName, "w")
            fileObj.writelines(allLine)
            fileObj.close()
        except Exception as e:
            print("Exception in processing update", e)

    return SuccessString