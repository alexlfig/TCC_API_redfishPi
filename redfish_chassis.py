import psutil
import json
import os

CHASSIS_ID = 0
SYSTEM_ID = 1
MANAGER_ID = 2

# CHASSIS ROOT 

def get_chassis():
    chassis = {
        "@odata.type": "#ChassisCollection.ChassisCollection",
        "Name": "Chassis Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID)
            }
        ],
        "@odata.id": "/redfish/v1/Chassis",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return chassis

# CHASSIS ID

def get_chassis_id():
    chassis_id = {
        "@odata.type": "#Chassis.v1_15_0.Chassis",
        "Id": str(CHASSIS_ID),
        "Name": "PREENCHER",
        "ChassisType": "PREENCHER",
        "AssetTag": "PREENCHER",
        "Manufacturer": "PREENCHER",
        "Model": "PREENCHER",
        "SKU": "PREENCHER",
        "SerialNumber": "PREENCHER",
        "PartNumber": "PREENCHER",
        "PowerState": "PREENCHER",
        "IndicatorLED": "PREENCHER",
        "HeightMm": "PREENCHER",
        "WidthMm": "PREENCHER",
        "DepthMm": "PREENCHER",
        "WeightKg": "PREENCHER",
        "Location": {
            "PostalAddress": {
                "Country": "PREENCHER",
                "Territory": "PREENCHER",
                "City": "PREENCHER",
                "Street": "PREENCHER",
                "HouseNumber": "PREENCHER",
                "Name": "PREENCHER",
                "PostalCode": "PREENCHER",
            },
            "Placement": {
                "Row": "PREENCHER",
                "Rack": "PREENCHER",
                "RackOffsetUnits": "PREENCHER",
                "RackOffset": "PREENCHER",
            }
        },
        "Status": {
            "State": "PREENCHER",
            "Health": "PREENCHER",
        },
        "ThermalSubsystem": {
            "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID) + "/ThermalSubsystem"
        },
        "PowerSubsystem": {
            "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID) + "/PowerSubsystem"
        },
        "EnvironmentMetrics": {
            "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID) + "/EnvironmentMetrics"
        },
        "Sensors": {
            "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID) + "/Sensors"
        },
        "Links": {
            "ComputerSystems": [
                {
                    "@odata.id": "/redfish/v1/Systems/" + str(SYSTEM_ID)
                }
            ],
            "ManagedBy": [
                {
                    "@odata.id": "/redfish/v1/Managers/" + str(MANAGER_ID)
                }
            ],
            "ManagersInChassis": [
                {
                    "@odata.id": "/redfish/v1/Managers/" + str(MANAGER_ID)
                }
            ]
        },
        "@odata.id": "/redfish/v1/Chassis/" + str(CHASSIS_ID),
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return chassis_id

# CHASSIS THERMAL SUBSYSTEM

def get_thermalSubsystem():
    pass

def get_fans():
    pass

def get_bay1():
    pass

def get_cpu1():
    pass

def get_thermalMetrics():
    pass

# CHASSIS POWER SUBSYSTEM

def get_powerSubsystem():
    pass

# CHASSIS ENVIRONMENT METRICS

def get_environmentMetrics():
    pass

# CHASSIS SENSORS

def get_sensors():
    pass