

class Context:
	def __init__(self,fog_index,nodes_ip,nodes_number,epoch_number,epoch_index):
		self.fog_index=fog_index
		self.nodes_ip=nodes_ip
		self.nodes_number=nodes_number
		self.epoch_number=epoch_number
		self.epoch_index=epoch_index
		self.example_number=[]
		self.client_models=[]
		self.global_model=None
	
	def save(self):
		f=open("context.txt","w")
		f.write("{}\n".format(self.fog_index))	#fog index
		for node in self.nodes_ip:
			f.write("{}".format(node))
			if self.nodes_ip.index(node)!= len(self.nodes_ip)-1:
				f.write(" ")
		f.write("\n") #fog nodes ip	
		f.write("{}\n".format(self.nodes_number)) #fog nodes number
		f.write("{}\n".format(self.epoch_number)) #epochs number
		f.write("{}\n".format(self.epoch_index)) #epochs index
		f.close()
	
def readContext():
	f=open("context.txt","r") 
	fog_index=int(f.readline()) #fog_index
	if fog_index!=0:
		fog_nodes=f.readline().split("\n")[0].split(" ") #fog nodes ip
	else:
		f.readline()
		fog_nodes=[]
	print(fog_nodes)
	nodes_number= int(f.readline())
	epoch_number= int(f.readline())
	epoch_index=int(f.readline())
	f.close()
	context= Context(fog_index,fog_nodes,nodes_number,epoch_number,epoch_index)
	return context
		
	
