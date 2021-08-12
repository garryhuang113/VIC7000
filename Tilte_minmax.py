from vic import *
import requests
import threading
import time
import json

lock = threading.Lock()
Gas_dict={}
Gas_param = {}
Gas_return = {}



def mainLoop(info, arr):
	
	ID_string = str(PAGE01.OCR337).replace(' ', '')
	char_list = split(ID_string)
	colon_list = []
	slash_list = []
	E_ID = ''
	U_ID = ''
	print(char_list)
	
	for i in range(len(char_list)):
		if char_list[i] == ':':
			colon_list.append(i)
		if char_list[i] == '/':
			slash_list.append(i)
	
	for i in range(colon_list[0] + 1, slash_list[0]):
		E_ID += char_list[i]

	print(E_ID)
	
	print(colon_list)
	print(slash_list)
			
			
	pass

def split(word):
	return[char for char in word]

def SetGasParam(**kwargs):
	
	global Gas_param, lock
	
	Gas_param_temp = {}
	
	try:
		E_ID = kwargs['E_ID']
		Gas_param_temp['E_ID'] = E_ID
	except:
		return {'error_message':'Cannot find E_ID.', 'is_success':'N'}
	
	try:
		U_ID = kwargs['U_ID']
		Gas_param_temp['U_ID'] = U_ID
	except:
		return {'error_message':'Cannot find U_ID.', 'is_success':'N'}
	
	try:
		O_ID = kwargs['O_ID']
		Gas_param_temp['O_ID'] = O_ID
	except:
		return {'error_message':'Cannot find O_ID.', 'is_success':'N'}
	
	try:
		F_ID = kwargs['F_ID']
		Gas_param_temp['F_ID'] = F_ID
	except:
		return {'error_message':'Cannot find F_ID.', 'is_success':'N'}
	
	try:
		Gas_set = kwargs['Gas_set']
		Gas_param_temp['Gas_set'] = Gas_set
	except:
		return {'error_message':'Cannot find Gas_set.', 'is_success':'N'}
	
	
	lock.acquire()
	
	Gas_param[F_ID] = json.dumps(Gas_param_temp)
	
	lock.release()
	
	#print(Gas_param)
	
	return {'is_success':'Y'}
	

	
