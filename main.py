# FN28 uy ishi

# ---------------------------------------------------------------------------------------

# 1 misol

# class FayildagiRaqamlarniQoshish:
#     def __init__(self , filename , mode = "r" , encoding = "utf-8" ):
#         self.filename = filename
#         self.mode = mode
#         self.encoding = encoding
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename , self.mode , encoding=self.encoding)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with FayildagiRaqamlarniQoshish("birinchi_misol_uchun.txt") as l:
#     royhat = []
#     a = l.read()
#     b = a.split(" ")
#     for i in b:
#         royhat.append(int(i))
#     print(sum(royhat))




# ---------------------------------------------------------------------------------------


# Barcha misolar multiprocessing da ishlansin.

from multiprocessing import Process , Queue
import time
import random

# ---------------------------------------------------------------------------------------

# 1 misol


# def royhatdagi_raqamlar_yigindisi(royhat:list , q :Queue):
#     yigindi = 0
#     i = 0
#     while i < len(royhat):
#         yigindi += royhat[i]
#         i +=1
#     q.put(yigindi)
#
#
# if __name__ == "__main__":
#     q = Queue()
#     royhatdagi_sonlar = [1,2,3,4,5,6]
#     pro = Process(target=royhatdagi_raqamlar_yigindisi , args=(royhatdagi_sonlar , q))
#     pro.start()
#     pro.join()
#     print(q.get())


# ---------------------------------------------------------------------------------------

# 2 misol

# def royhat_aralshtirish(royhat : list , q:Queue):
#     random.shuffle(royhat)
#     q.put(royhat)
#
#
# if __name__ =="__main__":
#     q = Queue()
#     royhat_asil = [1, 2, 3, 4]
#     pr = Process(target=royhat_aralshtirish , args=(royhat_asil , q))
#     pr.start()
#     pr.join()
#     print(q.get())

# ---------------------------------------------------------------------------------------

# 3 misol

# def max_and_min(royhat: list , max_son:Queue , min_son:Queue):
#     max_son.put(max(royhat))
#     min_son.put(min(royhat))
#
# if __name__ == "__main__":
#     katta = Queue()
#     kichik = Queue()
#
#     royhat = [4,5,9,8,72,3,98]
#     yuborish = Process(target=max_and_min , args=(royhat , katta , kichik))
#     yuborish.start()
#     yuborish.join()
#     print(katta.get())
#     print(kichik.get())

# ---------------------------------------------------------------------------------------

# 4 misol

# def borlikga_tekshirish(royhat:list , q:Queue):
#     if royhat:
#         q.put("Ro'yhatda malumotlar bor")
#     else:
#         q.put("Ro'yhat bosh")
#
# if __name__ == "__main__":
#     q = Queue()
#     royhatimiz = [4]
#     pr = Process(target=borlikga_tekshirish , args=(royhatimiz , q))
#     pr.start()
#     pr.join()
#
#     print(q.get())

# ---------------------------------------------------------------------------------------

# 5 misol

# def takrorlanganlar_olib_tashlash(royhat:list , q :Queue):
#     new_royhat = []
#     for i in royhat:
#         if i not in new_royhat:
#             new_royhat.append(i)
#     q.put(new_royhat)
#
# if __name__ == "__main__":
#     q = Queue()
#     royhat = [1,2,3,3,5,6,66,7,8,9,88,88,66,6,7]
#     pr = Process(target=takrorlanganlar_olib_tashlash , args=(royhat , q))
#     pr.start()
#     pr.join()
#     print(q.get())

# ---------------------------------------------------------------------------------------

# 6 misol

# def royhat_matin_teskari(royhat:list[str] , q:Queue):
#     teskari_royhat = []
#     for i in royhat:
#         if i.isalpha():
#             teskari_royhat.append(i[::-1])
#
#     q.put(teskari_royhat)
#
#
# if __name__ == "__main__":
#     q = Queue()
#     royhat = ["assalom" , "hello" , "privet"]
#     pro = Process(target=royhat_matin_teskari , args=(royhat ,q))
#     pro.start()
#     pro.join()
#     print(q.get())

