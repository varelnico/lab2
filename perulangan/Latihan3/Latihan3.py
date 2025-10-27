jawab = 'ya'
hitung = 0
while jawab.lower() == 'ya':
    hitung += 1
    print("Perulangan ke-", hitung)
    jawab = input("Ulang lagi tidak? (ya/tidak): ")
print("Total perulangan:", hitung)
