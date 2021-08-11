# @file configData.py
#
# @brief
#
# @version
#   09/Aug/2021:  Author. Akshay Shrivas

hostString = "localhost" 
myPort = "9999"
supportedMethod = ["GET", "POST"]
sslContext=('cert.pem', 'key.pem')

debug = 1
isTest = 0
ErrorString = {"Error": "Error in Handling Reqeust"}
SuccessString = {"OperationStatus": "Success"}
UpdateFailed = {"OperationStatus": "Nothing to Update"}
NoDataSetPresent = {"Error": "No Tasks scheduled yet"}
DeleteFailed = {"OperationStatus": "Nothing to Delete"}

urlS = [
        '/getTaskDetails',
        '/insertUpdateTask',
        '/deleteTheTask'
    ]

delimiter = "|"
newLine = "\n"
dataFileName = "dataFile.ds"
serverLogFile = "serverLogs.log"

DETAILS = "TaskDetails"
USER = "TaskUser"
DATE = "TaskDate"
OP = "Operation"

dummyData = {"akshay": "MyName"}

dummyInsertData = {
"TaskData": "Server Started",
"Date": "08-Aug-2021",
"User": "Akshay"
}

'''
Dummy INSERT

{
"TaskData": "Server Stopped",
"TaskDate": "11-Aug-2021",
"TaskUser": "Rajeev",
"Operation": "Add"
}

DUMMAY UPDATE

{
"TaskData": "Server Stopped",
"TaskDate": "11-Aug-2021",
"TaskUser": "Rajeev",
"Operation": "Update"
}

Dummy Delete

{
"TaskData": "Server Stopped",
"TaskDate": "11-Aug-2021",
"TaskUser": "Rajeev"
}

'''