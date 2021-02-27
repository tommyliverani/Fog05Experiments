from flask import Flask
from flask import request
from Context import Context
from Model import Net
from fl_utils import wga
from fl_utils import post_model




app=Flask(__name__)
 
context=None

		
#start a federate learning process
@app.route('/start',methods=['PUT'])
def start():
	global context
	print('[AGGREGATOR] started')
	context= Context(0,[],request.form['fogs'],request.form['epochs'],0)
	#context.save()
	return '[AGGREGATOR] started'

#used by a fog node to register his ip

@app.route('/get_id',methods=['GET'])
def add_ip():
	global context
	#context=readContext()	
	id=context.fog_index
	context.nodes_ip.append(request.form['ip'])
	context.fog_index=context.fog_index+1
	context.example_number.append(request.form['example_number'])
	if context.fog_index==context.fog_number: #all fog nodes are working
		context.fog_index=0
		post_model(contxt.nodes_ip,context.global_model)
	#context.save()	#used to save the context in a file	
	return "{}".format(id)
	
	
@app.route('/update',methods=['POST'])
def update_model():
	global context
	file=request.files['model']
	id=request.form['id']
	ip=request.form['ip']
	context.example_number.append(request.form['example_number'])
	#context.nodes_ip[id]=ip	 #to use in case of node migration
	file.save('{}'.format(id))	#necessario?
	context.fog_index=fog_index+1
	#TODO da rivedere quando è stata fatta la net{
	net=Net() 
	net.load_state_dict(torch.load('{}'.format(id)))		
	context.client_models.append(net)
	#}
	if context.fog_index==context.fog_number:	#epoch terminated
		context.epoch_index=context.epoch_index+1
		context.fog_index=0
		#aggregate the model
		wga(context.global_model,context.client_models)
		context.client_models=[]		#empty list	
		context.example_number=[]
		post_model(contxt.nodes_ip,context.global_model)
		if contex.epoch_index==context.epoch_number:
			#TODO federate learning process finish
	
	

	
if __name__=='main':		
	app.run(host='0.0.0.0')
