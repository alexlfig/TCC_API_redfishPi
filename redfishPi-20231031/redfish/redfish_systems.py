import readings
import psutil
import json
import os
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict
from copy import deepcopy

# SYSTEMS ROOT

def get_systems():
    systems = {
        "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
        "Name": "Computer System Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Systems/"+readings.boot_id()
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems",
        "@odata.id": "/redfish/v1/Systems",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return systems

# SYSTEMS ID

def get_systems_id():
    systems_id = {
        "@odata.type": "#ComputerSystem.v1_1_0.ComputerSystem",
        "Id": readings.boot_id(),
        "Name": "WebFrontEnd483",
        "SystemType": "Physical",
        "AssetTag": "Chicago-45Z-2381",
        "Manufacturer": "Contoso",
        "Model": readings.model(),
        "SKU": "8675309",
        "SerialNumber": readings.serial(),
        "PartNumber": "224071-J23",
        "Description": "Web Front End node",
        "UUID": readings.system_uuid(),
        "HostName": readings.hostname(),
        "Status": {
            "State": "Enabled",
            "Health": "OK",
            "HealthRollUp": "OK"
        },
        "IndicatorLED": "Off",
        "PowerState": "On",
        "ProcessorSummary": {
            "Count": "2",
            "ProcessorFamily": readings.cpu_model(),
            "Status": {
                "State": "Enabled",
                "Health": "OK",
                "HealthRollUp": "OK"
            }
        },
        "MemorySummary": {
            "TotalSystemMemoryMiB": readings.memory_total(),
            "Status": {
                "State": "Enabled",
                "Health": "OK",
                "HealthRollUp": "OK"
            }
        },
        "Processors": {
            "@odata.id": "redfish/v1/Systems/" + readings.boot_id() + "/Processors"
        },
        "Memory": {
            "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Memory"
        },
        "EthernetInterfaces": {
            "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces"
        },
        "SimpleStorage": {
            "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/SimpleStorage"
        },
        "LogServices": {
            "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/LogServices"
        },
        "Links": {
            "Chassis": [
                {
                    "@odata.id": "/redfish/v1/Chassis/" + readings.machine_id()
                }
            ],
        },
        "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id(),
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return systems_id

# SYSTEMS ID PROCESSORS

def get_systems_id_processors():
    procs = {
        "@odata.type": "#ProcssorCollection.ProcessorCollection",
        "Name": "Processors Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Processors/CPU1"
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems/Links/Members/" + readings.boot_id() + "/Processors/#entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Processors",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return procs

def get_systems_id_processors_cpu1():
    cpu1 = {
        "@odata.type": "#Processor.v1_0_2.Processor",
        "Id": "CPU1",
        "Socket": "CPU 1",
        "ProcessorType": "CPU",
        "ProcessorArchitecture": readings.cpu_arch(),
        "InstructionSet": readings.cpu_arch(),
        "Manufacturer": "Intel(R) Corporation",
        "Model": readings.cpu_model(),
        "ProcessorID": {
            "VendorID": readings.cpu_vendor(),
            "IdentificationRegisters": "0x34AC34DC8901274A",
            "EffectiveFamily": "0x42",
            "EffectiveModel": "0x61",
            "Step": "0x1",
            "MicrocodeInfo": "0x429943"
        },
        "MaxSpeedMHz": readings.cpu_freq(),
        "TotalCores": readings.cpu_cores(),
        "TotalThreads": readings.cpu_threads(),
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/Processors/Members/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Processors/CPU1",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return cpu1

# SYSTEMS ID MEMORY

def get_systems_id_memory():
    mem = {
        "@odata.type": "#MemoryCollection.MemoryCollection",
        "Name": "Memory Module Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Memory/DIMM"
            },
        ],
        "@odata.context": "/redfish/v1/$metadata#MemoryCollection.MemoryCollection",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Memory",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return mem

def get_systems_id_memory_dimm():
    ram = {
        "@odata.type": "#Memory.v1_0_0.Memory",
        "Name": "DIMM Slot 1",
        "Id": "DIMM1",
        "RankCount": 2,
        "MaxTDPMilliWatts": [
            12000
        ],
        "CapacityMiB": readings.memory_total(),
        "DataWidthBits": 64,
        "BusWidthBits": 72,
        "MemoryLocation": {
            "Socket": 1,
            "MemoryController": 1,
            "Channel": 1,
            "Slot": 1
        },
        "MemoryType": "DRAM",
        "MemoryDeviceType": "DDR4",
        "BaseModuleType": "RDIMM",
        "MemoryMedia": [
            "DRAM"
        ],
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "@odata.context": "/redfish/v1/$metadata#Memory.Memory",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Memory/DIMM",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return ram

# SYSTEMS ID ETHERNET INTERFACES

def get_systems_id_ethernetInterfaces():
    eth = {
        "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
        "Name": "Ethernet Interface Collection",
        "Description": "System NICs on Raspberry Pi",
        "Members@odata.count": readings.eth_count(),
        "Members": readings.eth_members(), # Dicionário
        "Oem": {},
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/EthernetInterfaces/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return eth

def dynamic_eth_funcs():
    systems_eth_endpoint_functions = []
    interface_counter = 1

    for member in readings.eth_names():

        def bind_interface_function():
            iface_name = deepcopy(member)
            iface_number = str(deepcopy(interface_counter))
            def interface_function():
                stats = readings.eth_stats(iface_name)

                interface = {
                    "@odata.type": "#EthernetInterface.v1_0_2.EthernetInterface",
                    "Id": iface_name,
                    "Name": "Ethernet Interface",
                    "Description": "System NIC " + iface_number,
                    "Status": {
                        "State": stats['state'],
                        "Health": "OK"
                    },
                    "FactoryMacAddress": stats['mac_address'],
                    "MacAddress": stats['mac_address'],
                    "SpeedMbps": stats['speed_mbps'],
                    "FullDuplex": stats['full_duplex'],
                    "IPv6DefaultGateway": stats['ipv6_gateway'],
                    "NameServers": stats['dns'],
                    "IPv4Addresses": stats['ipv4_addresses'],
                    "IPv6Addresses": stats['ipv6_addresses'],
                    "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/EthernetInterfaces/Members/$entity",
                    "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces/" + iface_name,
                    "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
                }
                return interface
            interface_function.__name__ = iface_name
            return interface_function

        systems_eth_endpoint_functions.append(bind_interface_function())
        interface_counter += 1
    return systems_eth_endpoint_functions

# SYSTEMS ID SIMPLE STORAGE

def get_systems_id_simpleStorage():
    storage = {
        "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
        "Name": "Simple Storage Collection",
        "Members@odata.count": readings.storage_count(),
        "Members": readings.storage_members(),
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/SimpleStorage/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/SimpleStorage",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return storage

def dynamic_storage_funcs():
    systems_storage_endpoint_functions = []
    storage_counter = 1

    for member in readings.storage_names():

        def bind_storage_function():
            str_name = deepcopy(member)
            str_number = str(deepcopy(storage_counter))
            def storage_function():
                #stats = readings.storage_stats(str_name)

                storage_device = {
                    "@odata.type": "#SimpleStorage.v1_0_2.SimpleStorage",
                    "Id": str_name,
                    "Name": "Simple Storage Controller",
                    "Description": "System SATA",
                    "Status": {
                        "State": "Enabled",
                        "Health": "OK",
                        "HealthRollUp": "Degraded"
                    },
                    "Devices": [
                        {
                            "Name": "SATA Bay 1",
                            "Manufacturer": "Contoso",
                            "Model": "3000GT8",
                            "CapacityBytes": 8000000000000,
                            "Status": {
                                "State": "Enabled",
                                "Health": "OK"
                            }
                        },
                    ],
                    "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/SimpleStorage/Members/$entity",
                    "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/SimpleStorage/" + str_name,
                    "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
                }
                
                return storage_device
            storage_function.__name__ = str_name
            return storage_function

        systems_storage_endpoint_functions.append(bind_storage_function())
        storage_counter += 1
    return systems_storage_endpoint_functions
