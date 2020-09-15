import xlrd
import requests
import json
import gensim
import os
import logging
import urllib3
import os
from sys import argv

requests.packages.urllib3.disable_warnings() 
from gensim.summarization import summarize
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

loc = ("C://Users/nandimar/Desktop/Go/R/groups_clouds.xlsx") 

os.system("morpheus groups get " + argv[1] + " -j > C://Users/nandimar/Desktop/Go/R/id.json")
with open('C://Users/nandimar/Desktop/Go/R/id.json') as f:
	data = json.load(f)
	#print (data['group'][0]['id'])

ID= data['group']['id']

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(1) 
sheet.cell_value(0, 0)

payload = {
	"zone":{
		"name": sheet.cell_value(0, 1),
		"code": "Azure",
		"description": sheet.cell_value(6, 1),
		"location": sheet.cell_value(7, 1),
		"zoneType":{"id": 16},
		"groupId": ID,
		"regionCode": sheet.cell_value(8, 1),
		"config":{
			"subscriberId": sheet.cell_value(5, 1),
			"tenantId": sheet.cell_value(4, 1),
			"clientId": sheet.cell_value(1, 1),
			"clientSecret": sheet.cell_value(2, 1),
			"resourceGroup": "All",
			"applianceUrl": "http://52.184.165.34",
#			"groups": [{"id": 22,"name": "morph test"}],
			"networkServer.id": "unmanaged",
			"networkServer":{
				"id": "unmanaged"
			}
		}
	}
}
	
mypayload = json.dumps(payload)	
print(mypayload)
resp = requests.post('https://uis.cmp.unisys-waf.com/api/zones', headers={'Authorization': 'BEARER ' + '7b00caab-9bfc-48f8-8126-7df5bd350b9b'},data = mypayload,verify = False)
print(resp.status_code)
if resp.status_code == 200:
	print('Azure : ' + sheet.cell_value(0, 1) + '  - is Successfully Created')
else:
	print('Azure : ' + sheet.cell_value(0, 1) + '  - is not Successfully Created due to json response issue')
os.remove("C://Users/nandimar/Desktop/Go/R/id.json")
	