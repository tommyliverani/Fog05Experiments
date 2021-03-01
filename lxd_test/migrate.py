from pylxd import Client
from pylxd.exceptions import LXDAPIException
import datetime

#client_source=Client(endpoint='https://192.168.56.139:8443',cert=('/etc/fos/plugins/plugin-fdu-lxd/templates/lxd.crt','/etc/fos/plugins/plugin-fdu-lxd/templates/lxd.key'),verify=False)
#client_destination=Client(endpoint='https://192.168.56.154:8443',cert=('/etc/fos/plugins/plugin-fdu-lxd/templates/lxd.crt','/etc/fos/plugins/plugin-fdu-lxd/templates/lxd.key'),verify=False)


client_source=Client(endpoint='https://192.168.56.139:8443',verify=False)

client_destination=Client(endpoint='https://192.168.56.154:8443',verify=False)

client_source.authenticate('fos')
client_destination.authenticate('fos')

cont = client_source.containers.get('cab6743a4-7663-474b-a9e5-219a98fd1548')
try:
	print('migrate at {}'.format(datetime.datetime.now()))
	cont.stop(force = False, wait = True)
	cont.sync()
	cont.migrate(client_destination, wait = True)
	print('migrated at {}'.format(datetime.datetime.now()))
except LXDAPIException as e:
                self.logger.info('migrate_fdu()', ' LXD Plugin - LXD error {}'.format(e))
                cont.delete()
