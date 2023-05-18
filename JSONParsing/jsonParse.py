import json

f=open('sample_data.json')

data=json.load(f)
final_list=[]

parameters=data["parametersList"]

for each_parameter in parameters:
    dict={
        "parametersName":each_parameter["parameterName"],
        "min_value":each_parameter["min"],
        "max_value":each_parameter["max"],
        "avg_value":each_parameter["avg"]
    }
    final_list.append(dict)

# print(final_list)

json_list=json.dumps(final_list,indent=4)

with open("output.json", "w") as file:
    file.write(json_list)

f.close()
