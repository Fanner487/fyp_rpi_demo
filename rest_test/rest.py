import requests
from pprint import pprint

r = requests.get('http://ec2-18-221-233-36.us-east-2.compute.amazonaws.com:8000/attendances/')

data_json = r.json()
data_text = r.text

print "\n\nJSON:"
pprint(data_json)

print "\n\nIn text:"
pprint(data_text)

name = []

print "\n\n"

for entry in data_json:
	pprint(entry['organiser'])
	name.append(entry['organiser'])

print "\n\nOrganisers:"
print name

