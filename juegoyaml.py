import yaml
import sys

filename='/root/REPOS/unf-data/objects/'+sys.argv[1]+'.yml'
f = open(filename)
# use safe_load instead load
data = yaml.safe_load(f)
f.close()

print data['parameters']['network']['peRtrName']
