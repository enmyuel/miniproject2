# make json more pretty
import json

with open("/data/project/data.json", "r", encoding='utf-8') as f:
    json_data = f.read()

#Convert JSON to Python object
obj = json.loads(json_data)

#Python pretty print JSON
json_formatted_str = json.dumps(obj, indent=4, ensure_ascii=False)
print(json_formatted_str)
