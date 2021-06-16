from vic import *
import requests
import threading
import time
import json

lock = threading.Lock()
Gas_dict = {}
Gas_param = {}
Gas_return = {}


def mainLoop(info, arr):
	
	pass


def SetGasParam(**kwargs):
	
	global Gas_param, lock
	
	Gas_param_temp = {}
	
	try:
		T_ID = kwargs['T_ID']
		Gas_param_temp['T_ID'] = T_ID
	except:
		return {'Error':'Cannot find T_ID.'}
	
	try:
		E_ID = kwargs['E_ID']
		Gas_param_temp['E_ID'] = E_ID
	except:
		return {'Error':'Cannot find E_ID.'}
	
	try:
		U_ID = kwargs['U_ID']
		Gas_param_temp['U_ID'] = U_ID
	except:
		return {'Error':'Cannot find U_ID.'}
	
	try:
		Gas_set = kwargs['Gas_set']
		Gas_param_temp['Gas_set'] = Gas_set
	except:
		return {'Error':'Cannot find Gas_set.'}
	
	ID = E_ID + U_ID
	
	lock.acquire()
	
	Gas_param[ID] = json.dumps(Gas_param_temp)
	
	lock.release()
	
	#print(Gas_param)
	
	return {'result':'OK'}
	
	
