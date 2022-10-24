import json

with open('_data\members.json', 'r') as f:
    data = json.load(f)

output = []
new_dict = {}

for member in data.keys():
    print(data[member]['name'])
    new_dict = data[member]
    new_dict['login'] = member
    output.append(new_dict)
    
with open('_data\members.json', 'w') as f:
    json.dump(output, f)