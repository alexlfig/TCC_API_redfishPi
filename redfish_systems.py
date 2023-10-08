import psutil
import json
import os

CHASSIS_ID = 0
SYSTEM_ID = 1
MANAGER_ID = 2

# SYSTEMS ROOT

def get_systems():
    systems = {
        "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
        "Name": "Computer System Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID)
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems",
        "@odata.id": "/redfish/v1/Systems",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }

# SYSTEMS ID

def get_systems_id():
    systems_id = {
        "@odata.type": "#ComputerSystem.v1_1_0.ComputerSystem",
        "Id": str(SYSTEM_ID),
        "Name": "WebFrontEnd483",
        "SystemType": "Physical",
        "AssetTag": "Chicago-45Z-2381",
        "Manufacturer": "Contoso",
        "Model": "3500RX",
        "SKU": "8675309",
        "SerialNumber": "437XR1138R2",
        "PartNumber": "224071-J23",
        "Description": "Web Front End node",
        "UUID": "38947555-7742-3448-3784-823347823834",
        "HostName": "web483",
        "Status": {
            "State": "Enabled",
            "Health": "OK",
            "HealthRollUp": "OK"
        },
        "IndicatorLED": "Off",
        "PowerState": "On",
        "Boot": {
            "BootSourceOverrideEnabled": "Once",
            "BootSourceOverrideTarget": "Pxe",
            "BootSourceOverrideTarget@Redfish.AllowableValues": [
                "None",
                "Pxe",
                "Cd",
                "Usb",
                "Hdd",
                "BiosSetup",
                "Utilities",
                "Diags",
                "SDCard",
                "UefiTarget"
            ],
            "BootSourceOverrideMode": "UEFI",
            "UefiTargetBootSourceOverride": "/0x31/0x33/0x01/0x01"
        },
        "TrustedModules": [
            {
                "FirmwareVersion": "1.13b",
                "InterfaceType": "TPM1_2",
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                }
            }
        ],
        "Oem": {
            "Contoso": {
                "@odata.type": "http://Contoso.com/Schema#Contoso.ComputerSystem",
                "ProductionLocation": {
                    "FacilityName": "PacWest Production Facility",
                    "Country": "USA"
                }
            },
            "Chipwise": {
                "@odata.type": "http://Chipwise.com/Schema#Chipwise.ComputerSystem",
                "Style": "Executive"
            }
        },
        "BiosVersion": "P79 v1.33 (02/28/2015)",
        "ProcessorSummary": {
            "Count": 2,
            "ProcessorFamily": "Multi-Core Intel(R) Xeon(R) processor 7xxx Series",
            "Status": {
                "State": "Enabled",
                "Health": "OK",
                "HealthRollUp": "OK"
            }
        },
        "MemorySummary": {
            "TotalSystemMemoryGiB": 96,
            "Status": {
                "State": "Enabled",
                "Health": "OK",
                "HealthRollUp": "OK"
            }
        },
        "Bios": {
            "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/BIOS"
        },
        "Processors": {
            "@odata.id": "redfish/v1/Systems/" + str(SYSTEM_ID) + "/Processors"
        },
        "Memory": {
            "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/Memory"
        },
        "EthernetInterfaces": {
            "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/EthernetInterfaces"
        },
        "SimpleStorage": {
            "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/SimpleStorage"
        },
        "LogServices": {
            "@odata.id:" "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/LogServices"
        },
        "Links": {
            "Chassis": [
                {
                    "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID)
                }
            ],
            "ManagedBy": [
                {
                    "@odata.id": "/redfish/v1/Managers/" + str(MANAGER_ID)
                }
            ]
        },
        "Actions": {
            "#ComputerSystem.Reset": {
                "target": "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/Actions/ComputerSystem.Reset",
                "ResetType@Redfish.AllowableValues": [
                    "On",
                    "ForceOff",
                    "GracefulShutdown",
                    "GracefulRestart",
                    "ForceRestart",
                    "Nmi",
                    "ForceOn",
                    "PushPowerButton"
                ]
            },
            "Oem": {
                "#Contoso.Reset": {
                    "target": "/redfish/v1/Systems/" + str(SYSTEM_ID) + "/Oem/Contoso/Actions/Contoso.Reset"
                }
            }
        },
        "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
        "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID),
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return systems_id

# SYSTEMS ID BIOS

def get_systems_id_bios():
    pass

def get_systems_id_bios_settings():
    pass

# SYSTEMS ID PROCESSORS

def get_systems_id_processors():
    pass

def get_systems_id_processors_cpu1():
    pass

# SYSTEMS ID MEMORY

def get_systems_id_memory():
    pass

def get_systems_id_memory_dimm1():
    pass

def get_systems_id_memory_dimm2():
    pass

def get_systems_id_memory_dimm3():
    pass

def get_systems_id_memory_dimm4():
    pass

# SYSTEMS ID ETHERNET INTERFACES

def get_systems_id_ethernetInterfaces():
    pass

def get_systems_id_ethernetInterfaces_macAddress1():
    pass

def get_systems_id_ethernetInterfaces_macAddress1_VLANs():
    pass

def get_systems_id_ethernetInterfaces_macAddress1_VLANs_1():
    pass

def get_systems_id_ethernetInterfaces_macAddress1_VLANs_2():
    pass

def get_systems_id_ethernetInterfaces_macAddress2():
    pass

def get_systems_id_ethernetInterfaces_macAddress2_VLANs_1():
    pass

def get_systems_id_ethernetInterfaces_macAddress2_VLANs_2():
    pass

# SYSTEMS ID SIMPLE STORAGE

def get_systems_id_simpleStorage():
    pass

def get_systems_id_simpleStorage_1():
    pass

# SYSTEMS ID LOG SERVICE

def get_systems_id_logServices():
    pass

def get_systems_id_logServices_id():
    pass

def get_systems_id_logServices_id_entries():
    pass

def get_systems_id_logServices_id_entries_1():
    pass

def get_systems_id_logServices_id_entries_2():
    pass