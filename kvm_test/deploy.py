import json
import time
from fog05 import FIMAPI
from fog05_sdk.interfaces.FDU import FDU
import datetime

def read_file(filepath):
	with open(filepath, 'r') as f:
		data = f.read()
	return data

n2='d85e9c0d-0a89-4a6c-a4b1-857ca652fc56'
n= '10856437-b455-4469-b124-59dceac73010'


api = FIMAPI('192.168.1.10')
desc = json.loads(read_file('fdu_ubuntu_live.json'))
#desc = json.loads(read_file('fdu_ubuntu_cold.json'))
fdu_descriptor =  FDU(desc)
fduD = api.fdu.onboard(fdu_descriptor)
fdu_id = fduD.get_uuid()
print ( 'fdu_id: {}'.format(fduD.get_uuid()))

print('instantiate at {}'.format(datetime.datetime.now()))
inst_info=api.fdu.define(fdu_id,n)
api.fdu.configure(inst_info.get_uuid())
print('instantiated at {}'.format(datetime.datetime.now()))

print('start at {}'.format(datetime.datetime.now()))
api.fdu.start(inst_info.get_uuid(), "MYENV=Hello World!")
print('started at {}'.format(datetime.datetime.now()))

print('migrate at {}'.format(datetime.datetime.now()))
api.fdu.migrate(inst_info.get_uuid(),n2)
print('migrated at {}'.format(datetime.datetime.now()))

print('Instance ID: {}'.format(inst_info.get_uuid()))

input('Press enter to terminate')

api.fdu.terminate(inst_info.get_uuid())

api.close()
exit(0)


