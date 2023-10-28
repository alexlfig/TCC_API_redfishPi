from subprocess import check_output, Popen, call, DEVNULL, STDOUT, PIPE
from collections import OrderedDict
import psutil
import json
import os

def serial():
    """Retorna a serial do Raspberry."""
    return check_output(["cat", "/sys/firmware/devicetree/base/serial-number"]).decode("utf-8").replace('\u0000', '')

def machine_id():
    """Retorna o Machine ID do Raspberry."""
    hostnamectl = Popen(['hostnamectl'], stdout=PIPE)
    machine_id_num = check_output(["grep", "Machine ID"], stdin=hostnamectl.stdout).decode("utf-8").replace('\n', '')
    id_num = machine_id_num.split()[2]
    return id_num

def boot_id():
    """Retorna o Boot ID do Raspberry."""
    hostnamectl = Popen(['hostnamectl'], stdout=PIPE)
    boot_id_num = check_output(["grep", "Boot ID"], stdin=hostnamectl.stdout).decode("utf-8").replace('\n', '')
    id_num = boot_id_num.split()[2]
    return id_num

def hostname():
    """Retorna o hostname do Raspberry."""
    hostnamectl = Popen(['hostnamectl'], stdout=PIPE)
    hostname = check_output(["grep", "Static hostname"], stdin=hostnamectl.stdout).decode("utf-8").replace('\n', '')
    name = hostname.split()[2]
    return name

def model():
    """Retorna o modelo do Raspberry."""
    return check_output(["cat", "/sys/firmware/devicetree/base/model"]).decode("utf-8").replace('\u0000', '')

def system_uuid():
    """Retorna a UUID do sistema."""
    lsblk = Popen(['lsblk', '-f', '--raw'], stdout=PIPE)
    disk_info = check_output(["grep", "rootfs"], stdin=lsblk.stdout).decode("utf-8")
    uuid = disk_info.split()[4]
    return uuid

def cpu_model():
    """Retorna o modelo do processador."""
    cpu_info = Popen(['cat', '/proc/cpuinfo'], stdout=PIPE)
    model = check_output(["grep", "Hardware"], stdin=cpu_info.stdout).decode("utf-8")
    model_name = model.split()[2]
    return model_name

def cpu_vendor():
    """Retorna o modelo dos núcleos."""
    lscpu = Popen(['lscpu'], stdout=PIPE)
    vendor = check_output(["grep", "Vendor ID"], stdin=lscpu.stdout).decode("utf-8")
    vendor_id = vendor.split()[2] 
    return vendor_id

def cpu_core_model():
    """Retorna o modelo dos núcleos."""
    lscpu_a = Popen(['lscpu'], stdout=PIPE)
    vendor = check_output(["grep", "Vendor ID"], stdin=lscpu_a.stdout).decode("utf-8")
    vendor_id = vendor.split()[2]
    lscpu_b = Popen(['lscpu'], stdout=PIPE)
    model = check_output(["grep", "Model name"], stdin=lscpu_b.stdout).decode("utf-8")
    model_name = model.split()[2]
    return vendor_id + " " + model_name

def cpu_arch():
    """Retorna o modelo da arquitetura do processador."""
    lscpu = Popen(['lscpu'], stdout=PIPE)
    arch_number = check_output(["grep", "Architecture"], stdin=lscpu.stdout).decode("utf-8")
    arch = arch_number.split()[1]
    return arch

def cpu_byte_order():
    """Retorna o endianess do processador."""
    lscpu = Popen(['lscpu'], stdout=PIPE)
    byte_order_out = check_output(["grep", "Byte Order"], stdin=lscpu.stdout).decode("utf-8")
    byte_order = byte_order_out.split()[2] + " " + byte_order_out.split()[3]
    return byte_order

def cpu_usage_percent():
    """Retorna a porcentagem de uso atual do processador."""
    return str(psutil.cpu_percent()) + "%"

def cpu_cores():
    """Retorna a quantidade de núcleos do processador."""
    return str(psutil.cpu_count(logical=False))

def cpu_threads():
    """Retorna a quantidade de threads do processador."""
    return str(psutil.cpu_count(logical=True))

def cpu_freq():
    """Retorna a frequência de operação atual do processador."""
    return str(psutil.cpu_freq()[0]) + " MHz"

def cpu_min_freq():
    """Retorna a frequência de operação mínima do processador."""
    return str(psutil.cpu_freq()[1]) + " MHz"

def cpu_max_freq():
    """Retorna a frequência de operação máxima do processador."""
    return str(psutil.cpu_freq()[2]) + " MHz"

