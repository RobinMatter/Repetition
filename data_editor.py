import json
jsonfile = open("data.json")
data_input = jsonfile.read()
data = json.loads(data_input)
jsonfile.close()

key_saver = []
print(data)
dict = {}
for element in data:
    key_from_element = list(element)[0]d
    print(key_from_element)
    key_saver[1:1] = [key_from_element]
print(key_saver)



#
# for element in self.__data_list:
#     print("B", key, value, element)
#     if key == list(element)[0]:
#         element[key] += value
#         data.append({key: value})
#         with open('data.json', 'w') as jsonfile:
#             json.dump(data, jsonfile)