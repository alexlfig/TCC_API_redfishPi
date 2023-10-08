import psutil
import json
import os

MANAGER_ID = 2

# MANAGERS ROOT

def get_managers():
    managers = {
        "@Redfish.Copyright": "Copyright 2014-2019 DMTF. All rights reserved.",
        "@odata.context": "/redfish/v1/$metadata#Managers",
        "@odata.id": "/redfish/v1/Managers",
        "@odata.type": "#ManagerCollection.ManagerCollection",
        "Name": "Manager Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Managers/" + str(MANAGER_ID)
            }
        ],
        "Oem": {}
    }
    return managers

# MANAGERS ID

def get_managers_id():
    pass

# MANAGERS ID NETWORK PROTOCOL

def get_managers_id_networkProtocol():
    pass

# MANAGERS ID NICS

def get_managers_id_nics():
    pass

def get_managers_id_nics_dedicated():
    pass

# MANAGERS ID SERIAL INTERFACES

def get_managers_id_serialInterfaces():
    pass

def get_managers_id_serialInterfaces_TTY0():
    pass

# MANAGERS ID LOG SERVICES

def get_managers_id_logServices():
    pass

def get_managers_id_logServices_log():
    pass

def get_managers_id_logServices_log_entries():
    pass

def get_managers_id_logServices_log_entries_id():
    pass