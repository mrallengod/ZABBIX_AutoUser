import pycurl
from StringIO import StringIO
import json
import UserLogin.py

def getUserId(token,username):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "user.get"

    params = {}
    params["output"] = ["userid"]
    params["filter"] = {"alias": username}

    query_obj["params"] = params

    # tmp = '{"jsonrpc":"2.0","method":"host.get","params":{"groupids":"47"},"auth":"' + ret['result']+ '","id":1}'
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    userid = json.loads(buffer.getvalue())['result'][0]['userid']
    return userid


def createUser(token, usrgrpid, username, name, surname, mailaddr):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["auth"] = token
    query_obj["jsonrpc"] = "2.0"
    query_obj["method"] = "user.create"

    params = {}
    params["alias"] = username
    params["name"] = name
    params["surname"] = surname
    params["usrgrps"] = {"usrgrpid": usrgrpid}
    params["type"] = "1"
    params["user_medias"] = {
        "mediatypeid": "1",
        "sendto": mailaddr,
        "active": 0,
        "severity": 63,
        "period": "1-7,00:00-24:00"
    }
    query_obj["params"] = params
    tmp = json.dumps(query_obj)
    c.setopt(c.POSTFIELDS, tmp)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    userid = json.loads(buffer.getvalue())['result']
    return userid
