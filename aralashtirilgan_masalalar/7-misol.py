matn = "Python anD data STRuctures are interesting!"

# matn ni parcha bilgilarini alohida element sifatida ruyxatga ta`minlaymiz
list_matn = list(matn)

# faqat kichik harflarni saqlash uchun list yaratib olamiz
list_alpha = []

# faqat kichik harflarni saqlash uchun shu loop dan foydalanamiz
for alpha in list_matn:
    if alpha.islower():
        list_alpha.append(alpha)
# natijani ekranga chop etamiz
print(list_alpha)