def cpu_cache_l1d():
    """Retorna a capacidade de memória cache L1d do processador."""
    lscpu = Popen(['lscpu'], stdout=PIPE)
    l1d = check_output(["grep", "L1d"], stdin=lscpu.stdout).decode("utf-8")
    cache_l1d = l1d.split()[2] + " " + l1d.split()[3]
    return cache_l1d

def cpu_cache_l1i():
    """Retorna a capacidade de memória cache L1i do processador."""
    lscpu = Popen(['lscpu'], stdout=PIPE)
    l1i = check_output(["grep", "L1i"], stdin=lscpu.stdout).decode("utf-8")
    cache_l1i = l1i.split()[2] + " " + l1i.split()[3]
    return cache_l1i

def cpu_cache_l2():
    """Retorna a capacidade de memória cache L2 do processador."""
    lscpu = Popen(['lscpu'], stdout=PIPE)
    l2 = check_output(["grep", "L2"], stdin=lscpu.stdout).decode("utf-8")
    cache_l2 = l2.split()[2] + " " + l2.split()[3]
    return cache_l2

def cpu_voltage():
    """Retorna a tensão de alimentação lida pelo processador."""
    vcgencmd = check_output(['vcgencmd', 'measure_volts', 'core']).decode("utf-8").replace('\n', '')
    volt = vcgencmd.split('=')[1]
    return volt

def cpu_temp():
    vcgencmd = check_output(['vcgencmd', 'measure_temp']).decode("utf-8").replace('\n', '')
    temp = vcgencmd.split('=')[1]
    return temp

def memory_total():
    """Retorna a memória total do Raspberry."""
    vcgencmd = Popen(['vcgencmd', 'get_config', 'int'], stdout=PIPE)
    total_mem = check_output(["grep", "total_mem"], stdin=vcgencmd.stdout).decode("utf-8").replace('\n', '')
    mem = total_mem.split('=')[1]
    return str(mem) + "M"

def memory_arm():
    """Retorna a memória do Raspberry alocada para CPU geral."""
    mem_arm = check_output(["vcgencmd", "get_mem", "arm"]).decode("utf-8").replace('\n', '')
    mem = mem_arm.split('=')[1]
    return mem

def memory_gpu():
    """Retorna a memória do Raspberry alocada para GPU."""
    mem_gpu = check_output(["vcgencmd", "get_mem", "gpu"]).decode("utf-8").replace('\n', '')
    mem = mem_gpu.split('=')[1]
    return mem

def memory_freq():
    """Retorna a velocidade de clock da memória."""
    vcgencmd = Popen(['vcgencmd', 'get_config', 'int'], stdout=PIPE)
    sdram_freq = check_output(["grep", "sdram_freq"], stdin=vcgencmd.stdout).decode("utf-8").replace('\n', '')
    freq = sdram_freq.split('=')[1]
    return str(freq) + " MHz"

def memory_used():
    """Retorna a quantidade de memória utilizada."""
    return str(int(psutil.virtual_memory()[3]/(2 ** 20))) + "M"

def memory_percent_used():
    """Retorna a porcentagem de memória utilizada."""
    return str(psutil.virtual_memory()[2]) + "%"

def memory_available():
    """Retorna a quantidade de memória disponível."""
    return str(int(psutil.virtual_memory()[1]/(2 ** 20))) + "M"

def memory_free():
    """Retorna a quantidade de memória livre."""
    return str(int(psutil.virtual_memory()[4]/(2 ** 20))) + "M"

def memory_voltage():
    """Retorna a tensão de alimentação lida pela memória SDRAM."""
    vcgencmd = check_output(['vcgencmd', 'measure_volts', 'sdram_i']).decode("utf-8").replace('\n', '')
    volt = vcgencmd.split('=')[1]
    return volt

def memory_buffers():
    """Retorna a quantidade de memória de buffers."""
    return str(int(psutil.virtual_memory()[7]/(2 ** 20))) + "M"

def memory_cached():
    """Retorna a quantidade de memória em cache."""
    return str(int(psutil.virtual_memory()[8]/(2 ** 20))) + "M"

def swap_total():
    """Retorna a memória de swap total."""
    return str(int(psutil.swap_memory()[0]/(2 ** 20))) + "M"

def swap_used():
    """Retorna a memória de swap utilizada no momento."""
    return str(int(psutil.swap_memory()[1]/(2 ** 20))) + "M"

