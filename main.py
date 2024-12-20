
# Fn28 4 oy 9 dars

# --------------------------------------------------------------------------------------------

# 1 misol

# import time
# from threading import Thread
#
# yigindi = None
#
#
# def raqamlar_yigindisi(raqam:int):
#     global yigindi
#     uzunligi = len(str(raqam))
#     raqamlar = []
#     for i in range(uzunligi):
#         oxirgi_raqam = raqam % 10
#         raqamlar.append(oxirgi_raqam)
#         raqam = int((raqam - oxirgi_raqam) / 10)
#     yigindi = sum(raqamlar)
#
# son = 1548
#
# start = time.time()
# th = Thread(target=raqamlar_yigindisi , args=(son,))
# th.start()
# th.join()
#
# end = time.time()
# print(f"Ish bajarilguncha {round((end-start) , 2)} vaqt ketidi {son} ning raqamlar yig'indisi {yigindi}")



# --------------------------------------------------------------------------------------------

# 2 misol

# from threading import Thread
#
# natija = None
#
# def sekundan_kunlarga_otish(sekund):
#     global natija
#     minut = None
#     soat = None
#     kun = None
#     if sekund > 60:
#         minut = sekund // 60
#         sekund_qoldiq = sekund % 60
#         if minut > 60:
#             soat = minut // 60
#             minut_qoldiq = minut % 60
#             if soat > 24:
#                 kun = soat // 24
#                 soat = soat % 24
#                 natija = f"{kun} kun , {soat} soat , {minut_qoldiq} minut , {sekund_qoldiq} sekund  dan iborat"
#             else:
#                 natija = f"{soat} soat , {minut_qoldiq} minut , {sekund_qoldiq} sekund  dan iborat"
#         else:
#             natija = f"{minut} minut , {sekund_qoldiq} sekund  dan iborat"
#     else:
#         natija = f"{sekund} sekund"
#
#
#
# a = 60450546
# th = Thread(target=sekundan_kunlarga_otish , args=(a,))
# th.start()
# th.join()
#
# print(f"Siz kirtgan {a} soniya {natija}")



# --------------------------------------------------------------------------------------------

# 3 misol

# from threading import Thread
#
#
# def title_qilish(text:str):
#     global title_sozlar
#     if text.isalpha():
#         title_sozlar.append(text.title())
#
# title_sozlar = []
# names = ['alfred', 'tabitha', 'william', 'arla']
# thredinglar = []
#
# for i in names:
#     the = Thread(target=title_qilish , args=(i,))
#     thredinglar.append(the)
#     the.start()
#
# for j in thredinglar:
#     j.join()
#
# print(title_sozlar)

# --------------------------------------------------------------------------------------------

# 4 misol

# from threading import Thread
#
# def katalik_quiz(son:int):
#     global katalar_raqamlar
#     if son >= 75:
#         katalar_raqamlar.append(son)
#
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# katalar_raqamlar = []
# thredinglar = []
#
# for i in scores:
#     the = Thread(target=katalik_quiz , args=(i,))
#     thredinglar.append(the)
#     the.start()
#
# for j in thredinglar:
#     j.join()
#
# print(katalar_raqamlar)

# --------------------------------------------------------------------------------------------

# 5 misol

# from threading import Thread
#
# def palindrom_quiz(text:str):
#     global palidrom_list
#     teskari_text = text[::-1].lower()
#     if text.lower() == teskari_text:
#         palidrom_list.append(text)
#
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# palidrom_list= []
# thredinglar =[]
#
# for i in words:
#     thr = Thread(target=palindrom_quiz , args=(i,))
#     thredinglar.append(thr)
#     thr.start()
#
# for i in thredinglar:
#     i.join()
#
# print(palidrom_list)

# --------------------------------------------------------------------------------------------

# 6 misol

# from threading import Thread
#
#
# def matin_e_ni_ozgartirish(harf):
#     global matin_list
#
#     if soz[i] == "e":
#         matin_list.append("3")
#     else:
#         matin_list.append(soz[i])
#
# soz = "elanea"
# harflar_soni = len(soz)
# i = 0
#
# matin_list = []
# threding =[]
# while i < harflar_soni:
#     the = Thread(target=matin_e_ni_ozgartirish , args=(soz[i], ))
#     threding.append(the)
#     the.start()
#     i= i + 1
#
# for l in threding:
#     l.join()
#
# text = "".join(matin_list)
# print(text)

# --------------------------------------------------------------------------------------------

# 7 misol

# from threading import Thread
#
# def matindaan_bosh_joy_olish(harf):
#     global new_matin_list
#     if harf != " ":
#         new_matin_list.append(harf)
#
#
# matin = "assalom alekum"
#
# new_matin_list = []
# harflar_soni = len(matin)
# treding = []
# i = 0
#
# while i < harflar_soni:
#     th = Thread(target=matindaan_bosh_joy_olish , args=(matin[i],))
#     treding.append(th)
#     th.start()
#     i +=1
#
# for i in treding:
#     i.join()
#
# natija = "".join(new_matin_list)
# print(natija)

# --------------------------------------------------------------------------------------------

# 8 misol

# from threading import Thread
#
# def kivadiratga(son:int):
#     global kivadirat_royhat
#     kivadirat_royhat.append(son**2)
#
# royhat = [1,2,3,4,5,10,9,8,7,6]
# kivadirat_royhat = []
# thredinlar = []
#
# for i in royhat:
#     th = Thread(target=kivadiratga , args=(i,))
#     thredinlar.append(th)
#     th.start()
#
# for k in thredinlar:
#     k.join()
#
# print(kivadirat_royhat)

# --------------------------------------------------------------------------------------------

# 9 misol

# from threading import Thread
# import random
#
# def tasodifiy_son():
#     global tasodifiy_sonlar_royhati
#     son = random.randint(1,100)
#     tasodifiy_sonlar_royhati.append(son)
#
# tasodifiy_sonlar_royhati = []
# tredinglar = []
#
# for i in range(10):
#     th = Thread(target=tasodifiy_son)
#     tredinglar.append(th)
#     th.start()
#
# for j in tredinglar:
#     j.join()
#
# print(tasodifiy_sonlar_royhati)


