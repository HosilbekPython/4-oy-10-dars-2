
from collections import namedtuple


# ----------------------------------------------------------------------------

# 1 misol


# talaba_list = [
#     {'name' : "Hosilek" , 'age' : 21 , "majon" : "Python"},
#     {'name' : "Rystamov Asilbek" , 'age' : 18 , "majon" : "JAVA"},
#     {'name' : "Qodirjon" , 'age' : 17 , "majon" : "Frontend"}
# ]
#
# Talaba = namedtuple("Talaba" , ['name' , 'age' , "majon"])
#
# for user in talaba_list:
#     talabalar = Talaba(**user)
#     print(f"Ismi : {talabalar.name} Yoshi : {talabalar.age} Yo'nalishi : {talabalar.majon}")



# ----------------------------------------------------------------------------

# 2 misol


# product = [
#     {"product_name" : "Sabzi" , "price" : "1500 som" , "quantity" : "5 kilo"},
#     {"product_name" : "Kartoshka" , "price" : "3000 som" , "quantity" : "6 kilo"}
# ]
#
# Maxsulot = namedtuple("Maxsulot" , ["product_name" , "price" , "quantity"])
#
# for maxsulot in product:
#     maxsulotning = Maxsulot(**maxsulot)
#     print(f"Maxsulot nomi : {maxsulotning.product_name} Narxi : {maxsulotning.price} dan {maxsulotning.quantity}")
#



# ----------------------------------------------------------------------------

# 3 misol

# shaxar_royhati = [
#     {"city_name": "Andijon" , "country" : "O'zbekiston" , "population" : "50000"},
#     {"city_name": "Fargona" , "country" : "O'zbekiston" , "population" : "80000"},
#     {"city_name": "Namangan" , "country" : "O'zbekiston" , "population" : "45000"},
# ]
#
# Shaxar = namedtuple("Shaxarlar" , ["city_name" , "country" , "population"])
# shaxarlar_axolisi = []
#
# for shaxarcha in shaxar_royhati:
#     shaxarcha["population"] = int(shaxarcha["population"])
#     shaxarning = Shaxar(**shaxarcha)
#     print(f"Shaxarning davlati : {shaxarning.country} , Shaxar nomi : {shaxarning.city_name} , Axoli soni {shaxarning.population}")
#     shaxarlar_axolisi.append(shaxarning.population)
#
#
# for i in shaxar_royhati:
#     shaxarning2 = Shaxar(**i)
#     if shaxarning2.population == max(shaxarlar_axolisi):
#         print(f"Bular ichida eng axolisi kopi {shaxarning2.city_name} {shaxarning2.population} ")
#
# print(f"Bular ichida eng axolisi kopi {max(shaxarlar_axolisi)}")



# ----------------------------------------------------------------------------

# 4 misol



# avtomabil_listt = [
#     {"make" : "UzAvto" , "model" : "Nexia3" , 'year' : 2019},
#     {"make" : "UzAvto" , "model" : "Nexia2" , 'year' : 2014},
#     {"make" : "UzAvto" , "model" : "Cobalt" , 'year' : 2015},
# ]
#
#
# Avtomabil = namedtuple("Avto" , ["make" , "model" , 'year'])
#
# avtomabil_yilari = []
#
# for avtomabil in avtomabil_listt:
#     avtomabilning = Avtomabil(**avtomabil)
#     print(f"Avtomabil ishlab chiqargan kampaniya {avtomabilning.make} Avtomabil nomi : {avtomabilning.model} Yili : {avtomabilning.year} ")
#     avtomabil_yilari.append(avtomabilning.year)
#
# for avtomabil2 in avtomabil_listt:
#     avtomabilning = Avtomabil(**avtomabil2)
#     if avtomabilning.year == max(avtomabil_yilari):
#         print(f"Eng yangi avtomabil : {avtomabilning.model} yilii : {avtomabilning.year}")



# ----------------------------------------------------------------------------

# 5 misol

# def uzavto(avto_companiy):
#     def inner(avto_name):
#         nonlocal avto_companiy
#         return f"Avtomabil ishlab chiqargan Kampaniya {avto_companiy} avtomabil nomi {avto_name}"
#     return inner
#
# avto1 = uzavto("Uz Avo Motor")
# print(avto1("Nexia 3"))



# ----------------------------------------------------------------------------

# 6 misol

# def add_text(ism):
#     def inner():
#         nonlocal ism
#         return f"Assalom alekum {ism}"
#     return inner
# name1 = add_text("Hosilbek")
# print(name1())



# ----------------------------------------------------------------------------

# 7 misol

# def kiritlgan_sonda_amal1(kirtilganda:str):
#     if kirtilganda.isdigit():
#         kirtilganda = int(kirtilganda)
#         def inner():
#             return kirtilganda + 5
#         return inner
#     else:
#         return "Siz raqam kirtmadiznigiz"
#
# kirtilgan_son = '45'
# son1 = kiritlgan_sonda_amal1(kirtilgan_son)
# print(son1())


# ----------------------------------------------------------------------------

# 8 misol

# def birga_oshirish():
#     son = 0
#     def inner():
#         nonlocal son
#         son+=1
#         return son
#     return inner
# amal1 = birga_oshirish()
# print(amal1())
# print(amal1())
# print(amal1())
# print(amal1())
# print(amal1())
# print(amal1())




# ----------------------------------------------------------------------------

# 9 misol


