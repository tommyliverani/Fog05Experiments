from fog05 import FIMAPI


api = FIMAPI('192.168.56.114')
nodes=api.node.list()
print("\n{0} nodes found".format(len(nodes)))
for node in nodes:
	print('\n\n---------NODE-------------\n')
	print(node)
	print('\n\n--------PLUGINS-----------\n')
	print(api.node.plugins(node))
