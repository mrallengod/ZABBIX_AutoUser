import pycurl
from StringIO import StringIO
import json


#
def userLogin(user, password):

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["method"] = "user.login"
    query_obj["jsonrpc"] = "2.0"

    params = {}
    params["user"] = user
    params["password"] = password

    query_obj["params"] = params
    c.setopt(c.POSTFIELDS, json.dumps(query_obj))

    c.setopt(c.WRITEDATA, buffer)
    c.perform()

    c.close()

    # need error handle
    token = json.loads(buffer.getvalue())['result']
    # return token only
    return token


def userLogout(token):

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, my_url)
    c.setopt(c.HTTPHEADER, my_header)

    query_obj = {}
    query_obj["id"] = 1
    query_obj["method"] = "user.logout"
    query_obj["jsonrpc"] = "2.0"
    query_obj["params"] = []

    c.setopt(c.POSTFIELDS, json.dumps(query_obj))
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    # need error handle
    result = json.loads(buffer.getvalue())['result']
    # return token only
    return result