def RecognizeImage(**args):
	
	global Gas_dict, Gas_param, Gas_return


	img = args['img']

	Gas_dict_temp = {}
	Gas_return_temp = {}

	result = {}
	
	result = PAGE_PROCESS('01', img)
	
	E_ID = ''
	U_ID = ''
	'''
	x1 = int(result['PATTERN01'].X)+int(result['PATTERN01'].WIDTH)
	y1 = int(result['PATTERN01'].Y)
	w1 = int(result['PATTERN02'].X)-x1
	h1 = int(result['PATTERN01'].HEIGHT)
	x2 = int(result['PATTERN03'].X)+int(result['PATTERN03'].WIDTH)
	y2 = int(result['PATTERN03'].Y)
	w2 = 50
	h2 = int(result['PATTERN03'].HEIGHT)
	E_ID = TOOL.OCR(1, '', x1, y1, w1, h1, img, {'segmentation':7, 'preprocess_resize':0, 'preprocess_resize_method': 0, 'preprocess_threshold_method':1, 'preprocess_threshold_algorithm': 1, 'preprocess_thredshold_value': 120})
	U_ID = TOOL.OCR(1, '', x2, y2, w2, h2, img, {'segmentation':7, 'preprocess_resize':0, 'preprocess_resize_method': 0, 'preprocess_threshold_method':1, 'preprocess_threshold_algorithm': 1, 'preprocess_thredshold_value': 120})	
	E_ID = str(E_ID)
	U_ID = str(U_ID)
	Gas_temp['E_ID'] = E_ID
	Gas_temp['U_ID'] = U_ID
	'''
	E_ID = args['E_ID']
	U_ID = args['U_ID']
	
	ID = E_ID + U_ID
	
	if ID in Gas_param.keys():

		Gas1_name=''
		Gas1_set=[]
		Gas1_error=[]
		Gas1_dict={}
		Gas1_name='SiCl4-100'
		Gas1_set=['100.0',
				 '100.0',
				 '10.0',
				 '50.0',
				 '90.0',
				 '100.0',
				 '100.0',
				 '100.0',
				 '100.0',
				 '100.0'
				 ]
		Gas1_error=['3.19',
				 '1.76',
				 '2.55',
				 '1.57',
				 '2.61',
				 '2.97',
				 '2.82',
				 '3.34',
				 '3.81',
				 '3.54'
				 ]

		Gas2_name=''
		Gas2_set=[]
		Gas2_error=[]
		Gas2_dict={}
		Gas2_name='H2-500'
		Gas2_set=['50.0',
				 '250.0',
				 '450.0',
				 '70.0',
				 '10.0',
				 '10.0',
				 '10.0',
				 '10.0',
				 '10.0',
				 '10.0'
				 ]
		Gas2_error=['-2.71',
				 '-2.57',
				 '-2.08',
				 '-2.28',
				 '-0.41',
				 '-0.02',
				 '3.26',
				 '3.23',
				 '3.31',
				 '3.32'
				 ]

		Gas3_name=''
		Gas3_set=[]
		Gas3_error=[]
		Gas3_dict={}
		Gas3_name='CH4-100'
		Gas3_set=['30.0',
				 '30.0',
				 '10.0',
				 '50.0',
				 '90.0',
				 '30.0',
				 '30.0',
				 '30.0',
				 '30.0',
				 '30.0'
				 ]
		Gas3_error=['0.29',
				 '0.15',
				 '-0.12',
				 '0.38',
				 '0.65',
				 '0.3',
				 '0.3',
				 '0.47',
				 '0.53',
				 '0.44'
				 ]

		Gas4_name=''
		Gas4_set=[]
		Gas4_error=[]
		Gas4_dict={}
		Gas4_name='CH2F2-100'
		Gas4_set=['35.0',
				 '35.0',
				 '10.0',
				 '50.0',
				 '90.0',
				 '35.0',
				 '35.0',
				 '35.0',
				 '35.0',
				 '35.0'
				 ]
		Gas4_error=['-0.11',
				 '-0.27',
				 '0.53',
				 '0.08',
				 '0.16',
				 '-0.11',
				 '0.04',
				 '-0.16',
				 '-0.04',
				 '0.0'
				 ]

		Gas5_name=''
		Gas5_set=[]
		Gas5_error=[]
		Gas5_dict={}
		Gas5_name='CF4-200'
		Gas5_set=['180.0',
				 '180.0',
				 '20.0',
				 '100.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0'
				 ]
		Gas5_error=['0.55',
				 '0.19',
				 '0.1',
				 '0.53',
				 '0.57',
				 '0.62',
				 '0.53',
				 '0.42',
				 '0.38',
				 '0.39'
				 ]

		Gas6_name=''
		Gas6_set=[]
		Gas6_error=[]
		Gas6_dict={}
		Gas6_name='SF6-200'
		Gas6_set=['20.0',
				 '100.0',
				 '180.0',
				 '23.0',
				 '',
				 '',
				 '',
				 '',
				 '',
				 ''
				 ]
		Gas6_error=['0.54',
				 '0.56',
				 '0.07',
				 '0.92',
				 '',
				 '',
				 '',
				 '',
				 '',
				 ''
				 ]

		Gas7_name=''
		Gas7_set=[]
		Gas7_error=[]
		Gas7_dict={}
		Gas7_name='N2-200'
		Gas7_set=['8.0',
				 '8.0',
				 '20.0',
				 '100.0',
				 '80.0',
				 '8.0',
				 '8.0',
				 '8.0',
				 '8.0',
				 '8.0'
				 ]
		Gas7_error=['1.11',
				 '1.1',
				 '-0.43',
				 '-1.02',
				 '-0.82',
				 '1.05',
				 '1.08',
				 '1.25',
				 '1.43',
				 '1.49'
				 ]

		Gas8_name=''
		Gas8_set=[]
		Gas8_error=[]
		Gas8_dict={}
		Gas8_name='SO2-200'
		Gas8_set=['185.0',
				 '185.0',
				 '20.0',
				 '100.0',
				 '180.0',
				 '185.0',
				 '185.0',
				 '185.0',
				 '185.0',
				 '185.0'
				 ]
		Gas8_error=['0.54',
				 '0.65',
				 '2.8',
				 '0.98',
				 '0.73',
				 '0.63',
				 '0.73',
				 '0.48',
				 '0.41',
				 '0.6'
				 ]

		Gas9_name=''
		Gas9_set=[]
		Gas9_error=[]
		Gas9_dict={}
		Gas9_name='O2-200'
		Gas9_set=['100.0',
				 '100.0',
				 '20.0',
				 '100.0',
				 '180.0',
				 '100.0',
				 '100.0',
				 '100.0',
				 '100.0',
				 '100.0'
				 ]
		Gas9_error=['0.82',
				 '0.85',
				 '0.86',
				 '0.8',
				 '1.05',
				 '0.93',
				 '0.84',
				 '0.83',
				 '0.73',
				 '0.93'
				 ]

		Gas10_name=''
		Gas10_set=[]
		Gas10_error=[]
		Gas10_dict={}
		Gas10_name='CHF3-300'
		Gas10_set=['180.0',
				 '180.0',
				 '30.0',
				 '150.0',
				 '270.0',
				 '180.0',
				 '180.0',
				 '',
				 '',
				 ''
				 ]
		Gas10_error=['1.16',
				 '1.3',
				 '0.67',
				 '1.18',
				 '0.81',
				 '1.3',
				 '1.39',
				 '',
				 '',
				 ''
				 ]

		Gas11_name=''
		Gas11_set=[]
		Gas11_error=[]
		Gas11_dict={}
		Gas11_name='CH3F-300'
		Gas11_set=['180.0',
				 '180.0',
				 '30.0',
				 '150.0',
				 '270.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0'
				 ]
		Gas11_error=['-0.09',
				 '-0.82',
				 '-1.02',
				 '0.19',
				 '0.39',
				 '0.07',
				 '0.11',
				 '-0.01',
				 '-0.02',
				 '0.1'
				 ]

		Gas12_name=''
		Gas12_set=[]
		Gas12_error=[]
		Gas12_dict={}
		Gas12_name='HBr-500'
		Gas12_set=['180.0',
				 '180.0',
				 '50.0',
				 '250.0',
				 '450.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0'
				 ]
		Gas12_error=['0.03',
				 '0.78',
				 '0.33',
				 '0.8',
				 '-0.11',
				 '0.1',
				 '0.08',
				 '-0.01',
				 '-0.33',
				 '-0.2'
				 ]

		Gas13_name=''
		Gas13_set=[]
		Gas13_error=[]
		Gas13_dict={}
		Gas13_name='NF3-500'
		Gas13_set=['20.0',
				 '20.0',
				 '50.0',
				 '250.0',
				 '450.0',
				 '20.0',
				 '50.0',
				 '50.0',
				 '50.0',
				 '50.0'
				 ]
		Gas13_error=['2.75',
				 '1.82',
				 '0.97',
				 '0.79',
				 '0.35',
				 '1.33',
				 '1.34',
				 '0.93',
				 '1.12',
				 '0.88'
				 ]

		Gas14_name=''
		Gas14_set=[]
		Gas14_error=[]
		Gas14_dict={}
		Gas14_name='Ar-500'
		Gas14_set=['180.0',
				 '180.0',
				 '50.0',
				 '250.0',
				 '450.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0',
				 '180.0'
				 ]
		Gas14_error=['0.71',
				 '0.85',
				 '1.01',
				 '0.88',
				 '1.14',
				 '0.81',
				 '0.84',
				 '0.97',
				 '0.76',
				 '0.79'
				 ]

		Gas15_name=''
		Gas15_set=[]
		Gas15_error=[]
		Gas15_dict={}
		Gas15_name='He-500'
		Gas15_set=['200.0',
				 '200.0',
				 '50.0',
				 '250.0',
				 '450.0',
				 '200.0',
				 '200.0',
				 '200.0',
				 '200.0',
				 '200.0'
				 ]
		Gas15_error=['-0.73',
				 '-0.67',
				 '0.71',
				 '-0.85',
				 '-0.85',
				 '-0.67',
				 '-0.64',
				 '-0.56',
				 '-0.65',
				 '-0.67'
				 ]

		Gas16_name=''
		Gas16_set=[]
		Gas16_error=[]
		Gas16_dict={}
		Gas16_name='Cl2-200'
		Gas16_set=['140.0',
				 '140.0',
				 '20.0',
				 '100.0',
				 '180.0',
				 '140.0',
				 '100.0',
				 '100.0',
				 '100.0',
				 '100.0'
				 ]
		Gas16_error=['0.4',
				 '0.74',
				 '0.96',
				 '0.9',
				 '0.88',
				 '0.8',
				 '0.45',
				 '0.89',
				 '0.87',
				 '0.68'
				 ]

		Gas17_name=''
		Gas17_set=[]
		Gas17_error=[]
		Gas17_dict={}
		Gas17_name='CH3F-50'
		Gas17_set=['5.0',
				 '25.0',
				 '45.0',
				 '',
				 '',
				 '',
				 '',
				 '',
				 '',
				 ''
				 ]
		Gas17_error=['-2.42',
				 '-1.43',
				 '0.69',
				 '',
				 '',
				 '',
				 '',
				 '',
				 '',
				 ''
				 ]

		Gas18_name=''
		Gas18_set=[]
		Gas18_error=[]
		Gas18_dict={}
		Gas18_name='He-500'
		Gas18_set=['50.0',
				 '250.0',
				 '450.0',
				 '',
				 '',
				 '',
				 '',
				 '',
				 '',
				 ''
				 ]
		Gas18_error=['1.48',
				 '1.3',
				 '1.28',
				 '',
				 '',
				 '',
				 '',
				 '',
				 '',
				 ''
				 ]

		for i in range(10):
			GasError(Gas1_dict, Gas1_set[i], Gas1_error[i])
			GasError(Gas2_dict, Gas2_set[i], Gas2_error[i])
			GasError(Gas3_dict, Gas3_set[i], Gas3_error[i])
			GasError(Gas4_dict, Gas4_set[i], Gas4_error[i])
			GasError(Gas5_dict, Gas5_set[i], Gas5_error[i])
			GasError(Gas6_dict, Gas6_set[i], Gas6_error[i])
			GasError(Gas7_dict, Gas7_set[i], Gas7_error[i])
			GasError(Gas8_dict, Gas8_set[i], Gas8_error[i])
			GasError(Gas9_dict, Gas9_set[i], Gas9_error[i])
			GasError(Gas10_dict, Gas10_set[i], Gas10_error[i])
			GasError(Gas11_dict, Gas11_set[i], Gas11_error[i])
			GasError(Gas12_dict, Gas12_set[i], Gas12_error[i])
			GasError(Gas13_dict, Gas13_set[i], Gas13_error[i])
			GasError(Gas14_dict, Gas14_set[i], Gas14_error[i])
			GasError(Gas15_dict, Gas15_set[i], Gas15_error[i])
			GasError(Gas16_dict, Gas16_set[i], Gas16_error[i])
			GasError(Gas17_dict, Gas17_set[i], Gas17_error[i])
			GasError(Gas18_dict, Gas18_set[i], Gas18_error[i])

		Gas_dict_temp[Gas1_name]=json.dumps(Gas1_dict)
		Gas_dict_temp[Gas2_name]=json.dumps(Gas2_dict)
		Gas_dict_temp[Gas3_name]=json.dumps(Gas3_dict)
		Gas_dict_temp[Gas4_name]=json.dumps(Gas4_dict)
		Gas_dict_temp[Gas5_name]=json.dumps(Gas5_dict)
		Gas_dict_temp[Gas6_name]=json.dumps(Gas6_dict)
		Gas_dict_temp[Gas7_name]=json.dumps(Gas7_dict)
		Gas_dict_temp[Gas8_name]=json.dumps(Gas8_dict)
		Gas_dict_temp[Gas9_name]=json.dumps(Gas9_dict)
		Gas_dict_temp[Gas10_name]=json.dumps(Gas10_dict)
		Gas_dict_temp[Gas11_name]=json.dumps(Gas11_dict)
		Gas_dict_temp[Gas12_name]=json.dumps(Gas12_dict)
		Gas_dict_temp[Gas13_name]=json.dumps(Gas13_dict)
		Gas_dict_temp[Gas14_name]=json.dumps(Gas14_dict)
		Gas_dict_temp[Gas15_name]=json.dumps(Gas15_dict)
		Gas_dict_temp[Gas16_name]=json.dumps(Gas16_dict)
		Gas_dict_temp[Gas17_name]=json.dumps(Gas17_dict)
		Gas_dict_temp[Gas18_name]=json.dumps(Gas18_dict)
		
		T_ID=json.loads(Gas_param[ID])['T_ID']
		Gas_dict_temp['T_ID'] = T_ID
		Gas_return_temp['T_ID'] = T_ID
		E_ID=json.loads(Gas_param[ID])['E_ID']
		Gas_dict_temp['E_ID'] = E_ID
		Gas_return_temp['E_ID'] = E_ID
		U_ID=json.loads(Gas_param[ID])['U_ID']
		Gas_dict_temp['U_ID'] = U_ID
		Gas_return_temp['U_ID'] = U_ID
		
		Gas_set=json.loads(Gas_param[ID])['Gas_set']
		Gas_set=Gas_set.split(',')
		
		for i in range(len(Gas_set)):
			temp=Gas_set[i].split('_')
			try:
				Gas_return_temp[temp[0]+'_'+temp[1]]=json.loads(Gas_dict_temp[temp[0]])[temp[1]]
			except:
				if not temp[0] in Gas_dict_temp.keys():
					Gas_return_temp[temp[0]]='Unknown'
				elif not temp[1] in json.loads(Gas_dict_temp[temp[0]]).keys():
					Gas_return_temp[temp[0]+'_'+temp[1]]='Unknown'
		
		lock.acquire()
		
		Gas_dict[ID] = json.dumps(Gas_dict_temp)
		Gas_return[ID] = json.dumps(Gas_return_temp)
		
		lock.release()
		
		#print(Gas_dict)
		#print(Gas_return)
		
		return {'result':'Data for E_ID = ' + E_ID +' and U_ID = ' + U_ID + ' is ready.'}
		
	else:
		return {'Error':'Cannot find data matching E_ID = ' + E_ID +' and U_ID = ' + U_ID + '.'}
	
	

	
	return {'result':'OK'}
	
	
	

def GasError(Gas_Temp_Dict, Set, Error):
	
	if Set=='' or Error=='':
		pass
	elif not Set in Gas_Temp_Dict.keys():
		Gas_Temp_Dict[Set]=Error

	
	
	
def GetGasData(**kwargs):
	
	global Gas_dict, Gas_return, Gas_param
	
	return_dict = {}
	
	try:
		E_ID=kwargs['E_ID']
	except:
		return {'Error':'Cannot find E_ID.'}
	
	try:
		U_ID=kwargs['U_ID']
	except:
		return {'Error':'Cannot find U_ID.'}
	
	ID = E_ID + U_ID
	
	if (ID in Gas_return.keys() and ID in Gas_dict.keys()) and ID in Gas_param.keys():

		return_dict = json.loads(Gas_return[ID])
		
		lock.acquire()
		
		Gas_dict.pop(ID, None)
		Gas_return.pop(ID, None)
		Gas_param.pop(ID, None)
		
		lock.release()
		
		return return_dict 

	else:
		return {'Error':'Cannot find data matching E_ID = ' + E_ID +' and U_ID = ' + U_ID + '.'}
		
	

