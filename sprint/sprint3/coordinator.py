import json
import time
from fog05 import FIMAPI
from fog05_sdk.interfaces.FDU import FDU

def read_file(filepath):
	with open(filepath, 'r') as f:
		data = f.read()
	return data

n= 'f1b36698-1a55-4924-8f15-5d11ba845dac'
api = FIMAPI()
desc = json.loads(read_file('fdu_lxd_net.json'))


input('Press enter to deploy')
fdu_descriptor =  FDU(desc)
fduD = api.fdu.onboard(fdu_descriptor)
fdu_id = fduD.get_uuid()
print ( 'fdu_id: {}'.format(fduD.get_uuid()))

inst_info=api.fdu.define(fdu_id,n)
api.fdu.configure(inst_info.get_uuid())

input('Press enter to start')
api.fdu.start(inst_info.get_uuid(), "MYENV=Hello World!")
print('Instance ID: {}'.format(inst_info.get_uuid()))


input('Press enter to terminate')
api.fdu.terminate(inst_info.get_uuid())
api.fdu.offload(fdu_id)

api.close()
exit(0)