# ---------------------------------------------------------------------------------------

# 7 misol

# def eng_uzunini_topsih(royhat :list , q :Queue):
#     eng_uzuni = royhat[0]
#     for i in royhat:
#         if len(i)>len(eng_uzuni):
#             eng_uzuni = i
#
#     q.put(eng_uzuni)
#
# if __name__ =="__main__":
#     q = Queue()
#     matinlar = ["assalom" , 'alekum' , 'hello' , 'privet']
#     pro = Process(target=eng_uzunini_topsih , args=(matinlar , q))
#     pro.start()
#     pro.join()
#
#     print(q.get())

# ---------------------------------------------------------------------------------------

# 8 misol

# def takrprlanganlar_aliqlash(royhat : list , q:Queue):
#     takrorlanganlar = []
#     for i in royhat:
#         counterda = royhat.count(i)
#         if counterda > 1 and i not in takrorlanganlar:
#             takrorlanganlar.append(i)
#
#     q.put(takrorlanganlar)
#
# if __name__ == "__main__":
#     q = Queue()
#     royhat = [1,2,3,3,5,6,66,7,8,9,88,88,66,6,7]
#     pro = Process(target=takrprlanganlar_aliqlash , args=(royhat , q))
#     pro.start()
#     pro.join()
#     print(q.get())


# ---------------------------------------------------------------------------------------

# 9 misol

# def raqamlarni_ajratish(royhat:list[str|int] , q :Queue):
#     raqamlar = []
#     for i in royhat:
#         if isinstance(i , int) or i.isdigit():
#             raqamlar.append(int(i))
#     q.put(raqamlar)
#
# if __name__ =="__main__":
#     q = Queue()
#     royhat = [1,2 , 'Assalom' , "456",3,3,5 ,"hhh",6,'66',7,8,9,88,88,66,6,7]
#     pro = Process(target=raqamlarni_ajratish , args=(royhat , q))
#     pro.start()
#     pro.join()
#     print(q.get())


# ---------------------------------------------------------------------------------------

# 10 misol

# def raqamlarni_ajratish(royhat:list[str|int] , q :Queue):
#     raqamlar = []
#     for i in royhat:
#         if isinstance(i , int) or i.isdigit():
#             raqamlar.append(int(i)*2)
#         else:
#             raqamlar.append(i)
#     q.put(raqamlar)
#
# if __name__ =="__main__":
#     q = Queue()
#     royhat = [1,2 , 'Assalom' , "456",3,3,5 ,"hhh",6,'66',7,8,9,88,88,66,6,7]
#     pro = Process(target=raqamlarni_ajratish , args=(royhat , q))
#     pro.start()
#     pro.join()
#     print(q.get())



# ---------------------------------------------------------------------------------------

# 11 misol

# def diksheriydagi_katta_qiymat_topish(dikt :dict , q : Queue , q1:Queue):
#     katta_key = next(iter(dikt))
#     eng_katta_valu = dikt[katta_key]
#
#     for key , value in dikt.items():
#         if value > eng_katta_valu:
#             katta_key = key
#             eng_katta_valu = value
#
#     q.put(katta_key)
#     q1.put(dikt[katta_key])
#
# if __name__=="__main__":
#     q = Queue()
#     q1 = Queue()
#     my_dict = {'a': 10, 'b': 200, 'c': 55}
#     pr = Process(target=diksheriydagi_katta_qiymat_topish , args=(my_dict , q , q1))
#     pr.start()
#     pr.join()
#     print(q.get())
#     print(q1.get())



# ---------------------------------------------------------------------------------------

# 12 misol

