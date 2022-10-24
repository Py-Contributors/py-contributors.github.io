import json
from github import Github
import argparse

arg = argparse.ArgumentParser()
arg.add_argument('-o', '--org', required=True, help='Organization name')
arg.add_argument('-t', '--token', required=True, help='Github token')
args = vars(arg.parse_args())

output = []
ORG_NAME = args['org']
PAT = args['token']

gh = Github(login_or_token=PAT)

org = gh.get_organization(ORG_NAME)

for member in org.get_members():
    user_data = {}
    user_data['login'] = member.login
    user_data["name"] = member.name
    user_data["location"] = member.location
    user_data["bio"] = member.bio
    user_data["blog"] = member.blog
    user_data["avatar"] = member.avatar_url
    output.append(user_data)

with open("_data/members.json.json", "w") as f:
    json.dump(output, f, indent=4)
