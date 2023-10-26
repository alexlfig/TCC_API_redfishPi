import readings
import psutil
import json
import os
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict


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
                "@odata.id": "/redfish/v1/Chassis/" +readings.serial()
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
        "Id": readings.serial(),
        "Name": "PREENCHER",
        "ChassisType": "PREENCHER",
        "AssetTag": "PREENCHER",
        "Manufacturer": "PREENCHER",
        "Model":readings.model() , 
        "SKU": "PREENCHER",
        "SerialNumber":readings.serial() , 
        "PartNumber": "PREENCHER",
        "PowerState": "PREENCHER",
        "IndicatorLED": "PREENCHER",
        "HeightMm": "PREENCHER",
        "WidthMm": "PREENCHER",
        "DepthMm": "PREENCHER",
        "WeightKg": "PREENCHER",
        "Status": {
            "State": "PREENCHER",
            "Health": "PREENCHER",
        },
        "ThermalSubsystem": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem"
        },
        "PowerSubsystem": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/PowerSubsystem"
        },
        "EnvironmentMetrics": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/EnvironmentMetrics"
        },
        "Sensors": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors"
        },
        "Links": {
            "ComputerSystems": [
                {
                    "@odata.id": "/redfish/v1/Systems/" +readings.boot_id()
                }
            ],
        },
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial(),
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return chassis_id

# CHASSIS THERMAL SUBSYSTEM

def get_thermalSubsystem():
    thermalsub = {
        "@odata.type": "#ThermalSubsystem.v1_0_0.ThermalSubsystem",
        "Name": "Thermal Subsystem for Chassis",
        "FanRedundancy": [
            {
                "RedundancyType": "NPlusM",
                "MaxSupportedInGroup": str(1),
                "MinNeededInGroup": str(1),
                "RedundancyGroup": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans/Bay1"
                    },
                ],
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                }
            },
            {
                "RedundancyType": "NPlusM",
                "MaxSupportedInGroup": 1,
                "MinNeededInGroup": 1,
                "RedundancyGroup": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans/CPU1"
                    },
                ],
                "Status": {
                    "State": "Disabled"
                }
            }
        ],
        "Fans": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans"
        },
        "ThermalMetrics": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/ThermalMetrics"
        },
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem"
        #"@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return thermalsub

def get_fans():
    fans = {
        "@odata.type": "#FanCollection.FanCollection",
        "Name": "Fan Club",
        "Members@odata.count": 2,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans/Bay1"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans/CPU1"
            }
        ],
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return fans

def get_bay1():
    bay1 = {
        "@odata.type": "#Fan.v1_0_0.Fan",
        "Id": "Bay1",
        "Name": "Fan Bay 1",
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "PhysicalContext": "Chassis",
        "Model": "RKS-440DC",
        "Manufacturer": "Contoso Fans",
        "PartNumber": "23456-133",
        "SparePartNumber": "93284-133",
        "LocationIndicatorActive": str(true),
        "HotPluggable": str(true),
        "SpeedPercent": {
            "Reading": str(45),
            "SpeedRPM": str(2200),
            "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+/Sensors/FanBay1"
        },
        "Location": {
            "PartLocation": {
                "ServiceLabel": "Chassis Fan Bay 1",
                "LocationType": "Bay",
                "LocationOrdinalValue": str(0)
            }
        },
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans/Bay1",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return bay1

def get_cpu1():
    temp_cpu1 = {
        "@odata.type": "#Fan.v1_0_0.Fan",
        "Id": "CPU1",
        "Name": "Fan for CPU 1",
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "PhysicalContext": "CPU",
        "Model": "RKS-440DC",
        "Manufacturer": "Contoso Fans",
        "PartNumber": "23456-133",
        "SparePartNumber": "93284-133",
        "LocationIndicatorActive": str(false),
        "HotPluggable": str(false),
        "SpeedPercent": {
            "Reading": str(45),
            "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/CPUFan1"
        },
        "Location": {
            "PartLocation": {
                "ServiceLabel": "CPU #1 Fan",
                "LocationType": "Bay",
                "LocationOrdinalValue": str(0)
            }
        },
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/Fans/CPU1",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return temp_cpu1

def get_thermalMetrics():
    metrics = {
        "@odata.type": "#ThermalMetrics.v1_0_0.ThermalMetrics",
        "Id": "ThermalMetrics",
        "Name": "Chassis Thermal Metrics",
        "TemperatureSummaryCelsius": {
            "Internal": {
                "Reading": str(39),
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/CPU1Temp"
            },
            "Intake": {
                "Reading": str(24.8),
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/IntakeTemp"
            },
            "Ambient": {
                "Reading": str(22.5),
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/AmbientTemp"
            },
            "Exhaust": {
                "Reading": str(22.5),
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/ExhaustTemp"
            }
        },
        "TemperatureReadingsCelsius": [
            {
                "Reading": str(22.5),
                "DeviceName": "Intake",
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/IntakeTemp"
            },
            {
                "Reading": str(22.5),
                "DeviceName": "Exhaust",
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/ExhaustTemp"
            }
        ],
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/ThermalSubsystem/ThermalMetrics",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return metrics

# CHASSIS POWER SUBSYSTEM

def get_powerSubsystem():
    power = {
        "@odata.type": "#PowerSubsystem.v1_0_0.PowerSubsystem",
        "Name": "Power Subsystem for Chassis",
        "CapacityWatts": str(2000),
        "Allocation": {
            "RequestedWatts": str(1500),
            "AllocatedWatts": str(1200)
        },
        "PowerSupplyRedundancy": [
            {
                "RedundancyType": "Failover",
                "MaxSupportedInGroup": 2,
                "MinNeededInGroup": 1,
                "RedundancyGroup": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/PowerSubsystem/PowerSupplies/Bay1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/PowerSubsystem/PowerSupplies/Bay2"
                    }
                ],
                "Status": {
                    "State": "UnavailableOffline",
                    "Health": "OK"
                }
            }
        ],
        "PowerSupplies": {
            "odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/PowerSubsystem/PowerSupplies"
        },
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/PowerSubsystem"
        #"@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return power

# CHASSIS ENVIRONMENT METRICS

def get_environmentMetrics():
    env = {
        "@odata.type": "#EnvironmentMetrics.v1_0_0.EnvironmentMetrics",
        "Name": "Chassis Environment Metrics",
        "TemperatureCelsius": {
            "Reading": 39,
            "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/CPU1Temp"
        },
        "PowerWatts": {
            "Reading": 374,
            "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/TotalPower"
        },
        "FanSpeedsPercent": [
            {
                "DeviceName": "Chassis Fan #1",
                "Reading": 45,
                "SpeedRPM": 1900,
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/FanBay1"
            },
            {
                "DeviceName": "Chassis Fan #2",
                "Reading": 55,
                "SpeedRPM": 2100,
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/FanBay2"
            }
        ],
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/EnvironmentMetrics"
        #"@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return env

# CHASSIS SENSORS

def get_sensors():
    sensors = {
        "@odata.type": "#SensorCollection.SensorCollection",
        "Name": "Chassis sensors",
        "Members@odata.count": 8,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/AmbientTemp"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/CPU1Temp"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/MemTemp"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/ExhaustTemp"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/IntakeTemp"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/PS1Energy"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/TotalEnergy"
            },
            {
                "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors/TotalPower"
            }
        ],
        "@odata.id": "/redfish/v1/Chassis/"+readings.serial()+"/Sensors",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return sensors