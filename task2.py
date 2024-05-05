# TASK1
# mylist=[-2,3,7,9,16,25,36,49,64,81,100]
# modifiedList = []

# def netice():
#     for i in mylist:
#         if i<0:
#             continue
#         elif float(pow(i, 0.5)) == int(pow(i, 0.5)):  # bu setiri elif float(pow(i, 0.5)).is_integer(): evez etmek olar
#             modifiedList.append(i)
#         else:
#             continue
# netice()
# print(modifiedList)

#  TASK2
# inputList = [-1,1,2,2,6,7,5,4,4,7,'say']
# modifiedList = []

# def netice():
#     for i in inputList:
#         if inputList.count(i) > 1:
#             continue
#         else :
#             modifiedList.append(i)

# netice()
# print(modifiedList)




# TASK 3
# def hasil():
#     ededler = input("ededleri daxil edin: ").split()
#     saver = 1
#     for i in ededler:
#         saver *= int(i)
#     return saver
# print(hasil())



# TASK4
# number = int(input("eded daxil edin: "))

#                 #   list comprehension
# print([i for i in range(1, number+1) if number % i == 0])

               #funksya ile
# def bolentap():
#     number = int(input("eded daxil edin: "))
#     i = 1
#     bolenler = []
#     while i <= number:
#         if number % i == 0:
#             bolenler.append(i)
#         i += 1
#     print(bolenler)

# bolentap()



# TASK5
# mylist=['may','iyun','iyul']
# myDict = {i: len(i) for i in mylist}
# print(myDict)


# TASK6
# given = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

#         # list comprehesion ile
# print([i.split()[0] for i in given])          

#         # loop elave ederk
# new = []
# for i in given:
#     new.append(i.split())

# names = [i[0] for i in new]
# print(names)


# TASK7
# nums1 = [1, 2, 5]
# nums2 = [4, 5, 6]
        #  umumi funksiya ile
# def hesab(a, b):
#     results = []
#     for i in range(len(a)):
#         results.append((a[i]+b[i])/2)
#     return results

# print(hesab(nums1, nums2))


        #   for ile
# results = []
# for i in range(len(nums1)):
#     results.append((nums1[i]+nums2[i])/2)
# print(results)

