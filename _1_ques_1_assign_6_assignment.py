import json

# read file
myjsonfile = open('_python_assingments\_6_Assingment\employee.json', 'r')
jsondata = myjsonfile.read()

# parse
obj = json.loads(jsondata)


list = obj['Employees']
print("\nList of Employees in Dictionary formate:")
print(list)
print("\n")

for i in range(len(list)):
    print("S.N.",i+1, "------> Employee Details:")
    print("Name: ",list[i].get("name"))
    print("DOB: ",list[i].get("DOB"))
    print("Height: ", list[i].get("height"))
    print("City: ", list[i].get("city"))
    print("State: ", list[i].get("state"))
    print("\n")


