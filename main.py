from flask import Flask
from flask import abort
import readings
import redfish_root
import redfish_chassis
import redfish_sessionservice
import redfish_systems
import redfish_taskservice

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

@app.route('/redfish/v1/Chassis/' + readings.machine_id() + '/ThermalSubsystem', methods=['GET'])
def get_chassis_id_thermalSubsystem():
    return redfish_chassis.get_thermalSubsystem()

@app.route('/redfish/v1/Chassis/' + readings.machine_id() + '/ThermalSubsystem/ThermalMetrics', methods=['GET'])
def get_chassis_id_thermalMetrics():
    return redfish_chassis.get_thermalMetrics()

@app.route('/redfish/v1/Chassis/' + readings.machine_id() + '/PowerSubsystem', methods=['GET'])
def get_chassis_id_powerSubsystem():
    return redfish_chassis.get_powerSubsystem()

@app.route('/redfish/v1/Chassis/' + readings.machine_id() + '/Sensors', methods=['GET'])
def get_chassis_id_sensors():
    return redfish_chassis.get_sensors()
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/Systems', methods=['GET'])
def get_systems():
    return redfish_systems.get_systems()

@app.route('/redfish/v1/Systems/' + readings.machine_id(), methods=['GET'])  # verificar possibilidade de excluir  
def get_systems_id():
    return redfish_systems.get_systems_id()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/Processors', methods=['GET'])
def get_systems_id_processors():
    return redfish_systems.get_systems_id_processors()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/Processors/CPU1', methods=['GET'])
def get_systems_id_processors_cpu1():
    return redfish_systems.get_systems_id_processors_cpu1()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/Memory', methods=['GET'])
def get_systems_id_memory():
    return redfish_systems.get_systems_id_memory()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/Memory/DIMM', methods=['GET'])
def get_systems_id_memory_dimm():
    return redfish_systems.get_systems_id_memory_dimm()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/EthernetInterfaces', methods=['GET'])
def get_systems_id_ethernetInterfaces():
    return redfish_systems.get_systems_id_ethernetInterfaces()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/EthernetInterfaces/<iface>', methods=['GET'])
def get_systems_id_ethernetInterfaces_iface(iface):
    funcs = redfish_systems.dynamic_eth_funcs()
    for func in funcs:
        if func.__name__ == iface:
            return func()
    abort(404)
    
@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/SimpleStorage', methods=['GET'])
def get_systems_id_simpleStorage():
    return redfish_systems.get_systems_id_simpleStorage()

@app.route('/redfish/v1/Systems/' + readings.machine_id() + '/SimpleStorage/<device>', methods=['GET'])
def get_systems_id_simpleStorage_device(device):
    funcs = redfish_systems.dynamic_storage_funcs()
    for func in funcs:
        if func.__name__ == device:
            return func()
    abort(404)
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/SessionService', methods=['GET'])
def get_SessionService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_sessionservice.get_sessionService()

@app.route('/redfish/v1/SessionService/<username>', methods=['GET'])
def get_SessionService_User(username):
    funcs = redfish_sessionservice.dynamic_session_funcs()
    for func in funcs:
        if func.__name__ == username:
            return func()
    abort(404)
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/redfish/v1/TaskService', methods=['GET'])
def get_TaskService():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return redfish_taskservice.get_taskService()

@app.route('/redfish/v1/TaskService/<task>', methods=['GET'])
def get_TaskService_id(task):
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    funcs = redfish_taskservice.dynamic_task_funcs()
    for func in funcs:
        if func.__name__ == task:
            return func()
    abort(404)
#-------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
