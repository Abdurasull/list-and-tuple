matn = "Learning Python is fun!"

#split() methodimiz orqali matndagi har bir so`zni alohida qilib list ga joylab olamiz
list_1 = matn.split()

#list imizni tuple ga o`zgartirib olamiz
tuple_1 = tuple(list_1)

#va oxirgi so`zimizni indexini chop etamiz`
print("oxirgi 'fun!' so`zimizning indexi {}".format(tuple_1.index("fun!")))