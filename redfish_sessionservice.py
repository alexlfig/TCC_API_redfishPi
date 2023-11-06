import readings
import psutil
from datetime import datetime
from copy import deepcopy #Usado para persistência dos dados na função geradora de funções

def get_sessionService():
    session_service = {
        "@odata.context": "/redfish/v1/$metadata#SessionService",
        "@odata.id": "/redfish/v1/SessionService",
        "@odata.type": "#Session.0.94.0.SessionCollection",
        "Name": "Session Collection",
        "Description": "Manager User Sessions",
        "Modified": datetime.now().isoformat(),
        "Links": {
            "Members@odata.count": readings.session_count(),
            "Members": readings.session_members(),
        }
    }
    return session_service

def dynamic_session_funcs():
    session_funcs = []
    session_counter = 0

    for session in psutil.users():

        def bind_session_function():
            username = deepcopy(session[0])
            usernumber = str(deepcopy(session_counter))
            def session_function():
                session_dict = {
                    "@odata.context": "/redfish/v1/$metadata/SessionService/Links/Members/$entity",
                    "@odata.id": "/redfish/v1/SessionService/" + username,
                    "@odata.type": "#SessionService.0.94.0.Session",
                    "Id": username,
                    "Description": "User Session",
                    "Modified": datetime.fromtimestamp(session[3]).isoformat(),
                    "UserName": username,
                    "Oem": {}
                }
                return session_dict
            session_function.__name__ = username
            return session_function

        session_funcs.append(bind_session_function())
        session_counter += 1
    return session_funcs