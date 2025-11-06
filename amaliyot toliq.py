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

#10
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(sonlar)-min(sonlar))

#11
#Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))

#12
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[-230:250])

#13
#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["Palov","Manti","Norin","Shashlik"]

#14
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#15
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('Palov')
nonushta.remove('Manti')
nonushta.remove('Norin')
nonushta.remove('Shashlik')
nonushta.append('non va qaymoq')

#16
##Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(nonushta)
print(taomlar)

#17
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"