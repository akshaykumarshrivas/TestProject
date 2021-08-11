# @file restAccess.py
#
# @brief
#
# @version
#   09/Aug/2021:  Author. Akshay Shrivas

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_api import status
import json 

from .Config.configData import hostString
from .Config.configData import myPort
from .Config.configData import supportedMethod
from .Config.configData import urlS
from .Config.configData import dummyData
from .Config.configData import ErrorString, UpdateFailed, DeleteFailed, NoDataSetPresent
from .Config.configData import debug

from .processor import getAllTaskHistory, setTaskDataInMemory, updateInMemory, deleteInMemory
from .dataFileProcessor import giveMeLines
from .LoggerUtil import log_write, openLogFile, closeLogFile

#hostString = "10.245.14.137" 
#myPort = "9999"
#dummyData = {"akshay": "MyName"}

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route(urlS[0], methods=[supportedMethod[0]])
def getTaskData():
    ipAddr = request.remote_addr
    logger = openLogFile()
    log_write(logger, ipAddr, "GetDetails", "" )
    closeLogFile(logger)
    
    try:
        if giveMeLines() >= 1:
            json_output = jsonify(getAllTaskHistory(ipAddr))
        else:
            json_output = NoDataSetPresent
    except:
        return jsonify(ErrorString), status.HTTP_500_INTERNAL_SERVER_ERROR

    return json_output

@app.route(urlS[1], methods=[supportedMethod[1]])
def setOrUpdateData():

    ipAddr = request.remote_addr
    logger = openLogFile()
    log_write(logger, ipAddr, "InsertUpdateDetails",request.get_json())
    closeLogFile(logger)

    if giveMeLines() >= 1 or True:
        if debug == 1:
            print("setOrUpdateData()",request, request.get_data())
        try:
            data = request.get_json()
            flag = data.get('Operation')
            if debug == 1:
                print("Received Data is ", data)
            
            flag = flag.upper()
            if flag == 'INSERT':
                json_output = jsonify(setTaskDataInMemory(data, ipAddr))
            elif giveMeLines() >= 1:
                json_output = jsonify(updateInMemory(data, ipAddr))
            else:
                json_output = UpdateFailed
        except:
            return jsonify(ErrorString), status.HTTP_500_INTERNAL_SERVER_ERROR

    return json_output

@app.route(urlS[2], methods=[supportedMethod[1]])
def deleteGivenData():

    ipAddr = request.remote_addr
    logger = openLogFile()
    log_write(logger, ipAddr, "DeleteDetailsBasedOnUser",request.get_json())
    closeLogFile(logger)

    if debug == 1:
        print("deleteGivenData()", request.get_data())
    try:
        data = request.get_json()
        if debug == 1:
            print(data)
        
        if giveMeLines() >= 1:
            json_output = jsonify(deleteInMemory(data, ipAddr))
        else:
            json_output = DeleteFailed
    except:
        return jsonify(ErrorString), status.HTTP_500_INTERNAL_SERVER_ERROR

    return json_output

if __name__ == '__main__':
    app.run(host=hostString, port=myPort) #, ssl_context = sslContext)
