Introduction:

    Function Requirement:
        1) REST API calls.
        2) Able to perform all CRUD (create, retrieve, udpate, delete) operations
        3) This is no database project, hence delimited file is used as database.

    Platform requirement:
        1) Supports Windows
        2) Supports Linux
        3) Since it is non-packaged project, hence needs below libraries:
            i. Python 3.9 and above
            ii. Python FLASK
            iii. CORs Support

Project Hierarchy:

    Src --->
            Config --->
                This file has all configurable parameters, which can be changed.
                i. Error Messages
                ii. Success Messages
                iii. Database file name
                iv. Debug level information
                v. Sample input data (JSON)
                vi. Delimiter and separater information
                vii. Server URL
                viii. Server URL, Port
                ix. HTTP Methods support
            
            Data --->
                In this directory, I have placed the data file in .ds format
                Another file is for In Memory implementation(which isn't covered)
            
            dataFileProcessor.py
                This file is responsible for processing the database file.
            
            processor.py
                An intermediate file, which can be used to redirect the request as 
                per database need. (Middleware)
            
            restAccess.py
                This is API configuration file, which actually routes the data.
                (a router file)
            
            ExecutorScripts --->
                This directory has two scripts:
                1) Windows  :   performTask.bat
                2) Linux    :   performTask.sh
                3) Python   :   taskExecution.py

This sample project will perform below operations:

    1) Insert
    2) Update
    3) Delete
    4) Retrieve

How to Use:
    1) Import/download the whole project.
    2) Changet the configuration file as per your environment
    4) If user wants to RUN it on WINDOWS then,
        i. Start the Server from CMD.
        ii. Run the batch file ---> startServer_windows.bat
        iii. Now once server is started, user will be able to Access below APIs:
                http://<URL>:<PORT>/getTaskDetails
                            ---> To retrieve the existing data
                http://<URL>:<PORT>/insertUpdateTask
                            ---> To Either insert or update the data.
                                Note:
                                    JSON variable Flag will define which operation is in process.
                                    if Flag is Add then Insert will be triggered.
                                    if Flag is Update then Update will be done (currently update is based in the TaskUser)
                http://<URL>:<PORT>/deleteTheTask
                            ---> To delete the existing data
                                Note:
                                    Currently delete is based in the TaskUser)

                Through Web Server/Browser
                        open: reqbin.com
                        and use accordingly.
                
                Through command line script [Incomplete - OUT of SCOPE]
                        Below is the format:
                        performTask.bat INSERT "TASK DETAILS" "TASK USER" "TASK DATE" 
                        performTask.bat UPDATE "TASK DETAILS" "TASK USER" "TASK DATE" 
                        performTask.bat DELETE "TASK DETAILS" "TASK USER" "TASK DATE" 
                        performTask.bat RETRIEVE

    5) If user wants to RUN it on LINUX then,

        Option 1: [PARTIAL WORKING]
        Note:  Only RETRIEVE is working, curl is having some issues in parsing the request while sending.
        i. Start the server from WINDOWS or LINUX
        ii. if LINUX run the shell file ----> startServer_linux.sh
        iii. Running from browser will be same as above.
        iv. Through Shell Script 
             Through command line script
                        Below is the format:
                        performTask.sh INSERT "TASK DETAILS" "TASK USER" "TASK DATE" 
                        performTask.sh UPDATE "TASK DETAILS" "TASK USER" "TASK DATE" 
                        performTask.sh DELETE "TASK DETAILS" "TASK USER" "TASK DATE" 
                        performTask.sh RETRIEVE
        
        Option 2: [WORKING]
        i. Open terminal
        ii. if LINUX run the shell file ----> startServer_linux.sh
        iii. Through taskExecution.py
            Below is the format:
                python taskExecution.py RETRIEVE
                python taskExecution.py INSERT TaskUserName TaskDetails TaskDate
                python taskExecution.py UPDATE TaskUserName TaskDetails TaskDate
                python taskExecution.py DELETE TaskUserName TaskDetails TaskDate