from jnpr.junos import Device
from lxml import etree

dev = Device(host='172.2.3.5',user='mario',ssh_private_key_file='/root/.ssh/VRF')
dev.open()

def sh_int(iface_type=""):
  if iface_type=="":
    c_out = dev.rpc.get_interface_information(terse=True)
  else:
    c_out = dev.rpc.get_interface_information(terse=True, interface_name=iface_type)
  for kk in c_out:
    print kk

sh_int()
