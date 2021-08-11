# @file taskExecution.py
#
# @brief
#
# @version
#   09/Aug/2021:  Author. Akshay Shrivas

import sys 
import requests
import json
#from ..Config.configData import debug, isTest
#from ..Config.configData import DATE, DETAILS, USER, OP

number_args = 0

DETAILS = "TaskData"
USER = "TaskUser"
DATE = "TaskDate"
OP = "Operation"

urlS =  ["/insertUpdateTask", "/deleteTheTask", "/getTaskDetails"]
proto = "http://" 
hostAddr = "localhost"
portAddr = "9999"
headers1 = {'content-type':'application/json'}

debug = 1
isTest = 0

def validation():
    if  isTest == 0  :
        number_args = len(sys.argv)  
        if  number_args < 2  :  
            print( "Wrong entry. Please use script in below formate.\n" ) 
            print( "taskProcessor INSERT TaskUser TaskDetails TaskDate" )
            print( "taskProcessor UPDATE TaskUser TaskDetails TaskDate" )
            print( "taskProcessor DELETE TaskUser TaskDetails TaskDate" )
            print( "taskProcessor RETRIEVE" )
            exit()
    else :
        number_args = 4  
    
    return number_args

def initVariable(test, na):

    operation = ""
    task_user = ""
    task_details = ""
    task_date = ""
    
    if test == 0:
        if na >= 4:
            if debug == 2:
                print("Command line data ", sys.argv)
            operation = sys.argv[1]
            task_user = sys.argv[2]
            task_details = sys.argv[3]
            task_date = sys.argv[4]
        else:
            operation = sys.argv[1]
    else :
        operation = "INSERT"
        task_user = "AKSHAY"
        task_details = "ServerStart"
        task_date = "09-Aug-2021"
    
    REQUEST=""
    if na >= 4:
        REQUEST = {
            DETAILS : task_details,
            USER : task_user,
            DATE : task_date,
            OP : operation
        }
    else:
        REQUEST=""

    if debug == 2:
        print("----------------------", REQUEST, na)

    return operation, REQUEST


def postMyData(req, op):

    print("Sending Reqeust for Data", req, " And reqeust type ", op)

    if op == "INSERT" or op == "UPDATE":
        URL  = proto + hostAddr + ":" + portAddr + "/" + urlS[0]
        res = requests.post(URL, data=json.dumps(req), headers=headers1)
    elif op == "DELETE":
        URL  = proto + hostAddr + ":" + portAddr + "/" + urlS[1]
        res = requests.post(URL, data=json.dumps(req), headers=headers1)
    
    return res

def getMyData():
    URL  = proto + hostAddr + ":" + portAddr + "/" + urlS[2]
    res = requests.get(URL)

    return res

def performOperation(op, REQUEST):

    if debug == 2:
        print("performOperation()", op)

    response = ""

    if  op == "INSERT" or op == "UPDATE" or op == "DELETE":
        if debug == 2:
            print( REQUEST )
        response = postMyData(REQUEST, op)
    elif op == "RETRIEVE":
        response = getMyData()
    else:
        print ("Invalid request", op)
    
    return response
    
def mainFucntion():
    na = validation()

    op = ""
    if isTest == 0:
        op, req = initVariable(0, na)
    else :
        op, req = initVariable(1, na)
    
    rs = performOperation(op, req)

    print("\n\nReceived Response is : \n")
    print(json.dumps(rs.json(), indent=4))

    return

mainFucntion()