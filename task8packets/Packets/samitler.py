letter_list = ["a", "e", "i", "o", "u", "ə", "ü", "ı", "ö", " "]

def samitler_al():
    cumle = input("metn daxil edin: ").lower()
    new_list = []
    for i in cumle:
        if i not in letter_list and i.isalpha() and i not in new_list:
            new_list.append(i)
    if new_list:
        return new_list
    else:
        return "Icinde metn olan cavab daxil edin"

print(samitler_al())
