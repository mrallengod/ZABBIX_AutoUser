import pycurl
from StringIO import StringIO
import json


def getHostGroupId(token, grpname):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "hostgroup.get"
    params = {}
    params["output"] = ["groupid"]
    params["filter"] = {"name": grpname}

    query_obj["params"] = params

    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    try:
        grpid = json.loads(buffer.getvalue())['result'][0]['groupid']
    except Exception, e:
        print Exception, ":", e
    return grpid


def createGroup(token, grpname):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "hostgroup.create"
    params = {}
    params["name"] = grpname

    query_obj["params"] = params

    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    try:
        grpid = json.loads(buffer.getvalue())['result'][0]['groupids']
    except e:
        print "run except"
        print e
    return grpid


# mass add hosts into Hostgroup.
def massAddHostGroup(token, grpids, hostids):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "hostgroup.massadd"
    params = {}
    params["groups"] = grpids
    params["hostids"] = hostids

    query_obj["params"] = params

    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    try:
        grpid = json.loads(buffer.getvalue())['result'][0]['groupids']
    except e:
        print "run except"
        print e
    return grpid


# mass update hosts into Hostgroup.
def massUpdateHostGroup(token, grpids, hostids):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "hostgroup.massupdate"
    params = {}
    params["groups"] = grpids
    params["hostids"] = hostids

    query_obj["params"] = params

    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    try:
        grpid = json.loads(buffer.getvalue())['result'][0]['groupids']
    except e:
        print "run except"
        print e
    return grpid
