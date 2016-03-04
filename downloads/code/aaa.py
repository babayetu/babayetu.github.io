import json

my_json = '{"Val": ["2222222"], "Rc": 0}'
json_obj = json.loads(my_json)
print json_obj["Val"]
print json_obj["Rc"]
print type(json_obj["Val"])