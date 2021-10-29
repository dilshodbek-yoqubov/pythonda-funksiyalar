
""" 1- Mavzu: Funksiyalarning ishlatilishi"""

# def salom_ber():
#     """Salom beruvchi funktsiya"""
#     print("Assalomu Alaykum")
# salom_ber()
#
#
# def salom_ber(ism):
#     """Ismni qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")
# salom_ber('dilshodbek')
#
#
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ismi va familiyasini jamlovchji funksiya"""
#     print(f"Salom, {ism.title()} {familiya.title()}")
# toliq_ism('dilshodbek', 'yoqubov')
#
#
# def yosh_hisobla(ism, yosh):
#     """Foydalanuvchi ismini oladi, yoshini hisoblaydi"""
#     print(f"Salom {ism.title()},siz {2021-yosh} yoshdasiz.")
# yosh_hisobla('dilshodbek',2002)
#
#
# def yosh_hisobla(tugilgan_yil, joriy_yil = 2021):
#     """Yosh hisoblaydigan funksiya"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(2002)
# yosh_hisobla(2001, 2021)


# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba = toliq_ism_yasa('dilshodbek', 'yoqubov')
# print(f"{talaba.title()} darsga keldi")


# def toliq_ism_yasa(ism, familiya, otasini_ismi = ""):
#     """To'liq ism qaytaradi"""
#     if otasini_ismi:
#         toliq_ism = f"{ism} {otasini_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('dilshod','yoqubov')
# talaba2 = toliq_ism_yasa('dilshod','yoqubov','ilyosbek og\'li')
# print(f"{talaba1}, {talaba2}")


""" 2 - Mavzu: Funksiyalaring qulayliklari"""


# def avto_info(kompaniya,model,rang,yili,narx=None):
#     """Avtolar haqida malumot qaytaradi"""
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rang,
#         'yili' : yili,
#         'narx' : narx
#     }
#     return avto
# avto1 = avto_info('GM','cobalt','ko\'k',2018,)
# avto2 = avto_info('GM','spark','oq',2016,5000)
# avtolar = [avto1, avto2]
# # print(avtolar)
#
# print("Online bozordagi avtomashinalar: ")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = 'Nomalum'
#     print(f"Modeli: {avto['model'].title()}, Rangi: {avto['rang'].title()}, Narxi: {avto['narx']}")

# def oraliq(min, max, qadam=None):
#     sonlar  = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#         if qadam:
#             sonlar.append(qadam)
#     return sonlar
# print(oraliq(0, 10, 2))
# print(oraliq(10, 21,))



# def avto_info(kompaniya,model,rang,yili,narx=None):
#     """Avtolar haqida malumot qaytaradi"""
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rang,
#         'yili' : yili,
#         'narx' : narx
#     }
#     return avto
# avtolar = []
# while True:
#     print("Salondagi mashinalar ro'yxatini shaklantiramiz: ")
#     kompaniya = input("Kompaniya: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     yili =input("Yili: ")
#     narx = input("Narxi: ")
#     avtolar.append(avto_info(kompaniya,model,rang,yili,narx))
#
#     jovob = input("Yana qo'shasizmi? (yes/no)")
#     if jovob != 'yes':
#         break
#
# print("\nSalonimizdagi avtomobillar: ")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = 'Nomalum'
#     print(f"{avto['rang'].title()} {avto['model'].title()},Yili {avto['yili']},Narxi {avto['narx']} ")


""" 3 - Mavzu:  *args, **kwargs """

# def summa(*sonlar): # istagancha argument qabul qiladi
#     """Kiritilgan sonlarni yiogindisini hisoblaydi"""
#     return sum(sonlar) # sum() royxat qabul qilib olib, yigindisini hisoblaydi
# print(summa(2, 4))
# print(summa(2, 4, 6, 8))
#
#
# def summa(x, y, *sonlar): # eng kamida 2 ta argument qabul qiladi
#     return x + y + sum(sonlar)
# print(summa(2, 8))
# print(summa(1, 3, 6, 2, 9))


# def avto_info(kompaniya, model, **malumotlar): # **malumotlar > lugat korinishda istagancha argument berihsh mumkin
#     """Avto haqidagi malumotytlarni lugat korinishida korsatadi"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# avto1 = avto_info('gm', 'cobalt', rang = 'oq', yili = 2018)
# avto2 = avto_info('gm', 'spark', narx = 4500, yili = 2016, rang = 'oq')
# print(avto1,'\n',avto2)
