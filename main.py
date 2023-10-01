
from flask import Flask
import psutil
import json


app = Flask(__name__)

@app.route('/')#decorator
def index():
    return'Bem Vindo a RedfishPi'
    #return '@odata.context": "/redfish/v1/$metadata#ServiceRoot",'

@app.route('/redfish/v1/', methods=['GET'])
def get_v1():  
    raizV1 = {
        'Chassis': '<a href=/redfish/v1/Chassis>/redfish/v1/Chassis</a>'
    }
    v1 = json.dumps(raizV1)
    #return '<a href="/redfish/v1/memory">Acesse o Google</a>'
    return v1

@app.route('/redfish/v1/Chassis', methods=['GET'])
def get_Chassis():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return 'Informações de Chassis'

@app.route('/redfish/v1/Systems', methods=['GET'])
def get_Systems():
    systemInfo = {
        'memory': '<a href=/redfish/v1/memory>/redfish/v1/memory</a>',
        'freqCpu': psutil.cpu_freq(),
        'Processors': '<a href=/redfish/v1/Processors>/redfish/v1/Processors</a>',
    }
    v1 = json.dumps(systemInfo)
    #return '<a href="/redfish/v1/memory">Acesse o Google</a>'
    return v1

@app.route('/redfish/v1/memory', methods=['GET'])
def get_memory():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return 'Informações de memoria'

@app.route('/redfish/v1/Processors', methods=['GET'])
def get_processors():
    processorsInfo = {
        'Processors': psutil.cpu_count(),
    }
    return processorsInfo



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
