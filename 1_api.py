from flask import Flask
import json
from flask import Flask, request
import psutil as ps
from flask import jsonify
my_app = Flask(__name__)


@my_app.route('/api/v1/vms/usage/1', methods = ['GET'])

def getUtilize():
    data={
        "CPU":getcpu(),
        "MEM":getmem(),
        "Disk":getdisk()
    }
    return jsonify(data),200

def getcpu():
    cpu = ps.cpu_percent(1)
    return "%s" %(cpu)

def getmem():
    mem = float(ps.virtual_memory().used)
    mem_real = (mem*1.0)/(1024**3)
    return "{}".format(mem_real)

def getdisk():
    disk = ps.disk_usage('.').percent
    return "%s" %(disk)

my_app.run(host="127.0.0.1")