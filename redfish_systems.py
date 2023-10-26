import readings
import psutil
import json
import os
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict

lsblk = Popen(['lsblk', '-f', '--raw'], stdout=PIPE)
disk_info = check_output(["grep", "ext4"], stdin=lsblk.stdout).decode("utf-8") #paras raspberry usar "rootfs"
UUID = disk_info.split()[3] #para raspberry usar [3]

CHASSIS_ID = 0
SYSTEM_ID = 1
MANAGER_ID = 2
MAC_ADDRESS_1 = "123456789A"
MAC_ADDRESS_2 = "23456789AB"

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
            "TotalSystemMemoryGiB": str(96),
            "Status": {
                "State": "Enabled",
                "Health": "OK",
                "HealthRollUp": "OK"
            }
        },
        "Bios": {
            "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/BIOS"
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
            "@odata.id:" "/redfish/v1/Systems/" + readings.boot_id() + "/LogServices"
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
                "target": "/redfish/v1/Systems/" + readings.boot_id() + "/Actions/ComputerSystem.Reset",
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
                    "target": "/redfish/v1/Systems/" + readings.boot_id() + "/Oem/Contoso/Actions/Contoso.Reset"
                }
            }
        },
        "@odata.context": "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id(),
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return systems_id

# SYSTEMS ID BIOS

