
# Fn28 guruh To'htarov Hosilbek
# 4 oy 8 dars

# ------------------------------------------------------------------------------------

# 1 misol

# def daraja(son):
#     return son**2
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# daraja = map(daraja , numbers)
# print(list(daraja))


# ------------------------------------------------------------------------------------

# 2 misol

# def filerlash(harf: str):
#     return harf.isupper()
#
# royhat = ["A", "a", "B", "b", "C", "c", "D", "d"]
# fil = filter(filerlash , royhat)
# print(list(fil))


# ------------------------------------------------------------------------------------

# 3 misol

# def telefon_numer_filter(number : str):
#
#     if number.startswith("+998"):
#         return "UZ" , number
#
#     elif number.startswith("+7945"):
#         return "RU" , number
#
#     elif number.startswith("+1438"):
#         return "EN" , number
#
#     else:
#         return "NOMALUM" , number
#
#
#
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# natija = map(telefon_numer_filter , phone_numbers)
#
# for dav , tel in list(natija):
#     print(f"Davlat = {dav} Tilifon raqam = {tel}")


# ------------------------------------------------------------------------------------

# 4 misol

# def uporer_qilish(text : str):
#     return text.title()
#
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# natija = map(uporer_qilish , names)
# print(list(natija))

# ------------------------------------------------------------------------------------

# 5 misol


# def tekshirish(son : int):
#     return son > 75
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# natija = filter(tekshirish , scores)
# print(list(natija))

# ------------------------------------------------------------------------------------

# 6 misol

# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
#
# natija = filter(lambda text : text.lower()[::-1] == text.lower(), words)
# print(list(natija))

# ------------------------------------------------------------------------------------

# 7 misol

# def len_topish(text):
#     return len(text)
#
#
# royhat = ['apple', 'banana', 'cherry']
# natija = map(len_topish , royhat)
# print(list(natija))

# ------------------------------------------------------------------------------------

# 8 misol

# def test_birlashtirish(text1 , text2):
#     return text1+text2
#
# matin1 = ['apple', 'banana', 'cherry']
# matin2 = ['orange', 'lemon', 'pineapple']
#
# natija = map(test_birlashtirish , matin1 , matin2)
# print(list(natija))


# ------------------------------------------------------------------------------------

# 9 misol


# royhat1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# royhat2 = ["Sobir", "Bakir", "Jalil", "Toxir"]
# new_royhat2 = royhat1 + royhat2
#
# print(new_royhat2)

# ------------------------------------------------------------------------------------

# 10 misol


# royhat = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# funksiya = lambda royhat , elemnt : [son for son in royhat if son == elemnt]
#
# natija = funksiya(royhat,21)
#
# print(len(natija))

# ------------------------------------------------------------------------------------

# 11 misol

# def funk(royhat: list):
#     for i in royhat:
        # royhat.count(i)

# royhat1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# royhat2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# umumiy = list(map(lambda x : x if x in royhat2 else None , royhat1))
# natija = [x for x in umumiy if x is not None]
# print(natija)


# ------------------------------------------------------------------------------------

# 12 misol

# def toq_chiqarish(matin):
#     for i in range(len(matin)):
#         if i % 2 ==0:
#             print(matin[i])
#
# elemet= ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# toq_chiqarish(elemet)

# ------------------------------------------------------------------------------------

# 13 misol



# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
#
# boshlash_nuqta = programming_languages.index("Basic")
# natija = programming_languages[boshlash_nuqta:]
# print(natija)


# ------------------------------------------------------------------------------------

# 14 misol

# talabalar = [
#     ['Ali', '1-A', 85.5],
#     ['Laylo', '1-B', 91.0],
#     ['Bekzod', '2-A', 76.0],
#     ['Said', '2-B', 88.5],
#     ['Olim', '3-A', 92.5]
# ]
#
# yuqori_baxo = max(talabalar , key=lambda talaba : talaba[2])
# print(f"Eng yuqori bahoga ega talaba: {yuqori_baxo[0]}, Guruh: {yuqori_baxo[1]}, Baho: {yuqori_baxo[2]}")



# ------------------------------------------------------------------------------------

# 15 misol


# def kivadirat(son):
#     return son**2
#
# listda = []
# for i in range(21):
#     listda.append(i)
#
# natija = map(kivadirat , listda)
# print(list(natija))






# ------------------------------------------------------------------------------------

# 16 misol

# def uzunlik(text):
#     return len(text)
# matin = ["Assalom alekum"]
# natija = map(uzunlik , matin)
# print(list(natija))


# ------------------------------------------------------------------------------------

# 17 misol

# def salomlashish(ism):
#     return f"Assalom alekum {ism}"
#
# ism_kiritish = input("Ismingizni kiritng : ")
# ism = [ism_kiritish]
# natija = map(salomlashish , ism)
# print(list(natija)[0])



