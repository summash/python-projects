info={'name':'karan','age':17,'eligiblilit':False}
print(type(info))
print(info.get('name2'))#will not show error if value is not present
print(info['name'])#will give an error
print(info.keys())
for key in info.keys():
    print(f"the value corresponding to the key{key} is {info[key]}")
print(info.items())
for key,value in info.items():
    print("the value corresponding to the key{key} is {value}")