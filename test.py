import json
from pprint import pprint

f = open('shokupan_recipe.json')
data = json.load(f)

for i in data['ingredients']:
    pprint(i["name"])
