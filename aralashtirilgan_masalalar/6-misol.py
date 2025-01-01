# 3 ta ruyxat elementlaridan iborat ruyxat hosil qilamiz
list_1 = [[1, 2, 4, 5], [44, 65, 43, 11], ["apple", "orange", True, False]]

# ichki ruyxatlarni oxirqi elementlarini saqlash uchun list yaratib olamiz
list_2 = []

# ichki ruyxatlarni oxirqi elementlarini saqlash uchun shu loop dan foydalanamiz
for items in list_1:
    list_2.append(items[len(items) - 1])

# yangi listimizni tuple ga o`zgartiramiz
tuple_1 = tuple(list_2)

# natijani ekranga chiqaramiz
print(tuple_1)

