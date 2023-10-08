import psutil
import json
import os

LOGIN_ID = 5

def get_sessionService():
    session_service = {
        "@odata.context": "/redfish/v1/$metadata#SessionService",
        "@odata.id": "/redfish/v1/SessionService",
        "@odata.type": "#Session.0.94.0.SessionCollection",
        "Name": "Session Collection",
        "Description": "Manager User Sessions",
        "Modified": "2013-01-31T23:45:08+00:00",
        "Links": {
            "Members@odata.count": 1,
            "Members": [
                {
                    "@odata.id": "/redfish/v1/SessionService/" + str(LOGIN_ID)
                }
            ]
        }
    }
    return session_service

def get_sessionService_id():
    session_service_id = {
        "@odata.context": "/redfish/v1/$metadata/SessionService/Links/Members/$entity",
        "@odata.id": "/redfish/v1/SessionService/" + str(LOGIN_ID),
        "@odata.type": "#SessionService.0.94.0.Session",
        "Id": "Administrator1",
        "Name": "User Session",
        "Description": "Manager User Session",
        "Modified": "2013-01-31T23:45:08+00:00",
        "UserName": "Administrator",
        "Oem": {}
    }
    return session_service_id