import readings

def get_redfish_v1():
    redfish_v1 = {
        "@odata.context": "/redfish/v1/$metadata#ServiceRoot",
        "@odata.type": "#ServiceRoot.1.0.0.ServiceRoot",
        "@odata.id": "/redfish/v1/",
        "Id": "RootService",
        "Name": "Root Service",
        "RedfishVersion": "1.0.0",
        "UUID": readings.system_uuid(), 
        "Chassis": {
            "@odata.id": "/redfish/v1/Chassis"
        },
        "TaskService": {
            "@odata.id": "/redfish/v1/TaskService"
        },
        "SessionService": {
            "@odata.id":  "/redfish/v1/SessionService"
        },
        "Systems": {
            "@odata.id": "/redfish/v1/Systems"
        },
    }
    
    return redfish_v1
    

def get_redfish_v1_compositionService():
    return get_redfish_v1()
