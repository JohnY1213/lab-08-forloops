myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755} 

keys = list(myData.keys())
values = list(myData.values())


for k,v in myData.items():
    print("key: "+ k + ","+ " value:",v)

print("ALL KEYS: " , keys)
print("ALL VALUES: " , values)