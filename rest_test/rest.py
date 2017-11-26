import requests
from pprint import pprint

r = requests.get('http://ec2-18-221-233-36.us-east-2.compute.amazonaws.com:8000/attendances/')

data = r.json()
data_text = r.text

pprint(data)
pprint(data_text)

name = []

for entry in data:
	pprint(entry['organiser'])
	name.append(entry['organiser'])

print data[0]['organiser']
