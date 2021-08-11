# @file processor.py
#
# @brief
#
# @version
#   09/Aug/2021:  Author. Akshay Shrivas

import json
from flask import jsonify

from .Data.globalTaskData import taskData, totalTask, taskUpdated, taskDeleted
from .Config.configData import debug, delimiter, newLine
from .Config.configData import SuccessString

from .dataFileProcessor import retrieveDataFromDataFile, processToDB, giveMeLines
from .LoggerUtil import log_write, openLogFile, closeLogFile

def getAllTaskHistory(ipAddr):

    logger = openLogFile()
    log_write(logger, ipAddr, "GetDetails","")
    closeLogFile(logger)

    response = retrieveDataFromDataFile()
    #response = jsonify(response)

    #print(jsonify(response))

    logger = openLogFile()
    log_write(logger, ipAddr, "GetDetails", response) #json.dumps(response, indent = 4, sort_keys=True) )
    closeLogFile(logger)
        
    return response

def setTaskDataInMemory(data, ipAddr):

    line = ""
    try: 
        for index, value in data.items():
            if debug == 2:
                print('Key \t {}  \t Value \t "{}!"'.format(index, value))
            if index == "TaskData":
                line = line + value 
            
            elif index == "TaskDate":
                line = line + delimiter + value
            
            elif  index == "TaskUser":
                #value = value + str(giveMeLines())
                line = line + delimiter + value
        
        processToDB(line, 1, ipAddr)

    except :
        if debug == 1 :
            print("Error In Processing setTaskDataInMemory()")
    return SuccessString

def updateInMemory(data, ipAddr):

    line = ""
    user = ""
    try: 
        for index, value in data.items():
            if debug == 2:
                print('Key \t {}  \t Value \t "{}!"'.format(index, value))
            if index == "TaskData":
                line = line + value 
            
            elif index == "TaskDate":
                line = line + delimiter + value

            elif  index == "TaskUser":
                line = line + delimiter + value

            if index == "TaskUser":
                user = value
        
        processToDB(line, user, ipAddr)

    except :
        if debug == 1 :
            print("Error In Processing updateInMemory()")

    return SuccessString


def deleteInMemory(data, ipAddr):

    line = ""
    user = ""
    try: 
        for index, value in data.items():
            '''
            if debug == 2:
                print('Key \t {}  \t Value \t "{}!"'.format(index, value))
            if index == "TaskData":
                line = line + value 
            
            elif index == "TaskDate":
                line = line + delimiter + value

            elif  index == "TaskUser":
                line = line + delimiter + value
            '''
            if index == "TaskUser":
                user = value
        
        processToDB(user, 2, ipAddr)

    except :
        if debug == 1 :
            print("Error In Processing deleteInMemory()")

    return SuccessString