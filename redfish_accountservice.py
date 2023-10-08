import psutil
import json
import os

ACCOUNT_ID = 6
ROLE_ID = 7

def get_accountService():
    account_service = {
        "@odata.context": "/redfish/v1/$metadata#AccountService",
        "@odata.id": "/redfish/v1/AccountService",
        "@odata.type": "#AccountService.0.94.0.AccountService",
        "Id": "AccountService",
        "Name": "Account Service",
        "Description": "BMC User Accounts",
        "Modified": "2036-09-11T14:17:21+00:00",
        "AuthFailureLoggingThreshold": 3,
        "MinPasswordLength": 8,
        "Links": {
            "Accounts": {
                "@odata.id": "/redfish/v1/AccountService/Accounts"
            },
            "Roles": {
                "@odata.id": "/redfish/v1/AccountService/Roles"
            }
        }
    }
    return account_service

def get_accountService_id():
    account_service_id = {
        "@odata.context": "/redfish/v1/$metadata#AccountService/Links/Members/Accounts/Links/Members/$entity",
        "@odata.id": "/redfish/v1/AccountService/Accounts/" + str(ACCOUNT_ID),
        "@odata.type": "#AccountService.0.94.0.ManagerAccount",
        "Id": "1",
        "Name": "User Account",
        "Modified": "2013-09-11T17:03:55+00:00",
        "Description": "User Account",
        "Password": "Password",
        "UserName": "Administrator",
        "Locked": "False",
        "Enabled": "True",
        "RoleId": "Admin",
        "Links": {
            "Role": {
                "@odata.id": "/redfish/v1/AccountService/Roles/Admin"
            }
        }
    }
    return account_service_id

def get_accountService_roles():
    roles = {
        "@odata.context": "/redfish/v1/$metadata#AccountService/Links/Members/Roles/$entity",
        "@odata.id": "/redfish/v1/AccountService/Roles",
        "@odata.type": "#RoleCollection.RoleCollection",
        "Name": "Roles Collection",
        "Modified": "2012-03-07T14:44",
        "Links": {
            "Members@odata.count": 3,
            "Members": [
                {
                    "@odata.id": "/redfish/v1/AccountService/Roles/Admin"
                },
                {
                    "@odata.id": "/redfish/v1/AccountService/Roles/Operator"
                },
                {
                    "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnlyUser"
                }
            ]
        }
    }
    return roles

def get_accountService_roles_admin():
    admin = {
        "@odata.context": "/redfish/v1/$metadata#AccountService/Links/Members/Roles/Links/Members/$entity",
        "@odata.id": "/redfish/v1/AccountService/Roles/Admin",
        "@odata.type": "#Role.1.0.0.Role",
        "Id": "Admin",
        "Name": "User Role",
        "Modified": "2013-09-11T17:03:55+00:00",
        "Description": "Admin User Role",
        "IsPredefined": "True",
        "AssignedPrivileges": [
            "Login",
            "ConfigureManager",
            "ConfigureUsers",
            "ConfigureSelf",
            "ConfigureComponents"
        ],
        "OEMPrivileges": [
            "OemClearLog",
            "OemPowerControl"
        ]
    }
    return admin

def get_accountService_roles_operator():
    operator = {
        "@odata.context": "/redfish/v1/$metadata#AccountService/Links/Members/Roles/Links/Members/$entity",
        "@odata.id": "/redfish/v1/AccountService/Roles/Operator",
        "@odata.type": "#Role.1.0.0.Role",
        "Id": "Operator",
        "Name": "User Role",
        "Modified": "2013-09-11T17:03:55+00:00",
        "Description": "Operator User Role",
        "IsPredefined": "True",
        "AssignedPrivileges": [
            "Login",
            "ConfigureSelf",
            "ConfigureComponents"
        ],
        "OEMPrivileges": []
    }
    return operator

def get_accountService_roles_readOnlyUser():
    ro_user = {
        "@odata.context": "/redfish/v1/$metadata#AccountService/Links/Members/Roles/Links/Members/$entity",
        "@odata.id": "/redfish/v1/AccountService/Roles/ReadOnlyUser",
        "@odata.type": "#Role.1.0.0.Role",
        "Id": "ReadOnlyUser",
        "Name": "User Role",
        "Modified": "2013-09-11T17:03:55+00:00",
        "Description": "ReadOnlyUser User Role",
        "IsPredefined": "True",
        "AssignedPrivileges": [
            "Login"
        ],
        "OEMPrivileges": []
    }
    return ro_user