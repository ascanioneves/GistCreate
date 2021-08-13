import requests
import json
import os
from pprint import pprint

def evaluate(s):
  return True if s == 'Public' else False

token = open('../token/token.txt').read()
query_url = "https://api.github.com/gists"
file_path = input()
f = open(file_path, 'r')
code = f.read()
gist_type = input('If you want to make a private gist write Private, otherwise write Public\n')
gist_type = evaluate(gist_type)

data = {
  "public": gist_type,
  "files": {
    "gist_test.py": {
      "content": code
    }
  }
}

headers = {'Authorization': f'token {token}'}
r = requests.post(query_url, headers=headers, data=json.dumps(data))
pprint(r.json())