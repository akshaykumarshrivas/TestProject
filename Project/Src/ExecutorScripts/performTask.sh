#!/bin/sh

IS_TEST=0

#JSON constant for request data
TASKDETAILS=\"TaskData\"
TASKDATE=\"TaskDate\"
TASKUSER=\"TaskUser\"
TASKDATE=\"TaskDate\"
OPERATIONTYPE=\"Operation\"

#Symbols
OPENING="{"
CLOSING="}"
COMMA=","
COLON=":"
SINGLEQUOTE="'"
SPACE=" "

#Curl Request Hanlders
CURL="curl"
HEADER=" --header"
CONTENT="\"Content-Type:application/json\""
REQ="--request "
METHOD1="POST"
METHOD2="GET"
DATA=" --data"
FLAGS=" -L"

#URL and Router configuration
PROTOCOL="http://"
URL="10.245.14.137"
PORT="9999"

#Routes
INSERT="/insertUpdateTask"
UPDATE="/insertUpdateTask"
DELETE="/deleteTheTask"
GETDATA="/getTaskDetails"

if [ $IS_TEST = 1 ]; then
    operation_type="DELETE"
    task_details="SERVER"
    task_user="AKSHAY"
    task_date="08-Aug-2021"
else
    operation_type=$1
    task_details=$2
    task_user=$3
    task_date=$4
fi

#echo $operation_type
#echo $task_details
#echo $task_user
#echo $task_date

REQUEST=""
COMMAND=""
TYPE=""

generate_post_data()
{
  cat <<EOF
        '{
        $TASKDETAILS:"$task_details",
        $TASKUSER:"$task_user",
        $TASKDATE:"$task_date",
        $OPERATIONTYPE:"$operation_type"
        }'
EOF
}

generate_post_data2()
{
        cat << EOF
        '{
"TaskData": "Server Started",
"TaskDate": "11-Aug-2021",
"TaskUser": "RAjeev",
"Operation": "Update"
}'

EOF
}

if [ "$operation_type" = "INSERT" ]; then
    #REQUEST="$OPENING$TASKDETAILS$COLON$task_details $COMMA $TASKUSER$COLON$task_user $COMMA $TASKDATE$COLON$task_date $COMMA $OPERATIONTYPE$COLON$operation_type$CLOSING";
    REQ1="{ \"TaskData\": \"$task_details\", \"TaskDate\": \"$task_date\", \"TaskUser\": \"$task_user\", \"Operation\": \"$operation_type\" }"
    TYPE=$INSERT;
elif  [ "$operation_type" = "UPDATE" ]; then
    REQUEST="$OPENING$TASKDETAILS$COLON\"$task_details\" $COMMA $TASKUSER$COLON\"$task_user\" $COMMA $TASKDATE$COLON\"$task_date\" $COMMA $OPERATIONTYPE$COLON\"$operation_type\"$CLOSING";
    REQ1="{ \"TaskData\": \"$task_details\", \"TaskDate\": \"$task_date\", \"TaskUser\": \"$task_user\", \"Operation\": \"$operation_type\" }"
    TYPE=$UPDATE;
elif  [ "$operation_type" = "DELETE" ]; then
    REQUEST="$OPENING$TASKDETAILS$COLON\"$task_details\" $COMMA $TASKUSER$COLON\"$task_user\" $COMMA $TASKDATE$COLON\"$task_date\"$CLOSING";
    REQ1="{ \"TaskData\": \"$task_details\", \"TaskDate\": \"$task_date\", \"TaskUser\": \"$task_user\", \"Operation\": \"$operation_type\" }"
    TYPE=$DELETE;
elif  [ "$operation_type" = "RETRIEVE" ]; then
    echo $REQUEST;
    REQ1="{\"REQUEST\" : \"$GETDATA\"}"
    TYPE=$GETDATA;
else
    echo "No Matched Operation Found";
    exit;
fi;

echo "Sending Request......"
echo $REQ1 | python -m json.tool
echo "for $operation_type";

if  [ "$operation_type" = "RETRIEVE" ]; then
        COMMAND="$CURL $FLAGS $SPACE $HEADER $SPACE $CONTENT $SPACE $REQ $METHOD2 $SPACE $PROTOCOL$URL$COLON$PORT$TYPE"
else
        #COMMAND="$CURL $FLAGS $SPACE $HEADER $SPACE $CONTENT $SPACE $REQ $METHOD1 $SPACE $DATA $SINGLEQUOTE$REQUEST$SINGLEQUOTE $PROTOCOL$URL$COLON$PORT$TYPE"
        #COMMAND="$CURL $FLAGS $SPACE $HEADER $SPACE $CONTENT $SPACE $REQ $METHOD1 $SPACE $DATA $(generate_post_data2) $PROTOCOL$URL$COLON$PORT$TYPE";
        COMMAND="curl $FLAGS --header 'Content-Type:application/json' --request POST --data '$REQ1' $PROTOCOL$URL$COLON$PORT$TYPE"
fi;

echo $COMMAND

RESPONSE=""
`$COMMAND`
RESPONSE=`$COMMAND`

echo "Response Received"

echo $RESPONSE | python -m json.tool

echo "CLOSING"