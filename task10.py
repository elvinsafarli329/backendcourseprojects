"""
Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara görə neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə  düzgün olmayacaq. (taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)
Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.
"""

# task1
import os
import shutil
from pathlib import Path

os.mkdir("Example")
os.makedirs("Example/subdirect")

photo = 'bookimage.jpeg'
with open("metn.txt", mode="a") as lorem:
    lorem.write("\nyeni txt file")

shutil.move(photo, "Example/subdirect")
shutil.move("metn.txt", "Example/subdirect")

axtarilan = "Example/subdirect"

with Path(axtarilan) as folder:
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(".txt"):
           shutil.move(file, "Example")

# task2
def siralar(xallar):
    neticeler = []
    for i, num in enumerate(xallar):
        rank = 1
        for novbeti_eded in xallar:
            if num < novbeti_eded:
                rank += 1
        neticeler.append(f"{rank}-ci yer")
    return neticeler

xallar = [8, 10, 5, 7, 9]
cavab = siralar(xallar)
print(cavab) 
