import json
import os
os.chdir(r"C:\Users\Admin\PycharmProjects\new project")

#dump ,dumps -->used to convert python to json (serialization or marshalling

#load , loads ---> used to conert json to python(Deseriallization or unmarshalling
data = {"name":"thanu","id":123}

'''x= json.dumps(data)
print(type(data))
print(x,type(x))

y= json.loads(x)
print(y,type(y))'''

##########################################################################################
#creating json file
with open("sample.json","w+") as file:


    json.dump(data,file)
    file.seek(0)
    data = json.load(file)
    print(data,type(data))
###############################################################################
import pickle