# def kivadirat_qaytaruvchi():
#     def inner(raqam:int):
#         return raqam**2
#     return inner
#
# kvadirat1 = kivadirat_qaytaruvchi()
# print(kvadirat1(45))



# ----------------------------------------------------------------------------

# 10 misol


# name_list = ["temur" , 'sobir' , 'bakir']
#
# def listga_qoshish(new_name):
#     def inner():
#         global name_list
#         name_list.append(new_name)
#         return f"{new_name} royhatga qo'shildi \n Ro'yhat {name_list}"
#     return inner
#
# qoshish = listga_qoshish("Hosilbek")
# print(qoshish())


# ----------------------------------------------------------------------------

# 11 misol


# def maxsulot_name_skidka(name:str , royhat : dict):
#     def maxsulot_skidka_son(foiz:str):
#         if foiz.isdigit():
#             foiz = int(foiz)
#             for key , valu in royhat.items():
#                 valu = int(valu)
#                 if key == name:
#                     return valu * foiz /100 + valu
#     return maxsulot_skidka_son
#
#
# maxsulotlar = {"Iphon11" : '300' , "Iphon12" : '350' , "Iphon13" : '400'}
# maxsulot_nomlari = []
#
# for key , valu in maxsulotlar.items():
#     print(f"{key} narxi {valu}")
#     maxsulot_nomlari.append(key)
#
# print('Shu maxsulotlardan qaysi biriga skidka qilinsin ')
#
# skidka_nomi_kiritildi = 'Iphon11'
#
#
#
# if skidka_nomi_kiritildi in maxsulot_nomlari:
#     foiz_kiritildi = '10'
#     maxulot = maxsulot_name_skidka(skidka_nomi_kiritildi , maxsulotlar)
#     print(maxulot(foiz_kiritildi))
#
# else:
#     print("Bunday maxsulotimiz yoq ")





# ----------------------------------------------------------------------------

# 12 misol

# def maxsulotlar(maxsulot):
#     text = ""
#     def inner():
#         nonlocal text
#         text += maxsulot + " " * 2
#         return text
#
#     return inner
# maxsulot1 = maxsulotlar("non")
# print(maxsulot1())
# print(maxsulot1())
# print(maxsulot1())



# ----------------------------------------------------------------------------

# 13 misol

# def qator(birinchi_qator):
#     a = birinchi_qator
#     def keyingi_qatorlar(new):
#         nonlocal a
#         a += new
#         return a
#     return keyingi_qatorlar
#
# text = qator("assalom alkeum")
# print(text(" Hello"))
# print(text("Privet"))
# print(text("Privet"))


# ----------------------------------------------------------------------------

# 14 misol

# def sonlar(max_son):
#     def inner():
#         nonlocal max_son
#         for i in range(max_son):
#             if i%2==1:
#                 print(i)
#     return inner()
#
# s = sonlar(10)


# ----------------------------------------------------------------------------

# 15 misol

# def darajaga_kotarish(son):
#     def innier(daraja):
#         return son ** daraja
#     return innier
#
# son1 = darajaga_kotarish(41)
# print(son1(2))




# ----------------------------------------------------------------------------

# 16 misol

# def string_teskari_ogirish():
#     def inner(matin):
#         return matin[::-1]
#     return inner
#
# text = string_teskari_ogirish()
# print(text('Assalom'))


# ----------------------------------------------------------------------------

# 17 misol


# def savatga_qoshish_fun(dokon_maxsulotlari_dict: dict ):
#     def inner(savatda:list):
#         counter_suma = 0
#         for key, valu in dokon_maxsulotlari_dict.items():
#             if key in savatda:
#                 counter_suma += int(valu)
#         maxsulotlar = ", ".join(savatda)
#         print(f"\nSavatda {maxsulotlar}")
#         return f"Umumiy narx : {counter_suma}"
#     return inner
#
#
#
# dokonda = {"olma": "4000" , "anor" : "5000" , 'bexi' : '10000'}
#
# print("Do'kondagi maxsulotlar \n")
#
# for key , valu in dokonda.items():
#     print(f"{key} narxi {valu} som")
#
#
# savatdagi_maxsulotlar = "olma,anor".split(",")
#
# dokon1 = savatga_qoshish_fun(dokonda)
# print(dokon1(savatdagi_maxsulotlar))



# ----------------------------------------------------------------------------

# 18 misol

# def maxsulot_narxini_ozgartirish(maxsulot_royhati:dict):
#     def inner(maxsulot_nomi:str , maxsulot_yangi_narxi:str):
#         for key, valu in maxsulot_royhati.items():
#             if maxsulot_nomi in key :
#                 maxsulot_royhati[key] = maxsulot_yangi_narxi
#                 return f"{key} yangi {maxsulot_yangi_narxi} narxiga o'zgardi"
#             else:
#                 return "Bunday maxsulot yoq"
#     return inner
#
#
# dokonda = {"olma": "4000" , "anor" : "5000" , 'bexi' : '10000'}
# # dokonda_maxsulotlar_nomi = []
#
# print("Do'kondagi maxsulotlar \n")
#
# for key , valu in dokonda.items():
#     # dokonda_maxsulotlar_nomi.append(key)
#     print(f"{key} narxi {valu} som")
#
#
# # savatdagi_maxsulotlar = "olma,anor".split(",")
#
#
# ozgarish1 = maxsulot_narxini_ozgartirish(dokonda)
# print(ozgarish1("olma" , "555"))
# print(dokonda)

























