tuple_1 = 12, 55.6, True, False, 6, 8, 6, 55, 12, False, False, False, 6
max = 0

for element in set(tuple_1):
    if max < tuple_1.count(element):
        max = tuple_1.count(element)
        max_value = element

print("Eng ko`p takrorlangane element: {}, {} marta takrorlandi".format(max_value, max))