# def raqamlar_ortacha_qiymati(royhat:list , q:Queue):
#     yigindisi = sum(royhat)
#     soni = len(royhat)
#     q.put(yigindisi/soni)
#
# if __name__ =="__main__":
#     q = Queue()
#     royhatda =[1,2,3,4,5,6,7,8,9]
#     pr = Process(target=raqamlar_ortacha_qiymati , args=(royhatda , q))
#     pr.start()
#     pr.join()
#
#     print(q.get())



# ---------------------------------------------------------------------------------------

# 13 misol

# def ikkta_royhat_birlashtirish(royhat1 :list , royhat2:list , q:Queue):
#     if royhat1 and royhat2:
#         royhat1.extend(royhat2)
#         q.put(royhat1)
#
# if __name__=="__main__":
#     q = Queue()
#     ro1 = [1,2,3]
#     ro2 = [4,5,6]
#     pro = Process(target=ikkta_royhat_birlashtirish , args=(ro1 , ro2 , q))
#     pro.start()
#     pro.join()
#     print(q.get())



# ---------------------------------------------------------------------------------------

# 14 misol


# def eng_uzun_eng_kalta_key(my_dikt :dict , q1:Queue , q2 :Queue):
#     katta_key = next(iter(my_dikt))
#     for key , valu in my_dikt.items():
#         if len(katta_key)<len(key):
#             katta_key = key
#     q1.put(katta_key)
#     kichik_key = next(iter(my_dikt))
#     for key, valu in my_dikt.items():
#         if len(kichik_key) > len(key):
#             kichik_key = key
#     q2.put(kichik_key)
#
# if __name__=="__main__":
#     q1 = Queue()
#     q2 = Queue()
#     my_dict = {'alfa': 10, 'bet': 200, 'gammmaa': 55}
#     pro =Process(target=eng_uzun_eng_kalta_key , args=(my_dict , q1 , q2))
#     pro.start()
#     pro.join()
#     print(f"Eng katta key = {q1.get()}")
#     print(f"Eng kichik key = {q2.get()}")




# ---------------------------------------------------------------------------------------

# 15 misol

# def royhatdagi_raqamlarni_int_qilish(royhat:list[str] , q =Queue):
#     new_royhat = []
#     for i in royhat:
#         if i.isdigit():
#             new_royhat.append(int(i))
#         else:
#             new_royhat.append(i)
#     q.put(new_royhat)
#
# if __name__=="__main__":
#     q = Queue()
#     royhat = ["assalom" , "4" , "ss" ,"78" , "56"]
#     pro = Process(target=royhatdagi_raqamlarni_int_qilish , args=(royhat, q))
#     pro.start()
#     pro.join()
#
#     print(q.get())


# ---------------------------------------------------------------------------------------

# 16 misol

# def royhatdagi_qiymatlarini_2_ga_kopaytirish(royhat:list[int] , q:Queue):
#     new_royhat = []
#     for i in royhat:
#         new_royhat.append(i*2)
#     q.put(new_royhat)
#
# if __name__ =="__main__":
#     q = Queue()
#     royhat = [1,2,3,4,5,6]
#     pr = Process(target=royhatdagi_qiymatlarini_2_ga_kopaytirish , args=(royhat , q))
#     pr.start()
#     pr.join()
#     print(q.get())

# ---------------------------------------------------------------------------------------

# 17 misol


# def stringi_teskari_qilish(royhat:list[str|int] , q:Queue):
#     new_royhat = []
#     for i in royhat:
#         if isinstance(i , str) and i.isalpha():
#             new_royhat.append(i[::-1])
#         else:
#             new_royhat.append(i)
#     q.put(new_royhat)
#
# if __name__=="__main__":
#     q = Queue()
#     royhatda = ['assalom' , "hello" , 4 ,8 ,"alik"]
#     pro = Process(target=stringi_teskari_qilish , args=(royhatda, q))
#     pro.start()
#     pro.join()
#     print(q.get())






