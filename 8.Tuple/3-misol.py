list_1 = [
        (1, 3, 2), 
        (6, 3, 5), 
        (2, 3, 4), 
        (1, 2, 3), 
        (2, 5, 3)]


#bu erda barcha tuple dagi elementalrni listga chiqarib olish uchun all_tuples nomli list yaratib olamiz
all_tuples = []

#Bu erda listimizga barcha tuple elementlarini set() function orqali takrorlanuvchi elementlarni faqat bittasini olamiz
for tuples in list_1:
    all_tuples.append([element for element in set(tuples)])

#bu erda esa barcha tuple dagi elementlarni listga o`tgazib olamiz
all_elements = [element for lists in all_tuples for element in lists]

#Va oxirgi bo`lim ya`ni barcha tuple larga tegishli bo`lgan elementni topish un ularni sonini dastlabki tuplelarda iborat bo`lgan listimizni uzunlihi bn solishtirib topib olamiz
for i in set(all_elements):
    if all_elements.count(i) == len(list_1):
        print(i)