def RecognizeImage(**args):
	
	global Gas_dict, Gas_param, Gas_return, lock

	try:
		img = args['img']
	except:
		return {'error_message':'Cannot find img.', 'is_success':'N'}
	
	Gas_dict_temp = {}
	Gas_return_temp = {}
	find = 0
	result = {}
	
	E_ID = ''
	U_ID = ''
	F_ID = ''
	ID = ''
	ID_temp = ''
	ID_string = ''
    char_list = []
	colon_list = []
	slash_list = []
	
	'''
	x1 = int(result['PATTERN01'].X)+int(result['PATTERN01'].WIDTH)
	y1 = int(result['PATTERN01'].Y)
	w1 = int(result['PATTERN02'].X)-x1
	h1 = int(result['PATTERN01'].HEIGHT)
	x2 = int(result['PATTERN03'].X)+int(result['PATTERN03'].WIDTH)
	y2 = int(result['PATTERN03'].Y)
	w2 = 100
	h2 = int(result['PATTERN03'].HEIGHT)
	E_ID = TOOL.OCR(0, 'epmm_ID', x1, y1, w1, h1, img, {'segmentation':7, 'preprocess_resize':7, 'preprocess_resize_method': 0, 'preprocess_threshold_method':1, 'preprocess_threshold_algorithm': 0, 'preprocess_threshold_value': 135})
	U_ID = TOOL.OCR(0, 'epmm_ID', x2, y2, w2, h2, img, {'segmentation':7, 'preprocess_resize':7, 'preprocess_resize_method': 0, 'preprocess_threshold_method':1, 'preprocess_threshold_algorithm': 0, 'preprocess_threshold_value': 135})	
	E_ID = str(E_ID).replace(' ', '')
	U_ID = str(U_ID).replace(' ', '')
	'''
	
	'''
	E_ID = args['E_ID']
	U_ID = args['U_ID']
	'''
	
	ID_string = TOOL.OCR(0, 'ID_test', 127,0,1393,22, img, {'segmentation':7, 'preprocess_resize':5, 'preprocess_resize_method': 0, 'preprocess_threshold_method':1, 'preprocess_threshold_algorithm': 1, 'preprocess_threshold_value': 135})
	ID_string = ID_string.replace(' ', '')
	char_list = split(ID_string)
    
	for i in range(len(char_list)):
		if char_list[i] == ':':
			colon_list.append(i)
		if char_list[i] == '/':
			slash_list.append(i)
	
	for i in range(colon_list[0] + 1, slash_list[0]):
		E_ID += char_list[i]
	
	for i in range(colon_list[3] + 1, len(char_list)):
		U_ID += char_list[i]
	
	ID = E_ID + U_ID
	
	for key in Gas_param.keys():
		ID_temp = ''
		ID_temp = json.loads(Gas_param[key])['E_ID'] + json.loads(Gas_param[key])['U_ID']
		if ID_temp == ID:
			find = 1
			F_ID = key
	
	if find == 1:
		
		result = PAGE_PROCESS('01', img)
		
		Gas1_name=''
		Gas1_set=[]
		Gas1_error=[]
		Gas1_dict={}
		Gas1_name=result['OCR01']
		Gas1_set=[result['OCR02'],
				 result['OCR03'],
				 result['OCR04'],
				 result['OCR05'],
				 result['OCR06'],
				 result['OCR07'],
				 result['OCR08'],
				 result['OCR09'],
				 result['OCR10'],
				 result['OCR11']
				 ]
		Gas1_error=[result['OCR12'],
				 result['OCR13'],
				 result['OCR14'],
				 result['OCR15'],
				 result['OCR16'],
				 result['OCR17'],
				 result['OCR18'],
				 result['OCR19'],
				 result['OCR20'],
				 result['OCR21']
				 ]

		Gas2_name=''
		Gas2_set=[]
		Gas2_error=[]
		Gas2_dict={}
		Gas2_name=result['OCR22']
		Gas2_set=[result['OCR23'],
				 result['OCR24'],
				 result['OCR25'],
				 result['OCR26'],
				 result['OCR27'],
				 result['OCR28'],
				 result['OCR29'],
				 result['OCR30'],
				 result['OCR31'],
				 result['OCR32']
				 ]
		Gas2_error=[result['OCR33'],
				 result['OCR34'],
				 result['OCR35'],
				 result['OCR36'],
				 result['OCR37'],
				 result['OCR38'],
				 result['OCR39'],
				 result['OCR40'],
				 result['OCR41'],
				 result['OCR42']
				 ]

		Gas3_name=''
		Gas3_set=[]
		Gas3_error=[]
		Gas3_dict={}
		Gas3_name=result['OCR43']
		Gas3_set=[result['OCR44'],
				 result['OCR45'],
				 result['OCR46'],
				 result['OCR47'],
				 result['OCR48'],
				 result['OCR49'],
				 result['OCR50'],
				 result['OCR51'],
				 result['OCR52'],
				 result['OCR53']
				 ]
		Gas3_error=[result['OCR54'],
				 result['OCR55'],
				 result['OCR56'],
				 result['OCR57'],
				 result['OCR58'],
				 result['OCR59'],
				 result['OCR60'],
				 result['OCR61'],
				 result['OCR62'],
				 result['OCR63']
				 ]

		Gas4_name=''
		Gas4_set=[]
		Gas4_error=[]
		Gas4_dict={}
		Gas4_name=result['OCR64']
		Gas4_set=[result['OCR65'],
				 result['OCR66'],
				 result['OCR67'],
				 result['OCR68'],
				 result['OCR69'],
				 result['OCR70'],
				 result['OCR71'],
				 result['OCR72'],
				 result['OCR73'],
				 result['OCR74']
				 ]
		Gas4_error=[result['OCR75'],
				 result['OCR76'],
				 result['OCR77'],
				 result['OCR78'],
				 result['OCR79'],
				 result['OCR80'],
				 result['OCR81'],
				 result['OCR82'],
				 result['OCR83'],
				 result['OCR84']
				 ]

		Gas5_name=''
		Gas5_set=[]
		Gas5_error=[]
		Gas5_dict={}
		Gas5_name=result['OCR85']
		Gas5_set=[result['OCR86'],
				 result['OCR87'],
				 result['OCR88'],
				 result['OCR89'],
				 result['OCR90'],
				 result['OCR91'],
				 result['OCR92'],
				 result['OCR93'],
				 result['OCR94'],
				 result['OCR95']
				 ]
		Gas5_error=[result['OCR96'],
				 result['OCR97'],
				 result['OCR98'],
				 result['OCR99'],
				 result['OCR100'],
				 result['OCR101'],
				 result['OCR102'],
				 result['OCR103'],
				 result['OCR104'],
				 result['OCR105']
				 ]

		Gas6_name=''
		Gas6_set=[]
		Gas6_error=[]
		Gas6_dict={}
		Gas6_name=result['OCR106']
		Gas6_set=[result['OCR107'],
				 result['OCR108'],
				 result['OCR109'],
				 result['OCR110'],
				 result['OCR111'],
				 result['OCR112'],
				 result['OCR113'],
				 result['OCR114'],
				 result['OCR115'],
				 result['OCR116']
				 ]
		Gas6_error=[result['OCR117'],
				 result['OCR118'],
				 result['OCR119'],
				 result['OCR120'],
				 result['OCR121'],
				 result['OCR122'],
				 result['OCR123'],
				 result['OCR124'],
				 result['OCR125'],
				 result['OCR126']
				 ]

		Gas7_name=''
		Gas7_set=[]
		Gas7_error=[]
		Gas7_dict={}
		Gas7_name=result['OCR127']
		Gas7_set=[result['OCR128'],
				 result['OCR129'],
				 result['OCR130'],
				 result['OCR131'],
				 result['OCR132'],
				 result['OCR133'],
				 result['OCR134'],
				 result['OCR135'],
				 result['OCR136'],
				 result['OCR137']
				 ]
		Gas7_error=[result['OCR138'],
				 result['OCR139'],
				 result['OCR140'],
				 result['OCR141'],
				 result['OCR142'],
				 result['OCR143'],
				 result['OCR144'],
				 result['OCR145'],
				 result['OCR146'],
				 result['OCR147']
				 ]

		Gas8_name=''
		Gas8_set=[]
		Gas8_error=[]
		Gas8_dict={}
		Gas8_name=result['OCR148']
		Gas8_set=[result['OCR149'],
				 result['OCR150'],
				 result['OCR151'],
				 result['OCR152'],
				 result['OCR153'],
				 result['OCR154'],
				 result['OCR155'],
				 result['OCR156'],
				 result['OCR157'],
				 result['OCR158']
				 ]
		Gas8_error=[result['OCR159'],
				 result['OCR160'],
				 result['OCR161'],
				 result['OCR162'],
				 result['OCR163'],
				 result['OCR164'],
				 result['OCR165'],
				 result['OCR166'],
				 result['OCR167'],
				 result['OCR168']
				 ]

		Gas9_name=''
		Gas9_set=[]
		Gas9_error=[]
		Gas9_dict={}
		Gas9_name=result['OCR169']
		Gas9_set=[result['OCR170'],
				 result['OCR171'],
				 result['OCR172'],
				 result['OCR173'],
				 result['OCR174'],
				 result['OCR175'],
				 result['OCR176'],
				 result['OCR177'],
				 result['OCR178'],
				 result['OCR179']
				 ]
		Gas9_error=[result['OCR180'],
				 result['OCR181'],
				 result['OCR182'],
				 result['OCR183'],
				 result['OCR184'],
				 result['OCR185'],
				 result['OCR186'],
				 result['OCR187'],
				 result['OCR188'],
				 result['OCR189']
				 ]

		Gas10_name=''
		Gas10_set=[]
		Gas10_error=[]
		Gas10_dict={}
		Gas10_name=result['OCR190']
		Gas10_set=[result['OCR191'],
				 result['OCR192'],
				 result['OCR193'],
				 result['OCR194'],
				 result['OCR195'],
				 result['OCR196'],
				 result['OCR197'],
				 result['OCR198'],
				 result['OCR199'],
				 result['OCR200']
				 ]
		Gas10_error=[result['OCR201'],
				 result['OCR202'],
				 result['OCR203'],
				 result['OCR204'],
				 result['OCR205'],
				 result['OCR206'],
				 result['OCR207'],
				 result['OCR208'],
				 result['OCR209'],
				 result['OCR210']
				 ]

		Gas11_name=''
		Gas11_set=[]
		Gas11_error=[]
		Gas11_dict={}
		Gas11_name=result['OCR211']
		Gas11_set=[result['OCR212'],
				 result['OCR213'],
				 result['OCR214'],
				 result['OCR215'],
				 result['OCR216'],
				 result['OCR217'],
				 result['OCR218'],
				 result['OCR219'],
				 result['OCR220'],
				 result['OCR221']
				 ]
		Gas11_error=[result['OCR222'],
				 result['OCR223'],
				 result['OCR224'],
				 result['OCR225'],
				 result['OCR226'],
				 result['OCR227'],
				 result['OCR228'],
				 result['OCR229'],
				 result['OCR230'],
				 result['OCR231']
				 ]

		Gas12_name=''
		Gas12_set=[]
		Gas12_error=[]
		Gas12_dict={}
		Gas12_name=result['OCR232']
		Gas12_set=[result['OCR233'],
				 result['OCR234'],
				 result['OCR235'],
				 result['OCR236'],
				 result['OCR237'],
				 result['OCR238'],
				 result['OCR239'],
				 result['OCR240'],
				 result['OCR241'],
				 result['OCR242']
				 ]
		Gas12_error=[result['OCR243'],
				 result['OCR244'],
				 result['OCR245'],
				 result['OCR246'],
				 result['OCR247'],
				 result['OCR248'],
				 result['OCR249'],
				 result['OCR250'],
				 result['OCR251'],
				 result['OCR252']
				 ]

		Gas13_name=''
		Gas13_set=[]
		Gas13_error=[]
		Gas13_dict={}
		Gas13_name=result['OCR253']
		Gas13_set=[result['OCR254'],
				 result['OCR255'],
				 result['OCR256'],
				 result['OCR257'],
				 result['OCR258'],
				 result['OCR259'],
				 result['OCR260'],
				 result['OCR261'],
				 result['OCR262'],
				 result['OCR263']
				 ]
		Gas13_error=[result['OCR264'],
				 result['OCR265'],
				 result['OCR266'],
				 result['OCR267'],
				 result['OCR268'],
				 result['OCR269'],
				 result['OCR270'],
				 result['OCR271'],
				 result['OCR272'],
				 result['OCR273']
				 ]

		Gas14_name=''
		Gas14_set=[]
		Gas14_error=[]
		Gas14_dict={}
		Gas14_name=result['OCR274']
		Gas14_set=[result['OCR275'],
				 result['OCR276'],
				 result['OCR277'],
				 result['OCR278'],
				 result['OCR279'],
				 result['OCR280'],
				 result['OCR281'],
				 result['OCR282'],
				 result['OCR283'],
				 result['OCR284']
				 ]
		Gas14_error=[result['OCR285'],
				 result['OCR286'],
				 result['OCR287'],
				 result['OCR288'],
				 result['OCR289'],
				 result['OCR290'],
				 result['OCR291'],
				 result['OCR292'],
				 result['OCR293'],
				 result['OCR294']
				 ]

		Gas15_name=''
		Gas15_set=[]
		Gas15_error=[]
		Gas15_dict={}
		Gas15_name=result['OCR295']
		Gas15_set=[result['OCR296'],
				 result['OCR297'],
				 result['OCR298'],
				 result['OCR299'],
				 result['OCR300'],
				 result['OCR301'],
				 result['OCR302'],
				 result['OCR303'],
				 result['OCR304'],
				 result['OCR305']
				 ]
		Gas15_error=[result['OCR306'],
				 result['OCR307'],
				 result['OCR308'],
				 result['OCR309'],
				 result['OCR310'],
				 result['OCR311'],
				 result['OCR312'],
				 result['OCR313'],
				 result['OCR314'],
				 result['OCR315']
				 ]

		Gas16_name=''
		Gas16_set=[]
		Gas16_error=[]
		Gas16_dict={}
		Gas16_name=result['OCR316']
		Gas16_set=[result['OCR317'],
				 result['OCR318'],
				 result['OCR319'],
				 result['OCR320'],
				 result['OCR321'],
				 result['OCR322'],
				 result['OCR323'],
				 result['OCR324'],
				 result['OCR325'],
				 result['OCR326']
				 ]
		Gas16_error=[result['OCR327'],
				 result['OCR328'],
				 result['OCR329'],
				 result['OCR330'],
				 result['OCR331'],
				 result['OCR332'],
				 result['OCR333'],
				 result['OCR334'],
				 result['OCR335'],
				 result['OCR336']
				 ]
		'''
		Gas17_name=''
		Gas17_set=[]
		Gas17_error=[]
		Gas17_dict={}
		Gas17_name='Tuning' + result['OCR337']
		Gas17_set=[result['OCR338'],
				 result['OCR339'],
				 result['OCR340'],
				 result['OCR341'],
				 result['OCR342'],
				 result['OCR343'],
				 result['OCR344'],
				 result['OCR345'],
				 result['OCR346'],
				 result['OCR347']
				 ]
		Gas17_error=[result['OCR348'],
				 result['OCR349'],
				 result['OCR350'],
				 result['OCR351'],
				 result['OCR352'],
				 result['OCR353'],
				 result['OCR354'],
				 result['OCR355'],
				 result['OCR356'],
				 result['OCR357']
				 ]

		Gas18_name=''
		Gas18_set=[]
		Gas18_error=[]
		Gas18_dict={}
		Gas18_name='Tuning' + result['OCR358']
		Gas18_set=[result['OCR359'],
				 result['OCR360'],
				 result['OCR361'],
				 result['OCR362'],
				 result['OCR363'],
				 result['OCR364'],
				 result['OCR365'],
				 result['OCR366'],
				 result['OCR367'],
				 result['OCR368']
				 ]
		Gas18_error=[result['OCR369'],
				 result['OCR370'],
				 result['OCR371'],
				 result['OCR372'],
				 result['OCR373'],
				 result['OCR374'],
				 result['OCR375'],
				 result['OCR376'],
				 result['OCR377'],
				 result['OCR378']
				 ]
		'''
		for i in range(len(Gas1_set)):
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
			#GasError(Gas17_dict, Gas17_set[i], Gas17_error[i])
			#GasError(Gas18_dict, Gas18_set[i], Gas18_error[i])

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
		#Gas_dict_temp[Gas17_name]=json.dumps(Gas17_dict)
		#Gas_dict_temp[Gas18_name]=json.dumps(Gas18_dict)
		#SHOW_IMAGE(img)

		E_ID=json.loads(Gas_param[F_ID])['E_ID']
		Gas_dict_temp['E_ID'] = E_ID
		Gas_return_temp['E_ID'] = E_ID
		U_ID=json.loads(Gas_param[F_ID])['U_ID']
		Gas_dict_temp['U_ID'] = U_ID
		Gas_return_temp['U_ID'] = U_ID
		O_ID=json.loads(Gas_param[F_ID])['O_ID']
		Gas_dict_temp['O_ID'] = O_ID
		Gas_return_temp['O_ID'] = O_ID
		F_ID=json.loads(Gas_param[F_ID])['F_ID']
		Gas_dict_temp['F_ID'] = F_ID
		Gas_return_temp['F_ID'] = F_ID
		
		Gas_set = json.loads(Gas_param[F_ID])['Gas_set']
		Gas_set = Gas_set.split(',')
		
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

		Gas_dict[F_ID] = json.dumps(Gas_dict_temp)
		Gas_return[F_ID] = json.dumps(Gas_return_temp)

		lock.release()

		#print(Gas_dict)
		#print(Gas_return)

		return {'result':'Data for F_ID = ' + F_ID +', E_ID = ' + E_ID + ', and U_ID = ' + U_ID + ' is ready.', 'is_success':'Y'}
	
	else:
		return {'error_message':'Cannot find data matching F_ID = ' + F_ID +', E_ID = ' + E_ID + ', and U_ID = ' + U_ID + '.', 'is_success':'N'}


	
	
	

