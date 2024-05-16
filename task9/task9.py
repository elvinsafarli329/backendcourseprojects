# 1) taskınız ilk olaraq bir text faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız .
# 2) daha sonra həmin textin ilk sətrindəki  sözlərin bütün hərflərini böyük hərflərə çeviririk .
# 3) Ən sonda bu sözləri başqa  bir text faylı yaradıb onun içərisində yazırıq.

import os

with open("task9.txt", mode="x", encoding="utf-8") as new_txt:
    new_txt.write("yeni txt file acildi \nsalam \njsjsjssj")

with open("task9.txt", mode="a") as new_txts:
    new_txt = ["\nNecesen?", "\nhello", "\nbyebye"]
    new_txts.writelines(new_txt)

setr_sayi = 0
with open("task9.txt", mode="r", encoding="utf-8") as setirler:
    for setr in setirler:
        setr_sayi +=1
        if setr_sayi == 1:
            setr1 = setr.strip().upper() 
            break 

setr1_upper = setr1.upper()
with open("task9_modified.txt", mode="w", encoding="utf-8") as new_file:
    new_file.write(setr1_upper)