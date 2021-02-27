from requests


#weighted gradient averaging algorithm
def wga(global_model, client_models, example_numbers):
  n=0
  state_dict=global_model.state_dict()
  for i in example_numbers:
    n=n+i
  for key in state_dict.keys():
    j=0
    state_dict[key]=0
    for client_model in client_models:
      state_dict[key]=state_dict[key] + example_numbers[j]*client_model.state_dict()[key]
      j=j+1
    state_dict[key]= state_dict[key]/n
  global_model.load_state_dict(state_dict)
	

def post_model(fog_ips, global_model):
	torch.save(global_mode.state_dict(),'global_model')
	for ip in fog_ips:
		requests.post('http://{}5000/'.format(ip),files={'model':open('global_model','rb')})
	
		
	
	


