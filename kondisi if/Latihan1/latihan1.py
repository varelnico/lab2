a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukan bilangan ketiga: "))
d = int(input("Masukan bilangan keempat: "))

angkaTerbesar = a 
if b > angkaTerbesar:
    angkaTerbesar = b
    if c > angkaTerbesar:
        angkaTerbesar = c
        if d > angkaTerbesar:
            angkaTerbesar = d

            print("Angka", angkaTerbesar, "adalah yang terbesar dari keempat angka tersebut.")
