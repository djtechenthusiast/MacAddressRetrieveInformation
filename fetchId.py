 
import requests 
import argparse

parser = argparse.ArgumentParser(description='Provide information about macaddress.')
parser.add_argument('macaddress', type=str,
                   help='a macaddress to retrieve information')
args = parser.parse_args()

# api endpoint 
URL = "https://api.macaddress.io/v1"
  
# params
apiKey = "at_OHlwjlnqAm3hyF2OzWm4UcnGwMq0v"
outputType = "json" 
macAdd = args.macaddress

# defining params dict
PARAMS = {'apiKey':apiKey,'output':outputType,'search':macAdd} 
  
# sending get request and saving response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json()  

# Displaying company name in readable format on command line
print("Name of the company owning this MAC Address is, "+data["vendorDetails"]["companyName"])