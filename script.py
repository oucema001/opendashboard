# write a script that reads the dashboard.json file and extract the base64 descoded value of the manifest key under the configurations key
# and writes it to a file called manifest.json

import json
import base64

with open('dashboard.json') as f:
    data_dashboard = json.load(f)

manifest = data_dashboard['configuration']['manifest']
decoded_manifest = base64.b64decode(manifest)

with open('manifest.json', 'w') as f:
    f.write(decoded_manifest.decode('utf-8'))

# remove the named element  "6870a1a9-c5a3-4fb4-b0b5-899954e7c750"  and all its child elements under widgets key in the decoded manifest and write the new manifest to a file called manifes

decoded_manifest2 = decoded_manifest.decode('utf-8')
decoded_manifest2 = json.loads(decoded_manifest2)
widgets = decoded_manifest2['widgets']
widgets.pop('6870a1a9-c5a3-4fb4-b0b5-899954e7c750', None)

with open('manifest2.json', 'w') as f:
    f.write(json.dumps(decoded_manifest2))


# read the sectors.json file and extract the elements that have '"type": "identity"' under the json array objects then extract the value of the "name" key and the id key and put it in  a dictionary


with open('sectors.json') as f:
    data = json.load(f)

identities = {}
data2 = data['objects']
for obj in data2:
    if obj['type'] == 'identity':
        identities[obj['id']] = obj['name']

print(identities)

# create a folder named dashboards and continue if it exists
import os
if not os.path.exists('dashboards'):
    os.makedirs('dashboards')


# iterate over the identities dictionary and create a file for each identity in the dashboards folder with 
#the name of the file being the name of the identity then change the decoded manifest key to replace all the occurences 
#of the word energy with the name value in identities and replace all occurences that start with identity- with the id value 
#in identities then base64 encode the new manifest and write it to a file containing as content the new base64 encoded manifest as
# a replacement to the configuration manifest key in the dasboard.json file

with open('dashboard.json') as f:
    data_dashboard2 = json.load(f)
print(data_dashboard2)
for id, name in identities.items():
    with open(f'dashboards/{name}.json', 'w') as f:
        decoded_manifest2 = decoded_manifest.decode('utf-8')
        decoded_manifest2 = json.loads(decoded_manifest2)
        decoded_manifest2 = json.dumps(decoded_manifest2).replace('energy', name).replace('identity-', id)
        encoded_manifest = base64.b64encode(decoded_manifest2.encode('utf-8'))
        data_dashboard2['configuration']['manifest'] = encoded_manifest.decode('utf-8')
        #with open('dashboard.json', 'w') as f:
        #    f.write(json.dumps(data))
    
        f.write(json.dumps(data_dashboard2))


