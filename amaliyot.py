#1
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]


#2
#Ro'yxatning uzunligini konsolga chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]
print("davlatlar")

#3
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]
sorted(davlatlar)
print(davlatlar)


#4
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]
print(sorted(davlatlar , reverse=True))

#5
#Asl ro'yxatni qaytadan konsolga chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]
print("Asl ro'yxati:",davlatlar)

#6
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]
davlatlar.reverse()
print(davlatlar)

#7
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
davlatlar = ["Uzbekistan", "Russia", "Turkiya","Korea","Yaponiya"]
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#8
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200))
print(sonlar)

#9
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

print("sonlar_yig'indisi: {sum(sonlar)}")
