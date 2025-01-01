# 8 ta elementga ega tuple yaratamiz
tuple_1 = 21, 33, "type_list", True, False, 33.5, 44.6, "apple"

# tuple ni faqat toq elementlarini saqlash uchun list yaratib olamiz, chunki ubi birdan boshqa bir tuple ga saqlab bo`lmaydi chunki tuple immutabe hisoblanadi
list_1 = []

# faqat toq elementlarini list_1 ga ta`minlash uchun shu loopdan foydalanamiz
for element in range(0, 8, 2):
    if element % 2 == 0:
        list_1.append(tuple_1[element])
print(list_1) 