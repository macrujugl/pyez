from jnpr.junos import Device
from lxml import etree

dev = Device(host='172.2.3.5',user='mario',ssh_private_key_file='/root/.ssh/VRF')
dev.open()

c_out = dev.rpc.get_bgp_summary_information(exact_instance='master')
print "----------------------------------------------------------"
print "|Remote-AS  "+"|Neigh     "+"|Session Status   |ACT|REC|ACC|SUP|"
print "----------------------------------------------------------"
for kk in c_out.findall('bgp-peer'):
	peer_as=kk.find('peer-as').text
	peer_address=kk.find('peer-address').text
	peer_state=kk.find('peer-state').text
	if peer_state=='Established':
        	peer_rib_active=kk.find('bgp-rib').find('active-prefix-count').text
        	peer_rib_received=kk.find('bgp-rib').find('received-prefix-count').text
        	peer_rib_accepted=kk.find('bgp-rib').find('accepted-prefix-count').text
        	peer_rib_suppressed=kk.find('bgp-rib').find('suppressed-prefix-count').text
        else :
		peer_rib_active,peer_rib_received,peer_rib_accepted,peer_rib_suppressed=0,0,0,0
	print '{}{:<11}{}{:<10}{}{:<17}{}{:<3}{}{:<3}{}{:<3}{}{:<3}{}'.format("|", peer_as, "|", peer_address, "|", peer_state, "|", peer_rib_active, "|",peer_rib_received, "|",peer_rib_accepted, "|",peer_rib_suppressed, "|")
print "=========================================================="
