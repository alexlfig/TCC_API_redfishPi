import readings
import psutil
import json
import os
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict

REGISTRY_ID = "Base.1.0.0"

def get_registries():
    registries = {
        "@Redfish.Copyright": "Copyright 2014-2019 DMTF. All rights reserved.",
        "@odata.context": "/redfish/v1/$metadata#MessageRegistryFileCollection.MessageRegistryFileCollection",
        "@odata.id": "/redfish/v1/Registries",
        "@odata.type": "#MessageRegistryFileCollection.MessageRegistryFileCollection",
        "Name": "Registry File Collection",
        "Description": "Registry Repository",
        "Members@odata.count": 1,
        "Members": [
            {
                "@odata.id": "/redfish/v1/Registries/" + str(REGISTRY_ID)
            }
        ]
    }
    return registries

def get_registries_id():
    registries_id = {
        "@Redfish.Copyright": "Copyright 2014-2019 DMTF. All rights reserved.",
        "@odata.context": "/redfish/v1/$metadata#Registries/Members/$entity",
        "@odata.id": "/redfish/v1/Registries/" + str(REGISTRY_ID),
        "@odata.type": "#MessageRegistryFile.1.0.0.MessageRegistryFile",
        "Id": str(REGISTRY_ID),
        "Name": "Base Message Registry File",
        "Description": "Base Message Registry File locations",
        "Languages": [
            "en"
        ],
        "Registry": "Base.1.0",
        "Location": [
            {
                "Language": "en",
                "ArchiveUri": "/<someuri>/Registries.gz",
                "PublicationUri": "http://redfish.dmtf.org/registries/Base.1.0.0.json",
                "ArchiveFile": "Base.1.0.0.json"
            },
            {
                "Language": "zh",
                "ArchiveUri": "/<someuri>/Registries.zh.gz",
                "PublicationUri": "http://redfish.dmtf.org/registries/Base.1.0.0.zh.json",
                "ArchiveFile": "Base.1.0.0.zh.json"
            },
            {
                "Language": "xy",
                "Uri": "/<someLocalUri>/Base.1.0.0.xy.json",
                "PublicationUri": "http://redfish.dmtf.org/registries/Base.1.0.0.xy.json"
            }
        ],
        "Oem": {}
    }
    return registries_id
    