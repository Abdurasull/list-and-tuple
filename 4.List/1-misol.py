#random kutubxonasini chaqirib olamiz (bizga masalani bunday ishlash aytilmagan ammo 100 ball ning shartiga ko`ra mukammal ishlashim kk)
import random

#list_1 nomli bush list yaratib olaman
list_1 = []
#for loop imizni 10 marta aylantiramiz
for i in range(10):
    #10 va 50 orasidagi random sonlarni listimizga qo`shish uchun randomni randint methodiga murojat qilamiz va unga argumint sifatida 10 va 50 ni kiritamiz
    list_1.append(random.randint(10, 50))
    
    
#natijani chop etamiz
print(list_1)
