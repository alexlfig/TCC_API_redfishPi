import psutil
import json
import os
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict

TASK_SERVICE_ID = 4

def get_taskService():
    task_service = {
        "@odata.context": "/rest/v1/$metadata#TaskService/$entity",
        "@odata.type": "#Tasks.0.94.0.TaskCollection",
        "Name": "Task Collection",
        "Modified": "2012-03-07T14:44",
        "Links": {
            "Members@odata.count": 1,
            "Members": [
                {
                    "@odata.id": "/redfish/v1/TaskService/" + str(TASK_SERVICE_ID)
                }
            ]
        }
    }
    return task_service

def get_taskService_id():
    task_service_id_func = {
        "@odata.context": "/redfish/v1/$metadata/TaskService/Links/Members/$entity",
        "@odata.id": "/redfish/v1/TaskService/" + str(TASK_SERVICE_ID),
        "@odata.type": "#TaskService.0.94.0.Task",
        "Id": str(TASK_SERVICE_ID),
        "Name": "Task 1",
        "Modified": "2012-03-07T14:44",
        "TaskState": "Completed",
        "StartTime": "2012-03-07T14:44",
        "EndTime": "2012-03-07T14:45",
        "TaskStatus": "OK"
    }
    return task_service_id_func