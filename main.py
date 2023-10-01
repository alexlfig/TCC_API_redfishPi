
from flask import Flask
import psutil
import os
import io

app = Flask(__name__)

@app.route('/')#decorator
def index():
    return'mostrá infomação'
    #return '@odata.context": "/redfish/v1/$metadata#ServiceRoot",'

@app.route('/redfish/v1/', methods=['GET'])

def get_systems():  
    systemInfo = {
        'freqCpu': psutil.cpu_freq()
    }
    return '<a href="/redfish/v1/memory">Acesse o Google</a>'
    #return systemInfo

@app.route('/redfish/v1/memory', methods=['GET'])
def get_memory():
    #Implemente a lógica para obter informações do sistema usando Redfish aqui
    return 'Informações de memoria'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
