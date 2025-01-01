list_1 = [12, 55.6, "float", False, [1,2,3], "Abdurasul"]

new_list = []
for element in list_1:
    if type(element) == str:
        new_list.append(element.upper())
    else:
        new_list.append(element)
print(new_list)