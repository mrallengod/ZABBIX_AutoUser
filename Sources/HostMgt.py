import pycurl
from StringIO import StringIO
import json
import UserLogin
import argparse


# login to retrieve token
def getHostId(token, hostname):

    # get machine id list from vc02 group
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "host.get"

    params = {}
    params["output"] = ["hostid"]
    params["filter"] = {"name": hostname}

    query_obj["params"] = params

    # tmp = '{"jsonrpc":"2.0","method":"host.get","params":{"groupids":"47"},"auth":"' + ret['result']+ '","id":1}'
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    host_ids = json.loads(buffer.getvalue())['result'][0]['hostid']
    return host_ids


def getInventory(token, hostname):

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "host.get"

    params = {}
    params["output"] = ["host"]
    params["filter"] = {"host": hostname}
    params["selectInventory"] = ["contact"]

    query_obj["params"] = params
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    host_inventory = json.loads(buffer.getvalue())['result']
    return host_inventory


def updateInventory(token, hostid, value):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "host.update"

    params = {}
    params["hostid"] = hostid
#    params["inventory_mode"] = 0
    params["inventory"] = {"contact": value}

    query_obj["params"] = params
    print query_obj
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    print buffer.getvalue()
    host_inventory = json.loads(buffer.getvalue())['result']
    return host_inventory
