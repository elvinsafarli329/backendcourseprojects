def samitler_al():
    letter_list = ["a", "e", "i", "o", "u", "ə", "ü", "ı", "ö" ]
    new_list = []
    cumle = input("metn daxil edin: ").split()
    for i in cumle:
        if i not in letter_list:
            new_list.append(i)