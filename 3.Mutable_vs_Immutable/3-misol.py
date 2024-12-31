#4 ta elementga ega list yaratamiz
list_1 = [1, 2, 3, 4]

#list_1 nomli listimizni tuple ga o`zgartiramiz
list_tuple = tuple(list_1)

#list_tuple nomle tuple ni yana list_2 nomli listga o`zgartiramiz`
list_2 = list(list_tuple)

#list_2 nomli listimizni 3-indexini 77 ga o`zgartirdik
list_2[3] = 77

print(list_2)

