#Bu erda biz ruyxat yaratish uchun tuple dan foydalanamiz, chunki biz ruyxatimiz elementlarini o`zgartirish imkonsiz ekanini isbotlash uchun :)

list_1 = 2, 6, "Akmal", True#biz tuple yaratishda uning elementlarini ()ichiga joylashtirishimiz biz qachonki bitta elementga ega tuple yaratayotganimizda kk bo`ladi qolgan vaqtda foydalanmasak ham hato bo`lmaydi

#Bu erda o`zgartirishimizdan oldingi 2-indexdagi elemint qiymatini chop etamiz
print(list_1[2])

#BU erda esa list_1 nomli ruyxatimizni 2- indexini Boburga o`zgartirtirishga harakat qilamiz
#ammo bu hatolikga olib keladi chunki tuple immutable hisoblanadi ya`ni o`zgarmas
list_1[2] = "Bobur"
