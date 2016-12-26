þ
rt standard configs for redundant 
#WAN and FW link deployments on switch
p21 = "int g0/0/21"
p22 = "int g0/0/22"
p23 = "int g0/0/23"
p24 = "int g0/0/24"
des_fw = "description FW"
des_RA = "description Router_A"
des_RB = "description Router_B"
des_ISP = "description AT&T"
sw = "switchport"
axs = "switchport mode access"
trunk = "switchport mode trunk"
vlan_10 = "switchport access vlan 10"
vlan_11 = "switchport access vlan 11"
vlan_12 =  "switchport access vlan 12"
vlan_13 = "switchport access vlan 13"
enable = "no shut"

###Function that allows engineer to automate config
def port():
    a = int(input("Port Number: "))
    if a == 21:
        print(p21)
        print(des_fw)
        print(sw)
        print(axs)
        print(vlan_10)
        print(enable)
    elif a == 22:
        print(sw)
        print(axs)
        print(vlan_11)
        print(enable)
    elif a == 23:
        print(p23)
        print(des_RB)
        print(sw)
        print(trunk)
        print(enable)
    elif a == 24:
        print(p24)
        print(des_ISP)
        print(sw)
        print(axs)
        print(vlan_13)
        print(enable)
