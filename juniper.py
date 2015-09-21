from jnpr.junos import Device
from jnpr.junos.utils.config import Config

import sys
 
VRF_instance=sys.argv[1]
print str(sys.argv[1])
print type(sys.argv[1])

dev = Device(host='172.2.3.5',user='mario',ssh_private_key_file='/root/.ssh/VRF')
dev.open()
 
conf=Config(dev)
variables={}
variables['VRF_instance']=sys.argv[1]
print variables

conf.load(template_path='templateVRF.conf', template_vars=variables, format='text')



#print conf
#print dev.facts['version']
#print dev.cli("show configuration system services")
 
dev.close()
