import UserLogin
import HostMgt
import UserMgt
import InventoryMgt

if __name__ == "__main__":

    my_url = 'http://10.67.51.200/api_jsonrpc.php'
    my_header = ['Content-Type: application/json']
    adminuser = "Allan"
    adminpwd = "Foxconn88"

    token = UserLogin.login(adminuser, adminpwd)
    hostid = HostMgt.getHostId(token, "vm-vc02-SR1779")
    # print hostid
    host_inventory = updateInventory(token, hostid, "Allen Yan")
    print host_inventory
    # print getInventory(token,"vm-vc02-SR1779")

    userlogout(token)
