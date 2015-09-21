
m jnpr.junos.factory import loadyaml
from jnpr.junos.op import *
from jnpr.junos import Device

globals().update( loadyaml('/root/pyez/bgp_table.yml'))
dev = Device(host='172.2.3.5',user='mario',ssh_private_key_file='/root/.ssh/VRF')
dev.open()
tbl=BgpNeigh(dev)
tbl.get()
