import readings
from copy import deepcopy #Usado para persistência dos dados na função geradora de funções

def get_taskService():
    task_service = {
        "@odata.context": "/rest/v1/$metadata#TaskService/$entity",
        "@odata.type": "#Tasks.0.94.0.TaskCollection",
        "Name": "Task Collection",
        "Modified": "2012-03-07T14:44",
        "Links": {
            "Members@odata.count": readings.process_counter(),
            "Members": readings.process_members()
        }
    }
    return task_service

def dynamic_task_funcs():
    task_funcs = []

    for task in readings.process_pids():
        def bind_task_function():
            taskid = deepcopy(task)
            def task_function():
                stats = readings.process_stats(taskid)
                task_dict = {
                    "@odata.context": "/redfish/v1/$metadata/TaskService/Links/Members/$entity",
                    "@odata.id": "/redfish/v1/TaskService/" + stats['pid'],
                    "@odata.type": "#TaskService.0.94.0.Task",
                    "Id": stats['pid'],
                    "Name": stats['name'],
                    "TaskState": stats['status'],
                    "StartTime": stats['start_time'],
                }
                return task_dict
            task_function.__name__ = taskid
            return task_function

        task_funcs.append(bind_task_function())
    return task_funcs