def get_systems_id_bios():
    system_bios = {
        "@odata.type": "#Bios.v1_0_0.Bios",
        "Id": "BIOS",
        "Name": "BIOS Configuration Current Settings",
        "AttributeRegistry": "BiosAttributeRegistryP89.v1_0_0",
        "Attributes": {
            "AdminPhone": "",
            "BootMode": "Uefi",
            "EmbeddedSata": "Raid",
            "NicBoot1": "NetworkBoot",
            "NicBoot2": "Disabled",
            "PowerProfile": "MaxPerf",
            "ProcCoreDisable": 0,
            "ProcHyperthreading": "Enabled",
            "ProcTurboMode": "Enabled",
            "UsbControl": "UsbEnabled"
        },
        "@Redfish.Settings": {
            "@odata.type": "#Settings.v1_0_0.Settings",
            "ETag": "9234ac83b9700123cc32",
            "Messages": [
                {
                    "MessageId": "Base.1.0.SettingsFailed",
                    "RelatedProperties": [
                        "#/Attributes/ProcTurboMode"
                    ]
                }
            ],
            "SettingsObject": {
                "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/BIOS/Settings"
            },
            "Time": "2016-03-07T14:44.30-05:00"
        },
        "Actions": {
            "#Bios.ResetBios": {
                "target": "/redfish/v1/Systems/" + readings.boot_id() + "/BIOS/Actions/Bios.ResetBios"
            },
            "#Bios.ChangePassword": {
                "target": "/redfish/v1/Systems/" + readings.boot_id() + "/BIOS/Actions/Bios.ChangePassword"
            }
        },
        "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/BIOS",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return system_bios

def get_systems_id_bios_settings():
    settings = {
        "@odata.type": "#Bios.v1_0_0.Bios",
        "Id": "Settings",
        "Name": "BIOS Configuration Pending Settings",
        "AttributeRegistry": "BiosAttributeRegistryP89.v1_0_0",
        "Attributes": {
            "AdminPhone": "(404) 555-1212",
            "BootMode": "Uefi",
            "EmbeddedSata": "Ahci",
            "NicBoot1": "NetworkBoot",
            "NicBoot2": "NetworkBoot",
            "PowerProfile": "MaxPerf",
            "ProcCoreDisable": 0,
            "ProcHyperthreading": "Enabled",
            "ProcTurboMode": "Disabled",
            "UsbControl": "UsbEnabled"
        },
        "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/BIOS/Settings",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return settings

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
        "ProcessorArchitecture":readings.cpu_arch(),
        "InstructionSet": "x86-64",
        "Manufacturer": "Intel(R) Corporation",
        "Model": readings.cpu_model(),
        "ProcessorID": {
            "VendorID": readings.cpu_vendor,
            "IdentificationRegisters": "0x34AC34DC8901274A",
            "EffectiveFamily": "0x42",
            "EffectiveModel": "0x61",
            "Step": "0x1",
            "MicrocodeInfo": "0x429943"
        },
        "MaxSpeedMHz": readings.cpu_freq(),
        "TotalCores": readings.cpu_cores(),
        "TotalThreads": readings.cpu_threads,
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
        "Members@odata.count": 4,
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
        "ErrorCorrection": "MultiBitECC",
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
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/Memory/DIMM1",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return ram

# SYSTEMS ID ETHERNET INTERFACES

def get_systems_id_ethernetInterfaces():
    eth = {
        "@odata.type": "#EthernetInterfaceCollection.EthernetInterfaceCollection",
        "Name": "Ethernet Interface Collection",
        "Description": "System NICs on Contoso Servers",
        "Members@odata.count": 2,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces/" + str(MAC_ADDRESS_1)
            },
            {
                "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces/" + str(MAC_ADDRESS_2)
            }
        ],
        "Oem": {},
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/EthernetInterfaces/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return eth

def get_systems_id_ethernetInterfaces_macAddress1():
    mac1 = {
        "@odata.type": "#EthernetInterface.v1_0_2.EthernetInterface",
        "Id": "1",
        "Name": "Ethernet Interface",
        "Description": "System NIC 1",
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "FactoryMacAddress": "12:44:6A:3B:04:11",
        "MacAddress": "12:44:6A:3B:04:11",
        "SpeedMbps": 1000,
        "FullDuplex": True,
        "HostName": "web483",
        "FQDN": "web483.contoso.com",
        "IPv6DefaultGateway": "fe80::3ed9:2bff:fe34:600",
        "NameServers": [
            "names.contoso.com"
        ],
        "IPv4Addresses": [
            {
                "Address": "192.168.0.10",
                "SubnetMask": "255.255.252.0",
                "AddressOrigin": "Static",
                "Gateway": "192.168.0.1"
            }
        ],
        "IPv6Addresses": [
            {
                "Address": "fe80::1ec1:deff:fe6f:1e24",
                "PrefixLength": 64,
                "AddressOrigin": "Static",
                "AddressState": "Preferred"
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/EthernetInterfaces/Members/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces/" + str(MAC_ADDRESS_1),
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return mac1

def get_systems_id_ethernetInterfaces_macAddress2():
    mac2 = {
        "@odata.type": "#EthernetInterface.v1_0_2.EthernetInterface",
        "Id": "2",
        "Name": "Ethernet Interface",
        "Description": "System NIC 2",
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "PermanentMACAddress": "12:44:6A:3B:88:90",
        "MACAddress": "AA:BB:CC:DD:EE:00",
        "SpeedMbps": 1000,
        "FullDuplex": True,
        "HostName": "backup-web483",
        "FQDN": "backup-web483.contoso.com",
        "IPv6DefaultGateway": "fe80::3ed9:2bff:fe34:600",
        "NameServers": [
            "names.contoso.com"
        ],
        "IPv4Addresses": [
            {
                "Address": "192.168.0.11",
                "SubnetMask": "255.255.255.0",
                "AddressOrigin": "Static",
                "Gateway": "192.168.0.1"
            }
        ],
        "IPv6Addresses": [
            {
                "Address": "fe80::1ec1:deff:fe6f:1e33",
                "PrefixLength": 64,
                "AddressOrigin": "Static",
                "AddressState": "Preferred"
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/EthernetInterfaces/Members/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/EthernetInterfaces/" + str(MAC_ADDRESS_2),
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return mac2

# SYSTEMS ID SIMPLE STORAGE

def get_systems_id_simpleStorage():
    storage = {
        "@odata.type": "#SimpleStorageCollection.SimpleStorageCollection",
        "Name": "Simple Storage Collection",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/SimpleStorage/1"
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/SimpleStorage/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/SimpleStorage",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return storage

def get_systems_id_simpleStorage_1():
    storage_1 = {
        "@odata.type": "#SimpleStorage.v1_0_2.SimpleStorage",
        "Id": "1",
        "Name": "Simple Storage Controller",
        "Description": "System SATA",
        "UEFIDevicePath": "Acpi(PNP0A03,0)/Pci(1F|1)/Ata(Primary,Master)/HD(Part3, Sig00110011)",
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
            {
                "Name": "SATA Bay 2",
                "Manufacturer": "Contoso",
                "Model": "3000GT7",
                "CapacityBytes": 4000000000000,
                "Status": {
                    "State": "Enabled",
                    "Health": "Degraded"
                }
            },
            {
                "Name": "SATA Bay 3",
                "Status": {
                    "State": "Absent"
                }
            },
            {
                "Name": "SATA Bay 4",
                "Status": {
                    "State": "Absent"
                }
            }
        ],
        "@odata.context": "/redfish/v1/$metadata#Systems/Members/" + readings.boot_id() + "/SimpleStorage/Members/$entity",
        "@odata.id": "/redfish/v1/Systems/" + readings.boot_id() + "/SimpleStorage/1",
        "@Redfish.Copyright": "Copyright 2014-2016 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright."
    }
    return storage_1