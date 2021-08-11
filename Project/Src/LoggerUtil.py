# @file LoggerUtil.py
#
# @brief
#
# @version
#   09/Aug/2021:  Author. Akshay Shrivas

import os
import json
from datetime import datetime

from .Config.configData import serverLogFile


def openLogFile():

    logger = ""

    dir_path = os.path.dirname(os.path.realpath(__file__))

    fileName = dir_path + "\Logger\\" + serverLogFile

    logger = open(fileName, "a")

    return logger

def closeLogFile(logger):

    logger.close()

    return 

def log_write(logger, user, operation, data):

    timeStamp = datetime.now()

    line = str(timeStamp) + "\t" + "User=>" + user + "\t" + "Operation=>" + operation + "\tData=>" + str(json.dumps(data))

    logger.write("\n")
    logger.write(line)

    return