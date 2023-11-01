import readings
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict
import psutil
import json
import os

def get_redfish_v1():
    redfish_v1 = OrderedDict([
        ("@odata.context", "/redfish/v1/$metadata#ServiceRoot"),
        ("@odata.type", "#ServiceRoot.1.0.0.ServiceRoot"),
        ("@odata.id", "/redfish/v1/"),
        ("Id", "RootService"),
        ("Name", "Root Service"),
        ("RedfishVersion", "1.0.0"),
        ("UUID", readings.system_uuid()), 
        ("Chassis", OrderedDict([("@odata.id", "/redfish/v1/Chassis")])),
        ("Managers", OrderedDict([("@odata.id", "/redfish/v1/Managers")])),
        ("TaskService", OrderedDict([("@odata.id", "/redfish/v1/TaskService")])),
        ("SessionService", OrderedDict([("@odata.id", "/redfish/v1/SessionService")])),
        ("AccountService", OrderedDict([("@odata.id", "/redfish/v1/AccountService")])),
        ("EventService", OrderedDict([("@odata.id", "/redfish/v1/EventService")])),
        ("Registries", OrderedDict([("@odata.id", "/redfish/v1/Registries")])),
        ("Systems", OrderedDict([("@odata.id", "/redfish/v1/Systems")])),
        ("CompositionService", OrderedDict([("@odata.id", "/redfish/v1/CompositionService")]))
    ])
    
    return redfish_v1
    

def get_redfish_v1_compositionService():
    return get_redfish_v1()
