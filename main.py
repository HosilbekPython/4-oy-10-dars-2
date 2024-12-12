
# 1 misol

# ---------------------------------------------------------------------

# class IteratorYaratish:
#     def __init__(self):
#         self.start = 1
#         self.stop = 10
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.stop:
#             raqam = self.start
#             self.start += 1
#             return raqam
#         else:
#             raise StopIteration ("Element qolmadi !!")
#
#
# iterator = IteratorYaratish()
# natija = iterator.__iter__()
# print(natija.__next__())
# print(natija.__next__())
#
# for i in natija:
#     print(i)



# ---------------------------------------------------------------------

# 2 misol

# list_royhat = ['bir' , 'ikki' , 'uch' , 'tort' , 'besh']
# iter_yaratish = list_royhat.__iter__()
# print(iter_yaratish.__next__())
# print(iter_yaratish.__next__())
# print(iter_yaratish.__next__())
# print(iter_yaratish.__next__())

# ---------------------------------------------------------------------

# 3 misol

# list_royhat = ['bir' , 'ikki' , 'uch' , 'tort' , 'besh']
#
#
# class TeskariIterableChiqarish:
#     def __init__(self , royhat):
#         self.__royhat = royhat
#         self.__start = len(self.__royhat)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__start >= 1:
#             self.__start += -1
#             return self.__royhat[self.__start]
#         else:
#             raise StopIteration("Element qolmadi !!!")
#
#
# royhat1 = TeskariIterableChiqarish(list_royhat)
# print(next(royhat1))
# print(next(royhat1))
# print(next(royhat1))
# print(next(royhat1))
# print(next(royhat1))


# ---------------------------------------------------------------------

# 4 misol

# text = " Assalom alekum , Hello World , Salom , hello"
#
# class QatorniIteratsiyaQilish:
#     def __init__(self , text:str):
#         self.__text = text
#         self.__elemnt = -1
#         self.__hariflar = [letter for word in text.split(" ") for letter in word]
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__elemnt += 1
#         if self.__elemnt >= len(self.__hariflar):
#             raise StopIteration("Element qolmadi !!!")
#         return self.__hariflar[self.__elemnt]
#
# qator1 = QatorniIteratsiyaQilish(text)
# qator_iter = qator1.__iter__()
# print(qator_iter.__next__())
# print(qator_iter.__next__())
# print(qator_iter.__next__())

# ---------------------------------------------------------------------

# 5 misol

# class FilterItarable:
#     def __init__(self , max_son):
#         self.__max_son = max_son
#         self.__min_son = -1
#         self.__juft_sonlar = [num for num in range(1 ,self.__max_son +1) if num % 2 == 0]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__min_son += 1
#         if self.__min_son < len(self.__juft_sonlar):
#             return self.__juft_sonlar[self.__min_son]
#
#         else:
#             raise StopIteration("Element qolmadi !!!")
#
# son1 = FilterItarable(9)
# son_items = son1.__iter__()
# print(son_items.__next__())
# print(son_items.__next__())
# print(son_items.__next__())
# print(son_items.__next__())

# ---------------------------------------------------------------------

# 6 misol

# royhat = [1,2,3,4,5,6]
#
# iterator_royhat = iter(royhat)
#
# countor = 0
#
# while True:
#     try:
#         countor += next(iterator_royhat)
#     except StopIteration:
#         break
#
# print(countor)



# ---------------------------------------------------------------------

# 7 misol


# royhat = ["1","2","3","4","5","6"]
# iterator_royhat = iter(royhat)
#
# qidirlyotgan_elemnt = "22"
# natija = "Yoq"
#
# for i in royhat:
#     if next(iterator_royhat) == qidirlyotgan_elemnt:
#         natija = "Bor"
# print(natija)



# ---------------------------------------------------------------------

# Generatorlarga oid

# ---------------------------------------------------------------------

# 1 misol


# def renge_gen(max_son):
#     countor = 0
#     while max_son > countor:
#         yield countor
#         countor += 1
#
# son = renge_gen(20)
# print(list(son))


# ---------------------------------------------------------------------

# 2 misol

# def matin_uzunligini_topish(matin:str):
#     royhat = matin.split(" ")
#     harflar = 0
#     for i in royhat:
#         harflar = 0
#         for j in i:
#             harflar +=1
#         yield f"{harflar}"
#
# text = matin_uzunligini_topish("Assalom alekum")
# print(list(text))

# ---------------------------------------------------------------------

# 3 misol

# def toq_son_gen(max_son):
#     for i in range(max_son):
#         if i %2==1:
#             yield i
# son = toq_son_gen(45)
# print(list(son))

# ---------------------------------------------------------------------

# 4 misol

# max_son = 20
# juft_son = (num for num in range(max_son) if num % 2 ==0)
# print(list(juft_son))

# ---------------------------------------------------------------------

# 5 misol


# def chaksiz_gen():
#     son = 0
#     while True:
#         son +=1
#         yield son
#
# son = chaksiz_gen()
#
# for i in range(20):
#     print(next(son))


# ---------------------------------------------------------------------

# 6 misol

# num = {i : i ** 2 for i in range(1,10)}
# print(num)


# ---------------------------------------------------------------------

# 7 misol


# def yigindi(max):
#     yigindi = 0
#     for i in range(max+1):
#         yigindi += i
#
#     yield yigindi
#
# son1 = yigindi(4)
# print(next(son1))

# ---------------------------------------------------------------------

# 8 misol


# listda = [1,5,-9,8,7,-4,-12,4,9,-5]
#
# def musbat_filter(royhat):
#     for i in royhat:
#         if i > 0 :
#             yield i
#
# son1 = musbat_filter(listda)
# print(list(son1))


# ---------------------------------------------------------------------

# 9 misol

# import random
#
# def tasadifiy_gen():
#     for i in range(4):
#         yield random.randint(1 , 100)
#
# son1 = tasadifiy_gen()
# print(list(son1))


# ---------------------------------------------------------------------

# 10 misol

# def tub_son(max_son):
#     bolinuvchilar_soni = 0
#     for i in range(1 , max_son+1):
#         bolinuvchilar_soni = 0
#         for j in range(1 , i+1):
#             if i % j == 0:
#                 bolinuvchilar_soni +=1
#         if bolinuvchilar_soni == 2:
#             yield i
# son1 = tub_son(20)
# print(list(son1))


# ---------------------------------------------------------------------

# 11 misol


# def teskari_matin(matin:str):
#     yield matin[::-1]
#
# matin1 = teskari_matin("Assalom")
# print(next(matin1))




# ---------------------------------------------------------------------

# 12 misol



# def kopaytma(max):
#     kopaytma = 1
#     for i in range(1 , max+1):
#         kopaytma *= i
#
#     yield kopaytma
#
# son1 = kopaytma(4)
# print(next(son1))








