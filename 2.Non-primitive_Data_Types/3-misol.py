#list_1 nomli 2ta elementga ega list yaratdik va bu listimizning ikkala elemente ham tuple dan iborat
list_1 = [(1, 1.1, "Apple"), (True, False, 36, "Abdurasul")]

#bu erda biz list_1 ni 1 - endikisida turgan tuple ni 0-index ni o`zgartirishga harakat qilyabmiz ammo tuple ni qoidasiga ko`ra bu imkonsiz 
list_1[1][0] = False

print(list_1[1][0])#Bu erda esa xato bizga ogohlantirish beradi, ya`ni biz qoidaga zid ish qilyabmiz