
from jnpr.junos.factory import loadyaml
from jnpr.junos import Device

globals().update( loadyaml('/root/pyez/interfaces_table.yml'))
dev = Device(host='172.2.3.5',user='mario',ssh_private_key_file='/root/.ssh/VRF')
dev.open()
tbl=IfacesEthernetTable(dev)
tbl.get()
for k in tbl:
	print k.items()
	for l in k.items()[2][1]:
		print l.items()