def GasError(Gas_Temp_Dict, Set, Error):
	
	if Set=='' or Error=='':
		pass
	elif not Set in Gas_Temp_Dict.keys():
		Gas_Temp_Dict[Set]=Error

'''
def GetGasSet(**kwargs):
	
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
		
		try:
			Gas_name = kwargs['Gas_name']
			Gas_name = Gas_name.split(',')
			Gas_dict_temp = json.loads(Gas_dict[ID])
	
			if 	Gas_name[0] == '':
				return {'Error':'There is no input parameter.'}
	
			for i in range(len(Gas_name)):
		
				try:
					return_dict[Gas_name[i]] = Gas_dict_temp[Gas_name[i]]
				except:
					if Gas_name[i] == '':
						return {'Error':'There is error in input parameters. Please check them.'}
					else:
						return_dict[Gas_name[i]] = 'Unknown Gas_name'
						
			return return_dict		
		except:
			return {'Error':'Cannot find Gas_name'}
	else:
		return {'Error':'Cannot find data matching E_ID = ' + E_ID +' and U_ID = ' + U_ID + '.'}
	
	
	return return_dict
'''	
	
	
def GetGasData(**kwargs):
	
	global Gas_dict, Gas_return, Gas_param, lock
	
	return_dict = {}
	
	try:
		F_ID=kwargs['F_ID']
	except:
		return {'error_message':'Cannot find F_ID.', 'is_success':'N'}
	
	
	if (F_ID in Gas_return.keys() and F_ID in Gas_dict.keys()) and F_ID in Gas_param.keys():

		return_dict['data'] = Gas_return[F_ID]
		return_dict['is_success'] = 'Y'
		
		lock.acquire()
		
		Gas_dict.pop(F_ID, None)
		Gas_return.pop(F_ID, None)
		Gas_param.pop(F_ID, None)
		
		lock.release()
		
		return return_dict 

	else:
		return {'error_message':'Cannot find data matching F_ID = ' + F_ID + '.', 'is_success':'N'}
		
	

