#Bu erda hohlasak list hohlasak esa tuple dan foydalanishimiz mumkin chunki shartimizda ruyxat elementlarini o`zgartirish haqida hichnima diyilmagan
tuple_1 = 21, "Akmal", 33.4, 23, "Bobur", "Muhammadjon", "AbduKarim", "Sobir", True, False
i = 0
#bush list yaratib olamiz
list_1 = []
#dastlabki 3 ta elementni listga joylab olamiz
while i < 3:
    list_1.append(tuple_1[i])
    i+=1

#oxirgi 3ta elementini listimizga qo`shib olamiz`
while i:
    list_1.append(tuple_1[len(tuple_1) - i])
    i-=1

#solishtirish uchun asil holatida chiqarib ko`ramiz`
print(list_1)

#listimiz elementlarini tiskariga chiqaramiz
print(list_1[::-1])