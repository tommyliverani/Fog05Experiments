import json
import time
from fog05 import FIMAPI
from fog05_sdk.interfaces.FDU import FDU

def read_file(filepath):
	with open(filepath, 'r') as f:
		data = f.read()
	return data

n= '630816a2-d83a-400e-8b93-f8d65dfd90f5'
api = FIMAPI()
desc = json.loads(read_file('fdu_helloworld.json'))
fdu_descriptor =  FDU(desc)
fduD = api.fdu.onboard(fdu_descriptor)
fdu_id = fduD.get_uuid()
print ( 'fdu_id: {}'.format(fduD.get_uuid()))

inst_info=api.fdu.define(fdu_id,n)
api.fdu.configure(inst_info.get_uuid())
api.fdu.start(inst_info.get_uuid(), "MYENV=Hello World!")
print('Instance ID: {}'.format(inst_info.get_uuid()))


time.sleep(1)
log = api.fdu.log(inst_info.get_uuid())
print('FDU Output:\n{}\n'.format(log))

input('Press enter to terminate')

api.fdu.terminate(inst_info.get_uuid())

api.close()
exit(0)

