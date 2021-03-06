#documentation: https://github.com/Yelp/yelp-python
import json
from pprint import pprint 
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

all_data_results=[]
# read API keys
with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

# params = {
#  	"limit": 20,
#  	"location": "London, UK",
#  	"term":"hotdogs"
# }   

# response = client.search(**params)
#print response
#print response.businesses[18].name, response.businesses[18].location.display_address, response.businesses[18].display_phone
#print response.businesses
#print response.businesses[0].location.display_address

#location, count, search_term=""
# def add_params(keyword):
# 	params["term"] = keyword
# 	return params 

def biz_info(response, num):
	for entry in range(num):
		print response.businesses[entry].name, response.businesses[entry].display_phone
		print response.businesses[entry].location.display_address, "\n"

def main():
	params = {}
	search_term = raw_input("What do you want to search for: ")
	params["term"]=search_term
	num_entries = int(raw_input("How many entries do you need? "))
	params["limit"]=num_entries
	designated_location= raw_input("Where do you want the addresses from: ")
	print params
	response = client.search(designated_location, **params)
	print "\n"
	print biz_info(response, num_entries)

if __name__ == '__main__':
	main() 
 
# # #print pprint(dir(response))

#  1. Get input for Location, Count, search_term
#  2. Append params dictionary with Key and values matching Yelp APi documentation and raw inputs 
#  3. reassign that params  dictionary for the `response` variable 



	# for info in all_contacts:
	# 		if info.first_name == fname and info.last_name == lname:
	# 			print(info.first_name, info.last_name, info.mobile_phone, info.home_p

#there is a note in here 



