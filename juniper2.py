from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys


def loadVRFConfig(VRF_number):
    if (1<int(VRF_number)<255):
            dev = Device(host='172.2.3.5',user='mario',ssh_private_key_file='/root/.ssh/VRF')
            dev.open()


            conf=Config(dev)
            variables={}
            variables['VRF_instance']=VRF_number

            conf.load(template_path='templateVRF_set.conf', template_vars=variables, format='set', merge=True)
            conf.pdiff()
	    if conf.commit_check():
		print 'This config would commit succesfully'
            else:
  		print 'Config puck`d up'
            dev.close()
    else:
        print 'The VRF number must be between 2 and 254'

def main():
    loadVRFConfig(str(sys.argv[1]))

main ()
