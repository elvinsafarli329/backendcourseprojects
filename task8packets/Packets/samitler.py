letter_list = ["a", "e", "i", "o", "u", "ə", "ü", "ı", "ö", " "]

def samitler_al():
    cumle = input("metn daxil edin: ").lower()
    new_list = set()
    for i in cumle:
        if i not in letter_list:
            new_list.add(i)
    return list(new_list)

print(samitler_al())

