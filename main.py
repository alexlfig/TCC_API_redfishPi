import readings
from flask import Flask
from collections import OrderedDict
from subprocess import check_output, Popen, PIPE
import redfish_root
import redfish_accountservice
import redfish_chassis
import redfish_eventservice
import redfish_registries
import redfish_sessionservice
import redfish_systems
import redfish_taskservice
import psutil
import json
import os

#chassis_id = check_output(["cat", "/sys/firmware/devicetree/base/serial-number"]).decode("utf-8").replace('\u0000', '')

app = Flask(__name__)

@app.route('/')  #decorator
def index():
    return'Bem Vindo a RedfishPi'
    #return '@odata.context": "/redfish/v1/metadataServiceRoot",'

@app.route('/redfish/v1/', methods=['GET'])
def get_v1():  
    return redfish_root.get_redfish_v1()
    
#--------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/Chassis', methods=['GET'])
def get_Chassis():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_chassis.get_chassis()

@app.route('/redfish/v1/Chassis/' + readings.machine_id(), methods=['GET']) #tirar as aspas
def get_chassis_id():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_chassis.get_chassis_id()

#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/Systems', methods=['GET'])
def get_Systems():
    return redfish_systems.get_systems()

@app.route('/redfish/v1/Systems/' + readings.boot_id(), methods=['GET'])  # verificar possibilidade de excluir  
def get_Systems_id():
    return redfish_systems.get_systems_id()
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/TaskService', methods=['GET'])
def get_TaskService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_taskservice.get_taskService()
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/SessionService', methods=['GET'])
def get_SessionService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_sessionservice.get_sessionService()
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/AccountService', methods=['GET'])
def get_AccountService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_accountservice.get_accountService()
#------------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/EventService', methods=['GET'])
def get_EventService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_eventservice.get_eventService()
#------------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/Registries', methods=['GET'])
def get_Registries():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_registries.get_registries()
#------------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/CompositionService', methods=['GET'])
def get_CompositionService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_accountservice.get_accountService()
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
