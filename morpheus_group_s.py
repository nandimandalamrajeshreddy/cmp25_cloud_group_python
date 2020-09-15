import xlrd
import requests
import json
import gensim
import os
import logging
import urllib3
requests.packages.urllib3.disable_warnings() 
from gensim.summarization import summarize
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

loc = ("C://Users/nandimar/Desktop/Go/R/groups_clouds.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

#payload = ""
payload = {
	"group":{
		"name": sheet.cell_value(0, 1),
		"description": sheet.cell_value(1, 1),
		"location": sheet.cell_value(2, 1)
		}
	}
mypayloadd = json.dumps(payload)	
print(mypayloadd)
resp = requests.post('https://uis.cmp.unisys-waf.com/api/groups', headers={'Authorization': 'BEARER ' + '7b00caab-9bfc-48f8-8126-7df5bd350b9b'},data = mypayloadd,verify = False)
if resp.status_code == 200:
	print('Azure : ' + sheet.cell_value(0, 1) + ' ' + 'group' +' - is Successfully Created')
else:
	print('Azure : ' + sheet.cell_value(0, 1) + ' ' + 'group' + '  - is not Successfully Created due to json response issue')
print(resp.text)