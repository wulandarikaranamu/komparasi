#latihan komparasi dan logika
#membuat kasus gabungan area dari rentang angka
#+++++++4-------8+++++++
inputUser = float(input("masukkan nilai yang kurang dari 4 atau lebih dari 8 :"))
kurangDari = (inputUser < 4)
print("kurang dari 4 =",kurangDari)

print("\n==========batas========")
lebihDari = (inputUser > 8)
print("\nlebih dari 7 =",lebihDari)

#cara menggabungkan program diatas menggunkan operator logika
isCorrect = kurangDari or lebihDari
print("angka yang anda masukkan adalah :",isCorrect)

print("\n==========batas========")
#-------4++++++++8---------
#kasus irisan
inputUser = float(input("\nmasukkan nilai yang lebih dari 4 dan kurang dari 8 :"))
lebih = (inputUser > 4 )
print("lebih dari 4 =",lebih)

print("\n============batas==========")
kurang = (inputUser < 8)
print("\nkurang dari 8 =",kurang)

#cara menggabungkan program diatas menggunkan operator logika
isCorrect = lebih and kurang
print("angka yang anda masukkan adalah :",isCorrect)