def swap_free():
    """Retorna a memória de swap livre no momento."""
    return str(int(psutil.swap_memory()[2]/(2 ** 20))) + "M"

def swap_percent():
    """Retorna a porcentagem de uso da memória de swap."""
    return str(psutil.swap_memory()[3]) + "%"

def os_name():
    """Retorna o nome do sistema operacional."""
    cat = Popen(['cat', '/etc/os-release'], stdout=PIPE)
    pretty_name = check_output(["grep", "PRETTY_NAME"], stdin=cat.stdout).decode("utf-8").replace('\n', '')
    name = pretty_name.split('=')[1].replace('"', '')
    return name

def os_version():
    """Retorna a versão do sistema operacional."""
    cat = Popen(['cat', '/etc/os-release'], stdout=PIPE)
    os_version = check_output(["grep", "VERSION_ID"], stdin=cat.stdout).decode("utf-8").replace('\n', '')
    version = os_version.split('=')[1].replace('"', '')
    return version

def os_kernel_version():
    """Retorna a versão do Kernel do sistema."""
    hostnamectl = Popen(['hostnamectl'], stdout=PIPE)
    kernel_name = check_output(["grep", "Kernel"], stdin=hostnamectl.stdout).decode("utf-8").replace('\n', '')
    name = kernel_name.split()[1:]
    kernel = ""
    for word in name:
        if kernel == "":
            kernel = word
        else:
            kernel = kernel + " " + word
    return kernel

def eth_count():
    """Retorna a quantidade de interfaces de rede do sistema."""
    return str(len(psutil.net_if_addrs().keys()))

def eth_names():
    """Retorna o nome das interfaces de rede do sistema."""
    return list(psutil.net_if_addrs().keys())

def eth_members():
    """Retorna a versão do Kernel do sistema."""
    interface_names = psutil.net_if_addrs().keys()
    interfaces = []
    for name in interface_names:
        interfaces.append({
            "@odata.id": "/redfish/v1/Systems/" + boot_id() + "/EthernetInterfaces/" + name
        })
    return interfaces

def eth_stats(iface: str):
    iface_addrs = psutil.net_if_addrs()[iface]
    iface_stats = psutil.net_if_stats()[iface]

    stats = {}

    stats['mac_address'] = "00:00:00:00:00:00"
    stats['speed_mbps'] = "0"
    stats['full_duplex'] = "False"
    stats['state'] = "Disabled"
    stats['ipv6_gateway'] = "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"
    stats['dns'] = []

    nmcli1 = Popen(['nmcli', 'dev', 'show', iface], stdout=PIPE)
    is_there_dns = call(["grep", "DNS"], stdin=nmcli1.stdout, stdout=DEVNULL, stderr=STDOUT)
    if(is_there_dns == 0):
        nmcli1 = Popen(['nmcli', 'dev', 'show', iface], stdout=PIPE)
        dns_parse = check_output(["grep", "DNS"], stdin=nmcli1.stdout).decode("utf-8")
        dns_break_lines = dns_parse.split('\n')[:-1]
        for line in dns_break_lines:
            stats['dns'].append(line.split()[1])
                
    stats['ipv4_addresses'] = []
    stats['ipv6_addresses'] = []

    for snicaddr in iface_addrs:
        if snicaddr[0] == 2:
            nmcli2 = Popen(['nmcli', 'dev', 'show', iface], stdout=PIPE)
            gateway_parse = check_output(["grep", "IP4.GATEWAY"], stdin=nmcli2.stdout).decode("utf-8").replace('\n', '')
            gateway = gateway_parse.split()[1]
            if gateway == "--": gateway = "Unknown"
            stats['ipv4_addresses'].append({"Address": snicaddr[1],
                                            "SubnetMask": snicaddr[2],
                                            "AddressOrigin": "Static",
                                            "Gateway": gateway})                
        elif snicaddr[0] == 10:
            prefix = bin(int(snicaddr[2].replace(':', ''), 16))
            prefix_length = len(str(prefix).replace('0', '').replace('b', ''))
            stats['ipv6_addresses'].append({"Address": snicaddr[1],
                                            "PrefixLength": prefix_length,
                                            "AddressOrigin": "Static",
                                            "AddressState": "Preferred"})
        elif snicaddr[0] == 17:
            stats['mac_address'] = snicaddr[1]
            
    if iface_stats[0]:
        stats['state'] = "Enabled"
    else:
        stats['state'] = "Disabled"

    if iface_stats[1] == 2:
        stats['full_duplex'] = "True"
                
    stats['speed_mbps'] = str(iface_stats[2])

    return stats
