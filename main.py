import readings
from flask import Flask
from flask import abort
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
def get_chassis():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_chassis.get_chassis()

@app.route('/redfish/v1/Chassis/' + readings.machine_id(), methods=['GET']) #tirar as aspas
def get_chassis_id():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_chassis.get_chassis_id()

#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/Systems', methods=['GET'])
def get_systems():
    return redfish_systems.get_systems()

@app.route('/redfish/v1/Systems/' + readings.boot_id(), methods=['GET'])  # verificar possibilidade de excluir  
def get_systems_id():
    return redfish_systems.get_systems_id()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/Processors', methods=['GET'])
def get_systems_id_processors():
    return redfish_systems.get_systems_id_processors()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/Processors/CPU1', methods=['GET'])
def get_systems_id_processors_cpu1():
    return redfish_systems.get_systems_id_processors_cpu1()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/Memory', methods=['GET'])
def get_systems_id_memory():
    return redfish_systems.get_systems_id_memory()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/Memory/DIMM', methods=['GET'])
def get_systems_id_memory_dimm():
    return redfish_systems.get_systems_id_memory_dimm()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/EthernetInterfaces', methods=['GET'])
def get_systems_id_ethernetInterfaces():
    return redfish_systems.get_systems_id_ethernetInterfaces()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/EthernetInterfaces/<iface>', methods=['GET'])
def get_systems_id_ethernetInterfaces_iface(iface):
    funcs = redfish_systems.dynamic_eth_funcs()
    for func in funcs:
        if func.__name__ == iface:
            return func()
    abort(404)
    
@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/SimpleStorage', methods=['GET'])
def get_systems_id_simpleStorage():
    return redfish_systems.get_systems_id_simpleStorage()

@app.route('/redfish/v1/Systems/' + readings.boot_id() + '/SimpleStorage/<device>', methods=['GET'])
def get_systems_id_simpleStorage_device(device):
    funcs = redfish_systems.dynamic_storage_funcs()
    for func in funcs:
        if func.__name__ == device:
            return func()
    abort(404)

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
