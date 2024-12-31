matn = "Python programming is amazing!"

#biz split() function orqali matinlarni listlarga bo`lib tashlashda foydalanamiz
list_matn = matn.split()

word = ''
for i in list_matn:
    word += i[0]

print(word)