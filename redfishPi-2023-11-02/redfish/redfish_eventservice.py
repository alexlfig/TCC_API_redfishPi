import readings
import psutil
import json
import os
from subprocess import check_output, Popen, PIPE
from collections import OrderedDict

def get_eventService():
    event_service = {
        "@Redfish.Copyright": "Copyright 2014-2019 DMTF. All rights reserved.",
        "@odata.context": "/redfish/v1/$metadata#EventService",
        "@odata.id": "/redfish/v1/EventService",
        "@odata.type": "#EventService.1.0.0.EventService",
        "Id": "EventService",
        "Name": "Event Service",
        "Status": {
            "State": "Enabled",
            "Health": "OK"
        },
        "ServiceEnabled": "True",
        "DeliveryRetryAttempts": 3,
        "DeliveryRetryIntervalInSeconds": 60,
        "EventTypesForSubscription": [
            "StatusChange",
            "ResourceUpdated",
            "ResourceAdded",
            "ResourceRemoved",
            "Alert"
        ],
        "Subscriptions": {
            "@odata.id": "/redfish/v1/EventService/Subscriptions",
        },
        "Actions": {
            "#EventService.SendTestEvent": {
                "target": "/redfish/v1/EventService/Actions/EventService.SendTestEvent",
                "EventType@Redfish.AllowableValues": [
                    "StatusChange",
                    "ResourceUpdated",
                    "ResourceAdded",
                    "ResourceRemoved",
                    "Alert"
                ]
            },
            "Oem": {}
        },
        "Oem": {}
    }
    return event_service

def get_eventService_subscriptions():
    return get_eventService()