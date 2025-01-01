# 10 ta elementga ega list yaratamiz
list_1 = [12, 55.6, "float", False, [1,2,3], "Abdurasul", 10, True, 888, 777]

# Yangi list yaratish un list_2 nomli bo`sh list yaratib olamiz 
list_2 = []

# Har uchinchi elementni teskari tartibda yangi ro'yxatga olish uchun quyidagi loopdan foydalanamiz
for element in range(3, len(list_1), 3):
    list_2.append(list_1[len(list_1) - element])

# listimizni yangi tuple ga ugirib olamiz
list_tuple = tuple(list_2)

# tuple ni true qiymatiga ega elementimizni endikisini ekranga chop etamiz
print(list_tuple.index(True))