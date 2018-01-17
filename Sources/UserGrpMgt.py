import pycurl
from StringIO import StringIO
import json
import UserLogin


def getUserGrpId(token, grpname):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "usergroup.get"

    params = {}
    params["output"] = ["usrgrpid"]
    params["filter"] = {"name": grpname}

    query_obj["params"] = params

    # tmp = '{"jsonrpc":"2.0","method":"host.get",
    # " params":{"groupids":"47"},"auth":"' + ret['result']+ '","id":1}'
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    usergrpid = json.loads(buffer.getvalue())['result'][0]['usrgrpid']
    return usergrpid


def createUserGrpId(token, grpname, grpid):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "usergroup.create"

    params = {}
    params["output"] = ["usrgrpid"]
    params["name"] = grpname
    params["rights"] = {
        "permission": 0,
        "id": grpid
    }

    query_obj["params"] = params

    # tmp = '{"jsonrpc":"2.0","method":"host.get",\
    # "params":{"groupids":"47"},"auth":"' + ret['result']+ '","id":1}'
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    usergrpid = json.loads(buffer.getvalue())['result'][0]['usrgrpid']
    return usergrpid
