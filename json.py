import json
x = json.loads('{"bar":["baz", null, 1.0, 2]}')
x["f"] = "k"
print(x) #{'bar': ['baz', None, 1.0, 2], 'f': 'k'}

print(json.dumps({"name": "John", "age": 30})) #'{"name": "John", "age": 30}'
print(json.dumps(["apple", "bananas"]))#'["apple", "bananas"]
print(json.dumps(("apple", "bananas")))#'["apple", "bananas"]
print(json.dumps("hello"))"hello"
print(json.dumps(42))#42
print(json.dumps(31.76))#31.76
print(json.dumps(True))#true
print(json.dumps(False))#false
print(json.dumps(None))#null