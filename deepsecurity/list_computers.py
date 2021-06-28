from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint
import csv
import requests



# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://cloudone.trendmicro.com/api'

# Authentication
configuration.api_key['api-secret-key'] = ''
# Initialization
# Set Any Required Values
api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
expand_options = deepsecurity.Expand()
expand_options.add(expand_options.none)
expand = expand_options.list()
overrides = False

try:
	api_response = api_instance.list_computers(api_version, expand=expand, overrides=overrides)
	pprint(api_response)
except ApiException as e:
	print("An exception occurred when calling ComputersApi.list_computers: %s\n" % e)



# Write to csv file

	
outputFile = open("output.csv", "w")

count = 0

reader = csv.writer(outputFile, delimiter=',')
reader.writerow(['COMPUTER NAME', 'PLATFORM', 'POLICY NAME', 'STATUS'])

api_response = str(api_response).split('\n')
api_response.pop(0)

for i in api_response:
	print('here is i', i)
	outputFile.writelines(i)
	count += 1

	if (count == 4):
		outputFile.write('\n')
		count = 0
	




