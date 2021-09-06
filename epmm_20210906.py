    try:
		c = kwargs['c']
	except:
		c =  ''
    
	if c == '1':
		Gas_param = {}
        
        
        
        
        for key in Gas_param.keys(): 
			if c_n == '1':
				ID_temp = ''
				#ID_temp = json.loads(Gas_param[key])['E_ID'] + json.loads(Gas_param[key])['U_ID']
				ID_temp = json.loads(Gas_param[key])['E_ID']
				E_ID += '#' + C_ID[-1]
				#ID = E_ID + U_ID
				ID = E_ID
			else:
				ID_temp = ''
				E_ID_temp = ''
				E_ID_temp = split(json.loads(Gas_param[key])['E_ID'])
				for i in range(len(E_ID_temp)):
					if E_ID_temp[i] == '#':
						tag = i
						break
				for i in range(tag):
					ID_temp += E_ID_temp[i]
				#ID_temp += json.loads(Gas_param[key])['U_ID']
				#ID = E_ID + U_ID
				ID = E_ID
				
			if ID_temp == ID or p == '1':
				find = 1
				T_ID = key
				break