import json
import time
from fog05 import FIMAPI
from fog05_sdk.interfaces.FDU import FDU
import datetime

def read_file(filepath):
	with open(filepath, 'r') as f:
		data = f.read()
	return data

n= '31d0eaa7-455c-4231-8860-9bb592fdb3cb'
n2= 'f60f2d18-582e-8ea4-4f36-d356603be81d'


api = FIMAPI()
input('Press enter to load the descriptor')
desc = json.loads(read_file('fdu_lxd.json'))
fdu_descriptor =  FDU(desc)

#onboard descriptors
fduD = api.fdu.onboard(fdu_descriptor)
fdu_id = fduD.get_uuid()

input('Press enter to define')
print('instantiate at {}'.format(datetime.datetime.now()))
inst_info=api.fdu.define(fdu_id,n)

print ( 'fdu_id: {}'.format(inst_info.get_uuid()))
api.fdu.configure(inst_info.get_uuid())
print('instantiated at {}'.format(datetime.datetime.now()))

input('Press enter to start')
print('start at {}'.format(datetime.datetime.now()))
api.fdu.start(inst_info.get_uuid(), "MYENV=Hello World!")

input('Press enter to terminate')
api.fdu.terminate(inst_info.get_uuid())
api.fdu.offload(fdu_id)


api.close()
exit(0)


