# Bir funksiyanız olacaq, funksiyada random kitabxanadan istifadə edərək 20 nən 50 arası 5 rəqəm listə append edin.
# Həmən listdəki cüt  rəqəmləri math kitabxanası istifadə edərək kvadrata yüksəldin.


import random
import math
         # way 1
# list_num = [random.randint(20, 50) for _ in range(5)]
# print(list_num)
# modifed_list = [math.pow(a, 2) for a in list_num if a % 2 == 0]
# print(modifed_list)

        # way 2
list_num = []
for i in range(5):
    numbers = random.randint(20, 50)
    list_num.append(numbers)
print(list_num)

modifed_list = []
for a in list_num:
    if a % 2 == 0:
        modifed_list.append(math.pow(a, 2))
print(modifed_list)