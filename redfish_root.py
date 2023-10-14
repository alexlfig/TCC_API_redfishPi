from subprocess import check_output, Popen, PIPE
import psutil
import json
import os

lsblk = Popen(['lsblk', '-f', '--raw'], stdout=PIPE)
disk_info = check_output(["grep", "ext4"], stdin=lsblk.stdout).decode("utf-8") #raspberry alterar "rootfs"
UUID = disk_info.split()[3] #raspberry alterar [4]

def get_redfish_v1():
    redfish_v1 = {
        "@odata.context": "/redfish/v1/$metadata#ServiceRoot",
        "@odata.type": "#ServiceRoot.1.0.0.ServiceRoot",
        "@odata.id": "/redfish/v1/",
        "Id": "RootService",
        "Name": "Root Service",
        "RedfishVersion": "1.0.0",
        "UUID": UUID,
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "Managers": {
            "@odata.id": "/redfish/v1/Managers"
        },
        "TaskService": {
            "@odata.id": "/redfish/v1/TaskService"
        },
        "SessionService": {
            "@odata.id": "/redfish/v1/SessionService"
        },
        "AccountService": {
            "@odata.id": "/redfish/v1/AccountService"
        },
        "EventService": {
            "@odata.id": "/redfish/v1/EventService"
        },
        "Registries": {
            "@odata.id": "/redfish/v1/Registries"
        },
        "Systems": {
            "@odata.id": "/redfish/v1/Systems"
        },
        "CompositionService": {
            "@odata.id": "/redfish/v1/CompositionService"
        }
    }
    return redfish_v1

def get_redfish_v1_compositionService():
    return get_redfish_v1()