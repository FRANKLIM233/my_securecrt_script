# $language = "Python"
# $interface = "1.0"

# -*- coding: utf-8 -*-
import io

crt.Screen.Synchronous = True
def MA5680t(port1,port2):
    f1 = io.open('logicID.txt','wb')
    f2 = io.open('count.txt','a')
    crt.Screen.Send("enable" + "\r\n")
    crt.Screen.WaitForString("enable" + "\r\n")
    crt.Screen.Send("scroll" + "\r\n")
    crt.Screen.WaitForString("scroll" + "\r\n")
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("\r\n")
    crt.Screen.Send("config" + "\r\n")
    crt.Screen.WaitForString("config" + "\r\n")

    crt.Screen.Send("display interface vlan199" + "\r\n")
    crt.Screen.WaitForString("display interface vlan199")
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    for info in arrCRPortInfo:
        if "Internet Address" in info:
            f1.write(str(info.split()[3])+'\r\n')
    f1.write(str(arrCRPortInfo[-1][:-8])+'\r\n')


    # slot = crt.Dialog.Prompt("input: Slot ", "slot:", "", False)
    # port = crt.Dialog.Prompt("input: port ", "port:", "", False)
    slot = port1
    port = port2
    crt.Screen.Send("interface epon 0/" + slot +  "\r\n")
    crt.Screen.WaitForString("interface epon 0/" + slot +  "\r\n")
    crt.Screen.Send("display port state " + port +  "\r\n")
    crt.Screen.WaitForString("display port state " + port +  "\r\n")
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    nLine = len(arrCRPortInfo)
    for arrinfo in arrCRPortInfo:
        if "power(dBm)" in arrinfo:
            transmit = arrinfo.split()
            transmit_power = transmit[-1]
            break
    f1.write('pon_transmit(dBm):'+ str(transmit_power)+'\r\n')
    f1.write('\r\n')
    value = float(float(transmit_power) - 28.5)
    f1.write('ID  '+'Power  '+'       logicID'+'\r\n')
    

    crt.Screen.Send("display ont optical-info " + port + " all" "\r\n")
    crt.Screen.WaitForString("display ont optical-info " + port + " all" "\r\n")
    powerInfo = crt.Screen.ReadString("#")
    arrpowerInfo = powerInfo.split("\n")
    powernLine = len(arrpowerInfo)
    receive_power = []
    problem_id = []
    for info in arrpowerInfo[4:powernLine-3]:
        power = info.split()
        if float(power[1])<value:
            problem_id.append(power[0])
            receive_power.append(power[1])
    # f2.write(str(len(problem_id))+'\r\n')
    crt.Screen.Send("quit"  +  "\r\n")
    crt.Screen.WaitForString("quit"  +  "\r\n")
    crt.Screen.Send("display current-configuration port 0/"  + slot +"/"+ port + "\r\n")
    crt.Screen.WaitForString("display current-configuration port 0/"  + slot +"/"+ port + "\r\n")
    logic_id = crt.Screen.ReadString("config]")
    arrlogic_id = logic_id.split("\n")
    logicnline = len(arrlogic_id)
    problem_logicid = []
    for logic in arrlogic_id[6:logicnline-2]:
        if "loid-auth" in logic:
            id = logic.split()
            if id[3] in problem_id:
                problem_logicid.append(id[5][1:-1])
    total = len(problem_logicid)
    for i in range(total):
        f1.write(str(problem_id[i])+'  '+str(receive_power[i])+'  '+str(problem_logicid[i])+'\r\n')
    f2.write(str(len(problem_id)).decode('utf8')+'\r\n')
    # f2.close()
    # crt.Dialog.Prompt("problem id:", "prompt", str(problem_id), False)
    # crt.Dialog.Prompt("logicID:", "prompt", str(problem_logicid), False)
    # crt.Dialog.Prompt("total:", "prompt", str(len(problem_id)), False)
    crt.Screen.Send("quit" + "\r\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send("quit" + "\n")
    crt.Screen.WaitForString("[n]:")
    crt.Screen.Send("y" + "\r\n")
    crt.Screen.WaitForString('请输入 : ')

    return f1,f2

def MA5800(port1,port2):
    f1 = io.open('logicID.txt','wb')
    f2 = io.open('count.txt','a')
    crt.Screen.Send("enable" + "\r\n")
    crt.Screen.WaitForString("enable")
    crt.Screen.Send("scroll" + "\r\n")
    crt.Screen.WaitForString("scroll")
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("\r\n")
    crt.Screen.Send("config" + "\r\n")
    crt.Screen.WaitForString("config")

    crt.Screen.Send("display interface vlan199" + "\r\n")
    crt.Screen.WaitForString("display interface vlan199")
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("\r\n")
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    for info in arrCRPortInfo:
        if "Internet Address" in info:
            f1.write(str(info.split()[3])+'\r\n')
    f1.write(str(arrCRPortInfo[-1][:-8])+'\r\n')

    # slot = crt.Dialog.Prompt("input: Slot ", "slot:", "", False)
    # port = crt.Dialog.Prompt("input: port ", "port:", "", False)
    slot = port1
    port = port2
    crt.Screen.Send("interface epon 0/" + slot +  "\r\n")
    crt.Screen.WaitForString("interface epon 0/" + slot)
    crt.Screen.Send("display port state " + port +  "\r\n")
    crt.Screen.WaitForString("display port state " + port )
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("\r\n")
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    nLine = len(arrCRPortInfo)
    for arrinfo in arrCRPortInfo:
        if "power(dBm)" in arrinfo:
            transmit = arrinfo.split()
            transmit_power = transmit[-1]
            break
    f1.write('pon_transmit(dBm):'+ str(transmit_power)+'\r\n')
    f1.write('\r\n')
    value = float(float(transmit_power) - 28.5)
    f1.write('ID  '+'Power  '+'       logicID'+'\r\n')

    crt.Screen.Send("display ont optical-info " + port + " all" + "\r\n")
    crt.Screen.WaitForString("display ont optical-info " + port + " all" )
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("\r\n")
    powerInfo = crt.Screen.ReadString("#")
    arrpowerInfo = powerInfo.split("\n")
    powernLine = len(arrpowerInfo)
    receive_power = []
    problem_id = []
    for info in arrpowerInfo[8:powernLine-3]:
        power = info.split()
        if float(power[1])<value:
            problem_id.append(power[0])
            receive_power.append(power[1])
    # f2.write(str(len(problem_id))+'\r\n')
    crt.Screen.Send("quit"  +  "\r\n")
    crt.Screen.WaitForString("quit")
    crt.Screen.Send("display current-configuration port 0/"  + slot +"/"+ port + "\r\n")
    crt.Screen.WaitForString("display current-configuration port 0/"  + slot +"/"+ port)
    crt.Screen.Send("\r\n")
    crt.Screen.WaitForString("\r\n")
    logic_id = crt.Screen.ReadString("config]")
    arrlogic_id = logic_id.split("\n")
    logicnline = len(arrlogic_id)
    problem_logicid = []
    for logic in arrlogic_id[10:logicnline-2]:
        if "loid-auth" in logic:
            id = logic.split()
            if id[3] in problem_id:
                problem_logicid.append(id[5][1:-1])
    total = len(problem_logicid)
    for i in range(total):
        f1.write(str(problem_id[i])+'  '+str(receive_power[i])+'  '+str(problem_logicid[i])+'\r\n')
    # crt.Dialog.Prompt("problem id:", "prompt", str(problem_id), False)
    # crt.Dialog.Prompt("logicID:", "prompt", str(problem_logicid), False)
    # crt.Dialog.Prompt("total:", "prompt", str(len(problem_id)), False)
    f2.write(str(len(problem_id)).decode('utf8')+'\r\n')
    # f2.close()
    crt.Screen.Send("quit\r\n")
    crt.Screen.WaitForString("#")
    crt.Screen.Send('quit\n')
    crt.Screen.WaitForString("  Check whether system data has been changed. Please save data before logout. Are you sure to log out? (y/n)[n]:")
    crt.Screen.Send("y" + '\n')
    crt.Screen.WaitForString('请输入 : ')
    return f1,f2

def ZTE300(port1,port2):
    f1 = io.open('logicID.txt','wb')
    f2 = io.open('count.txt','a')
    crt.Screen.Synchronous = True
    crt.Screen.Send("show interface vlan199" + "\r\n")
    crt.Screen.WaitForString("show interface vlan199")
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    for info in arrCRPortInfo:
        if "Internet address" in info:
            f1.write(str(info.split()[3])+'\r\n')
    f1.write(str(arrCRPortInfo[-1])+'\r\n')
    crt.Screen.Send("terminal length 0" + "\r\n")
    crt.Screen.WaitForString("terminal length 0")

    # slot = crt.Dialog.Prompt("input: Slot ", "slot:", "", False)
    # port = crt.Dialog.Prompt("input: port ", "port:", "", False)
    slot = port1
    port = port2
    crt.Screen.Send("show interface optical-module-info epon-olt_1/" + slot +"/" + port + "\r\n")
    crt.Screen.WaitForString("show interface optical-module-info epon-olt_1/" + slot +"/" + port)
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    for arrinfo in arrCRPortInfo:
        if "TxPower" in arrinfo:
            transmit = arrinfo.split()
            transmit_power = transmit[-1][:-5]
            break
    f1.write('pon_transmit(dBm):'+ str(transmit_power)+'\r\n')
    f1.write('\r\n')
    if len(str(transmit_power))!=0:
        # crt.Dialog.Prompt("total:", "prompt", str(len(transmit_power)), False)
        value = float(float(transmit_power) - 28.5)
        f1.write('ID  '+'Power  '+'       logicID'+'\r\n')

        crt.Screen.Send("show pon power onu-rx epon-olt_1/" + slot +"/" + port + "\r\n")
        crt.Screen.WaitForString("show pon power onu-rx epon-olt_1/" + slot +"/" + port)
        powerInfo = crt.Screen.ReadString("#")
        arrpowerInfo = powerInfo.split("\n")
        nLine = len(arrpowerInfo) 
        receive_power = []
        problem_id = []
        for info in arrpowerInfo[3:nLine-1]:
            power = info.split()
            if ("N/A" not in power[-1])and(float(power[-1][:-5])<value):
                problem_id.append(power[0][15:])
                receive_power.append(power[-1])
        # f2.write(str(len(problem_id))+'\r\n')
        crt.Screen.Send("show running-config interface epon-olt_1/" + slot +"/" + port + "\r\n")
        crt.Screen.WaitForString("show running-config interface epon-olt_1/" + slot +"/" + port)
        logic_id = crt.Screen.ReadString("!")
        arrlogic_id = logic_id.split("\n")
        logicnline = len(arrlogic_id)
        problem_logicid = []
        for logic in arrlogic_id[6:logicnline-1]:
            id = logic.split()
            if id[1] in problem_id:
                problem_logicid.append(id[5])

        total = len(problem_logicid)
        for i in range(total):
            f1.write(str(problem_id[i])+'  '+str(receive_power[i])+'  '+str(problem_logicid[i])+'\r\n')

        # crt.Dialog.Prompt("problem id:", "prompt", str(problem_id), False)
        # crt.Dialog.Prompt("logicID:", "prompt", str(problem_logicid), False)
        # crt.Dialog.Prompt("total:", "prompt", str(len(problem_id)), False)
        f2.write(str(len(problem_id)).decode('utf8')+'\r\n')
        # f2.close()
        crt.Screen.Send("exit\n")
        crt.Screen.WaitForString('[yes/no]:')
        crt.Screen.Send('y\n')
        crt.Screen.WaitForString('请输入 : ')
        return f1,f2
    else:
        f2.write('NA'.decode('utf8')+'\r\n')
        crt.Screen.Send("exit\n")
        crt.Screen.WaitForString('[yes/no]:')
        crt.Screen.Send('y\n')
        crt.Screen.WaitForString('请输入 : ')
        return f2


def ZTE600(port1,port2):
    f1 = io.open('logic.txt','wb')
    f2 = io.open('count.txt','a')
    crt.Screen.Synchronous = True
    crt.Screen.Send("terminal length 0" + "\r\n")
    crt.Screen.WaitForString("terminal length 0")
    # slot = crt.Dialog.Prompt("input: Slot ", "slot:", "", False)
    # port = crt.Dialog.Prompt("input: port ", "port:", "", False)
    slot = port1
    port = port2
    crt.Screen.Send("show optical-module-info epon_olt-1/" + slot +"/" + port + "\r\n")
    crt.Screen.WaitForString("show optical-module-info epon_olt-1/" + slot +"/" + port)
    sCRPortInfo = crt.Screen.ReadString("#")
    arrCRPortInfo = sCRPortInfo.split("\n")
    for arrinfo in arrCRPortInfo:
        if "TxPower" in arrinfo:
            transmit = arrinfo.split()
            transmit_power = transmit[-1][:-5]
            break
    #f1.write('pon_transmit(dBm):'+ str(transmit_power)+'\r\n')
    f1.write('\r\n')
    value = float(float(transmit_power) - 28.5)
    f1.write('ID  '+'Power  '+'       logicID'+'\r\n')

    crt.Screen.Send("show pon power onu-rx epon_olt-1/" + slot +"/" + port + "\r\n")
    crt.Screen.WaitForString("show pon power onu-rx epon_olt-1/" + slot +"/" + port)
    powerInfo = crt.Screen.ReadString("#")
    arrpowerInfo = powerInfo.split("\n")
    nLine = len(arrpowerInfo) 
    receive_power = []
    problem_id = []
    for info in arrpowerInfo[3:nLine-1]:
        power = info.split()
        if ("N/A" not in power[-1])and(float(power[-1][:-5])<value):
            problem_id.append(power[0][15:])
            receive_power.append(power[-1])

    crt.Screen.Send("show running-config-interface epon_olt-1/" + slot +"/" + port + "\r\n")
    crt.Screen.WaitForString("show running-config-interface epon_olt-1/" + slot +"/" + port)
    logic_id = crt.Screen.ReadString("!")
    arrlogic_id = logic_id.split("\n")
    logicnline = len(arrlogic_id)
    problem_logicid = []
    for logic in arrlogic_id[6:logicnline-1]:
        id = logic.split()
        if id[1] in problem_id:
            problem_logicid.append(id[5])

    total = len(problem_logicid)
    for i in range(total):
        f1.write(str(problem_id[i])+'  '+str(receive_power[i])+'  '+str(problem_logicid[i])+'\r\n')

    # crt.Dialog.Prompt("problem id:", "prompt", str(problem_id), False)
    # crt.Dialog.Prompt("logicID:", "prompt", str(problem_logicid), False)
    # crt.Dialog.Prompt("total:", "prompt", str(len(problem_id)), False)
    f2.write(str(len(problem_id)).decode('utf8')+'\r\n')
    # f2.close()
    crt.Screen.Send("exit\n")
    # crt.Screen.WaitForString('[yes/no]:')
    # crt.Screen.Send('y\n')
    crt.Screen.WaitForString('请输入 : ')
    return f1,f2

file = open("count.txt", 'w').close() 
porttxt1 = io.open('port1.txt','r')
porttxt2 = io.open('port2.txt','r')
iptxt = io.open('ip.txt','r')
dtypetxt = io.open('dtype.txt','r')
list_port1 = porttxt1.readlines()
list_port2 = porttxt2.readlines()
list_ip = iptxt.readlines()
list_dtype = dtypetxt.readlines()
for i in range(len(list_port1)):
    list_port1[i] = list_port1[i].rstrip('\n')
    list_port2[i] = list_port2[i].rstrip('\n')
    list_ip[i] = list_ip[i].rstrip('\n')
    list_dtype[i] = list_dtype[i].rstrip('\n')   


# DeviceType = crt.Dialog.Prompt("input: 5680 or 5800 or 300 or 600 ", "Device Type:", "", False)
for a in range(len(list_ip)):
    if list_ip[i]!='0':
        crt.Screen.Send('/'+list_ip[a]+'\r\n')
        crt.Screen.WaitForString('请输入 : ')
        crt.Screen.Send('0'+'\n')
        crt.Screen.WaitForStrings([">","#"])
        # if('5680' == list_dtype[a]):
        #     MA5680t(list_port1[a],list_port2[a])
        # elif('5800' == list_dtype[a]):
        #     MA5800(list_port1[a],list_port2[a])
        # elif('300'== list_dtype[a]):
        #     ZTE300(list_port1[a],list_port2[a])
        # else:
        #     ZTE600(list_port1[a],list_port2[a])
        if('5680' == list_dtype[a]):
            MA5680t(list_port1[a],list_port2[a])
        elif('5800' == list_dtype[a]):
            MA5800(list_port1[a],list_port2[a])
        elif('300'== list_dtype[a]):
            ZTE300(list_port1[a],list_port2[a])
        elif('600'== list_dtype[a]):
            ZTE600(list_port1[a],list_port2[a])
    else:
        f2 = io.open('count.txt','a')
        f2.write('error'.decode('utf8')+'\r\n')
        f2.close()

