import json

with open(r'_data\members.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

output = []


for member in data:
    print(member)
    new_dict = {}
    new_dict['name'] = member['name']
    new_dict['login'] = member['login']
    new_dict['location'] = member['location']
    new_dict['bio'] = member['bio']
    new_dict['blog'] = member['blog']
    new_dict['avatar'] = member['avatar']
    output.append(new_dict)
    
    
with open(r'_data\members.json', 'w') as f:
    json.dump(output, f)