import readings

# CHASSIS ROOT 

def get_chassis():
    chassis = {
        "@odata.type": "#ChassisCollection.ChassisCollection",
        "Name": "Chassis Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Chassis/" + readings.machine_id()
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
        "Id": readings.machine_id(),
        "Name": readings.board_name(),
        "Manufacturer": readings.manufacturer(),
        "Model":readings.model() , 
        "SerialNumber":readings.serial() , 
        "PowerState": "On",
        "IndicatorLED": readings.power_led(),
        "Status": {
            "Health": readings.cpu_health(),
        },
        "ThermalSubsystem": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/ThermalSubsystem"
        },
        "Sensors": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/Sensors"
        },
        "Links": {
            "ComputerSystems": [
                {
                    "@odata.id": "/redfish/v1/Systems/" +readings.machine_id()
                }
            ],
        },
        "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id(),
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return chassis_id

# CHASSIS THERMAL SUBSYSTEM

def get_thermalSubsystem():
    thermalsub = {
        "@odata.type": "#ThermalSubsystem.v1_0_0.ThermalSubsystem",
        "Name": "Thermal Subsystem for Chassis",
        "ThermalMetrics": {
            "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/ThermalSubsystem/ThermalMetrics"
        },
        "Status": {
            "Health": readings.temp_health(),
        },
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/ThermalSubsystem"
        #"@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return thermalsub

def get_thermalMetrics():
    metrics = {
        "@odata.type": "#ThermalMetrics.v1_0_0.ThermalMetrics",
        "Id": "ThermalMetrics",
        "Name": "Chassis Thermal Metrics",
        "TemperatureReadingsCelsius": [
            {
                "Reading": readings.cpu_temp(),
                "DeviceName": "CPU",
                "DataSourceUri": "/redfish/v1/Chassis/"+readings.machine_id()+"/Sensors"
            },
        ],
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/ThermalSubsystem/ThermalMetrics",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return metrics

# CHASSIS POWER SUBSYSTEM

def get_powerSubsystem():
    power = {
        "@odata.type": "#PowerSubsystem.v1_0_0.PowerSubsystem",
        "Name": "Power Subsystem for Chassis",
        "Core Voltage": readings.cpu_voltage(),
        "SDRAM_I Voltage": readings.memory_voltage(),
        "SDRAM_C Voltage": readings.memory_voltage_c(),
        "SDRAM_P Voltage": readings.memory_voltage_p(),
        "Status": {
            "Health": readings.power_health(),
        },
        "Oem": {},
        "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/PowerSubsystem"
        #"@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return power

# CHASSIS SENSORS

def get_sensors():
    sensors = {
        "@odata.type": "#SensorCollection.SensorCollection",
        "Name": "Chassis sensors",
        "CPU Temperature": readings.cpu_temp(),
        "CPU Voltage": readings.cpu_voltage(),
        "SDRAM_I Voltage": readings.memory_voltage(),
        "SDRAM_C Voltage": readings.memory_voltage_c(),
        "SDRAM_P Voltage": readings.memory_voltage_p(),
        "@odata.id": "/redfish/v1/Chassis/"+readings.machine_id()+"/Sensors",
        "@Redfish.Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return sensors